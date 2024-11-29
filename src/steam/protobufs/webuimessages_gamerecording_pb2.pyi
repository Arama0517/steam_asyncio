import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
import webuimessages_gamerecordingfiles_pb2 as _webuimessages_gamerecordingfiles_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ETimelineEntryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ETimelineEntryType_Invalid: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_GameMode: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_Event: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_StateDescription: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_Achievement: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_UserMarker: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_Screenshot: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_Error: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_Tag: _ClassVar[ETimelineEntryType]
    k_ETimelineEntryType_GamePhase: _ClassVar[ETimelineEntryType]

class EPhaseResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EPhaseResultType_Automatic: _ClassVar[EPhaseResultType]
    k_EPhaseResultType_Blank: _ClassVar[EPhaseResultType]
    k_EPhaseResultType_API: _ClassVar[EPhaseResultType]

class ETimelineChangeNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ETimelineChangeNotificationType_Started: _ClassVar[ETimelineChangeNotificationType]
    k_ETimelineChangeNotificationType_Stopped: _ClassVar[ETimelineChangeNotificationType]
    k_ETimelineChangeNotificationType_Deleted: _ClassVar[ETimelineChangeNotificationType]
    k_ETimelineChangeNotificationType_RecordingStarted: _ClassVar[ETimelineChangeNotificationType]
    k_ETimelineChangeNotificationType_RecordingStopped: _ClassVar[ETimelineChangeNotificationType]
    k_ETimelineChangeNotificationType_RecordingUpdated: _ClassVar[ETimelineChangeNotificationType]

class ERecordingSessionChangeNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ERecordingSessionChangeNotificationType_Started: _ClassVar[ERecordingSessionChangeNotificationType]
    k_ERecordingSessionChangeNotificationType_Stopped: _ClassVar[ERecordingSessionChangeNotificationType]
    k_ERecordingSessionChangeNotificationType_Deleted: _ClassVar[ERecordingSessionChangeNotificationType]
    k_ERecordingSessionChangeNotificationType_Updated: _ClassVar[ERecordingSessionChangeNotificationType]

class EDiskSpaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_eDiskSpaceType_Recording: _ClassVar[EDiskSpaceType]
    k_eDiskSpaceType_Clip: _ClassVar[EDiskSpaceType]

class EThumbnailTimePrecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ePrecise: _ClassVar[EThumbnailTimePrecision]
    k_eLoose: _ClassVar[EThumbnailTimePrecision]

class EThumbnailFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_eJPEG: _ClassVar[EThumbnailFormat]
    k_eRGB: _ClassVar[EThumbnailFormat]
k_ETimelineEntryType_Invalid: ETimelineEntryType
k_ETimelineEntryType_GameMode: ETimelineEntryType
k_ETimelineEntryType_Event: ETimelineEntryType
k_ETimelineEntryType_StateDescription: ETimelineEntryType
k_ETimelineEntryType_Achievement: ETimelineEntryType
k_ETimelineEntryType_UserMarker: ETimelineEntryType
k_ETimelineEntryType_Screenshot: ETimelineEntryType
k_ETimelineEntryType_Error: ETimelineEntryType
k_ETimelineEntryType_Tag: ETimelineEntryType
k_ETimelineEntryType_GamePhase: ETimelineEntryType
k_EPhaseResultType_Automatic: EPhaseResultType
k_EPhaseResultType_Blank: EPhaseResultType
k_EPhaseResultType_API: EPhaseResultType
k_ETimelineChangeNotificationType_Started: ETimelineChangeNotificationType
k_ETimelineChangeNotificationType_Stopped: ETimelineChangeNotificationType
k_ETimelineChangeNotificationType_Deleted: ETimelineChangeNotificationType
k_ETimelineChangeNotificationType_RecordingStarted: ETimelineChangeNotificationType
k_ETimelineChangeNotificationType_RecordingStopped: ETimelineChangeNotificationType
k_ETimelineChangeNotificationType_RecordingUpdated: ETimelineChangeNotificationType
k_ERecordingSessionChangeNotificationType_Started: ERecordingSessionChangeNotificationType
k_ERecordingSessionChangeNotificationType_Stopped: ERecordingSessionChangeNotificationType
k_ERecordingSessionChangeNotificationType_Deleted: ERecordingSessionChangeNotificationType
k_ERecordingSessionChangeNotificationType_Updated: ERecordingSessionChangeNotificationType
k_eDiskSpaceType_Recording: EDiskSpaceType
k_eDiskSpaceType_Clip: EDiskSpaceType
k_ePrecise: EThumbnailTimePrecision
k_eLoose: EThumbnailTimePrecision
k_eJPEG: EThumbnailFormat
k_eRGB: EThumbnailFormat

