import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CGameNetworking_AllocateFakeIP_Request(_message.Message):
    __slots__ = ("app_id", "num_fake_ports")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_FAKE_PORTS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    num_fake_ports: int
    def __init__(self, app_id: _Optional[int] = ..., num_fake_ports: _Optional[int] = ...) -> None: ...

class CGameNetworking_AllocateFakeIP_Response(_message.Message):
    __slots__ = ("fake_ip", "fake_ports")
    FAKE_IP_FIELD_NUMBER: _ClassVar[int]
    FAKE_PORTS_FIELD_NUMBER: _ClassVar[int]
    fake_ip: int
    fake_ports: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, fake_ip: _Optional[int] = ..., fake_ports: _Optional[_Iterable[int]] = ...) -> None: ...

class CGameNetworking_ReleaseFakeIP_Notification(_message.Message):
    __slots__ = ("app_id", "fake_ip", "fake_ports")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FAKE_IP_FIELD_NUMBER: _ClassVar[int]
    FAKE_PORTS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    fake_ip: int
    fake_ports: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, app_id: _Optional[int] = ..., fake_ip: _Optional[int] = ..., fake_ports: _Optional[_Iterable[int]] = ...) -> None: ...

class GameNetworking(_service.service): ...

class GameNetworking_Stub(GameNetworking): ...
