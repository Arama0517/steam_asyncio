import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientUDSP2PSessionStarted(_message.Message):
    __slots__ = ("steamid_remote", "appid")
    STEAMID_REMOTE_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    steamid_remote: int
    appid: int
    def __init__(self, steamid_remote: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CMsgClientUDSP2PSessionEnded(_message.Message):
    __slots__ = ("steamid_remote", "appid", "session_length_sec", "session_error", "nattype", "bytes_recv", "bytes_sent", "bytes_sent_relay", "bytes_recv_relay", "time_to_connect_ms")
    STEAMID_REMOTE_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    SESSION_LENGTH_SEC_FIELD_NUMBER: _ClassVar[int]
    SESSION_ERROR_FIELD_NUMBER: _ClassVar[int]
    NATTYPE_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECV_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
    BYTES_SENT_RELAY_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECV_RELAY_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_CONNECT_MS_FIELD_NUMBER: _ClassVar[int]
    steamid_remote: int
    appid: int
    session_length_sec: int
    session_error: int
    nattype: int
    bytes_recv: int
    bytes_sent: int
    bytes_sent_relay: int
    bytes_recv_relay: int
    time_to_connect_ms: int
    def __init__(self, steamid_remote: _Optional[int] = ..., appid: _Optional[int] = ..., session_length_sec: _Optional[int] = ..., session_error: _Optional[int] = ..., nattype: _Optional[int] = ..., bytes_recv: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., bytes_sent_relay: _Optional[int] = ..., bytes_recv_relay: _Optional[int] = ..., time_to_connect_ms: _Optional[int] = ...) -> None: ...

class CMsgClientGetClientDetails(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientGetClientDetailsResponse(_message.Message):
    __slots__ = ("package_version", "os", "machine_name", "ip_public", "ip_private", "games_running", "bytes_available", "protocol_version", "clientcomm_version", "local_users")
    class Game(_message.Message):
        __slots__ = ("appid", "extra_info", "time_running_sec")
        APPID_FIELD_NUMBER: _ClassVar[int]
        EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
        TIME_RUNNING_SEC_FIELD_NUMBER: _ClassVar[int]
        appid: int
        extra_info: str
        time_running_sec: int
        def __init__(self, appid: _Optional[int] = ..., extra_info: _Optional[str] = ..., time_running_sec: _Optional[int] = ...) -> None: ...
    PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    IP_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    GAMES_RUNNING_FIELD_NUMBER: _ClassVar[int]
    BYTES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENTCOMM_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_USERS_FIELD_NUMBER: _ClassVar[int]
    package_version: int
    os: str
    machine_name: str
    ip_public: str
    ip_private: str
    games_running: _containers.RepeatedCompositeFieldContainer[CMsgClientGetClientDetailsResponse.Game]
    bytes_available: int
    protocol_version: int
    clientcomm_version: int
    local_users: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, package_version: _Optional[int] = ..., os: _Optional[str] = ..., machine_name: _Optional[str] = ..., ip_public: _Optional[str] = ..., ip_private: _Optional[str] = ..., games_running: _Optional[_Iterable[_Union[CMsgClientGetClientDetailsResponse.Game, _Mapping]]] = ..., bytes_available: _Optional[int] = ..., protocol_version: _Optional[int] = ..., clientcomm_version: _Optional[int] = ..., local_users: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientGetClientAppList(_message.Message):
    __slots__ = ("media", "tools", "games", "only_installed", "only_changing", "comics", "include_client_info", "filter_appids")
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    GAMES_FIELD_NUMBER: _ClassVar[int]
    ONLY_INSTALLED_FIELD_NUMBER: _ClassVar[int]
    ONLY_CHANGING_FIELD_NUMBER: _ClassVar[int]
    COMICS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    FILTER_APPIDS_FIELD_NUMBER: _ClassVar[int]
    media: bool
    tools: bool
    games: bool
    only_installed: bool
    only_changing: bool
    comics: bool
    include_client_info: bool
    filter_appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, media: bool = ..., tools: bool = ..., games: bool = ..., only_installed: bool = ..., only_changing: bool = ..., comics: bool = ..., include_client_info: bool = ..., filter_appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientGetClientAppListResponse(_message.Message):
    __slots__ = ("apps", "bytes_available", "client_info")
    class App(_message.Message):
        __slots__ = ("appid", "category", "app_type", "favorite", "installed", "auto_update", "bytes_downloaded", "bytes_to_download", "bytes_download_rate", "dlcs", "download_paused", "num_downloading", "num_paused", "changing", "available_on_platform", "bytes_staged", "bytes_to_stage", "bytes_required", "source_buildid", "target_buildid", "estimated_seconds_remaining", "queue_position", "uninstalling", "rt_time_scheduled", "running")
        class DLC(_message.Message):
            __slots__ = ("appid", "installed")
            APPID_FIELD_NUMBER: _ClassVar[int]
            INSTALLED_FIELD_NUMBER: _ClassVar[int]
            appid: int
            installed: bool
            def __init__(self, appid: _Optional[int] = ..., installed: bool = ...) -> None: ...
        APPID_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_FIELD_NUMBER: _ClassVar[int]
        APP_TYPE_FIELD_NUMBER: _ClassVar[int]
        FAVORITE_FIELD_NUMBER: _ClassVar[int]
        INSTALLED_FIELD_NUMBER: _ClassVar[int]
        AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
        BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
        BYTES_TO_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
        BYTES_DOWNLOAD_RATE_FIELD_NUMBER: _ClassVar[int]
        DLCS_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_PAUSED_FIELD_NUMBER: _ClassVar[int]
        NUM_DOWNLOADING_FIELD_NUMBER: _ClassVar[int]
        NUM_PAUSED_FIELD_NUMBER: _ClassVar[int]
        CHANGING_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_ON_PLATFORM_FIELD_NUMBER: _ClassVar[int]
        BYTES_STAGED_FIELD_NUMBER: _ClassVar[int]
        BYTES_TO_STAGE_FIELD_NUMBER: _ClassVar[int]
        BYTES_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        SOURCE_BUILDID_FIELD_NUMBER: _ClassVar[int]
        TARGET_BUILDID_FIELD_NUMBER: _ClassVar[int]
        ESTIMATED_SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
        UNINSTALLING_FIELD_NUMBER: _ClassVar[int]
        RT_TIME_SCHEDULED_FIELD_NUMBER: _ClassVar[int]
        RUNNING_FIELD_NUMBER: _ClassVar[int]
        appid: int
        category: str
        app_type: str
        favorite: bool
        installed: bool
        auto_update: bool
        bytes_downloaded: int
        bytes_to_download: int
        bytes_download_rate: int
        dlcs: _containers.RepeatedCompositeFieldContainer[CMsgClientGetClientAppListResponse.App.DLC]
        download_paused: bool
        num_downloading: int
        num_paused: int
        changing: bool
        available_on_platform: bool
        bytes_staged: int
        bytes_to_stage: int
        bytes_required: int
        source_buildid: int
        target_buildid: int
        estimated_seconds_remaining: int
        queue_position: int
        uninstalling: bool
        rt_time_scheduled: int
        running: bool
        def __init__(self, appid: _Optional[int] = ..., category: _Optional[str] = ..., app_type: _Optional[str] = ..., favorite: bool = ..., installed: bool = ..., auto_update: bool = ..., bytes_downloaded: _Optional[int] = ..., bytes_to_download: _Optional[int] = ..., bytes_download_rate: _Optional[int] = ..., dlcs: _Optional[_Iterable[_Union[CMsgClientGetClientAppListResponse.App.DLC, _Mapping]]] = ..., download_paused: bool = ..., num_downloading: _Optional[int] = ..., num_paused: _Optional[int] = ..., changing: bool = ..., available_on_platform: bool = ..., bytes_staged: _Optional[int] = ..., bytes_to_stage: _Optional[int] = ..., bytes_required: _Optional[int] = ..., source_buildid: _Optional[int] = ..., target_buildid: _Optional[int] = ..., estimated_seconds_remaining: _Optional[int] = ..., queue_position: _Optional[int] = ..., uninstalling: bool = ..., rt_time_scheduled: _Optional[int] = ..., running: bool = ...) -> None: ...
    APPS_FIELD_NUMBER: _ClassVar[int]
    BYTES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[CMsgClientGetClientAppListResponse.App]
    bytes_available: int
    client_info: CMsgClientGetClientDetailsResponse
    def __init__(self, apps: _Optional[_Iterable[_Union[CMsgClientGetClientAppListResponse.App, _Mapping]]] = ..., bytes_available: _Optional[int] = ..., client_info: _Optional[_Union[CMsgClientGetClientDetailsResponse, _Mapping]] = ...) -> None: ...

class CMsgClientInstallClientApp(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgClientInstallClientAppResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class CMsgClientUninstallClientApp(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgClientUninstallClientAppResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class CMsgClientSetClientAppUpdateState(_message.Message):
    __slots__ = ("appid", "update")
    APPID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    update: bool
    def __init__(self, appid: _Optional[int] = ..., update: bool = ...) -> None: ...

class CMsgClientSetClientAppUpdateStateResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class CMsgClientLaunchClientApp(_message.Message):
    __slots__ = ("appid", "language", "launch_option_type", "launch_option", "launch_source", "args", "query_params")
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_OPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_OPTION_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    language: int
    launch_option_type: int
    launch_option: int
    launch_source: int
    args: str
    query_params: str
    def __init__(self, appid: _Optional[int] = ..., language: _Optional[int] = ..., launch_option_type: _Optional[int] = ..., launch_option: _Optional[int] = ..., launch_source: _Optional[int] = ..., args: _Optional[str] = ..., query_params: _Optional[str] = ...) -> None: ...

class CMsgClientLaunchClientAppResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class CMsgClientEnableOrDisableDownloads(_message.Message):
    __slots__ = ("enable",)
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    def __init__(self, enable: bool = ...) -> None: ...

class CMsgClientEnableOrDisableDownloadsResponse(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...
