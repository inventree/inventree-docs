---
title: Context Variables
---

## Context Variables 

### Report

!!! info "Specific Report Context"
    Specific report types may have additional context variables, see below.

Each report has access to a number of context variables by default. The following context variables are provided to every report template:

| Variable | Description |
| --- | --- |
| date | Current date, represented as a Python datetime.date object |
| datetime | Current datetime, represented as a Python datetime object |
| default_page_size | InvenTree default page size variable |
| report_name | Name of the report template |
| report_description | Description of the report template |
| report_revision | Revision of the report template |
| request | Django request object |
| user | User who made the request to render the template |

#### Label

Certain types of labels have different context variables then other labels.

##### Stock Item Label

The following variables are made available to the StockItem label template:

| Variable | Description |
| -------- | ----------- |
| item | The [StockItem](./context_variables.md#stockitem) object itself |
| part | The [Part](./context_variables.md#part) object which is referenced by the [StockItem](./context_variables.md#stockitem) object |
| name | The `name` field of the associated Part object | 
| ipn | The `IPN` field of the associated Part object |
| revision | The `revision` field of the associated Part object |
| quantity | The `quantity` field of the StockItem object |
| serial | The `serial` field of the StockItem object |
| uid | The `uid` field of the StockItem object |
| tests | Dict object of TestResult data associated with the StockItem |
| parameters | Dict object containing the parameters associated with the base Part |


##### Stock Location Label

The following variables are made available to the StockLocation label template:

| Variable | Description |
| -------- | ----------- |
| location | The [StockLocation](./context_variables.md#stocklocation) object itself |

### Parts

!!! incomplete "TODO"
    This section requires further work

#### Part
Each part object has access to a lot of context variables about the part. The following context variables are provided when accessing a `Part` object:

| Variable | Description |
|----------|-------------|
| name | Brief name for this part |
| full_name | Full name for this part (including IPN, if not null and including variant, if not null) |
| variant | Optional variant number for this part - Must be unique for the part name
| category | The [PartCategory](./context_variables.md#part-category) object to which this part belongs
| description | Longer form description of the part
| keywords | Optional keywords for improving part search results
| IPN | Internal part number (optional)
| revision | Part revision
| is_template | If True, this part is a 'template' part
| link | Link to an external page with more information about this part (e.g. internal Wiki)
| image | Image of this part
| default_location | The default [StockLocation](./context_variables.md#stocklocation) object where the item is normally stored (may be null)
| default_supplier | The default [SupplierPart](./context_variables.md#supplierpart) which should be used to procure and stock this part
| default_expiry | The default expiry duration for any StockItem instances of this part
| minimum_stock | Minimum preferred quantity to keep in stock
| units | Units of measure for this part (default='pcs')
| salable | Can this part be sold to customers?
| assembly | Can this part be build from other parts?
| component | Can this part be used to make other parts?
| purchaseable | Can this part be purchased from suppliers?
| trackable | Trackable parts can have unique serial numbers assigned, etc, etc
| active | Is this part active? Parts are deactivated instead of being deleted
| virtual | Is this part "virtual"? e.g. a software product or similar
| notes | Additional notes field for this part
| creation_date | Date that this part was added to the database
| creation_user | User who added this part to the database
| responsible | User who is responsible for this part (optional)
| starred | Wether the part is starred or not |
| disabled | Wether the part is disabled or not |
| total_stock | The total amount in stock |
| quantity_being_built | The amount being built |
| required_build_order_quantity | The amount required for build orders |
| allocated_build_order_quantity | The amount allocated for build orders |
| build_order_allocations | Query set with all build order allocations for that part |
| required_sales_order_quantity | The amount required for sales orders |
| allocated_sales_order_quantity | The amount allocated for sales orders |
| available | Wether the part is available or not | 
| on_order | The amount that are on order |
| required | The total amount required for build orders and sales orders |
| allocated | The total amount allocated for build orders and sales orders |

#### Part Category

| Variable | Description |
|----------|-------------|
| name | Name of this category |
| parent | Parent category |
| default_location | Default [StockLocation](./context_variables.md#stocklocation) object for parts in this category or child categories |
| default_keywords | Default keywords for parts created in this category |

### Stock

#### Stock Item

| Variable | Description |
|----------|-------------|
| parent | Link to another [StockItem](./context_variables.md#stockitem) from which this StockItem was created |
| uid | Field containing a unique-id which is mapped to a third-party identifier (e.g. a barcode) |
| part | Link to the master abstract [Part](./context_variables.md#part) that this [StockItem](./context_variables.md#stockitem) is an instance of |
| supplier_part | Link to a specific [SupplierPart](./context_variables.md#supplierpart) (optional) |
| location | The [StockLocation](./context_variables.md#stocklocation) Where this [StockItem](./context_variables.md#stockitem) is located |
| quantity | Number of stocked units |
| batch | Batch number for this [StockItem](./context_variables.md#stockitem) |
| serial | Unique serial number for this [StockItem](./context_variables.md#stockitem) |
| link | Optional URL to link to external resource |
| updated | Date that this stock item was last updated (auto) |
| expiry_date | Expiry date of the [StockItem](./context_variables.md#stockitem) (optional) |
| stocktake_date | Date of last stocktake for this item |
| stocktake_user | User that performed the most recent stocktake |
| review_needed | Flag if [StockItem](./context_variables.md#stockitem) needs review |
| delete_on_deplete | If True, [StockItem](./context_variables.md#stockitem) will be deleted when the stock level gets to zero |
| status | Status of this [StockItem](./context_variables.md#stockitem) (ref: InvenTree.status_codes.StockStatus) |
| notes | Extra notes field |
| build | Link to a Build (if this stock item was created from a build) |
| is_building | Boolean field indicating if this stock item is currently being built (or is "in production") |
| purchase_order | Link to a [PurchaseOrder](./context_variables.md#purchaseorder) (if this stock item was created from a PurchaseOrder) |
| infinite | If True this [StockItem](./context_variables.md#stockitem) can never be exhausted |
| sales_order | Link to a [SalesOrder](./context_variables.md#salesorder) object (if the StockItem has been assigned to a SalesOrder) |
| purchase_price | The unit purchase price for this [StockItem](./context_variables.md#stockitem) - this is the unit price at time of purchase (if this item was purchased from an external supplier) |
| packaging | Description of how the StockItem is packaged (e.g. "reel", "loose", "tape" etc) |

#### Stock Location

| Variable | Description |
|----------|-------------|
| barcode | Brief payload data (e.g. for labels). Example: {"stocklocation": 826} where 826 is the primary key|
| description | The description of the location  |
| icon | The name of the icon if set, e.g. fas fa-warehouse |
| item_count | Simply returns the number of stock items in this location | 
| name | The name of the location. This is only the name of this location, not the path | 
| owner | The owner of the location if it has one. The owner can only be assigned in the admin interface | 
| parent | The parent location. Returns None if it is already the top most one | 
| path | A queryset of locations that contains the hierarchy starting from the top most parent | 
| path_string | A string that contains all names of the path separated by slashes e.g. A/B/C | 
| structural | True if the location is structural | 

### Suppliers

#### Supplier

| Variable | Description |
|----------|-------------|
| name | Name of the company |
| description | Longer form description |
| website | URL for the company website |
| address | Postal address |
| contact | Contace Name |
| phone | Contact phone number |
| email | Contact email address |
| link | A second econdary URL to the company (Actually only accessible in the admin interface) |
| notes | Extra notes about the company (Actually only accessible in the admin interface) |
| is_customer | Boolean value, is this company a customer |
| is_supplier | Boolean value, is this company a supplier |
| is_manufacturer | Boolean value, is this company a manufacturer |
| currency_code | Default currency for the company |
| parts | Query set with all parts that the company supplies |

#### Supplier Part

| Variable | Description |
|----------|-------------|
| part | Link to the master Part (Obsolete) |
| source_item | The sourcing [StockItem](./context_variables.md#stockitem) linked to this [SupplierPart](./context_variables.md#supplierpart) instance |
| supplier | [Supplier](./context_variables.md#supplier) that supplies this part | 
| SKU | Stock keeping unit (supplier part number) | 
| link | Link to external website for this supplier part | 
| description | Descriptive notes field | 
| note | Longer form note field | 
| base_cost | Base charge added to order independent of quantity e.g. "Reeling Fee" |
| multiple | Multiple that the part is provided in |
| lead_time | Supplier lead time |
| packaging | packaging that the part is supplied in, e.g. "Reel" |
| pretty_name | The IPN, supplier name, supplier SKU and (if not null) manufacturer string joined by `|`. Ex. `P00037 | Company | 000021` |
| unit_pricing | The price for one unit. |
| price_breaks | Return the associated price breaks in the correct order |
| has_price_breaks | Wether this [SupplierPart](./context_variables.md#supplierpart) has price breaks |
| manufacturer_string | Format a MPN string for this [SupplierPart](./context_variables.md#supplierpart). Concatenates manufacture name and part number. |

### Manufacturers

!!! incomplete "TODO"
    This section requires further work

#### Manufacturer

| Variable | Description |
|----------|-------------|

#### ManufacturerPart 

| Variable | Description |
|----------|-------------|

### Orders

!!! incomplete "TODO"
    This section requires further work

#### Purchase Order

A [Purchase Order](../buy/po.md) object has the following context variables available.

| Variable | Description |
|----------|-------------|
| description | The order description |
| lines | The lines in the Purchase Order |
| reference | The reference number |
| supplier | The supplier for this Purchase Order |

#### SalesOrder

A [Sales Order](../sell/so.md) object has the following context variables available.

| Variable | Description |
|----------|-------------|
| customer | An object with information about the customer |
| description | The order description |
| lines | The lines in the Sales Order |
| reference | The reference number |

#### Return Order

A [Return Order](../sell/return.md) object has the following context variables avaiable.

| Variable | Description |
| --- | --- |
| customer | An object with information about the customer |
| description | The order description |
| lines | The lines in the Sales Order |
| reference | The reference number |


### User

| Variable | Description |
|----------|-------------|
| username | the username of the user |
| fist_name | The first name of the user |
| last_name | The last name of the user |
| email | The email address of the user |
| pk | The primary key of the user |
