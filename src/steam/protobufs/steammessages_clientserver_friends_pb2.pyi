import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientFriendMsg(_message.Message):
    __slots__ = ("steamid", "chat_entry_type", "message", "rtime32_server_timestamp", "echo_to_sender")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RTIME32_SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ECHO_TO_SENDER_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    chat_entry_type: int
    message: bytes
    rtime32_server_timestamp: int
    echo_to_sender: bool
    def __init__(self, steamid: _Optional[int] = ..., chat_entry_type: _Optional[int] = ..., message: _Optional[bytes] = ..., rtime32_server_timestamp: _Optional[int] = ..., echo_to_sender: bool = ...) -> None: ...

class CMsgClientFriendMsgIncoming(_message.Message):
    __slots__ = ("steamid_from", "chat_entry_type", "from_limited_account", "message", "rtime32_server_timestamp")
    STEAMID_FROM_FIELD_NUMBER: _ClassVar[int]
    CHAT_ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_LIMITED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RTIME32_SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    steamid_from: int
    chat_entry_type: int
    from_limited_account: bool
    message: bytes
    rtime32_server_timestamp: int
    def __init__(self, steamid_from: _Optional[int] = ..., chat_entry_type: _Optional[int] = ..., from_limited_account: bool = ..., message: _Optional[bytes] = ..., rtime32_server_timestamp: _Optional[int] = ...) -> None: ...

class CMsgClientAddFriend(_message.Message):
    __slots__ = ("steamid_to_add", "accountname_or_email_to_add")
    STEAMID_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNAME_OR_EMAIL_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    steamid_to_add: int
    accountname_or_email_to_add: str
    def __init__(self, steamid_to_add: _Optional[int] = ..., accountname_or_email_to_add: _Optional[str] = ...) -> None: ...

class CMsgClientAddFriendResponse(_message.Message):
    __slots__ = ("eresult", "steam_id_added", "persona_name_added")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_ADDED_FIELD_NUMBER: _ClassVar[int]
    PERSONA_NAME_ADDED_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    steam_id_added: int
    persona_name_added: str
    def __init__(self, eresult: _Optional[int] = ..., steam_id_added: _Optional[int] = ..., persona_name_added: _Optional[str] = ...) -> None: ...

class CMsgClientRemoveFriend(_message.Message):
    __slots__ = ("friendid",)
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    friendid: int
    def __init__(self, friendid: _Optional[int] = ...) -> None: ...

class CMsgClientHideFriend(_message.Message):
    __slots__ = ("friendid", "hide")
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    HIDE_FIELD_NUMBER: _ClassVar[int]
    friendid: int
    hide: bool
    def __init__(self, friendid: _Optional[int] = ..., hide: bool = ...) -> None: ...

class CMsgClientFriendsList(_message.Message):
    __slots__ = ("bincremental", "friends", "max_friend_count", "active_friend_count", "friends_limit_hit")
    class Friend(_message.Message):
        __slots__ = ("ulfriendid", "efriendrelationship")
        ULFRIENDID_FIELD_NUMBER: _ClassVar[int]
        EFRIENDRELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
        ulfriendid: int
        efriendrelationship: int
        def __init__(self, ulfriendid: _Optional[int] = ..., efriendrelationship: _Optional[int] = ...) -> None: ...
    BINCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    MAX_FRIEND_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FRIEND_COUNT_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_LIMIT_HIT_FIELD_NUMBER: _ClassVar[int]
    bincremental: bool
    friends: _containers.RepeatedCompositeFieldContainer[CMsgClientFriendsList.Friend]
    max_friend_count: int
    active_friend_count: int
    friends_limit_hit: bool
    def __init__(self, bincremental: bool = ..., friends: _Optional[_Iterable[_Union[CMsgClientFriendsList.Friend, _Mapping]]] = ..., max_friend_count: _Optional[int] = ..., active_friend_count: _Optional[int] = ..., friends_limit_hit: bool = ...) -> None: ...

