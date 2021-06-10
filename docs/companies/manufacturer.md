---
title: Manufacturers
---

## Manufacturers

A manufacturer is an external **producer** of parts and raw materials.

To access the manufacturer page, click on the "Buy" navigation tab and click on "Manufacturers" option in the dropdown list.

!!! warning
	**Viewing**, **adding**, **editing** and **deleting** manufacturers require the corresponding [Purchase Orders user permissions](../admin/permissions.md)

### Add Manufacturer

Once the manufacturer page is loaded, click on the "<span class='fas fa-plus-circle'></span> New Manufacturer" button: the "Create new Manufacturer" form opens. Fill-in the manufacturer informations (`Company name` and `Company description` are required) then click on the "Submit" button.

!!! info "Manufacturer vs Supplier"
	In the case the manufacturer sells directly to customers, you may want to enable the checkbox `is supplier` before submitting the form (you can also enable it later on). Purchase orders rely exclusively on [supplier parts](./supplier.md#supplier-parts), therefore the manufacturer will need to be set as a supplier too.

### Edit Manufacturer

To edit a manufacturer, click on its name in the list of manufacturers.

After the manufacturer details are loaded, click on the <span class='fas fa-edit'></span> icon under the manufacturer name. Edit the manufacturer information then click on the "Submit" button.

### Delete Manufacturer

!!! warning
	All manufacturer parts for this manufacturer will also be deleted!

To delete a manufacturer, click on its name in the list of manufacturers.

After the manufacturer details are loaded, click on the <span class='fas fa-trash-alt'></span> icon under the manufacturer name. Review the list of manufacturer parts to be deleted in consequence of deleting this manufacturer. Confirm the deletion using the checkbox then click on the "Submit" button.

## Manufacturer Parts

Manufacturer parts are linked to a manufacturer and defined as manufacturable items.

!!! warning
	**Viewing**, **adding**, **editing** and **deleting** manufacturer parts require the corresponding [Purchase Orders user permissions](../admin/permissions.md)

### Add Manufacturer Part

To create a manufacturer part, you have the following options:

* either navigate to a Part detail page then click on the "Manufacturers" tab
* or navigate to a Manufacturer detail page then click on the "Manufactured Parts" tab.

Whichever you pick, click on the "<span class='fas fa-plus-circle'></span> New Manufacturer Part" button to load the "Create New Manufacturer Part" form. Fill out the form with the manufacturer part information then click on the "Submit" button.

### Edit Manufacturer Part

To edit a manufacturer part, first access the manufacturer part detail page with one of the following options:

* either navigate to a Part detail page, click on the "Manufacturers" tab then click on the "MPN" link
* or navigate to a Manufacturer detail page, click on the "Manufactured Parts" tab then click on the "MPN" link.

After the manufacturer part details are loaded, click on the <span class='fas fa-edit'></span> icon next to the manufacturer part image. Edit the manufacturer part information then click on the "Submit" button.

### Delete Manufacturer Part

To delete a manufacturer part, first access the manufacturer part detail page like in the [Edit Manufacturer Part](#edit-manufacturer-part) section.

After the manufacturer part details are loaded, click on the <span class='fas fa-trash-alt'></span> icon next to the manufacturer part image. Review the the information for the manufacturer part to be deleted, confirm the deletion using the checkbox then click on the "Submit" button.
