import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EMMSLobbyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMMSLobbyStatusInvalid: _ClassVar[EMMSLobbyStatus]
    k_EMMSLobbyStatusExists: _ClassVar[EMMSLobbyStatus]
    k_EMMSLobbyStatusDoesNotExist: _ClassVar[EMMSLobbyStatus]
    k_EMMSLobbyStatusNotAMember: _ClassVar[EMMSLobbyStatus]
k_EMMSLobbyStatusInvalid: EMMSLobbyStatus
k_EMMSLobbyStatusExists: EMMSLobbyStatus
k_EMMSLobbyStatusDoesNotExist: EMMSLobbyStatus
k_EMMSLobbyStatusNotAMember: EMMSLobbyStatus

class CMsgClientMMSSetRatelimitPolicyOnClient(_message.Message):
    __slots__ = ("app_id", "enable_rate_limits", "seconds_per_message", "milliseconds_per_data_update")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RATE_LIMITS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_PER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MILLISECONDS_PER_DATA_UPDATE_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    enable_rate_limits: bool
    seconds_per_message: int
    milliseconds_per_data_update: int
    def __init__(self, app_id: _Optional[int] = ..., enable_rate_limits: bool = ..., seconds_per_message: _Optional[int] = ..., milliseconds_per_data_update: _Optional[int] = ...) -> None: ...

class CMsgClientMMSCreateLobby(_message.Message):
    __slots__ = ("app_id", "max_members", "lobby_type", "lobby_flags", "cell_id", "deprecated_public_ip", "metadata", "persona_name_owner", "public_ip", "network_ping_location")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    LOBBY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_FLAGS_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_OWNER_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    max_members: int
    lobby_type: int
    lobby_flags: int
    cell_id: int
    deprecated_public_ip: int
    metadata: bytes
    persona_name_owner: str
    public_ip: _steammessages_base_pb2.CMsgIPAddress
    network_ping_location: str
    def __init__(self, app_id: _Optional[int] = ..., max_members: _Optional[int] = ..., lobby_type: _Optional[int] = ..., lobby_flags: _Optional[int] = ..., cell_id: _Optional[int] = ..., deprecated_public_ip: _Optional[int] = ..., metadata: _Optional[bytes] = ..., persona_name_owner: _Optional[str] = ..., public_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., network_ping_location: _Optional[str] = ...) -> None: ...

class CMsgClientMMSCreateLobbyResponse(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "eresult")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    eresult: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., eresult: _Optional[int] = ...) -> None: ...

class CMsgClientMMSJoinLobby(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "persona_name", "network_ping_location", "cell_id")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    persona_name: str
    network_ping_location: str
    cell_id: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., persona_name: _Optional[str] = ..., network_ping_location: _Optional[str] = ..., cell_id: _Optional[int] = ...) -> None: ...

class CMsgClientMMSJoinLobbyResponse(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "chat_room_enter_response", "max_members", "lobby_type", "lobby_flags", "steam_id_owner", "metadata", "members")
    class Member(_message.Message):
        __slots__ = ("steam_id", "persona_name", "metadata")
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        steam_id: int
        persona_name: str
        metadata: bytes
        def __init__(self, steam_id: _Optional[int] = ..., persona_name: _Optional[str] = ..., metadata: _Optional[bytes] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOM_ENTER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    LOBBY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_FLAGS_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_OWNER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    chat_room_enter_response: int
    max_members: int
    lobby_type: int
    lobby_flags: int
    steam_id_owner: int
    metadata: bytes
    members: _containers.RepeatedCompositeFieldContainer[CMsgClientMMSJoinLobbyResponse.Member]
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., chat_room_enter_response: _Optional[int] = ..., max_members: _Optional[int] = ..., lobby_type: _Optional[int] = ..., lobby_flags: _Optional[int] = ..., steam_id_owner: _Optional[int] = ..., metadata: _Optional[bytes] = ..., members: _Optional[_Iterable[_Union[CMsgClientMMSJoinLobbyResponse.Member, _Mapping]]] = ...) -> None: ...

class CMsgClientMMSLeaveLobby(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ...) -> None: ...

class CMsgClientMMSLeaveLobbyResponse(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "eresult")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    eresult: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., eresult: _Optional[int] = ...) -> None: ...

