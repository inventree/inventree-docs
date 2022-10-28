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

### Further Reading

The [InvenTree Python Interface](https://github.com/inventree/inventree-python) is open source, and well documented. The best way to learn is to read through the source code and try for yourself!
