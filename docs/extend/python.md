---
title: Python Interface
---

## Python Module

A [Python module](https://github.com/inventree/inventree-python) is provided for rapid development of third party scripts or applications using the REST API. The python module handles authentication and API transactions, providing an extremely clean interface for interacting with and manipulating database data.

### Features

- Automatic authentication management using token-based authentication
- Pythonic data access
- Native file uploads
- Powerful functions for accessing related model data

### Installation

The inventree python interface can be easily installed via the [PIP package manager](https://pypi.org/project/inventree/):

```
pip3 install inventree
```

!!! tip "Upgrading"
    To upgrade to the latest version, run `pip install --upgrade inventree`

Alternatively, it can downloaded and installed from source, from [GitHub](https://github.com/inventree/inventree-python).

### Authentication

Authentication against an InvenTree server is simple:

#### Basic Auth

Connect using your username/password as follows:

```python
from inventree.api import InvenTreeAPI

SERVER_ADDRESS = 'http://127.0.0.1:8000'
MY_USERNAME = 'not_my_real_username'
MY_PASSWORD = 'not_my_real_password'

api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME, password=MY_PASSWORD)
```

#### Token Auth

Alternatively, if you already have an access token:

```python
api = InvenTreeAPI(SERVER_ADDRESS, token=MY_TOKEN)
```

#### Environment Variables

Authentication variables can also be set using environment variables:

- `INVENTREE_API_HOST`
- `INVENTREE_API_USERNAME`
- `INVENTREE_API_PASSWORD`
- `INVENTREE_API_TOKEN`

And simply connect as follows:

```python
api = InvenTreeAPI()
```


### Retrieving Data

Once a connection is established to the InvenTree server, querying individual items is simple.

#### Single Item

If the primary-key of an object is already known, retrieving it from the database is performed as follows:

```python
from inventree.part import PartCategory

category = PartCatgory(api, 10)
```

#### Multiple Items

Database items can be queried by using the `list` method for the given class. Note that arbitrary filter parameters can be applied (as specified by the [InvenTree API](./api.md)) to filter the returned results.

```python
from inventree.part import Part
from inventree.stock import StockItem

parts = Part.list(api, category=10, assembly=True)
items = StockItem.list(api, location=4, part=24)
```

The `items` variable above provides a list of `StockItem` objects.

### Item Methods

Once an object has been retrieved from the database, its related objects can be returned with the provided helper methods:

```python
part = Part(api, 25)
stock_items = part.getStockItems()
```

Some classes also have helper functions for performing certain actions, such as uploading file attachments or test results:

```python
stock_item = StockItem(api, 1001)
stock_item.uploadTestResult("Firmware", True, value="0x12345678", attachment="device_firmware.bin")
```

### Examples

#### Creating New Items

Use the `create` method to add new items to the database:

```python
from inventree.part import Part, PartCategory
from inventree.stock import StockItem

## Create a new PartCategory object,
## underneath the existing category with pk 7. Leave the parent empty fpr a top level category
furniture = PartCategory.create(api, {
    'name': 'Furniture',
    'description': 'Chairs, tables, etc',
    'parent': 7,
})

## Create a new Part
## Use the pk (primary-key) of the newly created category
couch = Part.create(api, {
    'name': 'Couch',
    'description': 'Long thing for sitting on',
    'category': furniture.pk,
    'active': True,
    'virtual': False,
    ## Note - You do not have to fill out *all* fields
})
```

#### Adding Parameters

Each [part](../part/part.md) can have multiple [parameters](../part/parameter.md). For the example of the sofa (above) *length* and *weight* make sense. Each parameter has a parameter template that combines the parameter name with a unit. So we first have to create the parameter templates and afterwards add the parameter values to the sofa.

```python
from inventree.part import Parameter
from inventree.part import ParameterTemplate

LengthTemplate = ParameterTemplate.create(api, { 'name' : 'Length', 'units' : 'Meters' })
WeightTemplate = ParameterTemplate.create(api, { 'name' : 'Weight', 'units' : 'kg' })

ParameterLength = Parameter.create(api, { 'part': couch.pk, 'template': LengthTemplate.pk, 'data' : 2 })
ParameterWeight = Parameter.create(api, { 'part': couch.pk, 'template': WeightTemplate.pk, 'data' : 60 })
```
These parameter templates need to be defined only once and can be used for all other parts. Lets finally add a picture.

```python
couch.upload_image('my_nice_couch.jpg')
```

#### Adding Location Data

If we have several sofas on stock we need to know there we have stored them. So let’s add stock locations to the part. Stock locations can be organized in a hierarchical manner e.g. boxes in shelves in aisles in rooms. So each location can have a parent. Let’s assume we have 10 sofas in box 12 and 3 sofas in box 13 located in shelve 43 aisle 3. First we have to create the locations, afterwards we can put the sofas inside.

```python

from inventree.stock import StockLocation
from inventree.stock import StockItem

...

## Create the stock locations. Leave the parent empty for top level hierarchy
Aisle3 = StockLocation.create(api, {'name':'Aisle 3','description':'Aisle for sofas','parent':''})
Shelve43 = StockLocation.create(api, {'name':'Shelve 43','description':'Shelve for sofas','parent':Aisle3.pk})
Box12 = StockLocation.create(api, {'name':'Box 12','description':'green box','parent':Shelve43.pk})
Box13 = StockLocation.create(api, {'name':'Box 13','description':'red box','parent':Shelve43.pk})

## Now fill them with items
Id1 = StockItem.create(api, { 'part': sofa.pk, 'quantity': 10, 'notes': 'new ones', 'location': Box12.pk, ‘status’:10 })
Id2 = StockItem.create(api, { 'part': sofa.pk, 'quantity': 3, 'notes': 'old ones', 'location': Box13.pk, ‘status’:55 })

```
Please recognize the different status flags. 10 means OK, 55 means damaged. We have the following choices:

* 10: OK
* 50: Attention needed
* 55: Damaged
* 60: Destroyed
* 65: Rejected
* 70: Lost
* 85: Returned

#### Adding Manufacturers and Supplier

We can add manufacturers and suppliers to parts. We first need to create two companies, ACME (manufacturer) and X-Store (supplier).

```python
from inventree.company import Company

...

acme = Company.create(api, {
    'name' : 'ACME',
    'description':'A Company that makes everything',
    'website':'https://www.acme.bla',
    'is_customer':0,
    'is_manufacturer':1,
    'is_supplier':0
})
xstore = Company.create(api, {
    'name' : 'X-Store',
    'description':'A really cool online store',
    'website':'https://www.xst.bla',
    'is_customer':0,
    'is_manufacturer':0,
    'is_supplier':1
})
```

Please recognize the different flag settings for is_supplier and is_manufacturer. Now lets add those to our couch:

```python
from inventree.company import SupplierPart

...

SupplierPart.create(api,{
    'part':couch.pk,
    'supplier':xstore.pk,
    'SKU':'some_code',
    'link':'https://www.xst.bla/products/stock?...'
})
SupplierPart.create(api,{
    'part':couch.pk,
    'manufacturer':acme.pk,
    'MPN':'Part code of the manufacturer'
})

```

#### Upload Attachments

We have the possibility to upload attachments against a particular Part. We can use pdf for documents but also other files like 3D drawings or pictures. To do so we add the following commands:

```python
from inventree.part import PartAttachment

# The ID of the Part to attach the files to
part_id = 47

PartAttachment.upload(api, part_id, 'manual.pdf', comment='Datasheet')
PartAttachment.upload(api, part_id, 'sofa.dxf', comment='Drawing')
```

Alternatively, we can upload an attachment directly against the `Part` instance:

```python
from inventree.part import Part

part = Part(api, pk=47)

part.uploadAttachment('data.txt', comment='A data file')
```

### Further Reading

The [InvenTree Python Interface](https://github.com/inventree/inventree-python) is open source, and well documented. The best way to learn is to read through the source code and try for yourself!
