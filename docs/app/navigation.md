---
title: App Navigation
---


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

## Tab Display

Some screens provide multiple tabbed views, which are displayed at the top of the screen:

{% with id="global_nav", url="app/app_tabs.png", maxheight="240px", description="App tabs" %}
{% include 'img.html' %}
{% endwith %}

Tabs can be navigated by pressing on the text of each tab, or by scrolling the screen left or right.

## Global Actions

The *Global Action* buttons are visible on most screens, displayed in the bottom left corner of the screen:

{% with id="global_nav", url="app/app_global_navigation.png", maxheight="240px", description="Global navigation actions" %}
{% include 'img.html' %}
{% endwith %}

### Open Drawer Menu

The <span class='fas fa-list'></span> action opens the *Drawer Menu*, which is a quick-access menu for global navigation:

{% with id="drawer", url="app/drawer.png", maxheight="240px", description="Open drawer menu" %}
{% include 'img.html' %}
{% endwith %}

The *Drawer Menu* can be accessed in the following ways:

- From the *Home Screen* select the *Drawer* icon in the top-left corner of the screen
- From any other screen, long-press the *Back* button in the top-left corner of the screen

### Search

The <span class='fas fa-search'></span> action opens the [Search](#search) screen

### Scan Barcode

The <span class='fas fa-qrcode'></span> action opens the [barcode scan](./barcode.md) window, which allows quick access to the barcode scanning functionality.

## Context Actions

Within a given view, certain context actions may be available. If there are contextual actions which can be performed, they are displayed in the bottom right corner:

{% with id="drawer", url="app/context_actions.png", maxheight="240px", description="Context actions" %}
{% include 'img.html' %}
{% endwith %}

!!! tip "Barcode Actions"
    Available barcode actions are displayed in a separate context action menu 
