# Elementary Particle Expirement Tutorials  

## Git Installation

To install git, go to [this website](https://git-scm.com/downloads) and download the installer for your operating system. If you do not already have a bash shell installed, make sure to also choose that option for install as git is a terminal application.

On Windows, make sure you configure the terminal emulator to use Windows' default console window. This will make it easier for you to access your computer's files and it is a lot nicer to look at.

On Mac, if you get a warning saying the .pkg file can’t be opened because it is from an unidentified developer, go to your System Preferences -> Security and Privacy and click on "open anyway." Follow the rest of the installer instructions to finish installing git.

## Anaconda Installation
To install anaconda, first go to [this website](https://www.anaconda.com/distribution/), and download the installer for Python 3. Once downloaded, follow the install wizard. The default settings are usually good choices. Make sure to choose Anaconda's python kernel as default, as it makes using the different frameworks and plugins much easier.

On Windows, make sure to select the option "Add Anaconda to my PATH environment variable". There will be red text saying it is not recommended, but you will not be able to access the Anaconda package from your bash terminal with out this option checked.

If you already have pip and Python 3 installed, you can run ```pip3 install anaconda``` in bash to get Anaconda.

## After installation
Once you have successfully installed git and anaconda, create a github account and sign in. You can download the repository by clicking on the green "Clone or Download" button and copy the link next to "Clone with HTTPS". Open up git bash, and type ```git clone [The web address here]```. This will download the repository to your local machine at your home directory. Then, open jupyter notebook either by the Anaconda Navigator or by going to git bash and typing ```jupyter notebook```.
