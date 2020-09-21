---
title: Python Interface
layout: page
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

## Create a new PartCategory object,
## underneath the existing category with pk 7
furniture = PartCategory.create(api, {
    'name': 'Furniture',
    'description': 'Chairs, tables, etc',
    parent, 7
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

## Create a new StockItem
item = StockItem.create(api, {
    'part': couch.pk,
    'quantity': 5,
    'notes': 'A stack of couches',
    location: 10,  ## PK of a StockLocation already in the database...
})

```