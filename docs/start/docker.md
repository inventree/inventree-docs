---
title: Docker Setup
---

## Docker Image

The most convenient method of installing and running InvenTree is to use the official [docker image](https://hub.docker.com/r/inventree/inventree), available from docker-hub.

The InvenTree docker image contains all the required system packages, python modules, and configuration files for running a containerised InvenTree web server.

### Environment Variables

InvenTree run-time configuration options described in the [configuration documentation](./config.md) can be passed to the InvenTree container as environment variables.

The following environment variables for InvenTree server configuration are specified as part of the docker image, and can be overridden if required:

| Variable | Description | Default Value |
| --- | --- | --- |
| INVENTREE_LOG_LEVEL | InvenTree logging verbosity level |INFO |
| INVENTREE_CONFIG_FILE | Location (within the docker image) of the InvenTree configuration file | /home/inventree/data/config.yaml |
| INVENTREE_SECRET_KEY_FILE | Location (within the docker image) of the InvenTree sercret key file | /home/inventree/data/secret_key.txt |
| INVENTREE_WEB_PORT | Internal container port on which the InvenTree web server is hosted | 8000 |

The following environment variables are explicitly **not configured** and *must* be passed to the container instance:

| Variable | Description |
| --- | --- |
| INVENTREE_DB_ENGINE | Database engine (e.g. 'postgresql') |
| INVENTREE_DB_NAME | Database name (e.g. 'inventree') |
| INVENTREE_DB_HOST | Database server host (e.g. 'inventree-server' if using default docker-compose script) |
| INVENTREE_DB_PORT | Database server port (e.g. '5432') |
| INVENTREE_DB_USER | Database user name (e.g. 'pguser') |
| INVENTREE_DB_PASSWORD | Database user password (e.g. 'pgpassword') |

### Data Directory

Persistent data (e.g. uploaded media files) should be stored outside the container instance.

InvenTree data are stored inside the container at `/home/inventree/data`.

This directory should be mounted as a volume which points to a directory on your local machine.

### Static Directory

Static files are stored internal to the container instance, at the location `/home/inventree/static`

### Configuration File

As discussed in the [configuration documentation](./config.md), InvenTree run-time settings can be provided in a configuration file.

By default, the docker container expects this configuration file in the location `/home/inventree/data/config.yaml`. If this file does not exist, it will be automatically created from a default template file.

As this config file is inside the "data" directory (which should be mounted as a volume) it can be edited outside the context of the container, if necessary.

### Secret Key

InvenTree uses a secret key to provide cryptographic signing for the application.

As specified in the [configuration documentation](./config.md#secret-key) this can be passed to the InvenTree application directly as an environment variable, or provided via a file.

By default, the InvenTree container expects the `INVENTREE_SECRET_KEY_FILE` to exist at `/home/inventree/data/secret_key.txt`. If this file does not exist, it will be created and a new key will be randomly generated.

!!! warning "Same Key"
    Each InvenTree container instance must use the same secret key value, otherwise unexpected behavior will occur.

## Docker Compose

It is strongly recommended that you use a [docker-compose](https://docs.docker.com/compose/) script to manage your InvenTree docker image.

An example docker compose script is provided below, which provides a robust "out of the box" setup for running InvenTree.

Firstly, here is the complete `docker-compose.yml` file which can be used "as is" or as a starting point for a custom setup:

``` yaml
{% include 'docker-compose.yml' %}
```

### Containers

The following containers are created:

#### PostgreSQL Database

A postgresql database container which creates a postgres user:password combination (which can be changed). This uses the official [PostgreSQL image](https://hub.docker.com/_/postgres).

*__Note__: An empty database must be manually created as part of the setup (below)*.

#### Web Server

Runs an InvenTree web server instance, powered by a Gunicorn web server. In the default configuration, the web server listens on port `8000`.

#### Background Worker

Runs the InvenTree background worker process. This spins up a second instance of the *inventree* container, with a different entrypoint command.

#### Nginx

Nginx working as a reverse proxy, separating requests for static files and directing everything else to Gunicorn.

This container uses the official [nginx image](https://hub.docker.com/_/nginx).

An nginx configuration file must be provided to the image. Use the example configuration below as a starting point:

```
{% include 'nginx.conf' %}
```

*__Note__: You must save this conf file in the same directory as your docker-compose.yml file*

!!! info "Proxy Pass"
    If you change the name (or port) of the InvenTree web server container, you will need to also adjust the `proxy_pass` setting in the nginx.conf file!

### Volumes

There are two container volumes created:

#### Data

InvenTree stores data which is meant to be persistent (e.g. uploaded media files, database data, etc) in a volume which is mapped to a local system directory.

!!! info "Data Directory"
    Make sure you change the path to the local directory where you want persistent data to be stored.

#### Static

Static files are shared between multiple containers (but not exposed to the local file system).

## Production Setup

With the docker-compose recipe above, follow the instructions below to initialize a complete production server for InvenTree.

### Required Files

The following files are required on your local machine (use the examples above, or edit as required):

- docker-compose.yml
- nginx.conf

!!! info "Command Directory"
    It is assumed that all commands will be run from the directory where `docker-compose.yml` is located. 

### Configure Compose File

Save and edit the `docker-compose.yml` file as required.

The only **required** change is to ensure that the `/path/to/data` entry (at the end of the file) points to the correct directory on your local file system, where you want InvenTree data to be stored.

!!! info "Database Credentials"
    You may also wish to change the default postgresql username and password!

### Launch Database Container

Before we can create the database, we need to launch the database server container:

```
docker-compose up -d inventree-db
```

This starts the database container.

### Create Database

As this is the first time we are interacting with the docker containers, the InvenTree database has not yet been created.

Run the following command to open a shell session for the database:

```
docker-compose run inventree-server pgcli -h inventree-db -p 5432 -u pguser
```

!!! info "User"
    If you have changed the `POSTGRES_USER` variable in the compose file, replace `pguser` with the different user.

You will be prompted to enter the database user password (default="pgpassword", unless altered in the compose file).

Once logged in, run the following command in the database shell:

```
create database inventree;
```

Then exit the shell with <kbd>Ctrl</kbd>+<kbd>d</kbd>

### Perform Database Migrations

The database has now been created, but it is empty! We need to perform the initial database migrations:

```
docker-compose run inventree-server invoke migrate
```

This will perform the required schema updates to create the required database tables.

### Collect Static Files

On first run, the required static files must be collected into the `static` volume:

```
docker-compose run inventree-server invoke static
```

### Create Admin Account

You need to create an admin (superuser) account for the database. Run the command below, and follow the prompts:

```
docker-compose run inventree-server invoke superuser
```

### Configure InvenTree Options

By default, all required InvenTree settings are specified in the docker compose file, with the `INVENTREE_DB_` prefix.

You are free to skip this step, if these InvenTree settings meet your requirements.

If you wish to tweak the InvenTree configuration options, you can either:

#### Environment Variables

Alter (or add) environment variables into the docker-compose `environment` section

#### Configuration File

A configuration file `config.yaml` has been created in the data volume (at the location specified on your local disk).

Edit this file (as per the [configuration guidelines](./config.md)).

### Run Web Server

Now that the database has been created, migrations applied, and you have created an admin account, we are ready to launch the web server:

```
docker-compose up -d
```

This command launches the remaining containers:

- `inventree-server` - InvenTree web server
- `inventree-worker` - Background worker
- `inventree-nginx` - Nginx reverse proxy

!!! success "Up and Running!"
    You should now be able to view the InvenTree login screen at [http://localhost:1337](http://localhost:1337)

## Updating InvenTree

To update your InvenTree installation to the latest version, follow these steps:

### Stop Containers

Stop all running containers as below:

```
docker-compose down
```

### Update Images

Pull down the latest version of the InvenTree docker image

```
docker-compose pull
```

This ensures that the InvenTree containers will be running the latest version of the InvenTree source code.

### Start Containers

Now restart the containers.

As part of the server initialization process, data migrations and static file updates will be performed automatically.

```
docker-compose up -d
``` 

## Data Backup

Database and media files are stored external to the container, in the volume location specified in the `docker-compose.yml` file. It is strongly recommended that a backup of the files in this volume is performed on a regular basis.

### Exporting Database as JSON

To export the database to an agnostic JSON file, perform the following command:

```
docker-compose run inventree-server invoke export-records /home/inventree/data/data.json
```

This will export database records to the file `data.json` in your mounted volume directory.
