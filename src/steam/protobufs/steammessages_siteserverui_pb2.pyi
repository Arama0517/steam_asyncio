import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SiteServerUI_Login_Request(_message.Message):
    __slots__ = ("username", "password", "steamguardcode", "remember_password")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARDCODE_FIELD_NUMBER: _ClassVar[int]
    REMEMBER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    steamguardcode: str
    remember_password: bool
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., steamguardcode: _Optional[str] = ..., remember_password: bool = ...) -> None: ...

class SiteServerUI_Login_Response(_message.Message):
    __slots__ = ("logon_state", "logon_eresult")
    LOGON_STATE_FIELD_NUMBER: _ClassVar[int]
    LOGON_ERESULT_FIELD_NUMBER: _ClassVar[int]
    logon_state: int
    logon_eresult: int
    def __init__(self, logon_state: _Optional[int] = ..., logon_eresult: _Optional[int] = ...) -> None: ...

class SiteServerUI_LoginStatus_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_LoginStatus_Response(_message.Message):
    __slots__ = ("username", "cached_credentials", "logon_state", "logon_eresult")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CACHED_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    LOGON_STATE_FIELD_NUMBER: _ClassVar[int]
    LOGON_ERESULT_FIELD_NUMBER: _ClassVar[int]
    username: str
    cached_credentials: bool
    logon_state: int
    logon_eresult: int
    def __init__(self, username: _Optional[str] = ..., cached_credentials: bool = ..., logon_state: _Optional[int] = ..., logon_eresult: _Optional[int] = ...) -> None: ...

class SiteServerUI_CancelLogin_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_CancelLogin_Response(_message.Message):
    __slots__ = ("logon_state", "logon_eresult")
    LOGON_STATE_FIELD_NUMBER: _ClassVar[int]
    LOGON_ERESULT_FIELD_NUMBER: _ClassVar[int]
    logon_state: int
    logon_eresult: int
    def __init__(self, logon_state: _Optional[int] = ..., logon_eresult: _Optional[int] = ...) -> None: ...

class SiteServerUI_Logout_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_Logout_Response(_message.Message):
    __slots__ = ("logon_state", "logout_eresult")
    LOGON_STATE_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_ERESULT_FIELD_NUMBER: _ClassVar[int]
    logon_state: int
    logout_eresult: int
    def __init__(self, logon_state: _Optional[int] = ..., logout_eresult: _Optional[int] = ...) -> None: ...

class SiteServerUI_Quit_Request(_message.Message):
    __slots__ = ("restart",)
    RESTART_FIELD_NUMBER: _ClassVar[int]
    restart: bool
    def __init__(self, restart: bool = ...) -> None: ...

class SiteServerUI_Quit_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_Status_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_Status_Response(_message.Message):
    __slots__ = ("logon_state", "logon_eresult", "connected", "cache_enabled", "acct_status")
    LOGON_STATE_FIELD_NUMBER: _ClassVar[int]
    LOGON_ERESULT_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    CACHE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACCT_STATUS_FIELD_NUMBER: _ClassVar[int]
    logon_state: int
    logon_eresult: int
    connected: bool
    cache_enabled: bool
    acct_status: int
    def __init__(self, logon_state: _Optional[int] = ..., logon_eresult: _Optional[int] = ..., connected: bool = ..., cache_enabled: bool = ..., acct_status: _Optional[int] = ...) -> None: ...

class SiteServerUI_GetLanguage_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_GetLanguage_Response(_message.Message):
    __slots__ = ("language",)
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: str
    def __init__(self, language: _Optional[str] = ...) -> None: ...

class SiteServerUI_SetLanguage_Request(_message.Message):
    __slots__ = ("language",)
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: str
    def __init__(self, language: _Optional[str] = ...) -> None: ...

class SiteServerUI_SetLanguage_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_ClientStatus_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_ClientStatus_Response(_message.Message):
    __slots__ = ("clients", "payments")
    class ClientInfo(_message.Message):
        __slots__ = ("ip", "hostname", "connected", "instance_id")
        IP_FIELD_NUMBER: _ClassVar[int]
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        CONNECTED_FIELD_NUMBER: _ClassVar[int]
        INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        ip: int
        hostname: str
        connected: bool
        instance_id: int
        def __init__(self, ip: _Optional[int] = ..., hostname: _Optional[str] = ..., connected: bool = ..., instance_id: _Optional[int] = ...) -> None: ...
    class Payment(_message.Message):
        __slots__ = ("transid", "steamid", "amount", "time_created", "purchase_status", "hostname", "persona_name", "profile_url", "avatar_url")
        TRANSID_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_STATUS_FIELD_NUMBER: _ClassVar[int]
        HOSTNAME_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
        AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
        transid: int
        steamid: int
        amount: str
        time_created: int
        purchase_status: int
        hostname: str
        persona_name: str
        profile_url: str
        avatar_url: str
        def __init__(self, transid: _Optional[int] = ..., steamid: _Optional[int] = ..., amount: _Optional[str] = ..., time_created: _Optional[int] = ..., purchase_status: _Optional[int] = ..., hostname: _Optional[str] = ..., persona_name: _Optional[str] = ..., profile_url: _Optional[str] = ..., avatar_url: _Optional[str] = ...) -> None: ...
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[SiteServerUI_ClientStatus_Response.ClientInfo]
    payments: _containers.RepeatedCompositeFieldContainer[SiteServerUI_ClientStatus_Response.Payment]
    def __init__(self, clients: _Optional[_Iterable[_Union[SiteServerUI_ClientStatus_Response.ClientInfo, _Mapping]]] = ..., payments: _Optional[_Iterable[_Union[SiteServerUI_ClientStatus_Response.Payment, _Mapping]]] = ...) -> None: ...

class SiteServerUI_ContentCacheStatus_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SiteServerUI_ContentCacheStatus_Response(_message.Message):
    __slots__ = ("enabled", "port", "cache_location", "max_size_gb", "p2p_enabled", "explicit_ip_address", "external_process", "current_size_gb", "current_bw", "total_bytes_served")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CACHE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    P2P_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PROCESS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BW_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_SERVED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    port: int
    cache_location: str
    max_size_gb: int
    p2p_enabled: bool
    explicit_ip_address: str
    external_process: bool
    current_size_gb: int
    current_bw: int
    total_bytes_served: int
    def __init__(self, enabled: bool = ..., port: _Optional[int] = ..., cache_location: _Optional[str] = ..., max_size_gb: _Optional[int] = ..., p2p_enabled: bool = ..., explicit_ip_address: _Optional[str] = ..., external_process: bool = ..., current_size_gb: _Optional[int] = ..., current_bw: _Optional[int] = ..., total_bytes_served: _Optional[int] = ...) -> None: ...

class SiteServerUI_ContentCacheConfig_Request(_message.Message):
    __slots__ = ("enabled", "port", "cache_location", "max_size_gb", "p2p_enabled", "external_process", "explicit_ip_address")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CACHE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    MAX_SIZE_GB_FIELD_NUMBER: _ClassVar[int]
    P2P_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PROCESS_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    port: int
    cache_location: str
    max_size_gb: int
    p2p_enabled: bool
    external_process: bool
    explicit_ip_address: str
    def __init__(self, enabled: bool = ..., port: _Optional[int] = ..., cache_location: _Optional[str] = ..., max_size_gb: _Optional[int] = ..., p2p_enabled: bool = ..., external_process: bool = ..., explicit_ip_address: _Optional[str] = ...) -> None: ...

class SiteServerUI_ContentCacheConfig_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
