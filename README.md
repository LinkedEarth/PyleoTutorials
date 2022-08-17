[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/LinkedEarth/PyleoTutorials/HEAD)
[![PyPI version](https://badge.fury.io/py/pyleoclim.svg)](https://badge.fury.io/py/pyleoclim)
[![license](https://img.shields.io/github/license/linkedearth/PyleoTutorials.svg)]()

# PyleoTutorials: A Gentle Introduction to the Pyleoclim Package. 

A collection of science-driven tutorials for using the [Pyleoclim](https://github.com/LinkedEarth/Pyleoclim_util) Python package.

## Contents
The _notebooks_ folder contains [Jupyter Notebooks](https://jupyter.org) that illustrate the main classes of the [Pyleoclim user interface](https://pyleoclim-util.readthedocs.io/en/master/core/api.html), using data hosted either in the Cloud or in the _data_ directory.

The notebooks are organized in three levels:
- **Level 0**: basic tutorials to understand the main classes and their uses, requiring minimal knowledge of Python
- **Level 1**: more advanced tutorials involving customization and more knowledge of Python
- **Level 2**: tutorials involving more advanced data analysis techniques, requiring some knowledge to apply and interpret properly.  

## How to run these notebooks

### Local installation
Use the environment.yml file with conda to install the required packages within an anaconda or miniconda installation. https://pyleoclim-util.readthedocs.io/en/master/installation.html

`conda env create -f environment.yml`

### Using myBinder

myBinder allows you to run the notebooks is a no-install cloud container. This is the best solution is you just want to get you feet wet with the code. Use the MyBinder badge to launch. The notebooks will be automatically pulled into your workspace.

### Using the LinkedEarth JupyterHub

**Coming Soon (September 2022)**

If you have access to a decent internet connection and do not want to install Python and Pyleoclim on your machine, the best option is to run these notebooks on the [LinkedEarth JupyterHub](https://linkedearth.2i2c.cloud/). Please contact [LinkedEarth](mailto:linkedearth@gmail.com) to obtain an account. 

In this case, the notebook will not directly be pulled to the hub. You first need to download, clone or fork this repository onto your local machine. You can do so my clicking on the green 'code' button at the top (right above the list of files in the repository).

<img width="526" alt="image" src="https://user-images.githubusercontent.com/11758571/185023757-093f9765-857c-404a-9707-07f6715e8e06.png">
 
To learn more about cloning/forking, see [this post](https://www.theserverside.com/answer/Git-fork-vs-clone-Whats-the-difference). Downloading is just a one time action.

Once the notebooks are on your local machine, you can upload them to your private instance on the hub using [this tutorial](https://foundations.projectpythia.org/foundations/jupyterlab.html).
