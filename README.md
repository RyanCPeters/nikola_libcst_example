This is just an example
===
This is an example of how to use the [libCST](https://github.com/Instagram/LibCST) to programmatically modify a [Nikola](https://github.com/getnikola/nikola) site's `conf.py` file according to the contents of a chosen theme's `conf.py.sample` file.

__*This example is mostly a proof of concept*__, and would likely require non-trivial evaluation to produce a more generalized solution for all possible use cases in Nikola. Though, if properly leveraged it seems practical to conclude that a tool built on libCST could allow for greater compartmentalization of configuration files upon startup with a runtime config file generation script that can compose multiple files into the single conf.py file Nikola currently uses.

Setup:
---
1. Using `git` clone this repo to your desire location and cd into it:
   ```shell script
   # in your prefered terminal, I'm using windows powershell
   PS /some/path> git clone https://github.com/RyanCPeters/nikola_libcst_example.git
   # bunch o'download and hash checking output ...
   PS /some/path> cd nikola_libcst_example
   PS /some/path/nikola_libcst_example>
   ```
2. Get you a virtual environment manager... 
   * You can use either of the following, though I only have personal experience with Miniconda:
      * Anaconda's [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
      * python's [venv](https://docs.python.org/3/tutorial/venv.html)
      * my further instructions might be specific to Miniconda, as I've yet to properly investigated `venv`
3. Create a virtual environment and activate it:
   * In your `conda` prompt:
      * `conda create -n nikola_libcst_example python pip`
      * `conda activate nikola_libcst_example`
   * you should see something like this:
   ```shell script
    # you may need to update conda first, but that's as simple as `conda update conda`
    (base) PS /some/path/nikola_libcst_example> conda create -n nikola_libcst_example python pip
    # bunch o'download and installation output ...
    (base) PS /some/path/nikola_libcst_example> conda activate nikola_libcst_example
    (nikola_libcst_example) PS /some/path/nikola_libcst_example>
   ```
4. You should now be in the repo's root folder, with your virtual environment activated (so you can safely install project dependencies without messing up other projects.) 
   * `python -m pip install -e .`
      * You should see output similar to this:
      ```shell script
      (nikola_libcst_example) PS /some/path/nikola_libcst_example> python -m pip install -e .
      # bunch o'requirement stuff
      # ...
      Successfully installed Programatic-conf-manip-example
      (nikola_libcst_example) PS /some/path/nikola_libcst_example>
      ```
     * if your output doesn't end with `Successfully installed Programatic-conf-manip-example` 
        * you can try the following:
        ```shell script
        # first we update conda on the base environment
        (nikola_libcst_example) PS /some/path/nikola_libcst_example>conda update -n base conda
        # if there are no updates, you can bail on the following steps; though I don't have any alternate ideas for a fix
        # otherwise, make sure the base python package is up to date, and then the rest of the base environment. 
        (nikola_libcst_example) PS /some/path/nikola_libcst_example>conda update -n base python
        (nikola_libcst_example) PS /some/path/nikola_libcst_example>conda update -n base --all
        # now we update local python and pip packages for the demo environment
        (nikola_libcst_example) PS /some/path/nikola_libcst_example>conda update python
        (nikola_libcst_example) PS /some/path/nikola_libcst_example>conda update pip
        # and finally we rerun the setup script
        (nikola_libcst_example) PS /some/path/nikola_libcst_example>python -m pip install -e .       
        ```
        * 
   * this will run `pip install` using the `setup.py` file found in the repo's root for the configuration details.
   * This will create 2 console entry points for the demo, [`programmatic_demo_simple`](#entry-1) and [`programmatic_demo`](#entry-2) (descriptions bellow), along with ensuring we have all package dependencies.
   

Inspecting the code
---
You'll see that the relevant source code is found inside the `/nikola_libcst_fix/` folder.

This example implements LibCST's visitor/transformer pattern; where the custom [visitor](https://libcst.readthedocs.io/en/latest/tutorial.html) subclasses for the implementation are defined in the `theme_visitor_subclasses.py` file.

The code for applying those subclasses can be found in the [`theme_config_adjustments.py`] file.

###### Note: 
Regarding the conf file names and their relative directory paths.
`conf.py` and `conf.py.sample` should be the same as one would find in a normal Nikola project using one of the hosted themes.

###### Also Note:
The `conf.py` file is a copy of that produced by the terminal command:
* `nikola init --demo some_site_structure`
* Note that I've only included the `conf.py` file for this example. 

And the theme's `conf.py.sample` file is copied from the Nikola hosted zen theme acquired with the following command:
* `nikola theme -i zen`

Run the code
---
Once you are ready to see the example's output, (from the command terminal) you can call one of the following terminal entry points:
* <a name="entry-1">`$ programmatic_demo_simple`</a>
   * This will run the hard coded demo that relies on relative pathing to the example provided with this repo in order to find the example conf.py and conf.py.sample files.
   * This is a minimal working code example that demonstrates programmatically updating a site's conf.py file according to a theme's conf.py.sample file.
* <a name="entry-2">`$ programmatic_demo`</a>
   * This is an alternate version of the demo that allows the caller to specify details for where to set the current working dir, theme name and if a conf.py file should be reverted to pre-theme state. 
   * You can call `programmatic_demo -h` to get a printout of commands and how to use them
   * will raise `FileNotFoundException` if given an invalid path or if the `conf.py` doesn't exist at the given root directory.
* Alternatively, you can use `doit` from the root of this repo instead of calling the terminal entry handles.
   * the following example calls need to be made in a terminal at the root folder of this repo.
   * `doit demo_help_docs` will list of the demo tasks available to you, along with a detailed description.
   * `doit demo_call_examples` will display examples of calling the demo tasks from various contexts.


Checking against actual site structure
---
If you would like to run this example on a fully defined Nikola site, the easiest approach would be to copy your own example site folder into `/nikola_libcst_example` (the root folder for this repo) then call `programmatic_demo -t <your preferred theme>` 
