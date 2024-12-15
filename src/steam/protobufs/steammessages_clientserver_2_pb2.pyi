import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientUpdateUserGameInfo(_message.Message):
    __slots__ = ("steamid_idgs", "gameid", "game_ip", "game_port", "token")
    STEAMID_IDGS_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAME_IP_FIELD_NUMBER: _ClassVar[int]
    GAME_PORT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    steamid_idgs: int
    gameid: int
    game_ip: int
    game_port: int
    token: bytes
    def __init__(self, steamid_idgs: _Optional[int] = ..., gameid: _Optional[int] = ..., game_ip: _Optional[int] = ..., game_port: _Optional[int] = ..., token: _Optional[bytes] = ...) -> None: ...

class CMsgClientRichPresenceUpload(_message.Message):
    __slots__ = ("rich_presence_kv", "steamid_broadcast")
    RICH_PRESENCE_KV_FIELD_NUMBER: _ClassVar[int]
    STEAMID_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    rich_presence_kv: bytes
    steamid_broadcast: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, rich_presence_kv: _Optional[bytes] = ..., steamid_broadcast: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientRichPresenceRequest(_message.Message):
    __slots__ = ("steamid_request",)
    STEAMID_REQUEST_FIELD_NUMBER: _ClassVar[int]
    steamid_request: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid_request: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientRichPresenceInfo(_message.Message):
    __slots__ = ("rich_presence",)
    class RichPresence(_message.Message):
        __slots__ = ("steamid_user", "rich_presence_kv")
        STEAMID_USER_FIELD_NUMBER: _ClassVar[int]
        RICH_PRESENCE_KV_FIELD_NUMBER: _ClassVar[int]
        steamid_user: int
        rich_presence_kv: bytes
        def __init__(self, steamid_user: _Optional[int] = ..., rich_presence_kv: _Optional[bytes] = ...) -> None: ...
    RICH_PRESENCE_FIELD_NUMBER: _ClassVar[int]
    rich_presence: _containers.RepeatedCompositeFieldContainer[CMsgClientRichPresenceInfo.RichPresence]
    def __init__(self, rich_presence: _Optional[_Iterable[_Union[CMsgClientRichPresenceInfo.RichPresence, _Mapping]]] = ...) -> None: ...

class CMsgClientCheckFileSignature(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    def __init__(self, app_id: _Optional[int] = ...) -> None: ...

class CMsgClientCheckFileSignatureResponse(_message.Message):
    __slots__ = ("app_id", "pid", "eresult", "filename", "esignatureresult", "sha_file", "signatureheader", "filesize", "getlasterror", "evalvesignaturecheckdetail")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ESIGNATURERESULT_FIELD_NUMBER: _ClassVar[int]
    SHA_FILE_FIELD_NUMBER: _ClassVar[int]
    SIGNATUREHEADER_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    GETLASTERROR_FIELD_NUMBER: _ClassVar[int]
    EVALVESIGNATURECHECKDETAIL_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    pid: int
    eresult: int
    filename: str
    esignatureresult: int
    sha_file: bytes
    signatureheader: bytes
    filesize: int
    getlasterror: int
    evalvesignaturecheckdetail: int
    def __init__(self, app_id: _Optional[int] = ..., pid: _Optional[int] = ..., eresult: _Optional[int] = ..., filename: _Optional[str] = ..., esignatureresult: _Optional[int] = ..., sha_file: _Optional[bytes] = ..., signatureheader: _Optional[bytes] = ..., filesize: _Optional[int] = ..., getlasterror: _Optional[int] = ..., evalvesignaturecheckdetail: _Optional[int] = ...) -> None: ...

class CMsgClientReadMachineAuth(_message.Message):
    __slots__ = ("filename", "offset", "cubtoread")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CUBTOREAD_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    cubtoread: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., cubtoread: _Optional[int] = ...) -> None: ...

class CMsgClientReadMachineAuthResponse(_message.Message):
    __slots__ = ("filename", "eresult", "filesize", "sha_file", "getlasterror", "offset", "cubread", "bytes_read", "filename_sentry")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    SHA_FILE_FIELD_NUMBER: _ClassVar[int]
    GETLASTERROR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CUBREAD_FIELD_NUMBER: _ClassVar[int]
    BYTES_READ_FIELD_NUMBER: _ClassVar[int]
    FILENAME_SENTRY_FIELD_NUMBER: _ClassVar[int]
    filename: str
    eresult: int
    filesize: int
    sha_file: bytes
    getlasterror: int
    offset: int
    cubread: int
    bytes_read: bytes
    filename_sentry: str
    def __init__(self, filename: _Optional[str] = ..., eresult: _Optional[int] = ..., filesize: _Optional[int] = ..., sha_file: _Optional[bytes] = ..., getlasterror: _Optional[int] = ..., offset: _Optional[int] = ..., cubread: _Optional[int] = ..., bytes_read: _Optional[bytes] = ..., filename_sentry: _Optional[str] = ...) -> None: ...

class CMsgClientUpdateMachineAuth(_message.Message):
    __slots__ = ("filename", "offset", "cubtowrite", "bytes", "otp_type", "otp_identifier", "otp_sharedsecret", "otp_timedrift")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CUBTOWRITE_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    OTP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OTP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    OTP_SHAREDSECRET_FIELD_NUMBER: _ClassVar[int]
    OTP_TIMEDRIFT_FIELD_NUMBER: _ClassVar[int]
    filename: str
    offset: int
    cubtowrite: int
    bytes: bytes
    otp_type: int
    otp_identifier: str
    otp_sharedsecret: bytes
    otp_timedrift: int
    def __init__(self, filename: _Optional[str] = ..., offset: _Optional[int] = ..., cubtowrite: _Optional[int] = ..., bytes: _Optional[bytes] = ..., otp_type: _Optional[int] = ..., otp_identifier: _Optional[str] = ..., otp_sharedsecret: _Optional[bytes] = ..., otp_timedrift: _Optional[int] = ...) -> None: ...

