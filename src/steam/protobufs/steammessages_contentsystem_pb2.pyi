import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EAppContentDetectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAppContentDetectionType_None: _ClassVar[EAppContentDetectionType]
    k_EAppContentDetectionType_AntiCheat: _ClassVar[EAppContentDetectionType]
    k_EAppContentDetectionType_GameEngine: _ClassVar[EAppContentDetectionType]
k_EAppContentDetectionType_None: EAppContentDetectionType
k_EAppContentDetectionType_AntiCheat: EAppContentDetectionType
k_EAppContentDetectionType_GameEngine: EAppContentDetectionType

class CContentServerDirectory_ConnectedSteamPipeServerInfo(_message.Message):
    __slots__ = ("type", "source_id", "hostname")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    type: str
    source_id: int
    hostname: str
    def __init__(self, type: _Optional[str] = ..., source_id: _Optional[int] = ..., hostname: _Optional[str] = ...) -> None: ...

class CContentServerDirectory_GetServersForSteamPipe_Request(_message.Message):
    __slots__ = ("cell_id", "max_servers", "ip_override", "launcher_type", "ipv6_public", "current_connections")
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_SERVERS_FIELD_NUMBER: _ClassVar[int]
    IP_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IPV6_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    cell_id: int
    max_servers: int
    ip_override: str
    launcher_type: int
    ipv6_public: str
    current_connections: _containers.RepeatedCompositeFieldContainer[CContentServerDirectory_ConnectedSteamPipeServerInfo]
    def __init__(self, cell_id: _Optional[int] = ..., max_servers: _Optional[int] = ..., ip_override: _Optional[str] = ..., launcher_type: _Optional[int] = ..., ipv6_public: _Optional[str] = ..., current_connections: _Optional[_Iterable[_Union[CContentServerDirectory_ConnectedSteamPipeServerInfo, _Mapping]]] = ...) -> None: ...

class CContentServerDirectory_ServerInfo(_message.Message):
    __slots__ = ("type", "source_id", "cell_id", "load", "weighted_load", "num_entries_in_client_list", "steam_china_only", "host", "vhost", "use_as_proxy", "proxy_request_path_template", "https_support", "allowed_app_ids", "priority_class", "bypass_proxies_of_type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    LOAD_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_LOAD_FIELD_NUMBER: _ClassVar[int]
    NUM_ENTRIES_IN_CLIENT_LIST_FIELD_NUMBER: _ClassVar[int]
    STEAM_CHINA_ONLY_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    VHOST_FIELD_NUMBER: _ClassVar[int]
    USE_AS_PROXY_FIELD_NUMBER: _ClassVar[int]
    PROXY_REQUEST_PATH_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    HTTPS_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_APP_IDS_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_CLASS_FIELD_NUMBER: _ClassVar[int]
    BYPASS_PROXIES_OF_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    source_id: int
    cell_id: int
    load: int
    weighted_load: float
    num_entries_in_client_list: int
    steam_china_only: bool
    host: str
    vhost: str
    use_as_proxy: bool
    proxy_request_path_template: str
    https_support: str
    allowed_app_ids: _containers.RepeatedScalarFieldContainer[int]
    priority_class: int
    bypass_proxies_of_type: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, type: _Optional[str] = ..., source_id: _Optional[int] = ..., cell_id: _Optional[int] = ..., load: _Optional[int] = ..., weighted_load: _Optional[float] = ..., num_entries_in_client_list: _Optional[int] = ..., steam_china_only: bool = ..., host: _Optional[str] = ..., vhost: _Optional[str] = ..., use_as_proxy: bool = ..., proxy_request_path_template: _Optional[str] = ..., https_support: _Optional[str] = ..., allowed_app_ids: _Optional[_Iterable[int]] = ..., priority_class: _Optional[int] = ..., bypass_proxies_of_type: _Optional[_Iterable[str]] = ...) -> None: ...

class CContentServerDirectory_GetServersForSteamPipe_Response(_message.Message):
    __slots__ = ("servers", "no_change")
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    NO_CHANGE_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[CContentServerDirectory_ServerInfo]
    no_change: bool
    def __init__(self, servers: _Optional[_Iterable[_Union[CContentServerDirectory_ServerInfo, _Mapping]]] = ..., no_change: bool = ...) -> None: ...

