import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CSteamEngine_UpdateTextFilterDictionary_Notification(_message.Message):
    __slots__ = ("language", "type")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    language: str
    type: str
    def __init__(self, language: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CSteamEngine_GetTextFilterDictionary_Request(_message.Message):
    __slots__ = ("language", "type")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    language: str
    type: str
    def __init__(self, language: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CSteamEngine_GetTextFilterDictionary_Response(_message.Message):
    __slots__ = ("dictionary",)
    DICTIONARY_FIELD_NUMBER: _ClassVar[int]
    dictionary: str
    def __init__(self, dictionary: _Optional[str] = ...) -> None: ...

class CSteamEngine_TextFilterDictionaryChanged_Notification(_message.Message):
    __slots__ = ("language", "type")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    language: str
    type: str
    def __init__(self, language: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class CSteamEngine_GetGameIDForPID_Request(_message.Message):
    __slots__ = ("pid",)
    PID_FIELD_NUMBER: _ClassVar[int]
    pid: int
    def __init__(self, pid: _Optional[int] = ...) -> None: ...

class CSteamEngine_GetGameIDForPID_Response(_message.Message):
    __slots__ = ("gameid",)
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    def __init__(self, gameid: _Optional[int] = ...) -> None: ...

class CSteamEngine_SetOverlayEscapeKeyHandling_Notification(_message.Message):
    __slots__ = ("gameid", "should_handle")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_HANDLE_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    should_handle: bool
    def __init__(self, gameid: _Optional[int] = ..., should_handle: bool = ...) -> None: ...

class SteamEngine(_service.service): ...

class SteamEngine_Stub(SteamEngine): ...
