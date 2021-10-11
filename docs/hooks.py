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

    if rtd:
        rtd_version = os.environ['READTHEDOCS_VERSION']
        rtd_language = os.environ['READTHEDOCS_LANGUAGE']

        site_url = f"https://inventree.readthedocs.io/{rtd_language}/{rtd_version}"
        assets_dir = f"/{rtd_language}/{rtd_version}/assets"

        print("Building within READTHEDOCS environment!")
        print(f" - Version: {rtd_version}")
        print(f" - Language: {rtd_language}")

        # Add *all* readthedocs related keys
        readthedocs = {}

        for key in os.environ.keys():
            if key.startswith('READTHEDOCS_'):
                k = key.replace('READTHEDOCS_', '').lower()
                readthedocs[k] = os.environ[key]

        # Supply this to the context
        config['readthedocs'] = readthedocs
        
    else:
        print("'READTHEDOCS' environment variable not found")
        print("Building for localhost configuration!")

        assets_dir = '/assets'
        site_url = config['site_url']

        config['readthedocs'] = False

    config['assets_dir'] = assets_dir
    config['site_url'] = site_url
 
    print(f"config.site_url = '{site_url}'")
    print(f"config.assets_dir = '{assets_dir}'")

    return config


def my_cfg(config, *args, **kwargs):

    # print(config.keys())

    for k in config.keys():
        print(f"- {k}")

    print(config['site_url'])

    return config

