import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import clientmetrics_pb2 as _clientmetrics_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ESteamPipeWorkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESteamPipeClientWorkType_Invalid: _ClassVar[ESteamPipeWorkType]
    k_ESteamPipeClientWorkType_StageFromChunkStores: _ClassVar[ESteamPipeWorkType]

class ESteamPipeOperationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESteamPipeOperationType_Invalid: _ClassVar[ESteamPipeOperationType]
    k_ESteamPipeOperationType_DecryptCPU: _ClassVar[ESteamPipeOperationType]
    k_ESteamPipeOperationType_DiskRead: _ClassVar[ESteamPipeOperationType]
    k_ESteamPipeOperationType_DiskWrite: _ClassVar[ESteamPipeOperationType]

class EClipShareMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EClipShareMethod_Chat: _ClassVar[EClipShareMethod]
    k_EClipShareMethod_Clipboard: _ClassVar[EClipShareMethod]
    k_EClipShareMethod_File: _ClassVar[EClipShareMethod]
    k_EClipShareMethod_SendClip: _ClassVar[EClipShareMethod]
    k_EClipShareMethod_SaveToMedia: _ClassVar[EClipShareMethod]
    k_EClipShareMethod_CreateLink: _ClassVar[EClipShareMethod]

class EClipRangeMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EClipRangeMethod_CreateClipButton: _ClassVar[EClipRangeMethod]
    k_EClipRangeMethod_Highlight: _ClassVar[EClipRangeMethod]
    k_EClipRangeMethod_BeginEndButtons: _ClassVar[EClipRangeMethod]
    k_EClipRangeMethod_ContextMenu: _ClassVar[EClipRangeMethod]
    k_EClipRangeMethod_Drag: _ClassVar[EClipRangeMethod]
    k_EClipRangeMethod_EntireClip: _ClassVar[EClipRangeMethod]
    k_EClipRangeMethod_PhaseRecording: _ClassVar[EClipRangeMethod]
k_ESteamPipeClientWorkType_Invalid: ESteamPipeWorkType
k_ESteamPipeClientWorkType_StageFromChunkStores: ESteamPipeWorkType
k_ESteamPipeOperationType_Invalid: ESteamPipeOperationType
k_ESteamPipeOperationType_DecryptCPU: ESteamPipeOperationType
k_ESteamPipeOperationType_DiskRead: ESteamPipeOperationType
k_ESteamPipeOperationType_DiskWrite: ESteamPipeOperationType
k_EClipShareMethod_Chat: EClipShareMethod
k_EClipShareMethod_Clipboard: EClipShareMethod
k_EClipShareMethod_File: EClipShareMethod
k_EClipShareMethod_SendClip: EClipShareMethod
k_EClipShareMethod_SaveToMedia: EClipShareMethod
k_EClipShareMethod_CreateLink: EClipShareMethod
k_EClipRangeMethod_CreateClipButton: EClipRangeMethod
k_EClipRangeMethod_Highlight: EClipRangeMethod
k_EClipRangeMethod_BeginEndButtons: EClipRangeMethod
k_EClipRangeMethod_ContextMenu: EClipRangeMethod
k_EClipRangeMethod_Drag: EClipRangeMethod
k_EClipRangeMethod_EntireClip: EClipRangeMethod
k_EClipRangeMethod_PhaseRecording: EClipRangeMethod

class CClientMetrics_AppInterfaceCreation(_message.Message):
    __slots__ = ("raw_version", "requested_interface_type")
    RAW_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    raw_version: str
    requested_interface_type: str
    def __init__(self, raw_version: _Optional[str] = ..., requested_interface_type: _Optional[str] = ...) -> None: ...

class CClientMetrics_AppInterfaceMethodCounts(_message.Message):
    __slots__ = ("interface_name", "method_name", "call_count")
    INTERFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    CALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    interface_name: str
    method_name: str
    call_count: int
    def __init__(self, interface_name: _Optional[str] = ..., method_name: _Optional[str] = ..., call_count: _Optional[int] = ...) -> None: ...

