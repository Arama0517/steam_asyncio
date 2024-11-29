import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CSiteManagerClient_IncomingClient_Request(_message.Message):
    __slots__ = ("site_instanceid", "client_steamid", "client_local_ip", "connection_key")
    SITE_INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_STEAMID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_LOCAL_IP_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_KEY_FIELD_NUMBER: _ClassVar[int]
    site_instanceid: int
    client_steamid: int
    client_local_ip: int
    connection_key: bytes
    def __init__(self, site_instanceid: _Optional[int] = ..., client_steamid: _Optional[int] = ..., client_local_ip: _Optional[int] = ..., connection_key: _Optional[bytes] = ...) -> None: ...

class CSiteManagerClient_IncomingClient_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSiteLicense_ClientSeatCheckout_Notification(_message.Message):
    __slots__ = ("appid", "eresult")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    eresult: int
    def __init__(self, appid: _Optional[int] = ..., eresult: _Optional[int] = ...) -> None: ...

class CSiteManagerClient_TrackedPayments_Notification(_message.Message):
    __slots__ = ("site_id", "payments")
    class Payment(_message.Message):
        __slots__ = ("transid", "steamid", "amount", "ecurrency", "time_created", "purchase_status", "machine_name", "persona_name", "profile_url", "avatar_url")
        TRANSID_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        ECURRENCY_FIELD_NUMBER: _ClassVar[int]
        TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_STATUS_FIELD_NUMBER: _ClassVar[int]
        MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
        AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
        transid: int
        steamid: int
        amount: int
        ecurrency: int
        time_created: int
        purchase_status: int
        machine_name: str
        persona_name: str
        profile_url: str
        avatar_url: str
        def __init__(self, transid: _Optional[int] = ..., steamid: _Optional[int] = ..., amount: _Optional[int] = ..., ecurrency: _Optional[int] = ..., time_created: _Optional[int] = ..., purchase_status: _Optional[int] = ..., machine_name: _Optional[str] = ..., persona_name: _Optional[str] = ..., profile_url: _Optional[str] = ..., avatar_url: _Optional[str] = ...) -> None: ...
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    site_id: int
    payments: _containers.RepeatedCompositeFieldContainer[CSiteManagerClient_TrackedPayments_Notification.Payment]
    def __init__(self, site_id: _Optional[int] = ..., payments: _Optional[_Iterable[_Union[CSiteManagerClient_TrackedPayments_Notification.Payment, _Mapping]]] = ...) -> None: ...

class CSiteLicense_InitiateAssociation_Request(_message.Message):
    __slots__ = ("site_steamid", "site_instanceid", "client_local_ip")
    SITE_STEAMID_FIELD_NUMBER: _ClassVar[int]
    SITE_INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_LOCAL_IP_FIELD_NUMBER: _ClassVar[int]
    site_steamid: int
    site_instanceid: int
    client_local_ip: int
    def __init__(self, site_steamid: _Optional[int] = ..., site_instanceid: _Optional[int] = ..., client_local_ip: _Optional[int] = ...) -> None: ...

class CSiteLicense_InitiateAssociation_Response(_message.Message):
    __slots__ = ("connection_key",)
    CONNECTION_KEY_FIELD_NUMBER: _ClassVar[int]
    connection_key: bytes
    def __init__(self, connection_key: _Optional[bytes] = ...) -> None: ...

class CSiteLicense_LCSAuthenticate_Request(_message.Message):
    __slots__ = ("instanceid",)
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    instanceid: int
    def __init__(self, instanceid: _Optional[int] = ...) -> None: ...

class CSiteLicense_LCSAuthenticate_Response(_message.Message):
    __slots__ = ("site_id", "site_name", "new_session", "no_site_licenses")
    SITE_ID_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_SESSION_FIELD_NUMBER: _ClassVar[int]
    NO_SITE_LICENSES_FIELD_NUMBER: _ClassVar[int]
    site_id: int
    site_name: str
    new_session: bool
    no_site_licenses: bool
    def __init__(self, site_id: _Optional[int] = ..., site_name: _Optional[str] = ..., new_session: bool = ..., no_site_licenses: bool = ...) -> None: ...

class CSiteLicense_LCSAssociateUser_Request(_message.Message):
    __slots__ = ("steamid", "local_ip", "instanceid", "machine_name")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_IP_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    local_ip: int
    instanceid: int
    machine_name: str
    def __init__(self, steamid: _Optional[int] = ..., local_ip: _Optional[int] = ..., instanceid: _Optional[int] = ..., machine_name: _Optional[str] = ...) -> None: ...

class CSiteLicense_LCSAssociateUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSiteLicense_ClientSeatCheckout_Request(_message.Message):
    __slots__ = ("steamid", "instanceid", "appid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    instanceid: int
    appid: int
    def __init__(self, steamid: _Optional[int] = ..., instanceid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CSiteLicense_ClientSeatCheckout_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSiteLicense_ClientGetAvailableSeats_Request(_message.Message):
    __slots__ = ("steamid", "instanceid", "appid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    instanceid: int
    appid: int
    def __init__(self, steamid: _Optional[int] = ..., instanceid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CSiteLicense_ClientGetAvailableSeats_Response(_message.Message):
    __slots__ = ("available_seats",)
    AVAILABLE_SEATS_FIELD_NUMBER: _ClassVar[int]
    available_seats: int
    def __init__(self, available_seats: _Optional[int] = ...) -> None: ...

class SiteManagerClient(_service.service): ...

class SiteManagerClient_Stub(SiteManagerClient): ...

class SiteLicense(_service.service): ...

class SiteLicense_Stub(SiteLicense): ...
