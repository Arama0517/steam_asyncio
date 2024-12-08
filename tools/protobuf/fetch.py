import os
import shutil
import subprocess
from pathlib import Path

from tools.protobuf import current_dir, protobufs_dir

protobufs_dir.mkdir(parents=True, exist_ok=True)
steam_tracking_repo_dir = current_dir / 'SteamTracking'


def git(*args, cwd: Path = steam_tracking_repo_dir):
    subprocess.check_call(['git'] + list(args), cwd=cwd)


def remove_read_only(func, path, exc_info):
    os.chmod(path, 0o777)
    func(path)


if steam_tracking_repo_dir.exists():
    print('delete')
    shutil.rmtree(steam_tracking_repo_dir, onerror=remove_read_only)

git(
    'clone',
    '--filter=tree:0',
    '--no-checkout',
    '--depth=1',
    '--config',
    'core.sparsecheckout=true',
    'https://github.com/SteamDatabase/SteamTracking.git',
    steam_tracking_repo_dir,
    cwd=current_dir,
)
with (steam_tracking_repo_dir / '.git' / 'info' / 'sparse-checkout').open('w') as f:
    f.write('Protobufs')

git('checkout', 'master')
shutil.copytree(steam_tracking_repo_dir / 'Protobufs', protobufs_dir, dirs_exist_ok=True)
shutil.rmtree(steam_tracking_repo_dir, onerror=remove_read_only)

for file in protobufs_dir.glob('*.steamclient.proto'):
    new_name = file.with_name(file.name.replace('.steamclient.proto', '.proto'))
    if new_name.exists():
        new_name.unlink()
    file.rename(new_name)

for proto_file in protobufs_dir.glob('*.proto'):
    with proto_file.open('r', encoding='utf-8') as f:
        content = f.read()
        content = content.replace('cc_generic_services', 'py_generic_services')
        content = content.replace('.steamclient.proto', '.proto')
    with proto_file.open('w', encoding='utf-8') as f:
        f.write(content)

for file in protobufs_dir.glob('*.proto.notouch'):
    file.rename(file.with_suffix('.proto'))
