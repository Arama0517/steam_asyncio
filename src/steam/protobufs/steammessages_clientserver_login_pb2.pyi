import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientHeartBeat(_message.Message):
    __slots__ = ("send_reply",)
    SEND_REPLY_FIELD_NUMBER: _ClassVar[int]
    send_reply: bool
    def __init__(self, send_reply: bool = ...) -> None: ...

class CMsgClientServerTimestampRequest(_message.Message):
    __slots__ = ("client_request_timestamp",)
    CLIENT_REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    client_request_timestamp: int
    def __init__(self, client_request_timestamp: _Optional[int] = ...) -> None: ...

class CMsgClientServerTimestampResponse(_message.Message):
    __slots__ = ("client_request_timestamp", "server_timestamp_ms")
    CLIENT_REQUEST_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    client_request_timestamp: int
    server_timestamp_ms: int
    def __init__(self, client_request_timestamp: _Optional[int] = ..., server_timestamp_ms: _Optional[int] = ...) -> None: ...

class CMsgClientSecret(_message.Message):
    __slots__ = ("version", "appid", "deviceid", "nonce", "hmac")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    HMAC_FIELD_NUMBER: _ClassVar[int]
    version: int
    appid: int
    deviceid: int
    nonce: int
    hmac: bytes
    def __init__(self, version: _Optional[int] = ..., appid: _Optional[int] = ..., deviceid: _Optional[int] = ..., nonce: _Optional[int] = ..., hmac: _Optional[bytes] = ...) -> None: ...

class CMsgClientHello(_message.Message):
    __slots__ = ("protocol_version",)
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    protocol_version: int
    def __init__(self, protocol_version: _Optional[int] = ...) -> None: ...