class CMsgClientFriendsGroupsList(_message.Message):
    __slots__ = ("bremoval", "bincremental", "friendGroups", "memberships")
    class FriendGroup(_message.Message):
        __slots__ = ("nGroupID", "strGroupName")
        NGROUPID_FIELD_NUMBER: _ClassVar[int]
        STRGROUPNAME_FIELD_NUMBER: _ClassVar[int]
        nGroupID: int
        strGroupName: str
        def __init__(self, nGroupID: _Optional[int] = ..., strGroupName: _Optional[str] = ...) -> None: ...
    class FriendGroupsMembership(_message.Message):
        __slots__ = ("ulSteamID", "nGroupID")
        ULSTEAMID_FIELD_NUMBER: _ClassVar[int]
        NGROUPID_FIELD_NUMBER: _ClassVar[int]
        ulSteamID: int
        nGroupID: int
        def __init__(self, ulSteamID: _Optional[int] = ..., nGroupID: _Optional[int] = ...) -> None: ...
    BREMOVAL_FIELD_NUMBER: _ClassVar[int]
    BINCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    FRIENDGROUPS_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIPS_FIELD_NUMBER: _ClassVar[int]
    bremoval: bool
    bincremental: bool
    friendGroups: _containers.RepeatedCompositeFieldContainer[CMsgClientFriendsGroupsList.FriendGroup]
    memberships: _containers.RepeatedCompositeFieldContainer[CMsgClientFriendsGroupsList.FriendGroupsMembership]
    def __init__(self, bremoval: bool = ..., bincremental: bool = ..., friendGroups: _Optional[_Iterable[_Union[CMsgClientFriendsGroupsList.FriendGroup, _Mapping]]] = ..., memberships: _Optional[_Iterable[_Union[CMsgClientFriendsGroupsList.FriendGroupsMembership, _Mapping]]] = ...) -> None: ...

class CMsgClientPlayerNicknameList(_message.Message):
    __slots__ = ("removal", "incremental", "nicknames")
    class PlayerNickname(_message.Message):
        __slots__ = ("steamid", "nickname")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        NICKNAME_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        nickname: str
        def __init__(self, steamid: _Optional[int] = ..., nickname: _Optional[str] = ...) -> None: ...
    REMOVAL_FIELD_NUMBER: _ClassVar[int]
    INCREMENTAL_FIELD_NUMBER: _ClassVar[int]
    NICKNAMES_FIELD_NUMBER: _ClassVar[int]
    removal: bool
    incremental: bool
    nicknames: _containers.RepeatedCompositeFieldContainer[CMsgClientPlayerNicknameList.PlayerNickname]
    def __init__(self, removal: bool = ..., incremental: bool = ..., nicknames: _Optional[_Iterable[_Union[CMsgClientPlayerNicknameList.PlayerNickname, _Mapping]]] = ...) -> None: ...

class CMsgClientSetPlayerNickname(_message.Message):
    __slots__ = ("steamid", "nickname")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    nickname: str
    def __init__(self, steamid: _Optional[int] = ..., nickname: _Optional[str] = ...) -> None: ...

class CMsgClientSetPlayerNicknameResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientRequestFriendData(_message.Message):
    __slots__ = ("persona_state_requested", "friends")
    PERSONA_STATE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    persona_state_requested: int
    friends: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, persona_state_requested: _Optional[int] = ..., friends: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientChangeStatus(_message.Message):
    __slots__ = ("persona_state", "player_name", "is_auto_generated_name", "high_priority", "persona_set_by_user", "persona_state_flags", "need_persona_response", "is_client_idle")
    PERSONA_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_GENERATED_NAME_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    PERSONA_SET_BY_USER_FIELD_NUMBER: _ClassVar[int]
    PERSONA_STATE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    NEED_PERSONA_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    IS_CLIENT_IDLE_FIELD_NUMBER: _ClassVar[int]
    persona_state: int
    player_name: str
    is_auto_generated_name: bool
    high_priority: bool
    persona_set_by_user: bool
    persona_state_flags: int
    need_persona_response: bool
    is_client_idle: bool
    def __init__(self, persona_state: _Optional[int] = ..., player_name: _Optional[str] = ..., is_auto_generated_name: bool = ..., high_priority: bool = ..., persona_set_by_user: bool = ..., persona_state_flags: _Optional[int] = ..., need_persona_response: bool = ..., is_client_idle: bool = ...) -> None: ...

