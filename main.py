import os
from posixpath import dirname

from urllib import request


def define_env(env):

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
