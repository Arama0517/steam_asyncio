import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientAppInfoUpdate(_message.Message):
    __slots__ = ("last_changenumber", "send_changelist")
    LAST_CHANGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SEND_CHANGELIST_FIELD_NUMBER: _ClassVar[int]
    last_changenumber: int
    send_changelist: bool
    def __init__(self, last_changenumber: _Optional[int] = ..., send_changelist: bool = ...) -> None: ...

class CMsgClientAppInfoChanges(_message.Message):
    __slots__ = ("current_change_number", "force_full_update", "appIDs")
    CURRENT_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    current_change_number: int
    force_full_update: bool
    appIDs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, current_change_number: _Optional[int] = ..., force_full_update: bool = ..., appIDs: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientAppInfoRequest(_message.Message):
    __slots__ = ("apps", "supports_batches")
    class App(_message.Message):
        __slots__ = ("app_id", "section_flags", "section_CRC")
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        SECTION_FLAGS_FIELD_NUMBER: _ClassVar[int]
        SECTION_CRC_FIELD_NUMBER: _ClassVar[int]
        app_id: int
        section_flags: int
        section_CRC: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, app_id: _Optional[int] = ..., section_flags: _Optional[int] = ..., section_CRC: _Optional[_Iterable[int]] = ...) -> None: ...
    APPS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_BATCHES_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[CMsgClientAppInfoRequest.App]
    supports_batches: bool
    def __init__(self, apps: _Optional[_Iterable[_Union[CMsgClientAppInfoRequest.App, _Mapping]]] = ..., supports_batches: bool = ...) -> None: ...

class CMsgClientPICSChangesSinceRequest(_message.Message):
    __slots__ = ("since_change_number", "send_app_info_changes", "send_package_info_changes", "num_app_info_cached", "num_package_info_cached")
    SINCE_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEND_APP_INFO_CHANGES_FIELD_NUMBER: _ClassVar[int]
    SEND_PACKAGE_INFO_CHANGES_FIELD_NUMBER: _ClassVar[int]
    NUM_APP_INFO_CACHED_FIELD_NUMBER: _ClassVar[int]
    NUM_PACKAGE_INFO_CACHED_FIELD_NUMBER: _ClassVar[int]
    since_change_number: int
    send_app_info_changes: bool
    send_package_info_changes: bool
    num_app_info_cached: int
    num_package_info_cached: int
    def __init__(self, since_change_number: _Optional[int] = ..., send_app_info_changes: bool = ..., send_package_info_changes: bool = ..., num_app_info_cached: _Optional[int] = ..., num_package_info_cached: _Optional[int] = ...) -> None: ...

class CMsgClientPICSChangesSinceResponse(_message.Message):
    __slots__ = ("current_change_number", "since_change_number", "force_full_update", "package_changes", "app_changes", "force_full_app_update", "force_full_package_update")
    class PackageChange(_message.Message):
        __slots__ = ("packageid", "change_number", "needs_token")
        PACKAGEID_FIELD_NUMBER: _ClassVar[int]
        CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NEEDS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        packageid: int
        change_number: int
        needs_token: bool
        def __init__(self, packageid: _Optional[int] = ..., change_number: _Optional[int] = ..., needs_token: bool = ...) -> None: ...
    class AppChange(_message.Message):
        __slots__ = ("appid", "change_number", "needs_token")
        APPID_FIELD_NUMBER: _ClassVar[int]
        CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NEEDS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        appid: int
        change_number: int
        needs_token: bool
        def __init__(self, appid: _Optional[int] = ..., change_number: _Optional[int] = ..., needs_token: bool = ...) -> None: ...
    CURRENT_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SINCE_CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    APP_CHANGES_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_APP_UPDATE_FIELD_NUMBER: _ClassVar[int]
    FORCE_FULL_PACKAGE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    current_change_number: int
    since_change_number: int
    force_full_update: bool
    package_changes: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSChangesSinceResponse.PackageChange]
    app_changes: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSChangesSinceResponse.AppChange]
    force_full_app_update: bool
    force_full_package_update: bool
    def __init__(self, current_change_number: _Optional[int] = ..., since_change_number: _Optional[int] = ..., force_full_update: bool = ..., package_changes: _Optional[_Iterable[_Union[CMsgClientPICSChangesSinceResponse.PackageChange, _Mapping]]] = ..., app_changes: _Optional[_Iterable[_Union[CMsgClientPICSChangesSinceResponse.AppChange, _Mapping]]] = ..., force_full_app_update: bool = ..., force_full_package_update: bool = ...) -> None: ...

