---
title: Install InvenTree
---

## Initial Setup

Follow the instructions below to install the requried system packages, python modules, and InvenTree source code.

### Install System Packages

Install required system packages (as superuser):

!!! warning "OS Specific Requirements"
    The following packages are required on a debian system. A different distribution may require a slightly different set of packages

```
sudo apt-get update
sudo apt-get install python3 python3-dev
sudo apt-get install python3-pip python3-invoke python3-venv
```

!!! warning "Weasyprint"
    On some systems, the dependencies for the `weasyprint` package might not be installed. Consider running through the [weasyprint installation steps](https://weasyprint.readthedocs.io/en/stable/install.html) before moving forward.


### Create InvenTree User

!!! warning "Running as Root"
    It is highly recommended that the InvenTree server is not run under root. The deployment instructions assume that InvenTree is installed and run from a different user account.
    
Create a user account from which we will run the server:

```
sudo useradd -m -d /home/inventree -s /bin/bash inventree
```

InvenTree source code, log files, etc will be located under the `/home/inventree/` directory.

Switch to the `inventree` user so commands are performed in the correct context:

```
sudo su inventree
```

### Create Required Directories

```
cd /home/inventree
mkdir log static data
```

This step creates directories required by InvenTree:

* `/home/inventree/log` - Store InvenTree log files
* `/home/inventree/static` - Location of static files for the web server
* `/home/inventre/data` - Location of uploaded media files

### Download Source Code

Download InvenTree source code, into the `./src` directory:

```
git clone https://github.com/inventree/inventree src
```

### Create Virtual Environment

Create a python virtual environment for installing required Python packages and binaries:

```
python3 -m venv env
source ./env/bin/activate
```

!!! info "(env) prefix"
    The shell prompt should now display the `(env)` prefix, showing that you are operating within the context of the python virtual environment

### Install InvenTree Packages

The Python packages required by the InvenTree server must be installed into the virtual environment. 

```
pip install -U -r src/requirements.txt
```

This installs all required Python packages using pip package manager. It also creates a (default) database configuration file which needs to be edited to meet user needs before proceeding (see next step below).

## Create Database

As part of the initial setup, an empty database needs to be created. Follow the instructions below particular to your database engine of choice:

### SQLite

SQLite uses a simple portable database file which is easy to use for debug and testing purposes.

Install required packages as follows:

!!! info "Sudo Actions"
    Perform sudo actions from a separate shell, as 'inventree' user does not have sudo access

```
sudo apt-get install sqlite3
```

A `.sqlite3` database file will be automatically created, at the location specified in the configuration options. No further steps necessary.

!!! warning "SQLite Case Sensitivity"
    SQLite has a known [string matching limitation](https://docs.djangoproject.com/en/dev/ref/databases/#substring-matching-and-case-sensitivity) for non ASCII characters. If you are using non ASCII characters (e.g. Cyrillic text), it is recommended that you do not use SQLite, as search functionality will not work correctly.

### PostgreSQL

#### Install PostgreSQL

Install required system packages:

!!! info "Sudo Actions"
    Perform sudo actions from a separate shell, as 'inventree' user does not have sudo access

```
sudo apt-get install postgresql postgresql-contrib libpq-dev
```

And start the postgresql service:

```
sudo service postgresql start
```

#### Create Database and User

We need to create new database, and a postgres user to allow database access.

```
sudo -u postgres psql
```

You should now be in an interactive database shell:

```
create database inventree;
create user myuser with encrypted password 'mypass';
grant all privileges on database inventree to myuser;
```

!!! info "Username / Password"
    You should change the username and password from the values specified above. This username and password will also be for the InvenTree database connection configuration.

#### Install Python Bindings

The PostgreSQL python binding must also be installed (into your virtual environment):

```
pip3 install psycopg2 pgcli
```

### MySQL / MariaDB

#### Install Backend

To run InvenTree with the MySQL or MariaDB backends, a number of extra packages need to be installed:

!!! info "Sudo Actions"
    Perform sudo actions from a separate shell, as 'inventree' user does not have sudo access

```
sudo apt-get install mysql-server libmysqlclient-dev
```

#### Install Python Bindings

Install the python bindings for MySQL (into the python virtual environment).

```
pip3 install mysqlclient mariadb
```

#### Create Database

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
mysql> CREATE USER 'myuser'@'%' IDENTIFIED WITH mysql_native_password BY 'mypass';
mysql> GRANT ALL ON blog_data.* TO 'djangouser'@'%';
mysql> FLUSH PRIVILEGES;
```

Exit the mysql shell:

```
mysql> EXIT;
```

!!! info "Username / Password"
    You should change the username and password from the values specified above. This username and password will also be for the InvenTree database connection configuration.

## Configure InvenTree Options

Once the required software packages are installed and the database has been created, the InvenTree server options must be configured.

InvenTree configuration can be performed using environment variables, or the `config.yaml` file (or a combination of both).

Edit the configuration file at  `/home/inventree/src/InvenTree/config.yaml`.

!!! info "Config Guidelines"
    Refer to the [configuration guidelines](./config.md) for full details.

!!! warning "Configure Database"
    Ensure database settings are correctly configured before proceeding to the next step! In particular, check that the database connection settings match the database you have created in the previous step.

## Initialize Database

The database has been configured above, but is currently empty. 

### Schema Migrations

Run the following command to initialize the database with the required tables.

```
cd /home/inventree/src
invoke update
```

### Create Admin Account

Create a superuser (admin) account for the InvenTree installation:

```
invoke superuser
```

!!! success "Ready to Serve"
    The InvenTree database is now fully configured, and ready to go. 

## Start Server

### Development Server

The InvenTree database is now setup and ready to run. A simple development server can be launched from the command line. 

The InvenTree development server is useful for testing and configuration - and it may be wholly sufficient for a small-scale installation.

Refer to the [development server instructions](./development.md) for further information.

### Production Server

In a production environment, a more robust server setup is required.

Refer to the [production server instructions](./production.md) for further information.
