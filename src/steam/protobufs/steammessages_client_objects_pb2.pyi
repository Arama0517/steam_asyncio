import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ECloudPendingRemoteOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ECloudPendingRemoteOperationNone: _ClassVar[ECloudPendingRemoteOperation]
    k_ECloudPendingRemoteOperationAppSessionActive: _ClassVar[ECloudPendingRemoteOperation]
    k_ECloudPendingRemoteOperationUploadInProgress: _ClassVar[ECloudPendingRemoteOperation]
    k_ECloudPendingRemoteOperationUploadPending: _ClassVar[ECloudPendingRemoteOperation]
    k_ECloudPendingRemoteOperationAppSessionSuspended: _ClassVar[ECloudPendingRemoteOperation]

class ESteamDeckKeyboardLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESteamDeckKeyboardLayout_QWERTY: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Bulgarian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Chinese_Simplified: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Chinese_Traditional: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Czech: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Danish: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Finnish: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_French: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_German: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Greek: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Hungarian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Italian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Japanese: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Korean: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Norwegian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Polish: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Portuguese: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Romanian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Russian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Spanish: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Swedish: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Thai: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Turkish_F: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Turkish_Q: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Ukrainian: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Vietnamese: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_QWERTY_International: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Dvorak: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Colemak: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Bulgarian_Phonetic_Traditional: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Bulgarian_Phonetic: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Chinese_Traditional_Bopomofo: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Chinese_Traditional_Cangjie: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Japanese_Kana: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Chinese_Traditional_Quick: _ClassVar[ESteamDeckKeyboardLayout]
    k_ESteamDeckKeyboardLayout_Indonesian: _ClassVar[ESteamDeckKeyboardLayout]
k_ECloudPendingRemoteOperationNone: ECloudPendingRemoteOperation
k_ECloudPendingRemoteOperationAppSessionActive: ECloudPendingRemoteOperation
k_ECloudPendingRemoteOperationUploadInProgress: ECloudPendingRemoteOperation
k_ECloudPendingRemoteOperationUploadPending: ECloudPendingRemoteOperation
k_ECloudPendingRemoteOperationAppSessionSuspended: ECloudPendingRemoteOperation
k_ESteamDeckKeyboardLayout_QWERTY: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Bulgarian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Chinese_Simplified: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Chinese_Traditional: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Czech: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Danish: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Finnish: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_French: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_German: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Greek: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Hungarian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Italian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Japanese: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Korean: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Norwegian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Polish: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Portuguese: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Romanian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Russian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Spanish: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Swedish: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Thai: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Turkish_F: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Turkish_Q: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Ukrainian: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Vietnamese: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_QWERTY_International: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Dvorak: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Colemak: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Bulgarian_Phonetic_Traditional: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Bulgarian_Phonetic: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Chinese_Traditional_Bopomofo: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Chinese_Traditional_Cangjie: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Japanese_Kana: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Chinese_Traditional_Quick: ESteamDeckKeyboardLayout
k_ESteamDeckKeyboardLayout_Indonesian: ESteamDeckKeyboardLayout

class SteamMessagesClientIClientForcedEnumDependencies(_message.Message):
    __slots__ = ("a", "b", "c", "d")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    a: _enums_pb2.EBluetoothDeviceType
    b: _enums_pb2.EStorageBlockContentType
    c: _enums_pb2.EStorageBlockFileSystemType
    d: _enums_pb2.ESDCardFormatStage
    def __init__(self, a: _Optional[_Union[_enums_pb2.EBluetoothDeviceType, str]] = ..., b: _Optional[_Union[_enums_pb2.EStorageBlockContentType, str]] = ..., c: _Optional[_Union[_enums_pb2.EStorageBlockFileSystemType, str]] = ..., d: _Optional[_Union[_enums_pb2.ESDCardFormatStage, str]] = ...) -> None: ...

class CMsgNetworkDeviceIP4Address(_message.Message):
    __slots__ = ("ip", "netmask")
    IP_FIELD_NUMBER: _ClassVar[int]
    NETMASK_FIELD_NUMBER: _ClassVar[int]
    ip: int
    netmask: int
    def __init__(self, ip: _Optional[int] = ..., netmask: _Optional[int] = ...) -> None: ...

class CMsgNetworkDeviceIP4Config(_message.Message):
    __slots__ = ("addresses", "dns_ip", "gateway_ip", "is_dhcp_enabled", "is_default_route", "is_enabled")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    DNS_IP_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    IS_DHCP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_ROUTE_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[CMsgNetworkDeviceIP4Address]
    dns_ip: _containers.RepeatedScalarFieldContainer[int]
    gateway_ip: int
    is_dhcp_enabled: bool
    is_default_route: bool
    is_enabled: bool
    def __init__(self, addresses: _Optional[_Iterable[_Union[CMsgNetworkDeviceIP4Address, _Mapping]]] = ..., dns_ip: _Optional[_Iterable[int]] = ..., gateway_ip: _Optional[int] = ..., is_dhcp_enabled: bool = ..., is_default_route: bool = ..., is_enabled: bool = ...) -> None: ...

class CMsgNetworkDeviceIP6Address(_message.Message):
    __slots__ = ("ip",)
    IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    def __init__(self, ip: _Optional[str] = ...) -> None: ...

class CMsgNetworkDeviceIP6Config(_message.Message):
    __slots__ = ("addresses", "dns_ip", "gateway_ip", "is_dhcp_enabled", "is_default_route", "is_enabled")
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    DNS_IP_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IP_FIELD_NUMBER: _ClassVar[int]
    IS_DHCP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_ROUTE_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[CMsgNetworkDeviceIP6Address]
    dns_ip: _containers.RepeatedScalarFieldContainer[str]
    gateway_ip: str
    is_dhcp_enabled: bool
    is_default_route: bool
    is_enabled: bool
    def __init__(self, addresses: _Optional[_Iterable[_Union[CMsgNetworkDeviceIP6Address, _Mapping]]] = ..., dns_ip: _Optional[_Iterable[str]] = ..., gateway_ip: _Optional[str] = ..., is_dhcp_enabled: bool = ..., is_default_route: bool = ..., is_enabled: bool = ...) -> None: ...

