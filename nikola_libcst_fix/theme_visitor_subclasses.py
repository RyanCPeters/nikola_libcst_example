import libcst as cst
from typing import List, Tuple, Dict, Optional, Union


class ThemeCollector(cst.CSTVisitor):
    def __init__(self, theme_replacement_name):
        super().__init__()
        # stack for storing the canonical name of the current function, used for generating unique keys to each node.
        self.stack: List[Tuple[str, ...]] = []
        # replacement_targets will be the mapping of fields from a theme's conf.py.backup.sample file which need to be updated
        # in the site's conf.py.backup file.
        #   Note: initializing replacement_targets with an entry for the `THEME` variable just in case the theme's conf
        #         file forgets to include it.
        self.replacement_targets:Dict[Tuple[str, ...], cst.CSTNode] = {
            ("THEME",):cst.parse_statement(f"THEME = '{theme_replacement_name}'").body[0]
        }

    def visit_AnnAssign(self, node: "AnnAssign") \
            -> Optional[bool]:
        if hasattr(node.targets[0].target, "elements"):
            self.stack.append(",".join(element.value.value for element in node.targets[0].target.elements))
        else:
            self.stack.append(node.targets[0].target.value)
        key = tuple(self.stack)
        self.replacement_targets[key] = node

    def leave_AnnAssign(self, original_node: "AnnAssign")\
            -> None:
        self.stack.pop()

    def visit_Assign(self, node: "Assign") \
            -> Optional[bool]:
        if hasattr(node.targets[0].target, "elements"):
            self.stack.append(",".join(element.value.value for element in node.targets[0].target.elements))
        else:
            self.stack.append(node.targets[0].target.value)
        key = tuple(self.stack)
        self.replacement_targets[key] = node

    def leave_Assign(self, original_node: "AnnAssign")\
            -> None:
        self.stack.pop()

    def visit_FunctionDef(self, node: "FunctionDef")\
            -> Optional[bool]:
        self.stack.append(node.name.value)
        self.replacement_targets[tuple(self.stack)] = node
        return False  # we don't need to perform any actions on the contents of theme functions

    def leave_FunctionDef(self, original_node: "FunctionDef")\
            -> None:
        self.stack.pop()


class ThemeTransformer(cst.CSTTransformer):
    def __init__(self, replacement_targets: Dict[Tuple[str, ...], cst.CSTNode]):
        super().__init__()
        # stack for storing the canonical name of the current function, used for generating unique keys to each node.
        self.stack: List[Tuple[str, ...]] = []
        self.replacement_targets:Dict[Tuple[str, ...], cst.CSTNode] = replacement_targets
        self.all_keys = set(self.replacement_targets.keys())
        self.utlized_keys = set()

    def visit_AnnAssign(self, node: "AnnAssign") \
            -> Optional[bool]:
        if hasattr(node.targets[0].target, "elements"):
            self.stack.append(",".join(element.value.value for element in node.targets[0].target.elements))
        else:
            self.stack.append(node.targets[0].target.value)

    def leave_AnnAssign( self, original_node: "AnnAssign", updated_node: "AnnAssign") \
            -> Union["BaseSmallStatement", cst.RemovalSentinel]:
        key = tuple(self.stack)
        self.stack.pop()
        if key in self.replacement_targets:
            self.utlized_keys.add(key)
            return self.replacement_targets[key]
        return updated_node

    def visit_Assign(self, node: "Assign") \
            -> Optional[bool]:
        if hasattr(node.targets[0].target, "elements"):
            self.stack.append(",".join(element.value.value for element in node.targets[0].target.elements))
        else:
            self.stack.append(node.targets[0].target.value)

    def leave_Assign(self, original_node: "Assign", updated_node: "Assign") \
            -> Union["BaseSmallStatement", cst.RemovalSentinel]:
        key = tuple(self.stack)
        self.stack.pop()
        if key in self.replacement_targets:
            self.utlized_keys.add(key)
            return self.replacement_targets[key]
        return updated_node

    def visit_FunctionDef(self, node: cst.FunctionDef) \
            -> Optional[bool]:
        self.stack.append(node.name.value)
        return False  # we don't need to perform any actions on the contents of theme functions

    def leave_FunctionDef(self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef) \
            -> cst.CSTNode:
        key = tuple(self.stack)
        self.stack.pop()
        if key in self.replacement_targets:
            return self.replacement_targets[key]
        return updated_node
