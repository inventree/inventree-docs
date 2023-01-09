---
title: Data Backup
---

## Data Backup

Backup functionality is provided natively using the [django-dbbackup library](https://django-dbbackup.readthedocs.io/en/master/). This library provides multiple options for creating backups of your InvenTree database and media files. In addition to local storage backup, multiple external storage solutions are supported (such as Amazon S3 or Dropbox).

Note that a *backup* operation is not the same as [migrating data](./migrate.md). While data *migration* exports data into a database-agnostic JSON file, *backup* exports a native database file and media file archive.

## Configuration

The following configuration options are available for backup:

| Environment Variable | Configuration File | Description | Default |
| --- | --- | --- | --- |
| INVENTREE_BACKUP_STORAGE | backup_storage | Backup storage backend | django.core.files.storage.FileSystemStorage |
| INVENTREE_BACKUP_DIR | backup_dir | Backup storage directory | *No default* |
| INVENTREE_BACKUP_OPTIONS | backup_options | Specific backup options (dict) | *No default* |

### Storage Providers

If you want to use an external storage provider, extra configuration is required. As a starting point, refer to the [django-dbbackup documentation](https://django-dbbackup.readthedocs.io/en/master/storage.html).

Specific storage configuration options are specified using the `backup_options` dict (in the [configuration file](./config.md)).

## Perform Backup

#### Manual Backup

To perform a manual backup operation, run the following command from the shell:

```
invoke backup
```

### Backup During Update

A database backup can optionally be performed as part of a system update. When performing a manual update of your InvenTree installation - via either [docker](./docker.md) or [bare metal](./install.md) - specify the `-b` or `--backup-data` option as part of the `invoke update` command, e.g.:

```
invoke update --backup-data
```

### Daily Backup

If desired, InvenTree can be configured to perform automated daily backups. The run-time setting to control this is found in the *Server Configuration* tab.

{% with id="auto-backup", url="start/auto-backup.png", description="Automatic daily backup" %}
{% include 'img.html' %}
{% endwith %}

## Restore from Backup

To restore from a previous backup, run the following command from the shell (within virtual environment if configured):

```
invoke restore
```