class CMsgNetworkDevicesData(_message.Message):
    __slots__ = ("devices", "is_wifi_enabled", "is_wifi_scanning_enabled")
    class Device(_message.Message):
        __slots__ = ("id", "etype", "estate", "mac", "vendor", "product", "ip4", "ip6", "wired", "wireless")
        class Wired(_message.Message):
            __slots__ = ("is_cable_present", "speed_mbit", "friendly_name")
            IS_CABLE_PRESENT_FIELD_NUMBER: _ClassVar[int]
            SPEED_MBIT_FIELD_NUMBER: _ClassVar[int]
            FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
            is_cable_present: bool
            speed_mbit: int
            friendly_name: str
            def __init__(self, is_cable_present: bool = ..., speed_mbit: _Optional[int] = ..., friendly_name: _Optional[str] = ...) -> None: ...
        class Wireless(_message.Message):
            __slots__ = ("aps", "esecurity_supported")
            class AP(_message.Message):
                __slots__ = ("id", "estrength", "ssid", "is_active", "is_autoconnect", "esecurity", "user_name", "password", "strength_raw")
                ID_FIELD_NUMBER: _ClassVar[int]
                ESTRENGTH_FIELD_NUMBER: _ClassVar[int]
                SSID_FIELD_NUMBER: _ClassVar[int]
                IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
                IS_AUTOCONNECT_FIELD_NUMBER: _ClassVar[int]
                ESECURITY_FIELD_NUMBER: _ClassVar[int]
                USER_NAME_FIELD_NUMBER: _ClassVar[int]
                PASSWORD_FIELD_NUMBER: _ClassVar[int]
                STRENGTH_RAW_FIELD_NUMBER: _ClassVar[int]
                id: int
                estrength: int
                ssid: str
                is_active: bool
                is_autoconnect: bool
                esecurity: int
                user_name: str
                password: str
                strength_raw: int
                def __init__(self, id: _Optional[int] = ..., estrength: _Optional[int] = ..., ssid: _Optional[str] = ..., is_active: bool = ..., is_autoconnect: bool = ..., esecurity: _Optional[int] = ..., user_name: _Optional[str] = ..., password: _Optional[str] = ..., strength_raw: _Optional[int] = ...) -> None: ...
            APS_FIELD_NUMBER: _ClassVar[int]
            ESECURITY_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
            aps: _containers.RepeatedCompositeFieldContainer[CMsgNetworkDevicesData.Device.Wireless.AP]
            esecurity_supported: int
            def __init__(self, aps: _Optional[_Iterable[_Union[CMsgNetworkDevicesData.Device.Wireless.AP, _Mapping]]] = ..., esecurity_supported: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        ETYPE_FIELD_NUMBER: _ClassVar[int]
        ESTATE_FIELD_NUMBER: _ClassVar[int]
        MAC_FIELD_NUMBER: _ClassVar[int]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_FIELD_NUMBER: _ClassVar[int]
        IP4_FIELD_NUMBER: _ClassVar[int]
        IP6_FIELD_NUMBER: _ClassVar[int]
        WIRED_FIELD_NUMBER: _ClassVar[int]
        WIRELESS_FIELD_NUMBER: _ClassVar[int]
        id: int
        etype: int
        estate: int
        mac: str
        vendor: str
        product: str
        ip4: CMsgNetworkDeviceIP4Config
        ip6: CMsgNetworkDeviceIP6Config
        wired: CMsgNetworkDevicesData.Device.Wired
        wireless: CMsgNetworkDevicesData.Device.Wireless
        def __init__(self, id: _Optional[int] = ..., etype: _Optional[int] = ..., estate: _Optional[int] = ..., mac: _Optional[str] = ..., vendor: _Optional[str] = ..., product: _Optional[str] = ..., ip4: _Optional[_Union[CMsgNetworkDeviceIP4Config, _Mapping]] = ..., ip6: _Optional[_Union[CMsgNetworkDeviceIP6Config, _Mapping]] = ..., wired: _Optional[_Union[CMsgNetworkDevicesData.Device.Wired, _Mapping]] = ..., wireless: _Optional[_Union[CMsgNetworkDevicesData.Device.Wireless, _Mapping]] = ...) -> None: ...
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    IS_WIFI_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_WIFI_SCANNING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[CMsgNetworkDevicesData.Device]
    is_wifi_enabled: bool
    is_wifi_scanning_enabled: bool
    def __init__(self, devices: _Optional[_Iterable[_Union[CMsgNetworkDevicesData.Device, _Mapping]]] = ..., is_wifi_enabled: bool = ..., is_wifi_scanning_enabled: bool = ...) -> None: ...

class CMsgNetworkDeviceConnect(_message.Message):
    __slots__ = ("device_id", "credentials", "ip4", "ip6", "ap_known", "ap_custom")
    class KnownAP(_message.Message):
        __slots__ = ("ap_id",)
        AP_ID_FIELD_NUMBER: _ClassVar[int]
        ap_id: int
        def __init__(self, ap_id: _Optional[int] = ...) -> None: ...
    class CustomAP(_message.Message):
        __slots__ = ("ssid", "esecurity")
        SSID_FIELD_NUMBER: _ClassVar[int]
        ESECURITY_FIELD_NUMBER: _ClassVar[int]
        ssid: str
        esecurity: int
        def __init__(self, ssid: _Optional[str] = ..., esecurity: _Optional[int] = ...) -> None: ...
    class Credentials(_message.Message):
        __slots__ = ("username", "password")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        username: str
        password: str
        def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    IP4_FIELD_NUMBER: _ClassVar[int]
    IP6_FIELD_NUMBER: _ClassVar[int]
    AP_KNOWN_FIELD_NUMBER: _ClassVar[int]
    AP_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    device_id: int
    credentials: CMsgNetworkDeviceConnect.Credentials
    ip4: CMsgNetworkDeviceIP4Config
    ip6: CMsgNetworkDeviceIP6Config
    ap_known: CMsgNetworkDeviceConnect.KnownAP
    ap_custom: CMsgNetworkDeviceConnect.CustomAP
    def __init__(self, device_id: _Optional[int] = ..., credentials: _Optional[_Union[CMsgNetworkDeviceConnect.Credentials, _Mapping]] = ..., ip4: _Optional[_Union[CMsgNetworkDeviceIP4Config, _Mapping]] = ..., ip6: _Optional[_Union[CMsgNetworkDeviceIP6Config, _Mapping]] = ..., ap_known: _Optional[_Union[CMsgNetworkDeviceConnect.KnownAP, _Mapping]] = ..., ap_custom: _Optional[_Union[CMsgNetworkDeviceConnect.CustomAP, _Mapping]] = ...) -> None: ...

class CMsgStorageDevicesData(_message.Message):
    __slots__ = ("drives", "block_devices", "is_unmount_supported", "is_trim_supported", "is_trim_running")
    class Drive(_message.Message):
        __slots__ = ("id", "model", "vendor", "serial", "is_ejectable", "size_bytes", "media_type")
        ID_FIELD_NUMBER: _ClassVar[int]
        MODEL_FIELD_NUMBER: _ClassVar[int]
        VENDOR_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        IS_EJECTABLE_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
        id: int
        model: str
        vendor: str
        serial: str
        is_ejectable: bool
        size_bytes: int
        media_type: _enums_pb2.EStorageDriveMediaType
        def __init__(self, id: _Optional[int] = ..., model: _Optional[str] = ..., vendor: _Optional[str] = ..., serial: _Optional[str] = ..., is_ejectable: bool = ..., size_bytes: _Optional[int] = ..., media_type: _Optional[_Union[_enums_pb2.EStorageDriveMediaType, str]] = ...) -> None: ...
    class BlockDevice(_message.Message):
        __slots__ = ("id", "drive_id", "path", "friendly_path", "label", "size_bytes", "is_formattable", "is_read_only", "is_root_device", "content_type", "filesystem_type", "mount_path")
        ID_FIELD_NUMBER: _ClassVar[int]
        DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        FRIENDLY_PATH_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        IS_FORMATTABLE_FIELD_NUMBER: _ClassVar[int]
        IS_READ_ONLY_FIELD_NUMBER: _ClassVar[int]
        IS_ROOT_DEVICE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        FILESYSTEM_TYPE_FIELD_NUMBER: _ClassVar[int]
        MOUNT_PATH_FIELD_NUMBER: _ClassVar[int]
        id: int
        drive_id: int
        path: str
        friendly_path: str
        label: str
        size_bytes: int
        is_formattable: bool
        is_read_only: bool
        is_root_device: bool
        content_type: _enums_pb2.EStorageBlockContentType
        filesystem_type: _enums_pb2.EStorageBlockFileSystemType
        mount_path: str
        def __init__(self, id: _Optional[int] = ..., drive_id: _Optional[int] = ..., path: _Optional[str] = ..., friendly_path: _Optional[str] = ..., label: _Optional[str] = ..., size_bytes: _Optional[int] = ..., is_formattable: bool = ..., is_read_only: bool = ..., is_root_device: bool = ..., content_type: _Optional[_Union[_enums_pb2.EStorageBlockContentType, str]] = ..., filesystem_type: _Optional[_Union[_enums_pb2.EStorageBlockFileSystemType, str]] = ..., mount_path: _Optional[str] = ...) -> None: ...
    DRIVES_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DEVICES_FIELD_NUMBER: _ClassVar[int]
    IS_UNMOUNT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_TRIM_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_TRIM_RUNNING_FIELD_NUMBER: _ClassVar[int]
    drives: _containers.RepeatedCompositeFieldContainer[CMsgStorageDevicesData.Drive]
    block_devices: _containers.RepeatedCompositeFieldContainer[CMsgStorageDevicesData.BlockDevice]
    is_unmount_supported: bool
    is_trim_supported: bool
    is_trim_running: bool
    def __init__(self, drives: _Optional[_Iterable[_Union[CMsgStorageDevicesData.Drive, _Mapping]]] = ..., block_devices: _Optional[_Iterable[_Union[CMsgStorageDevicesData.BlockDevice, _Mapping]]] = ..., is_unmount_supported: bool = ..., is_trim_supported: bool = ..., is_trim_running: bool = ...) -> None: ...

class CCloud_PendingRemoteOperation(_message.Message):
    __slots__ = ("operation", "machine_name", "client_id", "time_last_updated", "os_type", "device_type")
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    operation: ECloudPendingRemoteOperation
    machine_name: str
    client_id: int
    time_last_updated: int
    os_type: int
    device_type: int
    def __init__(self, operation: _Optional[_Union[ECloudPendingRemoteOperation, str]] = ..., machine_name: _Optional[str] = ..., client_id: _Optional[int] = ..., time_last_updated: _Optional[int] = ..., os_type: _Optional[int] = ..., device_type: _Optional[int] = ...) -> None: ...

class CMsgCloudPendingRemoteOperations(_message.Message):
    __slots__ = ("operations",)
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[CCloud_PendingRemoteOperation]
    def __init__(self, operations: _Optional[_Iterable[_Union[CCloud_PendingRemoteOperation, _Mapping]]] = ...) -> None: ...

class CMsgBluetoothDevicesData(_message.Message):
    __slots__ = ("adapters", "devices", "manager")
    class Adapter(_message.Message):
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
    class Device(_message.Message):
        __slots__ = ("id", "adapter_id", "etype", "mac", "name", "is_connected", "is_paired", "strength_raw", "wake_allowed", "wake_allowed_supported", "battery_percent")
        ID_FIELD_NUMBER: _ClassVar[int]
        ADAPTER_ID_FIELD_NUMBER: _ClassVar[int]
        ETYPE_FIELD_NUMBER: _ClassVar[int]
        MAC_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IS_CONNECTED_FIELD_NUMBER: _ClassVar[int]
        IS_PAIRED_FIELD_NUMBER: _ClassVar[int]
        STRENGTH_RAW_FIELD_NUMBER: _ClassVar[int]
        WAKE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
        WAKE_ALLOWED_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        BATTERY_PERCENT_FIELD_NUMBER: _ClassVar[int]
        id: int
        adapter_id: int
        etype: _enums_pb2.EBluetoothDeviceType
        mac: str
        name: str
        is_connected: bool
        is_paired: bool
        strength_raw: int
        wake_allowed: bool
        wake_allowed_supported: bool
        battery_percent: int
        def __init__(self, id: _Optional[int] = ..., adapter_id: _Optional[int] = ..., etype: _Optional[_Union[_enums_pb2.EBluetoothDeviceType, str]] = ..., mac: _Optional[str] = ..., name: _Optional[str] = ..., is_connected: bool = ..., is_paired: bool = ..., strength_raw: _Optional[int] = ..., wake_allowed: bool = ..., wake_allowed_supported: bool = ..., battery_percent: _Optional[int] = ...) -> None: ...
    class Manager(_message.Message):
        __slots__ = ("is_bluetooth_enabled",)
        IS_BLUETOOTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
        is_bluetooth_enabled: bool
        def __init__(self, is_bluetooth_enabled: bool = ...) -> None: ...
    ADAPTERS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    MANAGER_FIELD_NUMBER: _ClassVar[int]
    adapters: _containers.RepeatedCompositeFieldContainer[CMsgBluetoothDevicesData.Adapter]
    devices: _containers.RepeatedCompositeFieldContainer[CMsgBluetoothDevicesData.Device]
    manager: CMsgBluetoothDevicesData.Manager
    def __init__(self, adapters: _Optional[_Iterable[_Union[CMsgBluetoothDevicesData.Adapter, _Mapping]]] = ..., devices: _Optional[_Iterable[_Union[CMsgBluetoothDevicesData.Device, _Mapping]]] = ..., manager: _Optional[_Union[CMsgBluetoothDevicesData.Manager, _Mapping]] = ...) -> None: ...

class CMsgSystemPerfDiagnosticEntry(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CMsgSystemPerfNetworkInterface(_message.Message):
    __slots__ = ("name", "timestamp", "tx_bytes_total", "rx_bytes_total", "tx_bytes_per_sec", "rx_bytes_per_sec")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TX_BYTES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    RX_BYTES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TX_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    RX_BYTES_PER_SEC_FIELD_NUMBER: _ClassVar[int]
    name: str
    timestamp: float
    tx_bytes_total: int
    rx_bytes_total: int
    tx_bytes_per_sec: int
    rx_bytes_per_sec: int
    def __init__(self, name: _Optional[str] = ..., timestamp: _Optional[float] = ..., tx_bytes_total: _Optional[int] = ..., rx_bytes_total: _Optional[int] = ..., tx_bytes_per_sec: _Optional[int] = ..., rx_bytes_per_sec: _Optional[int] = ...) -> None: ...

class CMsgSystemPerfDiagnosticInfo(_message.Message):
    __slots__ = ("entries", "interfaces", "battery_temp_c")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    INTERFACES_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMP_C_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgSystemPerfDiagnosticEntry]
    interfaces: _containers.RepeatedCompositeFieldContainer[CMsgSystemPerfNetworkInterface]
    battery_temp_c: float
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgSystemPerfDiagnosticEntry, _Mapping]]] = ..., interfaces: _Optional[_Iterable[_Union[CMsgSystemPerfNetworkInterface, _Mapping]]] = ..., battery_temp_c: _Optional[float] = ...) -> None: ...

