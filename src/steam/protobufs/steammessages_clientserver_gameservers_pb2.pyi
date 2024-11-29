import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgGSServerType(_message.Message):
    __slots__ = ("app_id_served", "flags", "deprecated_game_ip_address", "game_port", "game_dir", "game_version", "game_query_port", "game_port_local", "sdr_logon", "fake_ip")
    APP_ID_SERVED_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_GAME_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GAME_PORT_FIELD_NUMBER: _ClassVar[int]
    GAME_DIR_FIELD_NUMBER: _ClassVar[int]
    GAME_VERSION_FIELD_NUMBER: _ClassVar[int]
    GAME_QUERY_PORT_FIELD_NUMBER: _ClassVar[int]
    GAME_PORT_LOCAL_FIELD_NUMBER: _ClassVar[int]
    SDR_LOGON_FIELD_NUMBER: _ClassVar[int]
    FAKE_IP_FIELD_NUMBER: _ClassVar[int]
    app_id_served: int
    flags: int
    deprecated_game_ip_address: int
    game_port: int
    game_dir: str
    game_version: str
    game_query_port: int
    game_port_local: int
    sdr_logon: bytes
    fake_ip: int
    def __init__(self, app_id_served: _Optional[int] = ..., flags: _Optional[int] = ..., deprecated_game_ip_address: _Optional[int] = ..., game_port: _Optional[int] = ..., game_dir: _Optional[str] = ..., game_version: _Optional[str] = ..., game_query_port: _Optional[int] = ..., game_port_local: _Optional[int] = ..., sdr_logon: _Optional[bytes] = ..., fake_ip: _Optional[int] = ...) -> None: ...

class CMsgGSStatusReply(_message.Message):
    __slots__ = ("is_secure",)
    IS_SECURE_FIELD_NUMBER: _ClassVar[int]
    is_secure: bool
    def __init__(self, is_secure: bool = ...) -> None: ...

class CMsgGSPlayerList(_message.Message):
    __slots__ = ("players",)
    class Player(_message.Message):
        __slots__ = ("steam_id", "deprecated_public_ip", "token", "public_ip")
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        DEPRECATED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
        steam_id: int
        deprecated_public_ip: int
        token: bytes
        public_ip: _steammessages_base_pb2.CMsgIPAddress
        def __init__(self, steam_id: _Optional[int] = ..., deprecated_public_ip: _Optional[int] = ..., token: _Optional[bytes] = ..., public_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CMsgGSPlayerList.Player]
    def __init__(self, players: _Optional[_Iterable[_Union[CMsgGSPlayerList.Player, _Mapping]]] = ...) -> None: ...

class CMsgGSUserPlaying(_message.Message):
    __slots__ = ("steam_id", "deprecated_public_ip", "token", "public_ip")
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    deprecated_public_ip: int
    token: bytes
    public_ip: _steammessages_base_pb2.CMsgIPAddress
    def __init__(self, steam_id: _Optional[int] = ..., deprecated_public_ip: _Optional[int] = ..., token: _Optional[bytes] = ..., public_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...) -> None: ...

class CMsgGSDisconnectNotice(_message.Message):
    __slots__ = ("steam_id",)
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    def __init__(self, steam_id: _Optional[int] = ...) -> None: ...

class CMsgGameServerData(_message.Message):
    __slots__ = ("revision", "query_port", "game_port", "spectator_port", "server_name", "game_description", "spectator_server_name", "fake_ip", "sdr_ping_location", "app_id", "gamedir", "version", "product", "region", "players", "max_players", "bot_count", "password", "secure", "dedicated", "os", "game_data", "game_type", "map")
    class Player(_message.Message):
        __slots__ = ("steam_id",)
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        steam_id: int
        def __init__(self, steam_id: _Optional[int] = ...) -> None: ...
    REVISION_FIELD_NUMBER: _ClassVar[int]
    QUERY_PORT_FIELD_NUMBER: _ClassVar[int]
    GAME_PORT_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_PORT_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    GAME_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    FAKE_IP_FIELD_NUMBER: _ClassVar[int]
    SDR_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    GAMEDIR_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    MAX_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    BOT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    GAME_DATA_FIELD_NUMBER: _ClassVar[int]
    GAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    revision: int
    query_port: int
    game_port: int
    spectator_port: int
    server_name: str
    game_description: str
    spectator_server_name: str
    fake_ip: int
    sdr_ping_location: str
    app_id: int
    gamedir: str
    version: str
    product: str
    region: str
    players: _containers.RepeatedCompositeFieldContainer[CMsgGameServerData.Player]
    max_players: int
    bot_count: int
    password: bool
    secure: bool
    dedicated: bool
    os: str
    game_data: str
    game_type: str
    map: str
    def __init__(self, revision: _Optional[int] = ..., query_port: _Optional[int] = ..., game_port: _Optional[int] = ..., spectator_port: _Optional[int] = ..., server_name: _Optional[str] = ..., game_description: _Optional[str] = ..., spectator_server_name: _Optional[str] = ..., fake_ip: _Optional[int] = ..., sdr_ping_location: _Optional[str] = ..., app_id: _Optional[int] = ..., gamedir: _Optional[str] = ..., version: _Optional[str] = ..., product: _Optional[str] = ..., region: _Optional[str] = ..., players: _Optional[_Iterable[_Union[CMsgGameServerData.Player, _Mapping]]] = ..., max_players: _Optional[int] = ..., bot_count: _Optional[int] = ..., password: bool = ..., secure: bool = ..., dedicated: bool = ..., os: _Optional[str] = ..., game_data: _Optional[str] = ..., game_type: _Optional[str] = ..., map: _Optional[str] = ...) -> None: ...

