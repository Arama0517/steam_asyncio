import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EAuthTokenPlatformType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthTokenPlatformType_Unknown: _ClassVar[EAuthTokenPlatformType]
    k_EAuthTokenPlatformType_SteamClient: _ClassVar[EAuthTokenPlatformType]
    k_EAuthTokenPlatformType_WebBrowser: _ClassVar[EAuthTokenPlatformType]
    k_EAuthTokenPlatformType_MobileApp: _ClassVar[EAuthTokenPlatformType]

class EAuthTokenAppType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthTokenAppType_Unknown: _ClassVar[EAuthTokenAppType]
    k_EAuthTokenAppType_Mobile_SteamApp: _ClassVar[EAuthTokenAppType]
    k_EAuthTokenAppType_Mobile_ChatApp: _ClassVar[EAuthTokenAppType]

class EAuthSessionGuardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthSessionGuardType_Unknown: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_None: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_EmailCode: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_DeviceCode: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_DeviceConfirmation: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_EmailConfirmation: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_MachineToken: _ClassVar[EAuthSessionGuardType]
    k_EAuthSessionGuardType_LegacyMachineAuth: _ClassVar[EAuthSessionGuardType]

class EAuthSessionSecurityHistory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthSessionSecurityHistory_Invalid: _ClassVar[EAuthSessionSecurityHistory]
    k_EAuthSessionSecurityHistory_UsedPreviously: _ClassVar[EAuthSessionSecurityHistory]
    k_EAuthSessionSecurityHistory_NoPriorHistory: _ClassVar[EAuthSessionSecurityHistory]

class ETokenRenewalType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ETokenRenewalType_None: _ClassVar[ETokenRenewalType]
    k_ETokenRenewalType_Allow: _ClassVar[ETokenRenewalType]

class EAuthenticationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthenticationType_Unknown: _ClassVar[EAuthenticationType]
    k_EAuthenticationType_Password: _ClassVar[EAuthenticationType]
    k_EAuthenticationType_QR: _ClassVar[EAuthenticationType]
    k_EAuthenticationType_AccountCreation: _ClassVar[EAuthenticationType]
    k_EAuthenticationType_GuestAccount: _ClassVar[EAuthenticationType]

class EAuthTokenRevokeAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthTokenRevokeLogout: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokePermanent: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokeReplaced: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokeSupport: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokeConsume: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokeNonRememberedLogout: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokeNonRememberedPermanent: _ClassVar[EAuthTokenRevokeAction]
    k_EAuthTokenRevokeAutomatic: _ClassVar[EAuthTokenRevokeAction]

class EAuthTokenState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAuthTokenState_Invalid: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_New: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_Confirmed: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_Issued: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_Denied: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_LoggedOut: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_Consumed: _ClassVar[EAuthTokenState]
    k_EAuthTokenState_Revoked: _ClassVar[EAuthTokenState]
