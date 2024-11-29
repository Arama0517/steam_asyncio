import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CSystemManager_Hibernate_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSystemManager_Hibernate_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSystemManager_WriteFile_Request(_message.Message):
    __slots__ = ("path", "data")
    PATH_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    path: str
    data: bytes
    def __init__(self, path: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class CSystemManager_WriteFile_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SystemManager(_service.service): ...

class SystemManager_Stub(SystemManager): ...