class CMsgClientLogon(_message.Message):
    __slots__ = ("protocol_version", "deprecated_obfustucated_private_ip", "cell_id", "last_session_id", "client_package_version", "client_language", "client_os_type", "should_remember_password", "wine_version", "deprecated_10", "obfuscated_private_ip", "deprecated_public_ip", "qos_level", "client_supplied_steam_id", "public_ip", "machine_id", "launcher_type", "ui_mode", "chat_mode", "steam2_auth_ticket", "email_address", "rtime32_account_creation", "account_name", "password", "game_server_token", "login_key", "was_converted_deprecated_msg", "anon_user_target_account_name", "resolved_user_steam_id", "eresult_sentryfile", "sha_sentryfile", "auth_code", "otp_type", "otp_value", "otp_identifier", "steam2_ticket_request", "sony_psn_ticket", "sony_psn_service_id", "create_new_psn_linked_account_if_needed", "sony_psn_name", "game_server_app_id", "steamguard_dont_remember_computer", "machine_name", "machine_name_userchosen", "country_override", "is_steam_box", "client_instance_id", "two_factor_code", "supports_rate_limit_response", "web_logon_nonce", "priority_reason", "embedded_client_secret", "disable_partner_autogrants", "is_steam_deck", "access_token", "is_chrome_os", "is_tesla")
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_OBFUSTUCATED_PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOULD_REMEMBER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    WINE_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_10_FIELD_NUMBER: _ClassVar[int]
    OBFUSCATED_PRIVATE_IP_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    QOS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPLIED_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LAUNCHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    UI_MODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_MODE_FIELD_NUMBER: _ClassVar[int]
    STEAM2_AUTH_TICKET_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RTIME32_ACCOUNT_CREATION_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOGIN_KEY_FIELD_NUMBER: _ClassVar[int]
    WAS_CONVERTED_DEPRECATED_MSG_FIELD_NUMBER: _ClassVar[int]
    ANON_USER_TARGET_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_USER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_SENTRYFILE_FIELD_NUMBER: _ClassVar[int]
    SHA_SENTRYFILE_FIELD_NUMBER: _ClassVar[int]
    AUTH_CODE_FIELD_NUMBER: _ClassVar[int]
    OTP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OTP_VALUE_FIELD_NUMBER: _ClassVar[int]
    OTP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    STEAM2_TICKET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SONY_PSN_TICKET_FIELD_NUMBER: _ClassVar[int]
    SONY_PSN_SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_PSN_LINKED_ACCOUNT_IF_NEEDED_FIELD_NUMBER: _ClassVar[int]
    SONY_PSN_NAME_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_DONT_REMEMBER_COMPUTER_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_NAME_USERCHOSEN_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    IS_STEAM_BOX_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_CODE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_RATE_LIMIT_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    WEB_LOGON_NONCE_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_REASON_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    DISABLE_PARTNER_AUTOGRANTS_FIELD_NUMBER: _ClassVar[int]
    IS_STEAM_DECK_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    IS_CHROME_OS_FIELD_NUMBER: _ClassVar[int]
    IS_TESLA_FIELD_NUMBER: _ClassVar[int]
    protocol_version: int
    deprecated_obfustucated_private_ip: int
    cell_id: int
    last_session_id: int
    client_package_version: int
    client_language: str
    client_os_type: int
    should_remember_password: bool
    wine_version: str
    deprecated_10: int
    obfuscated_private_ip: _steammessages_base_pb2.CMsgIPAddress
    deprecated_public_ip: int
    qos_level: int
    client_supplied_steam_id: int
    public_ip: _steammessages_base_pb2.CMsgIPAddress
    machine_id: bytes
    launcher_type: int
    ui_mode: int
    chat_mode: int
    steam2_auth_ticket: bytes
    email_address: str
    rtime32_account_creation: int
    account_name: str
    password: str
    game_server_token: str
    login_key: str
    was_converted_deprecated_msg: bool
    anon_user_target_account_name: str
    resolved_user_steam_id: int
    eresult_sentryfile: int
    sha_sentryfile: bytes
    auth_code: str
    otp_type: int
    otp_value: int
    otp_identifier: str
    steam2_ticket_request: bool
    sony_psn_ticket: bytes
    sony_psn_service_id: str
    create_new_psn_linked_account_if_needed: bool
    sony_psn_name: str
    game_server_app_id: int
    steamguard_dont_remember_computer: bool
    machine_name: str
    machine_name_userchosen: str
    country_override: str
    is_steam_box: bool
    client_instance_id: int
    two_factor_code: str
    supports_rate_limit_response: bool
    web_logon_nonce: str
    priority_reason: int
    embedded_client_secret: CMsgClientSecret
    disable_partner_autogrants: bool
    is_steam_deck: bool
    access_token: str
    is_chrome_os: bool
    is_tesla: bool
    def __init__(self, protocol_version: _Optional[int] = ..., deprecated_obfustucated_private_ip: _Optional[int] = ..., cell_id: _Optional[int] = ..., last_session_id: _Optional[int] = ..., client_package_version: _Optional[int] = ..., client_language: _Optional[str] = ..., client_os_type: _Optional[int] = ..., should_remember_password: bool = ..., wine_version: _Optional[str] = ..., deprecated_10: _Optional[int] = ..., obfuscated_private_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., deprecated_public_ip: _Optional[int] = ..., qos_level: _Optional[int] = ..., client_supplied_steam_id: _Optional[int] = ..., public_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., machine_id: _Optional[bytes] = ..., launcher_type: _Optional[int] = ..., ui_mode: _Optional[int] = ..., chat_mode: _Optional[int] = ..., steam2_auth_ticket: _Optional[bytes] = ..., email_address: _Optional[str] = ..., rtime32_account_creation: _Optional[int] = ..., account_name: _Optional[str] = ..., password: _Optional[str] = ..., game_server_token: _Optional[str] = ..., login_key: _Optional[str] = ..., was_converted_deprecated_msg: bool = ..., anon_user_target_account_name: _Optional[str] = ..., resolved_user_steam_id: _Optional[int] = ..., eresult_sentryfile: _Optional[int] = ..., sha_sentryfile: _Optional[bytes] = ..., auth_code: _Optional[str] = ..., otp_type: _Optional[int] = ..., otp_value: _Optional[int] = ..., otp_identifier: _Optional[str] = ..., steam2_ticket_request: bool = ..., sony_psn_ticket: _Optional[bytes] = ..., sony_psn_service_id: _Optional[str] = ..., create_new_psn_linked_account_if_needed: bool = ..., sony_psn_name: _Optional[str] = ..., game_server_app_id: _Optional[int] = ..., steamguard_dont_remember_computer: bool = ..., machine_name: _Optional[str] = ..., machine_name_userchosen: _Optional[str] = ..., country_override: _Optional[str] = ..., is_steam_box: bool = ..., client_instance_id: _Optional[int] = ..., two_factor_code: _Optional[str] = ..., supports_rate_limit_response: bool = ..., web_logon_nonce: _Optional[str] = ..., priority_reason: _Optional[int] = ..., embedded_client_secret: _Optional[_Union[CMsgClientSecret, _Mapping]] = ..., disable_partner_autogrants: bool = ..., is_steam_deck: bool = ..., access_token: _Optional[str] = ..., is_chrome_os: bool = ..., is_tesla: bool = ...) -> None: ...

