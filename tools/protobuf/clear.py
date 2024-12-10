import shutil

from tools.protobuf import protobufs_dir, protobufs_result_dir

shutil.rmtree(protobufs_result_dir)
protobufs_result_dir.mkdir(parents=True)
(protobufs_result_dir / '__init__.py').write_text('', encoding='utf-8')

shutil.rmtree(protobufs_dir)
protobufs_dir.mkdir(parents=True)
