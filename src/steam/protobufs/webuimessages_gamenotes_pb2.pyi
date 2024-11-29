import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CGameNotes_UploadImage_Request(_message.Message):
    __slots__ = ("file_prefix", "mime_type", "data")
    FILE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    file_prefix: str
    mime_type: str
    data: bytes
    def __init__(self, file_prefix: _Optional[str] = ..., mime_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class CGameNotes_UploadImage_Response(_message.Message):
    __slots__ = ("filename",)
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    filename: str
    def __init__(self, filename: _Optional[str] = ...) -> None: ...

class GameNotes(_service.service): ...

class GameNotes_Stub(GameNotes): ...
