---
title: Docker Production Server
---

## Docker Production Server

Using the [InvenTree docker image](./docker.md) streamlines the setup process for an InvenTree production server.

The following guide provides a streamlined production InvenTree installation, with minimal configuration required.

### Before You Start

#### Docker Compose

This guide assumes that you are comfortable with the basic concepts of docker and docker-compose.

#### Docker Image

This production setup guide uses the official InvenTree docker image, available from dockerhub. The provided docker-compose file targets `inventree:stable` by default.

#### Static and Media Files

The sample docker-compose configuration shown on this page uses nginx to serve static files and media files. If you change this configuration, you will need to ensure that static and media files are served correctly. When running with `debug=False`, django *will not serve these files* - see the [django documentation](https://docs.djangoproject.com/en/dev/howto/static-files/).

#### Required Files

The files required for this setup are provided with the InvenTree source, located in the `./docker/production` directory:

- **docker-compose.yml** : The docker compose script
- **.env** : Environment variables
- **nginx.prod.conf** : nginx proxy configuration file

This tutorial assumes you are working from the `./docker/production` directory. If this is not the case, ensure that these files are provided in your working directory.

### Containers

The example docker-compose file launches the following containers:

| Container | Description |
| --- | --- |
| inventree-db | PostgreSQL database |
| inventree-server | Gunicorn web server |
| invenrtee-worker | django-q background worker |
| inventree-proxy | nginx proxy |

#### PostgreSQL Database

A PostgreSQL database container which requires a username:password combination (which can be changed). This uses the official [PostgreSQL image](https://hub.docker.com/_/postgres).

#### Web Server

Runs an InvenTree web server instance, powered by a Gunicorn web server.

#### Background Worker

Runs the InvenTree background worker process. This spins up a second instance of the *inventree* container, with a different entrypoint command.

#### Nginx

Nginx working as a reverse proxy, separating requests for static and media files, and directing everything else to Gunicorn.

This container uses the official [nginx image](https://hub.docker.com/_/nginx).

### Data Volume

InvenTree stores data which is meant to be persistent (e.g. uploaded media files, database data, etc) in a volume which is mapped to a local system directory. The location of this directory must be configured in the `.env` file.

!!! info "Data Directory"
    Make sure you change the path to the local directory where you want persistent data to be stored.

## Production Setup Guide

!!! info "Starting Point"
    This setup guide assumes you are starting in the `./docker/production/` directory.

### Edit Environment Variables

The first step is to edit the environment variables, located in the `.env` file.

!!! warning "External Volume"
    You must define the `INVENTREE_EXT_VOLUME` variable - this must point to a directory *on your local machine* where persistent data is to be stored.

!!! warning "Database Credentials"
    You must also define the database username (`INVENTREE_DB_USER`) and password (`INVENTREE_DB_PASSWORD`). You should ensure they are changed from the default values for added security

### Create Database

Launch the postgresql database container, and create an empty database, with the following command:

```bash
docker-compose run -d inventree-db
```

This will start the `inventree_db` container (in the background) and create an empty database.

### Perform Database Setup

The database has now been created, but it is empty! Perform the initial database setup by running the following command:

```bash
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

### Start Docker Containers

Now that the database has been created, migrations applied, and you have created an admin account, we are ready to launch the InvenTree containers:

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
