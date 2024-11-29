import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDataPublisher_ClientContentCorruptionReport_Notification(_message.Message):
    __slots__ = ("appid", "depotid", "download_source", "objectid", "cellid", "is_manifest", "object_size", "corruption_type", "used_https", "oc_proxy_detected")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOTID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    OBJECTID_FIELD_NUMBER: _ClassVar[int]
    CELLID_FIELD_NUMBER: _ClassVar[int]
    IS_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    OBJECT_SIZE_FIELD_NUMBER: _ClassVar[int]
    CORRUPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    USED_HTTPS_FIELD_NUMBER: _ClassVar[int]
    OC_PROXY_DETECTED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depotid: int
    download_source: str
    objectid: str
    cellid: int
    is_manifest: bool
    object_size: int
    corruption_type: int
    used_https: bool
    oc_proxy_detected: bool
    def __init__(self, appid: _Optional[int] = ..., depotid: _Optional[int] = ..., download_source: _Optional[str] = ..., objectid: _Optional[str] = ..., cellid: _Optional[int] = ..., is_manifest: bool = ..., object_size: _Optional[int] = ..., corruption_type: _Optional[int] = ..., used_https: bool = ..., oc_proxy_detected: bool = ...) -> None: ...

class CDataPublisher_ClientUpdateAppJob_Notification(_message.Message):
    __slots__ = ("app_id", "depot_ids", "app_state", "job_app_error", "error_details", "job_duration", "files_validation_failed", "job_bytes_downloaded", "job_bytes_staged", "bytes_comitted", "start_app_state", "stats_machine_id", "branch_name", "total_bytes_downloaded", "total_bytes_staged", "total_bytes_restored", "is_borrowed", "is_free_weekend", "total_bytes_patched", "total_bytes_saved", "cell_id", "is_workshop", "is_shader", "seconds_not_played")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_IDS_FIELD_NUMBER: _ClassVar[int]
    APP_STATE_FIELD_NUMBER: _ClassVar[int]
    JOB_APP_ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    JOB_DURATION_FIELD_NUMBER: _ClassVar[int]
    FILES_VALIDATION_FAILED_FIELD_NUMBER: _ClassVar[int]
    JOB_BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    JOB_BYTES_STAGED_FIELD_NUMBER: _ClassVar[int]
    BYTES_COMITTED_FIELD_NUMBER: _ClassVar[int]
    START_APP_STATE_FIELD_NUMBER: _ClassVar[int]
    STATS_MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    BRANCH_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_STAGED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_RESTORED_FIELD_NUMBER: _ClassVar[int]
    IS_BORROWED_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_WEEKEND_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_PATCHED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_SAVED_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_WORKSHOP_FIELD_NUMBER: _ClassVar[int]
    IS_SHADER_FIELD_NUMBER: _ClassVar[int]
    SECONDS_NOT_PLAYED_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    depot_ids: _containers.RepeatedScalarFieldContainer[int]
    app_state: int
    job_app_error: int
    error_details: str
    job_duration: int
    files_validation_failed: int
    job_bytes_downloaded: int
    job_bytes_staged: int
    bytes_comitted: int
    start_app_state: int
    stats_machine_id: int
    branch_name: str
    total_bytes_downloaded: int
    total_bytes_staged: int
    total_bytes_restored: int
    is_borrowed: bool
    is_free_weekend: bool
    total_bytes_patched: int
    total_bytes_saved: int
    cell_id: int
    is_workshop: bool
    is_shader: bool
    seconds_not_played: int
    def __init__(self, app_id: _Optional[int] = ..., depot_ids: _Optional[_Iterable[int]] = ..., app_state: _Optional[int] = ..., job_app_error: _Optional[int] = ..., error_details: _Optional[str] = ..., job_duration: _Optional[int] = ..., files_validation_failed: _Optional[int] = ..., job_bytes_downloaded: _Optional[int] = ..., job_bytes_staged: _Optional[int] = ..., bytes_comitted: _Optional[int] = ..., start_app_state: _Optional[int] = ..., stats_machine_id: _Optional[int] = ..., branch_name: _Optional[str] = ..., total_bytes_downloaded: _Optional[int] = ..., total_bytes_staged: _Optional[int] = ..., total_bytes_restored: _Optional[int] = ..., is_borrowed: bool = ..., is_free_weekend: bool = ..., total_bytes_patched: _Optional[int] = ..., total_bytes_saved: _Optional[int] = ..., cell_id: _Optional[int] = ..., is_workshop: bool = ..., is_shader: bool = ..., seconds_not_played: _Optional[int] = ...) -> None: ...

