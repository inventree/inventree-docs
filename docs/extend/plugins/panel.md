---
title: Panel Mixin
---

## PanelMixin

The `PanelMixin` enables plugins to render custom content to "panels" on individual pages in the web interface.

Most pages in the web interface support multiple panels, which are selected via the sidebar menu on the left side of the screen:

{% with id="panels", url="plugin/panels.png", description="Display panels" %}
{% include 'img.html' %}
{% endwith %}

Each plugin which implements this mixin can return zero or more custom panels for a particular page. The plugin can decide (at runtime) which panels it wishes to render. This determination can be made based on the page routing, the item being viewed, the particular user, or other considerations.

### Panel Content

Panel content can be rendered by returning HTML directly, or by rendering from a template file.


Each plugin can register templates simply by providing a 'templates' directory in its root path.

The convention is that each 'templates' directory contains a subdirectory with the same name as the plugin :
  * e.g. templates/myplugin/my_template.html


In this case, the template can then be loaded (from any plugin!) by loading "myplugin/my_template.html".
    
    

### Javascript

Custom code can be provided which will run when the particular panel is first loaded (by selecting it from the side menu).

To add some javascript code, you can add a reference to a function that will be called when the panel is loaded  
```
  {
        'title': "Updates",
        'description': "Latest updates for this part",
        'javascript': 'alert("You just loaded this panel!")',
    }
```

Or to add a template file that will be renderered as javascript code : 
 ```
  {
        'title': "Updates",
        'description': "Latest updates for this part",
        'javascript_template ': 'pluginTemplatePath/myJavascriptFile.js',
    }
```
note : see convention for template directory above.
    
## Example Implementation

Refer to the `CustomPanelSample` example class in the `./plugin/samples/integration/` directory, for a fully worked example of how custom UI panels can be implemented.
