import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGameRecordingFile(_message.Message):
    __slots__ = ("timelines", "postgame_events", "temporary_clips", "tags")
    TIMELINES_FIELD_NUMBER: _ClassVar[int]
    POSTGAME_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_CLIPS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    timelines: _containers.RepeatedCompositeFieldContainer[CGameRecordingTimelineMetadata]
    postgame_events: _containers.RepeatedCompositeFieldContainer[CGameRecordingPostGameSummary]
    temporary_clips: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedCompositeFieldContainer[CGameRecordingTag]
    def __init__(self, timelines: _Optional[_Iterable[_Union[CGameRecordingTimelineMetadata, _Mapping]]] = ..., postgame_events: _Optional[_Iterable[_Union[CGameRecordingPostGameSummary, _Mapping]]] = ..., temporary_clips: _Optional[_Iterable[str]] = ..., tags: _Optional[_Iterable[_Union[CGameRecordingTag, _Mapping]]] = ...) -> None: ...

class CGameRecordingClipFile(_message.Message):
    __slots__ = ("timelines", "first_timeline_start_offset_ms", "date_recorded", "game_id", "published_file_id", "size_in_bytes", "name", "temporary", "original_device", "original_gaming_device_type", "date_downloaded", "thumbnail_width", "thumbnail_height", "tags", "phases")
    TIMELINES_FIELD_NUMBER: _ClassVar[int]
    FIRST_TIMELINE_START_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DATE_RECORDED_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_DEVICE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    PHASES_FIELD_NUMBER: _ClassVar[int]
    timelines: _containers.RepeatedCompositeFieldContainer[CGameRecordingTimelineMetadata]
    first_timeline_start_offset_ms: int
    date_recorded: int
    game_id: int
    published_file_id: int
    size_in_bytes: int
    name: str
    temporary: bool
    original_device: str
    original_gaming_device_type: int
    date_downloaded: int
    thumbnail_width: int
    thumbnail_height: int
    tags: _containers.RepeatedCompositeFieldContainer[CGameRecordingTag]
    phases: _containers.RepeatedCompositeFieldContainer[CGameRecordingPhase]
    def __init__(self, timelines: _Optional[_Iterable[_Union[CGameRecordingTimelineMetadata, _Mapping]]] = ..., first_timeline_start_offset_ms: _Optional[int] = ..., date_recorded: _Optional[int] = ..., game_id: _Optional[int] = ..., published_file_id: _Optional[int] = ..., size_in_bytes: _Optional[int] = ..., name: _Optional[str] = ..., temporary: bool = ..., original_device: _Optional[str] = ..., original_gaming_device_type: _Optional[int] = ..., date_downloaded: _Optional[int] = ..., thumbnail_width: _Optional[int] = ..., thumbnail_height: _Optional[int] = ..., tags: _Optional[_Iterable[_Union[CGameRecordingTag, _Mapping]]] = ..., phases: _Optional[_Iterable[_Union[CGameRecordingPhase, _Mapping]]] = ...) -> None: ...

class CGameRecordingTimelineMetadata(_message.Message):
    __slots__ = ("timeline_id", "game_id", "date_recorded", "duration_ms", "recordings", "phases", "significant_events")
    class Recording(_message.Message):
        __slots__ = ("recording_id", "start_offset_ms", "duration_ms", "recording_type", "delete_on_cleanup", "video_manager_clip_id", "video_manager_video_id", "cdn_manifest_url", "file_size", "recording_zero_timeline_offset_ms")
        RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
        START_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        RECORDING_TYPE_FIELD_NUMBER: _ClassVar[int]
        DELETE_ON_CLEANUP_FIELD_NUMBER: _ClassVar[int]
        VIDEO_MANAGER_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
        VIDEO_MANAGER_VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
        CDN_MANIFEST_URL_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        RECORDING_ZERO_TIMELINE_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
        recording_id: str
        start_offset_ms: int
        duration_ms: int
        recording_type: _enums_pb2.EGameRecordingType
        delete_on_cleanup: bool
        video_manager_clip_id: int
        video_manager_video_id: int
        cdn_manifest_url: str
        file_size: int
        recording_zero_timeline_offset_ms: int
        def __init__(self, recording_id: _Optional[str] = ..., start_offset_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., recording_type: _Optional[_Union[_enums_pb2.EGameRecordingType, str]] = ..., delete_on_cleanup: bool = ..., video_manager_clip_id: _Optional[int] = ..., video_manager_video_id: _Optional[int] = ..., cdn_manifest_url: _Optional[str] = ..., file_size: _Optional[int] = ..., recording_zero_timeline_offset_ms: _Optional[int] = ...) -> None: ...
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    DATE_RECORDED_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    RECORDINGS_FIELD_NUMBER: _ClassVar[int]
    PHASES_FIELD_NUMBER: _ClassVar[int]
    SIGNIFICANT_EVENTS_FIELD_NUMBER: _ClassVar[int]
    timeline_id: str
    game_id: int
    date_recorded: int
    duration_ms: int
    recordings: _containers.RepeatedCompositeFieldContainer[CGameRecordingTimelineMetadata.Recording]
    phases: _containers.RepeatedCompositeFieldContainer[CGameRecordingPhase]
    significant_events: _containers.RepeatedCompositeFieldContainer[CGameRecordingTimelineEvent]
    def __init__(self, timeline_id: _Optional[str] = ..., game_id: _Optional[int] = ..., date_recorded: _Optional[int] = ..., duration_ms: _Optional[int] = ..., recordings: _Optional[_Iterable[_Union[CGameRecordingTimelineMetadata.Recording, _Mapping]]] = ..., phases: _Optional[_Iterable[_Union[CGameRecordingPhase, _Mapping]]] = ..., significant_events: _Optional[_Iterable[_Union[CGameRecordingTimelineEvent, _Mapping]]] = ...) -> None: ...

