import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgTest_MessageToClient_Request(_message.Message):
    __slots__ = ("some_text",)
    SOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    some_text: str
    def __init__(self, some_text: _Optional[str] = ...) -> None: ...

class CMsgTest_MessageToClient_Response(_message.Message):
    __slots__ = ("some_text",)
    SOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    some_text: str
    def __init__(self, some_text: _Optional[str] = ...) -> None: ...

class CMsgTest_NotifyClient_Notification(_message.Message):
    __slots__ = ("some_text",)
    SOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    some_text: str
    def __init__(self, some_text: _Optional[str] = ...) -> None: ...

class CMsgTest_MessageToServer_Request(_message.Message):
    __slots__ = ("some_text",)
    SOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    some_text: str
    def __init__(self, some_text: _Optional[str] = ...) -> None: ...

class CMsgTest_MessageToServer_Response(_message.Message):
    __slots__ = ("some_text",)
    SOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    some_text: str
    def __init__(self, some_text: _Optional[str] = ...) -> None: ...

class CMsgTest_NotifyServer_Notification(_message.Message):
    __slots__ = ("some_text",)
    SOME_TEXT_FIELD_NUMBER: _ClassVar[int]
    some_text: str
    def __init__(self, some_text: _Optional[str] = ...) -> None: ...

class CMsgTest_NoBody_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgTest_CallClient_Response(_message.Message):
    __slots__ = ("testvalue",)
    TESTVALUE_FIELD_NUMBER: _ClassVar[int]
    testvalue: int
    def __init__(self, testvalue: _Optional[int] = ...) -> None: ...

class TestSteamClient(_service.service): ...

class TestSteamClient_Stub(TestSteamClient): ...

class TestServerFromClient(_service.service): ...

class TestServerFromClient_Stub(TestServerFromClient): ...

class TestExternalPrivilege(_service.service): ...

class TestExternalPrivilege_Stub(TestExternalPrivilege): ...