class CDataPublisher_GetVRDeviceInfo_Request(_message.Message):
    __slots__ = ("month_count",)
    MONTH_COUNT_FIELD_NUMBER: _ClassVar[int]
    month_count: int
    def __init__(self, month_count: _Optional[int] = ...) -> None: ...

class CDataPublisher_GetVRDeviceInfo_Response(_message.Message):
    __slots__ = ("device",)
    class Device(_message.Message):
        __slots__ = ("name", "ref", "aggregation_ref", "total", "driver", "device_class")
        NAME_FIELD_NUMBER: _ClassVar[int]
        REF_FIELD_NUMBER: _ClassVar[int]
        AGGREGATION_REF_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        DRIVER_FIELD_NUMBER: _ClassVar[int]
        DEVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
        name: str
        ref: int
        aggregation_ref: int
        total: int
        driver: str
        device_class: int
        def __init__(self, name: _Optional[str] = ..., ref: _Optional[int] = ..., aggregation_ref: _Optional[int] = ..., total: _Optional[int] = ..., driver: _Optional[str] = ..., device_class: _Optional[int] = ...) -> None: ...
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: _containers.RepeatedCompositeFieldContainer[CDataPublisher_GetVRDeviceInfo_Response.Device]
    def __init__(self, device: _Optional[_Iterable[_Union[CDataPublisher_GetVRDeviceInfo_Response.Device, _Mapping]]] = ...) -> None: ...

class CDataPublisher_SetVRDeviceInfoAggregationReference_Request(_message.Message):
    __slots__ = ("ref", "aggregation_ref")
    REF_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_REF_FIELD_NUMBER: _ClassVar[int]
    ref: int
    aggregation_ref: int
    def __init__(self, ref: _Optional[int] = ..., aggregation_ref: _Optional[int] = ...) -> None: ...

class CDataPublisher_SetVRDeviceInfoAggregationReference_Response(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class CDataPublisher_AddVRDeviceInfo_Request(_message.Message):
    __slots__ = ("manufacturer", "model", "driver", "controller_type", "device_class")
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DRIVER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    manufacturer: str
    model: str
    driver: str
    controller_type: str
    device_class: int
    def __init__(self, manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., driver: _Optional[str] = ..., controller_type: _Optional[str] = ..., device_class: _Optional[int] = ...) -> None: ...

class CDataPublisher_AddVRDeviceInfo_Response(_message.Message):
    __slots__ = ("result", "ref")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    result: int
    ref: int
    def __init__(self, result: _Optional[int] = ..., ref: _Optional[int] = ...) -> None: ...

class CValveHWSurvey_GetSurveySchedule_Request(_message.Message):
    __slots__ = ("surveydatetoken", "surveydatetokenversion")
    SURVEYDATETOKEN_FIELD_NUMBER: _ClassVar[int]
    SURVEYDATETOKENVERSION_FIELD_NUMBER: _ClassVar[int]
    surveydatetoken: str
    surveydatetokenversion: int
    def __init__(self, surveydatetoken: _Optional[str] = ..., surveydatetokenversion: _Optional[int] = ...) -> None: ...

class CValveHWSurvey_GetSurveySchedule_Response(_message.Message):
    __slots__ = ("surveydatetoken", "surveydatetokenversion")
    SURVEYDATETOKEN_FIELD_NUMBER: _ClassVar[int]
    SURVEYDATETOKENVERSION_FIELD_NUMBER: _ClassVar[int]
    surveydatetoken: int
    surveydatetokenversion: int
    def __init__(self, surveydatetoken: _Optional[int] = ..., surveydatetokenversion: _Optional[int] = ...) -> None: ...

class DataPublisher(_service.service): ...

class DataPublisher_Stub(DataPublisher): ...

class ValveHWSurvey(_service.service): ...

class ValveHWSurvey_Stub(ValveHWSurvey): ...
