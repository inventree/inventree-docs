---
title: Deploy InvenTree
---

## Deploying InvenTree

The development server provided by the Django ecosystem may be fine for a testing environment or small contained setups. However special consideration must be given when deploying InvenTree in a real-world environment.

Django apps provide multiple deployment methods - see the [Django documentation](https://docs.djangoproject.com/en/2.2/howto/deployment/).

There are also numerous online tutorials describing how to deploy a Django application either locally or on an online platform.

The following instructions provide a reasonably performant server, using [gunicorn](https://gunicorn.org/) as a webserver, and [supervisor](http://supervisord.org/) as a process manager.
    

## Install System Packages

Install required system packages (as superuser).

First, install required system packages as per the [OS requirements](../intro#os-requirements).

Then, install the supervisor process manager:

```
sudo apt-get install supervisor
```

Next, install the system packages required for your particular database:

### MySQL

```
sudo apt-get install mysql-server libmysqlclient-dev
```

### Postgresql

```
sudo apt-get install postgresql postgresql-contrib libpq-dev
```

### Initial Setup

### Create InvenTree User

It is highly recommended that the InvenTree server is not run under root. Create a user account from which we will run the server:

```
sudo useradd --create-home inventree
```

InvenTree source code, log files, etc will be located under the `/home/inventree/` directory.

Switch to the `inventree` user so commands are performed in the correct context:

```
sudo su inventree
```

### Download Source Code

Download InvenTree source code, into the `./src` directory:

```
cd /home/inventree
git clone https://github.com/inventree/inventree src
```

### Create Virtual Environment

Create a python virtual environment for installting required Python packages and binaries:

```
python3 -m venv env
source ./env/bin/activate
```

The shell prompt should now display the `(env)` prefix.

### Create Required Directories

```
mkdir log static media backup
```

This step creates directories required by InvenTree:

* **log** - Store InvenTree log files
* **static** - Location of static files for the web server
* **media** - Location of uploaded media files
* **backup** - Location of database backup files

## Install InvenTree Packages

The Python packages required by the InvenTree server must be installed into the virtual environment. 

Run the `invoke install` command (from within the src directory):

```
cd src
invoke install
```

This installs all required Python packages using pip package manager. It also creates a (default) database configuration file which needs to be edited to meet user needs before proceeding (see next step below).

Additionally, this step creates a *SECRET_KEY* file which is used for the django authentication framework. 

!!! warning "Keep it secret, keep it safe"
    The SECRET_KEY file should never be shared or made public.

You will also need to install the python packages required for your particular database backend:

### MySQL

```
pip3 install mysqlclient
```

### Postgresql

```
pip3 install psycopg2
```

## Configure InvenTree Options

Once the required software packages are installed, the database and server options must be configured.

Edit the configuration file at  `/home/inventree/src/InvenTree/config.yaml`.

!!! info "Config Guidelines"
    Refer to the [configuration guidelines](../config) for full details.

!!! warning "Configure Database"
    Ensure database settings are correctly configured in `config.yaml` before proceeding to the next step!

# Development Server

The InvenTree development server is useful for testing and configuration - and it may be wholly sufficient for a small-scale installation.

#### Running on a Local Machine

To run the development server on a local machine, run the command:

```
inv server -a 127.0.0.1:8000
```

Serving on the address `127.0.0.1` means that InvenTree will only be available *on that computer*. The server will be accessible from a web browser on the same computer, but not from any other computers on the local network.

#### Running on a Local Network

To enable access to the InvenTree server from other computers on a local network, you need to know the IP of the computer running the server. For example, if the server IP address is `192.168.120.1`:

```
inv server -a 192.168.120.1:8000
```

!!! warning "Not For Production"
    It should be noted that the *development server* provided with django / InvenTree is probably not suitable for your production environment. Instead, use a proper web-server (such as Gunicorn, below).

## Gunicorn

Following is a simple tutorial on serving InvenTree using [Gunicorn](https://gunicorn.org/). Gunicorn is a Python WSGI server which provides a multi-worker server which is well suited to handling multiple simultaneous requests. Gunicorn is a solid choice for a production server which is easy to configure and performs well in a multi-user environment.

### Install Gunicorn

Gunicorn can be installed using PIP:

```
pip3 install gunicorn
```

!!! warning "Python Environment"
    Ensure that gunicorn is installed within the same python environment context as the InvenTree install - otherwise gunicorn will not be able to import the correct python modules.

### Configure Static Directories

Directories for storing *media* files and *static* files should be specified in the ``config.yaml`` configuration file. These directories are the ``MEDIA_ROOT`` and ``STATIC_ROOT`` paths required by the Django app. Ensure that both of these directories are correctly configured for your setup.

### Collect Static Files

The required static files must be collected into the specified ``STATIC_ROOT`` directory:

```
inv static
```

This command collects all of the required static files (including script and css files) into the specified directory ready to be served.

### Configure Gunicorn

The Gunicorn server can be configured with a simple configuration file (e.g. python script). An example configuration file is provided in ``InvenTree/gunicorn.conf.py``

``` python
{% include 'gunicorn.conf.py' %}
```

This file can be used to configure the Gunicorn server to match particular requirements.

### Run Gunicorn

```
cd InvenTree
gunicorn -c gunicorn.conf.py InvenTree.wsgi
```