class CMsgSystemPerfLimits(_message.Message):
    __slots__ = ("cpu_governor_manual_min_mhz", "cpu_governor_manual_max_mhz", "fsr_sharpness_min", "fsr_sharpness_max", "gpu_performance_manual_min_mhz", "gpu_performance_manual_max_mhz", "perf_overlay_is_standalone", "is_dynamic_vrs_available", "is_manual_display_refresh_rate_available", "gpu_performance_levels_available", "display_refresh_manual_hz_min", "display_refresh_manual_hz_max", "fps_limit_options", "tdp_limit_min", "tdp_limit_max", "is_nis_supported", "nis_sharpness_min", "nis_sharpness_max", "display_external_refresh_manual_hz_min", "display_external_refresh_manual_hz_max", "fps_limit_options_external", "is_vrr_supported", "is_dynamic_refresh_rate_in_steam_supported", "is_split_scaling_and_filtering_supported", "split_scaling_filters_available", "split_scaling_scalers_available", "is_hdr_supported", "display_refresh_manual_hz_oc_max", "disable_refresh_rate_management")
    CPU_GOVERNOR_MANUAL_MIN_MHZ_FIELD_NUMBER: _ClassVar[int]
    CPU_GOVERNOR_MANUAL_MAX_MHZ_FIELD_NUMBER: _ClassVar[int]
    FSR_SHARPNESS_MIN_FIELD_NUMBER: _ClassVar[int]
    FSR_SHARPNESS_MAX_FIELD_NUMBER: _ClassVar[int]
    GPU_PERFORMANCE_MANUAL_MIN_MHZ_FIELD_NUMBER: _ClassVar[int]
    GPU_PERFORMANCE_MANUAL_MAX_MHZ_FIELD_NUMBER: _ClassVar[int]
    PERF_OVERLAY_IS_STANDALONE_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_VRS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_MANUAL_DISPLAY_REFRESH_RATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    GPU_PERFORMANCE_LEVELS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_REFRESH_MANUAL_HZ_MIN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_REFRESH_MANUAL_HZ_MAX_FIELD_NUMBER: _ClassVar[int]
    FPS_LIMIT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TDP_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
    TDP_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
    IS_NIS_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    NIS_SHARPNESS_MIN_FIELD_NUMBER: _ClassVar[int]
    NIS_SHARPNESS_MAX_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_EXTERNAL_REFRESH_MANUAL_HZ_MIN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_EXTERNAL_REFRESH_MANUAL_HZ_MAX_FIELD_NUMBER: _ClassVar[int]
    FPS_LIMIT_OPTIONS_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    IS_VRR_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_REFRESH_RATE_IN_STEAM_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_SPLIT_SCALING_AND_FILTERING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    SPLIT_SCALING_FILTERS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SPLIT_SCALING_SCALERS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_REFRESH_MANUAL_HZ_OC_MAX_FIELD_NUMBER: _ClassVar[int]
    DISABLE_REFRESH_RATE_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    cpu_governor_manual_min_mhz: int
    cpu_governor_manual_max_mhz: int
    fsr_sharpness_min: int
    fsr_sharpness_max: int
    gpu_performance_manual_min_mhz: int
    gpu_performance_manual_max_mhz: int
    perf_overlay_is_standalone: bool
    is_dynamic_vrs_available: bool
    is_manual_display_refresh_rate_available: bool
    gpu_performance_levels_available: _containers.RepeatedScalarFieldContainer[_enums_pb2.EGPUPerformanceLevel]
    display_refresh_manual_hz_min: int
    display_refresh_manual_hz_max: int
    fps_limit_options: _containers.RepeatedScalarFieldContainer[int]
    tdp_limit_min: int
    tdp_limit_max: int
    is_nis_supported: bool
    nis_sharpness_min: int
    nis_sharpness_max: int
    display_external_refresh_manual_hz_min: int
    display_external_refresh_manual_hz_max: int
    fps_limit_options_external: _containers.RepeatedScalarFieldContainer[int]
    is_vrr_supported: bool
    is_dynamic_refresh_rate_in_steam_supported: bool
    is_split_scaling_and_filtering_supported: bool
    split_scaling_filters_available: _containers.RepeatedScalarFieldContainer[_enums_pb2.ESplitScalingFilter]
    split_scaling_scalers_available: _containers.RepeatedScalarFieldContainer[_enums_pb2.ESplitScalingScaler]
    is_hdr_supported: bool
    display_refresh_manual_hz_oc_max: int
    disable_refresh_rate_management: bool
    def __init__(self, cpu_governor_manual_min_mhz: _Optional[int] = ..., cpu_governor_manual_max_mhz: _Optional[int] = ..., fsr_sharpness_min: _Optional[int] = ..., fsr_sharpness_max: _Optional[int] = ..., gpu_performance_manual_min_mhz: _Optional[int] = ..., gpu_performance_manual_max_mhz: _Optional[int] = ..., perf_overlay_is_standalone: bool = ..., is_dynamic_vrs_available: bool = ..., is_manual_display_refresh_rate_available: bool = ..., gpu_performance_levels_available: _Optional[_Iterable[_Union[_enums_pb2.EGPUPerformanceLevel, str]]] = ..., display_refresh_manual_hz_min: _Optional[int] = ..., display_refresh_manual_hz_max: _Optional[int] = ..., fps_limit_options: _Optional[_Iterable[int]] = ..., tdp_limit_min: _Optional[int] = ..., tdp_limit_max: _Optional[int] = ..., is_nis_supported: bool = ..., nis_sharpness_min: _Optional[int] = ..., nis_sharpness_max: _Optional[int] = ..., display_external_refresh_manual_hz_min: _Optional[int] = ..., display_external_refresh_manual_hz_max: _Optional[int] = ..., fps_limit_options_external: _Optional[_Iterable[int]] = ..., is_vrr_supported: bool = ..., is_dynamic_refresh_rate_in_steam_supported: bool = ..., is_split_scaling_and_filtering_supported: bool = ..., split_scaling_filters_available: _Optional[_Iterable[_Union[_enums_pb2.ESplitScalingFilter, str]]] = ..., split_scaling_scalers_available: _Optional[_Iterable[_Union[_enums_pb2.ESplitScalingScaler, str]]] = ..., is_hdr_supported: bool = ..., display_refresh_manual_hz_oc_max: _Optional[int] = ..., disable_refresh_rate_management: bool = ...) -> None: ...

