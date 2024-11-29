from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Offline_Ticket(_message.Message):
    __slots__ = ("encrypted_ticket", "signature", "kdf1", "salt1", "kdf2", "salt2")
    ENCRYPTED_TICKET_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    KDF1_FIELD_NUMBER: _ClassVar[int]
    SALT1_FIELD_NUMBER: _ClassVar[int]
    KDF2_FIELD_NUMBER: _ClassVar[int]
    SALT2_FIELD_NUMBER: _ClassVar[int]
    encrypted_ticket: bytes
    signature: bytes
    kdf1: int
    salt1: bytes
    kdf2: int
    salt2: bytes
    def __init__(self, encrypted_ticket: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., kdf1: _Optional[int] = ..., salt1: _Optional[bytes] = ..., kdf2: _Optional[int] = ..., salt2: _Optional[bytes] = ...) -> None: ...