k_EAuthTokenPlatformType_Unknown: EAuthTokenPlatformType
k_EAuthTokenPlatformType_SteamClient: EAuthTokenPlatformType
k_EAuthTokenPlatformType_WebBrowser: EAuthTokenPlatformType
k_EAuthTokenPlatformType_MobileApp: EAuthTokenPlatformType
k_EAuthTokenAppType_Unknown: EAuthTokenAppType
k_EAuthTokenAppType_Mobile_SteamApp: EAuthTokenAppType
k_EAuthTokenAppType_Mobile_ChatApp: EAuthTokenAppType
k_EAuthSessionGuardType_Unknown: EAuthSessionGuardType
k_EAuthSessionGuardType_None: EAuthSessionGuardType
k_EAuthSessionGuardType_EmailCode: EAuthSessionGuardType
k_EAuthSessionGuardType_DeviceCode: EAuthSessionGuardType
k_EAuthSessionGuardType_DeviceConfirmation: EAuthSessionGuardType
k_EAuthSessionGuardType_EmailConfirmation: EAuthSessionGuardType
k_EAuthSessionGuardType_MachineToken: EAuthSessionGuardType
k_EAuthSessionGuardType_LegacyMachineAuth: EAuthSessionGuardType
k_EAuthSessionSecurityHistory_Invalid: EAuthSessionSecurityHistory
k_EAuthSessionSecurityHistory_UsedPreviously: EAuthSessionSecurityHistory
k_EAuthSessionSecurityHistory_NoPriorHistory: EAuthSessionSecurityHistory
k_ETokenRenewalType_None: ETokenRenewalType
k_ETokenRenewalType_Allow: ETokenRenewalType
k_EAuthenticationType_Unknown: EAuthenticationType
k_EAuthenticationType_Password: EAuthenticationType
k_EAuthenticationType_QR: EAuthenticationType
k_EAuthenticationType_AccountCreation: EAuthenticationType
k_EAuthenticationType_GuestAccount: EAuthenticationType
k_EAuthTokenRevokeLogout: EAuthTokenRevokeAction
k_EAuthTokenRevokePermanent: EAuthTokenRevokeAction
k_EAuthTokenRevokeReplaced: EAuthTokenRevokeAction
k_EAuthTokenRevokeSupport: EAuthTokenRevokeAction
k_EAuthTokenRevokeConsume: EAuthTokenRevokeAction
k_EAuthTokenRevokeNonRememberedLogout: EAuthTokenRevokeAction
k_EAuthTokenRevokeNonRememberedPermanent: EAuthTokenRevokeAction
k_EAuthTokenRevokeAutomatic: EAuthTokenRevokeAction
k_EAuthTokenState_Invalid: EAuthTokenState
k_EAuthTokenState_New: EAuthTokenState
k_EAuthTokenState_Confirmed: EAuthTokenState
k_EAuthTokenState_Issued: EAuthTokenState
k_EAuthTokenState_Denied: EAuthTokenState
k_EAuthTokenState_LoggedOut: EAuthTokenState
k_EAuthTokenState_Consumed: EAuthTokenState
k_EAuthTokenState_Revoked: EAuthTokenState

class CAuthentication_GetPasswordRSAPublicKey_Request(_message.Message):
    __slots__ = ("account_name",)
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    def __init__(self, account_name: _Optional[str] = ...) -> None: ...

