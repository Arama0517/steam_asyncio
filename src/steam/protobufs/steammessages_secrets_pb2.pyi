import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EKeyEscrowUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EKeyEscrowUsageStreamingDevice: _ClassVar[EKeyEscrowUsage]
k_EKeyEscrowUsageStreamingDevice: EKeyEscrowUsage

class CKeyEscrow_Request(_message.Message):
    __slots__ = ("rsa_oaep_sha_ticket", "password", "usage", "device_name")
    RSA_OAEP_SHA_TICKET_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    rsa_oaep_sha_ticket: bytes
    password: bytes
    usage: EKeyEscrowUsage
    device_name: str
    def __init__(self, rsa_oaep_sha_ticket: _Optional[bytes] = ..., password: _Optional[bytes] = ..., usage: _Optional[_Union[EKeyEscrowUsage, str]] = ..., device_name: _Optional[str] = ...) -> None: ...

class CKeyEscrow_Ticket(_message.Message):
    __slots__ = ("password", "identifier", "payload", "timestamp", "usage", "device_name", "device_model", "device_serial", "device_provisioning_id")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SERIAL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PROVISIONING_ID_FIELD_NUMBER: _ClassVar[int]
    password: bytes
    identifier: int
    payload: bytes
    timestamp: int
    usage: EKeyEscrowUsage
    device_name: str
    device_model: str
    device_serial: str
    device_provisioning_id: int
    def __init__(self, password: _Optional[bytes] = ..., identifier: _Optional[int] = ..., payload: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., usage: _Optional[_Union[EKeyEscrowUsage, str]] = ..., device_name: _Optional[str] = ..., device_model: _Optional[str] = ..., device_serial: _Optional[str] = ..., device_provisioning_id: _Optional[int] = ...) -> None: ...

class CKeyEscrow_Response(_message.Message):
    __slots__ = ("ticket",)
    TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket: CKeyEscrow_Ticket
    def __init__(self, ticket: _Optional[_Union[CKeyEscrow_Ticket, _Mapping]] = ...) -> None: ...

class Secrets(_service.service): ...

class Secrets_Stub(Secrets): ...
