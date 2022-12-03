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
 
- **IPN_regex:** Regular expression that filter the result according to a match with the IPN (string)
- **limit:** Number of results returned (int)
- ...

**returns:** A list of all parts in the database that match the filter criteria given in the optional arguments.

If no optional arguments are given, all parts returned. 

### create

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
- **name:** Name of the part. This is also used as URL and cannot contain blank spaces and hashes (string)  
- **description:** Description of the part (string)  
- **link:** An URL to further information (string)  
- **category:** the primary key of the category where the part will be put in. The category must exist. Otherwise create will fail. (int)  

**returns:** Handle of the created part

### Get a specific part

```python
parthandle=Part(api, pk=x)
```  

- **api:** Inventree api
- **x** Primary kex of the part to get

**returns:** Handle of the part with the requested primary key


The handle of a part can be used for further actions that are described in the following section. 

#### delete
```python
parthandle.delete()
```  

This deletes the part from the database. It also deletes all related attachments. A part cannot 
be deleted when it is active or has part relationships to other parts. These must be deleted before
and the part needs to be set to inactive. 

#### getCategory
```python
parthandle.getCategory()
```  

**returns:** Category object where the part is in

#### is_valid
```python
parthandle.is_valid()
```  
**returns:** Boolean: True if the part is valid, false otherwise 

#### uploadAttachment
Upload attachments like datasheets to the database. You can upload any file up to a limit of...
```python
parthandle.uploadAttachment(file, comment)
```  
- **file:** Filename including path name (string)
- **comment:** Comment for the attachment (string)

**returns:**

#### uploadImage

```python
parthandle.uploadImage(file)
```
- **file:** Filename of the picture including path name (string)

**returns:**

#### save
```python
parthandle.save(data={'key':'value',...)
```

This function changes attributes of the part and saves changes to the database. The available keys can be found in parthandle._data. 
The function can be called without any arguments just to save the data. 

#### _data

```python
parthandle._data
```
**returns:** Dict with all data of the part (dict)

The data can be modified and saved afterwards using the save() method. The following example
will set a part to inactive: 

```python
parthandle._data['active']=False
parthandle.save()
# or
parthandle.save(data={'active':False})
```

#### pk

```python
parthandle.pk
```
**returns:** Primary key of the part (int)

#### uploadImage

```python
parthandle.uploadImage(file)
```
- **file:** Filename of the picture including path name (string)


## Supplier Parts
```python
from inventree.company import SupplierPart
SupplierPart.create(api,{'part':ppk,'supplier':spk,'SKU':Partnumber,'link':Supplierlink})
```
- **api:** Inventree api handle
- **ppk:** Primary key of the part where the supplier part will be added (int)
- **spk:** Primary key of the supplier company (int)
- **Partnumber:** Partnumber or name of the part at the supplier (string)
- **Supplierlink:** URL to the part at the website of the supplier (string)
  
**returns:** Handle of the created supplierpart

## Supplier Part Price Breaks
```python
from inventree.company import SupplierPriceBreak
SupplierPriceBreak.create(api,{'part':spk,'price':Price,'quantity':Quantity, 'price_currency':Currency})
```
- **api:** Inventree api handle
- **spk:** Primary key of the supplier part where the price break will be added (int)
- **Price:** Price of the part up to the given quantity (float) 
- **Quantity:** Quantity of parts for this price (int)
- **Currency:** Currency of the price. The available currencies are stored in Inventree (string)
  
**returns:** Handle of the created pricebreak

