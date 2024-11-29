import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGameServers_GetServerList_Request(_message.Message):
    __slots__ = ("filter", "limit")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    filter: str
    limit: int
    def __init__(self, filter: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class CGameServers_GetServerList_Response(_message.Message):
    __slots__ = ("servers",)
    class Server(_message.Message):
        __slots__ = ("addr", "gameport", "specport", "steamid", "name", "appid", "gamedir", "version", "product", "region", "players", "max_players", "bots", "map", "secure", "dedicated", "os", "gametype")
        ADDR_FIELD_NUMBER: _ClassVar[int]
        GAMEPORT_FIELD_NUMBER: _ClassVar[int]
        SPECPORT_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        GAMEDIR_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        MAX_PLAYERS_FIELD_NUMBER: _ClassVar[int]
        BOTS_FIELD_NUMBER: _ClassVar[int]
        MAP_FIELD_NUMBER: _ClassVar[int]
        SECURE_FIELD_NUMBER: _ClassVar[int]
        DEDICATED_FIELD_NUMBER: _ClassVar[int]
        OS_FIELD_NUMBER: _ClassVar[int]
        GAMETYPE_FIELD_NUMBER: _ClassVar[int]
        addr: str
        gameport: int
        specport: int
        steamid: int
        name: str
        appid: int
        gamedir: str
        version: str
        product: str
        region: int
        players: int
        max_players: int
        bots: int
        map: str
        secure: bool
        dedicated: bool
        os: str
        gametype: str
        def __init__(self, addr: _Optional[str] = ..., gameport: _Optional[int] = ..., specport: _Optional[int] = ..., steamid: _Optional[int] = ..., name: _Optional[str] = ..., appid: _Optional[int] = ..., gamedir: _Optional[str] = ..., version: _Optional[str] = ..., product: _Optional[str] = ..., region: _Optional[int] = ..., players: _Optional[int] = ..., max_players: _Optional[int] = ..., bots: _Optional[int] = ..., map: _Optional[str] = ..., secure: bool = ..., dedicated: bool = ..., os: _Optional[str] = ..., gametype: _Optional[str] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[CGameServers_GetServerList_Response.Server]
    def __init__(self, servers: _Optional[_Iterable[_Union[CGameServers_GetServerList_Response.Server, _Mapping]]] = ...) -> None: ...

class CGameServers_GetServerSteamIDsByIP_Request(_message.Message):
    __slots__ = ("server_ips",)
    SERVER_IPS_FIELD_NUMBER: _ClassVar[int]
    server_ips: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, server_ips: _Optional[_Iterable[str]] = ...) -> None: ...

class CGameServers_IPsWithSteamIDs_Response(_message.Message):
    __slots__ = ("servers",)
    class Server(_message.Message):
        __slots__ = ("addr", "steamid")
        ADDR_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        addr: str
        steamid: int
        def __init__(self, addr: _Optional[str] = ..., steamid: _Optional[int] = ...) -> None: ...
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[CGameServers_IPsWithSteamIDs_Response.Server]
    def __init__(self, servers: _Optional[_Iterable[_Union[CGameServers_IPsWithSteamIDs_Response.Server, _Mapping]]] = ...) -> None: ...

class CGameServers_GetServerIPsBySteamID_Request(_message.Message):
    __slots__ = ("server_steamids",)
    SERVER_STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    server_steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, server_steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CGameServers_QueryByFakeIP_Request(_message.Message):
    __slots__ = ("fake_ip", "fake_port", "app_id", "query_type")
    class EQueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Query_Invalid: _ClassVar[CGameServers_QueryByFakeIP_Request.EQueryType]
        Query_Ping: _ClassVar[CGameServers_QueryByFakeIP_Request.EQueryType]
        Query_Players: _ClassVar[CGameServers_QueryByFakeIP_Request.EQueryType]
        Query_Rules: _ClassVar[CGameServers_QueryByFakeIP_Request.EQueryType]
    Query_Invalid: CGameServers_QueryByFakeIP_Request.EQueryType
    Query_Ping: CGameServers_QueryByFakeIP_Request.EQueryType
    Query_Players: CGameServers_QueryByFakeIP_Request.EQueryType
    Query_Rules: CGameServers_QueryByFakeIP_Request.EQueryType
    FAKE_IP_FIELD_NUMBER: _ClassVar[int]
    FAKE_PORT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    fake_ip: int
    fake_port: int
    app_id: int
    query_type: CGameServers_QueryByFakeIP_Request.EQueryType
    def __init__(self, fake_ip: _Optional[int] = ..., fake_port: _Optional[int] = ..., app_id: _Optional[int] = ..., query_type: _Optional[_Union[CGameServers_QueryByFakeIP_Request.EQueryType, str]] = ...) -> None: ...

class CMsgGameServerPingQueryData(_message.Message):
    __slots__ = ("server_ip", "query_port", "game_port", "spectator_port", "spectator_server_name", "server_name", "steamid", "app_id", "gamedir", "map", "game_description", "gametype", "num_players", "max_players", "num_bots", "password", "secure", "dedicated", "version", "sdr_popid", "sdr_location_string")
    SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    QUERY_PORT_FIELD_NUMBER: _ClassVar[int]
    GAME_PORT_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_PORT_FIELD_NUMBER: _ClassVar[int]
    SPECTATOR_SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    GAMEDIR_FIELD_NUMBER: _ClassVar[int]
    MAP_FIELD_NUMBER: _ClassVar[int]
    GAME_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GAMETYPE_FIELD_NUMBER: _ClassVar[int]
    NUM_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    MAX_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    NUM_BOTS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SDR_POPID_FIELD_NUMBER: _ClassVar[int]
    SDR_LOCATION_STRING_FIELD_NUMBER: _ClassVar[int]
    server_ip: _steammessages_base_pb2.CMsgIPAddress
    query_port: int
    game_port: int
    spectator_port: int
    spectator_server_name: str
    server_name: str
    steamid: int
    app_id: int
    gamedir: str
    map: str
    game_description: str
    gametype: str
    num_players: int
    max_players: int
    num_bots: int
    password: bool
    secure: bool
    dedicated: bool
    version: str
    sdr_popid: int
    sdr_location_string: str
    def __init__(self, server_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., query_port: _Optional[int] = ..., game_port: _Optional[int] = ..., spectator_port: _Optional[int] = ..., spectator_server_name: _Optional[str] = ..., server_name: _Optional[str] = ..., steamid: _Optional[int] = ..., app_id: _Optional[int] = ..., gamedir: _Optional[str] = ..., map: _Optional[str] = ..., game_description: _Optional[str] = ..., gametype: _Optional[str] = ..., num_players: _Optional[int] = ..., max_players: _Optional[int] = ..., num_bots: _Optional[int] = ..., password: bool = ..., secure: bool = ..., dedicated: bool = ..., version: _Optional[str] = ..., sdr_popid: _Optional[int] = ..., sdr_location_string: _Optional[str] = ...) -> None: ...

class CMsgGameServerPlayersQueryData(_message.Message):
    __slots__ = ("players",)
    class Player(_message.Message):
        __slots__ = ("name", "score", "time_played")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        TIME_PLAYED_FIELD_NUMBER: _ClassVar[int]
        name: str
        score: int
        time_played: int
        def __init__(self, name: _Optional[str] = ..., score: _Optional[int] = ..., time_played: _Optional[int] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CMsgGameServerPlayersQueryData.Player]
    def __init__(self, players: _Optional[_Iterable[_Union[CMsgGameServerPlayersQueryData.Player, _Mapping]]] = ...) -> None: ...

class CMsgGameServerRulesQueryData(_message.Message):
    __slots__ = ("rules",)
    class Rule(_message.Message):
        __slots__ = ("rule", "value")
        RULE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        rule: str
        value: str
        def __init__(self, rule: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[CMsgGameServerRulesQueryData.Rule]
    def __init__(self, rules: _Optional[_Iterable[_Union[CMsgGameServerRulesQueryData.Rule, _Mapping]]] = ...) -> None: ...

class CGameServers_GameServerQuery_Response(_message.Message):
    __slots__ = ("ping_data", "players_data", "rules_data")
    PING_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_DATA_FIELD_NUMBER: _ClassVar[int]
    RULES_DATA_FIELD_NUMBER: _ClassVar[int]
    ping_data: CMsgGameServerPingQueryData
    players_data: CMsgGameServerPlayersQueryData
    rules_data: CMsgGameServerRulesQueryData
    def __init__(self, ping_data: _Optional[_Union[CMsgGameServerPingQueryData, _Mapping]] = ..., players_data: _Optional[_Union[CMsgGameServerPlayersQueryData, _Mapping]] = ..., rules_data: _Optional[_Union[CMsgGameServerRulesQueryData, _Mapping]] = ...) -> None: ...

class GameServerClient_QueryServerData_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GameServerClient_QueryServerData_Response(_message.Message):
    __slots__ = ("ping_data", "players_data", "rules_data")
    PING_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_DATA_FIELD_NUMBER: _ClassVar[int]
    RULES_DATA_FIELD_NUMBER: _ClassVar[int]
    ping_data: CMsgGameServerPingQueryData
    players_data: CMsgGameServerPlayersQueryData
    rules_data: CMsgGameServerRulesQueryData
    def __init__(self, ping_data: _Optional[_Union[CMsgGameServerPingQueryData, _Mapping]] = ..., players_data: _Optional[_Union[CMsgGameServerPlayersQueryData, _Mapping]] = ..., rules_data: _Optional[_Union[CMsgGameServerRulesQueryData, _Mapping]] = ...) -> None: ...

class GameServers(_service.service): ...

class GameServers_Stub(GameServers): ...

class GameServerClient(_service.service): ...

class GameServerClient_Stub(GameServerClient): ...
