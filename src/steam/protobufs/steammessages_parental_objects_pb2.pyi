import steammessages_base_pb2 as _steammessages_base_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParentalApp(_message.Message):
    __slots__ = ("appid", "is_allowed")
    APPID_FIELD_NUMBER: _ClassVar[int]
    IS_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    is_allowed: bool
    def __init__(self, appid: _Optional[int] = ..., is_allowed: bool = ...) -> None: ...

class ParentalPlaytimeDay(_message.Message):
    __slots__ = ("allowed_time_windows", "allowed_daily_minutes")
    ALLOWED_TIME_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DAILY_MINUTES_FIELD_NUMBER: _ClassVar[int]
    allowed_time_windows: int
    allowed_daily_minutes: int
    def __init__(self, allowed_time_windows: _Optional[int] = ..., allowed_daily_minutes: _Optional[int] = ...) -> None: ...

class ParentalPlaytimeRestrictions(_message.Message):
    __slots__ = ("apply_playtime_restrictions", "playtime_days")
    APPLY_PLAYTIME_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_DAYS_FIELD_NUMBER: _ClassVar[int]
    apply_playtime_restrictions: bool
    playtime_days: _containers.RepeatedCompositeFieldContainer[ParentalPlaytimeDay]
    def __init__(self, apply_playtime_restrictions: bool = ..., playtime_days: _Optional[_Iterable[_Union[ParentalPlaytimeDay, _Mapping]]] = ...) -> None: ...

class ParentalTemporaryPlaytimeRestrictions(_message.Message):
    __slots__ = ("restrictions", "rtime_expires")
    RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    RTIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    restrictions: ParentalPlaytimeDay
    rtime_expires: int
    def __init__(self, restrictions: _Optional[_Union[ParentalPlaytimeDay, _Mapping]] = ..., rtime_expires: _Optional[int] = ...) -> None: ...

class ParentalSettings(_message.Message):
    __slots__ = ("steamid", "applist_base_id", "applist_base_description", "applist_base", "applist_custom", "passwordhashtype", "salt", "passwordhash", "is_enabled", "enabled_features", "recovery_email", "is_site_license_lock", "temporary_enabled_features", "rtime_temporary_feature_expiration", "playtime_restrictions", "temporary_playtime_restrictions", "excluded_store_content_descriptors", "excluded_community_content_descriptors", "utility_appids")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPLIST_BASE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLIST_BASE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPLIST_BASE_FIELD_NUMBER: _ClassVar[int]
    APPLIST_CUSTOM_FIELD_NUMBER: _ClassVar[int]
    PASSWORDHASHTYPE_FIELD_NUMBER: _ClassVar[int]
    SALT_FIELD_NUMBER: _ClassVar[int]
    PASSWORDHASH_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    IS_SITE_LICENSE_LOCK_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_ENABLED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    RTIME_TEMPORARY_FEATURE_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PLAYTIME_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_STORE_CONTENT_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_COMMUNITY_CONTENT_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    UTILITY_APPIDS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    applist_base_id: int
    applist_base_description: str
    applist_base: _containers.RepeatedCompositeFieldContainer[ParentalApp]
    applist_custom: _containers.RepeatedCompositeFieldContainer[ParentalApp]
    passwordhashtype: int
    salt: bytes
    passwordhash: bytes
    is_enabled: bool
    enabled_features: int
    recovery_email: str
    is_site_license_lock: bool
    temporary_enabled_features: int
    rtime_temporary_feature_expiration: int
    playtime_restrictions: ParentalPlaytimeRestrictions
    temporary_playtime_restrictions: ParentalTemporaryPlaytimeRestrictions
    excluded_store_content_descriptors: _containers.RepeatedScalarFieldContainer[int]
    excluded_community_content_descriptors: _containers.RepeatedScalarFieldContainer[int]
    utility_appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid: _Optional[int] = ..., applist_base_id: _Optional[int] = ..., applist_base_description: _Optional[str] = ..., applist_base: _Optional[_Iterable[_Union[ParentalApp, _Mapping]]] = ..., applist_custom: _Optional[_Iterable[_Union[ParentalApp, _Mapping]]] = ..., passwordhashtype: _Optional[int] = ..., salt: _Optional[bytes] = ..., passwordhash: _Optional[bytes] = ..., is_enabled: bool = ..., enabled_features: _Optional[int] = ..., recovery_email: _Optional[str] = ..., is_site_license_lock: bool = ..., temporary_enabled_features: _Optional[int] = ..., rtime_temporary_feature_expiration: _Optional[int] = ..., playtime_restrictions: _Optional[_Union[ParentalPlaytimeRestrictions, _Mapping]] = ..., temporary_playtime_restrictions: _Optional[_Union[ParentalTemporaryPlaytimeRestrictions, _Mapping]] = ..., excluded_store_content_descriptors: _Optional[_Iterable[int]] = ..., excluded_community_content_descriptors: _Optional[_Iterable[int]] = ..., utility_appids: _Optional[_Iterable[int]] = ...) -> None: ...

class ParentalFeatureRequest(_message.Message):
    __slots__ = ("requestid", "family_groupid", "steamid", "features", "time_requested", "approved", "steamid_responder", "time_responded")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    TIME_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    STEAMID_RESPONDER_FIELD_NUMBER: _ClassVar[int]
    TIME_RESPONDED_FIELD_NUMBER: _ClassVar[int]
    requestid: int
    family_groupid: int
    steamid: int
    features: int
    time_requested: int
    approved: bool
    steamid_responder: int
    time_responded: int
    def __init__(self, requestid: _Optional[int] = ..., family_groupid: _Optional[int] = ..., steamid: _Optional[int] = ..., features: _Optional[int] = ..., time_requested: _Optional[int] = ..., approved: bool = ..., steamid_responder: _Optional[int] = ..., time_responded: _Optional[int] = ...) -> None: ...

class ParentalPlaytimeRequest(_message.Message):
    __slots__ = ("requestid", "family_groupid", "steamid", "current_playtime_restrictions", "time_expires", "time_requested", "approved", "steamid_responder", "time_responded", "restrictions_approved")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PLAYTIME_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    TIME_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    STEAMID_RESPONDER_FIELD_NUMBER: _ClassVar[int]
    TIME_RESPONDED_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    requestid: int
    family_groupid: int
    steamid: int
    current_playtime_restrictions: ParentalPlaytimeDay
    time_expires: int
    time_requested: int
    approved: bool
    steamid_responder: int
    time_responded: int
    restrictions_approved: ParentalTemporaryPlaytimeRestrictions
    def __init__(self, requestid: _Optional[int] = ..., family_groupid: _Optional[int] = ..., steamid: _Optional[int] = ..., current_playtime_restrictions: _Optional[_Union[ParentalPlaytimeDay, _Mapping]] = ..., time_expires: _Optional[int] = ..., time_requested: _Optional[int] = ..., approved: bool = ..., steamid_responder: _Optional[int] = ..., time_responded: _Optional[int] = ..., restrictions_approved: _Optional[_Union[ParentalTemporaryPlaytimeRestrictions, _Mapping]] = ...) -> None: ...
