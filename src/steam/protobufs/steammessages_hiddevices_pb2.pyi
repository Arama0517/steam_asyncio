from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EHIDDeviceLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EDeviceLocationLocal: _ClassVar[EHIDDeviceLocation]
    k_EDeviceLocationRemote: _ClassVar[EHIDDeviceLocation]
    k_EDeviceLocationAny: _ClassVar[EHIDDeviceLocation]

class EHIDDeviceDisconnectMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EDeviceDisconnectMethodUnknown: _ClassVar[EHIDDeviceDisconnectMethod]
    k_EDeviceDisconnectMethodBluetooth: _ClassVar[EHIDDeviceDisconnectMethod]
    k_EDeviceDisconnectMethodFeatureReport: _ClassVar[EHIDDeviceDisconnectMethod]
    k_EDeviceDisconnectMethodOutputReport: _ClassVar[EHIDDeviceDisconnectMethod]
k_EDeviceLocationLocal: EHIDDeviceLocation
k_EDeviceLocationRemote: EHIDDeviceLocation
k_EDeviceLocationAny: EHIDDeviceLocation
k_EDeviceDisconnectMethodUnknown: EHIDDeviceDisconnectMethod
k_EDeviceDisconnectMethodBluetooth: EHIDDeviceDisconnectMethod
k_EDeviceDisconnectMethodFeatureReport: EHIDDeviceDisconnectMethod
k_EDeviceDisconnectMethodOutputReport: EHIDDeviceDisconnectMethod

class CHIDDeviceInfo(_message.Message):
    __slots__ = ("location", "path", "vendor_id", "product_id", "serial_number", "release_number", "manufacturer_string", "product_string", "usage_page", "usage", "interface_number", "ostype", "is_generic_gamepad", "is_generic_joystick", "caps_bits", "session_id", "eControllerType_OBSOLETE", "is_xinput_device_OBSOLETE", "session_remote_play_together_appid", "is_steamvr_device")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    RELEASE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_STRING_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_STRING_FIELD_NUMBER: _ClassVar[int]
    USAGE_PAGE_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OSTYPE_FIELD_NUMBER: _ClassVar[int]
    IS_GENERIC_GAMEPAD_FIELD_NUMBER: _ClassVar[int]
    IS_GENERIC_JOYSTICK_FIELD_NUMBER: _ClassVar[int]
    CAPS_BITS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ECONTROLLERTYPE_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    IS_XINPUT_DEVICE_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    SESSION_REMOTE_PLAY_TOGETHER_APPID_FIELD_NUMBER: _ClassVar[int]
    IS_STEAMVR_DEVICE_FIELD_NUMBER: _ClassVar[int]
    location: EHIDDeviceLocation
    path: str
    vendor_id: int
    product_id: int
    serial_number: str
    release_number: int
    manufacturer_string: str
    product_string: str
    usage_page: int
    usage: int
    interface_number: int
    ostype: int
    is_generic_gamepad: bool
    is_generic_joystick: bool
    caps_bits: int
    session_id: int
    eControllerType_OBSOLETE: int
    is_xinput_device_OBSOLETE: bool
    session_remote_play_together_appid: int
    is_steamvr_device: bool
    def __init__(self, location: _Optional[_Union[EHIDDeviceLocation, str]] = ..., path: _Optional[str] = ..., vendor_id: _Optional[int] = ..., product_id: _Optional[int] = ..., serial_number: _Optional[str] = ..., release_number: _Optional[int] = ..., manufacturer_string: _Optional[str] = ..., product_string: _Optional[str] = ..., usage_page: _Optional[int] = ..., usage: _Optional[int] = ..., interface_number: _Optional[int] = ..., ostype: _Optional[int] = ..., is_generic_gamepad: bool = ..., is_generic_joystick: bool = ..., caps_bits: _Optional[int] = ..., session_id: _Optional[int] = ..., eControllerType_OBSOLETE: _Optional[int] = ..., is_xinput_device_OBSOLETE: bool = ..., session_remote_play_together_appid: _Optional[int] = ..., is_steamvr_device: bool = ...) -> None: ...

