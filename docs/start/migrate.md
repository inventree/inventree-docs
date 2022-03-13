---
title: Migrating Data
---

## Migrating Data

In the case that data needs to be migrated from one database installation to another, the following procedure can be used to export data, initialize the new database, and re-import the data.


!!! warning "Backup Database"
	Ensure that the original database is securely backed up first!

!!! info "Up to Date"
    Ensure that the original database is up to date, by running `inv migrate`

### Export Data

Export the database contents to a JSON file using the following command:

```
invoke export-records -f data.json
```

This will create JSON file at the specified location which contains all database records.

!!! info "Specifying filename"
    The filename of the exported file can be specified using the `-f` option

### Initialize New Database

Configure the new database using the normal processes (see [Configuration](./config.md))

Then, ensure that the database schema are correctly initialized in the new database:

```
invoke migrate
```

This ensures that the required database tables exist, which must be the case before data can be imported.

### Import Data

The new database should now be correctly initialized with the correct table structures requried to import the data. Run the following command to load the databased dump file into the new database.

!!! warning "Empty Database"
    If the database is not *empty* (i.e. it contains data records) then the data import process will fail. If errors occur during the import process, run `invoke delete-data` to clear all existing data from the database.

```
invoke import-records -f data.json
```

!!! info "Import Filename"
    A different filename can be specified using the `-f` option 

!!! warning "Character Encoding"
	If the character encoding of the data file does not exactly match the target database, the import operation may not succeed. In this case, some manual editing of the database JSON file may be required.
