# API reference

## Part

### list

List all parts in the database that match certain filter criteria. 
```python
from inventree.part import Part
Part.list(api, optional arguments)
```
- **api:** Inventree api

Optional arguments:
 
- **IPN_regex:** Regular expression that filter the rasulta accorting to a match with the IPN (string)
- **limit:** Number of results returned (int)
- ...

**returns:** A ist of all parts in the database that match the filter criteria given in the optional arguments.

If no optional arguments are given, all parts returned. 

### Create

Create a part in the database.
```python
Part.create(api, {
        'name': name,
        'description': description,
        'link': link,
        'IPN': IPNs,
        'keywords': keywords,
        'category': categoryPKpk,
        'units': units,
        'active': active,
        'purchaseable': True,
        'component': True,
        'virtual': False,
        'default_expiry': time,
        'notes': comments
        })
```
- **api:** Inventree api
- **name:** Name if the part. This is also used as URL and cannot contain blank spaces and hashes (string)  

**returns:** Handle of the created part

### uploadAttachment
Upload atachments like datasheets to the database. You can upload any file up to a limit of...
```python
parthandle.uploadAttachment(file, comment)
```  
  -**file:** Filename including path name (string)
  -**comment:** Comment for the attachment (string)

**returns:**

### uploadImage

```python
parthandle.uploadImage(file)
```
-**file:** Filename of the picture including path name

**returns:**

## Supplier Parts
```python
from inventree.company import SupplierPart

SupplierPart.create(api,{'part':ppk,'supplier':spk,'SKU':Partnumber,'link':Supplierlink})
  
```
  - **api:** taInventree api handle
  - **ppk:** Primary key of the part where the supplier üart will be adddeda (int)
  - **spk:** Primary key of the supplier company (int)
  - **Partnumber:** Partnumber or name of the part at the suppplier (string)
  - **Supplierlink:** URL to the part at the website of the supplier (string)
  
**returns:** Handle of the created supplierpart