class CContentServerDirectory_GetDepotPatchInfo_Request(_message.Message):
    __slots__ = ("appid", "depotid", "source_manifestid", "target_manifestid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOTID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    TARGET_MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depotid: int
    source_manifestid: int
    target_manifestid: int
    def __init__(self, appid: _Optional[int] = ..., depotid: _Optional[int] = ..., source_manifestid: _Optional[int] = ..., target_manifestid: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_GetDepotPatchInfo_Response(_message.Message):
    __slots__ = ("is_available", "patch_size", "patched_chunks_size")
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    PATCHED_CHUNKS_SIZE_FIELD_NUMBER: _ClassVar[int]
    is_available: bool
    patch_size: int
    patched_chunks_size: int
    def __init__(self, is_available: bool = ..., patch_size: _Optional[int] = ..., patched_chunks_size: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_GetClientUpdateHosts_Request(_message.Message):
    __slots__ = ("cached_signature",)
    CACHED_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    cached_signature: str
    def __init__(self, cached_signature: _Optional[str] = ...) -> None: ...

class CContentServerDirectory_GetClientUpdateHosts_Response(_message.Message):
    __slots__ = ("hosts_kv", "valid_until_time", "ip_country")
    HOSTS_KV_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_TIME_FIELD_NUMBER: _ClassVar[int]
    IP_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    hosts_kv: str
    valid_until_time: int
    ip_country: str
    def __init__(self, hosts_kv: _Optional[str] = ..., valid_until_time: _Optional[int] = ..., ip_country: _Optional[str] = ...) -> None: ...

class CContentServerDirectory_GetManifestRequestCode_Request(_message.Message):
    __slots__ = ("app_id", "depot_id", "manifest_id", "app_branch", "branch_password_hash")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    APP_BRANCH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    depot_id: int
    manifest_id: int
    app_branch: str
    branch_password_hash: str
    def __init__(self, app_id: _Optional[int] = ..., depot_id: _Optional[int] = ..., manifest_id: _Optional[int] = ..., app_branch: _Optional[str] = ..., branch_password_hash: _Optional[str] = ...) -> None: ...

class CContentServerDirectory_GetManifestRequestCode_Response(_message.Message):
    __slots__ = ("manifest_request_code",)
    MANIFEST_REQUEST_CODE_FIELD_NUMBER: _ClassVar[int]
    manifest_request_code: int
    def __init__(self, manifest_request_code: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_GetCDNAuthToken_Request(_message.Message):
    __slots__ = ("depot_id", "host_name", "app_id")
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    depot_id: int
    host_name: str
    app_id: int
    def __init__(self, depot_id: _Optional[int] = ..., host_name: _Optional[str] = ..., app_id: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_GetCDNAuthToken_Response(_message.Message):
    __slots__ = ("token", "expiration_time")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    token: str
    expiration_time: int
    def __init__(self, token: _Optional[str] = ..., expiration_time: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_RequestPeerContentServer_Request(_message.Message):
    __slots__ = ("remote_client_id", "steamid", "server_remote_client_id", "app_id", "current_build_id")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SERVER_REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    steamid: int
    server_remote_client_id: int
    app_id: int
    current_build_id: int
    def __init__(self, remote_client_id: _Optional[int] = ..., steamid: _Optional[int] = ..., server_remote_client_id: _Optional[int] = ..., app_id: _Optional[int] = ..., current_build_id: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_RequestPeerContentServer_Response(_message.Message):
    __slots__ = ("server_port", "installed_depots", "access_token")
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_DEPOTS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    server_port: int
    installed_depots: _containers.RepeatedScalarFieldContainer[int]
    access_token: int
    def __init__(self, server_port: _Optional[int] = ..., installed_depots: _Optional[_Iterable[int]] = ..., access_token: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_GetPeerContentInfo_Request(_message.Message):
    __slots__ = ("remote_client_id", "steamid", "server_remote_client_id")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SERVER_REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    steamid: int
    server_remote_client_id: int
    def __init__(self, remote_client_id: _Optional[int] = ..., steamid: _Optional[int] = ..., server_remote_client_id: _Optional[int] = ...) -> None: ...

class CContentServerDirectory_GetPeerContentInfo_Response(_message.Message):
    __slots__ = ("appids", "ip_public")
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    IP_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    ip_public: str
    def __init__(self, appids: _Optional[_Iterable[int]] = ..., ip_public: _Optional[str] = ...) -> None: ...

class CDepotContentDetection_GetAllDetectedAppContent_Request(_message.Message):
    __slots__ = ("detection_type",)
    DETECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    detection_type: EAppContentDetectionType
    def __init__(self, detection_type: _Optional[_Union[EAppContentDetectionType, str]] = ...) -> None: ...

class DetectedAppContent(_message.Message):
    __slots__ = ("app_id", "depot_id", "detected_content")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    depot_id: int
    detected_content: int
    def __init__(self, app_id: _Optional[int] = ..., depot_id: _Optional[int] = ..., detected_content: _Optional[int] = ...) -> None: ...

class CDepotContentDetection_GetAllDetectedAppContent_Response(_message.Message):
    __slots__ = ("detected_app_content",)
    DETECTED_APP_CONTENT_FIELD_NUMBER: _ClassVar[int]
    detected_app_content: _containers.RepeatedCompositeFieldContainer[DetectedAppContent]
    def __init__(self, detected_app_content: _Optional[_Iterable[_Union[DetectedAppContent, _Mapping]]] = ...) -> None: ...

class ContentServerDirectory(_service.service): ...

class ContentServerDirectory_Stub(ContentServerDirectory): ...

class DepotContentDetection(_service.service): ...

class DepotContentDetection_Stub(DepotContentDetection): ...
