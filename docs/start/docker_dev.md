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

The [InvenTree docker image](https://github.com/inventree/InvenTree/blob/master/docker/Dockerfile) uses a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/) process to allow both production and development setups from the same image. The key difference is that the production image is pre-built using InvenTree source code from GitHub, while the development image uses the source code from your local machine (allowing live code updates).

### Docker Compose

A docker compose script for running a development server is provided in the source repository at [./docker/docker-compose.dev.yml](https://github.com/inventree/InvenTree/blob/master/docker/docker-compose.dev.yml).

This script specifies the following containers:

| Container | Description |
| --- | --- |
| inventree-dev-server | Web server using the django development server |
| inventree-dev-worker | Background task manager |

!!! success "Works out of the box"
    You should not need to make any changes to the `docker-compose.dev.yml` file to run the development docker container

### Environment Variables

Environment variables for the docker containers can be found in the file `dev-config.env` in the `docker` directory.

!!! success "Works out of the box"
    You should not normally need to change these variables from their default values.

## Setup

### Download Source Code

First download the source code from GitHub:

```
git clone git@github.com:inventree/InvenTree.git inventree
```

### Build Docker Containers

Build the docker containers with the following commands:

```
cd inventree/docker
docker-compose -f docker-compose.dev.yml build
```

### Create Database

!!! info "First Run Only"
    This command only needs to be executed on the first run, if the development database has not already been initialized

```
docker-compose -f docker-compose.dev.yml run inventree-dev-server invoke update
```

This command performs the following tasks:

- Install required python packages into a local python virtual environment
- Create an SQLite database and perform schema migrations
- Collect static files

### Create Superuser

!!! info "First Run Only"
    This command only needs to be executed on the first run, if you have not already created a superuser account for the database

```
docker-compose -f docker-compose.dev.yml run inventree-dev-server invoke superuser
```

This will prompt you to create a superuser account for the InvenTree instance.

### Run Containers

Launch the server and worker containers with the following command:

```
docker-compose -f docker-compose.dev.yml up -d
```

!!! success "Check Connection"
    Check that the server is running at [http://localhost:8000](http://localhost:8000). The server may take a few minutes to be ready.

## Restarting Services

Once initial setup is complete, stopping and restarting the services is much simpler:

### Stop InvenTree Services

To stop the InvenTree development server, simply run the following command:

```
docker-compose -f docker-compose.dev.yml down
```

### Start InvenTree Services

To restart the InvenTree development server, simply run the following command:

```
docker-compose -f docker-compose.dev.yml up -d
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
