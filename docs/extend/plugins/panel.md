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

To add some javascript code, you can add a reference to a function that will be called when the panel is loaded with the 'javascript' key in the panel description :
```
  {
        'title': "Updates",
        'description': "Latest updates for this part",
        'javascript': 'alert("You just loaded this panel!")',
    }
```

Or to add a template file that will be rendered as javascript code, from the plugin template folder, with the 'javascript_template' key in the panel description :
 ```
  {
        'title': "Updates",
        'description': "Latest updates for this part",
        'javascript_template': 'pluginTemplatePath/myJavascriptFile.js',
    }
```
note : see convention for template directory above.
    
## Example Implementation

Refer to the `CustomPanelSample` example class in the `./plugin/samples/integration/` directory, for a fully worked example of how custom UI panels can be implemented.

### An example with button 

Lets have a look at another example. We like to have a new panel that contains a button. 
Each time the button is clicked, a python function in our plugin shall be executed and
do something usefull. The result will look like that:

{% with id="panels", url="plugin/mouser.png", description="Panel example with button" %} {% include "img.html" %} {% endwith %}

First we need to write the plugin code, similar as in the example above. 

```python
from django.conf.urls import url
from django.http import HttpResponse

from order.views import PurchaseOrderDetail
from plugin import InvenTreePlugin
from plugin.mixins import PanelMixin, SettingsMixin, UrlsMixin

class MouserCartPanel(PanelMixin, SettingsMixin, InvenTreePlugin, UrlsMixin):

    value=1

    NAME = "MouserCart"
    SLUG = "mousercart"
    TITLE = "Create Mouser Cart"
    DESCRIPTION = "An example plugin demonstrating a button calling a python function."
    VERSION = "0.1"

    def get_custom_panels(self, view, request):
        panels = []

        # This panel will *only* display on the PurchaseOrder view,
        if isinstance(view, PurchaseOrderDetail):
            panels.append({
                'title': 'Mouser Actions',
                'icon': 'fa-user',
                'content_template': 'mouser/mouser.html',
            })
        return panels

    def setup_urls(self):
        return [
            url(r'mouser/getcart', self.GetCart, name='get-cart'),
        ]

#----------------------------------------------------------------------------
    def GetCart(self,request):

        print('User:',request.user)
        self.value=self.value+1
        return HttpResponse(f'OK')


```

The code is simple and really stripped down to the minimum. In the plugin class we first define the plugin metadata. 
Afterwards we define the custom panel. Here we use a html template to describe the content of the panel. We need to 
add the path here because the template resides in the subdirectory templates/mouser.
Then we setup the url. This is important. The url connects the http request with the function to be executed. 

 * mouser/getcart: Path of the url together with SLUG
 * self.GetCart: This is the function to be called. It is defined further down
 * get-cart: This is the name of the url that needs to be referenced in the html template. We see that later.

Finally we define the function. This is a simple increment of a class value. 


New lets have a look at the template file mouser.html

```html
{% raw %}
{% load i18n %}

<script>
async function JGetCart(){
    response = await fetch( '{% url "plugin:mousercart:get-cart" %}');
    location.reload();
}
</script>

<button type='button' class='btn btn-info' onclick="JGetCart()" title='{% trans "Get Mouser shopping Cart" %}'>
<span class='fas fa-redo-alt'></span> {% trans "Get Cart" %}
</button>

<br>
{{ order.description }}
{{ plugin.value }}
{% endraw %}
```

We start with a bit of javascript. The function JGetCart just calls the url that has been defined in the python code above. 
The url consists of a full path plugin:plugin-name:url-name. The plugin-name is the SLUG that was defined in the plugin code.
Then just a reload.

The button is defined  withe class="btn btn-info" This is an InvenTree predefined button. There a are lots of others available. 
Here are some examples of available colors:

{% with id="panels", url="plugin/buttons.png", description="Button examples" %} {% include "img.html" %} {% endwith %}

Please have a look at the css files for more options. The last line renders the value that was defined in the plugin. 

Just give it a try: Each time you press the button, the value will be increased.

Have fun
