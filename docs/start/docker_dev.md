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

### Docker Compose

A docker compose script for running a development server is provided at `docker/docker-compose.dev.yml`:

### Setup

#### Download Source Code

First download the source code from GitHub:

```
git clone git@github.com:inventree/InvenTree.git
cd inventree/docker
```

#### Edit docker-compose File

Now, edit the `docker-compose.dev.yml` file (in the `docker` subdirectory), ensuring that the `src` volume points to the directory on your local machine where you have just cloned the source code.

#### Launch Development Server

Launch the development server with the following command:

```
docker-compose -f docker-compose.dev.yml up -d inventree-server
```

This launches the InvenTree server (in development mode) and also performs the following tasks:

- Creates an sqlite database
- Creates a `config.yaml` file
- Creates a `secret_key.txt` file
- Creates `inventree_media` directory for uploaded media files
- Creates `inventree_static` directory for storing static files

!!! info "Wait for Install"
    The first time the server is launched, it will take a few minutes to install the required python packages.

Check that the server is running at [http://localhost:8000](http://localhost:8000)

#### Create Superuser

Once the development server is running, create a superuser (admin) account:

```
docker-compose -f docker-compose.dev.yml run inventree-server bash
```

Inside the docker shell, run the following commands:

```
source ./inventree-docker-dev/bin/activate
invoke superuser
```

#### Start Background Worker

To launch the backround worker process:

```
docker-compose -f docker-compose.dev.yml up -d inventree-worker
```
