---
title: Manufacturers
---

## Manufacturers

A manufacturer is an external **producer** of parts and raw materials.

To access the manufacturer page, click on the "Buy" navigation tab and click on "Manufacturers" option in the dropdown list.

!!! warning
	**Viewing**, **adding**, **editing** and **deleting** manufacturers require the corresponding [Purchase Orders user permissions](../../admin/permissions)

### Add Manufacturer

Once the manufacturer page is loaded, click on the "<span class='fas fa-plus-circle'></span> New Manufacturer" button: the "Create new Manufacturer" form opens. Fill-in the manufacturer informations (`Company name` and `Company description` are required) then click on the "Submit" button.

!!! note "Manufacturer vs Supplier"
	In the case the manufacturer sells directly to customers, you may want to enable the checkbox `is supplier` before submitting the form (you can also enable it later on). Purchase orders rely exclusively on [supplier parts](../supplier#supplier-parts), therefore the manufacturer will need to be set as a supplier too.

### Edit Manufacturer

To edit a manufacturer, click on its name in the list of manufacturers.

After the manufacturer details are loaded, click on the <span class='fas fa-edit'></span> icon under the manufacturer name. Edit the manufacturer information then click on the "Submit" button.

### Delete Manufacturer

!!! warning
	All manufacturer parts for this manufacturer will also be deleted!

To delete a manufacturer, click on its name in the list of manufacturers.

After the manufacturer details are loaded, click on the <span class='fas fa-trash-alt'></span> icon under the manufacturer name. Review the list of manufacturer parts to be deleted in consequence of deleting this manufacturer. Confirm the deletion using the checkbox then click on the "Submit" button.

## Manufacturer Parts

Manufacturer parts are connected to the manufacturer they belong to. Most importantly, they are **linked** to a supplier part. In other words, manufacturer parts do **not** exist without a corresponding supplier part and they are the actual "items" sold by a supplier.

!!! warning
	**Viewing**, **adding**, **editing** and **deleting** manufacturer parts require the corresponding [Purchase Orders user permissions](../../admin/permissions)

### Add Manufacturer Part

Adding a manufacturer part is the same process as [adding a supplier part](../supplier#add-supplier-part).

### Edit Manufacturer Part

Editing a manufacturer part is the same process as [editing a supplier part](../supplier#edit-supplier-part).

### Delete Manufacturer Part

Deleting a manufacturer part is the same process as [deleting a supplier part](../supplier#delete-supplier-part).
