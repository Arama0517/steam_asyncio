import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CSharedJSContext_GetDesiredSteamUIWindows_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgSteamUIBrowserWindow(_message.Message):
    __slots__ = ("id", "pid", "browser_id", "window_type", "x", "y", "appid", "parent_window_handle", "app_name", "gamepadui_via_gamescope")
    ID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    BROWSER_ID_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    PARENT_WINDOW_HANDLE_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    GAMEPADUI_VIA_GAMESCOPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    pid: int
    browser_id: int
    window_type: int
    x: int
    y: int
    appid: int
    parent_window_handle: int
    app_name: str
    gamepadui_via_gamescope: bool
    def __init__(self, id: _Optional[int] = ..., pid: _Optional[int] = ..., browser_id: _Optional[int] = ..., window_type: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., appid: _Optional[int] = ..., parent_window_handle: _Optional[int] = ..., app_name: _Optional[str] = ..., gamepadui_via_gamescope: bool = ...) -> None: ...

class CSharedJSContext_GetDesiredSteamUIWindows_Response(_message.Message):
    __slots__ = ("windows",)
    WINDOWS_FIELD_NUMBER: _ClassVar[int]
    windows: _containers.RepeatedCompositeFieldContainer[CMsgSteamUIBrowserWindow]
    def __init__(self, windows: _Optional[_Iterable[_Union[CMsgSteamUIBrowserWindow, _Mapping]]] = ...) -> None: ...

class SharedJSContext(_service.service): ...

class SharedJSContext_Stub(SharedJSContext): ...
