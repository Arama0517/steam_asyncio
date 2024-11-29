import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CTimedTrial_GetTimeRemaining_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CTimedTrial_GetTimeRemaining_Response(_message.Message):
    __slots__ = ("seconds_played", "seconds_allowed", "packageid", "mastersub_appid")
    SECONDS_PLAYED_FIELD_NUMBER: _ClassVar[int]
    SECONDS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    MASTERSUB_APPID_FIELD_NUMBER: _ClassVar[int]
    seconds_played: int
    seconds_allowed: int
    packageid: int
    mastersub_appid: int
    def __init__(self, seconds_played: _Optional[int] = ..., seconds_allowed: _Optional[int] = ..., packageid: _Optional[int] = ..., mastersub_appid: _Optional[int] = ...) -> None: ...

class CTimedTrial_RecordPlaytime_Request(_message.Message):
    __slots__ = ("appid", "seconds_played")
    APPID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_PLAYED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    seconds_played: int
    def __init__(self, appid: _Optional[int] = ..., seconds_played: _Optional[int] = ...) -> None: ...

class CTimedTrial_RecordPlaytime_Response(_message.Message):
    __slots__ = ("seconds_played", "seconds_allowed")
    SECONDS_PLAYED_FIELD_NUMBER: _ClassVar[int]
    SECONDS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    seconds_played: int
    seconds_allowed: int
    def __init__(self, seconds_played: _Optional[int] = ..., seconds_allowed: _Optional[int] = ...) -> None: ...

class CTimedTrial_ResetPlaytime_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CTimedTrial_ResetPlaytime_Response(_message.Message):
    __slots__ = ("seconds_played", "seconds_allowed")
    SECONDS_PLAYED_FIELD_NUMBER: _ClassVar[int]
    SECONDS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    seconds_played: int
    seconds_allowed: int
    def __init__(self, seconds_played: _Optional[int] = ..., seconds_allowed: _Optional[int] = ...) -> None: ...

class TimedTrial(_service.service): ...

class TimedTrial_Stub(TimedTrial): ...
