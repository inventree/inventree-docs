---
title: Migrating Data
---

## Migrating Data

In the case that data needs to be migrated from one database installation to another, the following procedure can be used to export data, initialize the new database, and re-import the data.

For example, if you wish to migrate from an SQLite database backend to a MySQL database backend, you will need to export the data into a standardized format, and then read it back in to the new database.

!!! warning "Backup Database"
	Ensure that the original database is securely backed up first!

!!! info "Up to Date"
    Ensure that the original database is up to date, by running `inv migrate`

### Export Data

Export the database contents to a JSON file using the following command:

```
inv export-records -f data.json
```

This will create JSON file at the specified location which contains all database records.

!!! info "Specifying filename"
    The filename of the exported file can be specified using the `-f` option

### Initialize New Database

Configure the new database using the normal processes (see [Configuration](../config))

Then, ensure that the database schema are correctly initialized in the new database:

```
inv migrate
```

This ensures that the required database tables exist, which must be the case before data can be imported.

### Import Data

The new database should now be correctly initialized with the correct table structures requried to import the data. Run the following command to load the databased dump file into the new database.

```
inv import-records -f data.json
```

!!! info "Import Filename"
    A different filename can be specified using the `-f` option 

!!! warning "Character Encoding"
	If the character encoding of the data file does not exactly match the target database, the import operation may not succeed. In this case, some manual editing of the database JSON file may be required.

### Backup and Restore

To backup your database data and media files, first define a [Backup Location](../config/#backup-location) in your configuration file.

Then run the following command to backup the data:
```
inv backup
```

It should create two separate backup files in the [Backup Location](../config/#backup-location) folder: one for the database data and one for the media files (part pictures, etc.)

To restore your data from a backup, use the following command:
```
inv restore
```
