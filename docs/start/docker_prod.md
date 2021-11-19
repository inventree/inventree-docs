---
title: Docker Production Server
---

## Docker Production Server

Using the [InvenTree docker image](./docker.md) streamlines the setup process for an InvenTree production server.

!!! warning "Static and Media Files"
    The sample docker-compose configuration shown on this page uses nginx to serve static files and media files. If you change this configuration, you will need to ensure that static and media files are served correctly. When running with `debug=False`, django *will not serve these files* - see the [django documentation](https://docs.djangoproject.com/en/dev/howto/static-files/).

## Docker Compose

It is strongly recommended that you use a [docker-compose](https://docs.docker.com/compose/) script to manage your InvenTree docker image.

### Example Script

An example docker compose file can be [found here](https://github.com/inventree/InvenTree/blob/master/docker/docker-compose.yml) - the documentation below will be using this docker compose file.

!!! info "Stable Version"
    The example docker-compose file targets `inventree:stable` docker image by default

### Containers

The example docker-compose file launches the following containers:

| Container | Description |
| --- | --- |
| inventree-db | PostgreSQL database |
| inventree-server | Gunicorn web server |
| invenrtee-worker | django-q background worker |
| inventree-proxy | nginx proxy |

#### PostgreSQL Database

A postgresql database container which creates a postgres user:password combination (which can be changed). This uses the official [PostgreSQL image](https://hub.docker.com/_/postgres).

*__Note__: An empty database must be manually created as part of the setup (below)*.

#### Web Server

Runs an InvenTree web server instance, powered by a Gunicorn web server. In the default configuration, the web server listens on port `8000`.

#### Background Worker

Runs the InvenTree background worker process. This spins up a second instance of the *inventree* container, with a different entrypoint command.

#### Nginx

Nginx working as a reverse proxy, separating requests for static and media files, and directing everything else to Gunicorn.

This container uses the official [nginx image](https://hub.docker.com/_/nginx).

!!! info "Configuration File"
    An nginx configuration file must be provided to the image. Use the [example configuration file](https://github.com/inventree/InvenTree/blob/master/docker/nginx.conf) as a starting point.

    *__Note__: You must save the `nginx.conf` file in the same directory as your docker-compose.yml file*

!!! info "Proxy Pass"
    If you change the name (or port) of the InvenTree web server container, you will need to also adjust the `proxy_pass` setting in the nginx.conf file!

### Data Volume

InvenTree stores data which is meant to be persistent (e.g. uploaded media files, database data, etc) in a volume which is mapped to a local system directory.

!!! info "Data Directory"
    Make sure you change the path to the local directory where you want persistent data to be stored.

The InvenTree docker server will manage the following directories and files within the 'data' volume:

| Path | Description |
| --- | --- |
| ./config.yaml | InvenTree server configuration file |
| ./secret_key.txt | Secret key file |
| ./media | Directory for storing uploaded media files |
| ./static | Directory for storing static files |

## Production Setup

With the docker-compose recipe above, follow the instructions below to initialize a complete production server for InvenTree.

### Required Files

The following files are required on your local machine (use the examples above, or edit as required):

| File | Description |
| --- | --- |
| [docker-compose.yml](https://github.com/inventree/InvenTree/blob/master/docker/docker-compose.yml) | docker-compose script |
| [nginx.conf](https://github.com/inventree/InvenTree/blob/master/docker/nginx.conf) | nginx proxy server configuration file |
| [prod-config.env](https://github.com/inventree/InvenTree/blob/master/docker/prod-config.env) | Docker container environment variables |

!!! info "Command Directory"
    It is assumed that all following commands will be run from the directory where `docker-compose.yml` is located. 

#### Edit Configuration Files

Edit the `docker-compose.yml` file as required.

!!! warning "Change Data Directory"
    The only **required** change is to ensure that the `/path/to/data` entry (at the end of the file) points to the correct directory on your local file system, where you want InvenTree data to be stored.

!!! info "Database Credentials"
    You may also wish to change the default postgresql username and password!

You may also edit the `nginx.conf` and `prod-config.env` files if necessary.

### Launch Database Container

Before we can create the database, we need to launch the database server container:

```
docker-compose up -d inventree-db
```

This starts the database container (in this example, a PostgreSQL server).

### Create Database

If this is the first time we are interacting with the docker containers, the InvenTree database has not yet been created.

!!! success "First Run Only"
    If you have already created the InvenTree database you can progress to the next step

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

### Database Setup

The database has now been created, but it is empty! Perform the initial database setup by running the following command:

```
docker-compose run inventree-server invoke update
```

This command performs the following steps:

- Ensure required python packages are installed
- Perform the required schema updates to create the required database tables
- Update translation files
- Collect all required static files into a directory where they can be served by nginx

### Create Admin Account

If you are creating the initial database, you need to create an admin (superuser) account for the database. Run the command below, and follow the prompts:

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

!!! info "Tagged Version"
    If you are targetting a particular "tagged" version of InvenTree, you may wish to edit your docker-compose file before issuing the `docker-compose pull` command

### Update Database

Run the following command to ensure that the InvenTree database is updated:

```
docker-compose run inventree-server invoke update
```

### Start Containers

Now restart the docker containers:

```
docker-compose up -d
``` 

## Data Backup

Database and media files are stored external to the container, in the volume location specified in the `docker-compose.yml` file. It is strongly recommended that a backup of the files in this volume is performed on a regular basis.

### Exporting Database as JSON

To export the database to an agnostic JSON file, perform the following command:

```
docker-compose run inventree-server invoke export-records -f /home/inventree/data/data.json
```

This will export database records to the file `data.json` in your mounted volume directory.
