---
title: Update InvenTree
layout: page
---

## Update InvenTree

Administrators wishing to update InvenTree to the latest version should follow the instructions below. The commands listed below should be run from the InvenTree root directory.

!!! info "Update Database"
	It is advisable to backup the InvenTree database before performing these steps. The particular backup procedure may depend on your installation details.

### Stop InvenTree Server

Ensure the InvenTree server is stopped. This will depend on the particulars of your database installation.

### Update Source Code

Update the InvenTree source code to the latest version (or a particular commit if required).

For example, pull down the latest InvenTree sourcecode using Git:

```
git pull origin master
```

### Perform Database Migrations

Updating the database is as simple as calling the `update` script:

```
invoke update
```

This command performs the following steps:

* Ensure all rquired packages are installed and up to date
* Perform required database schema changes
* Run the user through any steps which require interaction
* Collect any new or updated static files

### Restart Server

Ensure the InvenTree server is restarted. This will depend on the particulars of your database installation.