import steammessages_base_pb2 as _steammessages_base_pb2
import encrypted_app_ticket_pb2 as _encrypted_app_ticket_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientRegisterAuthTicketWithCM(_message.Message):
    __slots__ = ("protocol_version", "ticket", "client_instance_id")
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    protocol_version: int
    ticket: bytes
    client_instance_id: int
    def __init__(self, protocol_version: _Optional[int] = ..., ticket: _Optional[bytes] = ..., client_instance_id: _Optional[int] = ...) -> None: ...

class CMsgClientTicketAuthComplete(_message.Message):
    __slots__ = ("steam_id", "game_id", "estate", "eauth_session_response", "DEPRECATED_ticket", "ticket_crc", "ticket_sequence", "owner_steam_id")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ESTATE_FIELD_NUMBER: _ClassVar[int]
    EAUTH_SESSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_TICKET_FIELD_NUMBER: _ClassVar[int]
    TICKET_CRC_FIELD_NUMBER: _ClassVar[int]
    TICKET_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    game_id: int
    estate: int
    eauth_session_response: int
    DEPRECATED_ticket: bytes
    ticket_crc: int
    ticket_sequence: int
    owner_steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., game_id: _Optional[int] = ..., estate: _Optional[int] = ..., eauth_session_response: _Optional[int] = ..., DEPRECATED_ticket: _Optional[bytes] = ..., ticket_crc: _Optional[int] = ..., ticket_sequence: _Optional[int] = ..., owner_steam_id: _Optional[int] = ...) -> None: ...

class CMsgClientP2PConnectionInfo(_message.Message):
    __slots__ = ("steam_id_dest", "steam_id_src", "app_id", "candidate", "legacy_connection_id_src", "rendezvous")
    STEAM_ID_DEST_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_SRC_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    LEGACY_CONNECTION_ID_SRC_FIELD_NUMBER: _ClassVar[int]
    RENDEZVOUS_FIELD_NUMBER: _ClassVar[int]
    steam_id_dest: int
    steam_id_src: int
    app_id: int
    candidate: bytes
    legacy_connection_id_src: int
    rendezvous: bytes
    def __init__(self, steam_id_dest: _Optional[int] = ..., steam_id_src: _Optional[int] = ..., app_id: _Optional[int] = ..., candidate: _Optional[bytes] = ..., legacy_connection_id_src: _Optional[int] = ..., rendezvous: _Optional[bytes] = ...) -> None: ...

class CMsgClientP2PConnectionFailInfo(_message.Message):
    __slots__ = ("steam_id_dest", "steam_id_src", "app_id", "ep2p_session_error", "connection_id_dest", "close_reason", "close_message")
    STEAM_ID_DEST_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_SRC_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    EP2P_SESSION_ERROR_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ID_DEST_FIELD_NUMBER: _ClassVar[int]
    CLOSE_REASON_FIELD_NUMBER: _ClassVar[int]
    CLOSE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    steam_id_dest: int
    steam_id_src: int
    app_id: int
    ep2p_session_error: int
    connection_id_dest: int
    close_reason: int
    close_message: str
    def __init__(self, steam_id_dest: _Optional[int] = ..., steam_id_src: _Optional[int] = ..., app_id: _Optional[int] = ..., ep2p_session_error: _Optional[int] = ..., connection_id_dest: _Optional[int] = ..., close_reason: _Optional[int] = ..., close_message: _Optional[str] = ...) -> None: ...

class CMsgClientNetworkingCertRequest(_message.Message):
    __slots__ = ("key_data", "app_id")
    KEY_DATA_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    key_data: bytes
    app_id: int
    def __init__(self, key_data: _Optional[bytes] = ..., app_id: _Optional[int] = ...) -> None: ...

class CMsgClientNetworkingCertReply(_message.Message):
    __slots__ = ("cert", "ca_key_id", "ca_signature")
    CERT_FIELD_NUMBER: _ClassVar[int]
    CA_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    CA_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    cert: bytes
    ca_key_id: int
    ca_signature: bytes
    def __init__(self, cert: _Optional[bytes] = ..., ca_key_id: _Optional[int] = ..., ca_signature: _Optional[bytes] = ...) -> None: ...