class CMsgClientMMSGetLobbyList(_message.Message):
    __slots__ = ("app_id", "num_lobbies_requested", "cell_id", "deprecated_public_ip", "filters", "public_ip", "network_ping_location")
    class Filter(_message.Message):
        __slots__ = ("key", "value", "comparision", "filter_type")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        COMPARISION_FIELD_NUMBER: _ClassVar[int]
        FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        comparision: int
        filter_type: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., comparision: _Optional[int] = ..., filter_type: _Optional[int] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_LOBBIES_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    num_lobbies_requested: int
    cell_id: int
    deprecated_public_ip: int
    filters: _containers.RepeatedCompositeFieldContainer[CMsgClientMMSGetLobbyList.Filter]
    public_ip: _steammessages_base_pb2.CMsgIPAddress
    network_ping_location: str
    def __init__(self, app_id: _Optional[int] = ..., num_lobbies_requested: _Optional[int] = ..., cell_id: _Optional[int] = ..., deprecated_public_ip: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[CMsgClientMMSGetLobbyList.Filter, _Mapping]]] = ..., public_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., network_ping_location: _Optional[str] = ...) -> None: ...

class CMsgClientMMSGetLobbyListResponse(_message.Message):
    __slots__ = ("app_id", "eresult", "lobbies")
    class Lobby(_message.Message):
        __slots__ = ("steam_id", "max_members", "lobby_type", "lobby_flags", "metadata", "num_members", "distance", "weight", "ping", "missing_ping")
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        LOBBY_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOBBY_FLAGS_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        PING_FIELD_NUMBER: _ClassVar[int]
        MISSING_PING_FIELD_NUMBER: _ClassVar[int]
        steam_id: int
        max_members: int
        lobby_type: int
        lobby_flags: int
        metadata: bytes
        num_members: int
        distance: float
        weight: int
        ping: int
        missing_ping: int
        def __init__(self, steam_id: _Optional[int] = ..., max_members: _Optional[int] = ..., lobby_type: _Optional[int] = ..., lobby_flags: _Optional[int] = ..., metadata: _Optional[bytes] = ..., num_members: _Optional[int] = ..., distance: _Optional[float] = ..., weight: _Optional[int] = ..., ping: _Optional[int] = ..., missing_ping: _Optional[int] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    LOBBIES_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    eresult: int
    lobbies: _containers.RepeatedCompositeFieldContainer[CMsgClientMMSGetLobbyListResponse.Lobby]
    def __init__(self, app_id: _Optional[int] = ..., eresult: _Optional[int] = ..., lobbies: _Optional[_Iterable[_Union[CMsgClientMMSGetLobbyListResponse.Lobby, _Mapping]]] = ...) -> None: ...

class CMsgClientMMSSetLobbyData(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_member", "max_members", "lobby_type", "lobby_flags", "metadata", "network_ping_location")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_MEMBER_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    LOBBY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_FLAGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_member: int
    max_members: int
    lobby_type: int
    lobby_flags: int
    metadata: bytes
    network_ping_location: str
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_member: _Optional[int] = ..., max_members: _Optional[int] = ..., lobby_type: _Optional[int] = ..., lobby_flags: _Optional[int] = ..., metadata: _Optional[bytes] = ..., network_ping_location: _Optional[str] = ...) -> None: ...

class CMsgClientMMSSetLobbyDataResponse(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "eresult")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    eresult: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., eresult: _Optional[int] = ...) -> None: ...

class CMsgClientMMSGetLobbyData(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ...) -> None: ...

class CMsgClientMMSLobbyData(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "num_members", "max_members", "lobby_type", "lobby_flags", "steam_id_owner", "metadata", "members", "lobby_cellid", "owner_should_accept_changes")
    class Member(_message.Message):
        __slots__ = ("steam_id", "persona_name", "metadata", "ping_data")
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        PING_DATA_FIELD_NUMBER: _ClassVar[int]
        steam_id: int
        persona_name: str
        metadata: bytes
        ping_data: str
        def __init__(self, steam_id: _Optional[int] = ..., persona_name: _Optional[str] = ..., metadata: _Optional[bytes] = ..., ping_data: _Optional[str] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    NUM_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    LOBBY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOBBY_FLAGS_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_OWNER_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    LOBBY_CELLID_FIELD_NUMBER: _ClassVar[int]
    OWNER_SHOULD_ACCEPT_CHANGES_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    num_members: int
    max_members: int
    lobby_type: int
    lobby_flags: int
    steam_id_owner: int
    metadata: bytes
    members: _containers.RepeatedCompositeFieldContainer[CMsgClientMMSLobbyData.Member]
    lobby_cellid: int
    owner_should_accept_changes: bool
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., num_members: _Optional[int] = ..., max_members: _Optional[int] = ..., lobby_type: _Optional[int] = ..., lobby_flags: _Optional[int] = ..., steam_id_owner: _Optional[int] = ..., metadata: _Optional[bytes] = ..., members: _Optional[_Iterable[_Union[CMsgClientMMSLobbyData.Member, _Mapping]]] = ..., lobby_cellid: _Optional[int] = ..., owner_should_accept_changes: bool = ...) -> None: ...

