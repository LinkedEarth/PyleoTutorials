[![PyPI version](https://badge.fury.io/py/pyleoclim.svg)](https://badge.fury.io/py/pyleoclim)
[![license](https://img.shields.io/github/license/linkedearth/PyleoTutorials.svg)]()
[![NSF-2126510](https://img.shields.io/badge/NSF-2126510-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=2126510)
[![DOI](https://zenodo.org/badge/509538632.svg)](https://zenodo.org/badge/latestdoi/509538632)

# PyleoTutorials: A Gentle Introduction to the Pyleoclim Package.

A collection of science-driven tutorials for using the [Pyleoclim](https://github.com/LinkedEarth/Pyleoclim_util) Python package.

## Contents

The notebooks are organized in three levels:
- **Getting Started**: basic tutorials to understand the main classes and their uses, requiring minimal knowledge of Python
- **Manipulating Data and Graphics**: more advanced tutorials involving customization and more knowledge of Python
- **Data Analysis with Pyleoclim**: tutorials involving more advanced data analysis techniques, requiring some domain knowledge to apply and interpret properly.  

```{tableofcontents}
```

## How to run these notebooks

### Using myBinder

[myBinder](https://mybinder.org) allows you to run the notebooks in a no-install cloud container. This is the best solution if you just want to get you feet wet with the code. The top right corner of each tutorial has a spaceship icon that will launch a [myBinder](https://mybinder.org) instance of each notebook. Beware: it takes a few minutes for the BinderHub to be spun up the first time around. After repeated uses (not just by you) it becomes much faster, but the first time you launch might need to coincide with a coffee break, a run around the nearest park, or catching up on the literature.

### Local installation
You may also download each notebook and run them with a local install. To do so, the best is to use the `environment.yml` file with `conda` to install the required packages within an [anaconda](https://anaconda.org) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installation. That is, open a terminal, navigate to a folder containing `environment.yml` , then run the command :

`conda env create -f environment.yml`

This will install all the required packages and their dependencies. It may take a few minutes the first time, but after that you will have the power of Pyleoclim at your local disposal.

If you are new to conda, just know that it is an environment manager for Python. What is an environment, you may ask? Think of it as a piece on your computer where all the Python libraries that you need for a specific application live in perfect harmony. To access this paradise, you need to activate the environment. If you used the `environment.yml` file:

`conda activate pyleo`

### Using the LinkedEarth JupyterHub


If you have access to a decent internet connection and do not want to install Python and Pyleoclim on your machine, you can also run these (and your own) notebooks on the [LinkedEarth JupyterHub](http://linked.earth/research_hub.html). To do so, please contact [LinkedEarth](mailto:linkedearth@gmail.com) to obtain an account, which may take 1-2 business days to review. Use of the LinkedEarth Hub implies that you subscribe to the LinkedEarth [code of conduct](https://github.com/LinkedEarth/governance/blob/main/code-of-conduct.md) which pretty much amounts to being a decent human being.  This is a good solution if you intend on using Pyleoclim in your own work, particularly for [paleoclimate data-model comparisons](https://medium.com/cyberpaleo/announcing-the-next-linkedearth-chapter-paleocube-790778b6ffb0).

If you choose this route, know that the PyleoTutorials notebooks will not be directly pulled to the hub (unlike the myBinder solution). You will first need to download, clone or fork this repository onto your local machine. You can do so by clicking on the green 'code' button at the top of the [repository page](https://github.com/LinkedEarth/PyleoTutorials) (right above the list of files):

<img width="526" alt="image" src="https://user-images.githubusercontent.com/11758571/185023757-093f9765-857c-404a-9707-07f6715e8e06.png">

To learn more about cloning/forking, see [this post](https://www.theserverside.com/answer/Git-fork-vs-clone-Whats-the-difference). Downloading is just a one time action.

Once the notebooks and data are on your local machine, you can upload them to your private instance on the hub using [this tutorial](https://foundations.projectpythia.org/foundations/jupyterlab.html).

Please note that the notebooks use specific paths that you will either need to correct in the cells or reproduce on the hub (i.e., the notebooks and data folders).

Whichever path you choose, happy Pyleocliming, and please consider joining our user community on [Discourse](https://discourse.linked.earth). It is the best place to provide feedback on any of this, and make requests for new tutorials.

## Acknowledgements
This work was supported by NSF Grant [ICER 2126510](https://nsf.gov/awardsearch/showAward?AWD_ID=2126510&HistoricalAwards=false).
