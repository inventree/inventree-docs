---
title: Sales Order
---

## Sales Orders

Sales orders allow to track which stock items are sold to customers, therefore converting stock items / inventory into externally sold items.

To access the sales order page, click on the <span class="badge inventree nav main"><span class='fas fa-truck'></span> Sell</span> navigation tab and click on <span class="badge inventree nav main"><span class='fas fa-list'></span> Sales Orders</span> option in the dropdown list.

{% with id="sales_order_list", url="sell/so_list.png", description="Sales Order List" %}
{% include "img.html" %}
{% endwith %}

### Sales Order Reference

{% with prefix="SO-", label="Sales Order" %}
{% include "reference.html" %}
{% endwith %}


### Create Sales Order

Once the sales order page is loaded, click on <span class="badge inventree add"><span class='fas fa-plus-circle'></span> New Sales Order</span> which opens the "Create Sales Order" form.

A sales order is linked to a specific customer, select one in the list of existing customers.

!!! warning
	Only companies with the "Customer" attribute enabled will be shown and can be selected

Fill out the rest of the form with the sales order information then click on <span class="badge inventree confirm">Submit</span> 

#### Add Line Items

On the sales order detail page, user can link parts to the sales order selecting the <span class="badge inventree nav side"><span class='fas fa-list-ol'></span> Line Items</span> tab then clicking on the <span class="badge inventree add"><span class='fas fa-plus-circle'></span> Add Line Item</span> button.

Once the "Add Line Item" form opens, select a part in the list.

!!! warning
    Only parts that have the "Salable" attribute enabled will be shown and can be selected

Fill out the rest of the form then click on <span class="badge inventree confirm">Submit</span> 

#### Shipments

After all line items were added to the sales order, user needs to create one or more [shipments](./shipment.md) in order to allocate stock for those parts.

In order to create a new shipment:

1. Click on the <span class="badge inventree nav side"><span class='fas fa-truck-loading'></span> Pending Shipments</span> tab
2. Click on <span class="badge inventree add"><span class='fas fa-plus-circle'></span> New Shipment</span> button, fill out the form with the shipment number (tracking number can be added but is optional) then click on <span class="badge inventree confirm">Submit</span>

Repeat the two steps above to create more shipments.

#### Allocate Stock Items

After shipments were created, user can either:

* allocate stock items for that part to the sales order (click on <span class='fas fa-sign-in-alt'></span> button)
* or create a build order for that part to cover the quantity of the sales order (click on <span class='fas fa-tools'></span> button)

During the allocation process, user is required to select the desired shipment that will contain the stock items.

#### Complete Shipment

To complete a shipment, click on the <span class="badge inventree nav side"><span class='fas fa-truck-loading'></span> Pending Shipments</span> tab then click on <span class='fas fa-truck'></span> button shown in the shipment table.

Fill out the "Complete Shipment" form then click on <span class="badge inventree confirm">Submit</span>.

To view all the completed shipment, click on the <span class="badge inventree nav side"><span class='fas fa-truck'></span> Completed Shipments</span> tab. In the completed shipments table, click on the <span class='fas fa-plus'></span> icon next to each shipment reference to see the items and quantities which were shipped.

### Complete Order

Once all items in the sales order have been shipped, click on <span class="badge inventree add"><span class='fas fa-check-circle'></span> Complete Order</span> to mark the sales order as complete.

### Cancel Order

To cancel the order, click on the <span class='fas fa-tools'></span> menu button next to the <span class="badge inventree add"><span class='fas fa-check-circle'></span> Complete Order</span> button, then click on the "<span class='fas fa-tools'></span> Cancel Order" menu option. Confirm then click on the <span class="badge inventree confirm">Submit</span> to cancel the order.
