---
title: InvenTree
layout: page
permalink: "/"
---

## InvenTree - Intuitive Inventory Management 

InvenTree is an open-source inventory management system which provides intuitive parts management and stock control. 

InvenTree is designed to be lightweight and easy to use for SME or hobbyist applications, where many existing stock management solutions are bloated and cumbersome to use. However, powerful business logic works in the background to ensure that stock tracking history is maintained, and users have ready access to stock level information.

### How it Works

InvenTree is a [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/) application which stores data in a relational database, and serves this data to the user(s) via a web browser, and (optionally) can be integrated into custom applications via an API.

InvenTree is designed to allow for a flexible installation. You could run the InvenTree server on Raspberry Pi SBC and have a simple single-user setup with a lightweight sqlite database. Or it can be run on the "cloud" using MySQL or PostgreSQL and support multiple simultaneous users.

## Features

### Organize Parts

Parts are the fundemental element of any inventory. InvenTree groups parts into structured categories which allow you to arrange parts to meet your particular needs. 

[Read more...](part/part)

### Manage Suppliers

Link parts to multiple suppliers, 

[Read more...](buy/supplier)

### Instant Stock Knowledge

Instantly view current stock for a certain part, in a particular location, or required for an individual build. Stock items are organized in cascading locations and sub-locations, allowing flexible inspection of stock under any location. Stock items can be serialized for tracking of individual items, and test results can be stored against a serialized stock item for the purpose of acceptance testing and commissioning.

[Read more...](stock/stock)

### BOM Management

Intelligent BOM (Bill of Material) management provides a clear understanding of the sub-parts required to make a new part. 

[Read more...](build/bom)

### Build Parts

Consume stock items to make new parts

[Read more...](build/build)

### Report

Generate a wide range of reports using custom templates. [Read more...](docs/report/report)

### Extend and Customize

InvenTree is designed to be highly extensible. If the core InvenTree functionality does not meet your particular need, InvenTree provides a RESTful API, a native Python library, and a powerful plugin system.

[Read more...](extend/api)

## Getting Started

Refer to the [installation guide](start/install) for instructions on installing InvenTree. The server where InvenTree is to be installed will need to meet some basic package requirements, and a certain level of system administration understanding is assumed.