---
title: URLs Mixin
---

## UrlsMixin

Use the class constant `URLS` for a array of URLs that should be added to InvenTrees URL paths or override the `plugin.setup_urls` function.  

The array has to contain valid URL patterns as defined in the [django documentation](https://docs.djangoproject.com/en/stable/topics/http/urls/).

Minimal sample:

``` python
from django.utils.translation import gettext_lazy as _
from django.urls import re_path
from django.http import HttpResponse

from plugin import InvenTreePlugin
from plugin.mixins import UrlsMixin


def start_page(request):

    return HttpResponse("Hello, World!")


class CustomPagerPlugin(UrlsMixin, InvenTreePlugin):
    """Plugin to display custom pages"""

    NAME = "Sample URL Plugin"
    SLUG = "sampleurl"
    TITLE = _("Sample URL Plugin")
    DESCRIPTION = _("Sample URL Plugin")
    VERSION = "0.0.1"
    AUTHOR = _("Plugin Guy")

    URLS = [
        # Start page
        re_path(r'^.*$', start_page, name='sample-plugin-url-start'),
    ]
```

The URLs get exposed under `/plugin/{plugin.slug}/*` and get exposed to the template engine with the prefix `plugin:{plugin.slug}:` (for usage with the [url tag](https://docs.djangoproject.com/en/stable/ref/templates/builtins/#url)).