class CClientMetrics_AppInterfaceStats_Notification(_message.Message):
    __slots__ = ("game_id", "interfaces_created", "methods_called", "session_length_seconds")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_CREATED_FIELD_NUMBER: _ClassVar[int]
    METHODS_CALLED_FIELD_NUMBER: _ClassVar[int]
    SESSION_LENGTH_SECONDS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    interfaces_created: _containers.RepeatedCompositeFieldContainer[CClientMetrics_AppInterfaceCreation]
    methods_called: _containers.RepeatedCompositeFieldContainer[CClientMetrics_AppInterfaceMethodCounts]
    session_length_seconds: int
    def __init__(self, game_id: _Optional[int] = ..., interfaces_created: _Optional[_Iterable[_Union[CClientMetrics_AppInterfaceCreation, _Mapping]]] = ..., methods_called: _Optional[_Iterable[_Union[CClientMetrics_AppInterfaceMethodCounts, _Mapping]]] = ..., session_length_seconds: _Optional[int] = ...) -> None: ...

class CClientMetrics_IPv6Connectivity_Result(_message.Message):
    __slots__ = ("protocol_tested", "connectivity_state")
    PROTOCOL_TESTED_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITY_STATE_FIELD_NUMBER: _ClassVar[int]
    protocol_tested: int
    connectivity_state: int
    def __init__(self, protocol_tested: _Optional[int] = ..., connectivity_state: _Optional[int] = ...) -> None: ...

class CClientMetrics_IPv6Connectivity_Notification(_message.Message):
    __slots__ = ("cell_id", "results", "private_ip_is_rfc6598")
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_IP_IS_RFC6598_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    results: _containers.RepeatedCompositeFieldContainer[CClientMetrics_IPv6Connectivity_Result]
    private_ip_is_rfc6598: bool
    def __init__(self, cell_id: _Optional[int] = ..., results: _Optional[_Iterable[_Union[CClientMetrics_IPv6Connectivity_Result, _Mapping]]] = ..., private_ip_is_rfc6598: bool = ...) -> None: ...

class CClientMetrics_SteamPipeWorkStats_Operation(_message.Message):
    __slots__ = ("type", "num_ops", "num_bytes", "busy_time_ms", "idle_time_ms", "sum_run_time_ms", "sum_wait_time_ms")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_OPS_FIELD_NUMBER: _ClassVar[int]
    NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    BUSY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SUM_RUN_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SUM_WAIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    type: ESteamPipeOperationType
    num_ops: int
    num_bytes: int
    busy_time_ms: int
    idle_time_ms: int
    sum_run_time_ms: int
    sum_wait_time_ms: int
    def __init__(self, type: _Optional[_Union[ESteamPipeOperationType, str]] = ..., num_ops: _Optional[int] = ..., num_bytes: _Optional[int] = ..., busy_time_ms: _Optional[int] = ..., idle_time_ms: _Optional[int] = ..., sum_run_time_ms: _Optional[int] = ..., sum_wait_time_ms: _Optional[int] = ...) -> None: ...

class CClientMetrics_SteamPipeWorkStats_Notification(_message.Message):
    __slots__ = ("appid", "depotid", "work_type", "operations", "hardware_type")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOTID_FIELD_NUMBER: _ClassVar[int]
    WORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depotid: int
    work_type: ESteamPipeWorkType
    operations: _containers.RepeatedCompositeFieldContainer[CClientMetrics_SteamPipeWorkStats_Operation]
    hardware_type: int
    def __init__(self, appid: _Optional[int] = ..., depotid: _Optional[int] = ..., work_type: _Optional[_Union[ESteamPipeWorkType, str]] = ..., operations: _Optional[_Iterable[_Union[CClientMetrics_SteamPipeWorkStats_Operation, _Mapping]]] = ..., hardware_type: _Optional[int] = ...) -> None: ...

