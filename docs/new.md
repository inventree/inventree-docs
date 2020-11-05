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

#### InvenTree Settings
##### Dedicated sections

Dedicated sections were added for:

- Category
- Build
- Purchase Order
- Sales Order

!!! TODO
	More information to come soon

##### Category Parameter Templates

Added support for configuring parameter templates defined by categories.

!!! TODO
	More information to come soon