class CMsgGameServerRemove(_message.Message):
    __slots__ = ("legacy_steam_id_gs", "legacy_query_port")
    LEGACY_STEAM_ID_GS_FIELD_NUMBER: _ClassVar[int]
    LEGACY_QUERY_PORT_FIELD_NUMBER: _ClassVar[int]
    legacy_steam_id_gs: int
    legacy_query_port: int
    def __init__(self, legacy_steam_id_gs: _Optional[int] = ..., legacy_query_port: _Optional[int] = ...) -> None: ...

class CMsgClientGMSServerQuery(_message.Message):
    __slots__ = ("app_id", "geo_location_ip", "region_code", "filter_text", "max_servers")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    GEO_LOCATION_IP_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    FILTER_TEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_SERVERS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    geo_location_ip: int
    region_code: int
    filter_text: str
    max_servers: int
    def __init__(self, app_id: _Optional[int] = ..., geo_location_ip: _Optional[int] = ..., region_code: _Optional[int] = ..., filter_text: _Optional[str] = ..., max_servers: _Optional[int] = ...) -> None: ...

class CMsgGMSClientServerQueryResponse(_message.Message):
    __slots__ = ("servers", "error", "default_server_data", "server_strings")
    class EFlags(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        k_EFlag_HasPassword: _ClassVar[CMsgGMSClientServerQueryResponse.EFlags]
        k_EFlag_Secure: _ClassVar[CMsgGMSClientServerQueryResponse.EFlags]
    k_EFlag_HasPassword: CMsgGMSClientServerQueryResponse.EFlags
    k_EFlag_Secure: CMsgGMSClientServerQueryResponse.EFlags
    class Server(_message.Message):
        __slots__ = ("deprecated_server_ip", "query_port", "auth_players", "server_ip", "steam_id", "revision", "players", "game_port", "sdr_popid", "sdr_ping_location", "flags", "app_id", "max_players", "bots", "spectator_port", "gamedir_str", "gamedir_strindex", "map_str", "map_strindex", "name_str", "name_strindex", "game_description_str", "game_description_strindex", "version_str", "version_strindex", "gametype_str", "gametype_strindex", "spectator_name_str", "spectator_name_strindex")
        DEPRECATED_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        QUERY_PORT_FIELD_NUMBER: _ClassVar[int]
        AUTH_PLAYERS_FIELD_NUMBER: _ClassVar[int]
        SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        REVISION_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        GAME_PORT_FIELD_NUMBER: _ClassVar[int]
        SDR_POPID_FIELD_NUMBER: _ClassVar[int]
        SDR_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
        FLAGS_FIELD_NUMBER: _ClassVar[int]
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_PLAYERS_FIELD_NUMBER: _ClassVar[int]
        BOTS_FIELD_NUMBER: _ClassVar[int]
        SPECTATOR_PORT_FIELD_NUMBER: _ClassVar[int]
        GAMEDIR_STR_FIELD_NUMBER: _ClassVar[int]
        GAMEDIR_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        MAP_STR_FIELD_NUMBER: _ClassVar[int]
        MAP_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_STR_FIELD_NUMBER: _ClassVar[int]
        NAME_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        GAME_DESCRIPTION_STR_FIELD_NUMBER: _ClassVar[int]
        GAME_DESCRIPTION_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        VERSION_STR_FIELD_NUMBER: _ClassVar[int]
        VERSION_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        GAMETYPE_STR_FIELD_NUMBER: _ClassVar[int]
        GAMETYPE_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        SPECTATOR_NAME_STR_FIELD_NUMBER: _ClassVar[int]
        SPECTATOR_NAME_STRINDEX_FIELD_NUMBER: _ClassVar[int]
        deprecated_server_ip: int
        query_port: int
        auth_players: int
        server_ip: _steammessages_base_pb2.CMsgIPAddress
        steam_id: int
        revision: int
        players: int
        game_port: int
        sdr_popid: int
        sdr_ping_location: str
        flags: int
        app_id: int
        max_players: int
        bots: int
        spectator_port: int
        gamedir_str: str
        gamedir_strindex: int
        map_str: str
        map_strindex: int
        name_str: str
        name_strindex: int
        game_description_str: str
        game_description_strindex: int
        version_str: str
        version_strindex: int
        gametype_str: str
        gametype_strindex: int
        spectator_name_str: str
        spectator_name_strindex: int
        def __init__(self, deprecated_server_ip: _Optional[int] = ..., query_port: _Optional[int] = ..., auth_players: _Optional[int] = ..., server_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., steam_id: _Optional[int] = ..., revision: _Optional[int] = ..., players: _Optional[int] = ..., game_port: _Optional[int] = ..., sdr_popid: _Optional[int] = ..., sdr_ping_location: _Optional[str] = ..., flags: _Optional[int] = ..., app_id: _Optional[int] = ..., max_players: _Optional[int] = ..., bots: _Optional[int] = ..., spectator_port: _Optional[int] = ..., gamedir_str: _Optional[str] = ..., gamedir_strindex: _Optional[int] = ..., map_str: _Optional[str] = ..., map_strindex: _Optional[int] = ..., name_str: _Optional[str] = ..., name_strindex: _Optional[int] = ..., game_description_str: _Optional[str] = ..., game_description_strindex: _Optional[int] = ..., version_str: _Optional[str] = ..., version_strindex: _Optional[int] = ..., gametype_str: _Optional[str] = ..., gametype_strindex: _Optional[int] = ..., spectator_name_str: _Optional[str] = ..., spectator_name_strindex: _Optional[int] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SERVER_DATA_FIELD_NUMBER: _ClassVar[int]
    SERVER_STRINGS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[CMsgGMSClientServerQueryResponse.Server]
    error: str
    default_server_data: CMsgGMSClientServerQueryResponse.Server
    server_strings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, servers: _Optional[_Iterable[_Union[CMsgGMSClientServerQueryResponse.Server, _Mapping]]] = ..., error: _Optional[str] = ..., default_server_data: _Optional[_Union[CMsgGMSClientServerQueryResponse.Server, _Mapping]] = ..., server_strings: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgGameServerOutOfDate(_message.Message):
    __slots__ = ("steam_id_gs", "reject", "message")
    STEAM_ID_GS_FIELD_NUMBER: _ClassVar[int]
    REJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    steam_id_gs: int
    reject: bool
    message: str
    def __init__(self, steam_id_gs: _Optional[int] = ..., reject: bool = ..., message: _Optional[str] = ...) -> None: ...

class CMsgGSAssociateWithClan(_message.Message):
    __slots__ = ("steam_id_clan",)
    STEAM_ID_CLAN_FIELD_NUMBER: _ClassVar[int]
    steam_id_clan: int
    def __init__(self, steam_id_clan: _Optional[int] = ...) -> None: ...

class CMsgGSAssociateWithClanResponse(_message.Message):
    __slots__ = ("steam_id_clan", "eresult")
    STEAM_ID_CLAN_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    steam_id_clan: int
    eresult: int
    def __init__(self, steam_id_clan: _Optional[int] = ..., eresult: _Optional[int] = ...) -> None: ...

class CMsgGSComputeNewPlayerCompatibility(_message.Message):
    __slots__ = ("steam_id_candidate",)
    STEAM_ID_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    steam_id_candidate: int
    def __init__(self, steam_id_candidate: _Optional[int] = ...) -> None: ...

class CMsgGSComputeNewPlayerCompatibilityResponse(_message.Message):
    __slots__ = ("steam_id_candidate", "eresult", "is_clan_member", "ct_dont_like_you", "ct_you_dont_like", "ct_clanmembers_dont_like_you")
    STEAM_ID_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    IS_CLAN_MEMBER_FIELD_NUMBER: _ClassVar[int]
    CT_DONT_LIKE_YOU_FIELD_NUMBER: _ClassVar[int]
    CT_YOU_DONT_LIKE_FIELD_NUMBER: _ClassVar[int]
    CT_CLANMEMBERS_DONT_LIKE_YOU_FIELD_NUMBER: _ClassVar[int]
    steam_id_candidate: int
    eresult: int
    is_clan_member: bool
    ct_dont_like_you: int
    ct_you_dont_like: int
    ct_clanmembers_dont_like_you: int
    def __init__(self, steam_id_candidate: _Optional[int] = ..., eresult: _Optional[int] = ..., is_clan_member: bool = ..., ct_dont_like_you: _Optional[int] = ..., ct_you_dont_like: _Optional[int] = ..., ct_clanmembers_dont_like_you: _Optional[int] = ...) -> None: ...
