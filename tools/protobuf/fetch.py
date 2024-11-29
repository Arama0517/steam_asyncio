import os
import shutil
import subprocess

from tools.protobuf import current_dir, protobufs_dir

protobufs_dir.mkdir(parents=True, exist_ok=True)
temp_dir = current_dir / 'SteamTracking'


def git(*args, **kwargs):
    if not kwargs.get('cwd'):
        kwargs['cwd'] = temp_dir
    subprocess.check_call(['git'] + list(args), **kwargs)


def remove_read_only(func, path, exc_info):
    os.chmod(path, 0o777)
    func(path)


if temp_dir.exists():
    shutil.rmtree(temp_dir, onerror=remove_read_only)

git(
    'clone',
    '--filter=tree:0',
    '--no-checkout',
    '--depth=1',
    '--config',
    'core.sparsecheckout=true',
    'https://github.com/SteamDatabase/SteamTracking.git',
    cwd=temp_dir.parent,
)
with (temp_dir / '.git' / 'info' / 'sparse-checkout').open('w') as f:
    f.write('Protobufs')

git('checkout', 'master')
shutil.copytree(temp_dir / 'Protobufs', current_dir / 'protobufs', dirs_exist_ok=True)
shutil.rmtree(temp_dir, onerror=remove_read_only)

special_files = [
    'steammessages_physicalgoods.proto',
    'steammessages_webui_friends.proto',
    'steammessages_gc.proto',
    'steammessages_test_messages.proto',
]

for file_name in special_files:
    file_path = protobufs_dir / file_name
    if file_path.exists():
        file_path.rename(file_path.with_suffix('.proto.notouch'))

for file in protobufs_dir.glob('*.steamclient.proto'):
    new_name = file.with_name(file.name.replace('.steamclient.proto', '.proto'))
    if new_name.exists():
        new_name.unlink()
    file.rename(new_name)

for proto_file in protobufs_dir.glob('*.proto'):
    with proto_file.open('r+', encoding='utf-8') as f:
        content = f.read()

        if not content.startswith('syntax = "proto2";\n'):
            content = 'syntax = "proto2";\n' + content
        content = content.replace('cc_generic_services', 'py_generic_services')
        content = content.replace('.steamclient.proto', '.proto')

        f.seek(0)
        f.write(content)
        f.truncate()

for file in protobufs_dir.glob('*.proto.notouch'):
    file.rename(file.with_suffix('.proto'))
