import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGameRecording_AudioSessionsChanged_Notification(_message.Message):
    __slots__ = ("sessions",)
    class Session(_message.Message):
        __slots__ = ("id", "name", "is_system", "is_muted", "is_active", "is_captured", "recent_peak", "is_game", "is_steam", "is_saved")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
        IS_MUTED_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        IS_CAPTURED_FIELD_NUMBER: _ClassVar[int]
        RECENT_PEAK_FIELD_NUMBER: _ClassVar[int]
        IS_GAME_FIELD_NUMBER: _ClassVar[int]
        IS_STEAM_FIELD_NUMBER: _ClassVar[int]
        IS_SAVED_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        is_system: bool
        is_muted: bool
        is_active: bool
        is_captured: bool
        recent_peak: float
        is_game: bool
        is_steam: bool
        is_saved: bool
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., is_system: bool = ..., is_muted: bool = ..., is_active: bool = ..., is_captured: bool = ..., recent_peak: _Optional[float] = ..., is_game: bool = ..., is_steam: bool = ..., is_saved: bool = ...) -> None: ...
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[CGameRecording_AudioSessionsChanged_Notification.Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[CGameRecording_AudioSessionsChanged_Notification.Session, _Mapping]]] = ...) -> None: ...
