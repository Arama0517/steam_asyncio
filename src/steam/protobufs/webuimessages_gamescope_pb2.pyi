import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgDisplayInfo(_message.Message):
    __slots__ = ("make", "model", "connector_name", "supported_refresh_rates", "supported_frame_rates", "is_external", "is_hdr_capable", "is_vrr_capable")
    MAKE_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_REFRESH_RATES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FRAME_RATES_FIELD_NUMBER: _ClassVar[int]
    IS_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_CAPABLE_FIELD_NUMBER: _ClassVar[int]
    IS_VRR_CAPABLE_FIELD_NUMBER: _ClassVar[int]
    make: str
    model: str
    connector_name: str
    supported_refresh_rates: _containers.RepeatedScalarFieldContainer[int]
    supported_frame_rates: _containers.RepeatedScalarFieldContainer[int]
    is_external: bool
    is_hdr_capable: bool
    is_vrr_capable: bool
    def __init__(self, make: _Optional[str] = ..., model: _Optional[str] = ..., connector_name: _Optional[str] = ..., supported_refresh_rates: _Optional[_Iterable[int]] = ..., supported_frame_rates: _Optional[_Iterable[int]] = ..., is_external: bool = ..., is_hdr_capable: bool = ..., is_vrr_capable: bool = ...) -> None: ...

class CMsgGamescopeState(_message.Message):
    __slots__ = ("is_service_available", "is_reshade_supported", "is_app_hdr_enabled", "is_app_refresh_rate_supported", "active_display_info", "is_app_refresh_rate_capable", "is_refresh_rate_switching_supported", "is_refresh_rate_switching_restricted", "is_hdr_visualization_supported", "is_mura_correction_supported", "is_global_action_binding_supported")
    IS_SERVICE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_RESHADE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_APP_HDR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_APP_REFRESH_RATE_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_DISPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_APP_REFRESH_RATE_CAPABLE_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_RATE_SWITCHING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_REFRESH_RATE_SWITCHING_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_VISUALIZATION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_MURA_CORRECTION_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_GLOBAL_ACTION_BINDING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    is_service_available: bool
    is_reshade_supported: bool
    is_app_hdr_enabled: bool
    is_app_refresh_rate_supported: bool
    active_display_info: CMsgDisplayInfo
    is_app_refresh_rate_capable: bool
    is_refresh_rate_switching_supported: bool
    is_refresh_rate_switching_restricted: bool
    is_hdr_visualization_supported: bool
    is_mura_correction_supported: bool
    is_global_action_binding_supported: bool
    def __init__(self, is_service_available: bool = ..., is_reshade_supported: bool = ..., is_app_hdr_enabled: bool = ..., is_app_refresh_rate_supported: bool = ..., active_display_info: _Optional[_Union[CMsgDisplayInfo, _Mapping]] = ..., is_app_refresh_rate_capable: bool = ..., is_refresh_rate_switching_supported: bool = ..., is_refresh_rate_switching_restricted: bool = ..., is_hdr_visualization_supported: bool = ..., is_mura_correction_supported: bool = ..., is_global_action_binding_supported: bool = ...) -> None: ...

class CGamescope_GetState_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGamescope_GetState_Response(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: CMsgGamescopeState
    def __init__(self, state: _Optional[_Union[CMsgGamescopeState, _Mapping]] = ...) -> None: ...

class CGamescope_StateChanged_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGamescope_SetBlurParams_Request(_message.Message):
    __slots__ = ("mode", "radius", "fade_duration_ms")
    MODE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    FADE_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    mode: _enums_pb2.EGamescopeBlurMode
    radius: int
    fade_duration_ms: int
    def __init__(self, mode: _Optional[_Union[_enums_pb2.EGamescopeBlurMode, str]] = ..., radius: _Optional[int] = ..., fade_duration_ms: _Optional[int] = ...) -> None: ...

class CGamescope_SetBlurParams_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGamescope_ReArmMuraCalibration_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGamescope_ReArmMuraCalibration_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Gamescope(_service.service): ...

class Gamescope_Stub(Gamescope): ...
