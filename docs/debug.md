---
title: Debug
layout: page
---

## Debug

### Readthedocs

*[Reference](https://docs.readthedocs.io/en/stable/development/design/theme-context.html#context-injected)*

<ul>
  <li>readthedocs.v1.meta.READTHEDOCS - {{ readthedocs.v1.meta.READTHEDOCS }}</li>
  <li>readthedocs - {{ readthedocs | pretty }}</li>
  <li>READTHEDOCS - {{ READTHEDOCS }}</li>
  <li>meta - {{ meta | pretty }}</li>
  <li>meta2 - {{ context(meta) | pretty }}</li>
</ul>

{{ readthedocs.v1.meta | pretty }}

### Mkdocs

#### Base URL

base_url: `{{ base_url }}`

#### Environment

{{ context(environment) | pretty }}

#### Global Variables

{{ context(extra) | pretty }}

#### Config

{{ context(config) | pretty }}