class CMsgSystemPerfSettingsGlobal(_message.Message):
    __slots__ = ("diagnostic_update_rate", "system_trace_service_state", "graphics_profiling_service_state", "perf_overlay_service_state", "perf_overlay_level", "is_show_perf_overlay_over_steam_enabled", "is_advanced_settings_enabled", "allow_external_display_refresh_control", "is_hdr_enabled", "hdr_on_sdr_tonemap_operator", "is_hdr_debug_heatmap_enabled", "force_hdr_wide_gammut_for_sdr", "allow_experimental_hdr", "sdr_to_hdr_brightness", "debug_force_hdr_support", "force_hdr_10pq_output_debug", "is_display_oc_enabled", "is_color_management_enabled")
    DIAGNOSTIC_UPDATE_RATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TRACE_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    GRAPHICS_PROFILING_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    PERF_OVERLAY_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    PERF_OVERLAY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_PERF_OVERLAY_OVER_STEAM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_ADVANCED_SETTINGS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXTERNAL_DISPLAY_REFRESH_CONTROL_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HDR_ON_SDR_TONEMAP_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_DEBUG_HEATMAP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FORCE_HDR_WIDE_GAMMUT_FOR_SDR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXPERIMENTAL_HDR_FIELD_NUMBER: _ClassVar[int]
    SDR_TO_HDR_BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FORCE_HDR_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    FORCE_HDR_10PQ_OUTPUT_DEBUG_FIELD_NUMBER: _ClassVar[int]
    IS_DISPLAY_OC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_COLOR_MANAGEMENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    diagnostic_update_rate: float
    system_trace_service_state: _enums_pb2.ESystemServiceState
    graphics_profiling_service_state: _enums_pb2.ESystemServiceState
    perf_overlay_service_state: _enums_pb2.ESystemServiceState
    perf_overlay_level: _enums_pb2.EGraphicsPerfOverlayLevel
    is_show_perf_overlay_over_steam_enabled: bool
    is_advanced_settings_enabled: bool
    allow_external_display_refresh_control: bool
    is_hdr_enabled: bool
    hdr_on_sdr_tonemap_operator: _enums_pb2.EHDRToneMapOperator
    is_hdr_debug_heatmap_enabled: bool
    force_hdr_wide_gammut_for_sdr: bool
    allow_experimental_hdr: bool
    sdr_to_hdr_brightness: float
    debug_force_hdr_support: bool
    force_hdr_10pq_output_debug: bool
    is_display_oc_enabled: bool
    is_color_management_enabled: bool
    def __init__(self, diagnostic_update_rate: _Optional[float] = ..., system_trace_service_state: _Optional[_Union[_enums_pb2.ESystemServiceState, str]] = ..., graphics_profiling_service_state: _Optional[_Union[_enums_pb2.ESystemServiceState, str]] = ..., perf_overlay_service_state: _Optional[_Union[_enums_pb2.ESystemServiceState, str]] = ..., perf_overlay_level: _Optional[_Union[_enums_pb2.EGraphicsPerfOverlayLevel, str]] = ..., is_show_perf_overlay_over_steam_enabled: bool = ..., is_advanced_settings_enabled: bool = ..., allow_external_display_refresh_control: bool = ..., is_hdr_enabled: bool = ..., hdr_on_sdr_tonemap_operator: _Optional[_Union[_enums_pb2.EHDRToneMapOperator, str]] = ..., is_hdr_debug_heatmap_enabled: bool = ..., force_hdr_wide_gammut_for_sdr: bool = ..., allow_experimental_hdr: bool = ..., sdr_to_hdr_brightness: _Optional[float] = ..., debug_force_hdr_support: bool = ..., force_hdr_10pq_output_debug: bool = ..., is_display_oc_enabled: bool = ..., is_color_management_enabled: bool = ...) -> None: ...

class CMsgSystemPerfSettingsPerApp(_message.Message):
    __slots__ = ("gpu_performance_manual_mhz", "fps_limit", "is_variable_resolution_enabled", "is_dynamic_refresh_rate_enabled", "tdp_limit", "cpu_governor", "cpu_governor_manual_mhz", "scaling_filter", "fsr_sharpness", "is_fps_limit_enabled", "is_tdp_limit_enabled", "is_low_latency_mode_enabled", "display_refresh_manual_hz", "is_game_perf_profile_enabled", "gpu_performance_level", "nis_sharpness", "display_external_refresh_manual_hz", "fps_limit_external", "is_tearing_enabled", "is_vrr_enabled", "use_dynamic_refresh_rate_in_steam", "split_scaling_filter", "split_scaling_scaler")
    GPU_PERFORMANCE_MANUAL_MHZ_FIELD_NUMBER: _ClassVar[int]
    FPS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    IS_VARIABLE_RESOLUTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_REFRESH_RATE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TDP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    CPU_GOVERNOR_MANUAL_MHZ_FIELD_NUMBER: _ClassVar[int]
    SCALING_FILTER_FIELD_NUMBER: _ClassVar[int]
    FSR_SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    IS_FPS_LIMIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_TDP_LIMIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_LATENCY_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_REFRESH_MANUAL_HZ_FIELD_NUMBER: _ClassVar[int]
    IS_GAME_PERF_PROFILE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GPU_PERFORMANCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NIS_SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_EXTERNAL_REFRESH_MANUAL_HZ_FIELD_NUMBER: _ClassVar[int]
    FPS_LIMIT_EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    IS_TEARING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_VRR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    USE_DYNAMIC_REFRESH_RATE_IN_STEAM_FIELD_NUMBER: _ClassVar[int]
    SPLIT_SCALING_FILTER_FIELD_NUMBER: _ClassVar[int]
    SPLIT_SCALING_SCALER_FIELD_NUMBER: _ClassVar[int]
    gpu_performance_manual_mhz: int
    fps_limit: int
    is_variable_resolution_enabled: bool
    is_dynamic_refresh_rate_enabled: bool
    tdp_limit: int
    cpu_governor: _enums_pb2.ECPUGovernor
    cpu_governor_manual_mhz: int
    scaling_filter: int
    fsr_sharpness: int
    is_fps_limit_enabled: bool
    is_tdp_limit_enabled: bool
    is_low_latency_mode_enabled: bool
    display_refresh_manual_hz: int
    is_game_perf_profile_enabled: bool
    gpu_performance_level: _enums_pb2.EGPUPerformanceLevel
    nis_sharpness: int
    display_external_refresh_manual_hz: int
    fps_limit_external: int
    is_tearing_enabled: bool
    is_vrr_enabled: bool
    use_dynamic_refresh_rate_in_steam: bool
    split_scaling_filter: _enums_pb2.ESplitScalingFilter
    split_scaling_scaler: _enums_pb2.ESplitScalingScaler
    def __init__(self, gpu_performance_manual_mhz: _Optional[int] = ..., fps_limit: _Optional[int] = ..., is_variable_resolution_enabled: bool = ..., is_dynamic_refresh_rate_enabled: bool = ..., tdp_limit: _Optional[int] = ..., cpu_governor: _Optional[_Union[_enums_pb2.ECPUGovernor, str]] = ..., cpu_governor_manual_mhz: _Optional[int] = ..., scaling_filter: _Optional[int] = ..., fsr_sharpness: _Optional[int] = ..., is_fps_limit_enabled: bool = ..., is_tdp_limit_enabled: bool = ..., is_low_latency_mode_enabled: bool = ..., display_refresh_manual_hz: _Optional[int] = ..., is_game_perf_profile_enabled: bool = ..., gpu_performance_level: _Optional[_Union[_enums_pb2.EGPUPerformanceLevel, str]] = ..., nis_sharpness: _Optional[int] = ..., display_external_refresh_manual_hz: _Optional[int] = ..., fps_limit_external: _Optional[int] = ..., is_tearing_enabled: bool = ..., is_vrr_enabled: bool = ..., use_dynamic_refresh_rate_in_steam: bool = ..., split_scaling_filter: _Optional[_Union[_enums_pb2.ESplitScalingFilter, str]] = ..., split_scaling_scaler: _Optional[_Union[_enums_pb2.ESplitScalingScaler, str]] = ...) -> None: ...

