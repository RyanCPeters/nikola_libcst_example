from nikola_libcst_fix.theme_config_adjustments import simple_demo,demo
import doit


def task_simple_demo():
    """Runs nikola_libcst_fix.theme_config_adjustments.simple_demo():"""

    return dict(actions=[simple_demo],verbosity=2)

task_simple_demo.__doc__ += f"""

    simple_demo::
    {simple_demo.__doc__}
    """

def task_demo_with_args():
    """Runs nikola_libcst_fix.theme_config_adjustments.demo(...):
    
    default path_to_custom_site will map to where the doit.run call was issued from.
    """
    theme_name_param = dict(name="name_of_theme", long="theme_name", short="t", default="canterville", type=str,
                            help="\nA string giving the name of the theme we should find the `conf.py.sample` file in.\n")
    path_to_site_param = dict(name="path_to_custom_site", long="site_path", short="p", type=str,
                              help="\nA string or pl.Path object that defines the path to a Nikola site's root folder;")
    reset_conf_param = dict(name="reset_conf", long="reset_conf", short="r", default=False, type=bool,
                            help="\nA bool specifying if we should reset the conf.py file to match it's saved backup"
                                 "\n(the backup is automatically generated and stored the first time this function runs)\n")
    path_to_site_param["default"] = doit.get_initial_workdir()
    path_to_site_param["help"] += "\ndefaults to doit.get_initial_workdir()\n"
    return dict(actions=[demo],
                params=[theme_name_param,
                        path_to_site_param,
                        reset_conf_param
                        ],
                verbosity=2)


task_demo_with_args.__doc__ += f"""

    demo::
    {demo.__doc__}
    """


def print_demo_help():
    s = []
    s.append(f"demo_help:\n{'-':-<80}\n{'-':-<80}\n")
    template = f"{'+':+<120}\n{{}}:\n{'=':=<120}\n{{}}\n{'-':-<120}\n"
    s.append(template.format("simple_demo", task_simple_demo.__doc__))
    s.append(template.format("demo_with_args", task_demo_with_args.__doc__))
    s = "\n".join(s)
    print(s)


def task_demo_help_docs():
    """prints the full doc strings for each of the demo tasks provided in this file"""

    return dict(actions=[print_demo_help],verbosity=2)


def print_examples():
    s = []
    s.append(f"{'-':-<120}")
    s.append("The basic execution sequence for a call to demo_with_args task looks something like this:"
             "\n\ncall nikola_libcst_fix.theme_config_adjustments.demo function\n"
             "\n  1. temporarily change working directory to site_path parameter's value if that path exists, else raise FileNotFoundError"
             "\n  2. check that we can find the conf.py file in your_site_root2, else raise FileNotFoundError"
             "\n  3. check if the the tasks default theme target is already present in the site's `themes` folder,"
             "\n     * if theme check fails, we attempt to call os.system(f'nikola theme -i {theme_name}')"
             "\n       - reraising any errors that may occur"
             "\n  4. call the nikola_libcst_fix.theme_config_adjustments.theme_update function"
             "\n     * passing the resolved paths to conf.py and conf.py.sample"
             )
    s.append(f"{'*':*<120}")
    s.append(
        "\nNote: <things between chevrons> are just placeholders, replace them (including the chevrons) in your actual calls.\n")

    s.append("Calling the demo_with_args task from the same directory as this dodo.py file:")
    s.append("  doit demo_with_args -t <some theme name> -p <path/to/valid/nikola/site root>"
             "\n  doit demo_with_args --theme_name <some theme name> --site_path <path/to/valid/nikola/site root>\n")

    s.append("Calling the demo_with_args task from a Nikola site's root folder:")
    s.append(
        "  doit -f <relative/or/absolute/path/to/nikola_libcst_example>/dodo.py demo_with_args -t <some theme name>"
        "\n  doit -f <relative/or/absolute/path/to/nikola_libcst_example>/dodo.py demo_with_args --theme_name <some theme name>\n")
    s.append(f"{'+':+<120}")
    s.append("\n\n\tLiteral call examples for this repo:\n")

    s.append("calling demo_with_args from repo root:\n")
    s.append("\tdoit demo_with_args -t zen -p ./nikola_libcst_fix/some_site_structure")
    s.append("\tdoit demo_with_args -t canterville -p ./nikola_libcst_fix/some_site_structure\n")

    s.append("\ncalling demo_with_args from /nikola_libcst_example/nikola_libcst_fix/some_site_structure folder:\n")
    s.append("\tdoit -f ../../dodo.py demo_with_args -t zen")
    s.append("\tdoit -f ../../dodo.py demo_with_args -t canterville\n")
    s.append(f"{'^':^<120}\n")
    s = "\n".join(s)
    print(s)


def task_demo_call_examples():
    """prints several examples of how to make doit calls to the demo_with_args task under different contexts"""
    return dict(actions=[print_examples],verbosity=2)
