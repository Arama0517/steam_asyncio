import subprocess

from tools.protobuf import protobufs_dir, protobufs_result_dir

protobufs_result_dir.mkdir(parents=True, exist_ok=True)

subprocess.check_call([
    'protoc',
    f'--python_out={protobufs_result_dir}',
    f'--pyi_out={protobufs_result_dir}',
    f'--proto_path={protobufs_dir}',
    protobufs_dir / '*.proto',
])

for file_path in protobufs_result_dir.rglob('*_pb2.py'):
    with file_path.open('r', encoding='utf-8') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        if line.startswith('import sys'):
            modified_lines.append(line)
        elif line.startswith('import '):
            modified_lines.append('import steam.protobufs.' + line[7:])  # 替换前缀
        else:
            modified_lines.append(line)

    # 将修改后的内容写回文件
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)