class CMsgSystemPerfSettings(_message.Message):
    __slots__ = ("per_app",)
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    PER_APP_FIELD_NUMBER: _ClassVar[int]
    per_app: CMsgSystemPerfSettingsPerApp
    def __init__(self, per_app: _Optional[_Union[CMsgSystemPerfSettingsPerApp, _Mapping]] = ..., **kwargs) -> None: ...

class CMsgSystemPerfSettingsV1(_message.Message):
    __slots__ = ("diagnostic_update_rate", "system_trace_service_state", "graphics_profiling_service_state", "perf_overlay_service_state", "perf_overlay_level", "gpu_performance_level", "gpu_performance_manual_mhz", "fps_limit", "is_variable_resolution_enabled", "is_dynamic_refresh_rate_enabled", "tdp_limit", "cpu_governor", "cpu_governor_manual_mhz", "scaling_filter", "fsr_sharpness", "is_fps_limit_enabled", "is_tdp_limit_enabled", "is_show_perf_overlay_over_steam_enabled", "is_low_latency_mode_enabled", "display_refresh_manual_hz", "is_game_perf_profile_enabled")
    DIAGNOSTIC_UPDATE_RATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TRACE_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    GRAPHICS_PROFILING_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    PERF_OVERLAY_SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    PERF_OVERLAY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GPU_PERFORMANCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    GPU_PERFORMANCE_MANUAL_MHZ_FIELD_NUMBER: _ClassVar[int]
    FPS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    IS_VARIABLE_RESOLUTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_DYNAMIC_REFRESH_RATE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TDP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_GOVERNOR_FIELD_NUMBER: _ClassVar[int]
    CPU_GOVERNOR_MANUAL_MHZ_FIELD_NUMBER: _ClassVar[int]
    SCALING_FILTER_FIELD_NUMBER: _ClassVar[int]
    FSR_SHARPNESS_FIELD_NUMBER: _ClassVar[int]
    IS_FPS_LIMIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_TDP_LIMIT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_PERF_OVERLAY_OVER_STEAM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_LOW_LATENCY_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_REFRESH_MANUAL_HZ_FIELD_NUMBER: _ClassVar[int]
    IS_GAME_PERF_PROFILE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    diagnostic_update_rate: float
    system_trace_service_state: _enums_pb2.ESystemServiceState
    graphics_profiling_service_state: _enums_pb2.ESystemServiceState
    perf_overlay_service_state: _enums_pb2.ESystemServiceState
    perf_overlay_level: _enums_pb2.EGraphicsPerfOverlayLevel
    gpu_performance_level: _enums_pb2.EGPUPerformanceLevel
    gpu_performance_manual_mhz: int
    fps_limit: int
    is_variable_resolution_enabled: bool
    is_dynamic_refresh_rate_enabled: bool
    tdp_limit: int
    cpu_governor: _enums_pb2.ECPUGovernor
    cpu_governor_manual_mhz: int
    scaling_filter: int
    fsr_sharpness: int
    is_fps_limit_enabled: bool
    is_tdp_limit_enabled: bool
    is_show_perf_overlay_over_steam_enabled: bool
    is_low_latency_mode_enabled: bool
    display_refresh_manual_hz: int
    is_game_perf_profile_enabled: bool
    def __init__(self, diagnostic_update_rate: _Optional[float] = ..., system_trace_service_state: _Optional[_Union[_enums_pb2.ESystemServiceState, str]] = ..., graphics_profiling_service_state: _Optional[_Union[_enums_pb2.ESystemServiceState, str]] = ..., perf_overlay_service_state: _Optional[_Union[_enums_pb2.ESystemServiceState, str]] = ..., perf_overlay_level: _Optional[_Union[_enums_pb2.EGraphicsPerfOverlayLevel, str]] = ..., gpu_performance_level: _Optional[_Union[_enums_pb2.EGPUPerformanceLevel, str]] = ..., gpu_performance_manual_mhz: _Optional[int] = ..., fps_limit: _Optional[int] = ..., is_variable_resolution_enabled: bool = ..., is_dynamic_refresh_rate_enabled: bool = ..., tdp_limit: _Optional[int] = ..., cpu_governor: _Optional[_Union[_enums_pb2.ECPUGovernor, str]] = ..., cpu_governor_manual_mhz: _Optional[int] = ..., scaling_filter: _Optional[int] = ..., fsr_sharpness: _Optional[int] = ..., is_fps_limit_enabled: bool = ..., is_tdp_limit_enabled: bool = ..., is_show_perf_overlay_over_steam_enabled: bool = ..., is_low_latency_mode_enabled: bool = ..., display_refresh_manual_hz: _Optional[int] = ..., is_game_perf_profile_enabled: bool = ...) -> None: ...

class CMsgSystemPerfState(_message.Message):
    __slots__ = ("limits", "settings", "current_game_id", "active_profile_game_id")
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_PROFILE_GAME_ID_FIELD_NUMBER: _ClassVar[int]
    limits: CMsgSystemPerfLimits
    settings: CMsgSystemPerfSettings
    current_game_id: int
    active_profile_game_id: int
    def __init__(self, limits: _Optional[_Union[CMsgSystemPerfLimits, _Mapping]] = ..., settings: _Optional[_Union[CMsgSystemPerfSettings, _Mapping]] = ..., current_game_id: _Optional[int] = ..., active_profile_game_id: _Optional[int] = ...) -> None: ...

class CMsgSystemPerfUpdateSettings(_message.Message):
    __slots__ = ("gameid", "skip_storage_update", "reset_to_default", "settings_delta")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    SKIP_STORAGE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    RESET_TO_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_DELTA_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    skip_storage_update: bool
    reset_to_default: bool
    settings_delta: CMsgSystemPerfSettings
    def __init__(self, gameid: _Optional[int] = ..., skip_storage_update: bool = ..., reset_to_default: bool = ..., settings_delta: _Optional[_Union[CMsgSystemPerfSettings, _Mapping]] = ...) -> None: ...

class CMsgSystemPerfLegacySettingEntry(_message.Message):
    __slots__ = ("profile_game_id", "settings")
    PROFILE_GAME_ID_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    profile_game_id: int
    settings: CMsgSystemPerfSettingsPerApp
    def __init__(self, profile_game_id: _Optional[int] = ..., settings: _Optional[_Union[CMsgSystemPerfSettingsPerApp, _Mapping]] = ...) -> None: ...

class CMsgSystemPerfLegacySettings(_message.Message):
    __slots__ = ("per_app_settings",)
    GLOBAL_FIELD_NUMBER: _ClassVar[int]
    PER_APP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    per_app_settings: _containers.RepeatedCompositeFieldContainer[CMsgSystemPerfLegacySettingEntry]
    def __init__(self, per_app_settings: _Optional[_Iterable[_Union[CMsgSystemPerfLegacySettingEntry, _Mapping]]] = ..., **kwargs) -> None: ...

