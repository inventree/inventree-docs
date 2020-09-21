---
title: Parts
layout: page
---

# Part

The *Part* is the core element of the InvenTree ecosystem. A Part object is the archetype of any stock item in your inventory. Parts are arranged in heirarchical categories which are used to organise and filter parts by function.

## Part Category 

Part categories are very flexible and can be easily arranged to match a particular user requirement. Each part category displays a list of all parts *under* that given category. This means that any part belonging to a particular category, or belonging to a sub-category, will be displayed.

Each part category also shows a list of sub-categories which exist underneath it.

{% with id="part_category", url="part/part_category.png", description="Parts are arranged in categories" %}
{% include 'img.html' %}
{% endwith %}

The category part list provides an overview of each part:

* Part name and description
* Part image thumbnail
* Part category
* Part stock level

The list of parts underneath a given category can be filtered by multiple user-configurable filters, which is especially useful when a large number of parts exist under a certain category.

Clicking on the part name links to the [*Part Detail*](/part/views) view.

