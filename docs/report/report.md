---
title: Report Generation
layout: page
---

## Custom Reporting

InvenTree supports a customizable reporting ecosystem, allowing the user to develop reporting templates that meet their particular needs.

PDF reports can be generated from either [HTML](https://github.com/fdemmer/django-weasyprint) or [LaTeX](https://github.com/weinbusch/django-tex) template files which are written by the user.

Reports are used in a variety of situations to format data in a friendly format for printing, distribution, conformance and testing.

In addition to providing the ability for end-users to provide their own reporting templates, some report types offer "built-in" report templates ready for use.

## Report Types

Following is a list of available report types

* [Test Report](/report/test): Format results of a test report against for a particular StockItem
* [Packing List](/report/pack): Format a list of items for shipping or transfer
* [Order List](/report/order): Order line items 

## Template Formats

Report templates can be written in multiple formats as per the requirement of the user. Uploaded template files are passed through the django/jinja rendering framework, and as such accept the same variable template strings as any other django template file.

For example, rendering the name of a part (which is available in the particular template context as *part*) is as follows:

*The name of the part is **\{\{ part.name \}\}**.*

!!! info "Variables"
	Templates will have different variables available to them depending on the report type. Read the detail information on each report type for further information.

### HTML

HTML templating uses the [django-weasyprint](https://github.com/fdemmer/django-weasyprint) engine for rendering templated HTML files to PDF.

### LaTeX

LaTeX templating uses the [django-tex](https://github.com/weinbusch/django-tex) engine for rendering templated LaTeX files to PDF. Using LaTeX templates is much more complicated and requires advanced knowledge of configuring a LaTeX install. However it provides a much more powerful framework for generation of publication-quality documents.

!!! info "LaTeX Configuration"
	To use LaTeX templating, the system where InvenTree is installed must have a LaTeX toolchain accessible from the command line. Installation of such a toolchain is beyond the scope of this documenation.

!!! info "Special Characters"
	Special care must be taken to ensure that the LaTeX template file does not contain any LaTeX control characters that look like jinja template control codes!

#### Intepreter Selection

Out of the box, the LaTeX template rendering system is set to use *pdflatex* as the LaTeX interpreter. However this can easily be changed in the *config.yaml* configuration file:

``` yaml
## LaTeX report rendering
## InvenTree uses the django-tex plugin to enable LaTeX report rendering
## Ref: https://pypi.org/project/django-tex/
latex:
  ## Select the LaTeX interpreter to use for PDF rendering
  ## Note: The intepreter needs to be installed on the system!
  ## e.g. to install pdflatex: apt-get texlive-latex-base
  interpreter: pdflatex 
  ## Extra options to pass through to the LaTeX interpreter
  options: ''
```

## Uploading Templates

Custom report templates can be uploaded using the [Admin Interface](/admin/admin). Only users with admin access can upload and/or edit report template files.