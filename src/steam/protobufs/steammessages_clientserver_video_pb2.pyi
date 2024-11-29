import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgVideoGameRecordingRepresentation(_message.Message):
    __slots__ = ("representation_name", "horizontal_resolution", "vertical_resolution", "frame_rate", "bandwidth", "audio_sample_rate", "frame_rate_string", "codec", "audio_channel_config", "segment_info")
    REPRESENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_STRING_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    representation_name: str
    horizontal_resolution: int
    vertical_resolution: int
    frame_rate: float
    bandwidth: int
    audio_sample_rate: int
    frame_rate_string: str
    codec: str
    audio_channel_config: int
    segment_info: _containers.RepeatedCompositeFieldContainer[CVideo_GameRecordingSegmentInfo]
    def __init__(self, representation_name: _Optional[str] = ..., horizontal_resolution: _Optional[int] = ..., vertical_resolution: _Optional[int] = ..., frame_rate: _Optional[float] = ..., bandwidth: _Optional[int] = ..., audio_sample_rate: _Optional[int] = ..., frame_rate_string: _Optional[str] = ..., codec: _Optional[str] = ..., audio_channel_config: _Optional[int] = ..., segment_info: _Optional[_Iterable[_Union[CVideo_GameRecordingSegmentInfo, _Mapping]]] = ...) -> None: ...

class CMsgVideoGameRecordingComponent(_message.Message):
    __slots__ = ("component_name", "contents", "segment_size", "file_type", "representations")
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATIONS_FIELD_NUMBER: _ClassVar[int]
    component_name: str
    contents: int
    segment_size: int
    file_type: str
    representations: _containers.RepeatedCompositeFieldContainer[CMsgVideoGameRecordingRepresentation]
    def __init__(self, component_name: _Optional[str] = ..., contents: _Optional[int] = ..., segment_size: _Optional[int] = ..., file_type: _Optional[str] = ..., representations: _Optional[_Iterable[_Union[CMsgVideoGameRecordingRepresentation, _Mapping]]] = ...) -> None: ...

class CMsgVideoGameRecordingDef(_message.Message):
    __slots__ = ("steamid", "app_id", "num_segments", "length_milliseconds", "segment_duration_timescale", "segment_duration", "components", "start_time_ms", "start_offset_in_timeline_ms")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_DURATION_TIMESCALE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_DURATION_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_OFFSET_IN_TIMELINE_MS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    app_id: int
    num_segments: int
    length_milliseconds: int
    segment_duration_timescale: int
    segment_duration: int
    components: _containers.RepeatedCompositeFieldContainer[CMsgVideoGameRecordingComponent]
    start_time_ms: int
    start_offset_in_timeline_ms: int
    def __init__(self, steamid: _Optional[int] = ..., app_id: _Optional[int] = ..., num_segments: _Optional[int] = ..., length_milliseconds: _Optional[int] = ..., segment_duration_timescale: _Optional[int] = ..., segment_duration: _Optional[int] = ..., components: _Optional[_Iterable[_Union[CMsgVideoGameRecordingComponent, _Mapping]]] = ..., start_time_ms: _Optional[int] = ..., start_offset_in_timeline_ms: _Optional[int] = ...) -> None: ...

class CVideo_GameRecordingSegmentInfo(_message.Message):
    __slots__ = ("segment_number", "segment_size_bytes", "component_name", "representation_name")
    SEGMENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    segment_number: int
    segment_size_bytes: int
    component_name: str
    representation_name: str
    def __init__(self, segment_number: _Optional[int] = ..., segment_size_bytes: _Optional[int] = ..., component_name: _Optional[str] = ..., representation_name: _Optional[str] = ...) -> None: ...

class CVideo_GameRecordingSegmentUploadInfo(_message.Message):
    __slots__ = ("segment_info", "url_host", "url_path", "use_https", "request_headers")
    class HTTPHeaders(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SEGMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    URL_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    segment_info: CVideo_GameRecordingSegmentInfo
    url_host: str
    url_path: str
    use_https: bool
    request_headers: _containers.RepeatedCompositeFieldContainer[CVideo_GameRecordingSegmentUploadInfo.HTTPHeaders]
    def __init__(self, segment_info: _Optional[_Union[CVideo_GameRecordingSegmentInfo, _Mapping]] = ..., url_host: _Optional[str] = ..., url_path: _Optional[str] = ..., use_https: bool = ..., request_headers: _Optional[_Iterable[_Union[CVideo_GameRecordingSegmentUploadInfo.HTTPHeaders, _Mapping]]] = ...) -> None: ...
