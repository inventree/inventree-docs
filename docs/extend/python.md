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

Alternatively, it can downloaded and installed from source, from [GitHub](https://github.com/inventree/inventree-python).

### Examples

The inventree Python module is designed to be very lightweight and simple to use. Some simple examples are provided below:

#### Authentication

Authentication against an InvenTree server is simple:

```python
from inventree.api import InvenTreeAPI

SERVER_ADDRESS = 'http://127.0.0.1:8000'
MY_USERNAME = 'not_my_real_username'
MY_PASSWORD = 'not_my_real_password'

api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME, password=MY_PASSWORD)
```

Alternatively, if you already have an access token:

```python
api = InvenTreeAPI(SERVER_ADDRESS, token=MY_TOKEN)
```

#### Retrieving Individual Items

If the primary-key of an object is already known, retrieving it from the database is performed as follows:

```python
from inventree.part import PartCategory

category = PartCatgory(api, 10)
```

#### Querying / Listing Items

Database items can be queried by using the `list` method for the given class:

```python
from inventree.part import Part
from inventree.stock import StockItem

parts = Part.list(api, category=10, assembly=True)
items = StockItem.list(api, location=4, part=24)
```

Once an object has been retrieved from the database, its related objects can be returned with helper functions:

```python
part = Part(api, 25)
stock_items = part.getStockItems()
```

Some classes also have helper functions for performing certain actions, such as uploading file attachments or test results:

```python
stock_item = StockItem(api, 1001)
stock_item.uploadTestResult("Firmware", True, value="0x12345678", attachment="device_firmware.bin")
```

#### Creating New Items

```python
from inventree.part import Part, PartCategory
from inventree.stock import StockItem
from inventree.base import Parameter
from inventree.base import ParameterTemplate

## Create a new PartCategory object,
## underneath the existing category with pk 7
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

## Before we can add parameters to the couch, we neeed to create the parameter templates
## These parameter templates need to be defined only once and can be used for all other parts. 
LengthTemplate = ParameterTemplate.create(api, { 'name' : 'Length', 'units' : 'Meters' })
WeightTemplate = ParameterTemplate.create(api, { 'name' : 'Weight', 'units' : 'kg' })

## Now we create the parameters
ParameterLength = Parameter.create(api, { 'part': couch.pk, 'template': LengthTemplate.pk, 'data' : 2 })
ParameterWeight = Parameter.create(api, { 'part': couch.pk, 'template': WeightTemplate.pk, 'data' : 60 })

## Create a new StockItem
item = StockItem.create(api, {
    'part': couch.pk,
    'quantity': 5,
    'notes': 'A stack of couches',
    'location': 10,  ## PK of a StockLocation already in the database...
})
```

#### Adding manufacturers and supplier

We can add manufacturers and suppliers to parts. If we add a manufacturer, a supplier is also mandatory. So we first need to create two companies, ACME (manufacturer) and X-Store (supplier).

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
    'manufacturer':acme.pk
})
```

Supplier and manufacturer are added with just one command. The SKU is the code under which the couch is listed in the store.