class CMsgClientPICSProductInfoRequest(_message.Message):
    __slots__ = ("packages", "apps", "meta_data_only", "num_prev_failed", "OBSOLETE_supports_package_tokens", "sequence_number", "single_response")
    class AppInfo(_message.Message):
        __slots__ = ("appid", "access_token", "only_public_obsolete")
        APPID_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        ONLY_PUBLIC_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
        appid: int
        access_token: int
        only_public_obsolete: bool
        def __init__(self, appid: _Optional[int] = ..., access_token: _Optional[int] = ..., only_public_obsolete: bool = ...) -> None: ...
    class PackageInfo(_message.Message):
        __slots__ = ("packageid", "access_token")
        PACKAGEID_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        packageid: int
        access_token: int
        def __init__(self, packageid: _Optional[int] = ..., access_token: _Optional[int] = ...) -> None: ...
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    APPS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    NUM_PREV_FAILED_FIELD_NUMBER: _ClassVar[int]
    OBSOLETE_SUPPORTS_PACKAGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SINGLE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSProductInfoRequest.PackageInfo]
    apps: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSProductInfoRequest.AppInfo]
    meta_data_only: bool
    num_prev_failed: int
    OBSOLETE_supports_package_tokens: int
    sequence_number: int
    single_response: bool
    def __init__(self, packages: _Optional[_Iterable[_Union[CMsgClientPICSProductInfoRequest.PackageInfo, _Mapping]]] = ..., apps: _Optional[_Iterable[_Union[CMsgClientPICSProductInfoRequest.AppInfo, _Mapping]]] = ..., meta_data_only: bool = ..., num_prev_failed: _Optional[int] = ..., OBSOLETE_supports_package_tokens: _Optional[int] = ..., sequence_number: _Optional[int] = ..., single_response: bool = ...) -> None: ...

class CMsgClientPICSProductInfoResponse(_message.Message):
    __slots__ = ("apps", "unknown_appids", "packages", "unknown_packageids", "meta_data_only", "response_pending", "http_min_size", "http_host")
    class AppInfo(_message.Message):
        __slots__ = ("appid", "change_number", "missing_token", "sha", "buffer", "only_public", "size")
        APPID_FIELD_NUMBER: _ClassVar[int]
        CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        MISSING_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SHA_FIELD_NUMBER: _ClassVar[int]
        BUFFER_FIELD_NUMBER: _ClassVar[int]
        ONLY_PUBLIC_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        appid: int
        change_number: int
        missing_token: bool
        sha: bytes
        buffer: bytes
        only_public: bool
        size: int
        def __init__(self, appid: _Optional[int] = ..., change_number: _Optional[int] = ..., missing_token: bool = ..., sha: _Optional[bytes] = ..., buffer: _Optional[bytes] = ..., only_public: bool = ..., size: _Optional[int] = ...) -> None: ...
    class PackageInfo(_message.Message):
        __slots__ = ("packageid", "change_number", "missing_token", "sha", "buffer", "size")
        PACKAGEID_FIELD_NUMBER: _ClassVar[int]
        CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        MISSING_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SHA_FIELD_NUMBER: _ClassVar[int]
        BUFFER_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        packageid: int
        change_number: int
        missing_token: bool
        sha: bytes
        buffer: bytes
        size: int
        def __init__(self, packageid: _Optional[int] = ..., change_number: _Optional[int] = ..., missing_token: bool = ..., sha: _Optional[bytes] = ..., buffer: _Optional[bytes] = ..., size: _Optional[int] = ...) -> None: ...
    APPS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_APPIDS_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_PACKAGEIDS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_PENDING_FIELD_NUMBER: _ClassVar[int]
    HTTP_MIN_SIZE_FIELD_NUMBER: _ClassVar[int]
    HTTP_HOST_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSProductInfoResponse.AppInfo]
    unknown_appids: _containers.RepeatedScalarFieldContainer[int]
    packages: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSProductInfoResponse.PackageInfo]
    unknown_packageids: _containers.RepeatedScalarFieldContainer[int]
    meta_data_only: bool
    response_pending: bool
    http_min_size: int
    http_host: str
    def __init__(self, apps: _Optional[_Iterable[_Union[CMsgClientPICSProductInfoResponse.AppInfo, _Mapping]]] = ..., unknown_appids: _Optional[_Iterable[int]] = ..., packages: _Optional[_Iterable[_Union[CMsgClientPICSProductInfoResponse.PackageInfo, _Mapping]]] = ..., unknown_packageids: _Optional[_Iterable[int]] = ..., meta_data_only: bool = ..., response_pending: bool = ..., http_min_size: _Optional[int] = ..., http_host: _Optional[str] = ...) -> None: ...

