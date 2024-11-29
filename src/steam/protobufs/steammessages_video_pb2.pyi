import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CVideo_ClientGetVideoURL_Request(_message.Message):
    __slots__ = ("video_id", "client_cellid")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CELLID_FIELD_NUMBER: _ClassVar[int]
    video_id: int
    client_cellid: int
    def __init__(self, video_id: _Optional[int] = ..., client_cellid: _Optional[int] = ...) -> None: ...

class CVideo_ClientGetVideoURL_Response(_message.Message):
    __slots__ = ("video_id", "video_url")
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    video_id: int
    video_url: str
    def __init__(self, video_id: _Optional[int] = ..., video_url: _Optional[str] = ...) -> None: ...

class VideoBookmark(_message.Message):
    __slots__ = ("app_id", "playback_position_in_seconds", "video_track_id", "audio_track_id", "timedtext_track_id", "last_modified", "hide_from_watch_history", "hide_from_library")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_POSITION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEDTEXT_TRACK_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    HIDE_FROM_WATCH_HISTORY_FIELD_NUMBER: _ClassVar[int]
    HIDE_FROM_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    playback_position_in_seconds: int
    video_track_id: int
    audio_track_id: int
    timedtext_track_id: int
    last_modified: int
    hide_from_watch_history: bool
    hide_from_library: bool
    def __init__(self, app_id: _Optional[int] = ..., playback_position_in_seconds: _Optional[int] = ..., video_track_id: _Optional[int] = ..., audio_track_id: _Optional[int] = ..., timedtext_track_id: _Optional[int] = ..., last_modified: _Optional[int] = ..., hide_from_watch_history: bool = ..., hide_from_library: bool = ...) -> None: ...

class CVideo_SetVideoBookmark_Notification(_message.Message):
    __slots__ = ("bookmarks",)
    BOOKMARKS_FIELD_NUMBER: _ClassVar[int]
    bookmarks: _containers.RepeatedCompositeFieldContainer[VideoBookmark]
    def __init__(self, bookmarks: _Optional[_Iterable[_Union[VideoBookmark, _Mapping]]] = ...) -> None: ...

class CVideo_GetVideoBookmarks_Request(_message.Message):
    __slots__ = ("appids", "updated_since")
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SINCE_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    updated_since: int
    def __init__(self, appids: _Optional[_Iterable[int]] = ..., updated_since: _Optional[int] = ...) -> None: ...

class CVideo_GetVideoBookmarks_Response(_message.Message):
    __slots__ = ("bookmarks",)
    BOOKMARKS_FIELD_NUMBER: _ClassVar[int]
    bookmarks: _containers.RepeatedCompositeFieldContainer[VideoBookmark]
    def __init__(self, bookmarks: _Optional[_Iterable[_Union[VideoBookmark, _Mapping]]] = ...) -> None: ...

class CVideo_UnlockedH264_Notification(_message.Message):
    __slots__ = ("encryption_key",)
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    encryption_key: bytes
    def __init__(self, encryption_key: _Optional[bytes] = ...) -> None: ...

class CFovasVideo_ClientGetOPFSettings_Request(_message.Message):
    __slots__ = ("app_id", "client_cellid")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CELLID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    client_cellid: int
    def __init__(self, app_id: _Optional[int] = ..., client_cellid: _Optional[int] = ...) -> None: ...

class CFovasVideo_ClientGetOPFSettings_Response(_message.Message):
    __slots__ = ("app_id", "opf_settings")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    OPF_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    opf_settings: str
    def __init__(self, app_id: _Optional[int] = ..., opf_settings: _Optional[str] = ...) -> None: ...

class Video(_service.service): ...

class Video_Stub(Video): ...

class VideoClient(_service.service): ...

class VideoClient_Stub(VideoClient): ...

class FovasVideo(_service.service): ...

class FovasVideo_Stub(FovasVideo): ...