class CHIDDeviceInputReport(_message.Message):
    __slots__ = ("full_report", "delta_report", "delta_report_size", "delta_report_crc")
    FULL_REPORT_FIELD_NUMBER: _ClassVar[int]
    DELTA_REPORT_FIELD_NUMBER: _ClassVar[int]
    DELTA_REPORT_SIZE_FIELD_NUMBER: _ClassVar[int]
    DELTA_REPORT_CRC_FIELD_NUMBER: _ClassVar[int]
    full_report: bytes
    delta_report: bytes
    delta_report_size: int
    delta_report_crc: int
    def __init__(self, full_report: _Optional[bytes] = ..., delta_report: _Optional[bytes] = ..., delta_report_size: _Optional[int] = ..., delta_report_crc: _Optional[int] = ...) -> None: ...

class CHIDMessageToRemote(_message.Message):
    __slots__ = ("request_id", "device_open", "device_close", "device_write", "device_read", "device_send_feature_report", "device_get_feature_report", "device_get_vendor_string", "device_get_product_string", "device_get_serial_number_string", "device_start_input_reports", "device_request_full_report", "device_disconnect")
    class DeviceOpen(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: CHIDDeviceInfo
        def __init__(self, info: _Optional[_Union[CHIDDeviceInfo, _Mapping]] = ...) -> None: ...
    class DeviceClose(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: int
        def __init__(self, device: _Optional[int] = ...) -> None: ...
    class DeviceWrite(_message.Message):
        __slots__ = ("device", "data")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        device: int
        data: bytes
        def __init__(self, device: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    class DeviceRead(_message.Message):
        __slots__ = ("device", "length", "timeout_ms")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
        device: int
        length: int
        timeout_ms: int
        def __init__(self, device: _Optional[int] = ..., length: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...
    class DeviceSendFeatureReport(_message.Message):
        __slots__ = ("device", "data")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        device: int
        data: bytes
        def __init__(self, device: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    class DeviceGetFeatureReport(_message.Message):
        __slots__ = ("device", "report_number", "length")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        REPORT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        device: int
        report_number: bytes
        length: int
        def __init__(self, device: _Optional[int] = ..., report_number: _Optional[bytes] = ..., length: _Optional[int] = ...) -> None: ...
    class DeviceGetVendorString(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: int
        def __init__(self, device: _Optional[int] = ...) -> None: ...
    class DeviceGetProductString(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: int
        def __init__(self, device: _Optional[int] = ...) -> None: ...
    class DeviceGetSerialNumberString(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: int
        def __init__(self, device: _Optional[int] = ...) -> None: ...
    class DeviceStartInputReports(_message.Message):
        __slots__ = ("device", "length")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        device: int
        length: int
        def __init__(self, device: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...
    class DeviceRequestFullReport(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: int
        def __init__(self, device: _Optional[int] = ...) -> None: ...
    class DeviceDisconnect(_message.Message):
        __slots__ = ("device", "disconnectMethod", "data")
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTMETHOD_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        device: int
        disconnectMethod: EHIDDeviceDisconnectMethod
        data: bytes
        def __init__(self, device: _Optional[int] = ..., disconnectMethod: _Optional[_Union[EHIDDeviceDisconnectMethod, str]] = ..., data: _Optional[bytes] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_OPEN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLOSE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_WRITE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_READ_FIELD_NUMBER: _ClassVar[int]
    DEVICE_SEND_FEATURE_REPORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_GET_FEATURE_REPORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_GET_VENDOR_STRING_FIELD_NUMBER: _ClassVar[int]
    DEVICE_GET_PRODUCT_STRING_FIELD_NUMBER: _ClassVar[int]
    DEVICE_GET_SERIAL_NUMBER_STRING_FIELD_NUMBER: _ClassVar[int]
    DEVICE_START_INPUT_REPORTS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_REQUEST_FULL_REPORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DISCONNECT_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    device_open: CHIDMessageToRemote.DeviceOpen
    device_close: CHIDMessageToRemote.DeviceClose
    device_write: CHIDMessageToRemote.DeviceWrite
    device_read: CHIDMessageToRemote.DeviceRead
    device_send_feature_report: CHIDMessageToRemote.DeviceSendFeatureReport
    device_get_feature_report: CHIDMessageToRemote.DeviceGetFeatureReport
    device_get_vendor_string: CHIDMessageToRemote.DeviceGetVendorString
    device_get_product_string: CHIDMessageToRemote.DeviceGetProductString
    device_get_serial_number_string: CHIDMessageToRemote.DeviceGetSerialNumberString
    device_start_input_reports: CHIDMessageToRemote.DeviceStartInputReports
    device_request_full_report: CHIDMessageToRemote.DeviceRequestFullReport
    device_disconnect: CHIDMessageToRemote.DeviceDisconnect
    def __init__(self, request_id: _Optional[int] = ..., device_open: _Optional[_Union[CHIDMessageToRemote.DeviceOpen, _Mapping]] = ..., device_close: _Optional[_Union[CHIDMessageToRemote.DeviceClose, _Mapping]] = ..., device_write: _Optional[_Union[CHIDMessageToRemote.DeviceWrite, _Mapping]] = ..., device_read: _Optional[_Union[CHIDMessageToRemote.DeviceRead, _Mapping]] = ..., device_send_feature_report: _Optional[_Union[CHIDMessageToRemote.DeviceSendFeatureReport, _Mapping]] = ..., device_get_feature_report: _Optional[_Union[CHIDMessageToRemote.DeviceGetFeatureReport, _Mapping]] = ..., device_get_vendor_string: _Optional[_Union[CHIDMessageToRemote.DeviceGetVendorString, _Mapping]] = ..., device_get_product_string: _Optional[_Union[CHIDMessageToRemote.DeviceGetProductString, _Mapping]] = ..., device_get_serial_number_string: _Optional[_Union[CHIDMessageToRemote.DeviceGetSerialNumberString, _Mapping]] = ..., device_start_input_reports: _Optional[_Union[CHIDMessageToRemote.DeviceStartInputReports, _Mapping]] = ..., device_request_full_report: _Optional[_Union[CHIDMessageToRemote.DeviceRequestFullReport, _Mapping]] = ..., device_disconnect: _Optional[_Union[CHIDMessageToRemote.DeviceDisconnect, _Mapping]] = ...) -> None: ...

class CHIDMessageFromRemote(_message.Message):
    __slots__ = ("update_device_list", "response", "reports", "close_device", "close_all_devices")
    class UpdateDeviceList(_message.Message):
        __slots__ = ("devices",)
        DEVICES_FIELD_NUMBER: _ClassVar[int]
        devices: _containers.RepeatedCompositeFieldContainer[CHIDDeviceInfo]
        def __init__(self, devices: _Optional[_Iterable[_Union[CHIDDeviceInfo, _Mapping]]] = ...) -> None: ...
    class RequestResponse(_message.Message):
        __slots__ = ("request_id", "result", "data")
        REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        request_id: int
        result: int
        data: bytes
        def __init__(self, request_id: _Optional[int] = ..., result: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
    class DeviceInputReports(_message.Message):
        __slots__ = ("device_reports",)
        class DeviceInputReport(_message.Message):
            __slots__ = ("device", "reports")
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            REPORTS_FIELD_NUMBER: _ClassVar[int]
            device: int
            reports: _containers.RepeatedCompositeFieldContainer[CHIDDeviceInputReport]
            def __init__(self, device: _Optional[int] = ..., reports: _Optional[_Iterable[_Union[CHIDDeviceInputReport, _Mapping]]] = ...) -> None: ...
        DEVICE_REPORTS_FIELD_NUMBER: _ClassVar[int]
        device_reports: _containers.RepeatedCompositeFieldContainer[CHIDMessageFromRemote.DeviceInputReports.DeviceInputReport]
        def __init__(self, device_reports: _Optional[_Iterable[_Union[CHIDMessageFromRemote.DeviceInputReports.DeviceInputReport, _Mapping]]] = ...) -> None: ...
    class CloseDevice(_message.Message):
        __slots__ = ("device",)
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        device: int
        def __init__(self, device: _Optional[int] = ...) -> None: ...
    class CloseAllDevices(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    UPDATE_DEVICE_LIST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    CLOSE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_ALL_DEVICES_FIELD_NUMBER: _ClassVar[int]
    update_device_list: CHIDMessageFromRemote.UpdateDeviceList
    response: CHIDMessageFromRemote.RequestResponse
    reports: CHIDMessageFromRemote.DeviceInputReports
    close_device: CHIDMessageFromRemote.CloseDevice
    close_all_devices: CHIDMessageFromRemote.CloseAllDevices
    def __init__(self, update_device_list: _Optional[_Union[CHIDMessageFromRemote.UpdateDeviceList, _Mapping]] = ..., response: _Optional[_Union[CHIDMessageFromRemote.RequestResponse, _Mapping]] = ..., reports: _Optional[_Union[CHIDMessageFromRemote.DeviceInputReports, _Mapping]] = ..., close_device: _Optional[_Union[CHIDMessageFromRemote.CloseDevice, _Mapping]] = ..., close_all_devices: _Optional[_Union[CHIDMessageFromRemote.CloseAllDevices, _Mapping]] = ...) -> None: ...
