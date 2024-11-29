import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CWorkshop_GetEULAStatus_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CWorkshop_GetEULAStatus_Response(_message.Message):
    __slots__ = ("version", "timestamp_action", "accepted", "needs_action")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_ACTION_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    NEEDS_ACTION_FIELD_NUMBER: _ClassVar[int]
    version: int
    timestamp_action: int
    accepted: bool
    needs_action: bool
    def __init__(self, version: _Optional[int] = ..., timestamp_action: _Optional[int] = ..., accepted: bool = ..., needs_action: bool = ...) -> None: ...

class Workshop(_service.service): ...

class Workshop_Stub(Workshop): ...
