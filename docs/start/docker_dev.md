---
title: Docker Development Server
---

## Docker Development Server

You can use docker to launch and manage a development server, in a similar fashion to managing a production server.

There are some key differences compared to the [docker production setup](./docker_prod.md):

- The docker image is built locally, rather than being downloaded from DockerHub
- The docker image points to the source code on your local machine, instead of cloning from GitHub
- The django webserver is used, instead of running behind Gunicorn
- The server will automatically reload when code changes are detected

!!! info "Static and Media Files"
    The development server runs in DEBUG mode, and serves static and media files natively.

The InvenTree dockerfile (`./docker/Dockerfile`) uses a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) process to allow both production and development setups from the same image. The key difference is that the production image is pre-built using InvenTree source code from GitHub, while the development image uses the source code from your local machine (allowing live code updates).

!!! info "Hacker Mode"
    The following setup guide starts a development server which will reload "on the fly" as changes are made to the source code. This is designed for programmers and developers who wish to add and test new InvenTree features.

## Development Setup Guide

!!! info "Starting Point"
    This setup guide assumes you are starting in the `./docker/` directory.

### Edit Environment Variables 

If required, the user may edit the environment variables, located in the `.env` file.

!!! success "This step is optional"
    This step can be skipped, as the default variables will work just fine!

!!! info "Database Credentials"
    You may also wish to change the database username (`INVENTREE_DB_USER`) and password (`INVENTREE_DB_PASSWORD`) from their default values

### Create Database

Launch the postgresql database container, and create an empty database, with the following command:

```bash
docker-compose run -d inventree-dev-db
```

This will start the `inventree-dev-db` container (in the background) and create an empty database.

### Perform Initial Setup

The database has now been created, but it is empty! Perform the initial database setup by running the following command:

```bash
docker-compose run inventree-dev-server invoke update
```

If this is the first time you are configuring the development server, this command will build a development version of the inventree docker image.

This command also performs the following steps:

- Ensure required python packages are installed
- Perform the required schema updates to create the required database tables
- Update translation files
- Collect all required static files into a directory where they can be served by nginx

!!! info "Grab a coffee"
    This initial build process may take a few minutes!

### Create Admin Account

If you are creating the initial database, you need to create an admin (superuser) account for the database. Run the command below, and follow the prompts:

```
docker-compose run inventree-dev-server invoke superuser
```

### Start Docker Containers

Now that the database has been created, migrations applied, and you have created an admin account, we are ready to launch the InvenTree containers:

```
docker-compose up -d
```

This command launches the remaining containers:

- `inventree-dev-server` - InvenTree web server
- `inventree-dev-worker` - Background worker

!!! success "Check Connection"
    Check that the server is running at [http://localhost:8000](http://localhost:8000). The server may take a few minutes to be ready.

## Restarting Services

Once initial setup is complete, stopping and restarting the services is much simpler:

### Stop InvenTree Services

To stop the InvenTree development server, simply run the following command:

```
docker-compose down
```

### Start InvenTree Services

To start the InvenTree development server, simply run the following command:

```
docker-compose up -d
```

### Restart InvenTree Services

A restart cycle is as simple as:

```
docker-compose restart
```

## Editing InvenTree Source

Any changes made to the InvenTree source code are automatically detected by the services running under docker.

Thus, you can freely edit the InvenTree source files in your editor of choice.

### Database Updates

Any updates which require a database schema change must be reflected in the database itself.

To run database migrations inside the docker container, run the following command:

```
docker-compose run inventree-dev-server invoke update
```
