import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientSiteInfo(_message.Message):
    __slots__ = ("site_id", "site_name", "allow_cached_credentials")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_CACHED_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    site_id: int
    site_name: str
    allow_cached_credentials: bool
    def __init__(self, site_id: _Optional[int] = ..., site_name: _Optional[str] = ..., allow_cached_credentials: bool = ...) -> None: ...

class CMsgClientSiteLicenseCheckout(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgClientSiteLicenseCheckoutResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientSiteLicenseGetAvailableSeats(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgClientSiteLicenseGetAvailableSeatsResponse(_message.Message):
    __slots__ = ("eresult", "seats")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    seats: int
    def __init__(self, eresult: _Optional[int] = ..., seats: _Optional[int] = ...) -> None: ...

class CMsgClientSiteLicenseGetContentCacheInfo(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientSiteLicenseGetContentCacheInfoResponse(_message.Message):
    __slots__ = ("use_cache", "ipv4_address", "port_number", "p2p_group", "ip_address")
    USE_CACHE_FIELD_NUMBER: _ClassVar[int]
    IPV4_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    P2P_GROUP_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    use_cache: bool
    ipv4_address: int
    port_number: int
    p2p_group: int
    ip_address: str
    def __init__(self, use_cache: bool = ..., ipv4_address: _Optional[int] = ..., port_number: _Optional[int] = ..., p2p_group: _Optional[int] = ..., ip_address: _Optional[str] = ...) -> None: ...