class CMsgClientLogonResponse(_message.Message):
    __slots__ = ("eresult", "legacy_out_of_game_heartbeat_seconds", "heartbeat_seconds", "deprecated_public_ip", "rtime32_server_time", "account_flags", "cell_id", "email_domain", "steam2_ticket", "eresult_extended", "cell_id_ping_threshold", "deprecated_use_pics", "vanity_url", "public_ip", "user_country", "client_supplied_steamid", "ip_country_code", "parental_settings", "parental_setting_signature", "count_loginfailures_to_migrate", "count_disconnects_to_migrate", "ogs_data_report_time_window", "client_instance_id", "force_client_update_check", "agreement_session_url", "token_id", "family_group_id")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    LEGACY_OUT_OF_GAME_HEARTBEAT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    RTIME32_SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    STEAM2_TICKET_FIELD_NUMBER: _ClassVar[int]
    ERESULT_EXTENDED_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_PING_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_USE_PICS_FIELD_NUMBER: _ClassVar[int]
    VANITY_URL_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    USER_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SUPPLIED_STEAMID_FIELD_NUMBER: _ClassVar[int]
    IP_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_SETTING_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    COUNT_LOGINFAILURES_TO_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_DISCONNECTS_TO_MIGRATE_FIELD_NUMBER: _ClassVar[int]
    OGS_DATA_REPORT_TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_CLIENT_UPDATE_CHECK_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_SESSION_URL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    legacy_out_of_game_heartbeat_seconds: int
    heartbeat_seconds: int
    deprecated_public_ip: int
    rtime32_server_time: int
    account_flags: int
    cell_id: int
    email_domain: str
    steam2_ticket: bytes
    eresult_extended: int
    cell_id_ping_threshold: int
    deprecated_use_pics: bool
    vanity_url: str
    public_ip: _steammessages_base_pb2.CMsgIPAddress
    user_country: str
    client_supplied_steamid: int
    ip_country_code: str
    parental_settings: bytes
    parental_setting_signature: bytes
    count_loginfailures_to_migrate: int
    count_disconnects_to_migrate: int
    ogs_data_report_time_window: int
    client_instance_id: int
    force_client_update_check: bool
    agreement_session_url: str
    token_id: int
    family_group_id: int
    def __init__(self, eresult: _Optional[int] = ..., legacy_out_of_game_heartbeat_seconds: _Optional[int] = ..., heartbeat_seconds: _Optional[int] = ..., deprecated_public_ip: _Optional[int] = ..., rtime32_server_time: _Optional[int] = ..., account_flags: _Optional[int] = ..., cell_id: _Optional[int] = ..., email_domain: _Optional[str] = ..., steam2_ticket: _Optional[bytes] = ..., eresult_extended: _Optional[int] = ..., cell_id_ping_threshold: _Optional[int] = ..., deprecated_use_pics: bool = ..., vanity_url: _Optional[str] = ..., public_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., user_country: _Optional[str] = ..., client_supplied_steamid: _Optional[int] = ..., ip_country_code: _Optional[str] = ..., parental_settings: _Optional[bytes] = ..., parental_setting_signature: _Optional[bytes] = ..., count_loginfailures_to_migrate: _Optional[int] = ..., count_disconnects_to_migrate: _Optional[int] = ..., ogs_data_report_time_window: _Optional[int] = ..., client_instance_id: _Optional[int] = ..., force_client_update_check: bool = ..., agreement_session_url: _Optional[str] = ..., token_id: _Optional[int] = ..., family_group_id: _Optional[int] = ...) -> None: ...

