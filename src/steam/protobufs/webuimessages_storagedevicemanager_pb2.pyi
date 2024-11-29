import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CStorageDeviceManager_IsServiceAvailable_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_IsServiceAvailable_Response(_message.Message):
    __slots__ = ("is_available",)
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    is_available: bool
    def __init__(self, is_available: bool = ...) -> None: ...

class CStorageDeviceManagerDrive(_message.Message):
    __slots__ = ("id", "model", "vendor", "serial", "is_ejectable", "size_bytes", "media_type", "is_unformatted", "adopt_stage", "is_formattable", "is_media_available")
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    IS_EJECTABLE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_UNFORMATTED_FIELD_NUMBER: _ClassVar[int]
    ADOPT_STAGE_FIELD_NUMBER: _ClassVar[int]
    IS_FORMATTABLE_FIELD_NUMBER: _ClassVar[int]
    IS_MEDIA_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    id: int
    model: str
    vendor: str
    serial: str
    is_ejectable: bool
    size_bytes: int
    media_type: _enums_pb2.EStorageDriveMediaType
    is_unformatted: bool
    adopt_stage: _enums_pb2.EStorageFormatStage
    is_formattable: bool
    is_media_available: bool
    def __init__(self, id: _Optional[int] = ..., model: _Optional[str] = ..., vendor: _Optional[str] = ..., serial: _Optional[str] = ..., is_ejectable: bool = ..., size_bytes: _Optional[int] = ..., media_type: _Optional[_Union[_enums_pb2.EStorageDriveMediaType, str]] = ..., is_unformatted: bool = ..., adopt_stage: _Optional[_Union[_enums_pb2.EStorageFormatStage, str]] = ..., is_formattable: bool = ..., is_media_available: bool = ...) -> None: ...

class CStorageDeviceManagerBlockDevice(_message.Message):
    __slots__ = ("id", "drive_id", "path", "friendly_path", "label", "size_bytes", "is_formattable", "is_read_only", "is_root_device", "content_type", "filesystem_type", "mount_paths", "is_unmounting", "has_steam_library")
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
    MOUNT_PATHS_FIELD_NUMBER: _ClassVar[int]
    IS_UNMOUNTING_FIELD_NUMBER: _ClassVar[int]
    HAS_STEAM_LIBRARY_FIELD_NUMBER: _ClassVar[int]
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
    mount_paths: _containers.RepeatedScalarFieldContainer[str]
    is_unmounting: bool
    has_steam_library: bool
    def __init__(self, id: _Optional[int] = ..., drive_id: _Optional[int] = ..., path: _Optional[str] = ..., friendly_path: _Optional[str] = ..., label: _Optional[str] = ..., size_bytes: _Optional[int] = ..., is_formattable: bool = ..., is_read_only: bool = ..., is_root_device: bool = ..., content_type: _Optional[_Union[_enums_pb2.EStorageBlockContentType, str]] = ..., filesystem_type: _Optional[_Union[_enums_pb2.EStorageBlockFileSystemType, str]] = ..., mount_paths: _Optional[_Iterable[str]] = ..., is_unmounting: bool = ..., has_steam_library: bool = ...) -> None: ...

class CStorageDeviceManagerState(_message.Message):
    __slots__ = ("drives", "block_devices", "is_unmount_supported", "is_trim_supported", "is_trim_running", "is_adopt_supported")
    DRIVES_FIELD_NUMBER: _ClassVar[int]
    BLOCK_DEVICES_FIELD_NUMBER: _ClassVar[int]
    IS_UNMOUNT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_TRIM_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    IS_TRIM_RUNNING_FIELD_NUMBER: _ClassVar[int]
    IS_ADOPT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    drives: _containers.RepeatedCompositeFieldContainer[CStorageDeviceManagerDrive]
    block_devices: _containers.RepeatedCompositeFieldContainer[CStorageDeviceManagerBlockDevice]
    is_unmount_supported: bool
    is_trim_supported: bool
    is_trim_running: bool
    is_adopt_supported: bool
    def __init__(self, drives: _Optional[_Iterable[_Union[CStorageDeviceManagerDrive, _Mapping]]] = ..., block_devices: _Optional[_Iterable[_Union[CStorageDeviceManagerBlockDevice, _Mapping]]] = ..., is_unmount_supported: bool = ..., is_trim_supported: bool = ..., is_trim_running: bool = ..., is_adopt_supported: bool = ...) -> None: ...

class CStorageDeviceManager_GetState_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_GetState_Response(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: CStorageDeviceManagerState
    def __init__(self, state: _Optional[_Union[CStorageDeviceManagerState, _Mapping]] = ...) -> None: ...

class CStorageDeviceManager_StateChanged_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_Eject_Request(_message.Message):
    __slots__ = ("drive_id",)
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    drive_id: int
    def __init__(self, drive_id: _Optional[int] = ...) -> None: ...

class CStorageDeviceManager_Eject_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_Adopt_Request(_message.Message):
    __slots__ = ("drive_id", "label", "validate")
    DRIVE_ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_FIELD_NUMBER: _ClassVar[int]
    drive_id: int
    label: str
    validate: bool
    def __init__(self, drive_id: _Optional[int] = ..., label: _Optional[str] = ..., validate: bool = ...) -> None: ...

class CStorageDeviceManager_Adopt_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_Format_Request(_message.Message):
    __slots__ = ("block_device_id",)
    BLOCK_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    block_device_id: int
    def __init__(self, block_device_id: _Optional[int] = ...) -> None: ...

class CStorageDeviceManager_Format_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_Unmount_Request(_message.Message):
    __slots__ = ("block_device_id",)
    BLOCK_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    block_device_id: int
    def __init__(self, block_device_id: _Optional[int] = ...) -> None: ...

class CStorageDeviceManager_Unmount_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_TrimAll_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStorageDeviceManager_TrimAll_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageDeviceManager(_service.service): ...

class StorageDeviceManager_Stub(StorageDeviceManager): ...
