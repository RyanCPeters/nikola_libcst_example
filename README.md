# This is just an example
This is an example of how to use the [libCST](https://github.com/Instagram/LibCST) to programmatically modify a [Nikola](https://github.com/getnikola/nikola) site's `conf.py` file according to the contents of a chosen theme's `conf.py.sample` file.

__*This example is mostly a proof of concept*__, and would require non-trivial evaluation to produce a more generalized solution for Nikola. Though, if properly leveraged it seems practical to conclude that a tool built on libCST could allow for greater compartmentalization of configuration files upon startup with a runtime config file generation script that can compose multiple files into the single conf.py file Nikola currently uses.

### Setup:

1. Using `git` clone this repo to your desire location and cd into it:
   * `git clone https://github.com/RyanCPeters/nikola_libcst_example.git`
   * `cd .\nikola_libcst_example\`
2. Get you a virtual environment manager... 
   * You can use either of the following, though I only have personal experience with Miniconda:
      * my further instructions might be specific to Miniconda, as I've never properly investigated `venv`
      * Anaconda's [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
      * python's [venv](https://docs.python.org/3/tutorial/venv.html)
3. Create a virtual environment and activate it:
   * In your `conda` prompt:
   ```sh
    # you may need to update conda first, but that's as simple as `conda update conda`
    (base) PS path/to/repo> conda create -n nikola_libcst_example python pip
    # conda's download and installation output ...
    (base) PS path/to/repo> conda activate nikola_libcst_example
    (nikola_libcst_example) PS path/to/repo> 
   ```
4. You should now be in the repo's root folder, with your virtual environment activated (so you can safely install project dependencies without messing up other projects.)
   * `python -m pip install -e .`
   * this will run `pip install` using the `setup.py` file found in the repo's root for the configuration details.

### Run the code:
You should look through the repo's folder structure. You'll find that the relevant source code is found inside the `/nikola_libcst_fix/` folder 