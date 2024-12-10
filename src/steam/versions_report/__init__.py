import platform
import sys
from importlib.metadata import distribution

from rich import print
from rich.markdown import Markdown


def versions_report():
    """Print a report of all dependency versions, and environment"""

    text = f'# Dependencies\n- **steam**: `{distribution("steam").version}`'
    for dep in [
        'cachetools',
        'pycryptodomex',
        'requests',
        'vdf',
        'protobuf',
        'websockets',
        'aiohttp',
        'dnspython',
        'lxml',
    ]:
        text += f'\n- {dep}: `{distribution(dep).version}`'
    text += f"""
# Python runtime
- executable: `{sys.executable}`
- version: `{sys.version}`
- platform: `{sys.platform}`
# System info
- system: `{platform.system()}`
- machine: `{platform.machine()}`
- release: `{platform.release()}`
- version: `{platform.version()}`
"""
    print(Markdown(text))
