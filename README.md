# README #


nbahub is a simple command line application that (restfully) scrapes nba.com and basketball-reference.com for NBA statistics, and aggregates them in a format of your choosing. For now options are limited, but more will be coming soon!

### Setup ###

nbahub requires python 3.6, so first ensure that it is installed. You can download Python 3.6 [here](https://www.python.org/downloads/). It is recommended, but not required, that you use a [virtual environment](https://docs.python.org/3/tutorial/venv.html).

#### Setup with venv ####
1.) Create your virtual environment: 

    python3.6 -m venv nbahub-env

2.) Activate the environment:
- for Windows: `nbahub-env\Scripts\activate.bat`
- for Unix or MacOS: `source nbahub-env/bin/activate`

3.) Install nbahub: `pip install nbahub`

#### Setup without venv ####

1.) There's only one step: `pip3.6 install nbahub`


### Usage ###
Say, for example, you want to update all stats from 2016-17, get them in excel, and place the data in a directory named `nbahub_updates`:

```nbahub update_all --season 2016-17 --format excel --output nbahub_updates```

As of right now (version 0.1.2), `update_all` is the only command available, and you'll get all the statistics the program is capable of grabbing. More statistics will be added at some point, as well as the ability to select only a subset of those that are available.


### Contact ###
You can open an issue on this repository, send me an email (In my profile), or find me on Twitter (@JohnGriebel).