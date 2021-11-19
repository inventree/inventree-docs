import os
import yaml

here = os.path.dirname(__file__)

tld = os.path.abspath(os.path.join(here, '..'))

config_file = os.path.join(tld, 'mkdocs.yml')

with open(config_file, 'r') as f:
    data = yaml.safe_load(f)

    assert data['strict'] == True