class CMsgPersonaChangeResponse(_message.Message):
    __slots__ = ("result", "player_name")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    result: int
    player_name: str
    def __init__(self, result: _Optional[int] = ..., player_name: _Optional[str] = ...) -> None: ...

class CMsgClientPersonaState(_message.Message):
    __slots__ = ("status_flags", "friends")
    class Friend(_message.Message):
        __slots__ = ("friendid", "persona_state", "game_played_app_id", "game_server_ip", "game_server_port", "persona_state_flags", "online_session_instances", "persona_set_by_user", "player_name", "query_port", "steamid_source", "avatar_hash", "last_logoff", "last_logon", "last_seen_online", "clan_rank", "game_name", "gameid", "game_data_blob", "clan_data", "clan_tag", "rich_presence", "broadcast_id", "game_lobby_id", "watching_broadcast_accountid", "watching_broadcast_appid", "watching_broadcast_viewers", "watching_broadcast_title", "is_community_banned", "player_name_pending_review", "avatar_pending_review", "on_steam_deck")
        class ClanData(_message.Message):
            __slots__ = ("ogg_app_id", "chat_group_id")
            OGG_APP_ID_FIELD_NUMBER: _ClassVar[int]
            CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
            ogg_app_id: int
            chat_group_id: int
            def __init__(self, ogg_app_id: _Optional[int] = ..., chat_group_id: _Optional[int] = ...) -> None: ...
        class KV(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        FRIENDID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_STATE_FIELD_NUMBER: _ClassVar[int]
        GAME_PLAYED_APP_ID_FIELD_NUMBER: _ClassVar[int]
        GAME_SERVER_IP_FIELD_NUMBER: _ClassVar[int]
        GAME_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
        PERSONA_STATE_FLAGS_FIELD_NUMBER: _ClassVar[int]
        ONLINE_SESSION_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        PERSONA_SET_BY_USER_FIELD_NUMBER: _ClassVar[int]
        PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_PORT_FIELD_NUMBER: _ClassVar[int]
        STEAMID_SOURCE_FIELD_NUMBER: _ClassVar[int]
        AVATAR_HASH_FIELD_NUMBER: _ClassVar[int]
        LAST_LOGOFF_FIELD_NUMBER: _ClassVar[int]
        LAST_LOGON_FIELD_NUMBER: _ClassVar[int]
        LAST_SEEN_ONLINE_FIELD_NUMBER: _ClassVar[int]
        CLAN_RANK_FIELD_NUMBER: _ClassVar[int]
        GAME_NAME_FIELD_NUMBER: _ClassVar[int]
        GAMEID_FIELD_NUMBER: _ClassVar[int]
        GAME_DATA_BLOB_FIELD_NUMBER: _ClassVar[int]
        CLAN_DATA_FIELD_NUMBER: _ClassVar[int]
        CLAN_TAG_FIELD_NUMBER: _ClassVar[int]
        RICH_PRESENCE_FIELD_NUMBER: _ClassVar[int]
        BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
        GAME_LOBBY_ID_FIELD_NUMBER: _ClassVar[int]
        WATCHING_BROADCAST_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        WATCHING_BROADCAST_APPID_FIELD_NUMBER: _ClassVar[int]
        WATCHING_BROADCAST_VIEWERS_FIELD_NUMBER: _ClassVar[int]
        WATCHING_BROADCAST_TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_COMMUNITY_BANNED_FIELD_NUMBER: _ClassVar[int]
        PLAYER_NAME_PENDING_REVIEW_FIELD_NUMBER: _ClassVar[int]
        AVATAR_PENDING_REVIEW_FIELD_NUMBER: _ClassVar[int]
        ON_STEAM_DECK_FIELD_NUMBER: _ClassVar[int]
        friendid: int
        persona_state: int
        game_played_app_id: int
        game_server_ip: int
        game_server_port: int
        persona_state_flags: int
        online_session_instances: int
        persona_set_by_user: bool
        player_name: str
        query_port: int
        steamid_source: int
        avatar_hash: bytes
        last_logoff: int
        last_logon: int
        last_seen_online: int
        clan_rank: int
        game_name: str
        gameid: int
        game_data_blob: bytes
        clan_data: CMsgClientPersonaState.Friend.ClanData
        clan_tag: str
        rich_presence: _containers.RepeatedCompositeFieldContainer[CMsgClientPersonaState.Friend.KV]
        broadcast_id: int
        game_lobby_id: int
        watching_broadcast_accountid: int
        watching_broadcast_appid: int
        watching_broadcast_viewers: int
        watching_broadcast_title: str
        is_community_banned: bool
        player_name_pending_review: bool
        avatar_pending_review: bool
        on_steam_deck: bool
        def __init__(self, friendid: _Optional[int] = ..., persona_state: _Optional[int] = ..., game_played_app_id: _Optional[int] = ..., game_server_ip: _Optional[int] = ..., game_server_port: _Optional[int] = ..., persona_state_flags: _Optional[int] = ..., online_session_instances: _Optional[int] = ..., persona_set_by_user: bool = ..., player_name: _Optional[str] = ..., query_port: _Optional[int] = ..., steamid_source: _Optional[int] = ..., avatar_hash: _Optional[bytes] = ..., last_logoff: _Optional[int] = ..., last_logon: _Optional[int] = ..., last_seen_online: _Optional[int] = ..., clan_rank: _Optional[int] = ..., game_name: _Optional[str] = ..., gameid: _Optional[int] = ..., game_data_blob: _Optional[bytes] = ..., clan_data: _Optional[_Union[CMsgClientPersonaState.Friend.ClanData, _Mapping]] = ..., clan_tag: _Optional[str] = ..., rich_presence: _Optional[_Iterable[_Union[CMsgClientPersonaState.Friend.KV, _Mapping]]] = ..., broadcast_id: _Optional[int] = ..., game_lobby_id: _Optional[int] = ..., watching_broadcast_accountid: _Optional[int] = ..., watching_broadcast_appid: _Optional[int] = ..., watching_broadcast_viewers: _Optional[int] = ..., watching_broadcast_title: _Optional[str] = ..., is_community_banned: bool = ..., player_name_pending_review: bool = ..., avatar_pending_review: bool = ..., on_steam_deck: bool = ...) -> None: ...
    STATUS_FLAGS_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    status_flags: int
    friends: _containers.RepeatedCompositeFieldContainer[CMsgClientPersonaState.Friend]
    def __init__(self, status_flags: _Optional[int] = ..., friends: _Optional[_Iterable[_Union[CMsgClientPersonaState.Friend, _Mapping]]] = ...) -> None: ...

class CMsgClientFriendProfileInfo(_message.Message):
    __slots__ = ("steamid_friend",)
    STEAMID_FRIEND_FIELD_NUMBER: _ClassVar[int]
    steamid_friend: int
    def __init__(self, steamid_friend: _Optional[int] = ...) -> None: ...

class CMsgClientFriendProfileInfoResponse(_message.Message):
    __slots__ = ("eresult", "steamid_friend", "time_created", "real_name", "city_name", "state_name", "country_name", "headline", "summary")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FRIEND_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    REAL_NAME_FIELD_NUMBER: _ClassVar[int]
    CITY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    steamid_friend: int
    time_created: int
    real_name: str
    city_name: str
    state_name: str
    country_name: str
    headline: str
    summary: str
    def __init__(self, eresult: _Optional[int] = ..., steamid_friend: _Optional[int] = ..., time_created: _Optional[int] = ..., real_name: _Optional[str] = ..., city_name: _Optional[str] = ..., state_name: _Optional[str] = ..., country_name: _Optional[str] = ..., headline: _Optional[str] = ..., summary: _Optional[str] = ...) -> None: ...

class CMsgClientCreateFriendsGroup(_message.Message):
    __slots__ = ("steamid", "groupname", "steamid_friends")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FRIENDS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    groupname: str
    steamid_friends: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid: _Optional[int] = ..., groupname: _Optional[str] = ..., steamid_friends: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientCreateFriendsGroupResponse(_message.Message):
    __slots__ = ("eresult", "groupid")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    groupid: int
    def __init__(self, eresult: _Optional[int] = ..., groupid: _Optional[int] = ...) -> None: ...

class CMsgClientDeleteFriendsGroup(_message.Message):
    __slots__ = ("steamid", "groupid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    groupid: int
    def __init__(self, steamid: _Optional[int] = ..., groupid: _Optional[int] = ...) -> None: ...

class CMsgClientDeleteFriendsGroupResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientManageFriendsGroup(_message.Message):
    __slots__ = ("groupid", "groupname", "steamid_friends_added", "steamid_friends_removed")
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    GROUPNAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FRIENDS_ADDED_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FRIENDS_REMOVED_FIELD_NUMBER: _ClassVar[int]
    groupid: int
    groupname: str
    steamid_friends_added: _containers.RepeatedScalarFieldContainer[int]
    steamid_friends_removed: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, groupid: _Optional[int] = ..., groupname: _Optional[str] = ..., steamid_friends_added: _Optional[_Iterable[int]] = ..., steamid_friends_removed: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientManageFriendsGroupResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientAddFriendToGroup(_message.Message):
    __slots__ = ("groupid", "steamiduser")
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMIDUSER_FIELD_NUMBER: _ClassVar[int]
    groupid: int
    steamiduser: int
    def __init__(self, groupid: _Optional[int] = ..., steamiduser: _Optional[int] = ...) -> None: ...

class CMsgClientAddFriendToGroupResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientRemoveFriendFromGroup(_message.Message):
    __slots__ = ("groupid", "steamiduser")
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMIDUSER_FIELD_NUMBER: _ClassVar[int]
    groupid: int
    steamiduser: int
    def __init__(self, groupid: _Optional[int] = ..., steamiduser: _Optional[int] = ...) -> None: ...

class CMsgClientRemoveFriendFromGroupResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientGetEmoticonList(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgClientEmoticonList(_message.Message):
    __slots__ = ("emoticons", "stickers", "effects")
    class Emoticon(_message.Message):
        __slots__ = ("name", "count", "time_last_used", "use_count", "time_received", "appid")
        NAME_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        TIME_LAST_USED_FIELD_NUMBER: _ClassVar[int]
        USE_COUNT_FIELD_NUMBER: _ClassVar[int]
        TIME_RECEIVED_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        name: str
        count: int
        time_last_used: int
        use_count: int
        time_received: int
        appid: int
        def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., time_last_used: _Optional[int] = ..., use_count: _Optional[int] = ..., time_received: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...
    class Sticker(_message.Message):
        __slots__ = ("name", "count", "time_received", "appid", "time_last_used", "use_count")
        NAME_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        TIME_RECEIVED_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        TIME_LAST_USED_FIELD_NUMBER: _ClassVar[int]
        USE_COUNT_FIELD_NUMBER: _ClassVar[int]
        name: str
        count: int
        time_received: int
        appid: int
        time_last_used: int
        use_count: int
        def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., time_received: _Optional[int] = ..., appid: _Optional[int] = ..., time_last_used: _Optional[int] = ..., use_count: _Optional[int] = ...) -> None: ...
    class Effect(_message.Message):
        __slots__ = ("name", "count", "time_received", "infinite_use", "appid")
        NAME_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        TIME_RECEIVED_FIELD_NUMBER: _ClassVar[int]
        INFINITE_USE_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        name: str
        count: int
        time_received: int
        infinite_use: bool
        appid: int
        def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ..., time_received: _Optional[int] = ..., infinite_use: bool = ..., appid: _Optional[int] = ...) -> None: ...
    EMOTICONS_FIELD_NUMBER: _ClassVar[int]
    STICKERS_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    emoticons: _containers.RepeatedCompositeFieldContainer[CMsgClientEmoticonList.Emoticon]
    stickers: _containers.RepeatedCompositeFieldContainer[CMsgClientEmoticonList.Sticker]
    effects: _containers.RepeatedCompositeFieldContainer[CMsgClientEmoticonList.Effect]
    def __init__(self, emoticons: _Optional[_Iterable[_Union[CMsgClientEmoticonList.Emoticon, _Mapping]]] = ..., stickers: _Optional[_Iterable[_Union[CMsgClientEmoticonList.Sticker, _Mapping]]] = ..., effects: _Optional[_Iterable[_Union[CMsgClientEmoticonList.Effect, _Mapping]]] = ...) -> None: ...
