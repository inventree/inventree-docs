---
title: Demo Dataset
---

## Demo Dataset

A demonstration dataset is [available on GitHub](https://github.com/inventree/demo-dataset).

This dataset can be used to populate an empty database for demonstration purposes, to test and evaluate various InvenTree features.

It may also be useful to developers who need a dataset for developing and/or testing new InvenTree features

## Login Details

The default *superuser* login details for the demo dataset are:

| Username | Password |
| --- | --- |
| admin | inventree |

## Setup

Follow these instructions to setup an InvenTree instance with the demo data:

### Download Dataset

Download the demo dataset, e.g. using git:

```
git clone git@github.com:inventree/demo-dataset.git ~/inventree-data
```

!!! info "Data Directory
    For the purpose of these instructions it is assumed that the demo data repository has been cloned to ~/inventree-data.

### Initialize Database

You will need to configure an *empty* database before importing the data fixtures.

Follow the [installation instructions](./intro.md) to initialize a database using your backend of choice.

### Configure InvenTree Settings

You will need to adjust your InvenTree settings (either via environment variables or in the `config.yaml` file) as follows:

#### Media Files

Ensure that `INVENTREE_MEDIA_ROOT` points to the media files at ~/inventree-data/media

### Run Migrations

You will need to ensure that the database migrations are performed before importing records

```
invoke migrate
```

### Import Data

Now that you have an empty database (which has had the schema migrations applied) you can import the demo dataset:

```
invoke import-records -f ~/inventree-data/inventree_data.json
```

## Contribute

Contributions to the demo dataset are encouraged! A richer dataset provides a better demo experience and helps to showcase the various features available in InvenTree.

To contribute back to the InvenTree demo dataset:

### Import Data

Follow the directions above to create an InvenTree instance using the latest demo dataset

### Git Branch

Create a git branch for the demo-dataset repository

### Edit Data

Create / edit / update the InvenTree database and media files as required

### Export Data

Export the updated data, overwriting the original data file:

```
invoke export-records -f ~/inventree-data/inventree_data.json
```

### Create Pull Request

Create a pull request on the [demo-dataset repository](https://github.com/inventree/demo-dataset) with the changes you have made.