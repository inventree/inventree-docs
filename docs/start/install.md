---
title: Install InvenTree
layout: page
---

## Introduction

The InvenTree server application communicates with a backend database, and serves data to the user(s) via a web framework and an API. Before users can interact with the InvenTree system, the server must be installed and properly configured, and then the server process must be started (at a network location which is accessible to the users).

### Supported Databases

InvenTree can be used by any database backend which is supported by the [Django framework](https://docs.djangoproject.com/en/3.0/ref/databases/):

* SQLite
* PostgreSQL
* MariaDB
* MySQL
* Oracle

Database selection should be determined by your particular installation requirements. By default, InvenTree uses SQLite which provides a simple file-based database that allows a quick setup for development and testing.

### Serving Data

Once a database is setup, you need a way of accessing the data. InvenTree provides a "server" application out of the box, but this may not scale particularly well with multiple users. Instead, InvenTree can be served using a webserver such as [Gunicorn](https://gunicorn.org/). For more information see the [deployment documentation](start/deploy).

## Setup

To install a complete *development* environment for InvenTree, follow the steps presented below. A production environment will require further work as per the particular application requirements. 

!!! warning "Windows"
    If you are using the Windows operating system, it is recommended that you use the <a href='https://docs.microsoft.com/en-us/windows/wsl/install-win10'>WSL (Windows Subsystem for Linux) framework</a>

### Requirements

To install InvenTree you will need python3 (>3.6) installed, as well as PIP (the Python package manager).

Install these required programs (e.g. using apt or similar) before running the setup scripts.

For example:

```
sudo apt-get update
sudo apt-get install python3 python3-dev python3-pip
```

!!! warning "Sudo"
    `apt-get` commands will (most likely) be required to run under sudo. Take care not to run the installation scripts under sudo, as this may alter the system python path and cause the InvenTree installation to not work correctly

### Python Virtual Environment

Installing the required Python packages inside a virtual environment allows a local install separate to the system-wide Python installation. While not strictly necessary, using a virtual environment is highly recommended as it prevents conflicts between the different Python installations.

You can read more about Python virtual environments [here](https://docs.python.org/3/tutorial/venv.html).

To configure Inventree inside a virtual environment, ``cd`` into the inventree base directory and run the following commands:

```
sudo apt-get install python3-venv
python3 -m venv inventree-env
source inventree-env/bin/activate
```

This will place the current shell session inside a virtual environment - the terminal should display the ``(inventree-env)`` prefix.

!!! warning "Activate virtual environment"
    Remember to activate the virtual environment when starting each shell session, before running Inventree commands. This will ensure that the correct environment is being used.

### Invoke

InvenTree setup is performed using the [invoke](https://www.pyinvoke.org/) Python build tool. Various useful scripts are defined in the `tasks.py` file.

Install invoke as follows:

```
pip3 install invoke
```

To display a list of the available configuration scripts, run the following command:

```
invoke --list
```

## Download Source Code

Download the InvenTree source code to a local directory. It is recommended to perform this step using git, as this allows the InvenTree installation to be easily updated to the latest version.

```
git clone https://github.com/inventree/inventree/
```

Alternatively, the source can be downloaded as a [.zip archive](https://github.com/inventree/InvenTree/archive/master.zip).

Once the source is downloaded, cd into the source directory:

```
cd /path/to/inventree/
```

*(substitute /path/to/inventree/ with the directory where you have downloaded the source code)*.

## Installation

Now that the source code is downloaded (and optionally you have configured a Python virtual environment), the Python packages required to run InvenTree can be installed. InvenTree is a Python/Django application and relies on the pip package manager. All packages required to develop and test InvenTree are installed via pip. Package requirements can be found in ``requirements.txt``.


To setup the InvenTree environment, run the following commands (from the InvenTree source directory):

```
invoke install
```

This installs all required Python packages using pip package manager. It also creates a (default) database configuration file which needs to be edited to meet user needs before proceeding (see next step below).

Additionally, this step creates a *SECRET_KEY* file which is used for the django authentication framework. 

!!! warning "Keep it secret, keep it safe"
    The SECRET_KEY file should never be shared or made public.

### Database Configuration

Once the required packages are installed, the database configuration must be adjusted to suit your particular needs. InvenTree provides a simple default setup which should work *out of the box* for testing and debug purposes.

As part of the previous *install* step, a configuration file (**config.yaml**) is created. The configuration file provides administrators control over various setup options without digging into the Django *settings.py* script. The default setup uses a local sqlite database with *DEBUG* mode enabled.

For further information on installation configuration, refer to the [Configuration](start/config) section.

!!! warning "Configure Database"
    Ensure database settings are correctly configured in `config.yaml` before proceeding to the next step!

### Initialize Database

Once install settings are correctly configured (in *config.yaml*) run the initial setup script:

```
invoke migrate
```

This performs the initial database migrations, creating the required tables, etc.

The database should now be installed!

### Create Admin Account

Create an initial superuser (administrator) account for the InvenTree instance:

```
invoke superuser
```

### Run Development Server

The InvenTree database is now setup and ready to run. A simple development server can be launched from the command line. 

To launch the development server, run the following commands:

```
invoke server
```

For more server options, run:

```
invoke server -h
```

This will launch the InvenTree web interface at `http://127.0.0.1:8000`. For other options refer to the [django docs](https://docs.djangoproject.com/en/2.2/ref/django-admin/)

### Run Production Server

For a production install, refer to [deployment instructions](start/deploy).
