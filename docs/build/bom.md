---
title: Bill of Materials
---

## Bill of Materials

A Bill of Materials (BOM) defines the list of component parts required to make an assembly, [create builds](./build.md) and allocate inventory.

A part which can be built from other sub components is called an *Assembly*. 

## BOM Line Items

A BOM for a particular assembly is comprised of a number (zero or more) of BOM "Line Items", each of which has the following properties:

| Property | Description |
| --- | --- |
| Part | A reference to another *Part* object which is required to build this assembly |
| Quantity | The quantity of *Part* required for the assembly |
| Reference | Optional reference field to describe the BOM Line Item, e.g. part designator |
| Overage | Estimated losses for a build. Can be expressed as absolute values (e.g. 1, 7, etc) or as a percentage (e.g. 2%) |
| Inherited | A boolean field which indicates whether this BOM Line Item will be "inherited" by BOMs for parts which are a variant (or sub-variant) of the part for which this BOM is defined. |
| Optional | A boolean field which indicates if this BOM Line Item is "optional" |
| Note | Optional note field for additional information

!!! missing "Overage"
    While the overage field exists, it is currently non-functional and has no effect on BOM operation

!!! missing "Optional"
    The Optional field is currently for indication only - it does not serve a functional purpose (yet)

### Inherited BOM Line Items

When using the InvenTree [template / variant](../part/template.md) feature, it may be useful to make use of the *inheritance* capability of BOM Line Items.

If a BOM Line Item is designed as *Inherited*, it will be automatically included in the BOM of any part which is a variant (or sub-variant) of the part for which the BOM Line Item is defined.

This is particulary useful if a template part is defined with the "common" BOM items which exist for all variants of that template.

Consider the example diagram below:

{% with id="inherited_bom", url="build/inherited_bom.png", description="Inherited BOM Line Items" %}
{% include 'img.html' %}
{% endwith %}

**Template Part A** has two BOM line items defined: *A1* and *A2*.

- *A1* is inherited by all variant parts underneath *Template Part A*
- *A2* is not inherited, and is only included in the BOM for *Template Part A*

**Variant B** has two line items:

- *A1* is inherited from parent part *A*
- *B1* is defined for part *B* (and is also defined as an inherited BOM Line Item)

**Variant C**

- *A1* inherited from *A*
- *C1* defined for *C*

**Variant D**

- *A1* inherited from *A*
- *B1* inherited from *B*
- *D1* defined for *D*

**Variant E**

- Well, you get the idea.

Note that inherited BOM Line Items only flow "downwards" in the variant inheritance chain. Parts which are higher up the variant chain cannot inherit BOM items from child parts.

!!! info "Editing Inherited Items"
    When editing an inherited BOM Line Item for a template part, the changes are automatically reflected in the BOM of any variant parts.

## BOM Creation

BOMs can be created manually, by adjusting individual line items, or by upload an existing BOM file.

### Add BOM Item

To manually add a BOM item, navigate to the part/assembly detail page then click on the "BOM" tab. On top of the tab view, click on the <span class='fas fa-edit'></span> icon then, after the page reloads, click on the <span class='fas fa-plus-circle'></span> icon.

The `Create BOM Item` form will be displayed:
{% with id="bom_add_item", url="build/bom_add_item.png", description="Create BOM Item Form" %}
{% include 'img.html' %}
{% endwith %}

Fill-out the `Quantity` (required), `Reference`, `Overage` and `Note` (optional) fields then click on <span class="badge inventree confirm">Submit</span> to add the BOM item to this part's BOM.

### Add Substitute for BOM Item

To manually add a substitute for a BOM item, click on the <span class='fas fa-exchange-alt'></span> icon in the *Actions* columns.

The `Edit BOM Item Substitutes` form will be displayed:
{% with id="bom_substitute_item", url="build/bom_substitute_item.png", description="Edit BOM Item Substitutes" %}
{% include 'img.html' %}
{% endwith %}

Select a part in the list and click on "Add Substitute" button to confirm.

### Upload BOM

Uploading a BOM to InvenTree is a three steps process:

1. upload BOM file
0. select matching InvenTree fields
0. select matching InvenTree parts.

To upload a BOM file, navigate to the part/assembly detail page then click on the "BOM" tab. On top of the tab view, click on the <span class='fas fa-edit'></span> icon then, after the page reloads, click on the <span class='fas fa-file-upload'></span> icon.

The following view will load:
{% with id="bom_upload_file", url="build/bom_upload_file.png", description="BOM Upload View" %}
{% include 'img.html' %}
{% endwith %}

#### Upload BOM File

Click on the "Choose File" button, select your BOM file when prompted then click on the "Upload File" button.

!!! info "BOM Formats"
	The following BOM file formats are supported: CSV, TSV, XLS, XLSX, JSON and YAML

#### Select Fields

Once the BOM file is uploaded, the following view will load:
{% with id="bom_select_fields", url="build/bom_select_fields.png", description="Select Fields View" %}
{% include 'img.html' %}
{% endwith %}

InvenTree will attempt to automatically match the BOM file columns with InvenTree part fields. `Part_Name` is a **required** field for the upload process and moving on to the next step. Specifying the `Part_IPN` field matching is very powerful as it allows to create direct pointers to InvenTree parts.

Once you have selected the corresponding InvenTree fields, click on the "Submit Selections" button to move on to the next step.

#### Select Parts

Once the BOM file columns and InvenTree fields are correctly matched, the following view will load:
{% with id="bom_select_parts", url="build/bom_select_parts.png", description="Select Parts View" %}
{% include 'img.html' %}
{% endwith %}

InvenTree automatically tries to match parts from the BOM file with parts in its database. For parts that are found in InvenTree's database, the `Select Part` field selection will automatically point to the matching database part.

In this view, you can also edit the parts `Reference` and `Quantity` fields.

Once you have selected the corresponding InvenTree parts, click on the "Submit BOM" button to complete the BOM upload process.

### Validate BOM

After [adding BOM items manually](#add-bom-item) or [uploading a BOM file](#upload-bom), you should see the following view:
{% with id="bom_invalid", url="build/bom_invalid.png", description="Invalid BOM View" %}
{% include 'img.html' %}
{% endwith %}

The first message in the red box `The BOM for PCBA TEST has changed, and must be validated.` points out that InvenTree BOM needs to be "validated". BOM validation is a way to ensure a BOM does not have duplicate items/parts.

To process with BOM validation, click on the <span class='fas fa-clipboard-check'></span> icon and the `Validate BOM` form will be displayed. Click one the "Validate" switch then click on <span class="badge inventree confirm">Submit</span>

Voilà, this Bill of Materials is validated <span class='far fa-smile'></span>

{% with id="bom_valid", url="build/bom_valid.png", description="Valid BOM View" %}
{% include 'img.html' %}
{% endwith %}
