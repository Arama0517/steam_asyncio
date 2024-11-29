import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import enums_pb2 as _enums_pb2
import steammessages_client_objects_pb2 as _steammessages_client_objects_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CCloud_ClientLogUploadCheck_Notification(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    def __init__(self, client_id: _Optional[int] = ...) -> None: ...

class CCloud_ClientLogUploadComplete_Notification(_message.Message):
    __slots__ = ("client_id", "request_id")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    request_id: int
    def __init__(self, client_id: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...

class CCloud_GetUploadServerInfo_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CCloud_GetUploadServerInfo_Response(_message.Message):
    __slots__ = ("server_url",)
    SERVER_URL_FIELD_NUMBER: _ClassVar[int]
    server_url: str
    def __init__(self, server_url: _Optional[str] = ...) -> None: ...

class CCloud_BeginHTTPUpload_Request(_message.Message):
    __slots__ = ("appid", "file_size", "filename", "file_sha", "is_public", "platforms_to_sync", "request_headers_names", "request_headers_values", "upload_batch_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_TO_SYNC_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_NAMES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_VALUES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    file_size: int
    filename: str
    file_sha: str
    is_public: bool
    platforms_to_sync: _containers.RepeatedScalarFieldContainer[str]
    request_headers_names: _containers.RepeatedScalarFieldContainer[str]
    request_headers_values: _containers.RepeatedScalarFieldContainer[str]
    upload_batch_id: int
    def __init__(self, appid: _Optional[int] = ..., file_size: _Optional[int] = ..., filename: _Optional[str] = ..., file_sha: _Optional[str] = ..., is_public: bool = ..., platforms_to_sync: _Optional[_Iterable[str]] = ..., request_headers_names: _Optional[_Iterable[str]] = ..., request_headers_values: _Optional[_Iterable[str]] = ..., upload_batch_id: _Optional[int] = ...) -> None: ...

class CCloud_BeginHTTPUpload_Response(_message.Message):
    __slots__ = ("ugcid", "timestamp", "url_host", "url_path", "use_https", "request_headers")
    class HTTPHeaders(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    UGCID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    URL_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ugcid: int
    timestamp: int
    url_host: str
    url_path: str
    use_https: bool
    request_headers: _containers.RepeatedCompositeFieldContainer[CCloud_BeginHTTPUpload_Response.HTTPHeaders]
    def __init__(self, ugcid: _Optional[int] = ..., timestamp: _Optional[int] = ..., url_host: _Optional[str] = ..., url_path: _Optional[str] = ..., use_https: bool = ..., request_headers: _Optional[_Iterable[_Union[CCloud_BeginHTTPUpload_Response.HTTPHeaders, _Mapping]]] = ...) -> None: ...

class CCloud_CommitHTTPUpload_Request(_message.Message):
    __slots__ = ("transfer_succeeded", "appid", "file_sha", "filename")
    TRANSFER_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    transfer_succeeded: bool
    appid: int
    file_sha: str
    filename: str
    def __init__(self, transfer_succeeded: bool = ..., appid: _Optional[int] = ..., file_sha: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class CCloud_CommitHTTPUpload_Response(_message.Message):
    __slots__ = ("file_committed",)
    FILE_COMMITTED_FIELD_NUMBER: _ClassVar[int]
    file_committed: bool
    def __init__(self, file_committed: bool = ...) -> None: ...

class CCloud_BeginUGCUpload_Request(_message.Message):
    __slots__ = ("appid", "file_size", "filename", "file_sha", "content_type")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    file_size: int
    filename: str
    file_sha: str
    content_type: str
    def __init__(self, appid: _Optional[int] = ..., file_size: _Optional[int] = ..., filename: _Optional[str] = ..., file_sha: _Optional[str] = ..., content_type: _Optional[str] = ...) -> None: ...

class CCloud_BeginUGCUpload_Response(_message.Message):
    __slots__ = ("storage_system", "ugcid", "timestamp", "url_host", "url_path", "use_https", "request_headers")
    class HTTPHeaders(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STORAGE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    UGCID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    URL_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    storage_system: _enums_pb2.EPublishedFileStorageSystem
    ugcid: int
    timestamp: int
    url_host: str
    url_path: str
    use_https: bool
    request_headers: _containers.RepeatedCompositeFieldContainer[CCloud_BeginUGCUpload_Response.HTTPHeaders]
    def __init__(self, storage_system: _Optional[_Union[_enums_pb2.EPublishedFileStorageSystem, str]] = ..., ugcid: _Optional[int] = ..., timestamp: _Optional[int] = ..., url_host: _Optional[str] = ..., url_path: _Optional[str] = ..., use_https: bool = ..., request_headers: _Optional[_Iterable[_Union[CCloud_BeginUGCUpload_Response.HTTPHeaders, _Mapping]]] = ...) -> None: ...

class CCloud_CommitUGCUpload_Request(_message.Message):
    __slots__ = ("transfer_succeeded", "appid", "ugcid")
    TRANSFER_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    UGCID_FIELD_NUMBER: _ClassVar[int]
    transfer_succeeded: bool
    appid: int
    ugcid: int
    def __init__(self, transfer_succeeded: bool = ..., appid: _Optional[int] = ..., ugcid: _Optional[int] = ...) -> None: ...

class CCloud_CommitUGCUpload_Response(_message.Message):
    __slots__ = ("file_committed",)
    FILE_COMMITTED_FIELD_NUMBER: _ClassVar[int]
    file_committed: bool
    def __init__(self, file_committed: bool = ...) -> None: ...

class CCloud_GetFileDetails_Request(_message.Message):
    __slots__ = ("ugcid", "appid")
    UGCID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    ugcid: int
    appid: int
    def __init__(self, ugcid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CCloud_UserFile(_message.Message):
    __slots__ = ("appid", "ugcid", "filename", "timestamp", "file_size", "url", "steamid_creator", "flags", "platforms_to_sync", "file_sha")
    APPID_FIELD_NUMBER: _ClassVar[int]
    UGCID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    STEAMID_CREATOR_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_TO_SYNC_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA_FIELD_NUMBER: _ClassVar[int]
    appid: int
    ugcid: int
    filename: str
    timestamp: int
    file_size: int
    url: str
    steamid_creator: int
    flags: int
    platforms_to_sync: _containers.RepeatedScalarFieldContainer[str]
    file_sha: str
    def __init__(self, appid: _Optional[int] = ..., ugcid: _Optional[int] = ..., filename: _Optional[str] = ..., timestamp: _Optional[int] = ..., file_size: _Optional[int] = ..., url: _Optional[str] = ..., steamid_creator: _Optional[int] = ..., flags: _Optional[int] = ..., platforms_to_sync: _Optional[_Iterable[str]] = ..., file_sha: _Optional[str] = ...) -> None: ...

class CCloud_GetFileDetails_Response(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: CCloud_UserFile
    def __init__(self, details: _Optional[_Union[CCloud_UserFile, _Mapping]] = ...) -> None: ...

class CCloud_EnumerateUserFiles_Request(_message.Message):
    __slots__ = ("appid", "extended_details", "count", "start_index")
    APPID_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    appid: int
    extended_details: bool
    count: int
    start_index: int
    def __init__(self, appid: _Optional[int] = ..., extended_details: bool = ..., count: _Optional[int] = ..., start_index: _Optional[int] = ...) -> None: ...

class CCloud_EnumerateUserFiles_Response(_message.Message):
    __slots__ = ("files", "total_files")
    FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[CCloud_UserFile]
    total_files: int
    def __init__(self, files: _Optional[_Iterable[_Union[CCloud_UserFile, _Mapping]]] = ..., total_files: _Optional[int] = ...) -> None: ...

class CCloud_Delete_Request(_message.Message):
    __slots__ = ("filename", "appid", "upload_batch_id")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    appid: int
    upload_batch_id: int
    def __init__(self, filename: _Optional[str] = ..., appid: _Optional[int] = ..., upload_batch_id: _Optional[int] = ...) -> None: ...

class CCloud_Delete_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_GetClientEncryptionKey_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_GetClientEncryptionKey_Response(_message.Message):
    __slots__ = ("key", "crc")
    KEY_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    crc: int
    def __init__(self, key: _Optional[bytes] = ..., crc: _Optional[int] = ...) -> None: ...

class CCloud_CDNReport_Notification(_message.Message):
    __slots__ = ("steamid", "url", "success", "http_status_code", "expected_bytes", "received_bytes", "duration")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    url: str
    success: bool
    http_status_code: int
    expected_bytes: int
    received_bytes: int
    duration: int
    def __init__(self, steamid: _Optional[int] = ..., url: _Optional[str] = ..., success: bool = ..., http_status_code: _Optional[int] = ..., expected_bytes: _Optional[int] = ..., received_bytes: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class CCloud_ExternalStorageTransferReport_Notification(_message.Message):
    __slots__ = ("host", "path", "is_upload", "success", "http_status_code", "bytes_expected", "bytes_actual", "duration_ms", "cellid", "proxied", "ipv6_local", "ipv6_remote", "time_to_connect_ms", "time_to_send_req_ms", "time_to_first_byte_ms", "time_to_last_byte_ms")
    HOST_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    IS_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    BYTES_EXPECTED_FIELD_NUMBER: _ClassVar[int]
    BYTES_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CELLID_FIELD_NUMBER: _ClassVar[int]
    PROXIED_FIELD_NUMBER: _ClassVar[int]
    IPV6_LOCAL_FIELD_NUMBER: _ClassVar[int]
    IPV6_REMOTE_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_CONNECT_MS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_SEND_REQ_MS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FIRST_BYTE_MS_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_LAST_BYTE_MS_FIELD_NUMBER: _ClassVar[int]
    host: str
    path: str
    is_upload: bool
    success: bool
    http_status_code: int
    bytes_expected: int
    bytes_actual: int
    duration_ms: int
    cellid: int
    proxied: bool
    ipv6_local: bool
    ipv6_remote: bool
    time_to_connect_ms: int
    time_to_send_req_ms: int
    time_to_first_byte_ms: int
    time_to_last_byte_ms: int
    def __init__(self, host: _Optional[str] = ..., path: _Optional[str] = ..., is_upload: bool = ..., success: bool = ..., http_status_code: _Optional[int] = ..., bytes_expected: _Optional[int] = ..., bytes_actual: _Optional[int] = ..., duration_ms: _Optional[int] = ..., cellid: _Optional[int] = ..., proxied: bool = ..., ipv6_local: bool = ..., ipv6_remote: bool = ..., time_to_connect_ms: _Optional[int] = ..., time_to_send_req_ms: _Optional[int] = ..., time_to_first_byte_ms: _Optional[int] = ..., time_to_last_byte_ms: _Optional[int] = ...) -> None: ...

class CCloud_BeginAppUploadBatch_Request(_message.Message):
    __slots__ = ("appid", "machine_name", "files_to_upload", "files_to_delete", "client_id", "app_build_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    FILES_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    APP_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    machine_name: str
    files_to_upload: _containers.RepeatedScalarFieldContainer[str]
    files_to_delete: _containers.RepeatedScalarFieldContainer[str]
    client_id: int
    app_build_id: int
    def __init__(self, appid: _Optional[int] = ..., machine_name: _Optional[str] = ..., files_to_upload: _Optional[_Iterable[str]] = ..., files_to_delete: _Optional[_Iterable[str]] = ..., client_id: _Optional[int] = ..., app_build_id: _Optional[int] = ...) -> None: ...

class CCloud_BeginAppUploadBatch_Response(_message.Message):
    __slots__ = ("batch_id", "app_change_number")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    APP_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    batch_id: int
    app_change_number: int
    def __init__(self, batch_id: _Optional[int] = ..., app_change_number: _Optional[int] = ...) -> None: ...

class CCloud_CompleteAppUploadBatch_Notification(_message.Message):
    __slots__ = ("appid", "batch_id", "batch_eresult")
    APPID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ERESULT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    batch_id: int
    batch_eresult: int
    def __init__(self, appid: _Optional[int] = ..., batch_id: _Optional[int] = ..., batch_eresult: _Optional[int] = ...) -> None: ...

class CCloud_CompleteAppUploadBatch_Request(_message.Message):
    __slots__ = ("appid", "batch_id", "batch_eresult")
    APPID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_ERESULT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    batch_id: int
    batch_eresult: int
    def __init__(self, appid: _Optional[int] = ..., batch_id: _Optional[int] = ..., batch_eresult: _Optional[int] = ...) -> None: ...

class CCloud_CompleteAppUploadBatch_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_ClientBeginFileUpload_Request(_message.Message):
    __slots__ = ("appid", "file_size", "raw_file_size", "file_sha", "time_stamp", "filename", "platforms_to_sync", "cell_id", "can_encrypt", "is_shared_file", "deprecated_realm", "upload_batch_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RAW_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_TO_SYNC_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_ENCRYPT_FIELD_NUMBER: _ClassVar[int]
    IS_SHARED_FILE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_REALM_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    file_size: int
    raw_file_size: int
    file_sha: bytes
    time_stamp: int
    filename: str
    platforms_to_sync: int
    cell_id: int
    can_encrypt: bool
    is_shared_file: bool
    deprecated_realm: int
    upload_batch_id: int
    def __init__(self, appid: _Optional[int] = ..., file_size: _Optional[int] = ..., raw_file_size: _Optional[int] = ..., file_sha: _Optional[bytes] = ..., time_stamp: _Optional[int] = ..., filename: _Optional[str] = ..., platforms_to_sync: _Optional[int] = ..., cell_id: _Optional[int] = ..., can_encrypt: bool = ..., is_shared_file: bool = ..., deprecated_realm: _Optional[int] = ..., upload_batch_id: _Optional[int] = ...) -> None: ...

class ClientCloudFileUploadBlockDetails(_message.Message):
    __slots__ = ("url_host", "url_path", "use_https", "http_method", "request_headers", "block_offset", "block_length", "explicit_body_data", "may_parallelize")
    class HTTPHeaders(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    URL_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
    HTTP_METHOD_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    BLOCK_LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_BODY_DATA_FIELD_NUMBER: _ClassVar[int]
    MAY_PARALLELIZE_FIELD_NUMBER: _ClassVar[int]
    url_host: str
    url_path: str
    use_https: bool
    http_method: int
    request_headers: _containers.RepeatedCompositeFieldContainer[ClientCloudFileUploadBlockDetails.HTTPHeaders]
    block_offset: int
    block_length: int
    explicit_body_data: bytes
    may_parallelize: bool
    def __init__(self, url_host: _Optional[str] = ..., url_path: _Optional[str] = ..., use_https: bool = ..., http_method: _Optional[int] = ..., request_headers: _Optional[_Iterable[_Union[ClientCloudFileUploadBlockDetails.HTTPHeaders, _Mapping]]] = ..., block_offset: _Optional[int] = ..., block_length: _Optional[int] = ..., explicit_body_data: _Optional[bytes] = ..., may_parallelize: bool = ...) -> None: ...

class CCloud_ClientBeginFileUpload_Response(_message.Message):
    __slots__ = ("encrypt_file", "block_requests")
    ENCRYPT_FILE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    encrypt_file: bool
    block_requests: _containers.RepeatedCompositeFieldContainer[ClientCloudFileUploadBlockDetails]
    def __init__(self, encrypt_file: bool = ..., block_requests: _Optional[_Iterable[_Union[ClientCloudFileUploadBlockDetails, _Mapping]]] = ...) -> None: ...

class CCloud_ClientCommitFileUpload_Request(_message.Message):
    __slots__ = ("transfer_succeeded", "appid", "file_sha", "filename")
    TRANSFER_SUCCEEDED_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SHA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    transfer_succeeded: bool
    appid: int
    file_sha: bytes
    filename: str
    def __init__(self, transfer_succeeded: bool = ..., appid: _Optional[int] = ..., file_sha: _Optional[bytes] = ..., filename: _Optional[str] = ...) -> None: ...

class CCloud_ClientCommitFileUpload_Response(_message.Message):
    __slots__ = ("file_committed",)
    FILE_COMMITTED_FIELD_NUMBER: _ClassVar[int]
    file_committed: bool
    def __init__(self, file_committed: bool = ...) -> None: ...

class CCloud_ClientFileDownload_Request(_message.Message):
    __slots__ = ("appid", "filename", "realm", "force_proxy")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    REALM_FIELD_NUMBER: _ClassVar[int]
    FORCE_PROXY_FIELD_NUMBER: _ClassVar[int]
    appid: int
    filename: str
    realm: int
    force_proxy: bool
    def __init__(self, appid: _Optional[int] = ..., filename: _Optional[str] = ..., realm: _Optional[int] = ..., force_proxy: bool = ...) -> None: ...

class CCloud_ClientFileDownload_Response(_message.Message):
    __slots__ = ("appid", "file_size", "raw_file_size", "sha_file", "time_stamp", "is_explicit_delete", "url_host", "url_path", "use_https", "request_headers", "encrypted")
    class HTTPHeaders(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RAW_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHA_FILE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    IS_EXPLICIT_DELETE_FIELD_NUMBER: _ClassVar[int]
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    URL_PATH_FIELD_NUMBER: _ClassVar[int]
    USE_HTTPS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    file_size: int
    raw_file_size: int
    sha_file: bytes
    time_stamp: int
    is_explicit_delete: bool
    url_host: str
    url_path: str
    use_https: bool
    request_headers: _containers.RepeatedCompositeFieldContainer[CCloud_ClientFileDownload_Response.HTTPHeaders]
    encrypted: bool
    def __init__(self, appid: _Optional[int] = ..., file_size: _Optional[int] = ..., raw_file_size: _Optional[int] = ..., sha_file: _Optional[bytes] = ..., time_stamp: _Optional[int] = ..., is_explicit_delete: bool = ..., url_host: _Optional[str] = ..., url_path: _Optional[str] = ..., use_https: bool = ..., request_headers: _Optional[_Iterable[_Union[CCloud_ClientFileDownload_Response.HTTPHeaders, _Mapping]]] = ..., encrypted: bool = ...) -> None: ...

class CCloud_ClientDeleteFile_Request(_message.Message):
    __slots__ = ("appid", "filename", "is_explicit_delete", "upload_batch_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    IS_EXPLICIT_DELETE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    filename: str
    is_explicit_delete: bool
    upload_batch_id: int
    def __init__(self, appid: _Optional[int] = ..., filename: _Optional[str] = ..., is_explicit_delete: bool = ..., upload_batch_id: _Optional[int] = ...) -> None: ...

class CCloud_ClientDeleteFile_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_ClientConflictResolution_Notification(_message.Message):
    __slots__ = ("appid", "chose_local_files")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CHOSE_LOCAL_FILES_FIELD_NUMBER: _ClassVar[int]
    appid: int
    chose_local_files: bool
    def __init__(self, appid: _Optional[int] = ..., chose_local_files: bool = ...) -> None: ...

class CCloud_EnumerateUserApps_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_EnumerateUserApps_Response(_message.Message):
    __slots__ = ("apps",)
    class Apps(_message.Message):
        __slots__ = ("appid", "totalcount", "totalsize")
        APPID_FIELD_NUMBER: _ClassVar[int]
        TOTALCOUNT_FIELD_NUMBER: _ClassVar[int]
        TOTALSIZE_FIELD_NUMBER: _ClassVar[int]
        appid: int
        totalcount: int
        totalsize: int
        def __init__(self, appid: _Optional[int] = ..., totalcount: _Optional[int] = ..., totalsize: _Optional[int] = ...) -> None: ...
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[CCloud_EnumerateUserApps_Response.Apps]
    def __init__(self, apps: _Optional[_Iterable[_Union[CCloud_EnumerateUserApps_Response.Apps, _Mapping]]] = ...) -> None: ...

class CCloud_GetAppFileChangelist_Request(_message.Message):
    __slots__ = ("appid", "synced_change_number")
    APPID_FIELD_NUMBER: _ClassVar[int]
    SYNCED_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    appid: int
    synced_change_number: int
    def __init__(self, appid: _Optional[int] = ..., synced_change_number: _Optional[int] = ...) -> None: ...

class CCloud_AppFileInfo(_message.Message):
    __slots__ = ("file_name", "sha_file", "time_stamp", "raw_file_size", "persist_state", "platforms_to_sync", "path_prefix_index", "machine_name_index")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHA_FILE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PERSIST_STATE_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_TO_SYNC_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIX_INDEX_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_INDEX_FIELD_NUMBER: _ClassVar[int]
    file_name: str
    sha_file: bytes
    time_stamp: int
    raw_file_size: int
    persist_state: _enums_pb2.ECloudStoragePersistState
    platforms_to_sync: int
    path_prefix_index: int
    machine_name_index: int
    def __init__(self, file_name: _Optional[str] = ..., sha_file: _Optional[bytes] = ..., time_stamp: _Optional[int] = ..., raw_file_size: _Optional[int] = ..., persist_state: _Optional[_Union[_enums_pb2.ECloudStoragePersistState, str]] = ..., platforms_to_sync: _Optional[int] = ..., path_prefix_index: _Optional[int] = ..., machine_name_index: _Optional[int] = ...) -> None: ...

class CCloud_GetAppFileChangelist_Response(_message.Message):
    __slots__ = ("current_change_number", "files", "is_only_delta", "path_prefixes", "machine_names", "app_buildid_hwm")
    CURRENT_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    IS_ONLY_DELTA_FIELD_NUMBER: _ClassVar[int]
    PATH_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAMES_FIELD_NUMBER: _ClassVar[int]
    APP_BUILDID_HWM_FIELD_NUMBER: _ClassVar[int]
    current_change_number: int
    files: _containers.RepeatedCompositeFieldContainer[CCloud_AppFileInfo]
    is_only_delta: bool
    path_prefixes: _containers.RepeatedScalarFieldContainer[str]
    machine_names: _containers.RepeatedScalarFieldContainer[str]
    app_buildid_hwm: int
    def __init__(self, current_change_number: _Optional[int] = ..., files: _Optional[_Iterable[_Union[CCloud_AppFileInfo, _Mapping]]] = ..., is_only_delta: bool = ..., path_prefixes: _Optional[_Iterable[str]] = ..., machine_names: _Optional[_Iterable[str]] = ..., app_buildid_hwm: _Optional[int] = ...) -> None: ...

class CCloud_AppSessionSuspend_Request(_message.Message):
    __slots__ = ("appid", "client_id", "machine_name", "cloud_sync_completed")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_SYNC_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    client_id: int
    machine_name: str
    cloud_sync_completed: bool
    def __init__(self, appid: _Optional[int] = ..., client_id: _Optional[int] = ..., machine_name: _Optional[str] = ..., cloud_sync_completed: bool = ...) -> None: ...

class CCloud_AppSessionSuspend_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_AppSessionResume_Request(_message.Message):
    __slots__ = ("appid", "client_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    client_id: int
    def __init__(self, appid: _Optional[int] = ..., client_id: _Optional[int] = ...) -> None: ...

class CCloud_AppSessionResume_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloud_AppLaunchIntent_Request(_message.Message):
    __slots__ = ("appid", "client_id", "machine_name", "ignore_pending_operations", "os_type", "device_type")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    IGNORE_PENDING_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    client_id: int
    machine_name: str
    ignore_pending_operations: bool
    os_type: int
    device_type: int
    def __init__(self, appid: _Optional[int] = ..., client_id: _Optional[int] = ..., machine_name: _Optional[str] = ..., ignore_pending_operations: bool = ..., os_type: _Optional[int] = ..., device_type: _Optional[int] = ...) -> None: ...

class CCloud_AppLaunchIntent_Response(_message.Message):
    __slots__ = ("pending_remote_operations",)
    PENDING_REMOTE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    pending_remote_operations: _containers.RepeatedCompositeFieldContainer[_steammessages_client_objects_pb2.CCloud_PendingRemoteOperation]
    def __init__(self, pending_remote_operations: _Optional[_Iterable[_Union[_steammessages_client_objects_pb2.CCloud_PendingRemoteOperation, _Mapping]]] = ...) -> None: ...

class CCloud_AppExitSyncDone_Notification(_message.Message):
    __slots__ = ("appid", "client_id", "uploads_completed", "uploads_required")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOADS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    UPLOADS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    client_id: int
    uploads_completed: bool
    uploads_required: bool
    def __init__(self, appid: _Optional[int] = ..., client_id: _Optional[int] = ..., uploads_completed: bool = ..., uploads_required: bool = ...) -> None: ...

class CCloud_ClientGetAppQuotaUsage_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CCloud_ClientGetAppQuotaUsage_Response(_message.Message):
    __slots__ = ("existing_files", "existing_bytes", "max_num_files", "max_num_bytes")
    EXISTING_FILES_FIELD_NUMBER: _ClassVar[int]
    EXISTING_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_FILES_FIELD_NUMBER: _ClassVar[int]
    MAX_NUM_BYTES_FIELD_NUMBER: _ClassVar[int]
    existing_files: int
    existing_bytes: int
    max_num_files: int
    max_num_bytes: int
    def __init__(self, existing_files: _Optional[int] = ..., existing_bytes: _Optional[int] = ..., max_num_files: _Optional[int] = ..., max_num_bytes: _Optional[int] = ...) -> None: ...

class CCloud_AppCloudStateChange_Notification(_message.Message):
    __slots__ = ("appid", "app_change_number")
    APPID_FIELD_NUMBER: _ClassVar[int]
    APP_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    appid: int
    app_change_number: int
    def __init__(self, appid: _Optional[int] = ..., app_change_number: _Optional[int] = ...) -> None: ...

class CCloud_ClientLogUploadRequest_Notification(_message.Message):
    __slots__ = ("request_id",)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    def __init__(self, request_id: _Optional[int] = ...) -> None: ...

class Cloud(_service.service): ...

class Cloud_Stub(Cloud): ...

class CloudClient(_service.service): ...

class CloudClient_Stub(CloudClient): ...
