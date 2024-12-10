from os import environ
from pathlib import Path
from sys import version_info

with Path(environ['GITHUB_ENV']).open('w') as f:
    f.write(f'PYTHON_VERSION={version_info.major}.{version_info.minor}.{version_info.micro}')
