---
title: Docker Setup
---

## Docker Image

The most convenient method of installing and running InvenTree is to use the official [docker image](https://hub.docker.com/inventree/inventree).

The InvenTree docker image contains all the required system packages, python modules, and configuration files for running InvenTree.

## Docker Compose

An example docker compose script is provided below, which provides a robust "out of the box" setup for running InvenTree.

### Containers

The following containers are created:

#### PostgreSQL Database

A postgresql database container which creates a postgres user:password combination (which can be changed)

#### Web Server

InvenTree web server running on a Gunicorn backend

#### Background Worker

InvenTree background worker process manager

#### Nginx

Nginx working as a reverse proxy, separating requests for static files and directing everything else to Gunicorn

### Volumes

There are two container volumes created:

#### Data

InvenTree stores data which is meant to be persistent (e.g. uploaded media files, database data, etc) in a volume which is mapped to a local system directory.

!!! info "Data Directory"
    Make sure you change the path to the local directory where you want persistent data to be stored.

#### Static

Static files are shared between multiple containers (but not exposed to the local file system).

### Docker Compose File

Use the following docker-compose file as a starting point:

``` yaml
{% include 'docker-compose.yml' %}
```

## Initial Setup Process

Follow the instructions below to initialize a complete docker deployment for InvenTree.

!!! info "Directory"
    It is assumed that all commands will be run from the directory where `docker-compose.yml` is located. 

### Configure Compose File

Save and edit the `docker-compose.yml` file as required.

The only **required** change is to ensure that the `/path/to/data` entry (at the end of the file) points to the correct directory on your local file system, where you want InvenTree data to be stored.

### Build

Build the docker containers:

```
docker-compose build
```

### Launch Database Server

Before we can create the database, we need to launch the database server container:

```
docker-compose up -d db
```

This starts the database container.

### Create Database

Run the following command to open a shell session for the database:

```
docker-compose run inventree pgcli -h db -p 5432 -u pguser
```

!!! info "User"
    If you have changed the `POSTGRES_USER` variable in the compose file, replace `pguser` with the different user.

You will be prompted to enter the database user password (default="pgpassword", unless altered in the compose file).

Next, run the following command in the database shell:

```
create database inventree;
```

Then exit the shell with <kbd>Ctrl</kbd>+<kbd>d</kbd>

### Perform Database Migrations

The database has been created, but it is empty! We need to perform the initial database migrations.

```
docker-compose run inventree invoke migrate
```

This will perform the required schema updates to create the required database tables.

### Collect Static Files

On first run, the required static files must be collected into the `static` volume:

```
docker-compose run inventree invoke static
```

### Create Admin Account

You need to create an admin (superuser) account for the database. Run the command below, and follow the prompts:

```
docker-compose run inventree invoke superuser
```

### Configure InvenTree Options

By default, all required InvenTree settings are specified in the docker compose file, with the `INVENTREE_DB_` prefix.

You are free to skip this step, if these InvenTree settings meet your requirements.

If you wish to tweak the InvenTree configuration options, you can either:

#### Environment Variables

Alter (or add) environment variables into the docker-compose `environment` section

#### Configuration File

A configuration file `config.yaml` has been created in the data volume (at the location specified on your local disk).

Edit this file (as per the [configuration guidelines](../config)).

### Run Web Server

Now that the database has been created, migrations applied, and you have created an admin account, we are ready to launch the web server:

```
docker-compose up -d
```

This command launches the remaining container processes:

- `inventree` - InvenTree web server
- `worker` - Background worker
- `nginx` - Nginx reverse proxy

!!! success "Up and Running!"
    You should now be able to view the InvenTree login screen at [http://localhost:1337](http://localhost:1337)
