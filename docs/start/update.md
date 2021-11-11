---
title: Update InvenTree
---

## Update InvenTree

Administrators wishing to update InvenTree to the latest version should follow the instructions below. The commands listed below should be run from the InvenTree root directory.

!!! info "Update Database"
	It is advisable to backup the InvenTree database before performing these steps. The particular backup procedure may depend on your installation details.

### Stop InvenTree Server

Ensure the InvenTree server is stopped. This will depend on the particulars of your database installation.

!!! info "Stop Server"
    The method by which the InvenTree server is stopped depends on your particular installation!

### Update Source Code

Update the InvenTree source code to the latest version (or a particular commit if required).

For example, pull down the latest InvenTree sourcecode using Git:

```
git pull origin master
```

!!! info "Release Versions"
    If you are using a particular version of InvenTree, you may wish to target a specific code branch or tag, instead of just pulling down latest master

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