class CClientMetrics_ReportReactUsage_Notification(_message.Message):
    __slots__ = ("product", "version", "routes", "components", "actions")
    class RouteData(_message.Message):
        __slots__ = ("route", "count")
        ROUTE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        route: str
        count: int
        def __init__(self, route: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    class ComponentData(_message.Message):
        __slots__ = ("component", "count")
        COMPONENT_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        component: str
        count: int
        def __init__(self, component: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    class ActionData(_message.Message):
        __slots__ = ("action", "count")
        ACTION_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        action: str
        count: int
        def __init__(self, action: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    product: str
    version: str
    routes: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ReportReactUsage_Notification.RouteData]
    components: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ReportReactUsage_Notification.ComponentData]
    actions: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ReportReactUsage_Notification.ActionData]
    def __init__(self, product: _Optional[str] = ..., version: _Optional[str] = ..., routes: _Optional[_Iterable[_Union[CClientMetrics_ReportReactUsage_Notification.RouteData, _Mapping]]] = ..., components: _Optional[_Iterable[_Union[CClientMetrics_ReportReactUsage_Notification.ComponentData, _Mapping]]] = ..., actions: _Optional[_Iterable[_Union[CClientMetrics_ReportReactUsage_Notification.ActionData, _Mapping]]] = ...) -> None: ...

class CClientMetrics_ReportClientError_Notification(_message.Message):
    __slots__ = ("product", "version", "errors")
    class Error(_message.Message):
        __slots__ = ("identifier", "message", "count")
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        message: str
        count: int
        def __init__(self, identifier: _Optional[str] = ..., message: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    product: str
    version: str
    errors: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ReportClientError_Notification.Error]
    def __init__(self, product: _Optional[str] = ..., version: _Optional[str] = ..., errors: _Optional[_Iterable[_Union[CClientMetrics_ReportClientError_Notification.Error, _Mapping]]] = ...) -> None: ...

class CClientMetrics_ClientBootstrap_Notification(_message.Message):
    __slots__ = ("summary",)
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    summary: _clientmetrics_pb2.CClientMetrics_ClientBootstrap_Summary
    def __init__(self, summary: _Optional[_Union[_clientmetrics_pb2.CClientMetrics_ClientBootstrap_Summary, _Mapping]] = ...) -> None: ...

class CClientMetrics_DownloadRates_Notification(_message.Message):
    __slots__ = ("cell_id", "stats", "throttling_kbps", "os_type", "device_type")
    class StatsInfo(_message.Message):
        __slots__ = ("source_type", "source_id", "bytes", "host_name", "microseconds", "used_ipv6", "proxied", "used_http2", "cache_hits", "cache_misses", "hit_bytes", "miss_bytes")
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        BYTES_FIELD_NUMBER: _ClassVar[int]
        HOST_NAME_FIELD_NUMBER: _ClassVar[int]
        MICROSECONDS_FIELD_NUMBER: _ClassVar[int]
        USED_IPV6_FIELD_NUMBER: _ClassVar[int]
        PROXIED_FIELD_NUMBER: _ClassVar[int]
        USED_HTTP2_FIELD_NUMBER: _ClassVar[int]
        CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
        CACHE_MISSES_FIELD_NUMBER: _ClassVar[int]
        HIT_BYTES_FIELD_NUMBER: _ClassVar[int]
        MISS_BYTES_FIELD_NUMBER: _ClassVar[int]
        source_type: int
        source_id: int
        bytes: int
        host_name: str
        microseconds: int
        used_ipv6: bool
        proxied: bool
        used_http2: bool
        cache_hits: int
        cache_misses: int
        hit_bytes: int
        miss_bytes: int
        def __init__(self, source_type: _Optional[int] = ..., source_id: _Optional[int] = ..., bytes: _Optional[int] = ..., host_name: _Optional[str] = ..., microseconds: _Optional[int] = ..., used_ipv6: bool = ..., proxied: bool = ..., used_http2: bool = ..., cache_hits: _Optional[int] = ..., cache_misses: _Optional[int] = ..., hit_bytes: _Optional[int] = ..., miss_bytes: _Optional[int] = ...) -> None: ...
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    THROTTLING_KBPS_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    stats: _containers.RepeatedCompositeFieldContainer[CClientMetrics_DownloadRates_Notification.StatsInfo]
    throttling_kbps: int
    os_type: int
    device_type: int
    def __init__(self, cell_id: _Optional[int] = ..., stats: _Optional[_Iterable[_Union[CClientMetrics_DownloadRates_Notification.StatsInfo, _Mapping]]] = ..., throttling_kbps: _Optional[int] = ..., os_type: _Optional[int] = ..., device_type: _Optional[int] = ...) -> None: ...

