---
title: Bill of Materials
---

## Bill of Materials

A Bill of Materials (BOM) defines the list of component parts required to make an assembly, [create builds](/build/build) and allocate inventory.

### Add BOM Item

To manually add a BOM item, navigate to the part/assembly detail page then click on the "BOM" tab. On top of the tab view, click on the :fontawesome-solid-edit: icon then, after the page reloads, click on the :fontawesome-solid-plus-circle: icon.

The `Create BOM Item` form will be displayed:
{% with id="bom_add_item", url="build/bom_add_item.png", description="Create BOM Item Form" %}
{% include 'img.html' %}
{% endwith %}

Fill-out the `Quantity` (required), `Reference`, `Overage` and `Note` (optional) fields then click on the "Submit" button to add the BOM item to this part's BOM.

### Upload BOM

Uploading a BOM to InvenTree is a three steps process:

1. upload BOM file
0. select matching InvenTree fields
0. select matching InvenTree parts.

To upload a BOM file, navigate to the part/assembly detail page then click on the "BOM" tab. On top of the tab view, click on the :fontawesome-solid-edit: icon then, after the page reloads, click on the :fontawesome-solid-file-upload: icon.

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

InvenTree will attempt to automatically match the BOM file columns with InvenTree part fields. `Part_Name` is a **required** field for the upload process and moving on to the next step. Sprcifying the `Part_IPN` field matching is very powerful as it allows to create direct pointers to InvenTree parts.

Once you have selected the corresponding InvenTree fields, click on the "Submit Selections" button to move on to the next step.

#### Select Parts

Once the BOM file columns and InvenTree fields are correctly matched, the following view will load:
{% with id="bom_select_parts", url="build/bom_select_parts.png", description="Select Parts View" %}
{% include 'img.html' %}
{% endwith %}

InvenTree automatically tries to match parts from the BOM file with parts in its database. For parts that are found in InvenTree's database, the `Select Part` field selection will automatically point to the matching database part.

!!! info "Create New Part"
	The :fontawesome-solid-plus: icon in the `Select Part` column let's you load the `Create New Part` form which allows you to create an InvenTree part during the BOM upload process.

In this view, you can also edit the parts `Reference` and `Quantity` fields.

Once you have selected the corresponding InvenTree parts, click on the "Submit BOM" button to complete the BOM upload process.

### Validate BOM

After [adding BOM items manually](#add-bom-item) or [uploading a BOM file](#upload-bom), you should see the following view:
{% with id="bom_invalid", url="build/bom_invalid.png", description="Invalid BOM View" %}
{% include 'img.html' %}
{% endwith %}

The first message in the red box `The BOM for PCBA TEST has changed, and must be validated.` points out that InvenTree BOM needs to be "validated". BOM validation is a way to ensure a BOM does not have duplicate items/parts.

To process with BOM validation, click on the :fontawesome-solid-clipboard-check: icon and the `Validate BOM` form will be displayed. Click one the "Validate" switch then click on the "Submit" button.

Voilà, this Bill or Materials is validated :material-emoticon-cool:

{% with id="bom_valid", url="build/bom_valid.png", description="Valid BOM View" %}
{% include 'img.html' %}
{% endwith %}