class CMsgClientPICSAccessTokenRequest(_message.Message):
    __slots__ = ("packageids", "appids")
    PACKAGEIDS_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    packageids: _containers.RepeatedScalarFieldContainer[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, packageids: _Optional[_Iterable[int]] = ..., appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientPICSAccessTokenResponse(_message.Message):
    __slots__ = ("package_access_tokens", "package_denied_tokens", "app_access_tokens", "app_denied_tokens")
    class PackageToken(_message.Message):
        __slots__ = ("packageid", "access_token")
        PACKAGEID_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        packageid: int
        access_token: int
        def __init__(self, packageid: _Optional[int] = ..., access_token: _Optional[int] = ...) -> None: ...
    class AppToken(_message.Message):
        __slots__ = ("appid", "access_token")
        APPID_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        appid: int
        access_token: int
        def __init__(self, appid: _Optional[int] = ..., access_token: _Optional[int] = ...) -> None: ...
    PACKAGE_ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_DENIED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    APP_ACCESS_TOKENS_FIELD_NUMBER: _ClassVar[int]
    APP_DENIED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    package_access_tokens: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSAccessTokenResponse.PackageToken]
    package_denied_tokens: _containers.RepeatedScalarFieldContainer[int]
    app_access_tokens: _containers.RepeatedCompositeFieldContainer[CMsgClientPICSAccessTokenResponse.AppToken]
    app_denied_tokens: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, package_access_tokens: _Optional[_Iterable[_Union[CMsgClientPICSAccessTokenResponse.PackageToken, _Mapping]]] = ..., package_denied_tokens: _Optional[_Iterable[int]] = ..., app_access_tokens: _Optional[_Iterable[_Union[CMsgClientPICSAccessTokenResponse.AppToken, _Mapping]]] = ..., app_denied_tokens: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientPICSPrivateBetaRequest(_message.Message):
    __slots__ = ("appid", "access_token", "beta_name", "password_hash")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BETA_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    appid: int
    access_token: int
    beta_name: str
    password_hash: bytes
    def __init__(self, appid: _Optional[int] = ..., access_token: _Optional[int] = ..., beta_name: _Optional[str] = ..., password_hash: _Optional[bytes] = ...) -> None: ...

class CMsgClientPICSPrivateBetaResponse(_message.Message):
    __slots__ = ("eresult", "depot_section")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    DEPOT_SECTION_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    depot_section: bytes
    def __init__(self, eresult: _Optional[int] = ..., depot_section: _Optional[bytes] = ...) -> None: ...
