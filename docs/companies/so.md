---
title: Sales Order
---

## Sales Orders

Sales orders allow to track which stock items are sold to customers, therefore converting stock items / inventory into externally sold items.

To access the sales order page, click on the <span class="badge inventree nav main"><span class='fas fa-truck'></span> Sell</span> navigation tab and click on <span class="badge inventree nav main"><span class='fas fa-list'></span> Sales Orders</span> option in the dropdown list.

### Create Sales Order

Once the sales order page is loaded, click on <span class="badge inventree add"><span class='fas fa-plus-circle'></span> New Sales Order</span> which opens the "Create Sales Order" form.

A sales order is linked to a specific customer, select one in the list of existing customers.

!!! warning
	Only companies with the "Customer" attribute enabled will be shown and can be selected

Fill out the rest of the form with the sales order information then click on <span class="badge inventree confirm">Submit</span> 

### Add Line Items

On the sales order detail page, user can link parts to the sales order selecting the <span class="badge inventree nav side"><span class='fas fa-list'></span> Order Items</span> tab then clicking on the <span class="badge inventree add"><span class='fas fa-plus-circle'></span> Add Line Item</span> button.

Once the "Add Line Item" form opens, select a part in the list.

!!! warning
    Only parts that have the "Salable" attribute enabled will be shown and can be selected

Fill out the rest of the form then click on <span class="badge inventree confirm">Submit</span> 

### Allocate Stock Items

After adding line item and connecting a part to the sales order, user can either:

* allocate stock items for that part to the sales order (click on <span class='fas fa-sign-in-alt'></span> button)
* or create a build order for that part to cover the quantity of the sales order (click on <span class='fas fa-tools'></span> button)

### Ship Order

After all parts and stock items have been allocated, click on the <span class='fas fa-paper-plane'></span> button on the main sales order detail panel and confirm the order has been sent.

The sales order will be marked as __shipped__ and can __not__ be edited anymore.

### Cancel Order

In the event that the order won't be shipped out, user has the option of cancelling the order instead.
To do so, simply click on the <span class='fas fa-times-circle'></span> button on the main sales order detail panel and confirm the sales order has been cancelled.
