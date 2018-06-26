# Unfolding HATS 2018

Unfolding Hands-on Advanced Tutorial Session at the LPC

## Introduction

This is a set of tutorials for the CMS Unfolding Hands-on Advanced Tutorial Session (HATS). 
They are intended to show you how to apply unfolding to your CMS analysis.
We will introduce unfolding and three different methods for applying it.


Requirements:

- ROOT 6.10 : [TUnfold 17.6](http://www.desy.de/~sschmitt/tunfold.html)
- [PyMC3](http://docs.pymc.io/index.html)
- [PyFBU](https://pypi.org/project/fbu/)


## Overview

For each topic, there are different notebooks that introduce the different aspects of unfolding.
Each notebook provides an introduction into a new task that you will need to consider in your analysis.
At the end, the users are expected to apply this information to real CMS data.

0. [`0-setup-libraries.ipynb`](0-setup-libraries.ipynb): Setting up the environment.  
There are two environments to setup, one for TUnfold (requires ROOT accessed from CMSSW) and another for FBU (requires extra python libraries inconsistent with CMSSW).

#### TUnfold
- [`0-simple.ipynb`](tunfold/0-setup-libraries.ipynb): Simple introduction to TUnfold
- [`1-backgrounds.ipynb`](tunfold/1-backgrounds.ipynb): Unfolding with non-negligible backgrounds
- [`2-systematics.ipynb`](tunfold/2-systematics.ipynb): Unfolding with backgrounds and systematic uncertainties

Additionally, we have added the example scripts from TUnfold.
These can be viewed in the Jupyter notebooks:
- [`example1.ipynb`](tunfold/example1.ipynb): Executes the script `testUnfold1.C`
- [`example2.ipynb`](tunfold/example2.ipynb): Executes the script `testUnfold2.C`
- [`example3.ipynb`](tunfold/example3.ipynb): Executes the script `testUnfold3.C`
- [`example4.ipynb`](tunfold/example4.ipynb): Executes the script `testUnfold4.C`

#### Fully Bayesian Unfolding
- [`0-simple.ipynb`](fbu_exercises/0-setup-libraries.ipynb): Simple introduction to FBU
- [`1-backgrounds.ipynb`](fbu_exercises/1-backgrounds.ipynb): Unfolding with non-negligible backgrounds
- [`2-systematics.ipynb`](fbu_exercises/2-systematics.ipynb): Unfolding with backgrounds and systematic uncertainties
- [`3-regularization.ipynb`](fbu_exercises/3-regularization.ipynb): Unfolding with backgrounds, systematics, and regularization.  
*No regularization with FBU will be done today due to issue with PyFBU and PyMC3 implementation*


## Getting Started

Refer to this [Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/HATSatLPCSetup2018) page for details about the setup.  
The following describes a brief outline for getting setup.

### Initial Setup

We will be using the Vanderbilt JupyterHub. Point your browser to:

[https://jupyter.accre.vanderbilt.edu/](https://jupyter.accre.vanderbilt.edu/)

If this is the first time using this JupyterHub, you should see:

<p align="center">
  <img src="docs/vanderbilt.png" width="500"/>
</p>

Click the "Sign in with CILogon" button. 
On the following page, select CERN as your identity provider and click the "Log On" button. 
Then, enter your CERN credentials or use your CERN grid certificate to autheticate.

Now you should see the JupyterHub home directory. Click on "New" then "Terminal" in the top right to launch a new terminal.

<p align="center">
  <img src="docs/new_terminal.png" width="200"/>
</p>

To download the tutorials, type
```
git clone https://github.com/demarley/unfolding-hats.git -b v2018
```
Now, in your directory tab, there should be a new directory called `unfolding-hats`. 
All of the tutorials and exercises are in there.

### Post-Initial Setup

After the initial setup of this project, you may want to revisit the exercises.
When you reconnect to the Vanderbilt cluster, you simply need to open a new notebook.

At the end of each notebook, please select:
```
File
Close and Halt
```
To exit the notebook properly.
Additionally, at the end of your session, please stop your server:
```
Control Panel
Stop my Server
```


## Links

- [Indico](https://indico.cern.ch/event/726642/) page with links and other resources
- [Mattermost channel](https://mattermost.web.cern.ch/cms-exp/channels/hatslpc-2018) for live support
- [Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/HATSatLPC) with relevant information

## Questions, Comments, or Concerns
Contact the authors or submit an issue/PR

README outline borrowed from [ML-HATS](https://github.com/FNALLPC/machine-learning-hats/blob/master/README.md)
