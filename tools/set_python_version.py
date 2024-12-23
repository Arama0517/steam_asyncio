from os import environ
from pathlib import Path
from sys import version_info

with Path(environ['GITHUB_ENV']).open('a') as f:
    f.write(f'\nPYTHON_VERSION={version_info.major}.{version_info.minor}.{version_info.micro}')