class CMsgSystemDockUpdateState(_message.Message):
    __slots__ = ("state", "rtime_last_checked", "version_current", "version_available", "stage_progress", "rtime_estimated_completion", "old_fw_workaround")
    STATE_FIELD_NUMBER: _ClassVar[int]
    RTIME_LAST_CHECKED_FIELD_NUMBER: _ClassVar[int]
    VERSION_CURRENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STAGE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    RTIME_ESTIMATED_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    OLD_FW_WORKAROUND_FIELD_NUMBER: _ClassVar[int]
    state: _enums_pb2.EUpdaterState
    rtime_last_checked: int
    version_current: str
    version_available: str
    stage_progress: float
    rtime_estimated_completion: int
    old_fw_workaround: int
    def __init__(self, state: _Optional[_Union[_enums_pb2.EUpdaterState, str]] = ..., rtime_last_checked: _Optional[int] = ..., version_current: _Optional[str] = ..., version_available: _Optional[str] = ..., stage_progress: _Optional[float] = ..., rtime_estimated_completion: _Optional[int] = ..., old_fw_workaround: _Optional[int] = ...) -> None: ...

class CMsgSystemDockState(_message.Message):
    __slots__ = ("update_state",)
    UPDATE_STATE_FIELD_NUMBER: _ClassVar[int]
    update_state: CMsgSystemDockUpdateState
    def __init__(self, update_state: _Optional[_Union[CMsgSystemDockUpdateState, _Mapping]] = ...) -> None: ...

class CMsgSystemDockUpdateFirmware(_message.Message):
    __slots__ = ("check_only",)
    CHECK_ONLY_FIELD_NUMBER: _ClassVar[int]
    check_only: bool
    def __init__(self, check_only: bool = ...) -> None: ...

class CMsgSystemAudioVolume(_message.Message):
    __slots__ = ("entries", "is_muted")
    class ChannelEntry(_message.Message):
        __slots__ = ("echannel", "volume")
        ECHANNEL_FIELD_NUMBER: _ClassVar[int]
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        echannel: _enums_pb2.ESystemAudioChannel
        volume: float
        def __init__(self, echannel: _Optional[_Union[_enums_pb2.ESystemAudioChannel, str]] = ..., volume: _Optional[float] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    IS_MUTED_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgSystemAudioVolume.ChannelEntry]
    is_muted: bool
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgSystemAudioVolume.ChannelEntry, _Mapping]]] = ..., is_muted: bool = ...) -> None: ...

class CMsgSystemAudioManagerObject(_message.Message):
    __slots__ = ("id", "rtime_last_update")
    ID_FIELD_NUMBER: _ClassVar[int]
    RTIME_LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    rtime_last_update: int
    def __init__(self, id: _Optional[int] = ..., rtime_last_update: _Optional[int] = ...) -> None: ...

class CMsgSystemAudioManagerDevice(_message.Message):
    __slots__ = ("base", "name", "nick", "description", "api")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    base: CMsgSystemAudioManagerObject
    name: str
    nick: str
    description: str
    api: str
    def __init__(self, base: _Optional[_Union[CMsgSystemAudioManagerObject, _Mapping]] = ..., name: _Optional[str] = ..., nick: _Optional[str] = ..., description: _Optional[str] = ..., api: _Optional[str] = ...) -> None: ...

class CMsgSystemAudioManagerNode(_message.Message):
    __slots__ = ("base", "device_id", "name", "nick", "description", "edirection", "volume")
    BASE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NICK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EDIRECTION_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    base: CMsgSystemAudioManagerObject
    device_id: int
    name: str
    nick: str
    description: str
    edirection: _enums_pb2.ESystemAudioDirection
    volume: CMsgSystemAudioVolume
    def __init__(self, base: _Optional[_Union[CMsgSystemAudioManagerObject, _Mapping]] = ..., device_id: _Optional[int] = ..., name: _Optional[str] = ..., nick: _Optional[str] = ..., description: _Optional[str] = ..., edirection: _Optional[_Union[_enums_pb2.ESystemAudioDirection, str]] = ..., volume: _Optional[_Union[CMsgSystemAudioVolume, _Mapping]] = ...) -> None: ...

class CMsgSystemAudioManagerPort(_message.Message):
    __slots__ = ("base", "node_id", "name", "alias", "etype", "edirection", "is_physical", "is_terminal", "is_control", "is_monitor")
    BASE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    ETYPE_FIELD_NUMBER: _ClassVar[int]
    EDIRECTION_FIELD_NUMBER: _ClassVar[int]
    IS_PHYSICAL_FIELD_NUMBER: _ClassVar[int]
    IS_TERMINAL_FIELD_NUMBER: _ClassVar[int]
    IS_CONTROL_FIELD_NUMBER: _ClassVar[int]
    IS_MONITOR_FIELD_NUMBER: _ClassVar[int]
    base: CMsgSystemAudioManagerObject
    node_id: int
    name: str
    alias: str
    etype: _enums_pb2.ESystemAudioPortType
    edirection: _enums_pb2.ESystemAudioPortDirection
    is_physical: bool
    is_terminal: bool
    is_control: bool
    is_monitor: bool
    def __init__(self, base: _Optional[_Union[CMsgSystemAudioManagerObject, _Mapping]] = ..., node_id: _Optional[int] = ..., name: _Optional[str] = ..., alias: _Optional[str] = ..., etype: _Optional[_Union[_enums_pb2.ESystemAudioPortType, str]] = ..., edirection: _Optional[_Union[_enums_pb2.ESystemAudioPortDirection, str]] = ..., is_physical: bool = ..., is_terminal: bool = ..., is_control: bool = ..., is_monitor: bool = ...) -> None: ...

