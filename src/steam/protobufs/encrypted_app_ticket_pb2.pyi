from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EncryptedAppTicket(_message.Message):
    __slots__ = ("ticket_version_no", "crc_encryptedticket", "cb_encrypteduserdata", "cb_encrypted_appownershipticket", "encrypted_ticket")
    TICKET_VERSION_NO_FIELD_NUMBER: _ClassVar[int]
    CRC_ENCRYPTEDTICKET_FIELD_NUMBER: _ClassVar[int]
    CB_ENCRYPTEDUSERDATA_FIELD_NUMBER: _ClassVar[int]
    CB_ENCRYPTED_APPOWNERSHIPTICKET_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_TICKET_FIELD_NUMBER: _ClassVar[int]
    ticket_version_no: int
    crc_encryptedticket: int
    cb_encrypteduserdata: int
    cb_encrypted_appownershipticket: int
    encrypted_ticket: bytes
    def __init__(self, ticket_version_no: _Optional[int] = ..., crc_encryptedticket: _Optional[int] = ..., cb_encrypteduserdata: _Optional[int] = ..., cb_encrypted_appownershipticket: _Optional[int] = ..., encrypted_ticket: _Optional[bytes] = ...) -> None: ...