class CClientMetrics_ContentValidation_Notification(_message.Message):
    __slots__ = ("validation_result", "app_id", "staged_files", "user_initiated", "early_out", "chunks_scanned", "chunks_corrupt", "bytes_scanned", "chunk_bytes_corrupt", "total_file_size_corrupt")
    VALIDATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STAGED_FILES_FIELD_NUMBER: _ClassVar[int]
    USER_INITIATED_FIELD_NUMBER: _ClassVar[int]
    EARLY_OUT_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_SCANNED_FIELD_NUMBER: _ClassVar[int]
    CHUNKS_CORRUPT_FIELD_NUMBER: _ClassVar[int]
    BYTES_SCANNED_FIELD_NUMBER: _ClassVar[int]
    CHUNK_BYTES_CORRUPT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILE_SIZE_CORRUPT_FIELD_NUMBER: _ClassVar[int]
    validation_result: int
    app_id: int
    staged_files: bool
    user_initiated: bool
    early_out: bool
    chunks_scanned: int
    chunks_corrupt: int
    bytes_scanned: int
    chunk_bytes_corrupt: int
    total_file_size_corrupt: int
    def __init__(self, validation_result: _Optional[int] = ..., app_id: _Optional[int] = ..., staged_files: bool = ..., user_initiated: bool = ..., early_out: bool = ..., chunks_scanned: _Optional[int] = ..., chunks_corrupt: _Optional[int] = ..., bytes_scanned: _Optional[int] = ..., chunk_bytes_corrupt: _Optional[int] = ..., total_file_size_corrupt: _Optional[int] = ...) -> None: ...

