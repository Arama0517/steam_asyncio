import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CTwoFactor_Time_Request(_message.Message):
    __slots__ = ("sender_time",)
    SENDER_TIME_FIELD_NUMBER: _ClassVar[int]
    sender_time: int
    def __init__(self, sender_time: _Optional[int] = ...) -> None: ...

class CTwoFactor_Time_Response(_message.Message):
    __slots__ = ("server_time", "skew_tolerance_seconds", "large_time_jink", "probe_frequency_seconds", "adjusted_time_probe_frequency_seconds", "hint_probe_frequency_seconds", "sync_timeout", "try_again_seconds", "max_attempts")
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    SKEW_TOLERANCE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    LARGE_TIME_JINK_FIELD_NUMBER: _ClassVar[int]
    PROBE_FREQUENCY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ADJUSTED_TIME_PROBE_FREQUENCY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HINT_PROBE_FREQUENCY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    SYNC_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TRY_AGAIN_SECONDS_FIELD_NUMBER: _ClassVar[int]
    MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    server_time: int
    skew_tolerance_seconds: int
    large_time_jink: int
    probe_frequency_seconds: int
    adjusted_time_probe_frequency_seconds: int
    hint_probe_frequency_seconds: int
    sync_timeout: int
    try_again_seconds: int
    max_attempts: int
    def __init__(self, server_time: _Optional[int] = ..., skew_tolerance_seconds: _Optional[int] = ..., large_time_jink: _Optional[int] = ..., probe_frequency_seconds: _Optional[int] = ..., adjusted_time_probe_frequency_seconds: _Optional[int] = ..., hint_probe_frequency_seconds: _Optional[int] = ..., sync_timeout: _Optional[int] = ..., try_again_seconds: _Optional[int] = ..., max_attempts: _Optional[int] = ...) -> None: ...

