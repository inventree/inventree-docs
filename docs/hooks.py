"""
Custom mkdocs hooks, using the mkdocs-simple-hooks plugin
"""

import os


def on_config(config, *args, **kwargs):
    """
    Hosting multiple versions of the documenation on readthedocs.io is complex,
    as the required interactions between rtd and mkdocs do not exist.

    We want to be able to provide a *dynamic* config.site_url parameter to mkdocs,
    which tells it the base url, e.g.

    - https://readthedocs.io/en/latest
    - https://readthedocs.io/de/0.5.1

    Further, we need to know if we are building on readthedocs at all!

    readthedocs provides some environment variables:
    - https://docs.readthedocs.io/en/stable/builds.html#build-environment

    We can use these to determine (at run time) where we are hosting

    """

    rtd = os.environ.get('READTHEDOCS', False)

    if not rtd:
        print("'READTHEDOCS' environment variable not found")
        print("Building for localhost configuration!")

    else:
        rtd_version = os.environ['READTHEDOCS_VERSION']
        rtd_language = os.environ['READTHEDOCS_LANGUAGE']

        url = f"https://inventree.readthedocs.io/{rtd_language}/{rtd_version}"

        config['site_url'] = url

    return config


def my_cfg(config, *args, **kwargs):

    # print(config.keys())

    for k in config.keys():
        print(f"- {k}")

    print(config['site_url'])

    return config