class CGameRecordingPostGameSummary(_message.Message):
    __slots__ = ("game_id", "events")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    events: _containers.RepeatedCompositeFieldContainer[CGameRecordingTimelineEvent]
    def __init__(self, game_id: _Optional[int] = ..., events: _Optional[_Iterable[_Union[CGameRecordingTimelineEvent, _Mapping]]] = ...) -> None: ...

class CGameRecordingTimelineEvent(_message.Message):
    __slots__ = ("game_id", "rt_created", "possible_clip", "timeline_id", "entry_id", "timeline_offset_ms", "duration_ms", "marker_icon", "marker_title", "user_marker")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    RT_CREATED_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_CLIP_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    MARKER_ICON_FIELD_NUMBER: _ClassVar[int]
    MARKER_TITLE_FIELD_NUMBER: _ClassVar[int]
    USER_MARKER_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    rt_created: int
    possible_clip: int
    timeline_id: str
    entry_id: int
    timeline_offset_ms: int
    duration_ms: int
    marker_icon: str
    marker_title: str
    user_marker: bool
    def __init__(self, game_id: _Optional[int] = ..., rt_created: _Optional[int] = ..., possible_clip: _Optional[int] = ..., timeline_id: _Optional[str] = ..., entry_id: _Optional[int] = ..., timeline_offset_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ..., marker_icon: _Optional[str] = ..., marker_title: _Optional[str] = ..., user_marker: bool = ...) -> None: ...

class CGameRecordingTag(_message.Message):
    __slots__ = ("game_id", "tag", "references")
    class Timeline(_message.Message):
        __slots__ = ("clip_id", "timeline_id", "offset_ms")
        CLIP_ID_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
        OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
        clip_id: str
        timeline_id: str
        offset_ms: int
        def __init__(self, clip_id: _Optional[str] = ..., timeline_id: _Optional[str] = ..., offset_ms: _Optional[int] = ...) -> None: ...
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    tag: CTimelineTag
    references: _containers.RepeatedCompositeFieldContainer[CGameRecordingTag.Timeline]
    def __init__(self, game_id: _Optional[int] = ..., tag: _Optional[_Union[CTimelineTag, _Mapping]] = ..., references: _Optional[_Iterable[_Union[CGameRecordingTag.Timeline, _Mapping]]] = ...) -> None: ...

class CGameRecordingTagInstance(_message.Message):
    __slots__ = ("timeline_id", "entry_id", "timeline_offset_ms", "duration_ms")
    TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    timeline_id: str
    entry_id: int
    timeline_offset_ms: int
    duration_ms: int
    def __init__(self, timeline_id: _Optional[str] = ..., entry_id: _Optional[int] = ..., timeline_offset_ms: _Optional[int] = ..., duration_ms: _Optional[int] = ...) -> None: ...

class CGameRecordingPhase(_message.Message):
    __slots__ = ("phase_id", "duration_ms", "tags", "contained_tags", "background_timeline_offset", "attributes")
    class Tag(_message.Message):
        __slots__ = ("name", "group")
        NAME_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        name: str
        group: str
        def __init__(self, name: _Optional[str] = ..., group: _Optional[str] = ...) -> None: ...
    PHASE_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CONTAINED_TAGS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_TIMELINE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    phase_id: str
    duration_ms: int
    tags: _containers.RepeatedCompositeFieldContainer[CGameRecordingPhase.Tag]
    contained_tags: _containers.RepeatedCompositeFieldContainer[CGameRecordingPhase.Tag]
    background_timeline_offset: int
    attributes: _containers.RepeatedCompositeFieldContainer[CPhaseAttribute]
    def __init__(self, phase_id: _Optional[str] = ..., duration_ms: _Optional[int] = ..., tags: _Optional[_Iterable[_Union[CGameRecordingPhase.Tag, _Mapping]]] = ..., contained_tags: _Optional[_Iterable[_Union[CGameRecordingPhase.Tag, _Mapping]]] = ..., background_timeline_offset: _Optional[int] = ..., attributes: _Optional[_Iterable[_Union[CPhaseAttribute, _Mapping]]] = ...) -> None: ...

class CTimelineTag(_message.Message):
    __slots__ = ("name", "group", "icon", "priority")
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    group: str
    icon: str
    priority: int
    def __init__(self, name: _Optional[str] = ..., group: _Optional[str] = ..., icon: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...

class CPhaseAttribute(_message.Message):
    __slots__ = ("group", "value", "priority")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    group: str
    value: str
    priority: int
    def __init__(self, group: _Optional[str] = ..., value: _Optional[str] = ..., priority: _Optional[int] = ...) -> None: ...
