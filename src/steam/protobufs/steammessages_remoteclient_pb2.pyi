import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_remoteclient_discovery_pb2 as _steammessages_remoteclient_discovery_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgRemoteClientStatus(_message.Message):
    __slots__ = ("client_id", "instance_id", "status")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    instance_id: int
    status: _steammessages_remoteclient_discovery_pb2.CMsgRemoteClientBroadcastStatus
    def __init__(self, client_id: _Optional[int] = ..., instance_id: _Optional[int] = ..., status: _Optional[_Union[_steammessages_remoteclient_discovery_pb2.CMsgRemoteClientBroadcastStatus, _Mapping]] = ...) -> None: ...

class CMsgRemoteClientAppStatus(_message.Message):
    __slots__ = ("status_updates",)
    class AppUpdateInfo(_message.Message):
        __slots__ = ("time_update_start", "bytes_to_download", "bytes_downloaded", "bytes_to_process", "bytes_processed", "estimated_seconds_remaining", "update_result", "update_state")
        TIME_UPDATE_START_FIELD_NUMBER: _ClassVar[int]
        BYTES_TO_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
        BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        BYTES_TO_PROCESS_FIELD_NUMBER: _ClassVar[int]
        BYTES_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        UPDATE_RESULT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_STATE_FIELD_NUMBER: _ClassVar[int]
        time_update_start: int
        bytes_to_download: int
        bytes_downloaded: int
        bytes_to_process: int
        bytes_processed: int
        estimated_seconds_remaining: int
        update_result: int
        update_state: int
        def __init__(self, time_update_start: _Optional[int] = ..., bytes_to_download: _Optional[int] = ..., bytes_downloaded: _Optional[int] = ..., bytes_to_process: _Optional[int] = ..., bytes_processed: _Optional[int] = ..., estimated_seconds_remaining: _Optional[int] = ..., update_result: _Optional[int] = ..., update_state: _Optional[int] = ...) -> None: ...
    class ShortcutInfo(_message.Message):
        __slots__ = ("name", "icon", "categories", "exepath")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        CATEGORIES_FIELD_NUMBER: _ClassVar[int]
        EXEPATH_FIELD_NUMBER: _ClassVar[int]
        name: str
        icon: str
        categories: _containers.RepeatedScalarFieldContainer[str]
        exepath: str
        def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., categories: _Optional[_Iterable[str]] = ..., exepath: _Optional[str] = ...) -> None: ...
    class AppStatus(_message.Message):
        __slots__ = ("app_id", "app_state", "update_info", "shortcut_info", "vr_not_required")
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        APP_STATE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INFO_FIELD_NUMBER: _ClassVar[int]
        SHORTCUT_INFO_FIELD_NUMBER: _ClassVar[int]
        VR_NOT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        app_id: int
        app_state: int
        update_info: CMsgRemoteClientAppStatus.AppUpdateInfo
        shortcut_info: CMsgRemoteClientAppStatus.ShortcutInfo
        vr_not_required: bool
        def __init__(self, app_id: _Optional[int] = ..., app_state: _Optional[int] = ..., update_info: _Optional[_Union[CMsgRemoteClientAppStatus.AppUpdateInfo, _Mapping]] = ..., shortcut_info: _Optional[_Union[CMsgRemoteClientAppStatus.ShortcutInfo, _Mapping]] = ..., vr_not_required: bool = ...) -> None: ...
    STATUS_UPDATES_FIELD_NUMBER: _ClassVar[int]
    status_updates: _containers.RepeatedCompositeFieldContainer[CMsgRemoteClientAppStatus.AppStatus]
    def __init__(self, status_updates: _Optional[_Iterable[_Union[CMsgRemoteClientAppStatus.AppStatus, _Mapping]]] = ...) -> None: ...