class CGameRecording_GetAppsWithBackgroundVideo_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetAppsWithBackgroundVideo_Response(_message.Message):
    __slots__ = ("apps",)
    class App(_message.Message):
        __slots__ = ("game_id", "most_recent_start_time", "recording_type", "video_duration_seconds", "timeline_duration_seconds", "is_active", "file_size")
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        MOST_RECENT_START_TIME_FIELD_NUMBER: _ClassVar[int]
        RECORDING_TYPE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_DURATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        game_id: int
        most_recent_start_time: int
        recording_type: _enums_pb2.EGameRecordingType
        video_duration_seconds: float
        timeline_duration_seconds: float
        is_active: bool
        file_size: int
        def __init__(self, game_id: _Optional[int] = ..., most_recent_start_time: _Optional[int] = ..., recording_type: _Optional[_Union[_enums_pb2.EGameRecordingType, str]] = ..., video_duration_seconds: _Optional[float] = ..., timeline_duration_seconds: _Optional[float] = ..., is_active: bool = ..., file_size: _Optional[int] = ...) -> None: ...
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[CGameRecording_GetAppsWithBackgroundVideo_Response.App]
    def __init__(self, apps: _Optional[_Iterable[_Union[CGameRecording_GetAppsWithBackgroundVideo_Response.App, _Mapping]]] = ...) -> None: ...

class CGameRecording_GetTimelinesForApp_Request(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_GetTimelinesForApp_Response(_message.Message):
    __slots__ = ("timelines",)
    TIMELINES_FIELD_NUMBER: _ClassVar[int]
    timelines: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CGameRecordingTimelineMetadata]
    def __init__(self, timelines: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CGameRecordingTimelineMetadata, _Mapping]]] = ...) -> None: ...

class CGameRecording_GetTimelinesForClip_Request(_message.Message):
    __slots__ = ("clip_id",)
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    def __init__(self, clip_id: _Optional[str] = ...) -> None: ...

class CGameRecording_GetTimelinesForClip_Response(_message.Message):
    __slots__ = ("game_id", "timelines", "first_timeline_start_offset_ms")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINES_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIMELINE_START_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    timelines: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CGameRecordingTimelineMetadata]
    first_timeline_start_offset_ms: int
    def __init__(self, game_id: _Optional[int] = ..., timelines: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CGameRecordingTimelineMetadata, _Mapping]]] = ..., first_timeline_start_offset_ms: _Optional[int] = ...) -> None: ...

