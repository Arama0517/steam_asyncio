import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CTransportValidation_AppendToString_Request(_message.Message):
    __slots__ = ("append_strings",)
    APPEND_STRINGS_FIELD_NUMBER: _ClassVar[int]
    append_strings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, append_strings: _Optional[_Iterable[str]] = ...) -> None: ...

class CTransportValidation_AppendToString_Response(_message.Message):
    __slots__ = ("combined_text",)
    COMBINED_TEXT_FIELD_NUMBER: _ClassVar[int]
    combined_text: str
    def __init__(self, combined_text: _Optional[str] = ...) -> None: ...

class CTransportValidation_NotifyText_Notification(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class CTransportValidation_NotifyNumber_Notification(_message.Message):
    __slots__ = ("number",)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class CTransportValidation_GetLastNotifyNumber_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_GetLastNotifyNumber_Response(_message.Message):
    __slots__ = ("last_notify_number",)
    LAST_NOTIFY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    last_notify_number: int
    def __init__(self, last_notify_number: _Optional[int] = ...) -> None: ...

class CTransportValidation_TriggerSyntheticEvents_Request(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class CTransportValidation_TriggerSyntheticEvents_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_NotifySyntheticEvent_Notification(_message.Message):
    __slots__ = ("sequence",)
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    def __init__(self, sequence: _Optional[int] = ...) -> None: ...

class CTransportValidation_TriggerDataRequest_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_TriggerDataRequest_Response(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class CTransportValidation_DataRequest_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_DataRequest_Response(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: int
    def __init__(self, data: _Optional[int] = ...) -> None: ...

class CTransportValidation_AddNumbers_Request(_message.Message):
    __slots__ = ("numbers",)
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, numbers: _Optional[_Iterable[int]] = ...) -> None: ...

class CTransportValidation_AddNumbers_Response(_message.Message):
    __slots__ = ("accumulated",)
    ACCUMULATED_FIELD_NUMBER: _ClassVar[int]
    accumulated: int
    def __init__(self, accumulated: _Optional[int] = ...) -> None: ...

class CTransportValidation_CountOrderedBytes_Request(_message.Message):
    __slots__ = ("ordered_bytes",)
    ORDERED_BYTES_FIELD_NUMBER: _ClassVar[int]
    ordered_bytes: bytes
    def __init__(self, ordered_bytes: _Optional[bytes] = ...) -> None: ...

class CTransportValidation_CountOrderedBytes_Response(_message.Message):
    __slots__ = ("byte_count",)
    BYTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    byte_count: int
    def __init__(self, byte_count: _Optional[int] = ...) -> None: ...

class CTransportValidation_ThreadedCount_Request(_message.Message):
    __slots__ = ("start_num", "end_num")
    START_NUM_FIELD_NUMBER: _ClassVar[int]
    END_NUM_FIELD_NUMBER: _ClassVar[int]
    start_num: int
    end_num: int
    def __init__(self, start_num: _Optional[int] = ..., end_num: _Optional[int] = ...) -> None: ...

class CTransportValidation_ThreadedCount_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_NotifyCount_Notification(_message.Message):
    __slots__ = ("num",)
    NUM_FIELD_NUMBER: _ClassVar[int]
    num: int
    def __init__(self, num: _Optional[int] = ...) -> None: ...

class CTransportValidation_RequestInvalidBool_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_RequestInvalidBool_Response(_message.Message):
    __slots__ = ("before", "output", "after")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    before: int
    output: bool
    after: int
    def __init__(self, before: _Optional[int] = ..., output: bool = ..., after: _Optional[int] = ...) -> None: ...

class CTransportValidation_GetLargeResponse_Request(_message.Message):
    __slots__ = ("data_size",)
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    data_size: int
    def __init__(self, data_size: _Optional[int] = ...) -> None: ...

class CTransportValidation_GetLargeResponse_Response(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CTransportValidation_RequestLargeNotification_Request(_message.Message):
    __slots__ = ("data_size",)
    DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
    data_size: int
    def __init__(self, data_size: _Optional[int] = ...) -> None: ...

class CTransportValidation_RequestLargeNotification_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTransportValidation_NotifyLarge_Notification(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CTransportValidationClient_AddNumbers_Request(_message.Message):
    __slots__ = ("numbers",)
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    numbers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, numbers: _Optional[_Iterable[int]] = ...) -> None: ...

class CTransportValidationClient_AddNumbers_Response(_message.Message):
    __slots__ = ("accumulated",)
    ACCUMULATED_FIELD_NUMBER: _ClassVar[int]
    accumulated: int
    def __init__(self, accumulated: _Optional[int] = ...) -> None: ...

class TransportValidation(_service.service): ...

class TransportValidation_Stub(TransportValidation): ...

class TransportValidationClient(_service.service): ...

class TransportValidationClient_Stub(TransportValidationClient): ...