class CMsgRemoteClientStartStream(_message.Message):
    __slots__ = ("app_id", "environment", "gamepad_count", "launch_option", "lock_parental_lock", "unlock_parental_lock", "maximum_resolution_x", "maximum_resolution_y", "gamepads", "audio_channel_count", "supported_transport")
    class ReservedGamepad(_message.Message):
        __slots__ = ("controller_type", "controller_subtype")
        CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        controller_type: int
        controller_subtype: int
        def __init__(self, controller_type: _Optional[int] = ..., controller_subtype: _Optional[int] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    GAMEPAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_OPTION_FIELD_NUMBER: _ClassVar[int]
    LOCK_PARENTAL_LOCK_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_PARENTAL_LOCK_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_RESOLUTION_X_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_RESOLUTION_Y_FIELD_NUMBER: _ClassVar[int]
    GAMEPADS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    environment: int
    gamepad_count: int
    launch_option: int
    lock_parental_lock: bool
    unlock_parental_lock: str
    maximum_resolution_x: int
    maximum_resolution_y: int
    gamepads: _containers.RepeatedCompositeFieldContainer[CMsgRemoteClientStartStream.ReservedGamepad]
    audio_channel_count: int
    supported_transport: _containers.RepeatedScalarFieldContainer[_steammessages_remoteclient_discovery_pb2.EStreamTransport]
    def __init__(self, app_id: _Optional[int] = ..., environment: _Optional[int] = ..., gamepad_count: _Optional[int] = ..., launch_option: _Optional[int] = ..., lock_parental_lock: bool = ..., unlock_parental_lock: _Optional[str] = ..., maximum_resolution_x: _Optional[int] = ..., maximum_resolution_y: _Optional[int] = ..., gamepads: _Optional[_Iterable[_Union[CMsgRemoteClientStartStream.ReservedGamepad, _Mapping]]] = ..., audio_channel_count: _Optional[int] = ..., supported_transport: _Optional[_Iterable[_Union[_steammessages_remoteclient_discovery_pb2.EStreamTransport, str]]] = ...) -> None: ...

class CMsgRemoteClientStartStreamResponse(_message.Message):
    __slots__ = ("e_launch_result", "stream_port", "launch_options", "auth_token", "transport", "relay_server", "launch_task", "launch_task_detail", "launch_tasks_done", "launch_tasks_total", "vr_connection_params")
    E_LAUNCH_RESULT_FIELD_NUMBER: _ClassVar[int]
    STREAM_PORT_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RELAY_SERVER_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TASK_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TASK_DETAIL_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TASKS_DONE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_TASKS_TOTAL_FIELD_NUMBER: _ClassVar[int]
    VR_CONNECTION_PARAMS_FIELD_NUMBER: _ClassVar[int]
    e_launch_result: int
    stream_port: int
    launch_options: _containers.RepeatedScalarFieldContainer[int]
    auth_token: bytes
    transport: _steammessages_remoteclient_discovery_pb2.EStreamTransport
    relay_server: str
    launch_task: str
    launch_task_detail: str
    launch_tasks_done: int
    launch_tasks_total: int
    vr_connection_params: str
    def __init__(self, e_launch_result: _Optional[int] = ..., stream_port: _Optional[int] = ..., launch_options: _Optional[_Iterable[int]] = ..., auth_token: _Optional[bytes] = ..., transport: _Optional[_Union[_steammessages_remoteclient_discovery_pb2.EStreamTransport, str]] = ..., relay_server: _Optional[str] = ..., launch_task: _Optional[str] = ..., launch_task_detail: _Optional[str] = ..., launch_tasks_done: _Optional[int] = ..., launch_tasks_total: _Optional[int] = ..., vr_connection_params: _Optional[str] = ...) -> None: ...

class CMsgRemoteClientPing(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgRemoteClientPingResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgRemoteClientAcceptEULA(_message.Message):
    __slots__ = ("app_id", "eula_id", "eula_version")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    EULA_ID_FIELD_NUMBER: _ClassVar[int]
    EULA_VERSION_FIELD_NUMBER: _ClassVar[int]
    app_id: _containers.RepeatedScalarFieldContainer[int]
    eula_id: _containers.RepeatedScalarFieldContainer[str]
    eula_version: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, app_id: _Optional[_Iterable[int]] = ..., eula_id: _Optional[_Iterable[str]] = ..., eula_version: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgRemoteClientGetControllerConfig(_message.Message):
    __slots__ = ("app_id", "controller_index")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    controller_index: int
    def __init__(self, app_id: _Optional[int] = ..., controller_index: _Optional[int] = ...) -> None: ...

class CMsgRemoteClientGetControllerConfigResponse(_message.Message):
    __slots__ = ("eresult", "config_vdf")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VDF_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    config_vdf: bytes
    def __init__(self, eresult: _Optional[int] = ..., config_vdf: _Optional[bytes] = ...) -> None: ...

class CMsgRemoteClientStreamingEnabled(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...
