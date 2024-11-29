import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CTransportAuth_Authenticate_Request(_message.Message):
    __slots__ = ("auth_key",)
    AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
    auth_key: str
    def __init__(self, auth_key: _Optional[str] = ...) -> None: ...

class CTransportAuth_Authenticate_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportAuth_StartShutdown_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TransportAuth(_service.service): ...

class TransportAuth_Stub(TransportAuth): ...
