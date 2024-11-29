import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CCredentials_TestAvailablePassword_Request(_message.Message):
    __slots__ = ("password", "sha_digest_password", "account_name")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SHA_DIGEST_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    sha_digest_password: bytes
    account_name: str
    def __init__(self, password: _Optional[str] = ..., sha_digest_password: _Optional[bytes] = ..., account_name: _Optional[str] = ...) -> None: ...

class CCredentials_TestAvailablePassword_Response(_message.Message):
    __slots__ = ("is_valid",)
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    is_valid: bool
    def __init__(self, is_valid: bool = ...) -> None: ...

class CCredentials_GetSteamGuardDetails_Request(_message.Message):
    __slots__ = ("webcookie", "timestamp_minimum_wanted", "deprecated_ipaddress", "ip_address")
    WEBCOOKIE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MINIMUM_WANTED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    webcookie: str
    timestamp_minimum_wanted: int
    deprecated_ipaddress: int
    ip_address: _steammessages_base_pb2.CMsgIPAddress
    def __init__(self, webcookie: _Optional[str] = ..., timestamp_minimum_wanted: _Optional[int] = ..., deprecated_ipaddress: _Optional[int] = ..., ip_address: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...) -> None: ...

class CCredentials_GetSteamGuardDetails_Response(_message.Message):
    __slots__ = ("is_steamguard_enabled", "timestamp_steamguard_enabled", "deprecated_machine_name_userchosen", "deprecated_timestamp_machine_steamguard_enabled", "deprecated_authentication_exists_from_geoloc_before_mintime", "deprecated_machine_id", "session_data", "is_twofactor_enabled", "timestamp_twofactor_enabled", "is_phone_verified")
    class SessionData(_message.Message):
        __slots__ = ("machine_id", "machine_name_userchosen", "timestamp_machine_steamguard_enabled", "authentication_exists_from_geoloc_before_mintime", "authentication_exists_from_same_ip_before_mintime", "public_ipv4", "public_ip_address")
        MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
        MACHINE_NAME_USERCHOSEN_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_MACHINE_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_EXISTS_FROM_GEOLOC_BEFORE_MINTIME_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_EXISTS_FROM_SAME_IP_BEFORE_MINTIME_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_IPV4_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        machine_id: int
        machine_name_userchosen: str
        timestamp_machine_steamguard_enabled: int
        authentication_exists_from_geoloc_before_mintime: bool
        authentication_exists_from_same_ip_before_mintime: bool
        public_ipv4: int
        public_ip_address: str
        def __init__(self, machine_id: _Optional[int] = ..., machine_name_userchosen: _Optional[str] = ..., timestamp_machine_steamguard_enabled: _Optional[int] = ..., authentication_exists_from_geoloc_before_mintime: bool = ..., authentication_exists_from_same_ip_before_mintime: bool = ..., public_ipv4: _Optional[int] = ..., public_ip_address: _Optional[str] = ...) -> None: ...
    IS_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_MACHINE_NAME_USERCHOSEN_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_TIMESTAMP_MACHINE_STEAMGUARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_AUTHENTICATION_EXISTS_FROM_GEOLOC_BEFORE_MINTIME_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_DATA_FIELD_NUMBER: _ClassVar[int]
    IS_TWOFACTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_TWOFACTOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    is_steamguard_enabled: bool
    timestamp_steamguard_enabled: int
    deprecated_machine_name_userchosen: str
    deprecated_timestamp_machine_steamguard_enabled: int
    deprecated_authentication_exists_from_geoloc_before_mintime: bool
    deprecated_machine_id: int
    session_data: _containers.RepeatedCompositeFieldContainer[CCredentials_GetSteamGuardDetails_Response.SessionData]
    is_twofactor_enabled: bool
    timestamp_twofactor_enabled: int
    is_phone_verified: bool
    def __init__(self, is_steamguard_enabled: bool = ..., timestamp_steamguard_enabled: _Optional[int] = ..., deprecated_machine_name_userchosen: _Optional[str] = ..., deprecated_timestamp_machine_steamguard_enabled: _Optional[int] = ..., deprecated_authentication_exists_from_geoloc_before_mintime: bool = ..., deprecated_machine_id: _Optional[int] = ..., session_data: _Optional[_Iterable[_Union[CCredentials_GetSteamGuardDetails_Response.SessionData, _Mapping]]] = ..., is_twofactor_enabled: bool = ..., timestamp_twofactor_enabled: _Optional[int] = ..., is_phone_verified: bool = ...) -> None: ...