class CTwoFactor_Status_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CTwoFactor_Status_Response(_message.Message):
    __slots__ = ("state", "inactivation_reason", "authenticator_type", "authenticator_allowed", "steamguard_scheme", "token_gid", "email_validated", "device_identifier", "time_created", "revocation_attempts_remaining", "classified_agent", "allow_external_authenticator", "time_transferred", "version")
    STATE_FIELD_NUMBER: _ClassVar[int]
    INACTIVATION_REASON_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_SCHEME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_GID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_ATTEMPTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIED_AGENT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_EXTERNAL_AUTHENTICATOR_FIELD_NUMBER: _ClassVar[int]
    TIME_TRANSFERRED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    state: int
    inactivation_reason: int
    authenticator_type: int
    authenticator_allowed: bool
    steamguard_scheme: int
    token_gid: str
    email_validated: bool
    device_identifier: str
    time_created: int
    revocation_attempts_remaining: int
    classified_agent: str
    allow_external_authenticator: bool
    time_transferred: int
    version: int
    def __init__(self, state: _Optional[int] = ..., inactivation_reason: _Optional[int] = ..., authenticator_type: _Optional[int] = ..., authenticator_allowed: bool = ..., steamguard_scheme: _Optional[int] = ..., token_gid: _Optional[str] = ..., email_validated: bool = ..., device_identifier: _Optional[str] = ..., time_created: _Optional[int] = ..., revocation_attempts_remaining: _Optional[int] = ..., classified_agent: _Optional[str] = ..., allow_external_authenticator: bool = ..., time_transferred: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class CTwoFactor_AddAuthenticator_Request(_message.Message):
    __slots__ = ("steamid", "authenticator_time", "serial_number", "authenticator_type", "device_identifier", "http_headers", "version")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_TIME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    authenticator_time: int
    serial_number: int
    authenticator_type: int
    device_identifier: str
    http_headers: _containers.RepeatedScalarFieldContainer[str]
    version: int
    def __init__(self, steamid: _Optional[int] = ..., authenticator_time: _Optional[int] = ..., serial_number: _Optional[int] = ..., authenticator_type: _Optional[int] = ..., device_identifier: _Optional[str] = ..., http_headers: _Optional[_Iterable[str]] = ..., version: _Optional[int] = ...) -> None: ...

class CTwoFactor_AddAuthenticator_Response(_message.Message):
    __slots__ = ("shared_secret", "serial_number", "revocation_code", "uri", "server_time", "account_name", "token_gid", "identity_secret", "secret_1", "status", "phone_number_hint", "confirm_type")
    SHARED_SECRET_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_CODE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_GID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SECRET_FIELD_NUMBER: _ClassVar[int]
    SECRET_1_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_HINT_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_TYPE_FIELD_NUMBER: _ClassVar[int]
    shared_secret: bytes
    serial_number: int
    revocation_code: str
    uri: str
    server_time: int
    account_name: str
    token_gid: str
    identity_secret: bytes
    secret_1: bytes
    status: int
    phone_number_hint: str
    confirm_type: int
    def __init__(self, shared_secret: _Optional[bytes] = ..., serial_number: _Optional[int] = ..., revocation_code: _Optional[str] = ..., uri: _Optional[str] = ..., server_time: _Optional[int] = ..., account_name: _Optional[str] = ..., token_gid: _Optional[str] = ..., identity_secret: _Optional[bytes] = ..., secret_1: _Optional[bytes] = ..., status: _Optional[int] = ..., phone_number_hint: _Optional[str] = ..., confirm_type: _Optional[int] = ...) -> None: ...

class CTwoFactor_SendEmail_Request(_message.Message):
    __slots__ = ("steamid", "email_type", "include_activation_code")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ACTIVATION_CODE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    email_type: int
    include_activation_code: bool
    def __init__(self, steamid: _Optional[int] = ..., email_type: _Optional[int] = ..., include_activation_code: bool = ...) -> None: ...

class CTwoFactor_SendEmail_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTwoFactor_FinalizeAddAuthenticator_Request(_message.Message):
    __slots__ = ("steamid", "authenticator_code", "authenticator_time", "activation_code", "http_headers", "validate_sms_code")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_CODE_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATOR_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_CODE_FIELD_NUMBER: _ClassVar[int]
    HTTP_HEADERS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_SMS_CODE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    authenticator_code: str
    authenticator_time: int
    activation_code: str
    http_headers: _containers.RepeatedScalarFieldContainer[str]
    validate_sms_code: bool
    def __init__(self, steamid: _Optional[int] = ..., authenticator_code: _Optional[str] = ..., authenticator_time: _Optional[int] = ..., activation_code: _Optional[str] = ..., http_headers: _Optional[_Iterable[str]] = ..., validate_sms_code: bool = ...) -> None: ...

class CTwoFactor_FinalizeAddAuthenticator_Response(_message.Message):
    __slots__ = ("success", "server_time", "status")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    server_time: int
    status: int
    def __init__(self, success: bool = ..., server_time: _Optional[int] = ..., status: _Optional[int] = ...) -> None: ...

class CTwoFactor_UpdateTokenVersion_Request(_message.Message):
    __slots__ = ("steamid", "version", "signature")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    version: int
    signature: bytes
    def __init__(self, steamid: _Optional[int] = ..., version: _Optional[int] = ..., signature: _Optional[bytes] = ...) -> None: ...

class CTwoFactor_UpdateTokenVersion_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTwoFactor_RemoveAuthenticator_Request(_message.Message):
    __slots__ = ("revocation_code", "revocation_reason", "steamguard_scheme", "remove_all_steamguard_cookies")
    REVOCATION_CODE_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_REASON_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_SCHEME_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALL_STEAMGUARD_COOKIES_FIELD_NUMBER: _ClassVar[int]
    revocation_code: str
    revocation_reason: int
    steamguard_scheme: int
    remove_all_steamguard_cookies: bool
    def __init__(self, revocation_code: _Optional[str] = ..., revocation_reason: _Optional[int] = ..., steamguard_scheme: _Optional[int] = ..., remove_all_steamguard_cookies: bool = ...) -> None: ...

class CTwoFactor_RemoveAuthenticator_Response(_message.Message):
    __slots__ = ("success", "server_time", "revocation_attempts_remaining")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_ATTEMPTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    success: bool
    server_time: int
    revocation_attempts_remaining: int
    def __init__(self, success: bool = ..., server_time: _Optional[int] = ..., revocation_attempts_remaining: _Optional[int] = ...) -> None: ...

class CTwoFactor_RemoveAuthenticatorViaChallengeStart_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CTwoFactor_RemoveAuthenticatorViaChallengeStart_Response(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CTwoFactor_RemoveAuthenticatorViaChallengeContinue_Request(_message.Message):
    __slots__ = ("sms_code", "generate_new_token", "version")
    SMS_CODE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_NEW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    sms_code: str
    generate_new_token: bool
    version: int
    def __init__(self, sms_code: _Optional[str] = ..., generate_new_token: bool = ..., version: _Optional[int] = ...) -> None: ...

class CRemoveAuthenticatorViaChallengeContinue_Replacement_Token(_message.Message):
    __slots__ = ("shared_secret", "serial_number", "revocation_code", "uri", "server_time", "account_name", "token_gid", "identity_secret", "secret_1", "status", "steamguard_scheme", "steamid")
    SHARED_SECRET_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    REVOCATION_CODE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    TOKEN_GID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_SECRET_FIELD_NUMBER: _ClassVar[int]
    SECRET_1_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_SCHEME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    shared_secret: bytes
    serial_number: int
    revocation_code: str
    uri: str
    server_time: int
    account_name: str
    token_gid: str
    identity_secret: bytes
    secret_1: bytes
    status: int
    steamguard_scheme: int
    steamid: int
    def __init__(self, shared_secret: _Optional[bytes] = ..., serial_number: _Optional[int] = ..., revocation_code: _Optional[str] = ..., uri: _Optional[str] = ..., server_time: _Optional[int] = ..., account_name: _Optional[str] = ..., token_gid: _Optional[str] = ..., identity_secret: _Optional[bytes] = ..., secret_1: _Optional[bytes] = ..., status: _Optional[int] = ..., steamguard_scheme: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CTwoFactor_RemoveAuthenticatorViaChallengeContinue_Response(_message.Message):
    __slots__ = ("success", "replacement_token")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    success: bool
    replacement_token: CRemoveAuthenticatorViaChallengeContinue_Replacement_Token
    def __init__(self, success: bool = ..., replacement_token: _Optional[_Union[CRemoveAuthenticatorViaChallengeContinue_Replacement_Token, _Mapping]] = ...) -> None: ...

class TwoFactor(_service.service): ...

class TwoFactor_Stub(TwoFactor): ...
