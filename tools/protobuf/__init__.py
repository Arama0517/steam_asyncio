from tools import current_dir as _current_dir, source_code_dir as _source_code_dir

__all__ = ['protobufs_dir', 'protobufs_result_dir']

protobufs_dir = _current_dir / 'protobufs'
protobufs_result_dir = _source_code_dir / 'protobufs'
