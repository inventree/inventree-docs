---
title: Docker Development Setup
---

## Docker Development Setup

You can also use docker to launch and manage a development server, in a similar fashion to managing a production server.

There are some key differences compared to the docker production setup:

- The docker image is built locally, rather than being downloaded from DockerHub
- The docker image points to the source code on your local machine, instead of cloning from GitHub
- The django webserver is used, instead of running behind Gunicorn
- The server will automatically reload when code changes are detected

The [InvenTree docker image](https://github.com/inventree/InvenTree/blob/master/docker/Dockerfile) uses a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) process to allow both production and development setups from the same image. The key difference is that the production image is pre-built using InvenTree source code from GitHub, while the development image uses the source code from your local machine (allowing live code updates).

## Docker Compose

A docker compose script for running a development server is provided in the source repository at [./docker/docker-compose.dev.yml](https://github.com/inventree/InvenTree/blob/master/docker/docker-compose.dev.yml).

This script specifies the following containers:

| Container | Description |
| --- | --- |
| inventree-dev-server | Web server using the django development server |
| inventree-dev-worker | Background task manager |

## Setup

### Download Source Code

First download the source code from GitHub:

```
git clone git@github.com:inventree/InvenTree.git
cd inventree/docker
```

### (Optional) Edit docker-compose File

The default docker-compose recipe should work "out of the box". However you may want to edit this file to test some custom functionality.

Now, edit the `docker-compose.dev.yml` file (in the `docker` subdirectory), ensuring that the `src` volume points to the directory on your local machine where you have just cloned the source code.

!!! warning "Beware Changes"
    Ensure that you do not commit any changes to the docker-compose.dev.yml file to git!

### (Optional) Edit Environment Variables

Environment variables for the development server docker images are set in the file [dev-config.env](https://github.com/inventree/InvenTree/blob/master/docker/dev-config.env).

In the default configuration these should not need to be adjusted.

### Launch Development Server

Launch the development server with the following command:

```
docker-compose -f docker-compose.dev.yml up -d inventree-dev-server
```

This command will perform the following actions, in sequence:

#### Create Required Files

The following required files are created (if they do not already exist):

!!! success "File Creation"
    The following files are created (paths are relative to the top-level InvenTree source directory).

| File | Description |
| --- | --- |
| ./dev/config.yaml | InvenTree configuration file |
| ./dev/secret_key.txt | Secret key file |
| ./dev/media | Directory for storing uploaded media files |
| ./dev/static | Directory for storing static files |
| ./dev/env | Python virtual environment |

#### Install Required Python Packages

The required python packages will be installed into the `./dev/env/` directory.

!!! info "Wait for Install"
    The first time the server is launched, it will take a few minutes to install the required python packages.

#### Perform Database Migrations

Database schema migrations are automatically performed.

#### Launch Development Server

Once the required python packages are installed, the development web server is then started.

!!! success "Check Connection"
    Check that the server is running at [http://localhost:8000](http://localhost:8000) before proceeding.

### Create Superuser

Once the development server is running, you can now create a superuser (admin) account:

```
docker-compose -f docker-compose.dev.yml run inventree-dev-server bash
```

Inside the docker shell, run the following commands:

```
source ./dev/env/bin/activate
invoke superuser
```

### Start Background Worker

The InvenTree web server should now be running - but the background worker has not yet been started:

To launch the backround worker process:

```
docker-compose -f docker-compose.dev.yml up -d inventree-dev-worker
```

## Restarting Services

Once initial setup is complete, restarting the services is much simpler:

### Start InvenTree Services

To restart the InvenTree development server, simply run the following command:

```
docker-compose -f docker-compose.dev.yml up -d
```

### Stop InvenTree Services

To stop the InvenTree development server, simply run the following command:

```
docker-compose -f docker-compose-dev.yml down
```

## Editing InvenTree Source

Any changes made to the InvenTree source code are automatically detected by the services running under docker.

Thus, you can freely edit the InvenTree source files in your editor of choice.

### Database Updates

Any updates which require a database schema change must be reflected in the database itself.

To run database migrations inside the docker container, run the following command:

```
docker-compose -f docker-compose.dev.yml run inventree-dev-server invoke update
```
