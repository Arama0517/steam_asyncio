import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import steammessages_clientserver_video_pb2 as _steammessages_clientserver_video_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CVideoManagerClipID(_message.Message):
    __slots__ = ("video_manager_clip_id", "video_manager_video_id", "server_timeline_id", "manifest_url", "duration_ms", "start_offset_ms")
    VIDEO_MANAGER_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_MANAGER_VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMELINE_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_URL_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    video_manager_clip_id: int
    video_manager_video_id: int
    server_timeline_id: int
    manifest_url: str
    duration_ms: int
    start_offset_ms: int
    def __init__(self, video_manager_clip_id: _Optional[int] = ..., video_manager_video_id: _Optional[int] = ..., server_timeline_id: _Optional[int] = ..., manifest_url: _Optional[str] = ..., duration_ms: _Optional[int] = ..., start_offset_ms: _Optional[int] = ...) -> None: ...

class CGameRecordingClip(_message.Message):
    __slots__ = ("clip_id", "gameid", "date_recorded", "total_file_size_bytes", "video_ids", "owner_steamid", "upload_complete", "duration_ms")
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    DATE_RECORDED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    VIDEO_IDS_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    clip_id: int
    gameid: int
    date_recorded: int
    total_file_size_bytes: int
    video_ids: _containers.RepeatedCompositeFieldContainer[CVideoManagerClipID]
    owner_steamid: int
    upload_complete: bool
    duration_ms: int
    def __init__(self, clip_id: _Optional[int] = ..., gameid: _Optional[int] = ..., date_recorded: _Optional[int] = ..., total_file_size_bytes: _Optional[int] = ..., video_ids: _Optional[_Iterable[_Union[CVideoManagerClipID, _Mapping]]] = ..., owner_steamid: _Optional[int] = ..., upload_complete: bool = ..., duration_ms: _Optional[int] = ...) -> None: ...

class CGameRecording_CreateShareClip_Request(_message.Message):
    __slots__ = ("clip", "video_def")
    CLIP_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DEF_FIELD_NUMBER: _ClassVar[int]
    clip: CGameRecordingClip
    video_def: _containers.RepeatedCompositeFieldContainer[_steammessages_clientserver_video_pb2.CMsgVideoGameRecordingDef]
    def __init__(self, clip: _Optional[_Union[CGameRecordingClip, _Mapping]] = ..., video_def: _Optional[_Iterable[_Union[_steammessages_clientserver_video_pb2.CMsgVideoGameRecordingDef, _Mapping]]] = ...) -> None: ...

class CGameRecording_CreateShareClip_Response(_message.Message):
    __slots__ = ("clip",)
    CLIP_FIELD_NUMBER: _ClassVar[int]
    clip: CGameRecordingClip
    def __init__(self, clip: _Optional[_Union[CGameRecordingClip, _Mapping]] = ...) -> None: ...

class CGameRecording_DeleteSharedClip_Request(_message.Message):
    __slots__ = ("clip_id",)
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    clip_id: int
    def __init__(self, clip_id: _Optional[int] = ...) -> None: ...

class CGameRecording_DeleteSharedClip_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameRecording_GetSingleSharedClip_Request(_message.Message):
    __slots__ = ("clip_id",)
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    clip_id: int
    def __init__(self, clip_id: _Optional[int] = ...) -> None: ...

class CGameRecording_GetSingleSharedClip_Response(_message.Message):
    __slots__ = ("clip",)
    CLIP_FIELD_NUMBER: _ClassVar[int]
    clip: CGameRecordingClip
    def __init__(self, clip: _Optional[_Union[CGameRecordingClip, _Mapping]] = ...) -> None: ...

class CVideo_BeginGameRecordingSegmentsUpload_Request(_message.Message):
    __slots__ = ("recording_id", "component_name", "representation_name", "segments_to_store")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_TO_STORE_FIELD_NUMBER: _ClassVar[int]
    recording_id: int
    component_name: str
    representation_name: str
    segments_to_store: _containers.RepeatedCompositeFieldContainer[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentInfo]
    def __init__(self, recording_id: _Optional[int] = ..., component_name: _Optional[str] = ..., representation_name: _Optional[str] = ..., segments_to_store: _Optional[_Iterable[_Union[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentInfo, _Mapping]]] = ...) -> None: ...

class CVideo_BeginGameRecordingSegmentsUpload_Response(_message.Message):
    __slots__ = ("segments_needed", "call_again")
    SEGMENTS_NEEDED_FIELD_NUMBER: _ClassVar[int]
    CALL_AGAIN_FIELD_NUMBER: _ClassVar[int]
    segments_needed: _containers.RepeatedCompositeFieldContainer[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentUploadInfo]
    call_again: bool
    def __init__(self, segments_needed: _Optional[_Iterable[_Union[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentUploadInfo, _Mapping]]] = ..., call_again: bool = ...) -> None: ...

class CVideo_CommitGameRecordingSegmentsUpload_Request(_message.Message):
    __slots__ = ("recording_id", "component_name", "representation_name", "first_segment_number", "num_segments", "upload_result")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEGMENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NUM_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_RESULT_FIELD_NUMBER: _ClassVar[int]
    recording_id: int
    component_name: str
    representation_name: str
    first_segment_number: int
    num_segments: int
    upload_result: int
    def __init__(self, recording_id: _Optional[int] = ..., component_name: _Optional[str] = ..., representation_name: _Optional[str] = ..., first_segment_number: _Optional[int] = ..., num_segments: _Optional[int] = ..., upload_result: _Optional[int] = ...) -> None: ...

class CVideo_CommitGameRecordingSegmentsUpload_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CVideo_GameRecordingGetNextBatchOfSegmentsToUpload_Request(_message.Message):
    __slots__ = ("recording_id",)
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    recording_id: int
    def __init__(self, recording_id: _Optional[int] = ...) -> None: ...

class CVideo_GameRecordingGetNextBatchOfSegmentsToUpload_Response(_message.Message):
    __slots__ = ("segments_needed",)
    SEGMENTS_NEEDED_FIELD_NUMBER: _ClassVar[int]
    segments_needed: _containers.RepeatedCompositeFieldContainer[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentUploadInfo]
    def __init__(self, segments_needed: _Optional[_Iterable[_Union[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentUploadInfo, _Mapping]]] = ...) -> None: ...

class CVideo_GameRecordingCommitSegmentUploads_Request(_message.Message):
    __slots__ = ("recording_id", "segments_uploaded")
    RECORDING_ID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    recording_id: int
    segments_uploaded: _containers.RepeatedCompositeFieldContainer[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentInfo]
    def __init__(self, recording_id: _Optional[int] = ..., segments_uploaded: _Optional[_Iterable[_Union[_steammessages_clientserver_video_pb2.CVideo_GameRecordingSegmentInfo, _Mapping]]] = ...) -> None: ...

class CVideo_GameRecordingCommitSegmentUploads_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GameRecordingClip(_service.service): ...

class GameRecordingClip_Stub(GameRecordingClip): ...

class VideoClip(_service.service): ...

class VideoClip_Stub(VideoClip): ...
