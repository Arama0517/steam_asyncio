import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgFactoryResetState(_message.Message):
    __slots__ = ("is_running", "progress", "is_restart_pending", "rtime_estimated_completion")
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    IS_RESTART_PENDING_FIELD_NUMBER: _ClassVar[int]
    RTIME_ESTIMATED_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    is_running: bool
    progress: int
    is_restart_pending: bool
    rtime_estimated_completion: int
    def __init__(self, is_running: bool = ..., progress: _Optional[int] = ..., is_restart_pending: bool = ..., rtime_estimated_completion: _Optional[int] = ...) -> None: ...

class CSteamOSManagerState(_message.Message):
    __slots__ = ("is_service_available", "os_version", "is_mandatory_update_available", "startup_movie_variant", "is_status_led_control_available", "factory_reset_state", "is_tdp_limit_available", "tdp_limit_min", "tdp_limit_max", "is_cec_available", "is_wifi_debug_supported", "is_wifi_debug_force_disabled", "is_wifi_force_wpa_supplicant_supported")
    IS_SERVICE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_MANDATORY_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STARTUP_MOVIE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    IS_STATUS_LED_CONTROL_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FACTORY_RESET_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_TDP_LIMIT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    TDP_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
    TDP_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
    IS_CEC_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_WIFI_DEBUG_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_WIFI_DEBUG_FORCE_DISABLED_FIELD_NUMBER: _ClassVar[int]
    IS_WIFI_FORCE_WPA_SUPPLICANT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    is_service_available: bool
    os_version: str
    is_mandatory_update_available: bool
    startup_movie_variant: _enums_pb2.EStartupMovieVariant
    is_status_led_control_available: bool
    factory_reset_state: CMsgFactoryResetState
    is_tdp_limit_available: bool
    tdp_limit_min: int
    tdp_limit_max: int
    is_cec_available: bool
    is_wifi_debug_supported: bool
    is_wifi_debug_force_disabled: bool
    is_wifi_force_wpa_supplicant_supported: bool
    def __init__(self, is_service_available: bool = ..., os_version: _Optional[str] = ..., is_mandatory_update_available: bool = ..., startup_movie_variant: _Optional[_Union[_enums_pb2.EStartupMovieVariant, str]] = ..., is_status_led_control_available: bool = ..., factory_reset_state: _Optional[_Union[CMsgFactoryResetState, _Mapping]] = ..., is_tdp_limit_available: bool = ..., tdp_limit_min: _Optional[int] = ..., tdp_limit_max: _Optional[int] = ..., is_cec_available: bool = ..., is_wifi_debug_supported: bool = ..., is_wifi_debug_force_disabled: bool = ..., is_wifi_force_wpa_supplicant_supported: bool = ...) -> None: ...

class CSteamOSManager_GetState_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSManager_GetState_Response(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: CSteamOSManagerState
    def __init__(self, state: _Optional[_Union[CSteamOSManagerState, _Mapping]] = ...) -> None: ...

class CSteamOSManager_StateChanged_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSManager_IsTelemetryHelperAvailable_Request(_message.Message):
    __slots__ = ("etype",)
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    etype: _enums_pb2.ESLSHelper
    def __init__(self, etype: _Optional[_Union[_enums_pb2.ESLSHelper, str]] = ...) -> None: ...

class CSteamOSManager_IsTelemetryHelperAvailable_Response(_message.Message):
    __slots__ = ("available",)
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    available: bool
    def __init__(self, available: bool = ...) -> None: ...

class CSteamOSManager_OptOutOfSideloadedClient_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSManager_OptOutOfSideloadedClient_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSManager_ApplyMandatoryUpdate_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSManager_ApplyMandatoryUpdate_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSManager_FactoryReset_Request(_message.Message):
    __slots__ = ("reset_os", "reset_user_data")
    RESET_OS_FIELD_NUMBER: _ClassVar[int]
    RESET_USER_DATA_FIELD_NUMBER: _ClassVar[int]
    reset_os: bool
    reset_user_data: bool
    def __init__(self, reset_os: bool = ..., reset_user_data: bool = ...) -> None: ...

class CSteamOSManager_FactoryReset_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSSLSPlugin(_message.Message):
    __slots__ = ("etype", "is_available", "is_enabled")
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    etype: _enums_pb2.ESLSHelper
    is_available: bool
    is_enabled: bool
    def __init__(self, etype: _Optional[_Union[_enums_pb2.ESLSHelper, str]] = ..., is_available: bool = ..., is_enabled: bool = ...) -> None: ...

class CSteamOSSLSState(_message.Message):
    __slots__ = ("is_available", "is_enabled", "plugins")
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    is_available: bool
    is_enabled: bool
    plugins: _containers.RepeatedCompositeFieldContainer[CSteamOSSLSPlugin]
    def __init__(self, is_available: bool = ..., is_enabled: bool = ..., plugins: _Optional[_Iterable[_Union[CSteamOSSLSPlugin, _Mapping]]] = ...) -> None: ...

class CSteamOSSLS_GetState_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSSLS_GetState_Response(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: CSteamOSSLSState
    def __init__(self, state: _Optional[_Union[CSteamOSSLSState, _Mapping]] = ...) -> None: ...

class CSteamOSSLS_StateChanged_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSSLS_SetEnabled_Request(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CSteamOSSLS_SetEnabled_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamOSSLS_SetPluginEnabled_Request(_message.Message):
    __slots__ = ("etype", "enabled")
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    etype: _enums_pb2.ESLSHelper
    enabled: bool
    def __init__(self, etype: _Optional[_Union[_enums_pb2.ESLSHelper, str]] = ..., enabled: bool = ...) -> None: ...

class CSteamOSSLS_SetPluginEnabled_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SteamOSManager(_service.service): ...

class SteamOSManager_Stub(SteamOSManager): ...

class SteamOSSLS(_service.service): ...

class SteamOSSLS_Stub(SteamOSSLS): ...
