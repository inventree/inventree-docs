"""
Custom mkdocs hooks, using the mkdocs-simple-hooks plugin
"""

import json
import os
import re

from urllib import request


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
        
        # Determine if we want to display a 'version' banner
        # Basically we do, *unless* we are displaying the "stable" version
        config['version_banner'] = rtd_version != 'stable'

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

    # Download release information via the GitHub API
    print("Fetching InvenTree release information from api.github.com:")
    releases = []

    # Keep making API requests until we run out of results
    page = 1

    while 1:
        url = f"https://api.github.com/repos/inventree/inventree/releases?page={page}&per_page=50"

        print(f" - {url}")

        response = request.urlopen(url, timeout=30)
        assert(response.status == 200)

        data = json.loads(response.read().decode())
        
        # No more results
        if len(data) == 0:
            break

        # Request the next page of results
        page += 1

        for item in data:
            # Ignore draft releases
            if item['draft']:
                continue
                
            tag = item['tag_name']

            # Check that the tag is formatted correctly
            re.match('^\d+\.\d+\.\d+$', tag)

            if not re.match:
                print(f"Found badly formatted release: {tag}")
                continue

            # Check if there is a local file with release information
            local_path = os.path.join(
                os.path.dirname(__file__),
                'releases',
                f'{tag}.md',
            )

            if os.path.exists(local_path):
                item['local_path'] = local_path

            # Extract the date
            item['date'] = item['published_at'].split('T')[0]

            releases.append(item)
    
    print(f"- found {len(releases)} releases.")

    # Sort releases by descending date
    config['releases'] = sorted(releases, key=lambda it: it['date'], reverse=True)

    return config

