---
title: Connect to Server
---

## Connect to InvenTree

Use of the InvenTree app assumes that you (the user) have access to an InvenTree server.

When first running the app, no profile has been configured. The *server* icon in the top-right corner of the home screen is <span style='color: red'>red</span>, indicating that there is no connection to an InvenTree server:

{% with id="no_server", url="app/initial.png", maxheight="240px", description="No server configured" %}
{% include "img.html" %}
{% endwith %}

Press on the server icon to navigate to the server selection view:

{% with id="no_profiles", url="app/no_profiles.png", maxheight="240px", description="No server configured" %}
{% include "img.html" %}
{% endwith %}


### Create Server

!!! success "Server Profiles"
    The app supports multiple server profiles, providing simple switching between different InvenTree servers and/or account profiles.

Press the <span class='fas fa-plus-circle blue'></span> button in the bottom-right corner of the screen to create a new server profile.

{% with id="add_profile", url="app/add_server_profile.png", maxheight="240px", description="Add server" %}
{% include 'img.html' %}
{% endwith %}

Enter the required server details:

| Parameter | Description |
| --- | --- |
| **Name** | Name for the server profile (can be any value, simply for reference) |
| **Server** | InvenTree server address (including port, if required). e.g. `http://inventree.myserver.com:8080` |
| **Username** | Your account username (case sensitive) |
| **Password** | Your account password (case sensitive) |

### Connect to Server

Once the server profile is created, you need to connect to the server. Simply short press on the server profile to connect.

Alternatively, long press on the server profile to activate the context menu, then select *Connect to Server*.

When the app successfully connects to the server, a success message is briefly displayed at the bottom of the screen. A green <span class='fas fa-check-circle green'></span> icon next to the server profile indicate that the profile is currently *selected* and also the connection was successful.

{% with id="connected", url="app/connected.png", maxheight="240px", description="Connected to server" %}
{% include 'img.html' %}
{% endwith %}

### Connection Failure

If (for whatever reason) the app does not successfully connect to the InvenTree server, a failure message is displayed, and a red <span class='fas fa-times-circle red'></span> icon is displayed next to the server profile.

{% with id="failed", url="app/unauthorized.png", maxheight="240px", description="Connection failure" %}
{% include 'img.html' %}
{% endwith %}

In this case, the error message displayed at the bottom of the screen provides context as to why the app could not successfully connect to the server.

To edit the server profile details, long press on the server profile, and select *Edit Server Profile*:

{% with id="edit", url="app/edit_server.png", maxheight="240px", description="Edit server profile" %}
{% include 'img.html' %}
{% endwith %}

## Home Screen

The app *home screen* provides quick-access buttons for stock view and actions:

{% with id="home", url="app/home.png", maxheight="240px", description="Home screen" %}
{% include 'img.html' %}
{% endwith %}

### Scan Barcode

Select the *Scan Barcode* icon to open the [barcode scanner](./barcode.md). Scan a barcode to navigate to a detail view for the item you have scanned.

### Search

Select the *Search* icon to open the InvenTree search window. Entering a search term will return multiple search results, as shown in the examples below:

{% with id="search_1", url="app/search_1.png", maxheight="240px", description="Search results" %}
{% include 'img.html' %}
{% endwith %}

{% with id="search_2", url="app/search_2.png", maxheight="240px", description="Search results" %}
{% include 'img.html' %}
{% endwith %}

### Parts

Select the *Parts* icon to open the [parts display](./part.md). This initially displays the top-level part category, showing information for parts and sub categories.

### Starred Parts

Selected the *Starred Parts* icon to show a list of parts you have personally marked as your "favorite" parts.

### Stock

Select the *Stock* icon to open the [stock display](./stock.md). This initially displays the top-level stock category, showing information for stock items and sub locations.

### Purchase Orders

Select the *Purchase Orders* icon to open the [purchase orders display](./po.md). This shows a list of currently outstanding purchase orders, allowing line items to be received into stock.

### Settings

Select the *Settings* icon to open the [settings display](./settings.md)

## Drawer Menu

The *Drawer Menu* is a quick-access menu which is accessible from most display screens:

{% with id="drawer", url="app/drawer.png", maxheight="240px", description="Open drawer menu" %}
{% include 'img.html' %}
{% endwith %}

The *Drawer Menu* can be accessed in the following ways:

- From the *Home Screen* select the *Drawer* icon in the top-left corner of the screen
- From any other screen, long-press the *Back* button in the top-left corner of the screen

!!! tip "Long Press Menu"
    Performing a "long press" on the *back* button will provide quick access to the drawer menu from any view

The *Drawer Menu* provides instant access to the following actions:

### InvenTree

Select *InvenTree* to navigate to the [home screen](#home-screen).

### Scan Barcode

Select *Scan Barcode* to open the barcode scanner, and scan an InvenTree stock item or location to instantly jump to the relevant view. Refer to the [barcode documentation](./barcode.md) for more information.

### Search

Select *Search* to open a global search screen.

### Settings

Select *Settings* to navigate to the app [settings](./settings.md) menu.