class CMsgClientUpdateMachineAuthResponse(_message.Message):
    __slots__ = ("filename", "eresult", "filesize", "sha_file", "getlasterror", "offset", "cubwrote", "otp_type", "otp_value", "otp_identifier")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    SHA_FILE_FIELD_NUMBER: _ClassVar[int]
    GETLASTERROR_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    CUBWROTE_FIELD_NUMBER: _ClassVar[int]
    OTP_TYPE_FIELD_NUMBER: _ClassVar[int]
    OTP_VALUE_FIELD_NUMBER: _ClassVar[int]
    OTP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    filename: str
    eresult: int
    filesize: int
    sha_file: bytes
    getlasterror: int
    offset: int
    cubwrote: int
    otp_type: int
    otp_value: int
    otp_identifier: str
    def __init__(self, filename: _Optional[str] = ..., eresult: _Optional[int] = ..., filesize: _Optional[int] = ..., sha_file: _Optional[bytes] = ..., getlasterror: _Optional[int] = ..., offset: _Optional[int] = ..., cubwrote: _Optional[int] = ..., otp_type: _Optional[int] = ..., otp_value: _Optional[int] = ..., otp_identifier: _Optional[str] = ...) -> None: ...

class CMsgClientRegisterKey(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class CMsgClientPurchaseResponse(_message.Message):
    __slots__ = ("eresult", "purchase_result_details", "purchase_receipt_info")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RESULT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RECEIPT_INFO_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    purchase_result_details: int
    purchase_receipt_info: bytes
    def __init__(self, eresult: _Optional[int] = ..., purchase_result_details: _Optional[int] = ..., purchase_receipt_info: _Optional[bytes] = ...) -> None: ...

class CMsgClientActivateOEMLicense(_message.Message):
    __slots__ = ("bios_manufacturer", "bios_serialnumber", "license_file", "mainboard_manufacturer", "mainboard_product", "mainboard_serialnumber")
    BIOS_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    BIOS_SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    LICENSE_FILE_FIELD_NUMBER: _ClassVar[int]
    MAINBOARD_MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MAINBOARD_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    MAINBOARD_SERIALNUMBER_FIELD_NUMBER: _ClassVar[int]
    bios_manufacturer: str
    bios_serialnumber: str
    license_file: bytes
    mainboard_manufacturer: str
    mainboard_product: str
    mainboard_serialnumber: str
    def __init__(self, bios_manufacturer: _Optional[str] = ..., bios_serialnumber: _Optional[str] = ..., license_file: _Optional[bytes] = ..., mainboard_manufacturer: _Optional[str] = ..., mainboard_product: _Optional[str] = ..., mainboard_serialnumber: _Optional[str] = ...) -> None: ...

class CMsgClientRegisterOEMMachine(_message.Message):
    __slots__ = ("oem_register_file",)
    OEM_REGISTER_FILE_FIELD_NUMBER: _ClassVar[int]
    oem_register_file: bytes
    def __init__(self, oem_register_file: _Optional[bytes] = ...) -> None: ...

class CMsgClientRegisterOEMMachineResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientPurchaseWithMachineID(_message.Message):
    __slots__ = ("package_id", "machine_info")
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MACHINE_INFO_FIELD_NUMBER: _ClassVar[int]
    package_id: int
    machine_info: bytes
    def __init__(self, package_id: _Optional[int] = ..., machine_info: _Optional[bytes] = ...) -> None: ...

class CMsgTrading_InitiateTradeRequest(_message.Message):
    __slots__ = ("trade_request_id", "other_steamid", "other_name")
    TRADE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    OTHER_NAME_FIELD_NUMBER: _ClassVar[int]
    trade_request_id: int
    other_steamid: int
    other_name: str
    def __init__(self, trade_request_id: _Optional[int] = ..., other_steamid: _Optional[int] = ..., other_name: _Optional[str] = ...) -> None: ...

class CMsgTrading_InitiateTradeResponse(_message.Message):
    __slots__ = ("response", "trade_request_id", "other_steamid", "steamguard_required_days", "new_device_cooldown_days", "default_password_reset_probation_days", "password_reset_probation_days", "default_email_change_probation_days", "email_change_probation_days")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TRADE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    OTHER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_REQUIRED_DAYS_FIELD_NUMBER: _ClassVar[int]
    NEW_DEVICE_COOLDOWN_DAYS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PASSWORD_RESET_PROBATION_DAYS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_RESET_PROBATION_DAYS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_EMAIL_CHANGE_PROBATION_DAYS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_CHANGE_PROBATION_DAYS_FIELD_NUMBER: _ClassVar[int]
    response: int
    trade_request_id: int
    other_steamid: int
    steamguard_required_days: int
    new_device_cooldown_days: int
    default_password_reset_probation_days: int
    password_reset_probation_days: int
    default_email_change_probation_days: int
    email_change_probation_days: int
    def __init__(self, response: _Optional[int] = ..., trade_request_id: _Optional[int] = ..., other_steamid: _Optional[int] = ..., steamguard_required_days: _Optional[int] = ..., new_device_cooldown_days: _Optional[int] = ..., default_password_reset_probation_days: _Optional[int] = ..., password_reset_probation_days: _Optional[int] = ..., default_email_change_probation_days: _Optional[int] = ..., email_change_probation_days: _Optional[int] = ...) -> None: ...

class CMsgTrading_CancelTradeRequest(_message.Message):
    __slots__ = ("other_steamid",)
    OTHER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    other_steamid: int
    def __init__(self, other_steamid: _Optional[int] = ...) -> None: ...

class CMsgTrading_StartSession(_message.Message):
    __slots__ = ("other_steamid",)
    OTHER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    other_steamid: int
    def __init__(self, other_steamid: _Optional[int] = ...) -> None: ...

class CMsgClientGetDepotDecryptionKey(_message.Message):
    __slots__ = ("depot_id", "app_id")
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    depot_id: int
    app_id: int
    def __init__(self, depot_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class CMsgClientGetDepotDecryptionKeyResponse(_message.Message):
    __slots__ = ("eresult", "depot_id", "depot_encryption_key")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    depot_id: int
    depot_encryption_key: bytes
    def __init__(self, eresult: _Optional[int] = ..., depot_id: _Optional[int] = ..., depot_encryption_key: _Optional[bytes] = ...) -> None: ...

class CMsgClientCheckAppBetaPassword(_message.Message):
    __slots__ = ("app_id", "betapassword", "language")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    BETAPASSWORD_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    betapassword: str
    language: int
    def __init__(self, app_id: _Optional[int] = ..., betapassword: _Optional[str] = ..., language: _Optional[int] = ...) -> None: ...

class CMsgClientCheckAppBetaPasswordResponse(_message.Message):
    __slots__ = ("eresult", "betapasswords")
    class BetaPassword(_message.Message):
        __slots__ = ("betaname", "betapassword", "betadescription")
        BETANAME_FIELD_NUMBER: _ClassVar[int]
        BETAPASSWORD_FIELD_NUMBER: _ClassVar[int]
        BETADESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        betaname: str
        betapassword: str
        betadescription: str
        def __init__(self, betaname: _Optional[str] = ..., betapassword: _Optional[str] = ..., betadescription: _Optional[str] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    BETAPASSWORDS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    betapasswords: _containers.RepeatedCompositeFieldContainer[CMsgClientCheckAppBetaPasswordResponse.BetaPassword]
    def __init__(self, eresult: _Optional[int] = ..., betapasswords: _Optional[_Iterable[_Union[CMsgClientCheckAppBetaPasswordResponse.BetaPassword, _Mapping]]] = ...) -> None: ...

class CMsgClientUGSGetGlobalStats(_message.Message):
    __slots__ = ("gameid", "history_days_requested", "time_last_requested", "first_day_cached", "days_cached")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_DAYS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    FIRST_DAY_CACHED_FIELD_NUMBER: _ClassVar[int]
    DAYS_CACHED_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    history_days_requested: int
    time_last_requested: int
    first_day_cached: int
    days_cached: int
    def __init__(self, gameid: _Optional[int] = ..., history_days_requested: _Optional[int] = ..., time_last_requested: _Optional[int] = ..., first_day_cached: _Optional[int] = ..., days_cached: _Optional[int] = ...) -> None: ...

class CMsgClientUGSGetGlobalStatsResponse(_message.Message):
    __slots__ = ("eresult", "timestamp", "day_current", "days")
    class Day(_message.Message):
        __slots__ = ("day_id", "stats")
        class Stat(_message.Message):
            __slots__ = ("stat_id", "data")
            STAT_ID_FIELD_NUMBER: _ClassVar[int]
            DATA_FIELD_NUMBER: _ClassVar[int]
            stat_id: int
            data: int
            def __init__(self, stat_id: _Optional[int] = ..., data: _Optional[int] = ...) -> None: ...
        DAY_ID_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        day_id: int
        stats: _containers.RepeatedCompositeFieldContainer[CMsgClientUGSGetGlobalStatsResponse.Day.Stat]
        def __init__(self, day_id: _Optional[int] = ..., stats: _Optional[_Iterable[_Union[CMsgClientUGSGetGlobalStatsResponse.Day.Stat, _Mapping]]] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DAY_CURRENT_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    timestamp: int
    day_current: int
    days: _containers.RepeatedCompositeFieldContainer[CMsgClientUGSGetGlobalStatsResponse.Day]
    def __init__(self, eresult: _Optional[int] = ..., timestamp: _Optional[int] = ..., day_current: _Optional[int] = ..., days: _Optional[_Iterable[_Union[CMsgClientUGSGetGlobalStatsResponse.Day, _Mapping]]] = ...) -> None: ...

class CMsgClientRedeemGuestPass(_message.Message):
    __slots__ = ("guest_pass_id",)
    GUEST_PASS_ID_FIELD_NUMBER: _ClassVar[int]
    guest_pass_id: int
    def __init__(self, guest_pass_id: _Optional[int] = ...) -> None: ...

class CMsgClientRedeemGuestPassResponse(_message.Message):
    __slots__ = ("eresult", "package_id", "must_own_appid")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    MUST_OWN_APPID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    package_id: int
    must_own_appid: int
    def __init__(self, eresult: _Optional[int] = ..., package_id: _Optional[int] = ..., must_own_appid: _Optional[int] = ...) -> None: ...

class CMsgClientGetClanActivityCounts(_message.Message):
    __slots__ = ("steamid_clans",)
    STEAMID_CLANS_FIELD_NUMBER: _ClassVar[int]
    steamid_clans: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid_clans: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientGetClanActivityCountsResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientOGSReportString(_message.Message):
    __slots__ = ("accumulated", "sessionid", "severity", "formatter", "varargs")
    ACCUMULATED_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    VARARGS_FIELD_NUMBER: _ClassVar[int]
    accumulated: bool
    sessionid: int
    severity: int
    formatter: str
    varargs: bytes
    def __init__(self, accumulated: bool = ..., sessionid: _Optional[int] = ..., severity: _Optional[int] = ..., formatter: _Optional[str] = ..., varargs: _Optional[bytes] = ...) -> None: ...

class CMsgClientOGSReportBug(_message.Message):
    __slots__ = ("sessionid", "bugtext", "screenshot")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    BUGTEXT_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    sessionid: int
    bugtext: str
    screenshot: bytes
    def __init__(self, sessionid: _Optional[int] = ..., bugtext: _Optional[str] = ..., screenshot: _Optional[bytes] = ...) -> None: ...

class CMsgClientSentLogs(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgGCClient(_message.Message):
    __slots__ = ("appid", "msgtype", "payload", "steamid", "gcname", "ip")
    APPID_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GCNAME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    appid: int
    msgtype: int
    payload: bytes
    steamid: int
    gcname: str
    ip: int
    def __init__(self, appid: _Optional[int] = ..., msgtype: _Optional[int] = ..., payload: _Optional[bytes] = ..., steamid: _Optional[int] = ..., gcname: _Optional[str] = ..., ip: _Optional[int] = ...) -> None: ...

class CMsgClientRequestFreeLicense(_message.Message):
    __slots__ = ("appids",)
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientRequestFreeLicenseResponse(_message.Message):
    __slots__ = ("eresult", "granted_packageids", "granted_appids")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    GRANTED_PACKAGEIDS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_APPIDS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    granted_packageids: _containers.RepeatedScalarFieldContainer[int]
    granted_appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, eresult: _Optional[int] = ..., granted_packageids: _Optional[_Iterable[int]] = ..., granted_appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgDRMDownloadRequestWithCrashData(_message.Message):
    __slots__ = ("download_flags", "download_types_known", "guid_drm", "guid_split", "guid_merge", "module_name", "module_path", "crash_data")
    DOWNLOAD_FLAGS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_TYPES_KNOWN_FIELD_NUMBER: _ClassVar[int]
    GUID_DRM_FIELD_NUMBER: _ClassVar[int]
    GUID_SPLIT_FIELD_NUMBER: _ClassVar[int]
    GUID_MERGE_FIELD_NUMBER: _ClassVar[int]
    MODULE_NAME_FIELD_NUMBER: _ClassVar[int]
    MODULE_PATH_FIELD_NUMBER: _ClassVar[int]
    CRASH_DATA_FIELD_NUMBER: _ClassVar[int]
    download_flags: int
    download_types_known: int
    guid_drm: bytes
    guid_split: bytes
    guid_merge: bytes
    module_name: str
    module_path: str
    crash_data: bytes
    def __init__(self, download_flags: _Optional[int] = ..., download_types_known: _Optional[int] = ..., guid_drm: _Optional[bytes] = ..., guid_split: _Optional[bytes] = ..., guid_merge: _Optional[bytes] = ..., module_name: _Optional[str] = ..., module_path: _Optional[str] = ..., crash_data: _Optional[bytes] = ...) -> None: ...

class CMsgDRMDownloadResponse(_message.Message):
    __slots__ = ("eresult", "app_id", "blob_download_type", "merge_guid", "download_file_dfs_ip", "download_file_dfs_port", "download_file_url", "module_path")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_DOWNLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    MERGE_GUID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_DFS_IP_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_DFS_PORT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    MODULE_PATH_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    app_id: int
    blob_download_type: int
    merge_guid: bytes
    download_file_dfs_ip: int
    download_file_dfs_port: int
    download_file_url: str
    module_path: str
    def __init__(self, eresult: _Optional[int] = ..., app_id: _Optional[int] = ..., blob_download_type: _Optional[int] = ..., merge_guid: _Optional[bytes] = ..., download_file_dfs_ip: _Optional[int] = ..., download_file_dfs_port: _Optional[int] = ..., download_file_url: _Optional[str] = ..., module_path: _Optional[str] = ...) -> None: ...

class CMsgDRMFinalResult(_message.Message):
    __slots__ = ("eResult", "app_id", "blob_download_type", "error_detail", "merge_guid", "download_file_dfs_ip", "download_file_dfs_port", "download_file_url")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    BLOB_DOWNLOAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAIL_FIELD_NUMBER: _ClassVar[int]
    MERGE_GUID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_DFS_IP_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_DFS_PORT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FILE_URL_FIELD_NUMBER: _ClassVar[int]
    eResult: int
    app_id: int
    blob_download_type: int
    error_detail: int
    merge_guid: bytes
    download_file_dfs_ip: int
    download_file_dfs_port: int
    download_file_url: str
    def __init__(self, eResult: _Optional[int] = ..., app_id: _Optional[int] = ..., blob_download_type: _Optional[int] = ..., error_detail: _Optional[int] = ..., merge_guid: _Optional[bytes] = ..., download_file_dfs_ip: _Optional[int] = ..., download_file_dfs_port: _Optional[int] = ..., download_file_url: _Optional[str] = ...) -> None: ...

class CMsgClientDPCheckSpecialSurvey(_message.Message):
    __slots__ = ("survey_id",)
    SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
    survey_id: int
    def __init__(self, survey_id: _Optional[int] = ...) -> None: ...

class CMsgClientDPCheckSpecialSurveyResponse(_message.Message):
    __slots__ = ("eResult", "state", "name", "custom_url", "include_software", "token")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_URL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SOFTWARE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    eResult: int
    state: int
    name: str
    custom_url: str
    include_software: bool
    token: bytes
    def __init__(self, eResult: _Optional[int] = ..., state: _Optional[int] = ..., name: _Optional[str] = ..., custom_url: _Optional[str] = ..., include_software: bool = ..., token: _Optional[bytes] = ...) -> None: ...

class CMsgClientDPSendSpecialSurveyResponse(_message.Message):
    __slots__ = ("survey_id", "data")
    SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    survey_id: int
    data: bytes
    def __init__(self, survey_id: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class CMsgClientDPSendSpecialSurveyResponseReply(_message.Message):
    __slots__ = ("eResult", "token")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    eResult: int
    token: bytes
    def __init__(self, eResult: _Optional[int] = ..., token: _Optional[bytes] = ...) -> None: ...

class CMsgClientRequestForgottenPasswordEmail(_message.Message):
    __slots__ = ("account_name", "password_tried")
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_TRIED_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    password_tried: str
    def __init__(self, account_name: _Optional[str] = ..., password_tried: _Optional[str] = ...) -> None: ...

class CMsgClientRequestForgottenPasswordEmailResponse(_message.Message):
    __slots__ = ("eResult", "use_secret_question")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    USE_SECRET_QUESTION_FIELD_NUMBER: _ClassVar[int]
    eResult: int
    use_secret_question: bool
    def __init__(self, eResult: _Optional[int] = ..., use_secret_question: bool = ...) -> None: ...

class CMsgClientItemAnnouncements(_message.Message):
    __slots__ = ("count_new_items", "unseen_items")
    class UnseenItem(_message.Message):
        __slots__ = ("appid", "context_id", "asset_id", "amount", "rtime32_gained", "source_appid")
        APPID_FIELD_NUMBER: _ClassVar[int]
        CONTEXT_ID_FIELD_NUMBER: _ClassVar[int]
        ASSET_ID_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        RTIME32_GAINED_FIELD_NUMBER: _ClassVar[int]
        SOURCE_APPID_FIELD_NUMBER: _ClassVar[int]
        appid: int
        context_id: int
        asset_id: int
        amount: int
        rtime32_gained: int
        source_appid: int
        def __init__(self, appid: _Optional[int] = ..., context_id: _Optional[int] = ..., asset_id: _Optional[int] = ..., amount: _Optional[int] = ..., rtime32_gained: _Optional[int] = ..., source_appid: _Optional[int] = ...) -> None: ...
    COUNT_NEW_ITEMS_FIELD_NUMBER: _ClassVar[int]
    UNSEEN_ITEMS_FIELD_NUMBER: _ClassVar[int]
    count_new_items: int
    unseen_items: _containers.RepeatedCompositeFieldContainer[CMsgClientItemAnnouncements.UnseenItem]
    def __init__(self, count_new_items: _Optional[int] = ..., unseen_items: _Optional[_Iterable[_Union[CMsgClientItemAnnouncements.UnseenItem, _Mapping]]] = ...) -> None: ...

class CMsgClientRequestItemAnnouncements(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientUserNotifications(_message.Message):
    __slots__ = ("notifications",)
    class Notification(_message.Message):
        __slots__ = ("user_notification_type", "count")
        USER_NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        user_notification_type: int
        count: int
        def __init__(self, user_notification_type: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[CMsgClientUserNotifications.Notification]
    def __init__(self, notifications: _Optional[_Iterable[_Union[CMsgClientUserNotifications.Notification, _Mapping]]] = ...) -> None: ...

class CMsgClientCommentNotifications(_message.Message):
    __slots__ = ("count_new_comments", "count_new_comments_owner", "count_new_comments_subscriptions")
    COUNT_NEW_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    COUNT_NEW_COMMENTS_OWNER_FIELD_NUMBER: _ClassVar[int]
    COUNT_NEW_COMMENTS_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    count_new_comments: int
    count_new_comments_owner: int
    count_new_comments_subscriptions: int
    def __init__(self, count_new_comments: _Optional[int] = ..., count_new_comments_owner: _Optional[int] = ..., count_new_comments_subscriptions: _Optional[int] = ...) -> None: ...

class CMsgClientRequestCommentNotifications(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientOfflineMessageNotification(_message.Message):
    __slots__ = ("offline_messages", "friends_with_offline_messages")
    OFFLINE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_WITH_OFFLINE_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    offline_messages: int
    friends_with_offline_messages: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, offline_messages: _Optional[int] = ..., friends_with_offline_messages: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientRequestOfflineMessageCount(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientChatGetFriendMessageHistory(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CMsgClientChatGetFriendMessageHistoryResponse(_message.Message):
    __slots__ = ("steamid", "success", "messages")
    class FriendMessage(_message.Message):
        __slots__ = ("accountid", "timestamp", "message", "unread")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        UNREAD_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        timestamp: int
        message: str
        unread: bool
        def __init__(self, accountid: _Optional[int] = ..., timestamp: _Optional[int] = ..., message: _Optional[str] = ..., unread: bool = ...) -> None: ...
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    success: int
    messages: _containers.RepeatedCompositeFieldContainer[CMsgClientChatGetFriendMessageHistoryResponse.FriendMessage]
    def __init__(self, steamid: _Optional[int] = ..., success: _Optional[int] = ..., messages: _Optional[_Iterable[_Union[CMsgClientChatGetFriendMessageHistoryResponse.FriendMessage, _Mapping]]] = ...) -> None: ...

class CMsgClientChatGetFriendMessageHistoryForOfflineMessages(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientFSGetFriendsSteamLevels(_message.Message):
    __slots__ = ("accountids",)
    ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    accountids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, accountids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientFSGetFriendsSteamLevelsResponse(_message.Message):
    __slots__ = ("friends",)
    class Friend(_message.Message):
        __slots__ = ("accountid", "level")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        level: int
        def __init__(self, accountid: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    friends: _containers.RepeatedCompositeFieldContainer[CMsgClientFSGetFriendsSteamLevelsResponse.Friend]
    def __init__(self, friends: _Optional[_Iterable[_Union[CMsgClientFSGetFriendsSteamLevelsResponse.Friend, _Mapping]]] = ...) -> None: ...

class CMsgClientEmailAddrInfo(_message.Message):
    __slots__ = ("email_address", "email_is_validated", "email_validation_changed", "credential_change_requires_code", "password_or_secretqa_change_requires_code")
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_IS_VALIDATED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VALIDATION_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_CHANGE_REQUIRES_CODE_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_OR_SECRETQA_CHANGE_REQUIRES_CODE_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    email_is_validated: bool
    email_validation_changed: bool
    credential_change_requires_code: bool
    password_or_secretqa_change_requires_code: bool
    def __init__(self, email_address: _Optional[str] = ..., email_is_validated: bool = ..., email_validation_changed: bool = ..., credential_change_requires_code: bool = ..., password_or_secretqa_change_requires_code: bool = ...) -> None: ...

class CMsgCREItemVoteSummary(_message.Message):
    __slots__ = ("published_file_ids",)
    class PublishedFileId(_message.Message):
        __slots__ = ("published_file_id",)
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        def __init__(self, published_file_id: _Optional[int] = ...) -> None: ...
    PUBLISHED_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    published_file_ids: _containers.RepeatedCompositeFieldContainer[CMsgCREItemVoteSummary.PublishedFileId]
    def __init__(self, published_file_ids: _Optional[_Iterable[_Union[CMsgCREItemVoteSummary.PublishedFileId, _Mapping]]] = ...) -> None: ...

class CMsgCREItemVoteSummaryResponse(_message.Message):
    __slots__ = ("eresult", "item_vote_summaries")
    class ItemVoteSummary(_message.Message):
        __slots__ = ("published_file_id", "votes_for", "votes_against", "reports", "score")
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        VOTES_FOR_FIELD_NUMBER: _ClassVar[int]
        VOTES_AGAINST_FIELD_NUMBER: _ClassVar[int]
        REPORTS_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        votes_for: int
        votes_against: int
        reports: int
        score: float
        def __init__(self, published_file_id: _Optional[int] = ..., votes_for: _Optional[int] = ..., votes_against: _Optional[int] = ..., reports: _Optional[int] = ..., score: _Optional[float] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ITEM_VOTE_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    item_vote_summaries: _containers.RepeatedCompositeFieldContainer[CMsgCREItemVoteSummaryResponse.ItemVoteSummary]
    def __init__(self, eresult: _Optional[int] = ..., item_vote_summaries: _Optional[_Iterable[_Union[CMsgCREItemVoteSummaryResponse.ItemVoteSummary, _Mapping]]] = ...) -> None: ...

class CMsgCREUpdateUserPublishedItemVote(_message.Message):
    __slots__ = ("published_file_id", "vote_up")
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_UP_FIELD_NUMBER: _ClassVar[int]
    published_file_id: int
    vote_up: bool
    def __init__(self, published_file_id: _Optional[int] = ..., vote_up: bool = ...) -> None: ...

class CMsgCREUpdateUserPublishedItemVoteResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgCREGetUserPublishedItemVoteDetails(_message.Message):
    __slots__ = ("published_file_ids",)
    class PublishedFileId(_message.Message):
        __slots__ = ("published_file_id",)
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        def __init__(self, published_file_id: _Optional[int] = ...) -> None: ...
    PUBLISHED_FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    published_file_ids: _containers.RepeatedCompositeFieldContainer[CMsgCREGetUserPublishedItemVoteDetails.PublishedFileId]
    def __init__(self, published_file_ids: _Optional[_Iterable[_Union[CMsgCREGetUserPublishedItemVoteDetails.PublishedFileId, _Mapping]]] = ...) -> None: ...

class CMsgCREGetUserPublishedItemVoteDetailsResponse(_message.Message):
    __slots__ = ("eresult", "user_item_vote_details")
    class UserItemVoteDetail(_message.Message):
        __slots__ = ("published_file_id", "vote")
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        VOTE_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        vote: int
        def __init__(self, published_file_id: _Optional[int] = ..., vote: _Optional[int] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    USER_ITEM_VOTE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    user_item_vote_details: _containers.RepeatedCompositeFieldContainer[CMsgCREGetUserPublishedItemVoteDetailsResponse.UserItemVoteDetail]
    def __init__(self, eresult: _Optional[int] = ..., user_item_vote_details: _Optional[_Iterable[_Union[CMsgCREGetUserPublishedItemVoteDetailsResponse.UserItemVoteDetail, _Mapping]]] = ...) -> None: ...

class CMsgFSGetFollowerCount(_message.Message):
    __slots__ = ("steam_id",)
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ...) -> None: ...

class CMsgFSGetFollowerCountResponse(_message.Message):
    __slots__ = ("eresult", "count")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    count: int
    def __init__(self, eresult: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class CMsgFSGetIsFollowing(_message.Message):
    __slots__ = ("steam_id",)
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ...) -> None: ...

class CMsgFSGetIsFollowingResponse(_message.Message):
    __slots__ = ("eresult", "is_following")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    IS_FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    is_following: bool
    def __init__(self, eresult: _Optional[int] = ..., is_following: bool = ...) -> None: ...

class CMsgFSEnumerateFollowingList(_message.Message):
    __slots__ = ("start_index",)
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    start_index: int
    def __init__(self, start_index: _Optional[int] = ...) -> None: ...

class CMsgFSEnumerateFollowingListResponse(_message.Message):
    __slots__ = ("eresult", "total_results", "steam_ids")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    STEAM_IDS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    total_results: int
    steam_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, eresult: _Optional[int] = ..., total_results: _Optional[int] = ..., steam_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgDPGetNumberOfCurrentPlayers(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CMsgDPGetNumberOfCurrentPlayersResponse(_message.Message):
    __slots__ = ("eresult", "player_count")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_COUNT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    player_count: int
    def __init__(self, eresult: _Optional[int] = ..., player_count: _Optional[int] = ...) -> None: ...

class CMsgClientFriendUserStatusPublished(_message.Message):
    __slots__ = ("friend_steamid", "appid", "status_text")
    FRIEND_STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
    friend_steamid: int
    appid: int
    status_text: str
    def __init__(self, friend_steamid: _Optional[int] = ..., appid: _Optional[int] = ..., status_text: _Optional[str] = ...) -> None: ...

class CMsgClientServiceMethodLegacy(_message.Message):
    __slots__ = ("method_name", "serialized_method", "is_notification")
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_METHOD_FIELD_NUMBER: _ClassVar[int]
    IS_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    method_name: str
    serialized_method: bytes
    is_notification: bool
    def __init__(self, method_name: _Optional[str] = ..., serialized_method: _Optional[bytes] = ..., is_notification: bool = ...) -> None: ...

class CMsgClientServiceMethodLegacyResponse(_message.Message):
    __slots__ = ("method_name", "serialized_method_response")
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    SERIALIZED_METHOD_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    method_name: str
    serialized_method_response: bytes
    def __init__(self, method_name: _Optional[str] = ..., serialized_method_response: _Optional[bytes] = ...) -> None: ...

class CMsgClientUIMode(_message.Message):
    __slots__ = ("uimode", "chat_mode")
    UIMODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_MODE_FIELD_NUMBER: _ClassVar[int]
    uimode: int
    chat_mode: int
    def __init__(self, uimode: _Optional[int] = ..., chat_mode: _Optional[int] = ...) -> None: ...

class CMsgClientVanityURLChangedNotification(_message.Message):
    __slots__ = ("vanity_url",)
    VANITY_URL_FIELD_NUMBER: _ClassVar[int]
    vanity_url: str
    def __init__(self, vanity_url: _Optional[str] = ...) -> None: ...

class CMsgClientAuthorizeLocalDeviceRequest(_message.Message):
    __slots__ = ("device_description", "owner_account_id", "local_device_token")
    DEVICE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    device_description: str
    owner_account_id: int
    local_device_token: int
    def __init__(self, device_description: _Optional[str] = ..., owner_account_id: _Optional[int] = ..., local_device_token: _Optional[int] = ...) -> None: ...

class CMsgClientAuthorizeLocalDevice(_message.Message):
    __slots__ = ("eresult", "owner_account_id", "authed_device_token")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    OWNER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHED_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    owner_account_id: int
    authed_device_token: int
    def __init__(self, eresult: _Optional[int] = ..., owner_account_id: _Optional[int] = ..., authed_device_token: _Optional[int] = ...) -> None: ...

class CMsgClientAuthorizeLocalDeviceNotification(_message.Message):
    __slots__ = ("eresult", "owner_account_id", "local_device_token")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    OWNER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    owner_account_id: int
    local_device_token: int
    def __init__(self, eresult: _Optional[int] = ..., owner_account_id: _Optional[int] = ..., local_device_token: _Optional[int] = ...) -> None: ...

class CMsgClientDeauthorizeDeviceRequest(_message.Message):
    __slots__ = ("deauthorization_account_id", "deauthorization_device_token")
    DEAUTHORIZATION_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DEAUTHORIZATION_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deauthorization_account_id: int
    deauthorization_device_token: int
    def __init__(self, deauthorization_account_id: _Optional[int] = ..., deauthorization_device_token: _Optional[int] = ...) -> None: ...

class CMsgClientDeauthorizeDevice(_message.Message):
    __slots__ = ("eresult", "deauthorization_account_id")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    DEAUTHORIZATION_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    deauthorization_account_id: int
    def __init__(self, eresult: _Optional[int] = ..., deauthorization_account_id: _Optional[int] = ...) -> None: ...

class CMsgClientUseLocalDeviceAuthorizations(_message.Message):
    __slots__ = ("authorization_account_id", "device_tokens")
    class DeviceToken(_message.Message):
        __slots__ = ("owner_account_id", "token_id")
        OWNER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        owner_account_id: int
        token_id: int
        def __init__(self, owner_account_id: _Optional[int] = ..., token_id: _Optional[int] = ...) -> None: ...
    AUTHORIZATION_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    authorization_account_id: _containers.RepeatedScalarFieldContainer[int]
    device_tokens: _containers.RepeatedCompositeFieldContainer[CMsgClientUseLocalDeviceAuthorizations.DeviceToken]
    def __init__(self, authorization_account_id: _Optional[_Iterable[int]] = ..., device_tokens: _Optional[_Iterable[_Union[CMsgClientUseLocalDeviceAuthorizations.DeviceToken, _Mapping]]] = ...) -> None: ...

class CMsgClientGetAuthorizedDevices(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientGetAuthorizedDevicesResponse(_message.Message):
    __slots__ = ("eresult", "authorized_device")
    class AuthorizedDevice(_message.Message):
        __slots__ = ("auth_device_token", "device_name", "last_access_time", "borrower_id", "is_pending", "app_played")
        AUTH_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
        BORROWER_ID_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        APP_PLAYED_FIELD_NUMBER: _ClassVar[int]
        auth_device_token: int
        device_name: str
        last_access_time: int
        borrower_id: int
        is_pending: bool
        app_played: int
        def __init__(self, auth_device_token: _Optional[int] = ..., device_name: _Optional[str] = ..., last_access_time: _Optional[int] = ..., borrower_id: _Optional[int] = ..., is_pending: bool = ..., app_played: _Optional[int] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_DEVICE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    authorized_device: _containers.RepeatedCompositeFieldContainer[CMsgClientGetAuthorizedDevicesResponse.AuthorizedDevice]
    def __init__(self, eresult: _Optional[int] = ..., authorized_device: _Optional[_Iterable[_Union[CMsgClientGetAuthorizedDevicesResponse.AuthorizedDevice, _Mapping]]] = ...) -> None: ...

class CMsgClientSharedLibraryLockStatus(_message.Message):
    __slots__ = ("locked_library", "own_library_locked_by")
    class LockedLibrary(_message.Message):
        __slots__ = ("owner_id", "locked_by")
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        LOCKED_BY_FIELD_NUMBER: _ClassVar[int]
        owner_id: int
        locked_by: int
        def __init__(self, owner_id: _Optional[int] = ..., locked_by: _Optional[int] = ...) -> None: ...
    LOCKED_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    OWN_LIBRARY_LOCKED_BY_FIELD_NUMBER: _ClassVar[int]
    locked_library: _containers.RepeatedCompositeFieldContainer[CMsgClientSharedLibraryLockStatus.LockedLibrary]
    own_library_locked_by: int
    def __init__(self, locked_library: _Optional[_Iterable[_Union[CMsgClientSharedLibraryLockStatus.LockedLibrary, _Mapping]]] = ..., own_library_locked_by: _Optional[int] = ...) -> None: ...

class CMsgClientSharedLibraryStopPlaying(_message.Message):
    __slots__ = ("seconds_left", "stop_apps")
    class StopApp(_message.Message):
        __slots__ = ("app_id", "owner_id")
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        app_id: int
        owner_id: int
        def __init__(self, app_id: _Optional[int] = ..., owner_id: _Optional[int] = ...) -> None: ...
    SECONDS_LEFT_FIELD_NUMBER: _ClassVar[int]
    STOP_APPS_FIELD_NUMBER: _ClassVar[int]
    seconds_left: int
    stop_apps: _containers.RepeatedCompositeFieldContainer[CMsgClientSharedLibraryStopPlaying.StopApp]
    def __init__(self, seconds_left: _Optional[int] = ..., stop_apps: _Optional[_Iterable[_Union[CMsgClientSharedLibraryStopPlaying.StopApp, _Mapping]]] = ...) -> None: ...

class CMsgClientServiceCall(_message.Message):
    __slots__ = ("sysid_routing", "call_handle", "module_crc", "module_hash", "function_id", "cub_output_max", "flags", "callparameter", "ping_only", "max_outstanding_calls", "app_id")
    SYSID_ROUTING_FIELD_NUMBER: _ClassVar[int]
    CALL_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MODULE_CRC_FIELD_NUMBER: _ClassVar[int]
    MODULE_HASH_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_ID_FIELD_NUMBER: _ClassVar[int]
    CUB_OUTPUT_MAX_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    CALLPARAMETER_FIELD_NUMBER: _ClassVar[int]
    PING_ONLY_FIELD_NUMBER: _ClassVar[int]
    MAX_OUTSTANDING_CALLS_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    sysid_routing: bytes
    call_handle: int
    module_crc: int
    module_hash: bytes
    function_id: int
    cub_output_max: int
    flags: int
    callparameter: bytes
    ping_only: bool
    max_outstanding_calls: int
    app_id: int
    def __init__(self, sysid_routing: _Optional[bytes] = ..., call_handle: _Optional[int] = ..., module_crc: _Optional[int] = ..., module_hash: _Optional[bytes] = ..., function_id: _Optional[int] = ..., cub_output_max: _Optional[int] = ..., flags: _Optional[int] = ..., callparameter: _Optional[bytes] = ..., ping_only: bool = ..., max_outstanding_calls: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class CMsgClientServiceModule(_message.Message):
    __slots__ = ("module_crc", "module_hash", "module_content")
    MODULE_CRC_FIELD_NUMBER: _ClassVar[int]
    MODULE_HASH_FIELD_NUMBER: _ClassVar[int]
    MODULE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    module_crc: int
    module_hash: bytes
    module_content: bytes
    def __init__(self, module_crc: _Optional[int] = ..., module_hash: _Optional[bytes] = ..., module_content: _Optional[bytes] = ...) -> None: ...

class CMsgClientServiceCallResponse(_message.Message):
    __slots__ = ("sysid_routing", "call_handle", "module_crc", "module_hash", "ecallresult", "result_content", "os_version_info", "system_info", "load_address", "exception_record", "portable_os_version_info", "portable_system_info", "was_converted", "internal_result", "current_count", "last_call_handle", "last_call_module_crc", "last_call_sysid_routing", "last_ecallresult", "last_callissue_delta", "last_callcomplete_delta")
    SYSID_ROUTING_FIELD_NUMBER: _ClassVar[int]
    CALL_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MODULE_CRC_FIELD_NUMBER: _ClassVar[int]
    MODULE_HASH_FIELD_NUMBER: _ClassVar[int]
    ECALLRESULT_FIELD_NUMBER: _ClassVar[int]
    RESULT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    LOAD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_RECORD_FIELD_NUMBER: _ClassVar[int]
    PORTABLE_OS_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    PORTABLE_SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    WAS_CONVERTED_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_RESULT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_CALL_HANDLE_FIELD_NUMBER: _ClassVar[int]
    LAST_CALL_MODULE_CRC_FIELD_NUMBER: _ClassVar[int]
    LAST_CALL_SYSID_ROUTING_FIELD_NUMBER: _ClassVar[int]
    LAST_ECALLRESULT_FIELD_NUMBER: _ClassVar[int]
    LAST_CALLISSUE_DELTA_FIELD_NUMBER: _ClassVar[int]
    LAST_CALLCOMPLETE_DELTA_FIELD_NUMBER: _ClassVar[int]
    sysid_routing: bytes
    call_handle: int
    module_crc: int
    module_hash: bytes
    ecallresult: int
    result_content: bytes
    os_version_info: bytes
    system_info: bytes
    load_address: int
    exception_record: bytes
    portable_os_version_info: bytes
    portable_system_info: bytes
    was_converted: bool
    internal_result: int
    current_count: int
    last_call_handle: int
    last_call_module_crc: int
    last_call_sysid_routing: bytes
    last_ecallresult: int
    last_callissue_delta: int
    last_callcomplete_delta: int
    def __init__(self, sysid_routing: _Optional[bytes] = ..., call_handle: _Optional[int] = ..., module_crc: _Optional[int] = ..., module_hash: _Optional[bytes] = ..., ecallresult: _Optional[int] = ..., result_content: _Optional[bytes] = ..., os_version_info: _Optional[bytes] = ..., system_info: _Optional[bytes] = ..., load_address: _Optional[int] = ..., exception_record: _Optional[bytes] = ..., portable_os_version_info: _Optional[bytes] = ..., portable_system_info: _Optional[bytes] = ..., was_converted: bool = ..., internal_result: _Optional[int] = ..., current_count: _Optional[int] = ..., last_call_handle: _Optional[int] = ..., last_call_module_crc: _Optional[int] = ..., last_call_sysid_routing: _Optional[bytes] = ..., last_ecallresult: _Optional[int] = ..., last_callissue_delta: _Optional[int] = ..., last_callcomplete_delta: _Optional[int] = ...) -> None: ...

class CMsgAMUnlockH264(_message.Message):
    __slots__ = ("appid", "platform", "reason")
    APPID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    appid: int
    platform: int
    reason: int
    def __init__(self, appid: _Optional[int] = ..., platform: _Optional[int] = ..., reason: _Optional[int] = ...) -> None: ...

class CMsgAMUnlockH264Response(_message.Message):
    __slots__ = ("eresult", "encryption_key")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    encryption_key: bytes
    def __init__(self, eresult: _Optional[int] = ..., encryption_key: _Optional[bytes] = ...) -> None: ...

class CMsgClientPlayingSessionState(_message.Message):
    __slots__ = ("playing_blocked", "playing_app")
    PLAYING_BLOCKED_FIELD_NUMBER: _ClassVar[int]
    PLAYING_APP_FIELD_NUMBER: _ClassVar[int]
    playing_blocked: bool
    playing_app: int
    def __init__(self, playing_blocked: bool = ..., playing_app: _Optional[int] = ...) -> None: ...

class CMsgClientKickPlayingSession(_message.Message):
    __slots__ = ("only_stop_game",)
    ONLY_STOP_GAME_FIELD_NUMBER: _ClassVar[int]
    only_stop_game: bool
    def __init__(self, only_stop_game: bool = ...) -> None: ...

class CMsgClientVoiceCallPreAuthorize(_message.Message):
    __slots__ = ("caller_steamid", "receiver_steamid", "caller_id", "hangup")
    CALLER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    HANGUP_FIELD_NUMBER: _ClassVar[int]
    caller_steamid: int
    receiver_steamid: int
    caller_id: int
    hangup: bool
    def __init__(self, caller_steamid: _Optional[int] = ..., receiver_steamid: _Optional[int] = ..., caller_id: _Optional[int] = ..., hangup: bool = ...) -> None: ...

class CMsgClientVoiceCallPreAuthorizeResponse(_message.Message):
    __slots__ = ("caller_steamid", "receiver_steamid", "eresult", "caller_id")
    CALLER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    caller_steamid: int
    receiver_steamid: int
    eresult: int
    caller_id: int
    def __init__(self, caller_steamid: _Optional[int] = ..., receiver_steamid: _Optional[int] = ..., eresult: _Optional[int] = ..., caller_id: _Optional[int] = ...) -> None: ...

class CMsgBadgeCraftedNotification(_message.Message):
    __slots__ = ("appid", "badge_level")
    APPID_FIELD_NUMBER: _ClassVar[int]
    BADGE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    appid: int
    badge_level: int
    def __init__(self, appid: _Optional[int] = ..., badge_level: _Optional[int] = ...) -> None: ...

class CMsgClientStartPeerContentServer(_message.Message):
    __slots__ = ("steamid", "client_remote_id", "app_id", "current_build_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REMOTE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    client_remote_id: int
    app_id: int
    current_build_id: int
    def __init__(self, steamid: _Optional[int] = ..., client_remote_id: _Optional[int] = ..., app_id: _Optional[int] = ..., current_build_id: _Optional[int] = ...) -> None: ...

class CMsgClientStartPeerContentServerResponse(_message.Message):
    __slots__ = ("result", "server_port", "installed_depots", "access_token")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_DEPOTS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    result: int
    server_port: int
    installed_depots: _containers.RepeatedScalarFieldContainer[int]
    access_token: int
    def __init__(self, result: _Optional[int] = ..., server_port: _Optional[int] = ..., installed_depots: _Optional[_Iterable[int]] = ..., access_token: _Optional[int] = ...) -> None: ...

class CMsgClientGetPeerContentInfo(_message.Message):
    __slots__ = ("steamid", "client_remote_id", "owned_games_visible")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REMOTE_ID_FIELD_NUMBER: _ClassVar[int]
    OWNED_GAMES_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    client_remote_id: int
    owned_games_visible: bool
    def __init__(self, steamid: _Optional[int] = ..., client_remote_id: _Optional[int] = ..., owned_games_visible: bool = ...) -> None: ...

class CMsgClientGetPeerContentInfoResponse(_message.Message):
    __slots__ = ("result", "apps")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    APPS_FIELD_NUMBER: _ClassVar[int]
    result: int
    apps: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, result: _Optional[int] = ..., apps: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientPendingGameLaunch(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    def __init__(self, app_id: _Optional[int] = ...) -> None: ...

class CMsgClientPendingGameLaunchResponse(_message.Message):
    __slots__ = ("eresult", "app_id", "envkey")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ENVKEY_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    app_id: int
    envkey: str
    def __init__(self, eresult: _Optional[int] = ..., app_id: _Optional[int] = ..., envkey: _Optional[str] = ...) -> None: ...
