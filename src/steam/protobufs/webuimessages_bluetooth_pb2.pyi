import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CBluetoothManager_GetState_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgBluetoothManagerAdapterInfo(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CMsgBluetoothManagerDeviceInfo(_message.Message):
    __slots__ = ("id", "should_hide_hint", "etype", "is_connected", "is_paired", "strength_raw")
    ID_FIELD_NUMBER: _ClassVar[int]
    SHOULD_HIDE_HINT_FIELD_NUMBER: _ClassVar[int]
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    IS_PAIRED_FIELD_NUMBER: _ClassVar[int]
    STRENGTH_RAW_FIELD_NUMBER: _ClassVar[int]
    id: int
    should_hide_hint: bool
    etype: _enums_pb2.EBluetoothDeviceType
    is_connected: bool
    is_paired: bool
    strength_raw: int
    def __init__(self, id: _Optional[int] = ..., should_hide_hint: bool = ..., etype: _Optional[_Union[_enums_pb2.EBluetoothDeviceType, str]] = ..., is_connected: bool = ..., is_paired: bool = ..., strength_raw: _Optional[int] = ...) -> None: ...

class CBluetoothManager_GetState_Response(_message.Message):
    __slots__ = ("is_service_available", "is_enabled", "is_discovering", "adapters", "devices")
    IS_SERVICE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DISCOVERING_FIELD_NUMBER: _ClassVar[int]
    ADAPTERS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    is_service_available: bool
    is_enabled: bool
    is_discovering: bool
    adapters: _containers.RepeatedCompositeFieldContainer[CMsgBluetoothManagerAdapterInfo]
    devices: _containers.RepeatedCompositeFieldContainer[CMsgBluetoothManagerDeviceInfo]
    def __init__(self, is_service_available: bool = ..., is_enabled: bool = ..., is_discovering: bool = ..., adapters: _Optional[_Iterable[_Union[CMsgBluetoothManagerAdapterInfo, _Mapping]]] = ..., devices: _Optional[_Iterable[_Union[CMsgBluetoothManagerDeviceInfo, _Mapping]]] = ...) -> None: ...

class CBluetoothManager_GetAdapterDetails_Request(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CMsgBluetoothManagerAdapterDetails(_message.Message):
    __slots__ = ("id", "mac", "name", "is_enabled", "is_discovering")
    ID_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DISCOVERING_FIELD_NUMBER: _ClassVar[int]
    id: int
    mac: str
    name: str
    is_enabled: bool
    is_discovering: bool
    def __init__(self, id: _Optional[int] = ..., mac: _Optional[str] = ..., name: _Optional[str] = ..., is_enabled: bool = ..., is_discovering: bool = ...) -> None: ...

class CBluetoothManager_GetAdapterDetails_Response(_message.Message):
    __slots__ = ("adapter",)
    ADAPTER_FIELD_NUMBER: _ClassVar[int]
    adapter: CMsgBluetoothManagerAdapterDetails
    def __init__(self, adapter: _Optional[_Union[CMsgBluetoothManagerAdapterDetails, _Mapping]] = ...) -> None: ...

class CBluetoothManager_GetDeviceDetails_Request(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class CMsgBluetoothManagerDeviceDetails(_message.Message):
    __slots__ = ("id", "adapter_id", "etype", "mac", "name", "is_connected", "is_paired", "is_pairing", "wake_allowed", "wake_allowed_supported", "battery_percent", "operation_in_progress")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_ID_FIELD_NUMBER: _ClassVar[int]
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    IS_PAIRED_FIELD_NUMBER: _ClassVar[int]
    IS_PAIRING_FIELD_NUMBER: _ClassVar[int]
    WAKE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    WAKE_ALLOWED_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
    OPERATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    id: int
    adapter_id: int
    etype: _enums_pb2.EBluetoothDeviceType
    mac: str
    name: str
    is_connected: bool
    is_paired: bool
    is_pairing: bool
    wake_allowed: bool
    wake_allowed_supported: bool
    battery_percent: int
    operation_in_progress: bool
    def __init__(self, id: _Optional[int] = ..., adapter_id: _Optional[int] = ..., etype: _Optional[_Union[_enums_pb2.EBluetoothDeviceType, str]] = ..., mac: _Optional[str] = ..., name: _Optional[str] = ..., is_connected: bool = ..., is_paired: bool = ..., is_pairing: bool = ..., wake_allowed: bool = ..., wake_allowed_supported: bool = ..., battery_percent: _Optional[int] = ..., operation_in_progress: bool = ...) -> None: ...

class CBluetoothManager_GetDeviceDetails_Response(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: CMsgBluetoothManagerDeviceDetails
    def __init__(self, device: _Optional[_Union[CMsgBluetoothManagerDeviceDetails, _Mapping]] = ...) -> None: ...

class CBluetoothManager_StateChanged_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_SetDiscovering_Request(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CBluetoothManager_SetDiscovering_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_Pair_Request(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: int
    def __init__(self, device: _Optional[int] = ...) -> None: ...

class CBluetoothManager_Pair_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_CancelPair_Request(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: int
    def __init__(self, device: _Optional[int] = ...) -> None: ...

class CBluetoothManager_CancelPair_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_Forget_Request(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: int
    def __init__(self, device: _Optional[int] = ...) -> None: ...

class CBluetoothManager_Forget_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_Connect_Request(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: int
    def __init__(self, device: _Optional[int] = ...) -> None: ...

class CBluetoothManager_Connect_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_Disconnect_Request(_message.Message):
    __slots__ = ("device",)
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    device: int
    def __init__(self, device: _Optional[int] = ...) -> None: ...

class CBluetoothManager_Disconnect_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBluetoothManager_SetWakeAllowed_Request(_message.Message):
    __slots__ = ("device", "allowed")
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    device: int
    allowed: bool
    def __init__(self, device: _Optional[int] = ..., allowed: bool = ...) -> None: ...

class CBluetoothManager_SetWakeAllowed_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BluetoothManager(_service.service): ...

class BluetoothManager_Stub(BluetoothManager): ...
