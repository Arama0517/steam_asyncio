import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CCommunity_GetLinkFilterHashPrefixes_Request(_message.Message):
    __slots__ = ("hit_type", "count", "start")
    HIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    hit_type: int
    count: int
    start: int
    def __init__(self, hit_type: _Optional[int] = ..., count: _Optional[int] = ..., start: _Optional[int] = ...) -> None: ...

class CCommunity_GetLinkFilterHashPrefixes_Response(_message.Message):
    __slots__ = ("hash_prefixes",)
    HASH_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    hash_prefixes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, hash_prefixes: _Optional[_Iterable[int]] = ...) -> None: ...

class CCommunity_GetLinkFilterHashes_Request(_message.Message):
    __slots__ = ("hit_type", "count", "start")
    HIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    hit_type: int
    count: int
    start: int
    def __init__(self, hit_type: _Optional[int] = ..., count: _Optional[int] = ..., start: _Optional[int] = ...) -> None: ...

class CCommunity_GetLinkFilterHashes_Response(_message.Message):
    __slots__ = ("hashes",)
    HASHES_FIELD_NUMBER: _ClassVar[int]
    hashes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, hashes: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CCommunity_GetLinkFilterListVersion_Request(_message.Message):
    __slots__ = ("hit_type",)
    HIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    hit_type: int
    def __init__(self, hit_type: _Optional[int] = ...) -> None: ...

class CCommunity_GetLinkFilterListVersion_Response(_message.Message):
    __slots__ = ("version", "count")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    version: str
    count: int
    def __init__(self, version: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CommunityLinkFilter(_service.service): ...

class CommunityLinkFilter_Stub(CommunityLinkFilter): ...
