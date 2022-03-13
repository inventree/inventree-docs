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

#### Build Order

In addition to the default report context variables, the following context variables are made available to the build order report template for rendering:

| Variable | Description |
| --- | --- |
| build | The [Build](./context_variables.md#build) object the report is being generated against |
| part | The [Part](./context_variables.md#part) object that the build references |
| reference | The build order reference string |
| quantity | Build order quantity |

##### Build 

| Variable | Description |
| --- | --- |
| part | The [Part](./context_variables.md#part) to be built (from component BOM items) |
| reference | Build order reference (required, must be unique) |
| title | Brief title describing the build (required) |
| quantity | Number of units to be built |
| parent | Reference to a [Build](./context_variables.md#build) object for which this Build is required | 
| sales_order | References to a [Sales Order](./context_variables.md#salesorder) object for which this [Build](./context_variables.md#build) is required (e.g. the output of this build will be used to fulfil a sales order) |
| take_from | [StockLocation](./context_variables.md#stocklocation) to take stock from to make this build (if blank, can take from anywhere) |
| status | Build status code |
| batch | Batch code transferred to build parts (optional) |
| creation_date | Date the build was created (auto) |
| target_date | Date the build will be overdue |
| completion_date | Date the build was completed (or, if incomplete, the expected date of completion) |
| link | External URL for extra information | 
| notes | Text notes |
| completed_by | User that completed the build |
| issued_by | User that issued the build |
| responsible | User (or group) responsible for completing the build |

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

!!! incomplete "TODO"
    This section requires further work

#### StockItem

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

#### StockLocation

| Variable | Description |
|----------|-------------|
| barcode | Brief payload data (e.g. for labels) |
| item_count | Simply returns the number of stock items in this location. | 

### Suppliers

!!! incomplete "TODO"
    This section requires further work

#### Supplier

| Variable | Description |
|----------|-------------|

#### SupplierPart

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

#### PurchaseOrder
| Variable | Description |
|----------|-------------|
| description | The order description |
| lines | The lines in the Purchase Order |
| order | The order object itself |
| reference | The reference number |
| supplier | The supplier for this Purchase Order |
| prefix | Purchase Order reference prefix |
| title | The title of the order |


#### SalesOrder

!!! incomplete "TODO"
    This section requires further work

| Variable | Description |
|----------|-------------|
| customer | An object with information about the customer |
| description | The order description |
| lines | The lines in the Sales Order |
| order | The order object itself |
| prefix | Purchase Order reference prefix |
| reference | The reference number |
| title | The title of the order |