class CAuthentication_GetPasswordRSAPublicKey_Response(_message.Message):
    __slots__ = ("publickey_mod", "publickey_exp", "timestamp")
    PUBLICKEY_MOD_FIELD_NUMBER: _ClassVar[int]
    PUBLICKEY_EXP_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    publickey_mod: str
    publickey_exp: str
    timestamp: int
    def __init__(self, publickey_mod: _Optional[str] = ..., publickey_exp: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CAuthentication_DeviceDetails(_message.Message):
    __slots__ = ("device_friendly_name", "platform_type", "os_type", "gaming_device_type", "client_count", "machine_id", "app_type")
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    device_friendly_name: str
    platform_type: EAuthTokenPlatformType
    os_type: int
    gaming_device_type: int
    client_count: int
    machine_id: bytes
    app_type: EAuthTokenAppType
    def __init__(self, device_friendly_name: _Optional[str] = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., os_type: _Optional[int] = ..., gaming_device_type: _Optional[int] = ..., client_count: _Optional[int] = ..., machine_id: _Optional[bytes] = ..., app_type: _Optional[_Union[EAuthTokenAppType, str]] = ...) -> None: ...

class CAuthentication_BeginAuthSessionViaQR_Request(_message.Message):
    __slots__ = ("device_friendly_name", "platform_type", "device_details", "website_id")
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_ID_FIELD_NUMBER: _ClassVar[int]
    device_friendly_name: str
    platform_type: EAuthTokenPlatformType
    device_details: CAuthentication_DeviceDetails
    website_id: str
    def __init__(self, device_friendly_name: _Optional[str] = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., device_details: _Optional[_Union[CAuthentication_DeviceDetails, _Mapping]] = ..., website_id: _Optional[str] = ...) -> None: ...

class CAuthentication_AllowedConfirmation(_message.Message):
    __slots__ = ("confirmation_type", "associated_message")
    CONFIRMATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    confirmation_type: EAuthSessionGuardType
    associated_message: str
    def __init__(self, confirmation_type: _Optional[_Union[EAuthSessionGuardType, str]] = ..., associated_message: _Optional[str] = ...) -> None: ...

class CAuthentication_BeginAuthSessionViaQR_Response(_message.Message):
    __slots__ = ("client_id", "challenge_url", "request_id", "interval", "allowed_confirmations", "version")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHALLENGE_URL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    challenge_url: str
    request_id: bytes
    interval: float
    allowed_confirmations: _containers.RepeatedCompositeFieldContainer[CAuthentication_AllowedConfirmation]
    version: int
    def __init__(self, client_id: _Optional[int] = ..., challenge_url: _Optional[str] = ..., request_id: _Optional[bytes] = ..., interval: _Optional[float] = ..., allowed_confirmations: _Optional[_Iterable[_Union[CAuthentication_AllowedConfirmation, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class CAuthentication_BeginAuthSessionViaCredentials_Request(_message.Message):
    __slots__ = ("device_friendly_name", "account_name", "encrypted_password", "encryption_timestamp", "remember_login", "platform_type", "persistence", "website_id", "device_details", "guard_data", "language", "qos_level")
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    REMEMBER_LOGIN_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    GUARD_DATA_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    QOS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    device_friendly_name: str
    account_name: str
    encrypted_password: str
    encryption_timestamp: int
    remember_login: bool
    platform_type: EAuthTokenPlatformType
    persistence: _enums_pb2.ESessionPersistence
    website_id: str
    device_details: CAuthentication_DeviceDetails
    guard_data: str
    language: int
    qos_level: int
    def __init__(self, device_friendly_name: _Optional[str] = ..., account_name: _Optional[str] = ..., encrypted_password: _Optional[str] = ..., encryption_timestamp: _Optional[int] = ..., remember_login: bool = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., persistence: _Optional[_Union[_enums_pb2.ESessionPersistence, str]] = ..., website_id: _Optional[str] = ..., device_details: _Optional[_Union[CAuthentication_DeviceDetails, _Mapping]] = ..., guard_data: _Optional[str] = ..., language: _Optional[int] = ..., qos_level: _Optional[int] = ...) -> None: ...

class CAuthentication_BeginAuthSessionViaCredentials_Response(_message.Message):
    __slots__ = ("client_id", "request_id", "interval", "allowed_confirmations", "steamid", "weak_token", "agreement_session_url", "extended_error_message")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_CONFIRMATIONS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    WEAK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_SESSION_URL_FIELD_NUMBER: _ClassVar[int]
    EXTENDED_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    request_id: bytes
    interval: float
    allowed_confirmations: _containers.RepeatedCompositeFieldContainer[CAuthentication_AllowedConfirmation]
    steamid: int
    weak_token: str
    agreement_session_url: str
    extended_error_message: str
    def __init__(self, client_id: _Optional[int] = ..., request_id: _Optional[bytes] = ..., interval: _Optional[float] = ..., allowed_confirmations: _Optional[_Iterable[_Union[CAuthentication_AllowedConfirmation, _Mapping]]] = ..., steamid: _Optional[int] = ..., weak_token: _Optional[str] = ..., agreement_session_url: _Optional[str] = ..., extended_error_message: _Optional[str] = ...) -> None: ...

class CAuthentication_PollAuthSessionStatus_Request(_message.Message):
    __slots__ = ("client_id", "request_id", "token_to_revoke")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TO_REVOKE_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    request_id: bytes
    token_to_revoke: int
    def __init__(self, client_id: _Optional[int] = ..., request_id: _Optional[bytes] = ..., token_to_revoke: _Optional[int] = ...) -> None: ...

class CAuthentication_PollAuthSessionStatus_Response(_message.Message):
    __slots__ = ("new_client_id", "new_challenge_url", "refresh_token", "access_token", "had_remote_interaction", "account_name", "new_guard_data", "agreement_session_url")
    NEW_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_CHALLENGE_URL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HAD_REMOTE_INTERACTION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_GUARD_DATA_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_SESSION_URL_FIELD_NUMBER: _ClassVar[int]
    new_client_id: int
    new_challenge_url: str
    refresh_token: str
    access_token: str
    had_remote_interaction: bool
    account_name: str
    new_guard_data: str
    agreement_session_url: str
    def __init__(self, new_client_id: _Optional[int] = ..., new_challenge_url: _Optional[str] = ..., refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ..., had_remote_interaction: bool = ..., account_name: _Optional[str] = ..., new_guard_data: _Optional[str] = ..., agreement_session_url: _Optional[str] = ...) -> None: ...

class CAuthentication_GetAuthSessionInfo_Request(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    def __init__(self, client_id: _Optional[int] = ...) -> None: ...

class CAuthentication_GetAuthSessionInfo_Response(_message.Message):
    __slots__ = ("ip", "geoloc", "city", "state", "country", "platform_type", "device_friendly_name", "version", "login_history", "requestor_location_mismatch", "high_usage_login", "requested_persistence", "device_trust", "app_type")
    IP_FIELD_NUMBER: _ClassVar[int]
    GEOLOC_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    LOGIN_HISTORY_FIELD_NUMBER: _ClassVar[int]
    REQUESTOR_LOCATION_MISMATCH_FIELD_NUMBER: _ClassVar[int]
    HIGH_USAGE_LOGIN_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRUST_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    ip: str
    geoloc: str
    city: str
    state: str
    country: str
    platform_type: EAuthTokenPlatformType
    device_friendly_name: str
    version: int
    login_history: EAuthSessionSecurityHistory
    requestor_location_mismatch: bool
    high_usage_login: bool
    requested_persistence: _enums_pb2.ESessionPersistence
    device_trust: int
    app_type: EAuthTokenAppType
    def __init__(self, ip: _Optional[str] = ..., geoloc: _Optional[str] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., device_friendly_name: _Optional[str] = ..., version: _Optional[int] = ..., login_history: _Optional[_Union[EAuthSessionSecurityHistory, str]] = ..., requestor_location_mismatch: bool = ..., high_usage_login: bool = ..., requested_persistence: _Optional[_Union[_enums_pb2.ESessionPersistence, str]] = ..., device_trust: _Optional[int] = ..., app_type: _Optional[_Union[EAuthTokenAppType, str]] = ...) -> None: ...

class CAuthentication_GetAuthSessionRiskInfo_Request(_message.Message):
    __slots__ = ("client_id", "language")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    language: int
    def __init__(self, client_id: _Optional[int] = ..., language: _Optional[int] = ...) -> None: ...

class CAuthentication_GetAuthSessionRiskInfo_Response(_message.Message):
    __slots__ = ("location_confirmer", "location_requestor", "location_other", "platform_type")
    LOCATION_CONFIRMER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_REQUESTOR_FIELD_NUMBER: _ClassVar[int]
    LOCATION_OTHER_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    location_confirmer: str
    location_requestor: str
    location_other: str
    platform_type: EAuthTokenPlatformType
    def __init__(self, location_confirmer: _Optional[str] = ..., location_requestor: _Optional[str] = ..., location_other: _Optional[str] = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ...) -> None: ...

class CAuthentication_NotifyRiskQuizResults_Notification(_message.Message):
    __slots__ = ("client_id", "results", "selected_action", "did_confirm_login")
    class RiskQuizResults(_message.Message):
        __slots__ = ("platform", "location", "action")
        PLATFORM_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        platform: bool
        location: bool
        action: bool
        def __init__(self, platform: bool = ..., location: bool = ..., action: bool = ...) -> None: ...
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ACTION_FIELD_NUMBER: _ClassVar[int]
    DID_CONFIRM_LOGIN_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    results: CAuthentication_NotifyRiskQuizResults_Notification.RiskQuizResults
    selected_action: str
    did_confirm_login: bool
    def __init__(self, client_id: _Optional[int] = ..., results: _Optional[_Union[CAuthentication_NotifyRiskQuizResults_Notification.RiskQuizResults, _Mapping]] = ..., selected_action: _Optional[str] = ..., did_confirm_login: bool = ...) -> None: ...

class CAuthentication_UpdateAuthSessionWithMobileConfirmation_Request(_message.Message):
    __slots__ = ("version", "client_id", "steamid", "signature", "confirm", "persistence")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_FIELD_NUMBER: _ClassVar[int]
    version: int
    client_id: int
    steamid: int
    signature: bytes
    confirm: bool
    persistence: _enums_pb2.ESessionPersistence
    def __init__(self, version: _Optional[int] = ..., client_id: _Optional[int] = ..., steamid: _Optional[int] = ..., signature: _Optional[bytes] = ..., confirm: bool = ..., persistence: _Optional[_Union[_enums_pb2.ESessionPersistence, str]] = ...) -> None: ...

class CAuthentication_UpdateAuthSessionWithMobileConfirmation_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAuthentication_UpdateAuthSessionWithSteamGuardCode_Request(_message.Message):
    __slots__ = ("client_id", "steamid", "code", "code_type")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    steamid: int
    code: str
    code_type: EAuthSessionGuardType
    def __init__(self, client_id: _Optional[int] = ..., steamid: _Optional[int] = ..., code: _Optional[str] = ..., code_type: _Optional[_Union[EAuthSessionGuardType, str]] = ...) -> None: ...

class CAuthentication_UpdateAuthSessionWithSteamGuardCode_Response(_message.Message):
    __slots__ = ("agreement_session_url",)
    AGREEMENT_SESSION_URL_FIELD_NUMBER: _ClassVar[int]
    agreement_session_url: str
    def __init__(self, agreement_session_url: _Optional[str] = ...) -> None: ...

class CAuthentication_AccessToken_GenerateForApp_Request(_message.Message):
    __slots__ = ("refresh_token", "steamid", "renewal_type")
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_TYPE_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    steamid: int
    renewal_type: ETokenRenewalType
    def __init__(self, refresh_token: _Optional[str] = ..., steamid: _Optional[int] = ..., renewal_type: _Optional[_Union[ETokenRenewalType, str]] = ...) -> None: ...

class CAuthentication_AccessToken_GenerateForApp_Response(_message.Message):
    __slots__ = ("access_token", "refresh_token")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    def __init__(self, access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ...) -> None: ...

class CAuthentication_RefreshToken_Enumerate_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAuthentication_RefreshToken_Enumerate_Response(_message.Message):
    __slots__ = ("refresh_tokens", "requesting_token")
    class TokenUsageEvent(_message.Message):
        __slots__ = ("time", "ip", "locale", "country", "state", "city")
        TIME_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        time: int
        ip: _steammessages_base_pb2.CMsgIPAddress
        locale: str
        country: str
        state: str
        city: str
        def __init__(self, time: _Optional[int] = ..., ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., locale: _Optional[str] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    class RefreshTokenDescription(_message.Message):
        __slots__ = ("token_id", "token_description", "time_updated", "platform_type", "logged_in", "os_platform", "auth_type", "gaming_device_type", "first_seen", "last_seen", "os_type", "authentication_type")
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
        PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        OS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
        AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
        GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
        LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
        OS_TYPE_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        token_id: int
        token_description: str
        time_updated: int
        platform_type: EAuthTokenPlatformType
        logged_in: bool
        os_platform: int
        auth_type: int
        gaming_device_type: int
        first_seen: CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent
        last_seen: CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent
        os_type: int
        authentication_type: EAuthenticationType
        def __init__(self, token_id: _Optional[int] = ..., token_description: _Optional[str] = ..., time_updated: _Optional[int] = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., logged_in: bool = ..., os_platform: _Optional[int] = ..., auth_type: _Optional[int] = ..., gaming_device_type: _Optional[int] = ..., first_seen: _Optional[_Union[CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent, _Mapping]] = ..., last_seen: _Optional[_Union[CAuthentication_RefreshToken_Enumerate_Response.TokenUsageEvent, _Mapping]] = ..., os_type: _Optional[int] = ..., authentication_type: _Optional[_Union[EAuthenticationType, str]] = ...) -> None: ...
    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.RepeatedCompositeFieldContainer[CAuthentication_RefreshToken_Enumerate_Response.RefreshTokenDescription]
    requesting_token: int
    def __init__(self, refresh_tokens: _Optional[_Iterable[_Union[CAuthentication_RefreshToken_Enumerate_Response.RefreshTokenDescription, _Mapping]]] = ..., requesting_token: _Optional[int] = ...) -> None: ...

class CAuthentication_GetAuthSessionsForAccount_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAuthentication_GetAuthSessionsForAccount_Response(_message.Message):
    __slots__ = ("client_ids",)
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    client_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, client_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CAuthentication_MigrateMobileSession_Request(_message.Message):
    __slots__ = ("steamid", "token", "signature")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    token: str
    signature: str
    def __init__(self, steamid: _Optional[int] = ..., token: _Optional[str] = ..., signature: _Optional[str] = ...) -> None: ...

class CAuthentication_MigrateMobileSession_Response(_message.Message):
    __slots__ = ("refresh_token", "access_token")
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    refresh_token: str
    access_token: str
    def __init__(self, refresh_token: _Optional[str] = ..., access_token: _Optional[str] = ...) -> None: ...

class CAuthentication_Token_Revoke_Request(_message.Message):
    __slots__ = ("token", "revoke_action")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    REVOKE_ACTION_FIELD_NUMBER: _ClassVar[int]
    token: str
    revoke_action: EAuthTokenRevokeAction
    def __init__(self, token: _Optional[str] = ..., revoke_action: _Optional[_Union[EAuthTokenRevokeAction, str]] = ...) -> None: ...

class CAuthentication_Token_Revoke_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAuthentication_RefreshToken_Revoke_Request(_message.Message):
    __slots__ = ("token_id", "steamid", "revoke_action", "signature")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_ACTION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    steamid: int
    revoke_action: EAuthTokenRevokeAction
    signature: bytes
    def __init__(self, token_id: _Optional[int] = ..., steamid: _Optional[int] = ..., revoke_action: _Optional[_Union[EAuthTokenRevokeAction, str]] = ..., signature: _Optional[bytes] = ...) -> None: ...

class CAuthentication_RefreshToken_Revoke_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAuthenticationSupport_QueryRefreshTokensByAccount_Request(_message.Message):
    __slots__ = ("steamid", "include_revoked_tokens")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REVOKED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_revoked_tokens: bool
    def __init__(self, steamid: _Optional[int] = ..., include_revoked_tokens: bool = ...) -> None: ...

class CSupportRefreshTokenDescription(_message.Message):
    __slots__ = ("token_id", "token_description", "time_updated", "platform_type", "token_state", "owner_steamid", "os_platform", "os_type", "auth_type", "gaming_device_type", "first_seen", "last_seen")
    class TokenUsageEvent(_message.Message):
        __slots__ = ("time", "ip", "country", "state", "city")
        TIME_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        CITY_FIELD_NUMBER: _ClassVar[int]
        time: int
        ip: _steammessages_base_pb2.CMsgIPAddress
        country: str
        state: str
        city: str
        def __init__(self, time: _Optional[int] = ..., ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_STATE_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    OS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    token_description: str
    time_updated: int
    platform_type: EAuthTokenPlatformType
    token_state: EAuthTokenState
    owner_steamid: int
    os_platform: int
    os_type: int
    auth_type: int
    gaming_device_type: int
    first_seen: CSupportRefreshTokenDescription.TokenUsageEvent
    last_seen: CSupportRefreshTokenDescription.TokenUsageEvent
    def __init__(self, token_id: _Optional[int] = ..., token_description: _Optional[str] = ..., time_updated: _Optional[int] = ..., platform_type: _Optional[_Union[EAuthTokenPlatformType, str]] = ..., token_state: _Optional[_Union[EAuthTokenState, str]] = ..., owner_steamid: _Optional[int] = ..., os_platform: _Optional[int] = ..., os_type: _Optional[int] = ..., auth_type: _Optional[int] = ..., gaming_device_type: _Optional[int] = ..., first_seen: _Optional[_Union[CSupportRefreshTokenDescription.TokenUsageEvent, _Mapping]] = ..., last_seen: _Optional[_Union[CSupportRefreshTokenDescription.TokenUsageEvent, _Mapping]] = ...) -> None: ...

class CAuthenticationSupport_QueryRefreshTokensByAccount_Response(_message.Message):
    __slots__ = ("refresh_tokens", "last_token_reset")
    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    LAST_TOKEN_RESET_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.RepeatedCompositeFieldContainer[CSupportRefreshTokenDescription]
    last_token_reset: int
    def __init__(self, refresh_tokens: _Optional[_Iterable[_Union[CSupportRefreshTokenDescription, _Mapping]]] = ..., last_token_reset: _Optional[int] = ...) -> None: ...

class CAuthenticationSupport_QueryRefreshTokenByID_Request(_message.Message):
    __slots__ = ("token_id",)
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    def __init__(self, token_id: _Optional[int] = ...) -> None: ...

class CAuthenticationSupport_QueryRefreshTokenByID_Response(_message.Message):
    __slots__ = ("refresh_tokens",)
    REFRESH_TOKENS_FIELD_NUMBER: _ClassVar[int]
    refresh_tokens: _containers.RepeatedCompositeFieldContainer[CSupportRefreshTokenDescription]
    def __init__(self, refresh_tokens: _Optional[_Iterable[_Union[CSupportRefreshTokenDescription, _Mapping]]] = ...) -> None: ...

class CAuthenticationSupport_RevokeToken_Request(_message.Message):
    __slots__ = ("token_id", "steamid")
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    steamid: int
    def __init__(self, token_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CAuthenticationSupport_RevokeToken_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAuthenticationSupport_GetTokenHistory_Request(_message.Message):
    __slots__ = ("token_id",)
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    token_id: int
    def __init__(self, token_id: _Optional[int] = ...) -> None: ...

class CSupportRefreshTokenAudit(_message.Message):
    __slots__ = ("action", "time", "ip", "actor")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    action: int
    time: int
    ip: _steammessages_base_pb2.CMsgIPAddress
    actor: int
    def __init__(self, action: _Optional[int] = ..., time: _Optional[int] = ..., ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., actor: _Optional[int] = ...) -> None: ...

class CAuthenticationSupport_GetTokenHistory_Response(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[CSupportRefreshTokenAudit]
    def __init__(self, history: _Optional[_Iterable[_Union[CSupportRefreshTokenAudit, _Mapping]]] = ...) -> None: ...

class CAuthenticationSupport_MarkTokenCompromised_Request(_message.Message):
    __slots__ = ("steamid", "token_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    token_id: int
    def __init__(self, steamid: _Optional[int] = ..., token_id: _Optional[int] = ...) -> None: ...

class CAuthenticationSupport_MarkTokenCompromised_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCloudGaming_CreateNonce_Request(_message.Message):
    __slots__ = ("platform", "appid")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    platform: str
    appid: int
    def __init__(self, platform: _Optional[str] = ..., appid: _Optional[int] = ...) -> None: ...

class CCloudGaming_CreateNonce_Response(_message.Message):
    __slots__ = ("nonce", "expiry")
    NONCE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    nonce: str
    expiry: int
    def __init__(self, nonce: _Optional[str] = ..., expiry: _Optional[int] = ...) -> None: ...

class CCloudGaming_GetTimeRemaining_Request(_message.Message):
    __slots__ = ("platform", "appid_list")
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    APPID_LIST_FIELD_NUMBER: _ClassVar[int]
    platform: str
    appid_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, platform: _Optional[str] = ..., appid_list: _Optional[_Iterable[int]] = ...) -> None: ...

class CCloudGaming_TimeRemaining(_message.Message):
    __slots__ = ("appid", "minutes_remaining")
    APPID_FIELD_NUMBER: _ClassVar[int]
    MINUTES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    appid: int
    minutes_remaining: int
    def __init__(self, appid: _Optional[int] = ..., minutes_remaining: _Optional[int] = ...) -> None: ...

class CCloudGaming_GetTimeRemaining_Response(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CCloudGaming_TimeRemaining]
    def __init__(self, entries: _Optional[_Iterable[_Union[CCloudGaming_TimeRemaining, _Mapping]]] = ...) -> None: ...

class Authentication(_service.service): ...

class Authentication_Stub(Authentication): ...

class AuthenticationSupport(_service.service): ...

class AuthenticationSupport_Stub(AuthenticationSupport): ...

class CloudGaming(_service.service): ...

class CloudGaming_Stub(CloudGaming): ...
