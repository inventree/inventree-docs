import os
from posixpath import dirname

from urllib import request


def define_env(env):

    # Ensure that the config template is always up to date
    CFG_URL = "https://raw.githubusercontent.com/inventree/InvenTree/master/InvenTree/config_template.yaml"

    response = request.urlopen(CFG_URL)
    print(f"Reading config template from GitHub: Response {response.status}")
    
    if response.status == 200:
        data = response.read()

        if len(data) > 0:
            with open("_includes/config.yaml", "w") as f:
                f.write(str(data.decode()))

    @env.macro
    def listimages(subdir):
        """
        Return a listing of all asset files in the provided subdir
        """

        here = os.path.dirname(__file__)

        directory = os.path.join(here, 'docs', 'assets', 'images', subdir)

        assets = []

        allowed = [
            '.png',
            '.jpg',
        ]

        for asset in os.listdir(directory):

            if any([asset.endswith(x) for x in allowed]):
                assets.append(os.path.join(subdir, asset))

        return assets
