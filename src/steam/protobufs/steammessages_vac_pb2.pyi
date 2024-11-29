import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CFileVerification_SignatureCheck_Request(_message.Message):
    __slots__ = ("steamid", "appid", "file_size", "file_timestamp", "file_timestamp2", "signature_result", "filename", "client_package_version", "sha1hash")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FILE_TIMESTAMP2_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_RESULT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    SHA1HASH_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    file_size: int
    file_timestamp: int
    file_timestamp2: int
    signature_result: int
    filename: str
    client_package_version: int
    sha1hash: bytes
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ..., file_size: _Optional[int] = ..., file_timestamp: _Optional[int] = ..., file_timestamp2: _Optional[int] = ..., signature_result: _Optional[int] = ..., filename: _Optional[str] = ..., client_package_version: _Optional[int] = ..., sha1hash: _Optional[bytes] = ...) -> None: ...

class CFileVerification_SignatureCheck_Response(_message.Message):
    __slots__ = ("deny_operation",)
    DENY_OPERATION_FIELD_NUMBER: _ClassVar[int]
    deny_operation: bool
    def __init__(self, deny_operation: bool = ...) -> None: ...

class CFileVerification_SteamServiceCheck_Request(_message.Message):
    __slots__ = ("service_status", "client_package_version", "launcher_type", "os_type", "service_repair")
    SERVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_REPAIR_FIELD_NUMBER: _ClassVar[int]
    service_status: int
    client_package_version: int
    launcher_type: int
    os_type: int
    service_repair: int
    def __init__(self, service_status: _Optional[int] = ..., client_package_version: _Optional[int] = ..., launcher_type: _Optional[int] = ..., os_type: _Optional[int] = ..., service_repair: _Optional[int] = ...) -> None: ...

class CFileVerification_SteamServiceCheck_Response(_message.Message):
    __slots__ = ("attempt_repair",)
    ATTEMPT_REPAIR_FIELD_NUMBER: _ClassVar[int]
    attempt_repair: bool
    def __init__(self, attempt_repair: bool = ...) -> None: ...

class FileVerification(_service.service): ...

class FileVerification_Stub(FileVerification): ...