class CMsgClientMMSSendLobbyChatMsg(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_target", "lobby_message")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_TARGET_FIELD_NUMBER: _ClassVar[int]
    LOBBY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_target: int
    lobby_message: bytes
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_target: _Optional[int] = ..., lobby_message: _Optional[bytes] = ...) -> None: ...

class CMsgClientMMSLobbyChatMsg(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_sender", "lobby_message")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_SENDER_FIELD_NUMBER: _ClassVar[int]
    LOBBY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_sender: int
    lobby_message: bytes
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_sender: _Optional[int] = ..., lobby_message: _Optional[bytes] = ...) -> None: ...

class CMsgClientMMSSetLobbyOwner(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_new_owner")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_NEW_OWNER_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_new_owner: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_new_owner: _Optional[int] = ...) -> None: ...

class CMsgClientMMSSetLobbyOwnerResponse(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "eresult")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    eresult: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., eresult: _Optional[int] = ...) -> None: ...

class CMsgClientMMSSetLobbyLinked(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_lobby2")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY2_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_lobby2: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_lobby2: _Optional[int] = ...) -> None: ...

class CMsgClientMMSSetLobbyGameServer(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "deprecated_game_server_ip", "game_server_port", "game_server_steam_id", "game_server_ip", "network_ping_location")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_GAME_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    NETWORK_PING_LOCATION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    deprecated_game_server_ip: int
    game_server_port: int
    game_server_steam_id: int
    game_server_ip: _steammessages_base_pb2.CMsgIPAddress
    network_ping_location: str
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., deprecated_game_server_ip: _Optional[int] = ..., game_server_port: _Optional[int] = ..., game_server_steam_id: _Optional[int] = ..., game_server_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., network_ping_location: _Optional[str] = ...) -> None: ...

class CMsgClientMMSLobbyGameServerSet(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "deprecated_game_server_ip", "game_server_port", "game_server_steam_id", "game_server_ip")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_GAME_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    deprecated_game_server_ip: int
    game_server_port: int
    game_server_steam_id: int
    game_server_ip: _steammessages_base_pb2.CMsgIPAddress
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., deprecated_game_server_ip: _Optional[int] = ..., game_server_port: _Optional[int] = ..., game_server_steam_id: _Optional[int] = ..., game_server_ip: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ...) -> None: ...

class CMsgClientMMSUserJoinedLobby(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_user", "persona_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_USER_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_user: int
    persona_name: str
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_user: _Optional[int] = ..., persona_name: _Optional[str] = ...) -> None: ...

class CMsgClientMMSUserLeftLobby(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_user", "persona_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_USER_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_user: int
    persona_name: str
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_user: _Optional[int] = ..., persona_name: _Optional[str] = ...) -> None: ...

class CMsgClientMMSInviteToLobby(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "steam_id_user_invited")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_USER_INVITED_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    steam_id_user_invited: int
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., steam_id_user_invited: _Optional[int] = ...) -> None: ...

class CMsgClientMMSGetLobbyStatus(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "claim_membership", "claim_ownership")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    CLAIM_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    CLAIM_OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    claim_membership: bool
    claim_ownership: bool
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., claim_membership: bool = ..., claim_ownership: bool = ...) -> None: ...

class CMsgClientMMSGetLobbyStatusResponse(_message.Message):
    __slots__ = ("app_id", "steam_id_lobby", "lobby_status")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    LOBBY_STATUS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steam_id_lobby: int
    lobby_status: EMMSLobbyStatus
    def __init__(self, app_id: _Optional[int] = ..., steam_id_lobby: _Optional[int] = ..., lobby_status: _Optional[_Union[EMMSLobbyStatus, str]] = ...) -> None: ...
