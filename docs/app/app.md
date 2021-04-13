---
title: InvenTree Mobile App
---

## InvenTree Mobile App

The InvenTree Mobile App brings stock control to your pocket. Integrating seamlessly with the [InvenTree API](../../extend/api), the app provides immediate access to inventory data without requiring physical access to a computer.

Native barcode support provides a multitude of context-sensitive stock control actions, allowing streamlined inventory management at your fingertips. The app has been optimized for speed, providing instant access to stock knowledge and handy on-site functionality.

## Download

### Android

The InvenTree App can be downloaded for Android devices via the [Play Store](https://play.google.com/store/apps/details?id=inventree.inventree_app).

### iOS

!!! missing "Not Yet Available"
    The InvenTree app is not yet available for iOS devices

## Connect to InvenTree

Use of the InvenTree app assumes that you (the user) have access to an InvenTree server.

When first running the app, no profile has been configured. A message is displayed at the bottom of the screen, indicting that a server profile needs to be configured.

{% with id="no_server", url="app/initial_home_screen.jpg", maxheight="240px", description="No server configured" %}
{% include "img.html" %}
{% endwith %}

Press on the mesage to navigate to the server selection view:

### Create Server

!!! success "Server Profiles"
    The app supports multiple server profiles, providing simple switching between different InvenTree servers and/or account profiles.

Press the <span class='fas fa-plus-circle blue'></span> button in the bottom-right corner of the screen to create a new server profile.

{% with id="add_profile", url="app/add_server_profile.jpg", maxheight="240px", description="Add server" %}
{% include 'img.html' %}
{% endwith %}

Enter the required server details:

| Parameter | Description |
| --- | --- |
| Name | Name for the server profile (can be any value, simply for reference) |
| Server | InvenTree server address (including port, if required). e.g. `http://inventree.myserver.com:8080` |
| Username | Your account username (case sensitive) |
| Password | Your account password (case sensitive) |

### Connect to Server

Once the server profile is created, you need to connect to the server. Simply short press on the server profile to connect.

Alternatively, long press on the server profile to activate the context menu, then select *Connect to Server*.

When the app successfully connects to the server, a success message is briefly displayed at the bottom of the screen. A green <span class='fas fa-check-circle green'></span> icon next to the server profile indicate that the profile is currently *selected* and also the connection was successful.

{% with id="connected", url="app/connected.jpg", maxheight="240px", description="Connected to server" %}
{% include 'img.html' %}
{% endwith %}

### Connection Failure

If (for whatever reason) the app does not successfully connect to the InvenTree server, a failure message is displayed, and a red <span class='fas fa-times-circle red'></span> icon is displayed next to the server profile.

{% with id="failed", url="app/unauthorized.jpg", maxheight="240px", description="Connection failure" %}
{% include 'img.html' %}
{% endwith %}

In this case, the error message displayed at the bottom of the screen provides context as to why the app could not successfully connect to the server.

To edit the server profile details, long press on the server profile, and select *Edit Server Profile*:

{% with id="edit", url="app/edit_server.jpg", maxheight="240px", description="Edit server profile" %}
{% include 'img.html' %}
{% endwith %}

## Drawer Menu

The *Drawer Menu* is accessible from all top-level app views, and provides quick access to important app features. To open the drawer menu, select the <span class='fas fa-bars'></span> icon in the top-left corner of the screen (where available).

{% with id="drawer", url="app/drawer.jpg", maxheight="240px", description="Open drawer menu" %}
{% include 'img.html' %}
{% endwith %}

The *Drawer Menu* provides instant access to the following views:

### InvenTree

Select *InvenTree* to navigate to the [home screen](#home-screen).

### Scan Barcode

Select *Scan Barcode* to open the barcode scanner, and scan an InvenTree stock item or location to instantly jump to the relevent view. Refer to the [barcode documentation](./barcode) for more information.

### Search

Select *Search* to open a global search screen.

### Parts

Select *Parts* to navigate to the [Parts](./parts) view.

### Stock

Select *Stock* to navigate to the [Stock](./stock) view.

### Settings

Select *Settings* to navigate to the app [settings](./settings) menu.

## Home Screen

The app *home screen* provides quick-access buttons for stock view and actions.

Additionally, the connection status of the server is displayed at the bottom of the screen.

{% with id="home", url="app/home.jpg", maxheight="240px", description="Home screen" %}
{% include 'img.html' %}
{% endwith %}