---
title: Deploy InvenTree
---

## Initial Setup

### Install System Packages

Install required system packages (as superuser).

First, install required system packages as per the [OS requirements](../intro#os-requirements).

Next, install the system packages [required for your particular database](../intro#database-requirements).

### Create InvenTree User

!!! warning "Running as Root"
    It is highly recommended that the InvenTree server is not run under root. The deployment instructions assume that InvenTree is installed and run from a different user account.
    
Create a user account from which we will run the server:

```
sudo useradd --create-home inventree
```

InvenTree source code, log files, etc will be located under the `/home/inventree/` directory.

Switch to the `inventree` user so commands are performed in the correct context:

```
sudo su inventree
```

### Create Required Directories

```
cd /home/inventree
mkdir log static media backup
```

This step creates directories required by InvenTree:

* **log** - Store InvenTree log files
* **static** - Location of static files for the web server
* **media** - Location of uploaded media files
* **backup** - Location of database backup files

### Download Source Code

Download InvenTree source code, into the `./src` directory:

```
cd /home/inventree
git clone https://github.com/inventree/inventree src
```

### Create Virtual Environment

Create a python virtual environment for installing required Python packages and binaries:

```
python3 -m venv env
source ./env/bin/activate
```

The shell prompt should now display the `(env)` prefix.

### Install InvenTree Packages

The Python packages required by the InvenTree server must be installed into the virtual environment. 

Run the `invoke install` command (from within the src directory):

```
(env) cd src
(env) invoke install
```

This installs all required Python packages using pip package manager. It also creates a (default) database configuration file which needs to be edited to meet user needs before proceeding (see next step below).


## Create Database

As part of the initial setup, an empty database needs to be created. Follow the instructions below particular to your database engine of choice:

### SQLite

SQLite uses a simple portable database file which is easy to use for debug and testing purposes.

Install required packages as follows:

```
sudo apt-get install sqlite3
```

A `.sqlite3` database file will be automatically created, at the location specified in the configuration options. No further steps necessary.

### PostgreSQL

Install required system packages:

```
sudo apt-get install postgresql postgresql-contrib libpq-dev
```

The PostgreSQL python binding must also be installed (into your virtual environment):

```
(env) pip3 install psycopg2 pgcli
```

Assuming the postgresql server is installed and running, switch to the `postgres` user and create a new database:

```
sudo su - postgres
```

You should now be in a shell session for the `postgres` user. Login to the database server as follows:

```
psql
```

Create a new database:

```
CREATE DATABASE inventree;
```

*Note: The name of the database will be required in the configuration section*

Create a user account associated with the new database.

```
CREATE USER inventreeuser WITH PASSWORD "password";
```

*Note: Choose different username and password values, and remember them for the configuration section*.

Set the following database configuration options:

```
ALTER ROLE inventreeuser SET client_encoding TO 'utf8';
ALTER ROLE inventreeuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE inventreeuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE inventree TO inventreeuser;
```

Exit the postgresql shell:

```
\q
```

Exit out of the `postgres` user's shell:

```
exit
```

### MySQL / MariaDB

To run InvenTree with the MySQL or MariaDB backends, a number of extra packages need to be installed:

```
sudo apt-get install mysql-server libmysqlclient-dev
```

Install the python bindings for MySQL:

```
(env) pip3 install mysqlclient mariadb
```


Assuming the MySQL server is installed and running, login to the MySQL server as follows:

```
sudo mysql -u root
```

Create a new database as follows:

```
mysql> CREATE DATABASE inventree;
```

Create a new user with complete access to the database:

```
mysql> CREATE USER 'inventreeuser'@'%' IDENTIFIED WITH mysql_native_password BY 'inventree';
mysql> GRANT ALL ON blog_data.* TO 'djangouser'@'%';
mysql> FLUSH PRIVILEGES;
```

Exit the mysql shell:

```
mysql> EXIT;
```

## Configure InvenTree Options

Once the required software packages are installed and the database has been created, the InvenTree server options must be configured.

InvenTree configuration can be performed using environment variables, or the `config.yaml` file (or a combination of both).

Edit the configuration file at  `/home/inventree/src/InvenTree/config.yaml`.

!!! info "Config Guidelines"
    Refer to the [configuration guidelines](../config) for full details.

!!! warning "Configure Database"
    Ensure database settings are correctly configured before proceeding to the next step!

## Initialize Database

The database has been configured above, but is currently empty. 

### Schema Migrations

Run the following command to initialize the database with the required tables.

```
(env) invoke update
```

### Create Admin Account

Create a superuser (admin) account for the InvenTree installation:

```
(env) invoke superuser
```

!!! success "Ready to Serve"
    The InvenTree database is now fully configured, and ready to go. 

## Start Server

### Development Server

The InvenTree database is now setup and ready to run. A simple development server can be launched from the command line. 

The InvenTree development server is useful for testing and configuration - and it may be wholly sufficient for a small-scale installation.

Refer to the [development server instructions](../development) for further information.

### Production Server

In a production environment, a more robust server setup is required.

Refer to the [production server instructions](../production) for further information.

## Install Gunicorn

Gunicorn can be installed using PIP:

```
pip3 install gunicorn
```

!!! warning "Python Environment"
    Ensure that gunicorn is installed within the same python environment context as the InvenTree install - otherwise gunicorn will not be able to import the correct python modules.


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
