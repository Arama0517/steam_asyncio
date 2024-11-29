from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EContentDeltaChunkDataLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EContentDeltaChunkDataLocationInProtobuf: _ClassVar[EContentDeltaChunkDataLocation]
    k_EContentDeltaChunkDataLocationAfterProtobuf: _ClassVar[EContentDeltaChunkDataLocation]
k_EContentDeltaChunkDataLocationInProtobuf: EContentDeltaChunkDataLocation
k_EContentDeltaChunkDataLocationAfterProtobuf: EContentDeltaChunkDataLocation

class ContentManifestPayload(_message.Message):
    __slots__ = ("mappings",)
    class FileMapping(_message.Message):
        __slots__ = ("filename", "size", "flags", "sha_filename", "sha_content", "chunks", "linktarget")
        class ChunkData(_message.Message):
            __slots__ = ("sha", "crc", "offset", "cb_original", "cb_compressed")
            SHA_FIELD_NUMBER: _ClassVar[int]
            CRC_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            CB_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
            CB_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
            sha: bytes
            crc: int
            offset: int
            cb_original: int
            cb_compressed: int
            def __init__(self, sha: _Optional[bytes] = ..., crc: _Optional[int] = ..., offset: _Optional[int] = ..., cb_original: _Optional[int] = ..., cb_compressed: _Optional[int] = ...) -> None: ...
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        SHA_FILENAME_FIELD_NUMBER: _ClassVar[int]
        SHA_CONTENT_FIELD_NUMBER: _ClassVar[int]
        CHUNKS_FIELD_NUMBER: _ClassVar[int]
        LINKTARGET_FIELD_NUMBER: _ClassVar[int]
        filename: str
        size: int
        flags: int
        sha_filename: bytes
        sha_content: bytes
        chunks: _containers.RepeatedCompositeFieldContainer[ContentManifestPayload.FileMapping.ChunkData]
        linktarget: str
        def __init__(self, filename: _Optional[str] = ..., size: _Optional[int] = ..., flags: _Optional[int] = ..., sha_filename: _Optional[bytes] = ..., sha_content: _Optional[bytes] = ..., chunks: _Optional[_Iterable[_Union[ContentManifestPayload.FileMapping.ChunkData, _Mapping]]] = ..., linktarget: _Optional[str] = ...) -> None: ...
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[ContentManifestPayload.FileMapping]
    def __init__(self, mappings: _Optional[_Iterable[_Union[ContentManifestPayload.FileMapping, _Mapping]]] = ...) -> None: ...

class ContentManifestMetadata(_message.Message):
    __slots__ = ("depot_id", "gid_manifest", "creation_time", "filenames_encrypted", "cb_disk_original", "cb_disk_compressed", "unique_chunks", "crc_encrypted", "crc_clear")
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    GID_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    FILENAMES_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    CB_DISK_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    CB_DISK_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    CRC_ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    CRC_CLEAR_FIELD_NUMBER: _ClassVar[int]
    depot_id: int
    gid_manifest: int
    creation_time: int
    filenames_encrypted: bool
    cb_disk_original: int
    cb_disk_compressed: int
    unique_chunks: int
    crc_encrypted: int
    crc_clear: int
    def __init__(self, depot_id: _Optional[int] = ..., gid_manifest: _Optional[int] = ..., creation_time: _Optional[int] = ..., filenames_encrypted: bool = ..., cb_disk_original: _Optional[int] = ..., cb_disk_compressed: _Optional[int] = ..., unique_chunks: _Optional[int] = ..., crc_encrypted: _Optional[int] = ..., crc_clear: _Optional[int] = ...) -> None: ...

class ContentManifestSignature(_message.Message):
    __slots__ = ("signature",)
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    signature: bytes
    def __init__(self, signature: _Optional[bytes] = ...) -> None: ...

class ContentDeltaChunks(_message.Message):
    __slots__ = ("depot_id", "manifest_id_source", "manifest_id_target", "deltaChunks", "chunk_data_location")
    class DeltaChunk(_message.Message):
        __slots__ = ("sha_source", "sha_target", "size_original", "patch_method", "chunk", "size_delta")
        SHA_SOURCE_FIELD_NUMBER: _ClassVar[int]
        SHA_TARGET_FIELD_NUMBER: _ClassVar[int]
        SIZE_ORIGINAL_FIELD_NUMBER: _ClassVar[int]
        PATCH_METHOD_FIELD_NUMBER: _ClassVar[int]
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        SIZE_DELTA_FIELD_NUMBER: _ClassVar[int]
        sha_source: bytes
        sha_target: bytes
        size_original: int
        patch_method: int
        chunk: bytes
        size_delta: int
        def __init__(self, sha_source: _Optional[bytes] = ..., sha_target: _Optional[bytes] = ..., size_original: _Optional[int] = ..., patch_method: _Optional[int] = ..., chunk: _Optional[bytes] = ..., size_delta: _Optional[int] = ...) -> None: ...
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_ID_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_ID_TARGET_FIELD_NUMBER: _ClassVar[int]
    DELTACHUNKS_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    depot_id: int
    manifest_id_source: int
    manifest_id_target: int
    deltaChunks: _containers.RepeatedCompositeFieldContainer[ContentDeltaChunks.DeltaChunk]
    chunk_data_location: EContentDeltaChunkDataLocation
    def __init__(self, depot_id: _Optional[int] = ..., manifest_id_source: _Optional[int] = ..., manifest_id_target: _Optional[int] = ..., deltaChunks: _Optional[_Iterable[_Union[ContentDeltaChunks.DeltaChunk, _Mapping]]] = ..., chunk_data_location: _Optional[_Union[EContentDeltaChunkDataLocation, str]] = ...) -> None: ...