class CMsgSystemAudioManagerLink(_message.Message):
    __slots__ = ("base", "output_node_id", "output_port_id", "input_node_id", "input_port_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PORT_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_PORT_ID_FIELD_NUMBER: _ClassVar[int]
    base: CMsgSystemAudioManagerObject
    output_node_id: int
    output_port_id: int
    input_node_id: int
    input_port_id: int
    def __init__(self, base: _Optional[_Union[CMsgSystemAudioManagerObject, _Mapping]] = ..., output_node_id: _Optional[int] = ..., output_port_id: _Optional[int] = ..., input_node_id: _Optional[int] = ..., input_port_id: _Optional[int] = ...) -> None: ...

class CMsgSystemAudioManagerStateHW(_message.Message):
    __slots__ = ("devices", "nodes", "ports", "links")
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    PORTS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[CMsgSystemAudioManagerDevice]
    nodes: _containers.RepeatedCompositeFieldContainer[CMsgSystemAudioManagerNode]
    ports: _containers.RepeatedCompositeFieldContainer[CMsgSystemAudioManagerPort]
    links: _containers.RepeatedCompositeFieldContainer[CMsgSystemAudioManagerLink]
    def __init__(self, devices: _Optional[_Iterable[_Union[CMsgSystemAudioManagerDevice, _Mapping]]] = ..., nodes: _Optional[_Iterable[_Union[CMsgSystemAudioManagerNode, _Mapping]]] = ..., ports: _Optional[_Iterable[_Union[CMsgSystemAudioManagerPort, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[CMsgSystemAudioManagerLink, _Mapping]]] = ...) -> None: ...

class CMsgSystemAudioManagerState(_message.Message):
    __slots__ = ("rtime_filter", "counter", "hw")
    RTIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    HW_FIELD_NUMBER: _ClassVar[int]
    rtime_filter: int
    counter: int
    hw: CMsgSystemAudioManagerStateHW
    def __init__(self, rtime_filter: _Optional[int] = ..., counter: _Optional[int] = ..., hw: _Optional[_Union[CMsgSystemAudioManagerStateHW, _Mapping]] = ...) -> None: ...

class CMsgSystemAudioManagerUpdateSomething(_message.Message):
    __slots__ = ("counter",)
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    counter: int
    def __init__(self, counter: _Optional[int] = ...) -> None: ...

class CMsgSystemDisplayMode(_message.Message):
    __slots__ = ("id", "width", "height", "refresh_hz")
    ID_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_HZ_FIELD_NUMBER: _ClassVar[int]
    id: int
    width: int
    height: int
    refresh_hz: int
    def __init__(self, id: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., refresh_hz: _Optional[int] = ...) -> None: ...

class CMsgSystemDisplay(_message.Message):
    __slots__ = ("id", "name", "description", "is_primary", "is_enabled", "is_internal", "has_mode_override", "width_mm", "height_mm", "current_mode_id", "modes", "refresh_rate_min", "refresh_rate_max", "is_vrr_capable", "is_vrr_enabled", "is_hdr_capable", "is_hdr_enabled", "supported_refresh_rates")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    HAS_MODE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_MM_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_MM_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MODE_ID_FIELD_NUMBER: _ClassVar[int]
    MODES_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RATE_MIN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RATE_MAX_FIELD_NUMBER: _ClassVar[int]
    IS_VRR_CAPABLE_FIELD_NUMBER: _ClassVar[int]
    IS_VRR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_CAPABLE_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_REFRESH_RATES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    is_primary: bool
    is_enabled: bool
    is_internal: bool
    has_mode_override: bool
    width_mm: int
    height_mm: int
    current_mode_id: int
    modes: _containers.RepeatedCompositeFieldContainer[CMsgSystemDisplayMode]
    refresh_rate_min: int
    refresh_rate_max: int
    is_vrr_capable: bool
    is_vrr_enabled: bool
    is_hdr_capable: bool
    is_hdr_enabled: bool
    supported_refresh_rates: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_primary: bool = ..., is_enabled: bool = ..., is_internal: bool = ..., has_mode_override: bool = ..., width_mm: _Optional[int] = ..., height_mm: _Optional[int] = ..., current_mode_id: _Optional[int] = ..., modes: _Optional[_Iterable[_Union[CMsgSystemDisplayMode, _Mapping]]] = ..., refresh_rate_min: _Optional[int] = ..., refresh_rate_max: _Optional[int] = ..., is_vrr_capable: bool = ..., is_vrr_enabled: bool = ..., is_hdr_capable: bool = ..., is_hdr_enabled: bool = ..., supported_refresh_rates: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgSystemDisplayManagerState(_message.Message):
    __slots__ = ("displays", "is_mode_switching_supported", "compatibility_mode")
    DISPLAYS_FIELD_NUMBER: _ClassVar[int]
    IS_MODE_SWITCHING_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    displays: _containers.RepeatedCompositeFieldContainer[CMsgSystemDisplay]
    is_mode_switching_supported: bool
    compatibility_mode: _enums_pb2.ESystemDisplayCompatibilityMode
    def __init__(self, displays: _Optional[_Iterable[_Union[CMsgSystemDisplay, _Mapping]]] = ..., is_mode_switching_supported: bool = ..., compatibility_mode: _Optional[_Union[_enums_pb2.ESystemDisplayCompatibilityMode, str]] = ...) -> None: ...

class CMsgSystemDisplayManagerSetMode(_message.Message):
    __slots__ = ("display_id", "mode_id")
    DISPLAY_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_ID_FIELD_NUMBER: _ClassVar[int]
    display_id: int
    mode_id: int
    def __init__(self, display_id: _Optional[int] = ..., mode_id: _Optional[int] = ...) -> None: ...

class CMsgSystemManagerSettings(_message.Message):
    __slots__ = ("idle_backlight_dim_battery_seconds", "idle_backlight_dim_ac_seconds", "idle_suspend_battery_seconds", "idle_suspend_ac_seconds", "idle_suspend_supressed", "is_adaptive_brightness_available", "display_adaptive_brightness_enabled", "display_nightmode_enabled", "display_nightmode_tintstrength", "display_nightmode_maxhue", "display_nightmode_maxsat", "display_nightmode_uiexp", "display_nightmode_blend", "display_nightmode_reset", "display_nightmode_schedule_enabled", "display_nightmode_schedule_starttime", "display_nightmode_schedule_endtime", "display_diagnostics_enabled", "als_lux_primary", "als_lux_median", "display_backlight_raw", "display_brightness_adaptivemin", "display_brightness_adaptivemax", "is_wifi_powersave_enabled", "is_fan_control_available", "fan_control_mode", "is_display_brightness_available", "is_display_colormanagement_available", "display_colorgamut", "als_lux_alternate", "is_display_colortemp_available", "display_colortemp", "display_colortemp_default", "display_colortemp_enabled", "display_colorgamut_labelset", "display_brightness_overdrive_hdr_split")
    IDLE_BACKLIGHT_DIM_BATTERY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IDLE_BACKLIGHT_DIM_AC_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IDLE_SUSPEND_BATTERY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IDLE_SUSPEND_AC_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IDLE_SUSPEND_SUPRESSED_FIELD_NUMBER: _ClassVar[int]
    IS_ADAPTIVE_BRIGHTNESS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ADAPTIVE_BRIGHTNESS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_TINTSTRENGTH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_MAXHUE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_MAXSAT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_UIEXP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_BLEND_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_RESET_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_SCHEDULE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_SCHEDULE_STARTTIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NIGHTMODE_SCHEDULE_ENDTIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DIAGNOSTICS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALS_LUX_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    ALS_LUX_MEDIAN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BACKLIGHT_RAW_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BRIGHTNESS_ADAPTIVEMIN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BRIGHTNESS_ADAPTIVEMAX_FIELD_NUMBER: _ClassVar[int]
    IS_WIFI_POWERSAVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_FAN_CONTROL_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    FAN_CONTROL_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_DISPLAY_BRIGHTNESS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    IS_DISPLAY_COLORMANAGEMENT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_COLORGAMUT_FIELD_NUMBER: _ClassVar[int]
    ALS_LUX_ALTERNATE_FIELD_NUMBER: _ClassVar[int]
    IS_DISPLAY_COLORTEMP_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_COLORTEMP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_COLORTEMP_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_COLORTEMP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_COLORGAMUT_LABELSET_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_BRIGHTNESS_OVERDRIVE_HDR_SPLIT_FIELD_NUMBER: _ClassVar[int]
    idle_backlight_dim_battery_seconds: float
    idle_backlight_dim_ac_seconds: float
    idle_suspend_battery_seconds: float
    idle_suspend_ac_seconds: float
    idle_suspend_supressed: bool
    is_adaptive_brightness_available: bool
    display_adaptive_brightness_enabled: bool
    display_nightmode_enabled: bool
    display_nightmode_tintstrength: float
    display_nightmode_maxhue: float
    display_nightmode_maxsat: float
    display_nightmode_uiexp: float
    display_nightmode_blend: float
    display_nightmode_reset: bool
    display_nightmode_schedule_enabled: bool
    display_nightmode_schedule_starttime: float
    display_nightmode_schedule_endtime: float
    display_diagnostics_enabled: bool
    als_lux_primary: float
    als_lux_median: float
    display_backlight_raw: float
    display_brightness_adaptivemin: float
    display_brightness_adaptivemax: float
    is_wifi_powersave_enabled: bool
    is_fan_control_available: bool
    fan_control_mode: _enums_pb2.ESystemFanControlMode
    is_display_brightness_available: bool
    is_display_colormanagement_available: bool
    display_colorgamut: float
    als_lux_alternate: float
    is_display_colortemp_available: bool
    display_colortemp: float
    display_colortemp_default: float
    display_colortemp_enabled: bool
    display_colorgamut_labelset: _enums_pb2.EColorGamutLabelSet
    display_brightness_overdrive_hdr_split: float
    def __init__(self, idle_backlight_dim_battery_seconds: _Optional[float] = ..., idle_backlight_dim_ac_seconds: _Optional[float] = ..., idle_suspend_battery_seconds: _Optional[float] = ..., idle_suspend_ac_seconds: _Optional[float] = ..., idle_suspend_supressed: bool = ..., is_adaptive_brightness_available: bool = ..., display_adaptive_brightness_enabled: bool = ..., display_nightmode_enabled: bool = ..., display_nightmode_tintstrength: _Optional[float] = ..., display_nightmode_maxhue: _Optional[float] = ..., display_nightmode_maxsat: _Optional[float] = ..., display_nightmode_uiexp: _Optional[float] = ..., display_nightmode_blend: _Optional[float] = ..., display_nightmode_reset: bool = ..., display_nightmode_schedule_enabled: bool = ..., display_nightmode_schedule_starttime: _Optional[float] = ..., display_nightmode_schedule_endtime: _Optional[float] = ..., display_diagnostics_enabled: bool = ..., als_lux_primary: _Optional[float] = ..., als_lux_median: _Optional[float] = ..., display_backlight_raw: _Optional[float] = ..., display_brightness_adaptivemin: _Optional[float] = ..., display_brightness_adaptivemax: _Optional[float] = ..., is_wifi_powersave_enabled: bool = ..., is_fan_control_available: bool = ..., fan_control_mode: _Optional[_Union[_enums_pb2.ESystemFanControlMode, str]] = ..., is_display_brightness_available: bool = ..., is_display_colormanagement_available: bool = ..., display_colorgamut: _Optional[float] = ..., als_lux_alternate: _Optional[float] = ..., is_display_colortemp_available: bool = ..., display_colortemp: _Optional[float] = ..., display_colortemp_default: _Optional[float] = ..., display_colortemp_enabled: bool = ..., display_colorgamut_labelset: _Optional[_Union[_enums_pb2.EColorGamutLabelSet, str]] = ..., display_brightness_overdrive_hdr_split: _Optional[float] = ...) -> None: ...

class CMsgSelectOSBranchParams(_message.Message):
    __slots__ = ("branch", "custom_branch")
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BRANCH_FIELD_NUMBER: _ClassVar[int]
    branch: _enums_pb2.EOSBranch
    custom_branch: str
    def __init__(self, branch: _Optional[_Union[_enums_pb2.EOSBranch, str]] = ..., custom_branch: _Optional[str] = ...) -> None: ...

class CMsgSystemUpdateProgress(_message.Message):
    __slots__ = ("stage_progress", "stage_size_bytes", "rtime_estimated_completion")
    STAGE_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STAGE_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RTIME_ESTIMATED_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    stage_progress: float
    stage_size_bytes: int
    rtime_estimated_completion: int
    def __init__(self, stage_progress: _Optional[float] = ..., stage_size_bytes: _Optional[int] = ..., rtime_estimated_completion: _Optional[int] = ...) -> None: ...

class CMsgSystemUpdateCheckResult(_message.Message):
    __slots__ = ("type", "eresult", "rtime_checked", "available", "version", "auto_message", "system_restart_pending")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    RTIME_CHECKED_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    AUTO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_RESTART_PENDING_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.EUpdaterType
    eresult: int
    rtime_checked: int
    available: bool
    version: str
    auto_message: str
    system_restart_pending: bool
    def __init__(self, type: _Optional[_Union[_enums_pb2.EUpdaterType, str]] = ..., eresult: _Optional[int] = ..., rtime_checked: _Optional[int] = ..., available: bool = ..., version: _Optional[str] = ..., auto_message: _Optional[str] = ..., system_restart_pending: bool = ...) -> None: ...

class CMsgSystemUpdateApplyParams(_message.Message):
    __slots__ = ("apply_types",)
    APPLY_TYPES_FIELD_NUMBER: _ClassVar[int]
    apply_types: _containers.RepeatedScalarFieldContainer[_enums_pb2.EUpdaterType]
    def __init__(self, apply_types: _Optional[_Iterable[_Union[_enums_pb2.EUpdaterType, str]]] = ...) -> None: ...

class CMsgSystemUpdateApplyResult(_message.Message):
    __slots__ = ("type", "eresult", "requires_client_restart", "requires_system_restart")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_CLIENT_RESTART_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_SYSTEM_RESTART_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.EUpdaterType
    eresult: int
    requires_client_restart: bool
    requires_system_restart: bool
    def __init__(self, type: _Optional[_Union[_enums_pb2.EUpdaterType, str]] = ..., eresult: _Optional[int] = ..., requires_client_restart: bool = ..., requires_system_restart: bool = ...) -> None: ...

class CMsgSystemUpdateState(_message.Message):
    __slots__ = ("state", "progress", "update_check_results", "update_apply_results", "supports_os_updates")
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CHECK_RESULTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_APPLY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_OS_UPDATES_FIELD_NUMBER: _ClassVar[int]
    state: _enums_pb2.EUpdaterState
    progress: CMsgSystemUpdateProgress
    update_check_results: _containers.RepeatedCompositeFieldContainer[CMsgSystemUpdateCheckResult]
    update_apply_results: _containers.RepeatedCompositeFieldContainer[CMsgSystemUpdateApplyResult]
    supports_os_updates: bool
    def __init__(self, state: _Optional[_Union[_enums_pb2.EUpdaterState, str]] = ..., progress: _Optional[_Union[CMsgSystemUpdateProgress, _Mapping]] = ..., update_check_results: _Optional[_Iterable[_Union[CMsgSystemUpdateCheckResult, _Mapping]]] = ..., update_apply_results: _Optional[_Iterable[_Union[CMsgSystemUpdateApplyResult, _Mapping]]] = ..., supports_os_updates: bool = ...) -> None: ...

class CMsgAchievementChange(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgCellList(_message.Message):
    __slots__ = ("cells",)
    class Cell(_message.Message):
        __slots__ = ("cell_id", "loc_name")
        CELL_ID_FIELD_NUMBER: _ClassVar[int]
        LOC_NAME_FIELD_NUMBER: _ClassVar[int]
        cell_id: int
        loc_name: str
        def __init__(self, cell_id: _Optional[int] = ..., loc_name: _Optional[str] = ...) -> None: ...
    CELLS_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[CMsgCellList.Cell]
    def __init__(self, cells: _Optional[_Iterable[_Union[CMsgCellList.Cell, _Mapping]]] = ...) -> None: ...

class CMsgShortcutInfo(_message.Message):
    __slots__ = ("appid", "exe", "start_dir", "icon", "path", "args", "app_name", "override_appid", "flatpak_appid", "tags", "is_remote", "is_hidden", "is_temporary", "is_openvr", "allow_desktop_config", "allow_overlay", "rt_last_played_time", "is_devkit_shortcut", "devkit_gameid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    EXE_FIELD_NUMBER: _ClassVar[int]
    START_DIR_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_APPID_FIELD_NUMBER: _ClassVar[int]
    FLATPAK_APPID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    IS_REMOTE_FIELD_NUMBER: _ClassVar[int]
    IS_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IS_TEMPORARY_FIELD_NUMBER: _ClassVar[int]
    IS_OPENVR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DESKTOP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_OVERLAY_FIELD_NUMBER: _ClassVar[int]
    RT_LAST_PLAYED_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_DEVKIT_SHORTCUT_FIELD_NUMBER: _ClassVar[int]
    DEVKIT_GAMEID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    exe: str
    start_dir: str
    icon: str
    path: str
    args: str
    app_name: str
    override_appid: int
    flatpak_appid: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    is_remote: bool
    is_hidden: bool
    is_temporary: bool
    is_openvr: bool
    allow_desktop_config: bool
    allow_overlay: bool
    rt_last_played_time: int
    is_devkit_shortcut: bool
    devkit_gameid: str
    def __init__(self, appid: _Optional[int] = ..., exe: _Optional[str] = ..., start_dir: _Optional[str] = ..., icon: _Optional[str] = ..., path: _Optional[str] = ..., args: _Optional[str] = ..., app_name: _Optional[str] = ..., override_appid: _Optional[int] = ..., flatpak_appid: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., is_remote: bool = ..., is_hidden: bool = ..., is_temporary: bool = ..., is_openvr: bool = ..., allow_desktop_config: bool = ..., allow_overlay: bool = ..., rt_last_played_time: _Optional[int] = ..., is_devkit_shortcut: bool = ..., devkit_gameid: _Optional[str] = ...) -> None: ...

class CMsgShortcutAppIds(_message.Message):
    __slots__ = ("appids",)
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgMonitorInfo(_message.Message):
    __slots__ = ("selected_display_name", "monitors")
    class MonitorInfo(_message.Message):
        __slots__ = ("monitor_device_name", "monitor_display_name")
        MONITOR_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        MONITOR_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        monitor_device_name: str
        monitor_display_name: str
        def __init__(self, monitor_device_name: _Optional[str] = ..., monitor_display_name: _Optional[str] = ...) -> None: ...
    SELECTED_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    MONITORS_FIELD_NUMBER: _ClassVar[int]
    selected_display_name: str
    monitors: _containers.RepeatedCompositeFieldContainer[CMsgMonitorInfo.MonitorInfo]
    def __init__(self, selected_display_name: _Optional[str] = ..., monitors: _Optional[_Iterable[_Union[CMsgMonitorInfo.MonitorInfo, _Mapping]]] = ...) -> None: ...

class CMsgGenerateSystemReportReply(_message.Message):
    __slots__ = ("report_id",)
    REPORT_ID_FIELD_NUMBER: _ClassVar[int]
    report_id: str
    def __init__(self, report_id: _Optional[str] = ...) -> None: ...

class CMsgWebUITransportInfo(_message.Message):
    __slots__ = ("port", "auth_key")
    PORT_FIELD_NUMBER: _ClassVar[int]
    AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
    port: int
    auth_key: str
    def __init__(self, port: _Optional[int] = ..., auth_key: _Optional[str] = ...) -> None: ...

class CMsgWebUITransportFailure(_message.Message):
    __slots__ = ("connect_count",)
    CONNECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    connect_count: int
    def __init__(self, connect_count: _Optional[int] = ...) -> None: ...

class CMsgClientShaderHitCacheEntry(_message.Message):
    __slots__ = ("key_sha", "code_sha", "time_last_reported")
    KEY_SHA_FIELD_NUMBER: _ClassVar[int]
    CODE_SHA_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_REPORTED_FIELD_NUMBER: _ClassVar[int]
    key_sha: bytes
    code_sha: bytes
    time_last_reported: int
    def __init__(self, key_sha: _Optional[bytes] = ..., code_sha: _Optional[bytes] = ..., time_last_reported: _Optional[int] = ...) -> None: ...

class CMsgClientShaderHitCache(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CMsgClientShaderHitCacheEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CMsgClientShaderHitCacheEntry, _Mapping]]] = ...) -> None: ...