class CGameRecording_QueryPhases_Request(_message.Message):
    __slots__ = ("page", "count", "filter_gameid", "filter_search_string", "filter_tags", "filter_phase_id")
    class Tag(_message.Message):
        __slots__ = ("group", "name")
        GROUP_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        group: str
        name: str
        def __init__(self, group: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    PAGE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    FILTER_GAMEID_FIELD_NUMBER: _ClassVar[int]
    FILTER_SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    FILTER_TAGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    page: int
    count: int
    filter_gameid: int
    filter_search_string: str
    filter_tags: _containers.RepeatedCompositeFieldContainer[CGameRecording_QueryPhases_Request.Tag]
    filter_phase_id: str
    def __init__(self, page: _Optional[int] = ..., count: _Optional[int] = ..., filter_gameid: _Optional[int] = ..., filter_search_string: _Optional[str] = ..., filter_tags: _Optional[_Iterable[_Union[CGameRecording_QueryPhases_Request.Tag, _Mapping]]] = ..., filter_phase_id: _Optional[str] = ...) -> None: ...

class CGameRecording_QueryPhases_Response(_message.Message):
    __slots__ = ("phases", "total_count")
    class Phase(_message.Message):
        __slots__ = ("game_id", "date_recorded", "duration_ms", "tags", "contained_tags", "background_recording", "clip_ids", "type", "start_ms", "screenshots", "active", "phase_id", "significant_events", "attributes")
        class BackgroundRecording(_message.Message):
            __slots__ = ("timeline_id", "offset", "duration_ms")
            TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            DURATION_MS_FIELD_NUMBER: _ClassVar[int]
            timeline_id: str
            offset: int
            duration_ms: int
            def __init__(self, timeline_id: _Optional[str] = ..., offset: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        DATE_RECORDED_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        CONTAINED_TAGS_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_RECORDING_FIELD_NUMBER: _ClassVar[int]
        CLIP_IDS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        START_MS_FIELD_NUMBER: _ClassVar[int]
        SCREENSHOTS_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        PHASE_ID_FIELD_NUMBER: _ClassVar[int]
        SIGNIFICANT_EVENTS_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        game_id: int
        date_recorded: int
        duration_ms: int
        tags: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CTimelineTag]
        contained_tags: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CTimelineTag]
        background_recording: CGameRecording_QueryPhases_Response.Phase.BackgroundRecording
        clip_ids: _containers.RepeatedScalarFieldContainer[str]
        type: EPhaseResultType
        start_ms: int
        screenshots: _containers.RepeatedScalarFieldContainer[int]
        active: bool
        phase_id: str
        significant_events: _containers.RepeatedCompositeFieldContainer[CTimelineEntry]
        attributes: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CPhaseAttribute]
        def __init__(self, game_id: _Optional[int] = ..., date_recorded: _Optional[int] = ..., duration_ms: _Optional[int] = ..., tags: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CTimelineTag, _Mapping]]] = ..., contained_tags: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CTimelineTag, _Mapping]]] = ..., background_recording: _Optional[_Union[CGameRecording_QueryPhases_Response.Phase.BackgroundRecording, _Mapping]] = ..., clip_ids: _Optional[_Iterable[str]] = ..., type: _Optional[_Union[EPhaseResultType, str]] = ..., start_ms: _Optional[int] = ..., screenshots: _Optional[_Iterable[int]] = ..., active: bool = ..., phase_id: _Optional[str] = ..., significant_events: _Optional[_Iterable[_Union[CTimelineEntry, _Mapping]]] = ..., attributes: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CPhaseAttribute, _Mapping]]] = ...) -> None: ...
    PHASES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    phases: _containers.RepeatedCompositeFieldContainer[CGameRecording_QueryPhases_Response.Phase]
    total_count: int
    def __init__(self, phases: _Optional[_Iterable[_Union[CGameRecording_QueryPhases_Response.Phase, _Mapping]]] = ..., total_count: _Optional[int] = ...) -> None: ...

class CGameRecording_GetTags_Request(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_GetTags_Response(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CTimelineTag]
    def __init__(self, tags: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CTimelineTag, _Mapping]]] = ...) -> None: ...

class CGameRecording_GetEnoughDiskSpace_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetEnoughDiskSpace_Response(_message.Message):
    __slots__ = ("enough_space",)
    ENOUGH_SPACE_FIELD_NUMBER: _ClassVar[int]
    enough_space: bool
    def __init__(self, enough_space: bool = ...) -> None: ...

class CGameRecording_GetAvailableDiskSpace_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetAvailableDiskSpace_Response(_message.Message):
    __slots__ = ("size",)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: float
    def __init__(self, size: _Optional[float] = ...) -> None: ...

