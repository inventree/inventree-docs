---
title: What's New
---

## What's New

### Release 0.1.4

#### Build Management System

Improved build management system:

- Partial builds
- Batch tracking

!!! TODO
	More information to come soon

#### Related Parts
##### Definition

Related Part denotes a relationship between two parts, when users want to show their usage is "related" to another part or simply emphasize a link between two parts.

##### Implementation

- New PartRelated model/table to store relationships between parts (requires migration)
- New Related tab shown in Part detail page
- Ability to add relationships between parts through both main and admin interfaces
- Can only manage relationship if user has "change" permission on Part ruleset

##### Example View

{% with id="related_parts_example", url="https://user-images.githubusercontent.com/4020546/96306587-8f2d0b80-0fc5-11eb-8fdb-20cb2dabfcc6.png", description="Related Parts Example View" %}
{% include 'img.html' %}
{% endwith %}

#### InvenTree "Global" Settings

Global settings control the default value of fields across the entire web interface, for all-users.

!!! TODO
	More information to come soon

Also, dedicated settings sections were added for:

- Category
- Build
- Purchase Order
- Sales Order

For Category section, read [Category Parameter Templates](#category-parameter-templates)

Other section allows to set the prefix of build, puchase and sales orders.

#### Category Parameter Templates

Added support for configuring parameter templates defined by categories.

##### Features

* User can now setup a list of parameter templates for each (or all) part category(ies) in InvenTree settings
* During part creation, part parameters are automatically created using the list of parameter templates from the parent category it belongs to (if option is enabled)

##### Screenshots

* Select category

{% with id="related_parts_example", url="https://user-images.githubusercontent.com/4020546/98037571-c2ef9a00-1de9-11eb-96a1-542b18cdda7e.png", description="Select Category" %}
{% include 'img.html' %}
{% endwith %}

* Add parameter template

{% with id="related_parts_example", url="https://user-images.githubusercontent.com/4020546/98145792-1cfb6880-1e99-11eb-82eb-c96d1ba9541a.png", description="Add Parameter Template" %}
{% include 'img.html' %}
{% endwith %}

* Control global behavior within part settings

{% with id="related_parts_example", url="https://user-images.githubusercontent.com/4020546/98130420-39db7000-1e88-11eb-9ca0-78370e19ccdd.png", description="Global Settings For Category Templates" %}
{% include 'img.html' %}
{% endwith %}

* Control instance behavior during part creation

{% with id="related_parts_example", url="https://user-images.githubusercontent.com/4020546/98130496-4f509a00-1e88-11eb-9239-4dc215cbc620.png", description="Instance Settings For Category Templates" %}
{% include 'img.html' %}
{% endwith %}


#### Currency Support

!!! TODO
	More information to come soon