class CCredentials_ValidateEmailAddress_Request(_message.Message):
    __slots__ = ("stoken",)
    STOKEN_FIELD_NUMBER: _ClassVar[int]
    stoken: str
    def __init__(self, stoken: _Optional[str] = ...) -> None: ...

class CCredentials_ValidateEmailAddress_Response(_message.Message):
    __slots__ = ("was_validated",)
    WAS_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    was_validated: bool
    def __init__(self, was_validated: bool = ...) -> None: ...

class CCredentials_SteamGuardPhishingReport_Request(_message.Message):
    __slots__ = ("param_string", "ipaddress_actual")
    PARAM_STRING_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    param_string: str
    ipaddress_actual: str
    def __init__(self, param_string: _Optional[str] = ..., ipaddress_actual: _Optional[str] = ...) -> None: ...

class CCredentials_SteamGuardPhishingReport_Response(_message.Message):
    __slots__ = ("ipaddress_loginattempt", "countryname_loginattempt", "statename_loginattempt", "cityname_loginattempt", "ipaddress_actual", "countryname_actual", "statename_actual", "cityname_actual", "steamguard_code")
    IPADDRESS_LOGINATTEMPT_FIELD_NUMBER: _ClassVar[int]
    COUNTRYNAME_LOGINATTEMPT_FIELD_NUMBER: _ClassVar[int]
    STATENAME_LOGINATTEMPT_FIELD_NUMBER: _ClassVar[int]
    CITYNAME_LOGINATTEMPT_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    COUNTRYNAME_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    STATENAME_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    CITYNAME_ACTUAL_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_CODE_FIELD_NUMBER: _ClassVar[int]
    ipaddress_loginattempt: str
    countryname_loginattempt: str
    statename_loginattempt: str
    cityname_loginattempt: str
    ipaddress_actual: str
    countryname_actual: str
    statename_actual: str
    cityname_actual: str
    steamguard_code: str
    def __init__(self, ipaddress_loginattempt: _Optional[str] = ..., countryname_loginattempt: _Optional[str] = ..., statename_loginattempt: _Optional[str] = ..., cityname_loginattempt: _Optional[str] = ..., ipaddress_actual: _Optional[str] = ..., countryname_actual: _Optional[str] = ..., statename_actual: _Optional[str] = ..., cityname_actual: _Optional[str] = ..., steamguard_code: _Optional[str] = ...) -> None: ...

class CCredentials_LastCredentialChangeTime_Request(_message.Message):
    __slots__ = ("user_changes_only",)
    USER_CHANGES_ONLY_FIELD_NUMBER: _ClassVar[int]
    user_changes_only: bool
    def __init__(self, user_changes_only: bool = ...) -> None: ...

class CCredentials_LastCredentialChangeTime_Response(_message.Message):
    __slots__ = ("timestamp_last_password_change", "timestamp_last_email_change", "timestamp_last_password_reset")
    TIMESTAMP_LAST_PASSWORD_CHANGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_LAST_EMAIL_CHANGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_LAST_PASSWORD_RESET_FIELD_NUMBER: _ClassVar[int]
    timestamp_last_password_change: int
    timestamp_last_email_change: int
    timestamp_last_password_reset: int
    def __init__(self, timestamp_last_password_change: _Optional[int] = ..., timestamp_last_email_change: _Optional[int] = ..., timestamp_last_password_reset: _Optional[int] = ...) -> None: ...

class CCredentials_GetAccountAuthSecret_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCredentials_GetAccountAuthSecret_Response(_message.Message):
    __slots__ = ("secret_id", "secret")
    SECRET_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret_id: int
    secret: bytes
    def __init__(self, secret_id: _Optional[int] = ..., secret: _Optional[bytes] = ...) -> None: ...

class Credentials(_service.service): ...

class Credentials_Stub(Credentials): ...