class CMsgClientNetworkingMobileCertRequest(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    def __init__(self, app_id: _Optional[int] = ...) -> None: ...

class CMsgClientNetworkingMobileCertReply(_message.Message):
    __slots__ = ("encoded_cert",)
    ENCODED_CERT_FIELD_NUMBER: _ClassVar[int]
    encoded_cert: str
    def __init__(self, encoded_cert: _Optional[str] = ...) -> None: ...

class CMsgClientGetAppOwnershipTicket(_message.Message):
    __slots__ = ("app_id",)
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    def __init__(self, app_id: _Optional[int] = ...) -> None: ...

class CMsgClientGetAppOwnershipTicketResponse(_message.Message):
    __slots__ = ("eresult", "app_id", "ticket")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    app_id: int
    ticket: bytes
    def __init__(self, eresult: _Optional[int] = ..., app_id: _Optional[int] = ..., ticket: _Optional[bytes] = ...) -> None: ...

class CMsgClientSessionToken(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: int
    def __init__(self, token: _Optional[int] = ...) -> None: ...

class CMsgClientGameConnectTokens(_message.Message):
    __slots__ = ("max_tokens_to_keep", "tokens")
    MAX_TOKENS_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    max_tokens_to_keep: int
    tokens: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, max_tokens_to_keep: _Optional[int] = ..., tokens: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CMsgClientGamesPlayed(_message.Message):
    __slots__ = ("games_played", "client_os_type", "cloud_gaming_platform", "recent_reauthentication")
    class ProcessInfo(_message.Message):
        __slots__ = ("process_id", "process_id_parent", "parent_is_steam")
        PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
        PROCESS_ID_PARENT_FIELD_NUMBER: _ClassVar[int]
        PARENT_IS_STEAM_FIELD_NUMBER: _ClassVar[int]
        process_id: int
        process_id_parent: int
        parent_is_steam: bool
        def __init__(self, process_id: _Optional[int] = ..., process_id_parent: _Optional[int] = ..., parent_is_steam: bool = ...) -> None: ...
    class GamePlayed(_message.Message):
        __slots__ = ("steam_id_gs", "game_id", "deprecated_game_ip_address", "game_port", "is_secure", "token", "game_extra_info", "game_data_blob", "process_id", "streaming_provider_id", "game_flags", "owner_id", "vr_hmd_vendor", "vr_hmd_model", "launch_option_type", "primary_controller_type", "primary_steam_controller_serial", "total_steam_controller_count", "total_non_steam_controller_count", "controller_workshop_file_id", "launch_source", "vr_hmd_runtime", "game_ip_address", "controller_connection_type", "game_os_platform", "game_build_id", "compat_tool_id", "compat_tool_cmd", "compat_tool_build_id", "beta_name", "dlc_context", "process_id_list")
        STEAM_ID_GS_FIELD_NUMBER: _ClassVar[int]
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_GAME_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        GAME_PORT_FIELD_NUMBER: _ClassVar[int]
        IS_SECURE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        GAME_EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
        GAME_DATA_BLOB_FIELD_NUMBER: _ClassVar[int]
        PROCESS_ID_FIELD_NUMBER: _ClassVar[int]
        STREAMING_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
        GAME_FLAGS_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        VR_HMD_VENDOR_FIELD_NUMBER: _ClassVar[int]
        VR_HMD_MODEL_FIELD_NUMBER: _ClassVar[int]
        LAUNCH_OPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_STEAM_CONTROLLER_SERIAL_FIELD_NUMBER: _ClassVar[int]
        TOTAL_STEAM_CONTROLLER_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_NON_STEAM_CONTROLLER_COUNT_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_WORKSHOP_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        LAUNCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
        VR_HMD_RUNTIME_FIELD_NUMBER: _ClassVar[int]
        GAME_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        GAME_OS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
        GAME_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
        COMPAT_TOOL_ID_FIELD_NUMBER: _ClassVar[int]
        COMPAT_TOOL_CMD_FIELD_NUMBER: _ClassVar[int]
        COMPAT_TOOL_BUILD_ID_FIELD_NUMBER: _ClassVar[int]
        BETA_NAME_FIELD_NUMBER: _ClassVar[int]
        DLC_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        PROCESS_ID_LIST_FIELD_NUMBER: _ClassVar[int]
        steam_id_gs: int
        game_id: int
        deprecated_game_ip_address: int
        game_port: int
        is_secure: bool
        token: bytes
        game_extra_info: str
        game_data_blob: bytes
        process_id: int
        streaming_provider_id: int
        game_flags: int
        owner_id: int
        vr_hmd_vendor: str
        vr_hmd_model: str
        launch_option_type: int
        primary_controller_type: int
        primary_steam_controller_serial: str
        total_steam_controller_count: int
        total_non_steam_controller_count: int
        controller_workshop_file_id: int
        launch_source: int
        vr_hmd_runtime: int
        game_ip_address: _steammessages_base_pb2.CMsgIPAddress
        controller_connection_type: int
        game_os_platform: int
        game_build_id: int
        compat_tool_id: int
        compat_tool_cmd: str
        compat_tool_build_id: int
        beta_name: str
        dlc_context: int
        process_id_list: _containers.RepeatedCompositeFieldContainer[CMsgClientGamesPlayed.ProcessInfo]
        def __init__(self, steam_id_gs: _Optional[int] = ..., game_id: _Optional[int] = ..., deprecated_game_ip_address: _Optional[int] = ..., game_port: _Optional[int] = ..., is_secure: bool = ..., token: _Optional[bytes] = ..., game_extra_info: _Optional[str] = ..., game_data_blob: _Optional[bytes] = ..., process_id: _Optional[int] = ..., streaming_provider_id: _Optional[int] = ..., game_flags: _Optional[int] = ..., owner_id: _Optional[int] = ..., vr_hmd_vendor: _Optional[str] = ..., vr_hmd_model: _Optional[str] = ..., launch_option_type: _Optional[int] = ..., primary_controller_type: _Optional[int] = ..., primary_steam_controller_serial: _Optional[str] = ..., total_steam_controller_count: _Optional[int] = ..., total_non_steam_controller_count: _Optional[int] = ..., controller_workshop_file_id: _Optional[int] = ..., launch_source: _Optional[int] = ..., vr_hmd_runtime: _Optional[int] = ..., game_ip_address: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., controller_connection_type: _Optional[int] = ..., game_os_platform: _Optional[int] = ..., game_build_id: _Optional[int] = ..., compat_tool_id: _Optional[int] = ..., compat_tool_cmd: _Optional[str] = ..., compat_tool_build_id: _Optional[int] = ..., beta_name: _Optional[str] = ..., dlc_context: _Optional[int] = ..., process_id_list: _Optional[_Iterable[_Union[CMsgClientGamesPlayed.ProcessInfo, _Mapping]]] = ...) -> None: ...
    GAMES_PLAYED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_GAMING_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    RECENT_REAUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    games_played: _containers.RepeatedCompositeFieldContainer[CMsgClientGamesPlayed.GamePlayed]
    client_os_type: int
    cloud_gaming_platform: int
    recent_reauthentication: bool
    def __init__(self, games_played: _Optional[_Iterable[_Union[CMsgClientGamesPlayed.GamePlayed, _Mapping]]] = ..., client_os_type: _Optional[int] = ..., cloud_gaming_platform: _Optional[int] = ..., recent_reauthentication: bool = ...) -> None: ...

class CMsgGSApprove(_message.Message):
    __slots__ = ("steam_id", "owner_steam_id")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    owner_steam_id: int
    def __init__(self, steam_id: _Optional[int] = ..., owner_steam_id: _Optional[int] = ...) -> None: ...

class CMsgGSDeny(_message.Message):
    __slots__ = ("steam_id", "edeny_reason", "deny_string")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    EDENY_REASON_FIELD_NUMBER: _ClassVar[int]
    DENY_STRING_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    edeny_reason: int
    deny_string: str
    def __init__(self, steam_id: _Optional[int] = ..., edeny_reason: _Optional[int] = ..., deny_string: _Optional[str] = ...) -> None: ...

class CMsgGSKick(_message.Message):
    __slots__ = ("steam_id", "edeny_reason")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    EDENY_REASON_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    edeny_reason: int
    def __init__(self, steam_id: _Optional[int] = ..., edeny_reason: _Optional[int] = ...) -> None: ...

class CMsgClientAuthList(_message.Message):
    __slots__ = ("tokens_left", "last_request_seq", "last_request_seq_from_server", "tickets", "app_ids", "message_sequence", "filtered")
    TOKENS_LEFT_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_SEQ_FIELD_NUMBER: _ClassVar[int]
    LAST_REQUEST_SEQ_FROM_SERVER_FIELD_NUMBER: _ClassVar[int]
    TICKETS_FIELD_NUMBER: _ClassVar[int]
    APP_IDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    FILTERED_FIELD_NUMBER: _ClassVar[int]
    tokens_left: int
    last_request_seq: int
    last_request_seq_from_server: int
    tickets: _containers.RepeatedCompositeFieldContainer[_steammessages_base_pb2.CMsgAuthTicket]
    app_ids: _containers.RepeatedScalarFieldContainer[int]
    message_sequence: int
    filtered: bool
    def __init__(self, tokens_left: _Optional[int] = ..., last_request_seq: _Optional[int] = ..., last_request_seq_from_server: _Optional[int] = ..., tickets: _Optional[_Iterable[_Union[_steammessages_base_pb2.CMsgAuthTicket, _Mapping]]] = ..., app_ids: _Optional[_Iterable[int]] = ..., message_sequence: _Optional[int] = ..., filtered: bool = ...) -> None: ...

class CMsgClientAuthListAck(_message.Message):
    __slots__ = ("ticket_crc", "app_ids", "message_sequence")
    TICKET_CRC_FIELD_NUMBER: _ClassVar[int]
    APP_IDS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    ticket_crc: _containers.RepeatedScalarFieldContainer[int]
    app_ids: _containers.RepeatedScalarFieldContainer[int]
    message_sequence: int
    def __init__(self, ticket_crc: _Optional[_Iterable[int]] = ..., app_ids: _Optional[_Iterable[int]] = ..., message_sequence: _Optional[int] = ...) -> None: ...

class CMsgClientLicenseList(_message.Message):
    __slots__ = ("eresult", "licenses")
    class License(_message.Message):
        __slots__ = ("package_id", "time_created", "time_next_process", "minute_limit", "minutes_used", "payment_method", "flags", "purchase_country_code", "license_type", "territory_code", "change_number", "owner_id", "initial_period", "initial_time_unit", "renewal_period", "renewal_time_unit", "access_token", "master_package_id")
        PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
        TIME_NEXT_PROCESS_FIELD_NUMBER: _ClassVar[int]
        MINUTE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MINUTES_USED_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        LICENSE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TERRITORY_CODE_FIELD_NUMBER: _ClassVar[int]
        CHANGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        OWNER_ID_FIELD_NUMBER: _ClassVar[int]
        INITIAL_PERIOD_FIELD_NUMBER: _ClassVar[int]
        INITIAL_TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
        RENEWAL_PERIOD_FIELD_NUMBER: _ClassVar[int]
        RENEWAL_TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        MASTER_PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
        package_id: int
        time_created: int
        time_next_process: int
        minute_limit: int
        minutes_used: int
        payment_method: int
        flags: int
        purchase_country_code: str
        license_type: int
        territory_code: int
        change_number: int
        owner_id: int
        initial_period: int
        initial_time_unit: int
        renewal_period: int
        renewal_time_unit: int
        access_token: int
        master_package_id: int
        def __init__(self, package_id: _Optional[int] = ..., time_created: _Optional[int] = ..., time_next_process: _Optional[int] = ..., minute_limit: _Optional[int] = ..., minutes_used: _Optional[int] = ..., payment_method: _Optional[int] = ..., flags: _Optional[int] = ..., purchase_country_code: _Optional[str] = ..., license_type: _Optional[int] = ..., territory_code: _Optional[int] = ..., change_number: _Optional[int] = ..., owner_id: _Optional[int] = ..., initial_period: _Optional[int] = ..., initial_time_unit: _Optional[int] = ..., renewal_period: _Optional[int] = ..., renewal_time_unit: _Optional[int] = ..., access_token: _Optional[int] = ..., master_package_id: _Optional[int] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    LICENSES_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    licenses: _containers.RepeatedCompositeFieldContainer[CMsgClientLicenseList.License]
    def __init__(self, eresult: _Optional[int] = ..., licenses: _Optional[_Iterable[_Union[CMsgClientLicenseList.License, _Mapping]]] = ...) -> None: ...

class CMsgClientIsLimitedAccount(_message.Message):
    __slots__ = ("bis_limited_account", "bis_community_banned", "bis_locked_account", "bis_limited_account_allowed_to_invite_friends")
    BIS_LIMITED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BIS_COMMUNITY_BANNED_FIELD_NUMBER: _ClassVar[int]
    BIS_LOCKED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BIS_LIMITED_ACCOUNT_ALLOWED_TO_INVITE_FRIENDS_FIELD_NUMBER: _ClassVar[int]
    bis_limited_account: bool
    bis_community_banned: bool
    bis_locked_account: bool
    bis_limited_account_allowed_to_invite_friends: bool
    def __init__(self, bis_limited_account: bool = ..., bis_community_banned: bool = ..., bis_locked_account: bool = ..., bis_limited_account_allowed_to_invite_friends: bool = ...) -> None: ...

class CMsgClientRequestedClientStats(_message.Message):
    __slots__ = ("stats_to_send",)
    class StatsToSend(_message.Message):
        __slots__ = ("client_stat", "stat_aggregate_method")
        CLIENT_STAT_FIELD_NUMBER: _ClassVar[int]
        STAT_AGGREGATE_METHOD_FIELD_NUMBER: _ClassVar[int]
        client_stat: int
        stat_aggregate_method: int
        def __init__(self, client_stat: _Optional[int] = ..., stat_aggregate_method: _Optional[int] = ...) -> None: ...
    STATS_TO_SEND_FIELD_NUMBER: _ClassVar[int]
    stats_to_send: _containers.RepeatedCompositeFieldContainer[CMsgClientRequestedClientStats.StatsToSend]
    def __init__(self, stats_to_send: _Optional[_Iterable[_Union[CMsgClientRequestedClientStats.StatsToSend, _Mapping]]] = ...) -> None: ...

class CMsgClientStat2(_message.Message):
    __slots__ = ("stat_detail",)
    class StatDetail(_message.Message):
        __slots__ = ("client_stat", "ll_value", "time_of_day", "cell_id", "depot_id", "app_id")
        CLIENT_STAT_FIELD_NUMBER: _ClassVar[int]
        LL_VALUE_FIELD_NUMBER: _ClassVar[int]
        TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
        CELL_ID_FIELD_NUMBER: _ClassVar[int]
        DEPOT_ID_FIELD_NUMBER: _ClassVar[int]
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        client_stat: int
        ll_value: int
        time_of_day: int
        cell_id: int
        depot_id: int
        app_id: int
        def __init__(self, client_stat: _Optional[int] = ..., ll_value: _Optional[int] = ..., time_of_day: _Optional[int] = ..., cell_id: _Optional[int] = ..., depot_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...
    STAT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    stat_detail: _containers.RepeatedCompositeFieldContainer[CMsgClientStat2.StatDetail]
    def __init__(self, stat_detail: _Optional[_Iterable[_Union[CMsgClientStat2.StatDetail, _Mapping]]] = ...) -> None: ...

class CMsgClientInviteToGame(_message.Message):
    __slots__ = ("steam_id_dest", "steam_id_src", "connect_string", "remote_play")
    STEAM_ID_DEST_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_SRC_FIELD_NUMBER: _ClassVar[int]
    CONNECT_STRING_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PLAY_FIELD_NUMBER: _ClassVar[int]
    steam_id_dest: int
    steam_id_src: int
    connect_string: str
    remote_play: str
    def __init__(self, steam_id_dest: _Optional[int] = ..., steam_id_src: _Optional[int] = ..., connect_string: _Optional[str] = ..., remote_play: _Optional[str] = ...) -> None: ...

class CMsgClientChatInvite(_message.Message):
    __slots__ = ("steam_id_invited", "steam_id_chat", "steam_id_patron", "chatroom_type", "steam_id_friend_chat", "chat_name", "game_id")
    STEAM_ID_INVITED_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_CHAT_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_PATRON_FIELD_NUMBER: _ClassVar[int]
    CHATROOM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FRIEND_CHAT_FIELD_NUMBER: _ClassVar[int]
    CHAT_NAME_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id_invited: int
    steam_id_chat: int
    steam_id_patron: int
    chatroom_type: int
    steam_id_friend_chat: int
    chat_name: str
    game_id: int
    def __init__(self, steam_id_invited: _Optional[int] = ..., steam_id_chat: _Optional[int] = ..., steam_id_patron: _Optional[int] = ..., chatroom_type: _Optional[int] = ..., steam_id_friend_chat: _Optional[int] = ..., chat_name: _Optional[str] = ..., game_id: _Optional[int] = ...) -> None: ...

class CMsgClientConnectionStats(_message.Message):
    __slots__ = ("stats_logon", "stats_vconn")
    class Stats_Logon(_message.Message):
        __slots__ = ("connect_attempts", "connect_successes", "connect_failures", "connections_dropped", "seconds_running", "msec_tologonthistime", "count_bad_cms", "no_udp_connectivity", "no_tcp_connectivity", "no_websocket_443_connectivity", "no_websocket_non_443_connectivity")
        CONNECT_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        CONNECT_SUCCESSES_FIELD_NUMBER: _ClassVar[int]
        CONNECT_FAILURES_FIELD_NUMBER: _ClassVar[int]
        CONNECTIONS_DROPPED_FIELD_NUMBER: _ClassVar[int]
        SECONDS_RUNNING_FIELD_NUMBER: _ClassVar[int]
        MSEC_TOLOGONTHISTIME_FIELD_NUMBER: _ClassVar[int]
        COUNT_BAD_CMS_FIELD_NUMBER: _ClassVar[int]
        NO_UDP_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
        NO_TCP_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
        NO_WEBSOCKET_443_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
        NO_WEBSOCKET_NON_443_CONNECTIVITY_FIELD_NUMBER: _ClassVar[int]
        connect_attempts: int
        connect_successes: int
        connect_failures: int
        connections_dropped: int
        seconds_running: int
        msec_tologonthistime: int
        count_bad_cms: int
        no_udp_connectivity: bool
        no_tcp_connectivity: bool
        no_websocket_443_connectivity: bool
        no_websocket_non_443_connectivity: bool
        def __init__(self, connect_attempts: _Optional[int] = ..., connect_successes: _Optional[int] = ..., connect_failures: _Optional[int] = ..., connections_dropped: _Optional[int] = ..., seconds_running: _Optional[int] = ..., msec_tologonthistime: _Optional[int] = ..., count_bad_cms: _Optional[int] = ..., no_udp_connectivity: bool = ..., no_tcp_connectivity: bool = ..., no_websocket_443_connectivity: bool = ..., no_websocket_non_443_connectivity: bool = ...) -> None: ...
    class Stats_UDP(_message.Message):
        __slots__ = ("pkts_sent", "bytes_sent", "pkts_recv", "pkts_processed", "bytes_recv")
        PKTS_SENT_FIELD_NUMBER: _ClassVar[int]
        BYTES_SENT_FIELD_NUMBER: _ClassVar[int]
        PKTS_RECV_FIELD_NUMBER: _ClassVar[int]
        PKTS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
        BYTES_RECV_FIELD_NUMBER: _ClassVar[int]
        pkts_sent: int
        bytes_sent: int
        pkts_recv: int
        pkts_processed: int
        bytes_recv: int
        def __init__(self, pkts_sent: _Optional[int] = ..., bytes_sent: _Optional[int] = ..., pkts_recv: _Optional[int] = ..., pkts_processed: _Optional[int] = ..., bytes_recv: _Optional[int] = ...) -> None: ...
    class Stats_VConn(_message.Message):
        __slots__ = ("connections_udp", "connections_tcp", "stats_udp", "pkts_abandoned", "conn_req_received", "pkts_resent", "msgs_sent", "msgs_sent_failed", "msgs_recv", "datagrams_sent", "datagrams_recv", "bad_pkts_recv", "unknown_conn_pkts_recv", "missed_pkts_recv", "dup_pkts_recv", "failed_connect_challenges", "micro_sec_avg_latency", "micro_sec_min_latency", "micro_sec_max_latency")
        CONNECTIONS_UDP_FIELD_NUMBER: _ClassVar[int]
        CONNECTIONS_TCP_FIELD_NUMBER: _ClassVar[int]
        STATS_UDP_FIELD_NUMBER: _ClassVar[int]
        PKTS_ABANDONED_FIELD_NUMBER: _ClassVar[int]
        CONN_REQ_RECEIVED_FIELD_NUMBER: _ClassVar[int]
        PKTS_RESENT_FIELD_NUMBER: _ClassVar[int]
        MSGS_SENT_FIELD_NUMBER: _ClassVar[int]
        MSGS_SENT_FAILED_FIELD_NUMBER: _ClassVar[int]
        MSGS_RECV_FIELD_NUMBER: _ClassVar[int]
        DATAGRAMS_SENT_FIELD_NUMBER: _ClassVar[int]
        DATAGRAMS_RECV_FIELD_NUMBER: _ClassVar[int]
        BAD_PKTS_RECV_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_CONN_PKTS_RECV_FIELD_NUMBER: _ClassVar[int]
        MISSED_PKTS_RECV_FIELD_NUMBER: _ClassVar[int]
        DUP_PKTS_RECV_FIELD_NUMBER: _ClassVar[int]
        FAILED_CONNECT_CHALLENGES_FIELD_NUMBER: _ClassVar[int]
        MICRO_SEC_AVG_LATENCY_FIELD_NUMBER: _ClassVar[int]
        MICRO_SEC_MIN_LATENCY_FIELD_NUMBER: _ClassVar[int]
        MICRO_SEC_MAX_LATENCY_FIELD_NUMBER: _ClassVar[int]
        connections_udp: int
        connections_tcp: int
        stats_udp: CMsgClientConnectionStats.Stats_UDP
        pkts_abandoned: int
        conn_req_received: int
        pkts_resent: int
        msgs_sent: int
        msgs_sent_failed: int
        msgs_recv: int
        datagrams_sent: int
        datagrams_recv: int
        bad_pkts_recv: int
        unknown_conn_pkts_recv: int
        missed_pkts_recv: int
        dup_pkts_recv: int
        failed_connect_challenges: int
        micro_sec_avg_latency: int
        micro_sec_min_latency: int
        micro_sec_max_latency: int
        def __init__(self, connections_udp: _Optional[int] = ..., connections_tcp: _Optional[int] = ..., stats_udp: _Optional[_Union[CMsgClientConnectionStats.Stats_UDP, _Mapping]] = ..., pkts_abandoned: _Optional[int] = ..., conn_req_received: _Optional[int] = ..., pkts_resent: _Optional[int] = ..., msgs_sent: _Optional[int] = ..., msgs_sent_failed: _Optional[int] = ..., msgs_recv: _Optional[int] = ..., datagrams_sent: _Optional[int] = ..., datagrams_recv: _Optional[int] = ..., bad_pkts_recv: _Optional[int] = ..., unknown_conn_pkts_recv: _Optional[int] = ..., missed_pkts_recv: _Optional[int] = ..., dup_pkts_recv: _Optional[int] = ..., failed_connect_challenges: _Optional[int] = ..., micro_sec_avg_latency: _Optional[int] = ..., micro_sec_min_latency: _Optional[int] = ..., micro_sec_max_latency: _Optional[int] = ...) -> None: ...
    STATS_LOGON_FIELD_NUMBER: _ClassVar[int]
    STATS_VCONN_FIELD_NUMBER: _ClassVar[int]
    stats_logon: CMsgClientConnectionStats.Stats_Logon
    stats_vconn: CMsgClientConnectionStats.Stats_VConn
    def __init__(self, stats_logon: _Optional[_Union[CMsgClientConnectionStats.Stats_Logon, _Mapping]] = ..., stats_vconn: _Optional[_Union[CMsgClientConnectionStats.Stats_VConn, _Mapping]] = ...) -> None: ...

class CMsgClientServersAvailable(_message.Message):
    __slots__ = ("server_types_available", "server_type_for_auth_services")
    class Server_Types_Available(_message.Message):
        __slots__ = ("server", "changed")
        SERVER_FIELD_NUMBER: _ClassVar[int]
        CHANGED_FIELD_NUMBER: _ClassVar[int]
        server: int
        changed: bool
        def __init__(self, server: _Optional[int] = ..., changed: bool = ...) -> None: ...
    SERVER_TYPES_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TYPE_FOR_AUTH_SERVICES_FIELD_NUMBER: _ClassVar[int]
    server_types_available: _containers.RepeatedCompositeFieldContainer[CMsgClientServersAvailable.Server_Types_Available]
    server_type_for_auth_services: int
    def __init__(self, server_types_available: _Optional[_Iterable[_Union[CMsgClientServersAvailable.Server_Types_Available, _Mapping]]] = ..., server_type_for_auth_services: _Optional[int] = ...) -> None: ...

class CMsgClientReportOverlayDetourFailure(_message.Message):
    __slots__ = ("failure_strings",)
    FAILURE_STRINGS_FIELD_NUMBER: _ClassVar[int]
    failure_strings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, failure_strings: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgClientRequestEncryptedAppTicket(_message.Message):
    __slots__ = ("app_id", "userdata")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    USERDATA_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    userdata: bytes
    def __init__(self, app_id: _Optional[int] = ..., userdata: _Optional[bytes] = ...) -> None: ...

class CMsgClientRequestEncryptedAppTicketResponse(_message.Message):
    __slots__ = ("app_id", "eresult", "encrypted_app_ticket")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_APP_TICKET_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    eresult: int
    encrypted_app_ticket: _encrypted_app_ticket_pb2.EncryptedAppTicket
    def __init__(self, app_id: _Optional[int] = ..., eresult: _Optional[int] = ..., encrypted_app_ticket: _Optional[_Union[_encrypted_app_ticket_pb2.EncryptedAppTicket, _Mapping]] = ...) -> None: ...

class CMsgClientWalletInfoUpdate(_message.Message):
    __slots__ = ("has_wallet", "balance", "currency", "balance_delayed", "balance64", "balance64_delayed", "realm")
    HAS_WALLET_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BALANCE_DELAYED_FIELD_NUMBER: _ClassVar[int]
    BALANCE64_FIELD_NUMBER: _ClassVar[int]
    BALANCE64_DELAYED_FIELD_NUMBER: _ClassVar[int]
    REALM_FIELD_NUMBER: _ClassVar[int]
    has_wallet: bool
    balance: int
    currency: int
    balance_delayed: int
    balance64: int
    balance64_delayed: int
    realm: int
    def __init__(self, has_wallet: bool = ..., balance: _Optional[int] = ..., currency: _Optional[int] = ..., balance_delayed: _Optional[int] = ..., balance64: _Optional[int] = ..., balance64_delayed: _Optional[int] = ..., realm: _Optional[int] = ...) -> None: ...

class CMsgClientAMGetClanOfficers(_message.Message):
    __slots__ = ("steamid_clan",)
    STEAMID_CLAN_FIELD_NUMBER: _ClassVar[int]
    steamid_clan: int
    def __init__(self, steamid_clan: _Optional[int] = ...) -> None: ...

class CMsgClientAMGetClanOfficersResponse(_message.Message):
    __slots__ = ("eresult", "steamid_clan", "officer_count")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_CLAN_FIELD_NUMBER: _ClassVar[int]
    OFFICER_COUNT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    steamid_clan: int
    officer_count: int
    def __init__(self, eresult: _Optional[int] = ..., steamid_clan: _Optional[int] = ..., officer_count: _Optional[int] = ...) -> None: ...

class CMsgClientAMGetPersonaNameHistory(_message.Message):
    __slots__ = ("id_count", "Ids")
    class IdInstance(_message.Message):
        __slots__ = ("steamid",)
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        def __init__(self, steamid: _Optional[int] = ...) -> None: ...
    ID_COUNT_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    id_count: int
    Ids: _containers.RepeatedCompositeFieldContainer[CMsgClientAMGetPersonaNameHistory.IdInstance]
    def __init__(self, id_count: _Optional[int] = ..., Ids: _Optional[_Iterable[_Union[CMsgClientAMGetPersonaNameHistory.IdInstance, _Mapping]]] = ...) -> None: ...

class CMsgClientAMGetPersonaNameHistoryResponse(_message.Message):
    __slots__ = ("responses",)
    class NameTableInstance(_message.Message):
        __slots__ = ("eresult", "steamid", "names")
        class NameInstance(_message.Message):
            __slots__ = ("name_since", "name")
            NAME_SINCE_FIELD_NUMBER: _ClassVar[int]
            NAME_FIELD_NUMBER: _ClassVar[int]
            name_since: int
            name: str
            def __init__(self, name_since: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
        ERESULT_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        NAMES_FIELD_NUMBER: _ClassVar[int]
        eresult: int
        steamid: int
        names: _containers.RepeatedCompositeFieldContainer[CMsgClientAMGetPersonaNameHistoryResponse.NameTableInstance.NameInstance]
        def __init__(self, eresult: _Optional[int] = ..., steamid: _Optional[int] = ..., names: _Optional[_Iterable[_Union[CMsgClientAMGetPersonaNameHistoryResponse.NameTableInstance.NameInstance, _Mapping]]] = ...) -> None: ...
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[CMsgClientAMGetPersonaNameHistoryResponse.NameTableInstance]
    def __init__(self, responses: _Optional[_Iterable[_Union[CMsgClientAMGetPersonaNameHistoryResponse.NameTableInstance, _Mapping]]] = ...) -> None: ...

class CMsgClientDeregisterWithServer(_message.Message):
    __slots__ = ("eservertype", "app_id")
    ESERVERTYPE_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    eservertype: int
    app_id: int
    def __init__(self, eservertype: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class CMsgClientClanState(_message.Message):
    __slots__ = ("steamid_clan", "clan_account_flags", "name_info", "user_counts", "events", "announcements", "chat_room_private")
    class NameInfo(_message.Message):
        __slots__ = ("clan_name", "sha_avatar")
        CLAN_NAME_FIELD_NUMBER: _ClassVar[int]
        SHA_AVATAR_FIELD_NUMBER: _ClassVar[int]
        clan_name: str
        sha_avatar: bytes
        def __init__(self, clan_name: _Optional[str] = ..., sha_avatar: _Optional[bytes] = ...) -> None: ...
    class UserCounts(_message.Message):
        __slots__ = ("members", "online", "chatting", "in_game", "chat_room_members")
        MEMBERS_FIELD_NUMBER: _ClassVar[int]
        ONLINE_FIELD_NUMBER: _ClassVar[int]
        CHATTING_FIELD_NUMBER: _ClassVar[int]
        IN_GAME_FIELD_NUMBER: _ClassVar[int]
        CHAT_ROOM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        members: int
        online: int
        chatting: int
        in_game: int
        chat_room_members: int
        def __init__(self, members: _Optional[int] = ..., online: _Optional[int] = ..., chatting: _Optional[int] = ..., in_game: _Optional[int] = ..., chat_room_members: _Optional[int] = ...) -> None: ...
    class Event(_message.Message):
        __slots__ = ("gid", "event_time", "headline", "game_id", "just_posted")
        GID_FIELD_NUMBER: _ClassVar[int]
        EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
        HEADLINE_FIELD_NUMBER: _ClassVar[int]
        GAME_ID_FIELD_NUMBER: _ClassVar[int]
        JUST_POSTED_FIELD_NUMBER: _ClassVar[int]
        gid: int
        event_time: int
        headline: str
        game_id: int
        just_posted: bool
        def __init__(self, gid: _Optional[int] = ..., event_time: _Optional[int] = ..., headline: _Optional[str] = ..., game_id: _Optional[int] = ..., just_posted: bool = ...) -> None: ...
    STEAMID_CLAN_FIELD_NUMBER: _ClassVar[int]
    CLAN_ACCOUNT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    NAME_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_COUNTS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOM_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    steamid_clan: int
    clan_account_flags: int
    name_info: CMsgClientClanState.NameInfo
    user_counts: CMsgClientClanState.UserCounts
    events: _containers.RepeatedCompositeFieldContainer[CMsgClientClanState.Event]
    announcements: _containers.RepeatedCompositeFieldContainer[CMsgClientClanState.Event]
    chat_room_private: bool
    def __init__(self, steamid_clan: _Optional[int] = ..., clan_account_flags: _Optional[int] = ..., name_info: _Optional[_Union[CMsgClientClanState.NameInfo, _Mapping]] = ..., user_counts: _Optional[_Union[CMsgClientClanState.UserCounts, _Mapping]] = ..., events: _Optional[_Iterable[_Union[CMsgClientClanState.Event, _Mapping]]] = ..., announcements: _Optional[_Iterable[_Union[CMsgClientClanState.Event, _Mapping]]] = ..., chat_room_private: bool = ...) -> None: ...
