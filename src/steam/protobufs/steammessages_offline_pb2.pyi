import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import offline_ticket_pb2 as _offline_ticket_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class COffline_GetOfflineLogonTicket_Request(_message.Message):
    __slots__ = ("priority", "perform_encryption")
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PERFORM_ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    priority: int
    perform_encryption: bool
    def __init__(self, priority: _Optional[int] = ..., perform_encryption: bool = ...) -> None: ...

class COffline_GetOfflineLogonTicket_Response(_message.Message):
    __slots__ = ("serialized_ticket", "signature", "encrypted_ticket")
    SERIALIZED_TICKET_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_TICKET_FIELD_NUMBER: _ClassVar[int]
    serialized_ticket: bytes
    signature: bytes
    encrypted_ticket: _offline_ticket_pb2.Offline_Ticket
    def __init__(self, serialized_ticket: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., encrypted_ticket: _Optional[_Union[_offline_ticket_pb2.Offline_Ticket, _Mapping]] = ...) -> None: ...

class COffline_GetUnsignedOfflineLogonTicket_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class COffline_OfflineLogonTicket(_message.Message):
    __slots__ = ("accountid", "rtime32_creation_time")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    RTIME32_CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    rtime32_creation_time: int
    def __init__(self, accountid: _Optional[int] = ..., rtime32_creation_time: _Optional[int] = ...) -> None: ...

class COffline_GetUnsignedOfflineLogonTicket_Response(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: COffline_OfflineLogonTicket
    def __init__(self, ticket: _Optional[_Union[COffline_OfflineLogonTicket, _Mapping]] = ...) -> None: ...

class Offline(_service.service): ...

class Offline_Stub(Offline): ...
