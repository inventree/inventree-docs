---
title: Debug
layout: page
---

## Debug

### Readthedocs

*[Reference](https://docs.readthedocs.io/en/stable/development/design/theme-context.html#context-injected)*

<ul>
  <li>READTHEDOCS - {{ READTHEDOCS }}</li>
  <li>meta - {{ meta | pretty }}</li>
  <li>meta2 - {{ context(meta) | pretty }}</li>
</ul>

<b>config.docs_dir:</b> {{ config.docs_dir }}

### Mkdocs

#### Base URL

base_url: `{{ base_url }}`

#### Environment

{{ context(environment) | pretty }}

#### Global Variables

{{ context(extra) | pretty }}

#### Config

{{ context(config) | pretty }}
