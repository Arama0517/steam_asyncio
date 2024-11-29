from tools.protobuf import protobufs_dir, protobufs_result_dir

for file in protobufs_dir.rglob('*.proto'):
    file.unlink()

for file in protobufs_result_dir.rglob('*_pb2.py'):
    file.unlink()
