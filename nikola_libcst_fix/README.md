# This is just an example
This is an example of how to use the [libCST](https://github.com/Instagram/LibCST) to programmatically modify a [Nikola](https://github.com/getnikola/nikola) site's `conf.py` file according to the contents of a chosen theme's `conf.py.sample` file.

__*This example is mostly a proof of concept*__, and would require non-trivial evaluation to produce a more generalized solution for Nikola. Though, if properly leveraged it seems practical to conclude that a tool built on libCST could allow for greater compartmentalization of configuration files upon startup with a runtime config file generation script that can compose multiple files into the single conf.py file Nikola currently uses.

### Setup:

1. Using `git` clone this repo to your desire location and cd into it:
   * `git clone https://`
2. Get you a virtual environment manager... 
   * You can use either of the following, though I only have personal experience with Miniconda, so my further instructions might be specific to that tool (I've never properly investigated `venv`):
      * Anaconda's [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
      * python's [venv](https://docs.python.org/3/tutorial/venv.html)
3. Create a virtual environment:
   * In a conda prompt:
   ```bash
   # you may need to update conda first, but that's as simple as `conda update conda`
   >conda create -n your_env_name python pip
   # ... download and installation output
   >