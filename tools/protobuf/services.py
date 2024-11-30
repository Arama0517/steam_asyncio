from tools.protobuf import protobufs_dir, source_code_dir

unified_file = source_code_dir / 'core' / 'msg' / 'unified.py'
temp_file = unified_file.with_suffix('.tmp')
proto_files = protobufs_dir.glob('*.proto')

lines = unified_file.read_text(encoding='utf-8').splitlines()
start_index = next(i for i, line in enumerate(lines) if 'MARK_SERVICE_START' in line)
end_index = next(i for i, line in enumerate(lines) if 'MARK_SERVICE_END' in line)

temp_lines = lines[: start_index + 1]
for proto_file in proto_files:
    for line in proto_file.read_text(encoding='utf-8').splitlines():
        if line.startswith('service'):
            parts = line.replace('/', ' ').replace('.', ' ').replace(':', ' ').split()
            if len(parts) >= 2:
                temp_lines.append(
                    f"    '{parts[1]}': 'steam.protobufs.{proto_file.stem}_pb2',"
                )

temp_lines.extend(lines[end_index:])
temp_file.write_text('\n'.join(temp_lines), encoding='utf-8')
temp_file.replace(unified_file)