class CClientMetrics_CloudAppSyncStats_Notification(_message.Message):
    __slots__ = ("app_id", "platform_type", "preload", "blocking_app_launch", "files_uploaded", "files_downloaded", "files_deleted", "bytes_uploaded", "bytes_downloaded", "microsec_total", "microsec_init_caches", "microsec_validate_state", "microsec_ac_launch", "microsec_ac_prep_user_files", "microsec_ac_exit", "microsec_build_sync_list", "microsec_delete_files", "microsec_download_files", "microsec_upload_files", "hardware_type", "files_managed")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_FIELD_NUMBER: _ClassVar[int]
    BLOCKING_APP_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    FILES_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    FILES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    FILES_DELETED_FIELD_NUMBER: _ClassVar[int]
    BYTES_UPLOADED_FIELD_NUMBER: _ClassVar[int]
    BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_TOTAL_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_INIT_CACHES_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_VALIDATE_STATE_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_AC_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_AC_PREP_USER_FILES_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_AC_EXIT_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_BUILD_SYNC_LIST_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_DELETE_FILES_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_DOWNLOAD_FILES_FIELD_NUMBER: _ClassVar[int]
    MICROSEC_UPLOAD_FILES_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILES_MANAGED_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    platform_type: int
    preload: bool
    blocking_app_launch: bool
    files_uploaded: int
    files_downloaded: int
    files_deleted: int
    bytes_uploaded: int
    bytes_downloaded: int
    microsec_total: int
    microsec_init_caches: int
    microsec_validate_state: int
    microsec_ac_launch: int
    microsec_ac_prep_user_files: int
    microsec_ac_exit: int
    microsec_build_sync_list: int
    microsec_delete_files: int
    microsec_download_files: int
    microsec_upload_files: int
    hardware_type: int
    files_managed: int
    def __init__(self, app_id: _Optional[int] = ..., platform_type: _Optional[int] = ..., preload: bool = ..., blocking_app_launch: bool = ..., files_uploaded: _Optional[int] = ..., files_downloaded: _Optional[int] = ..., files_deleted: _Optional[int] = ..., bytes_uploaded: _Optional[int] = ..., bytes_downloaded: _Optional[int] = ..., microsec_total: _Optional[int] = ..., microsec_init_caches: _Optional[int] = ..., microsec_validate_state: _Optional[int] = ..., microsec_ac_launch: _Optional[int] = ..., microsec_ac_prep_user_files: _Optional[int] = ..., microsec_ac_exit: _Optional[int] = ..., microsec_build_sync_list: _Optional[int] = ..., microsec_delete_files: _Optional[int] = ..., microsec_download_files: _Optional[int] = ..., microsec_upload_files: _Optional[int] = ..., hardware_type: _Optional[int] = ..., files_managed: _Optional[int] = ...) -> None: ...

class CClientMetrics_ContentDownloadResponse_Counts_Notification(_message.Message):
    __slots__ = ("cell_id", "data")
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    data: _clientmetrics_pb2.CClientMetrics_ContentDownloadResponse_Hosts
    def __init__(self, cell_id: _Optional[int] = ..., data: _Optional[_Union[_clientmetrics_pb2.CClientMetrics_ContentDownloadResponse_Hosts, _Mapping]] = ...) -> None: ...

class CClientMetrics_ReportClientArgs_Notification(_message.Message):
    __slots__ = ("client_args", "gpu_webview_regkey_disabled", "suppress_gpu_chrome", "browser_not_supported", "hw_accel_video_regkey_disabled", "mini_mode_enabled", "fps_counter_enabled", "library_low_bandwidth_mode_enabled", "library_low_perf_mode_enabled", "gr_mode")
    CLIENT_ARGS_FIELD_NUMBER: _ClassVar[int]
    GPU_WEBVIEW_REGKEY_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_GPU_CHROME_FIELD_NUMBER: _ClassVar[int]
    BROWSER_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    HW_ACCEL_VIDEO_REGKEY_DISABLED_FIELD_NUMBER: _ClassVar[int]
    MINI_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FPS_COUNTER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_LOW_BANDWIDTH_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_LOW_PERF_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GR_MODE_FIELD_NUMBER: _ClassVar[int]
    client_args: _containers.RepeatedScalarFieldContainer[str]
    gpu_webview_regkey_disabled: bool
    suppress_gpu_chrome: bool
    browser_not_supported: bool
    hw_accel_video_regkey_disabled: bool
    mini_mode_enabled: bool
    fps_counter_enabled: bool
    library_low_bandwidth_mode_enabled: bool
    library_low_perf_mode_enabled: bool
    gr_mode: int
    def __init__(self, client_args: _Optional[_Iterable[str]] = ..., gpu_webview_regkey_disabled: bool = ..., suppress_gpu_chrome: bool = ..., browser_not_supported: bool = ..., hw_accel_video_regkey_disabled: bool = ..., mini_mode_enabled: bool = ..., fps_counter_enabled: bool = ..., library_low_bandwidth_mode_enabled: bool = ..., library_low_perf_mode_enabled: bool = ..., gr_mode: _Optional[int] = ...) -> None: ...