class CGameRecording_TimelineChanged_Notification(_message.Message):
    __slots__ = ("notification_type", "timeline_id", "game_id", "start_time", "duration_ms")
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    notification_type: ETimelineChangeNotificationType
    timeline_id: str
    game_id: int
    start_time: int
    duration_ms: int
    def __init__(self, notification_type: _Optional[_Union[ETimelineChangeNotificationType, str]] = ..., timeline_id: _Optional[str] = ..., game_id: _Optional[int] = ..., start_time: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class CGameRecording_RecordingSessionChanged_Notification(_message.Message):
    __slots__ = ("notification_type", "timeline_id", "game_id", "session_id", "start_offset", "duration_ms", "recording_type")
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    RECORDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    notification_type: ERecordingSessionChangeNotificationType
    timeline_id: str
    game_id: int
    session_id: str
    start_offset: int
    duration_ms: int
    recording_type: _enums_pb2.EGameRecordingType
    def __init__(self, notification_type: _Optional[_Union[ERecordingSessionChangeNotificationType, str]] = ..., timeline_id: _Optional[str] = ..., game_id: _Optional[int] = ..., session_id: _Optional[str] = ..., start_offset: _Optional[int] = ..., duration_ms: _Optional[int] = ..., recording_type: _Optional[_Union[_enums_pb2.EGameRecordingType, str]] = ...) -> None: ...

class CTimelineEntry(_message.Message):
    __slots__ = ("timeline_id", "entry_id", "time", "type", "game_mode", "range_title", "range_duration", "range_possible_clip", "timestamp_title", "marker_icon", "marker_description", "marker_priority", "screenshot_handle", "achievement_name", "tag", "phase_id", "attributes")
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GAME_MODE_FIELD_NUMBER: _ClassVar[int]
    RANGE_TITLE_FIELD_NUMBER: _ClassVar[int]
    RANGE_DURATION_FIELD_NUMBER: _ClassVar[int]
    RANGE_POSSIBLE_CLIP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TITLE_FIELD_NUMBER: _ClassVar[int]
    MARKER_ICON_FIELD_NUMBER: _ClassVar[int]
    MARKER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARKER_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    timeline_id: str
    entry_id: int
    time: int
    type: ETimelineEntryType
    game_mode: int
    range_title: str
    range_duration: int
    range_possible_clip: int
    timestamp_title: str
    marker_icon: str
    marker_description: str
    marker_priority: int
    screenshot_handle: int
    achievement_name: str
    tag: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CTimelineTag]
    phase_id: str
    attributes: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CPhaseAttribute]
    def __init__(self, timeline_id: _Optional[str] = ..., entry_id: _Optional[int] = ..., time: _Optional[int] = ..., type: _Optional[_Union[ETimelineEntryType, str]] = ..., game_mode: _Optional[int] = ..., range_title: _Optional[str] = ..., range_duration: _Optional[int] = ..., range_possible_clip: _Optional[int] = ..., timestamp_title: _Optional[str] = ..., marker_icon: _Optional[str] = ..., marker_description: _Optional[str] = ..., marker_priority: _Optional[int] = ..., screenshot_handle: _Optional[int] = ..., achievement_name: _Optional[str] = ..., tag: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CTimelineTag, _Mapping]]] = ..., phase_id: _Optional[str] = ..., attributes: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CPhaseAttribute, _Mapping]]] = ...) -> None: ...

