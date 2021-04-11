---
title: InvenTree
---

## InvenTree - Intuitive Inventory Management 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repo stars](https://img.shields.io/github/stars/inventree/inventree?label=View%20On%20GitHub&style=social)](https://github.com/inventree/inventree)
[![Docker Pulls](https://img.shields.io/docker/pulls/inventree/inventree)](https://hub.docker.com/inventree/inventree)


InvenTree is an open-source inventory management system which provides intuitive parts management and stock control. 

InvenTree is designed to be lightweight and easy to use for SME or hobbyist applications, where many existing stock management solutions are bloated and cumbersome to use. However, powerful business logic works in the background to ensure that stock tracking history is maintained, and users have ready access to stock level information.

### How it Works

InvenTree is a [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/) application which stores data in a relational database, and serves this data to the user(s) via a web browser, and (optionally) can be integrated into custom applications via an API.

InvenTree is designed to allow for a flexible installation. You could run the InvenTree server on Raspberry Pi SBC and have a simple single-user setup with a lightweight SQLite database. Or it can be run on the "cloud" using MySQL or PostgreSQL and support multiple simultaneous users.

## Features

Refer to the [features](./features) page for a rundown on the features that InvenTree provides out of the box.

## Getting Started

Refer to the [installation guide](./start/install) for instructions on installing InvenTree. The server where InvenTree is to be installed will need to meet some basic package requirements, and a certain level of system administration understanding is assumed.

## Get the App

InvenTree is supported by a [companion mobile app](./app/app) which is tightly integrated with the InvenTree database. Lightning fast stock control, in your pocket!