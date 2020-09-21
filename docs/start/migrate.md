---
title: Migrating Data
layout: page
---

## Migrating Data

In the case that data needs to be migrated from one database installation to another, the following procedure can be used to export data, initialize the new database, and re-import the data.

!!! warning "Backup Database"
	Ensure that the original database is securely backed up first!

### Export Data

```
python3 InvenTree/manage.py dumpdata --exclude contenttypes --exclude auth.permission --indent 2 > data.json
```

This will export all data (including user information) to a json data file.

### Initialize New Database

Configure the new database using the normal processes (see [Configuration](start/config))

Then, ensure that the database schema are correctly initialized in the new database:

```
python3 InvenTree/manage.py makemigrations
python3 InvenTree/manage.py migrate --run-syncdb
```

### Import Data

The new database should now be correctly initialized with the correct table structures requried to import the data. Run the following command to load the databased dump file into the new database.

```
python3 InvenTree/manage.py loaddata data.json
```
!!! info "Character Encoding"
	If the character encoding of the data file does not exactly match the target database, the import operation may not succeed. In this case, some manual editing of the database JSON file may be required.