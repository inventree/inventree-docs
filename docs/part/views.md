---
title: Part Views
---

The Part information page organizes part data into sections, displayed as tabs.

## Part Details

The *Details* tab shows a detail view which provides information about the particular part.

{% with id="part_overview", url="part/part_overview.png", description="Part details" %}
{% include 'img.html' %}
{% endwith %}

A Part is defined in the system by the following parameters:

### Part Definition Fields

**Part Name** - The Part name is a simple (unique) text label

**Description** - Longer form text field describing the Part

**Internal Part Number (IPN)** - A special code which can be used to link a part to a numbering system. The IPN field is not required, but may be useful where a part numbering system has been defined.

**Revision** - An optional revision code denoting the particular version for the part. Used when there are multiple revisions of the same master part object.

**Category** - The Part category is used to group or arrange parts, as per the particular requirements of the user. Categories are arranged in a 'tree' where each category may have multiple child categories.

**External Link** - An external URL field is provided to link to an external page. This could be useful the part has extra documentation located on an external server.

**Units** - Units of measure (UoM) for this Part. The default is 'pcs'

## Parameters

Parts can have multiple defined [parameters](../parameter).

## Variants

If a part is a *Template Part* then the *Variants* tab will be visible.

[Read about Part templates](../template)

## Stock

The *Stock* tab shows all the stock items for the selected *Part*. The user can quickly determine how many parts are in stock, where they are located, and the status of each *Stock Item*.

{% with id="part_stock", url="part/part_stock.png", description="Part Stock" %}
{% include 'img.html' %}
{% endwith %}

### Functions

The following functions are available from the *Part Stock* view.

#### Export

Exports the stocktake data for the selected Part. Launches a dialog to select export options, and then downloads a file containing data for all stock items for this Part.

#### New Stock Item

Launches a dialog to create a new *Stock Item* for the selected *Part*.

#### Stock Actions

If stock items are selected in the table, stock actions are enabled via the drop-down menu.

## Allocations

The *Allocated* tab displays how many units of this part have been allocated to pending build orders and/or sales orders. This tab is only visible if the Part is a *component* (meaning it can be used to make assemblies), or it is *salable* (meaning it can be sold to customers).

## BOM

The *BOM* tab displays the [Bill of Materials](../../build/bom) - a list of sub-components used to build an assembly. Each row in the BOM specifies a quantity of another Part which is required to build the assembly. This tab is only visible if the Part is an *assembly* (meaning it can be build from other parts).

## Build Orders

The *Build Orders* tab shows a list of the builds for this part. It provides a view for important build information like quantity, status, creation and completion dates.

## Used In

The *Used In* tab displays a list of other parts that this part is used to make. This tab is only visible if the Part is a *component*.

## Suppliers

The *Suppliers* tab displays all the *Supplier Parts* for the selected *Part*. 

This tab is only visible if the *Part* is designated as *Purchaseable*.

{% with id="part_suppliers", url="part/part_suppliers.png", description="Part Suppliers" %}
{% include 'img.html' %}
{% endwith %}

## Purchase Orders

The *Part Purchase Orders* tab lists all the Purchase Orders against the selected part.

This tab is only displayed if the part is marked as *Purchaseable*.

## Sales Orders

The *Sales Orders* tab shows a list of the sales orders for this part. It provides a view for important sales order information like customer, status, creation and shipment dates.

## Tests

If a part is marked as *trackable*, the user can define tests which must be performed on any stock items which are instances of this part. [Read more about testing](../test).

## Attachments

The *Part Attachments* tab displays file attachments associated with the selected *Part*. Multiple file attachements (such as datasheets) can be uploaded for each *Part*.

## Notes

A part may have notes attached, which support markdown formatting.