class CGameRecording_TimelineEntryChanged_Notification(_message.Message):
    __slots__ = ("entry", "game_id")
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    entry: CTimelineEntry
    game_id: int
    def __init__(self, entry: _Optional[_Union[CTimelineEntry, _Mapping]] = ..., game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_TimelineEntryRemoved_Notification(_message.Message):
    __slots__ = ("game_id", "timeline_id", "entry_id")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    timeline_id: str
    entry_id: int
    def __init__(self, game_id: _Optional[int] = ..., timeline_id: _Optional[str] = ..., entry_id: _Optional[int] = ...) -> None: ...

class CGameRecording_LowDiskSpace_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_PostGameHighlightsChanged_Notification(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_OpenOverlayToGamePhase_Notification(_message.Message):
    __slots__ = ("game_id", "phase_id")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    phase_id: str
    def __init__(self, game_id: _Optional[int] = ..., phase_id: _Optional[str] = ...) -> None: ...

class CGameRecording_OpenOverlayToTimelineEvent_Notification(_message.Message):
    __slots__ = ("game_id", "entry_id")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    entry_id: int
    def __init__(self, game_id: _Optional[int] = ..., entry_id: _Optional[int] = ...) -> None: ...

class CGameRecording_PhaseListChanged_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_ClipSummary(_message.Message):
    __slots__ = ("clip_id", "game_id", "duration_ms", "date_recorded", "start_timeline_id", "start_offset_ms", "published_file_id", "file_size", "name", "date_clipped", "temporary", "original_device", "original_gaming_device_type", "date_downloaded", "thumbnail_url", "thumbnail_width", "thumbnail_height")
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    DATE_RECORDED_FIELD_NUMBER: _ClassVar[int]
    START_TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_CLIPPED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DEVICE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    game_id: int
    duration_ms: int
    date_recorded: int
    start_timeline_id: str
    start_offset_ms: int
    published_file_id: int
    file_size: int
    name: str
    date_clipped: int
    temporary: bool
    original_device: str
    original_gaming_device_type: int
    date_downloaded: int
    thumbnail_url: str
    thumbnail_width: int
    thumbnail_height: int
    def __init__(self, clip_id: _Optional[str] = ..., game_id: _Optional[int] = ..., duration_ms: _Optional[int] = ..., date_recorded: _Optional[int] = ..., start_timeline_id: _Optional[str] = ..., start_offset_ms: _Optional[int] = ..., published_file_id: _Optional[int] = ..., file_size: _Optional[int] = ..., name: _Optional[str] = ..., date_clipped: _Optional[int] = ..., temporary: bool = ..., original_device: _Optional[str] = ..., original_gaming_device_type: _Optional[int] = ..., date_downloaded: _Optional[int] = ..., thumbnail_url: _Optional[str] = ..., thumbnail_width: _Optional[int] = ..., thumbnail_height: _Optional[int] = ...) -> None: ...

class CGameRecording_SaveClip_Request(_message.Message):
    __slots__ = ("game_id", "start", "end", "name", "src_clip_id", "temporary", "force_thumbnail")
    class Position(_message.Message):
        __slots__ = ("timeline_id", "offset_ms")
        TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
        timeline_id: str
        offset_ms: int
        def __init__(self, timeline_id: _Optional[str] = ..., offset_ms: _Optional[int] = ...) -> None: ...
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SRC_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    FORCE_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    start: CGameRecording_SaveClip_Request.Position
    end: CGameRecording_SaveClip_Request.Position
    name: str
    src_clip_id: str
    temporary: bool
    force_thumbnail: bool
    def __init__(self, game_id: _Optional[int] = ..., start: _Optional[_Union[CGameRecording_SaveClip_Request.Position, _Mapping]] = ..., end: _Optional[_Union[CGameRecording_SaveClip_Request.Position, _Mapping]] = ..., name: _Optional[str] = ..., src_clip_id: _Optional[str] = ..., temporary: bool = ..., force_thumbnail: bool = ...) -> None: ...

class CGameRecording_SaveClip_Response(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: CGameRecording_ClipSummary
    def __init__(self, summary: _Optional[_Union[CGameRecording_ClipSummary, _Mapping]] = ...) -> None: ...

class CGameRecording_DeleteClip_Request(_message.Message):
    __slots__ = ("clip_id",)
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    def __init__(self, clip_id: _Optional[str] = ...) -> None: ...

class CGameRecording_DeleteClip_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_ExportClip_Settings(_message.Message):
    __slots__ = ("bitrate_kbps", "width", "height", "frames_per_second", "codec")
    BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FRAMES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    bitrate_kbps: int
    width: int
    height: int
    frames_per_second: int
    codec: _enums_pb2.EExportCodec
    def __init__(self, bitrate_kbps: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., frames_per_second: _Optional[int] = ..., codec: _Optional[_Union[_enums_pb2.EExportCodec, str]] = ...) -> None: ...

class CGameRecording_ExportClip_Request(_message.Message):
    __slots__ = ("clip_id", "export_mp4_path", "settings", "use_unique_filename")
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    EXPORT_MP4_PATH_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    USE_UNIQUE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    export_mp4_path: str
    settings: CGameRecording_ExportClip_Settings
    use_unique_filename: bool
    def __init__(self, clip_id: _Optional[str] = ..., export_mp4_path: _Optional[str] = ..., settings: _Optional[_Union[CGameRecording_ExportClip_Settings, _Mapping]] = ..., use_unique_filename: bool = ...) -> None: ...

class CGameRecording_ExportClip_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_ExportClipPreview_Request(_message.Message):
    __slots__ = ("clip_id", "settings", "run_policy_checks")
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RUN_POLICY_CHECKS_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    settings: CGameRecording_ExportClip_Settings
    run_policy_checks: bool
    def __init__(self, clip_id: _Optional[str] = ..., settings: _Optional[_Union[CGameRecording_ExportClip_Settings, _Mapping]] = ..., run_policy_checks: bool = ...) -> None: ...

class CGameRecording_ExportClipPreview_Response(_message.Message):
    __slots__ = ("estimated_size", "settings")
    ESTIMATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    estimated_size: int
    settings: CGameRecording_ExportClip_Settings
    def __init__(self, estimated_size: _Optional[int] = ..., settings: _Optional[_Union[CGameRecording_ExportClip_Settings, _Mapping]] = ...) -> None: ...

class CGameRecording_TakeScreenshot_Request(_message.Message):
    __slots__ = ("game_id", "timeline_id", "timeline_offset_ms")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    timeline_id: str
    timeline_offset_ms: int
    def __init__(self, game_id: _Optional[int] = ..., timeline_id: _Optional[str] = ..., timeline_offset_ms: _Optional[int] = ...) -> None: ...

class CGameRecording_TakeScreenshot_Response(_message.Message):
    __slots__ = ("screenshot_id",)
    SCREENSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    screenshot_id: int
    def __init__(self, screenshot_id: _Optional[int] = ...) -> None: ...

class CGameRecording_UploadClipToSteam_Request(_message.Message):
    __slots__ = ("clip_id", "title", "desc", "visibility")
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    title: str
    desc: str
    visibility: int
    def __init__(self, clip_id: _Optional[str] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., visibility: _Optional[int] = ...) -> None: ...

class CGameRecording_UploadClipToSteam_Response(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: CGameRecording_ClipSummary
    def __init__(self, summary: _Optional[_Union[CGameRecording_ClipSummary, _Mapping]] = ...) -> None: ...

class CGameRecording_ZipClip_Request(_message.Message):
    __slots__ = ("clip_id",)
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    def __init__(self, clip_id: _Optional[str] = ...) -> None: ...

class CGameRecording_ZipClip_Response(_message.Message):
    __slots__ = ("zip_path",)
    ZIP_PATH_FIELD_NUMBER: _ClassVar[int]
    zip_path: str
    def __init__(self, zip_path: _Optional[str] = ...) -> None: ...

class CGameRecording_GetClips_Request(_message.Message):
    __slots__ = ("game_id", "created_after", "include_temporary")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    created_after: int
    include_temporary: bool
    def __init__(self, game_id: _Optional[int] = ..., created_after: _Optional[int] = ..., include_temporary: bool = ...) -> None: ...

class CGameRecording_GetClips_Response(_message.Message):
    __slots__ = ("clip",)
    CLIP_FIELD_NUMBER: _ClassVar[int]
    clip: _containers.RepeatedCompositeFieldContainer[CGameRecording_ClipSummary]
    def __init__(self, clip: _Optional[_Iterable[_Union[CGameRecording_ClipSummary, _Mapping]]] = ...) -> None: ...

class CGameRecording_GetAndTrimPostGameHighlights_Request(_message.Message):
    __slots__ = ("game_id", "created_after")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AFTER_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    created_after: int
    def __init__(self, game_id: _Optional[int] = ..., created_after: _Optional[int] = ...) -> None: ...

class CGameRecording_GetAndTrimPostGameHighlights_Response(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_webuimessages_gamerecordingfiles_pb2.CGameRecordingTimelineEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_webuimessages_gamerecordingfiles_pb2.CGameRecordingTimelineEvent, _Mapping]]] = ...) -> None: ...

class CGameRecording_UserAddTimelineEntry_Request(_message.Message):
    __slots__ = ("game_id", "entry", "clip_id")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    entry: CTimelineEntry
    clip_id: str
    def __init__(self, game_id: _Optional[int] = ..., entry: _Optional[_Union[CTimelineEntry, _Mapping]] = ..., clip_id: _Optional[str] = ...) -> None: ...

class CGameRecording_UserAddTimelineEntry_Response(_message.Message):
    __slots__ = ("entry_id",)
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: int
    def __init__(self, entry_id: _Optional[int] = ...) -> None: ...

class CGameRecording_UserUpdateTimelineEntry_Request(_message.Message):
    __slots__ = ("game_id", "entry", "clip_id")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    entry: CTimelineEntry
    clip_id: str
    def __init__(self, game_id: _Optional[int] = ..., entry: _Optional[_Union[CTimelineEntry, _Mapping]] = ..., clip_id: _Optional[str] = ...) -> None: ...

class CGameRecording_UserUpdateTimelineEntry_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_UserRemoveTimelineEntry_Request(_message.Message):
    __slots__ = ("game_id", "timeline_id", "entry_id", "clip_id")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    timeline_id: str
    entry_id: int
    clip_id: str
    def __init__(self, game_id: _Optional[int] = ..., timeline_id: _Optional[str] = ..., entry_id: _Optional[int] = ..., clip_id: _Optional[str] = ...) -> None: ...

class CGameRecording_UserRemoveTimelineEntry_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_ManuallyDeleteRecordingsForApps_Request(_message.Message):
    __slots__ = ("game_ids",)
    GAME_IDS_FIELD_NUMBER: _ClassVar[int]
    game_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, game_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CGameRecording_ManuallyDeleteRecordingsForApps_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetTotalDiskSpaceUsage_Request(_message.Message):
    __slots__ = ("folder_path", "type")
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    type: EDiskSpaceType
    def __init__(self, folder_path: _Optional[str] = ..., type: _Optional[_Union[EDiskSpaceType, str]] = ...) -> None: ...

class CGameRecording_GetTotalDiskSpaceUsage_Response(_message.Message):
    __slots__ = ("size",)
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class CGameRecording_GetThumbnails_Request(_message.Message):
    __slots__ = ("recording_id", "clip_id", "timeline_id", "start_offset_us", "major_axis", "time_precision", "format")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_US_FIELD_NUMBER: _ClassVar[int]
    MAJOR_AXIS_FIELD_NUMBER: _ClassVar[int]
    TIME_PRECISION_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    recording_id: str
    clip_id: str
    timeline_id: str
    start_offset_us: _containers.RepeatedScalarFieldContainer[int]
    major_axis: int
    time_precision: EThumbnailTimePrecision
    format: EThumbnailFormat
    def __init__(self, recording_id: _Optional[str] = ..., clip_id: _Optional[str] = ..., timeline_id: _Optional[str] = ..., start_offset_us: _Optional[_Iterable[int]] = ..., major_axis: _Optional[int] = ..., time_precision: _Optional[_Union[EThumbnailTimePrecision, str]] = ..., format: _Optional[_Union[EThumbnailFormat, str]] = ...) -> None: ...

class CGameRecording_GetThumbnails_Response(_message.Message):
    __slots__ = ("thumbnails",)
    class Thumbnail(_message.Message):
        __slots__ = ("image_data", "width", "height")
        IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        image_data: bytes
        width: int
        height: int
        def __init__(self, image_data: _Optional[bytes] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    THUMBNAILS_FIELD_NUMBER: _ClassVar[int]
    thumbnails: _containers.RepeatedCompositeFieldContainer[CGameRecording_GetThumbnails_Response.Thumbnail]
    def __init__(self, thumbnails: _Optional[_Iterable[_Union[CGameRecording_GetThumbnails_Response.Thumbnail, _Mapping]]] = ...) -> None: ...

class CGameRecording_StartRecording_Request(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_StartRecording_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_StopRecording_Request(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_StopRecording_Response(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: CGameRecording_ClipSummary
    def __init__(self, summary: _Optional[_Union[CGameRecording_ClipSummary, _Mapping]] = ...) -> None: ...

class CGameRecording_GetRecordingSize_Request(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_GetRecordingSize_Response(_message.Message):
    __slots__ = ("file_size",)
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_size: int
    def __init__(self, file_size: _Optional[int] = ...) -> None: ...

class CGameRecording_CleanupBackgroundRecordings_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_CleanupBackgroundRecordings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetPlatformCapabilities_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetPlatformCapabilities_Response(_message.Message):
    __slots__ = ("per_process_audio_capture",)
    PER_PROCESS_AUDIO_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    per_process_audio_capture: bool
    def __init__(self, per_process_audio_capture: bool = ...) -> None: ...

class CGameRecording_ClipCreated_Notification(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: CGameRecording_ClipSummary
    def __init__(self, summary: _Optional[_Union[CGameRecording_ClipSummary, _Mapping]] = ...) -> None: ...

class CGameRecording_ClipDeleted_Notification(_message.Message):
    __slots__ = ("clip_id", "game_id")
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    clip_id: str
    game_id: int
    def __init__(self, clip_id: _Optional[str] = ..., game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_ExportProgress_Notification(_message.Message):
    __slots__ = ("progress", "clip_id", "eresult")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    progress: float
    clip_id: str
    eresult: int
    def __init__(self, progress: _Optional[float] = ..., clip_id: _Optional[str] = ..., eresult: _Optional[int] = ...) -> None: ...

class CGameRecording_PerGameSettings(_message.Message):
    __slots__ = ("gameid", "enabled", "minutes", "bitrate", "infinite")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    MINUTES_FIELD_NUMBER: _ClassVar[int]
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    INFINITE_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    enabled: bool
    minutes: int
    bitrate: str
    infinite: bool
    def __init__(self, gameid: _Optional[int] = ..., enabled: bool = ..., minutes: _Optional[int] = ..., bitrate: _Optional[str] = ..., infinite: bool = ...) -> None: ...

class CGameRecording_GetPerGameSettings_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetPerGameSettings_Response(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[CGameRecording_PerGameSettings]
    def __init__(self, settings: _Optional[_Iterable[_Union[CGameRecording_PerGameSettings, _Mapping]]] = ...) -> None: ...

class CGameRecording_SetPerGameSettings_Request(_message.Message):
    __slots__ = ("game_settings",)
    GAME_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    game_settings: CGameRecording_PerGameSettings
    def __init__(self, game_settings: _Optional[_Union[CGameRecording_PerGameSettings, _Mapping]] = ...) -> None: ...

class CGameRecording_SetPerGameSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_DeletePerGameSettings_Request(_message.Message):
    __slots__ = ("gameid",)
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    def __init__(self, gameid: _Optional[int] = ...) -> None: ...

class CGameRecording_DeletePerGameSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_UploadProgress_Notification(_message.Message):
    __slots__ = ("progress", "clip_id", "eresult")
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    progress: float
    clip_id: str
    eresult: int
    def __init__(self, progress: _Optional[float] = ..., clip_id: _Optional[str] = ..., eresult: _Optional[int] = ...) -> None: ...

class CGameRecording_SwitchBackgroundRecordingGame_Request(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CGameRecording_SwitchBackgroundRecordingGame_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GameRecording(_service.service): ...

class GameRecording_Stub(GameRecording): ...