class CMsgClientRequestWebAPIAuthenticateUserNonce(_message.Message):
    __slots__ = ("token_type",)
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    token_type: int
    def __init__(self, token_type: _Optional[int] = ...) -> None: ...

class CMsgClientRequestWebAPIAuthenticateUserNonceResponse(_message.Message):
    __slots__ = ("eresult", "webapi_authenticate_user_nonce", "token_type")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    WEBAPI_AUTHENTICATE_USER_NONCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    webapi_authenticate_user_nonce: str
    token_type: int
    def __init__(self, eresult: _Optional[int] = ..., webapi_authenticate_user_nonce: _Optional[str] = ..., token_type: _Optional[int] = ...) -> None: ...

class CMsgClientLogOff(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientLoggedOff(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientNewLoginKey(_message.Message):
    __slots__ = ("unique_id", "login_key")
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_KEY_FIELD_NUMBER: _ClassVar[int]
    unique_id: int
    login_key: str
    def __init__(self, unique_id: _Optional[int] = ..., login_key: _Optional[str] = ...) -> None: ...

class CMsgClientNewLoginKeyAccepted(_message.Message):
    __slots__ = ("unique_id",)
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    unique_id: int
    def __init__(self, unique_id: _Optional[int] = ...) -> None: ...

class CMsgClientAccountInfo(_message.Message):
    __slots__ = ("persona_name", "ip_country", "count_authed_computers", "account_flags", "facebook_id", "facebook_name", "steamguard_machine_name_user_chosen", "is_phone_verified", "two_factor_state", "is_phone_identifying", "is_phone_needing_reverify")
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    COUNT_AUTHED_COMPUTERS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    FACEBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    FACEBOOK_NAME_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_MACHINE_NAME_USER_CHOSEN_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_IDENTIFYING_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_NEEDING_REVERIFY_FIELD_NUMBER: _ClassVar[int]
    persona_name: str
    ip_country: str
    count_authed_computers: int
    account_flags: int
    facebook_id: int
    facebook_name: str
    steamguard_machine_name_user_chosen: str
    is_phone_verified: bool
    two_factor_state: int
    is_phone_identifying: bool
    is_phone_needing_reverify: bool
    def __init__(self, persona_name: _Optional[str] = ..., ip_country: _Optional[str] = ..., count_authed_computers: _Optional[int] = ..., account_flags: _Optional[int] = ..., facebook_id: _Optional[int] = ..., facebook_name: _Optional[str] = ..., steamguard_machine_name_user_chosen: _Optional[str] = ..., is_phone_verified: bool = ..., two_factor_state: _Optional[int] = ..., is_phone_identifying: bool = ..., is_phone_needing_reverify: bool = ...) -> None: ...

class CMsgClientChallengeRequest(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgClientChallengeResponse(_message.Message):
    __slots__ = ("challenge",)
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    challenge: int
    def __init__(self, challenge: _Optional[int] = ...) -> None: ...
