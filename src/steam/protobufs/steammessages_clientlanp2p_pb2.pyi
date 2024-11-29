import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientLANP2PRequestChunks(_message.Message):
    __slots__ = ("chunk_keys",)
    class ChunkKey(_message.Message):
        __slots__ = ("depot_id", "sha")
        DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
        SHA_FIELD_NUMBER: _ClassVar[int]
        depot_id: int
        sha: bytes
        def __init__(self, depot_id: _Optional[int] = ..., sha: _Optional[bytes] = ...) -> None: ...
    CHUNK_KEYS_FIELD_NUMBER: _ClassVar[int]
    chunk_keys: _containers.RepeatedCompositeFieldContainer[CMsgClientLANP2PRequestChunks.ChunkKey]
    def __init__(self, chunk_keys: _Optional[_Iterable[_Union[CMsgClientLANP2PRequestChunks.ChunkKey, _Mapping]]] = ...) -> None: ...

class CMsgClientLANP2PRequestChunksResponse(_message.Message):
    __slots__ = ("chunk_responses",)
    class ChunkData(_message.Message):
        __slots__ = ("result", "depot_id", "sha", "chunk_data", "encrypted", "compressed")
        RESULT_FIELD_NUMBER: _ClassVar[int]
        DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
        SHA_FIELD_NUMBER: _ClassVar[int]
        CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
        COMPRESSED_FIELD_NUMBER: _ClassVar[int]
        result: int
        depot_id: int
        sha: bytes
        chunk_data: bytes
        encrypted: bool
        compressed: bool
        def __init__(self, result: _Optional[int] = ..., depot_id: _Optional[int] = ..., sha: _Optional[bytes] = ..., chunk_data: _Optional[bytes] = ..., encrypted: bool = ..., compressed: bool = ...) -> None: ...
    CHUNK_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    chunk_responses: _containers.RepeatedCompositeFieldContainer[CMsgClientLANP2PRequestChunksResponse.ChunkData]
    def __init__(self, chunk_responses: _Optional[_Iterable[_Union[CMsgClientLANP2PRequestChunksResponse.ChunkData, _Mapping]]] = ...) -> None: ...

class CMsgClientPeerChunkRequest(_message.Message):
    __slots__ = ("app_id", "depot_id", "sha", "access_token")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    depot_id: int
    sha: bytes
    access_token: int
    def __init__(self, app_id: _Optional[int] = ..., depot_id: _Optional[int] = ..., sha: _Optional[bytes] = ..., access_token: _Optional[int] = ...) -> None: ...

class CMsgClientPeerChunkResponse(_message.Message):
    __slots__ = ("result", "app_id", "depot_id", "sha", "encrypted", "compressed", "chunk_data")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
    result: int
    app_id: int
    depot_id: int
    sha: bytes
    encrypted: bool
    compressed: bool
    chunk_data: bytes
    def __init__(self, result: _Optional[int] = ..., app_id: _Optional[int] = ..., depot_id: _Optional[int] = ..., sha: _Optional[bytes] = ..., encrypted: bool = ..., compressed: bool = ..., chunk_data: _Optional[bytes] = ...) -> None: ...