class CClientMetrics_ReportLinuxStats_Notification(_message.Message):
    __slots__ = ("glibc_version_major", "glibc_version_minor", "account_type", "launcher_type", "game_server_appid", "process_name")
    GLIBC_VERSION_MAJOR_FIELD_NUMBER: _ClassVar[int]
    GLIBC_VERSION_MINOR_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_APPID_FIELD_NUMBER: _ClassVar[int]
    PROCESS_NAME_FIELD_NUMBER: _ClassVar[int]
    glibc_version_major: int
    glibc_version_minor: int
    account_type: int
    launcher_type: int
    game_server_appid: int
    process_name: str
    def __init__(self, glibc_version_major: _Optional[int] = ..., glibc_version_minor: _Optional[int] = ..., account_type: _Optional[int] = ..., launcher_type: _Optional[int] = ..., game_server_appid: _Optional[int] = ..., process_name: _Optional[str] = ...) -> None: ...

class CClientMetrics_ClipShare_Notification(_message.Message):
    __slots__ = ("eresult", "share_method", "seconds", "bytes", "gameid")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    SHARE_METHOD_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    share_method: EClipShareMethod
    seconds: float
    bytes: int
    gameid: int
    def __init__(self, eresult: _Optional[int] = ..., share_method: _Optional[_Union[EClipShareMethod, str]] = ..., seconds: _Optional[float] = ..., bytes: _Optional[int] = ..., gameid: _Optional[int] = ...) -> None: ...

class CClientMetrics_ClipRange_Notification(_message.Message):
    __slots__ = ("original_range_method", "start", "end", "seconds", "gameid")
    class RelativeRangeEdge(_message.Message):
        __slots__ = ("original_range_method", "latest_range_method", "delta_ms")
        ORIGINAL_RANGE_METHOD_FIELD_NUMBER: _ClassVar[int]
        LATEST_RANGE_METHOD_FIELD_NUMBER: _ClassVar[int]
        DELTA_MS_FIELD_NUMBER: _ClassVar[int]
        original_range_method: EClipRangeMethod
        latest_range_method: EClipRangeMethod
        delta_ms: int
        def __init__(self, original_range_method: _Optional[_Union[EClipRangeMethod, str]] = ..., latest_range_method: _Optional[_Union[EClipRangeMethod, str]] = ..., delta_ms: _Optional[int] = ...) -> None: ...
    ORIGINAL_RANGE_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    original_range_method: EClipRangeMethod
    start: CClientMetrics_ClipRange_Notification.RelativeRangeEdge
    end: CClientMetrics_ClipRange_Notification.RelativeRangeEdge
    seconds: float
    gameid: int
    def __init__(self, original_range_method: _Optional[_Union[EClipRangeMethod, str]] = ..., start: _Optional[_Union[CClientMetrics_ClipRange_Notification.RelativeRangeEdge, _Mapping]] = ..., end: _Optional[_Union[CClientMetrics_ClipRange_Notification.RelativeRangeEdge, _Mapping]] = ..., seconds: _Optional[float] = ..., gameid: _Optional[int] = ...) -> None: ...

class CClientMetrics_EndGameRecording_Notification(_message.Message):
    __slots__ = ("recording_type", "seconds", "bytes", "gameid", "instant_clip")
    RECORDING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    INSTANT_CLIP_FIELD_NUMBER: _ClassVar[int]
    recording_type: _enums_pb2.EGameRecordingType
    seconds: float
    bytes: int
    gameid: int
    instant_clip: bool
    def __init__(self, recording_type: _Optional[_Union[_enums_pb2.EGameRecordingType, str]] = ..., seconds: _Optional[float] = ..., bytes: _Optional[int] = ..., gameid: _Optional[int] = ..., instant_clip: bool = ...) -> None: ...

class ClientMetrics(_service.service): ...

class ClientMetrics_Stub(ClientMetrics): ...
