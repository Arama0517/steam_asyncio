from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CClientMetrics_ClientBootstrap_RequestInfo(_message.Message):
    __slots__ = ("original_hostname", "actual_hostname", "path", "base_name", "success", "status_code", "address_of_request_url", "response_time_ms", "bytes_received", "num_retries")
    ORIGINAL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    BASE_NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_OF_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BYTES_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: _ClassVar[int]
    original_hostname: str
    actual_hostname: str
    path: str
    base_name: str
    success: bool
    status_code: int
    address_of_request_url: str
    response_time_ms: int
    bytes_received: int
    num_retries: int
    def __init__(self, original_hostname: _Optional[str] = ..., actual_hostname: _Optional[str] = ..., path: _Optional[str] = ..., base_name: _Optional[str] = ..., success: bool = ..., status_code: _Optional[int] = ..., address_of_request_url: _Optional[str] = ..., response_time_ms: _Optional[int] = ..., bytes_received: _Optional[int] = ..., num_retries: _Optional[int] = ...) -> None: ...

class CClientMetrics_ClientBootstrap_Summary(_message.Message):
    __slots__ = ("launcher_type", "steam_realm", "beta_name", "download_completed", "total_time_ms", "manifest_requests", "package_requests")
    LAUNCHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    STEAM_REALM_FIELD_NUMBER: _ClassVar[int]
    BETA_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    launcher_type: int
    steam_realm: int
    beta_name: str
    download_completed: bool
    total_time_ms: int
    manifest_requests: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ClientBootstrap_RequestInfo]
    package_requests: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ClientBootstrap_RequestInfo]
    def __init__(self, launcher_type: _Optional[int] = ..., steam_realm: _Optional[int] = ..., beta_name: _Optional[str] = ..., download_completed: bool = ..., total_time_ms: _Optional[int] = ..., manifest_requests: _Optional[_Iterable[_Union[CClientMetrics_ClientBootstrap_RequestInfo, _Mapping]]] = ..., package_requests: _Optional[_Iterable[_Union[CClientMetrics_ClientBootstrap_RequestInfo, _Mapping]]] = ...) -> None: ...

class CClientMetrics_ContentDownloadResponse_Counts(_message.Message):
    __slots__ = ("class_100", "class_200", "class_300", "class_400", "class_500", "no_response", "class_unknown")
    CLASS_100_FIELD_NUMBER: _ClassVar[int]
    CLASS_200_FIELD_NUMBER: _ClassVar[int]
    CLASS_300_FIELD_NUMBER: _ClassVar[int]
    CLASS_400_FIELD_NUMBER: _ClassVar[int]
    CLASS_500_FIELD_NUMBER: _ClassVar[int]
    NO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CLASS_UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    class_100: int
    class_200: int
    class_300: int
    class_400: int
    class_500: int
    no_response: int
    class_unknown: int
    def __init__(self, class_100: _Optional[int] = ..., class_200: _Optional[int] = ..., class_300: _Optional[int] = ..., class_400: _Optional[int] = ..., class_500: _Optional[int] = ..., no_response: _Optional[int] = ..., class_unknown: _Optional[int] = ...) -> None: ...

class CClientMetrics_ContentDownloadResponse_HostCounts(_message.Message):
    __slots__ = ("hostname", "source_type", "counts")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    source_type: int
    counts: CClientMetrics_ContentDownloadResponse_Counts
    def __init__(self, hostname: _Optional[str] = ..., source_type: _Optional[int] = ..., counts: _Optional[_Union[CClientMetrics_ContentDownloadResponse_Counts, _Mapping]] = ...) -> None: ...

class CClientMetrics_ContentDownloadResponse_Hosts(_message.Message):
    __slots__ = ("hosts",)
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    hosts: _containers.RepeatedCompositeFieldContainer[CClientMetrics_ContentDownloadResponse_HostCounts]
    def __init__(self, hosts: _Optional[_Iterable[_Union[CClientMetrics_ContentDownloadResponse_HostCounts, _Mapping]]] = ...) -> None: ...
