import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import steammessages_parental_objects_pb2 as _steammessages_parental_objects_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CParental_EnableParentalSettings_Request(_message.Message):
    __slots__ = ("password", "settings", "sessionid", "enablecode", "steamid")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    ENABLECODE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    password: str
    settings: _steammessages_parental_objects_pb2.ParentalSettings
    sessionid: str
    enablecode: int
    steamid: int
    def __init__(self, password: _Optional[str] = ..., settings: _Optional[_Union[_steammessages_parental_objects_pb2.ParentalSettings, _Mapping]] = ..., sessionid: _Optional[str] = ..., enablecode: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_EnableParentalSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_DisableParentalSettings_Request(_message.Message):
    __slots__ = ("password", "steamid")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    password: str
    steamid: int
    def __init__(self, password: _Optional[str] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_DisableParentalSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_GetParentalSettings_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CParental_GetParentalSettings_Response(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _steammessages_parental_objects_pb2.ParentalSettings
    def __init__(self, settings: _Optional[_Union[_steammessages_parental_objects_pb2.ParentalSettings, _Mapping]] = ...) -> None: ...

class CParental_GetSignedParentalSettings_Request(_message.Message):
    __slots__ = ("priority",)
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    priority: int
    def __init__(self, priority: _Optional[int] = ...) -> None: ...

class CParental_GetSignedParentalSettings_Response(_message.Message):
    __slots__ = ("serialized_settings", "signature")
    SERIALIZED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    serialized_settings: bytes
    signature: bytes
    def __init__(self, serialized_settings: _Optional[bytes] = ..., signature: _Optional[bytes] = ...) -> None: ...

class CParental_SetParentalSettings_Request(_message.Message):
    __slots__ = ("password", "settings", "new_password", "sessionid", "steamid")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    password: str
    settings: _steammessages_parental_objects_pb2.ParentalSettings
    new_password: str
    sessionid: str
    steamid: int
    def __init__(self, password: _Optional[str] = ..., settings: _Optional[_Union[_steammessages_parental_objects_pb2.ParentalSettings, _Mapping]] = ..., new_password: _Optional[str] = ..., sessionid: _Optional[str] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_SetParentalSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_ValidateToken_Request(_message.Message):
    __slots__ = ("unlock_token",)
    UNLOCK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    unlock_token: str
    def __init__(self, unlock_token: _Optional[str] = ...) -> None: ...

class CParental_ValidateToken_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_ValidatePassword_Request(_message.Message):
    __slots__ = ("password", "session", "send_unlock_on_success")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    SEND_UNLOCK_ON_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    password: str
    session: str
    send_unlock_on_success: bool
    def __init__(self, password: _Optional[str] = ..., session: _Optional[str] = ..., send_unlock_on_success: bool = ...) -> None: ...

class CParental_ValidatePassword_Response(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class CParental_LockClient_Request(_message.Message):
    __slots__ = ("session",)
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: str
    def __init__(self, session: _Optional[str] = ...) -> None: ...

class CParental_LockClient_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_RequestRecoveryCode_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_RequestRecoveryCode_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_DisableWithRecoveryCode_Request(_message.Message):
    __slots__ = ("recovery_code", "steamid")
    RECOVERY_CODE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    recovery_code: int
    steamid: int
    def __init__(self, recovery_code: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_DisableWithRecoveryCode_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_RequestFeatureAccess_Request(_message.Message):
    __slots__ = ("features", "steamid")
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    features: int
    steamid: int
    def __init__(self, features: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_RequestFeatureAccess_Response(_message.Message):
    __slots__ = ("requestid",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestid: int
    def __init__(self, requestid: _Optional[int] = ...) -> None: ...

class CParental_ApproveFeatureAccess_Request(_message.Message):
    __slots__ = ("approve", "requestid", "features", "duration", "steamid")
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    approve: bool
    requestid: int
    features: int
    duration: int
    steamid: int
    def __init__(self, approve: bool = ..., requestid: _Optional[int] = ..., features: _Optional[int] = ..., duration: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_ApproveFeatureAccess_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_RequestPlaytime_Request(_message.Message):
    __slots__ = ("time_expires", "current_playtime_restrictions", "steamid")
    TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PLAYTIME_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    time_expires: int
    current_playtime_restrictions: _steammessages_parental_objects_pb2.ParentalPlaytimeDay
    steamid: int
    def __init__(self, time_expires: _Optional[int] = ..., current_playtime_restrictions: _Optional[_Union[_steammessages_parental_objects_pb2.ParentalPlaytimeDay, _Mapping]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_RequestPlaytime_Response(_message.Message):
    __slots__ = ("requestid",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestid: int
    def __init__(self, requestid: _Optional[int] = ...) -> None: ...

class CParental_ApprovePlaytime_Request(_message.Message):
    __slots__ = ("approve", "requestid", "restrictions_approved", "steamid")
    APPROVE_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    RESTRICTIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    approve: bool
    requestid: int
    restrictions_approved: _steammessages_parental_objects_pb2.ParentalTemporaryPlaytimeRestrictions
    steamid: int
    def __init__(self, approve: bool = ..., requestid: _Optional[int] = ..., restrictions_approved: _Optional[_Union[_steammessages_parental_objects_pb2.ParentalTemporaryPlaytimeRestrictions, _Mapping]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_ApprovePlaytime_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_GetRequests_Request(_message.Message):
    __slots__ = ("rt_include_completed_since", "family_groupid")
    RT_INCLUDE_COMPLETED_SINCE_FIELD_NUMBER: _ClassVar[int]
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    rt_include_completed_since: int
    family_groupid: int
    def __init__(self, rt_include_completed_since: _Optional[int] = ..., family_groupid: _Optional[int] = ...) -> None: ...

class CParental_GetRequests_Response(_message.Message):
    __slots__ = ("feature_requests", "playtime_requests")
    FEATURE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    feature_requests: _containers.RepeatedCompositeFieldContainer[_steammessages_parental_objects_pb2.ParentalFeatureRequest]
    playtime_requests: _containers.RepeatedCompositeFieldContainer[_steammessages_parental_objects_pb2.ParentalPlaytimeRequest]
    def __init__(self, feature_requests: _Optional[_Iterable[_Union[_steammessages_parental_objects_pb2.ParentalFeatureRequest, _Mapping]]] = ..., playtime_requests: _Optional[_Iterable[_Union[_steammessages_parental_objects_pb2.ParentalPlaytimeRequest, _Mapping]]] = ...) -> None: ...

class CParental_ReportPlaytimeAndNotify_Request(_message.Message):
    __slots__ = ("day_of_week", "minutes_used", "steamid")
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    MINUTES_USED_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    day_of_week: int
    minutes_used: int
    steamid: int
    def __init__(self, day_of_week: _Optional[int] = ..., minutes_used: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CParental_ReportPlaytimeAndNotify_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CParental_ParentalSettingsChange_Notification(_message.Message):
    __slots__ = ("serialized_settings", "signature", "password", "sessionid")
    SERIALIZED_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    serialized_settings: bytes
    signature: bytes
    password: str
    sessionid: str
    def __init__(self, serialized_settings: _Optional[bytes] = ..., signature: _Optional[bytes] = ..., password: _Optional[str] = ..., sessionid: _Optional[str] = ...) -> None: ...

class CParental_ParentalUnlock_Notification(_message.Message):
    __slots__ = ("password", "sessionid")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    password: str
    sessionid: str
    def __init__(self, password: _Optional[str] = ..., sessionid: _Optional[str] = ...) -> None: ...

class CParental_ParentalLock_Notification(_message.Message):
    __slots__ = ("sessionid",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionid: str
    def __init__(self, sessionid: _Optional[str] = ...) -> None: ...

class CParental_PlaytimeUsed_Notification(_message.Message):
    __slots__ = ("day_of_week", "minutes_used")
    DAY_OF_WEEK_FIELD_NUMBER: _ClassVar[int]
    MINUTES_USED_FIELD_NUMBER: _ClassVar[int]
    day_of_week: int
    minutes_used: int
    def __init__(self, day_of_week: _Optional[int] = ..., minutes_used: _Optional[int] = ...) -> None: ...

class Parental(_service.service): ...

class Parental_Stub(Parental): ...

class ParentalClient(_service.service): ...

class ParentalClient_Stub(ParentalClient): ...
