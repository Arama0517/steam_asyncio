import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CPartnerApps_RequestUploadToken_Request(_message.Message):
    __slots__ = ("filename", "appid")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    appid: int
    def __init__(self, filename: _Optional[str] = ..., appid: _Optional[int] = ...) -> None: ...

class CPartnerApps_RequestUploadToken_Response(_message.Message):
    __slots__ = ("upload_token", "location", "routing_id")
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ROUTING_ID_FIELD_NUMBER: _ClassVar[int]
    upload_token: int
    location: str
    routing_id: int
    def __init__(self, upload_token: _Optional[int] = ..., location: _Optional[str] = ..., routing_id: _Optional[int] = ...) -> None: ...

class CPartnerApps_FinishUpload_Request(_message.Message):
    __slots__ = ("upload_token", "routing_id", "app_id")
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROUTING_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    upload_token: int
    routing_id: int
    app_id: int
    def __init__(self, upload_token: _Optional[int] = ..., routing_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class CPartnerApps_FinishUploadKVSign_Response(_message.Message):
    __slots__ = ("signed_installscript",)
    SIGNED_INSTALLSCRIPT_FIELD_NUMBER: _ClassVar[int]
    signed_installscript: str
    def __init__(self, signed_installscript: _Optional[str] = ...) -> None: ...

class CPartnerApps_FinishUploadLegacyDRM_Request(_message.Message):
    __slots__ = ("upload_token", "routing_id", "app_id", "flags", "tool_name", "use_cloud")
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROUTING_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    upload_token: int
    routing_id: int
    app_id: int
    flags: int
    tool_name: str
    use_cloud: bool
    def __init__(self, upload_token: _Optional[int] = ..., routing_id: _Optional[int] = ..., app_id: _Optional[int] = ..., flags: _Optional[int] = ..., tool_name: _Optional[str] = ..., use_cloud: bool = ...) -> None: ...

class CPartnerApps_FinishUploadLegacyDRM_Response(_message.Message):
    __slots__ = ("file_id",)
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class CPartnerApps_FinishUpload_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPartnerApps_FinishUploadDepot_Request(_message.Message):
    __slots__ = ("upload_token", "routing_id", "app_id", "depot_id", "build_flags")
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROUTING_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    BUILD_FLAGS_FIELD_NUMBER: _ClassVar[int]
    upload_token: int
    routing_id: int
    app_id: int
    depot_id: int
    build_flags: int
    def __init__(self, upload_token: _Optional[int] = ..., routing_id: _Optional[int] = ..., app_id: _Optional[int] = ..., depot_id: _Optional[int] = ..., build_flags: _Optional[int] = ...) -> None: ...

class CPartnerApps_FinishUploadDepot_Response(_message.Message):
    __slots__ = ("build_routing_id",)
    BUILD_ROUTING_ID_FIELD_NUMBER: _ClassVar[int]
    build_routing_id: int
    def __init__(self, build_routing_id: _Optional[int] = ...) -> None: ...

class CPartnerApps_GetDepotBuildResult_Request(_message.Message):
    __slots__ = ("upload_token", "routing_id")
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ROUTING_ID_FIELD_NUMBER: _ClassVar[int]
    upload_token: int
    routing_id: int
    def __init__(self, upload_token: _Optional[int] = ..., routing_id: _Optional[int] = ...) -> None: ...

class CPartnerApps_GetDepotBuildResult_Response(_message.Message):
    __slots__ = ("manifest_id", "error_msg")
    MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_MSG_FIELD_NUMBER: _ClassVar[int]
    manifest_id: int
    error_msg: str
    def __init__(self, manifest_id: _Optional[int] = ..., error_msg: _Optional[str] = ...) -> None: ...

class CPartnerApps_FindDRMUploads_Request(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    def __init__(self, app_id: _Optional[int] = ...) -> None: ...

class CPartnerApps_ExistingDRMUpload(_message.Message):
    __slots__ = ("file_id", "app_id", "actor_id", "supplied_name", "flags", "mod_type", "timestamp", "orig_file_id")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPLIED_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    MOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORIG_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    app_id: int
    actor_id: int
    supplied_name: str
    flags: int
    mod_type: str
    timestamp: int
    orig_file_id: str
    def __init__(self, file_id: _Optional[str] = ..., app_id: _Optional[int] = ..., actor_id: _Optional[int] = ..., supplied_name: _Optional[str] = ..., flags: _Optional[int] = ..., mod_type: _Optional[str] = ..., timestamp: _Optional[int] = ..., orig_file_id: _Optional[str] = ...) -> None: ...

class CPartnerApps_FindDRMUploads_Response(_message.Message):
    __slots__ = ("uploads",)
    UPLOADS_FIELD_NUMBER: _ClassVar[int]
    uploads: _containers.RepeatedCompositeFieldContainer[CPartnerApps_ExistingDRMUpload]
    def __init__(self, uploads: _Optional[_Iterable[_Union[CPartnerApps_ExistingDRMUpload, _Mapping]]] = ...) -> None: ...

class CPartnerApps_Download_Request(_message.Message):
    __slots__ = ("file_id", "app_id")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    app_id: int
    def __init__(self, file_id: _Optional[str] = ..., app_id: _Optional[int] = ...) -> None: ...

class CPartnerApps_Download_Response(_message.Message):
    __slots__ = ("download_url", "app_id")
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    download_url: str
    app_id: int
    def __init__(self, download_url: _Optional[str] = ..., app_id: _Optional[int] = ...) -> None: ...

class PartnerApps(_service.service): ...

class PartnerApps_Stub(PartnerApps): ...
