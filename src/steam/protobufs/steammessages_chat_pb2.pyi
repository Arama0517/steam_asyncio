import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import steammessages_clientserver_friends_pb2 as _steammessages_clientserver_friends_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EChatRoomJoinState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EChatRoomJoinState_Default: _ClassVar[EChatRoomJoinState]
    k_EChatRoomJoinState_None: _ClassVar[EChatRoomJoinState]
    k_EChatRoomJoinState_Joined: _ClassVar[EChatRoomJoinState]
    k_EChatRoomJoinState_TestInvalid: _ClassVar[EChatRoomJoinState]

class EChatRoomGroupRank(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EChatRoomGroupRank_Default: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_Viewer: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_Guest: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_Member: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_Moderator: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_Officer: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_Owner: _ClassVar[EChatRoomGroupRank]
    k_EChatRoomGroupRank_TestInvalid: _ClassVar[EChatRoomGroupRank]

class EChatRoomNotificationLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EChatroomNotificationLevel_Invalid: _ClassVar[EChatRoomNotificationLevel]
    k_EChatroomNotificationLevel_None: _ClassVar[EChatRoomNotificationLevel]
    k_EChatroomNotificationLevel_MentionMe: _ClassVar[EChatRoomNotificationLevel]
    k_EChatroomNotificationLevel_MentionAll: _ClassVar[EChatRoomNotificationLevel]
    k_EChatroomNotificationLevel_AllMessages: _ClassVar[EChatRoomNotificationLevel]

class EChatRoomServerMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EChatRoomServerMsg_Invalid: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_RenameChatRoom: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_Joined: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_Parted: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_Kicked: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_Invited: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_InviteDismissed: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_ChatRoomTaglineChanged: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_ChatRoomAvatarChanged: _ClassVar[EChatRoomServerMessage]
    k_EChatRoomServerMsg_AppCustom: _ClassVar[EChatRoomServerMessage]

class EChatRoomMessageReactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EChatRoomMessageReactionType_Invalid: _ClassVar[EChatRoomMessageReactionType]
    k_EChatRoomMessageReactionType_Emoticon: _ClassVar[EChatRoomMessageReactionType]
    k_EChatRoomMessageReactionType_Sticker: _ClassVar[EChatRoomMessageReactionType]

class EChatRoomMemberStateChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EChatRoomMemberStateChange_Invalid: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_Joined: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_Parted: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_Kicked: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_Invited: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_RankChanged: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_InviteDismissed: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_Muted: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_Banned: _ClassVar[EChatRoomMemberStateChange]
    k_EChatRoomMemberStateChange_RolesChanged: _ClassVar[EChatRoomMemberStateChange]
k_EChatRoomJoinState_Default: EChatRoomJoinState
k_EChatRoomJoinState_None: EChatRoomJoinState
k_EChatRoomJoinState_Joined: EChatRoomJoinState
k_EChatRoomJoinState_TestInvalid: EChatRoomJoinState
k_EChatRoomGroupRank_Default: EChatRoomGroupRank
k_EChatRoomGroupRank_Viewer: EChatRoomGroupRank
k_EChatRoomGroupRank_Guest: EChatRoomGroupRank
k_EChatRoomGroupRank_Member: EChatRoomGroupRank
k_EChatRoomGroupRank_Moderator: EChatRoomGroupRank
k_EChatRoomGroupRank_Officer: EChatRoomGroupRank
k_EChatRoomGroupRank_Owner: EChatRoomGroupRank
k_EChatRoomGroupRank_TestInvalid: EChatRoomGroupRank
k_EChatroomNotificationLevel_Invalid: EChatRoomNotificationLevel
k_EChatroomNotificationLevel_None: EChatRoomNotificationLevel
k_EChatroomNotificationLevel_MentionMe: EChatRoomNotificationLevel
k_EChatroomNotificationLevel_MentionAll: EChatRoomNotificationLevel
k_EChatroomNotificationLevel_AllMessages: EChatRoomNotificationLevel
k_EChatRoomServerMsg_Invalid: EChatRoomServerMessage
k_EChatRoomServerMsg_RenameChatRoom: EChatRoomServerMessage
k_EChatRoomServerMsg_Joined: EChatRoomServerMessage
k_EChatRoomServerMsg_Parted: EChatRoomServerMessage
k_EChatRoomServerMsg_Kicked: EChatRoomServerMessage
k_EChatRoomServerMsg_Invited: EChatRoomServerMessage
k_EChatRoomServerMsg_InviteDismissed: EChatRoomServerMessage
k_EChatRoomServerMsg_ChatRoomTaglineChanged: EChatRoomServerMessage
k_EChatRoomServerMsg_ChatRoomAvatarChanged: EChatRoomServerMessage
k_EChatRoomServerMsg_AppCustom: EChatRoomServerMessage
k_EChatRoomMessageReactionType_Invalid: EChatRoomMessageReactionType
k_EChatRoomMessageReactionType_Emoticon: EChatRoomMessageReactionType
k_EChatRoomMessageReactionType_Sticker: EChatRoomMessageReactionType
k_EChatRoomMemberStateChange_Invalid: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_Joined: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_Parted: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_Kicked: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_Invited: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_RankChanged: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_InviteDismissed: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_Muted: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_Banned: EChatRoomMemberStateChange
k_EChatRoomMemberStateChange_RolesChanged: EChatRoomMemberStateChange

class CChat_RequestFriendPersonaStates_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChat_RequestFriendPersonaStates_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_CreateChatRoomGroup_Request(_message.Message):
    __slots__ = ("steamid_partner", "steamid_invited", "name", "steamid_invitees", "watching_broadcast_accountid", "watching_broadcast_channel_id")
    STEAMID_PARTNER_FIELD_NUMBER: _ClassVar[int]
    STEAMID_INVITED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_INVITEES_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    steamid_partner: int
    steamid_invited: int
    name: str
    steamid_invitees: _containers.RepeatedScalarFieldContainer[int]
    watching_broadcast_accountid: int
    watching_broadcast_channel_id: int
    def __init__(self, steamid_partner: _Optional[int] = ..., steamid_invited: _Optional[int] = ..., name: _Optional[str] = ..., steamid_invitees: _Optional[_Iterable[int]] = ..., watching_broadcast_accountid: _Optional[int] = ..., watching_broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CChatRole(_message.Message):
    __slots__ = ("role_id", "name", "ordinal")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    name: str
    ordinal: int
    def __init__(self, role_id: _Optional[int] = ..., name: _Optional[str] = ..., ordinal: _Optional[int] = ...) -> None: ...

class CChatRoleActions(_message.Message):
    __slots__ = ("role_id", "can_create_rename_delete_channel", "can_kick", "can_ban", "can_invite", "can_change_tagline_avatar_name", "can_chat", "can_view_history", "can_change_group_roles", "can_change_user_roles", "can_mention_all", "can_set_watching_broadcast")
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_RENAME_DELETE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CAN_KICK_FIELD_NUMBER: _ClassVar[int]
    CAN_BAN_FIELD_NUMBER: _ClassVar[int]
    CAN_INVITE_FIELD_NUMBER: _ClassVar[int]
    CAN_CHANGE_TAGLINE_AVATAR_NAME_FIELD_NUMBER: _ClassVar[int]
    CAN_CHAT_FIELD_NUMBER: _ClassVar[int]
    CAN_VIEW_HISTORY_FIELD_NUMBER: _ClassVar[int]
    CAN_CHANGE_GROUP_ROLES_FIELD_NUMBER: _ClassVar[int]
    CAN_CHANGE_USER_ROLES_FIELD_NUMBER: _ClassVar[int]
    CAN_MENTION_ALL_FIELD_NUMBER: _ClassVar[int]
    CAN_SET_WATCHING_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    role_id: int
    can_create_rename_delete_channel: bool
    can_kick: bool
    can_ban: bool
    can_invite: bool
    can_change_tagline_avatar_name: bool
    can_chat: bool
    can_view_history: bool
    can_change_group_roles: bool
    can_change_user_roles: bool
    can_mention_all: bool
    can_set_watching_broadcast: bool
    def __init__(self, role_id: _Optional[int] = ..., can_create_rename_delete_channel: bool = ..., can_kick: bool = ..., can_ban: bool = ..., can_invite: bool = ..., can_change_tagline_avatar_name: bool = ..., can_chat: bool = ..., can_view_history: bool = ..., can_change_group_roles: bool = ..., can_change_user_roles: bool = ..., can_mention_all: bool = ..., can_set_watching_broadcast: bool = ...) -> None: ...

class CChatPartyBeacon(_message.Message):
    __slots__ = ("app_id", "steamid_owner", "beacon_id", "game_metadata")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_OWNER_FIELD_NUMBER: _ClassVar[int]
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_METADATA_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steamid_owner: int
    beacon_id: int
    game_metadata: str
    def __init__(self, app_id: _Optional[int] = ..., steamid_owner: _Optional[int] = ..., beacon_id: _Optional[int] = ..., game_metadata: _Optional[str] = ...) -> None: ...

class CChatRoomGroupHeaderState(_message.Message):
    __slots__ = ("chat_group_id", "chat_name", "clanid", "accountid_owner", "appid", "tagline", "avatar_sha", "default_role_id", "roles", "role_actions", "watching_broadcast_accountid", "party_beacons", "watching_broadcast_channel_id", "active_minigame_id", "avatar_ugc_url", "disabled")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_NAME_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_OWNER_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    TAGLINE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    ROLE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    PARTY_BEACONS_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MINIGAME_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_UGC_URL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_name: str
    clanid: int
    accountid_owner: int
    appid: int
    tagline: str
    avatar_sha: bytes
    default_role_id: int
    roles: _containers.RepeatedCompositeFieldContainer[CChatRole]
    role_actions: _containers.RepeatedCompositeFieldContainer[CChatRoleActions]
    watching_broadcast_accountid: int
    party_beacons: _containers.RepeatedCompositeFieldContainer[CChatPartyBeacon]
    watching_broadcast_channel_id: int
    active_minigame_id: int
    avatar_ugc_url: str
    disabled: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_name: _Optional[str] = ..., clanid: _Optional[int] = ..., accountid_owner: _Optional[int] = ..., appid: _Optional[int] = ..., tagline: _Optional[str] = ..., avatar_sha: _Optional[bytes] = ..., default_role_id: _Optional[int] = ..., roles: _Optional[_Iterable[_Union[CChatRole, _Mapping]]] = ..., role_actions: _Optional[_Iterable[_Union[CChatRoleActions, _Mapping]]] = ..., watching_broadcast_accountid: _Optional[int] = ..., party_beacons: _Optional[_Iterable[_Union[CChatPartyBeacon, _Mapping]]] = ..., watching_broadcast_channel_id: _Optional[int] = ..., active_minigame_id: _Optional[int] = ..., avatar_ugc_url: _Optional[str] = ..., disabled: bool = ...) -> None: ...

class CChatRoomMember(_message.Message):
    __slots__ = ("accountid", "state", "rank", "time_kick_expire", "role_ids")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    TIME_KICK_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    state: EChatRoomJoinState
    rank: EChatRoomGroupRank
    time_kick_expire: int
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, accountid: _Optional[int] = ..., state: _Optional[_Union[EChatRoomJoinState, str]] = ..., rank: _Optional[_Union[EChatRoomGroupRank, str]] = ..., time_kick_expire: _Optional[int] = ..., role_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoomState(_message.Message):
    __slots__ = ("chat_id", "chat_name", "voice_allowed", "members_in_voice", "time_last_message", "sort_order", "last_message", "accountid_last_message")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_NAME_FIELD_NUMBER: _ClassVar[int]
    VOICE_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_IN_VOICE_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_LAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    chat_name: str
    voice_allowed: bool
    members_in_voice: _containers.RepeatedScalarFieldContainer[int]
    time_last_message: int
    sort_order: int
    last_message: str
    accountid_last_message: int
    def __init__(self, chat_id: _Optional[int] = ..., chat_name: _Optional[str] = ..., voice_allowed: bool = ..., members_in_voice: _Optional[_Iterable[int]] = ..., time_last_message: _Optional[int] = ..., sort_order: _Optional[int] = ..., last_message: _Optional[str] = ..., accountid_last_message: _Optional[int] = ...) -> None: ...

class CChatRoomGroupState(_message.Message):
    __slots__ = ("header_state", "members", "default_chat_id", "chat_rooms", "kicked")
    HEADER_STATE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOMS_FIELD_NUMBER: _ClassVar[int]
    KICKED_FIELD_NUMBER: _ClassVar[int]
    header_state: CChatRoomGroupHeaderState
    members: _containers.RepeatedCompositeFieldContainer[CChatRoomMember]
    default_chat_id: int
    chat_rooms: _containers.RepeatedCompositeFieldContainer[CChatRoomState]
    kicked: _containers.RepeatedCompositeFieldContainer[CChatRoomMember]
    def __init__(self, header_state: _Optional[_Union[CChatRoomGroupHeaderState, _Mapping]] = ..., members: _Optional[_Iterable[_Union[CChatRoomMember, _Mapping]]] = ..., default_chat_id: _Optional[int] = ..., chat_rooms: _Optional[_Iterable[_Union[CChatRoomState, _Mapping]]] = ..., kicked: _Optional[_Iterable[_Union[CChatRoomMember, _Mapping]]] = ...) -> None: ...

class CUserChatRoomState(_message.Message):
    __slots__ = ("chat_id", "time_joined", "time_last_ack", "desktop_notification_level", "mobile_notification_level", "time_last_mention", "unread_indicator_muted", "time_first_unread")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_JOINED_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_ACK_FIELD_NUMBER: _ClassVar[int]
    DESKTOP_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_MENTION_FIELD_NUMBER: _ClassVar[int]
    UNREAD_INDICATOR_MUTED_FIELD_NUMBER: _ClassVar[int]
    TIME_FIRST_UNREAD_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    time_joined: int
    time_last_ack: int
    desktop_notification_level: EChatRoomNotificationLevel
    mobile_notification_level: EChatRoomNotificationLevel
    time_last_mention: int
    unread_indicator_muted: bool
    time_first_unread: int
    def __init__(self, chat_id: _Optional[int] = ..., time_joined: _Optional[int] = ..., time_last_ack: _Optional[int] = ..., desktop_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., mobile_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., time_last_mention: _Optional[int] = ..., unread_indicator_muted: bool = ..., time_first_unread: _Optional[int] = ...) -> None: ...

class CUserChatRoomGroupState(_message.Message):
    __slots__ = ("chat_group_id", "time_joined", "user_chat_room_state", "desktop_notification_level", "mobile_notification_level", "time_last_group_ack", "unread_indicator_muted")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_JOINED_FIELD_NUMBER: _ClassVar[int]
    USER_CHAT_ROOM_STATE_FIELD_NUMBER: _ClassVar[int]
    DESKTOP_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MOBILE_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_GROUP_ACK_FIELD_NUMBER: _ClassVar[int]
    UNREAD_INDICATOR_MUTED_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    time_joined: int
    user_chat_room_state: _containers.RepeatedCompositeFieldContainer[CUserChatRoomState]
    desktop_notification_level: EChatRoomNotificationLevel
    mobile_notification_level: EChatRoomNotificationLevel
    time_last_group_ack: int
    unread_indicator_muted: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., time_joined: _Optional[int] = ..., user_chat_room_state: _Optional[_Iterable[_Union[CUserChatRoomState, _Mapping]]] = ..., desktop_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., mobile_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., time_last_group_ack: _Optional[int] = ..., unread_indicator_muted: bool = ...) -> None: ...

class CChatRoom_CreateChatRoomGroup_Response(_message.Message):
    __slots__ = ("chat_group_id", "state", "user_chat_state")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_CHAT_STATE_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    state: CChatRoomGroupState
    user_chat_state: CUserChatRoomGroupState
    def __init__(self, chat_group_id: _Optional[int] = ..., state: _Optional[_Union[CChatRoomGroupState, _Mapping]] = ..., user_chat_state: _Optional[_Union[CUserChatRoomGroupState, _Mapping]] = ...) -> None: ...

class CChatRoom_SaveChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id", "name")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    name: str
    def __init__(self, chat_group_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CChatRoom_SaveChatRoomGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_RenameChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id", "name")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    name: str
    def __init__(self, chat_group_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CChatRoom_RenameChatRoomGroup_Response(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CChatRoom_SetChatRoomGroupTagline_Request(_message.Message):
    __slots__ = ("chat_group_id", "tagline")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    TAGLINE_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    tagline: str
    def __init__(self, chat_group_id: _Optional[int] = ..., tagline: _Optional[str] = ...) -> None: ...

class CChatRoom_SetChatRoomGroupTagline_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_SetChatRoomGroupAvatar_Request(_message.Message):
    __slots__ = ("chat_group_id", "avatar_sha")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_SHA_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    avatar_sha: bytes
    def __init__(self, chat_group_id: _Optional[int] = ..., avatar_sha: _Optional[bytes] = ...) -> None: ...

class CChatRoom_SetChatRoomGroupAvatar_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_SetChatRoomGroupWatchingBroadcast_Request(_message.Message):
    __slots__ = ("chat_group_id", "watching_broadcast_accountid", "watching_broadcast_channel_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    watching_broadcast_accountid: int
    watching_broadcast_channel_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., watching_broadcast_accountid: _Optional[int] = ..., watching_broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CChatRoom_SetChatRoomGroupWatchingBroadcast_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_JoinMiniGameForChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_JoinMiniGameForChatRoomGroup_Response(_message.Message):
    __slots__ = ("minigame_id",)
    MINIGAME_ID_FIELD_NUMBER: _ClassVar[int]
    minigame_id: int
    def __init__(self, minigame_id: _Optional[int] = ...) -> None: ...

class CChatRoom_EndMiniGameForChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "minigame_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MINIGAME_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    minigame_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., minigame_id: _Optional[int] = ...) -> None: ...

class CChatRoom_EndMiniGameForChatRoomGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_MuteUser_Request(_message.Message):
    __slots__ = ("chat_group_id", "steamid", "expiration")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    steamid: int
    expiration: int
    def __init__(self, chat_group_id: _Optional[int] = ..., steamid: _Optional[int] = ..., expiration: _Optional[int] = ...) -> None: ...

class CChatRoom_MuteUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_KickUser_Request(_message.Message):
    __slots__ = ("chat_group_id", "steamid", "expiration")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    steamid: int
    expiration: int
    def __init__(self, chat_group_id: _Optional[int] = ..., steamid: _Optional[int] = ..., expiration: _Optional[int] = ...) -> None: ...

class CChatRoom_KickUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_SetUserBanState_Request(_message.Message):
    __slots__ = ("chat_group_id", "steamid", "ban_state")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BAN_STATE_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    steamid: int
    ban_state: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., steamid: _Optional[int] = ..., ban_state: bool = ...) -> None: ...

class CChatRoom_SetUserBanState_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_RevokeInvite_Request(_message.Message):
    __slots__ = ("chat_group_id", "steamid")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    steamid: int
    def __init__(self, chat_group_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CChatRoom_RevokeInvite_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_CreateRole_Request(_message.Message):
    __slots__ = ("chat_group_id", "name")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    name: str
    def __init__(self, chat_group_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CChatRoom_CreateRole_Response(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: CChatRoleActions
    def __init__(self, actions: _Optional[_Union[CChatRoleActions, _Mapping]] = ...) -> None: ...

class CChatRoom_GetRoles_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoom_GetRoles_Response(_message.Message):
    __slots__ = ("roles",)
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[CChatRole]
    def __init__(self, roles: _Optional[_Iterable[_Union[CChatRole, _Mapping]]] = ...) -> None: ...

class CChatRoom_RenameRole_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id", "name")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    name: str
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CChatRoom_RenameRole_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_ReorderRole_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id", "ordinal")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    ordinal: int
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ..., ordinal: _Optional[int] = ...) -> None: ...

class CChatRoom_ReorderRole_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_DeleteRole_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ...) -> None: ...

class CChatRoom_DeleteRole_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_GetRoleActions_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ...) -> None: ...

class CChatRoom_GetRoleActions_Response(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[CChatRoleActions]
    def __init__(self, actions: _Optional[_Iterable[_Union[CChatRoleActions, _Mapping]]] = ...) -> None: ...

class CChatRoom_ReplaceRoleActions_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id", "actions")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    actions: CChatRoleActions
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ..., actions: _Optional[_Union[CChatRoleActions, _Mapping]] = ...) -> None: ...

class CChatRoom_ReplaceRoleActions_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_AddRoleToUser_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id", "steamid")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    steamid: int
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CChatRoom_AddRoleToUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_GetRolesForUser_Request(_message.Message):
    __slots__ = ("chat_group_id", "steamid")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    steamid: int
    def __init__(self, chat_group_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CChatRoom_GetRolesForUser_Response(_message.Message):
    __slots__ = ("role_ids",)
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, role_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoom_DeleteRoleFromUser_Request(_message.Message):
    __slots__ = ("chat_group_id", "role_id", "steamid")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    role_id: int
    steamid: int
    def __init__(self, chat_group_id: _Optional[int] = ..., role_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CChatRoom_DeleteRoleFromUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_JoinChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id", "invite_code", "chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    invite_code: str
    chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., invite_code: _Optional[str] = ..., chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_JoinChatRoomGroup_Response(_message.Message):
    __slots__ = ("state", "user_chat_state", "join_chat_id", "time_expire")
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_CHAT_STATE_FIELD_NUMBER: _ClassVar[int]
    JOIN_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    state: CChatRoomGroupState
    user_chat_state: CUserChatRoomGroupState
    join_chat_id: int
    time_expire: int
    def __init__(self, state: _Optional[_Union[CChatRoomGroupState, _Mapping]] = ..., user_chat_state: _Optional[_Union[CUserChatRoomGroupState, _Mapping]] = ..., join_chat_id: _Optional[int] = ..., time_expire: _Optional[int] = ...) -> None: ...

class CChatRoom_InviteFriendToChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id", "steamid", "chat_id", "skip_friendsui_check")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_FRIENDSUI_CHECK_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    steamid: int
    chat_id: int
    skip_friendsui_check: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., steamid: _Optional[int] = ..., chat_id: _Optional[int] = ..., skip_friendsui_check: bool = ...) -> None: ...

class CChatRoom_InviteFriendToChatRoomGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_LeaveChatRoomGroup_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoom_LeaveChatRoomGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_CreateChatRoom_Request(_message.Message):
    __slots__ = ("chat_group_id", "name", "allow_voice")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_VOICE_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    name: str
    allow_voice: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., name: _Optional[str] = ..., allow_voice: bool = ...) -> None: ...

class CChatRoom_CreateChatRoom_Response(_message.Message):
    __slots__ = ("chat_room",)
    CHAT_ROOM_FIELD_NUMBER: _ClassVar[int]
    chat_room: CChatRoomState
    def __init__(self, chat_room: _Optional[_Union[CChatRoomState, _Mapping]] = ...) -> None: ...

class CChatRoom_DeleteChatRoom_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_DeleteChatRoom_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_RenameChatRoom_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "name")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    name: str
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CChatRoom_RenameChatRoom_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_ReorderChatRoom_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "move_after_chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MOVE_AFTER_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    move_after_chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., move_after_chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_ReorderChatRoom_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_SendChatMessage_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "message", "echo_to_sender")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ECHO_TO_SENDER_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    message: str
    echo_to_sender: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., message: _Optional[str] = ..., echo_to_sender: bool = ...) -> None: ...

class CChatRoom_SendChatMessage_Response(_message.Message):
    __slots__ = ("modified_message", "server_timestamp", "ordinal", "message_without_bb_code")
    MODIFIED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_WITHOUT_BB_CODE_FIELD_NUMBER: _ClassVar[int]
    modified_message: str
    server_timestamp: int
    ordinal: int
    message_without_bb_code: str
    def __init__(self, modified_message: _Optional[str] = ..., server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., message_without_bb_code: _Optional[str] = ...) -> None: ...

class CChatRoom_JoinVoiceChat_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_JoinVoiceChat_Response(_message.Message):
    __slots__ = ("voice_chatid",)
    VOICE_CHATID_FIELD_NUMBER: _ClassVar[int]
    voice_chatid: int
    def __init__(self, voice_chatid: _Optional[int] = ...) -> None: ...

class CChatRoom_LeaveVoiceChat_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_LeaveVoiceChat_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_GetMessageHistory_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "last_time", "last_ordinal", "start_time", "start_ordinal", "max_count")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    START_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    MAX_COUNT_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    last_time: int
    last_ordinal: int
    start_time: int
    start_ordinal: int
    max_count: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., last_time: _Optional[int] = ..., last_ordinal: _Optional[int] = ..., start_time: _Optional[int] = ..., start_ordinal: _Optional[int] = ..., max_count: _Optional[int] = ...) -> None: ...

class ServerMessage(_message.Message):
    __slots__ = ("message", "string_param", "accountid_param")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STRING_PARAM_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_PARAM_FIELD_NUMBER: _ClassVar[int]
    message: EChatRoomServerMessage
    string_param: str
    accountid_param: int
    def __init__(self, message: _Optional[_Union[EChatRoomServerMessage, str]] = ..., string_param: _Optional[str] = ..., accountid_param: _Optional[int] = ...) -> None: ...

class CChatRoom_GetMessageHistory_Response(_message.Message):
    __slots__ = ("messages", "more_available")
    class ChatMessage(_message.Message):
        __slots__ = ("sender", "server_timestamp", "message", "ordinal", "server_message", "deleted", "reactions")
        class MessageReaction(_message.Message):
            __slots__ = ("reaction_type", "reaction", "num_reactors", "has_user_reacted")
            REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
            REACTION_FIELD_NUMBER: _ClassVar[int]
            NUM_REACTORS_FIELD_NUMBER: _ClassVar[int]
            HAS_USER_REACTED_FIELD_NUMBER: _ClassVar[int]
            reaction_type: EChatRoomMessageReactionType
            reaction: str
            num_reactors: int
            has_user_reacted: bool
            def __init__(self, reaction_type: _Optional[_Union[EChatRoomMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., num_reactors: _Optional[int] = ..., has_user_reacted: bool = ...) -> None: ...
        SENDER_FIELD_NUMBER: _ClassVar[int]
        SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ORDINAL_FIELD_NUMBER: _ClassVar[int]
        SERVER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        REACTIONS_FIELD_NUMBER: _ClassVar[int]
        sender: int
        server_timestamp: int
        message: str
        ordinal: int
        server_message: ServerMessage
        deleted: bool
        reactions: _containers.RepeatedCompositeFieldContainer[CChatRoom_GetMessageHistory_Response.ChatMessage.MessageReaction]
        def __init__(self, sender: _Optional[int] = ..., server_timestamp: _Optional[int] = ..., message: _Optional[str] = ..., ordinal: _Optional[int] = ..., server_message: _Optional[_Union[ServerMessage, _Mapping]] = ..., deleted: bool = ..., reactions: _Optional[_Iterable[_Union[CChatRoom_GetMessageHistory_Response.ChatMessage.MessageReaction, _Mapping]]] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MORE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CChatRoom_GetMessageHistory_Response.ChatMessage]
    more_available: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[CChatRoom_GetMessageHistory_Response.ChatMessage, _Mapping]]] = ..., more_available: bool = ...) -> None: ...

class CChatRoom_GetMyChatRoomGroups_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_GetChatRoomGroupSummary_Response(_message.Message):
    __slots__ = ("chat_group_id", "chat_group_name", "active_member_count", "active_voice_member_count", "default_chat_id", "chat_rooms", "clanid", "chat_group_tagline", "accountid_owner", "top_members", "chat_group_avatar_sha", "rank", "default_role_id", "role_ids", "role_actions", "watching_broadcast_accountid", "appid", "party_beacons", "watching_broadcast_channel_id", "active_minigame_id", "avatar_ugc_url", "disabled")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_VOICE_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOMS_FIELD_NUMBER: _ClassVar[int]
    CLANID_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_TAGLINE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_OWNER_FIELD_NUMBER: _ClassVar[int]
    TOP_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_AVATAR_SHA_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    ROLE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    PARTY_BEACONS_FIELD_NUMBER: _ClassVar[int]
    WATCHING_BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_MINIGAME_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_UGC_URL_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_group_name: str
    active_member_count: int
    active_voice_member_count: int
    default_chat_id: int
    chat_rooms: _containers.RepeatedCompositeFieldContainer[CChatRoomState]
    clanid: int
    chat_group_tagline: str
    accountid_owner: int
    top_members: _containers.RepeatedScalarFieldContainer[int]
    chat_group_avatar_sha: bytes
    rank: EChatRoomGroupRank
    default_role_id: int
    role_ids: _containers.RepeatedScalarFieldContainer[int]
    role_actions: _containers.RepeatedCompositeFieldContainer[CChatRoleActions]
    watching_broadcast_accountid: int
    appid: int
    party_beacons: _containers.RepeatedCompositeFieldContainer[CChatPartyBeacon]
    watching_broadcast_channel_id: int
    active_minigame_id: int
    avatar_ugc_url: str
    disabled: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_group_name: _Optional[str] = ..., active_member_count: _Optional[int] = ..., active_voice_member_count: _Optional[int] = ..., default_chat_id: _Optional[int] = ..., chat_rooms: _Optional[_Iterable[_Union[CChatRoomState, _Mapping]]] = ..., clanid: _Optional[int] = ..., chat_group_tagline: _Optional[str] = ..., accountid_owner: _Optional[int] = ..., top_members: _Optional[_Iterable[int]] = ..., chat_group_avatar_sha: _Optional[bytes] = ..., rank: _Optional[_Union[EChatRoomGroupRank, str]] = ..., default_role_id: _Optional[int] = ..., role_ids: _Optional[_Iterable[int]] = ..., role_actions: _Optional[_Iterable[_Union[CChatRoleActions, _Mapping]]] = ..., watching_broadcast_accountid: _Optional[int] = ..., appid: _Optional[int] = ..., party_beacons: _Optional[_Iterable[_Union[CChatPartyBeacon, _Mapping]]] = ..., watching_broadcast_channel_id: _Optional[int] = ..., active_minigame_id: _Optional[int] = ..., avatar_ugc_url: _Optional[str] = ..., disabled: bool = ...) -> None: ...

class CChatRoomSummaryPair(_message.Message):
    __slots__ = ("user_chat_group_state", "group_summary")
    USER_CHAT_GROUP_STATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    user_chat_group_state: CUserChatRoomGroupState
    group_summary: CChatRoom_GetChatRoomGroupSummary_Response
    def __init__(self, user_chat_group_state: _Optional[_Union[CUserChatRoomGroupState, _Mapping]] = ..., group_summary: _Optional[_Union[CChatRoom_GetChatRoomGroupSummary_Response, _Mapping]] = ...) -> None: ...

class CChatRoom_GetMyChatRoomGroups_Response(_message.Message):
    __slots__ = ("chat_room_groups",)
    CHAT_ROOM_GROUPS_FIELD_NUMBER: _ClassVar[int]
    chat_room_groups: _containers.RepeatedCompositeFieldContainer[CChatRoomSummaryPair]
    def __init__(self, chat_room_groups: _Optional[_Iterable[_Union[CChatRoomSummaryPair, _Mapping]]] = ...) -> None: ...

class CChatRoom_GetChatRoomGroupState_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoom_GetChatRoomGroupState_Response(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: CChatRoomGroupState
    def __init__(self, state: _Optional[_Union[CChatRoomGroupState, _Mapping]] = ...) -> None: ...

class CChatRoom_GetChatRoomGroupSummary_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoom_SetAppChatRoomGroupForceActive_Request(_message.Message):
    __slots__ = ("chat_group_id", "requesting_app_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_APP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    requesting_app_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., requesting_app_id: _Optional[int] = ...) -> None: ...

class CChatRoom_SetAppChatRoomGroupForceActive_Response(_message.Message):
    __slots__ = ("result", "accounts_in_channel")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_IN_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    result: int
    accounts_in_channel: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, result: _Optional[int] = ..., accounts_in_channel: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoom_SetAppChatRoomGroupStopForceActive_Notification(_message.Message):
    __slots__ = ("chat_group_id", "requesting_app_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_APP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    requesting_app_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., requesting_app_id: _Optional[int] = ...) -> None: ...

class CChatRoom_AckChatMessage_Notification(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "timestamp")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    timestamp: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CChatRoom_CreateInviteLink_Request(_message.Message):
    __slots__ = ("chat_group_id", "seconds_valid", "chat_id")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_VALID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    seconds_valid: int
    chat_id: int
    def __init__(self, chat_group_id: _Optional[int] = ..., seconds_valid: _Optional[int] = ..., chat_id: _Optional[int] = ...) -> None: ...

class CChatRoom_CreateInviteLink_Response(_message.Message):
    __slots__ = ("invite_code", "seconds_valid")
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    SECONDS_VALID_FIELD_NUMBER: _ClassVar[int]
    invite_code: str
    seconds_valid: int
    def __init__(self, invite_code: _Optional[str] = ..., seconds_valid: _Optional[int] = ...) -> None: ...

class CChatRoom_GetInviteLinkInfo_Request(_message.Message):
    __slots__ = ("invite_code",)
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    invite_code: str
    def __init__(self, invite_code: _Optional[str] = ...) -> None: ...

class CChatRoom_GetInviteLinkInfo_Response(_message.Message):
    __slots__ = ("steamid_sender", "time_expires", "chat_id", "group_summary", "user_chat_group_state", "time_kick_expire", "banned")
    STEAMID_SENDER_FIELD_NUMBER: _ClassVar[int]
    TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    USER_CHAT_GROUP_STATE_FIELD_NUMBER: _ClassVar[int]
    TIME_KICK_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    steamid_sender: int
    time_expires: int
    chat_id: int
    group_summary: CChatRoom_GetChatRoomGroupSummary_Response
    user_chat_group_state: CUserChatRoomGroupState
    time_kick_expire: int
    banned: bool
    def __init__(self, steamid_sender: _Optional[int] = ..., time_expires: _Optional[int] = ..., chat_id: _Optional[int] = ..., group_summary: _Optional[_Union[CChatRoom_GetChatRoomGroupSummary_Response, _Mapping]] = ..., user_chat_group_state: _Optional[_Union[CUserChatRoomGroupState, _Mapping]] = ..., time_kick_expire: _Optional[int] = ..., banned: bool = ...) -> None: ...

class CChatRoom_GetInviteInfo_Request(_message.Message):
    __slots__ = ("steamid_invitee", "chat_group_id", "chat_id", "invite_code")
    STEAMID_INVITEE_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    steamid_invitee: int
    chat_group_id: int
    chat_id: int
    invite_code: str
    def __init__(self, steamid_invitee: _Optional[int] = ..., chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., invite_code: _Optional[str] = ...) -> None: ...

class CChatRoom_GetInviteInfo_Response(_message.Message):
    __slots__ = ("group_summary", "time_kick_expire", "banned")
    GROUP_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TIME_KICK_EXPIRE_FIELD_NUMBER: _ClassVar[int]
    BANNED_FIELD_NUMBER: _ClassVar[int]
    group_summary: CChatRoom_GetChatRoomGroupSummary_Response
    time_kick_expire: int
    banned: bool
    def __init__(self, group_summary: _Optional[_Union[CChatRoom_GetChatRoomGroupSummary_Response, _Mapping]] = ..., time_kick_expire: _Optional[int] = ..., banned: bool = ...) -> None: ...

class CChatRoom_GetInviteLinksForGroup_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoom_GetInviteLinksForGroup_Response(_message.Message):
    __slots__ = ("invite_links",)
    class LinkInfo(_message.Message):
        __slots__ = ("invite_code", "steamid_creator", "time_expires", "chat_id")
        INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
        STEAMID_CREATOR_FIELD_NUMBER: _ClassVar[int]
        TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
        CHAT_ID_FIELD_NUMBER: _ClassVar[int]
        invite_code: str
        steamid_creator: int
        time_expires: int
        chat_id: int
        def __init__(self, invite_code: _Optional[str] = ..., steamid_creator: _Optional[int] = ..., time_expires: _Optional[int] = ..., chat_id: _Optional[int] = ...) -> None: ...
    INVITE_LINKS_FIELD_NUMBER: _ClassVar[int]
    invite_links: _containers.RepeatedCompositeFieldContainer[CChatRoom_GetInviteLinksForGroup_Response.LinkInfo]
    def __init__(self, invite_links: _Optional[_Iterable[_Union[CChatRoom_GetInviteLinksForGroup_Response.LinkInfo, _Mapping]]] = ...) -> None: ...

class CChatRoom_GetBanList_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoom_GetBanList_Response(_message.Message):
    __slots__ = ("bans",)
    class BanInfo(_message.Message):
        __slots__ = ("accountid", "accountid_actor", "time_banned", "ban_reason")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTID_ACTOR_FIELD_NUMBER: _ClassVar[int]
        TIME_BANNED_FIELD_NUMBER: _ClassVar[int]
        BAN_REASON_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        accountid_actor: int
        time_banned: int
        ban_reason: str
        def __init__(self, accountid: _Optional[int] = ..., accountid_actor: _Optional[int] = ..., time_banned: _Optional[int] = ..., ban_reason: _Optional[str] = ...) -> None: ...
    BANS_FIELD_NUMBER: _ClassVar[int]
    bans: _containers.RepeatedCompositeFieldContainer[CChatRoom_GetBanList_Response.BanInfo]
    def __init__(self, bans: _Optional[_Iterable[_Union[CChatRoom_GetBanList_Response.BanInfo, _Mapping]]] = ...) -> None: ...

class CChatRoom_GetInviteList_Request(_message.Message):
    __slots__ = ("chat_group_id",)
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    def __init__(self, chat_group_id: _Optional[int] = ...) -> None: ...

class CChatRoomGroupInvite(_message.Message):
    __slots__ = ("accountid", "accountid_actor", "time_invited")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_ACTOR_FIELD_NUMBER: _ClassVar[int]
    TIME_INVITED_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    accountid_actor: int
    time_invited: int
    def __init__(self, accountid: _Optional[int] = ..., accountid_actor: _Optional[int] = ..., time_invited: _Optional[int] = ...) -> None: ...

class CChatRoom_GetInviteList_Response(_message.Message):
    __slots__ = ("invites",)
    INVITES_FIELD_NUMBER: _ClassVar[int]
    invites: _containers.RepeatedCompositeFieldContainer[CChatRoomGroupInvite]
    def __init__(self, invites: _Optional[_Iterable[_Union[CChatRoomGroupInvite, _Mapping]]] = ...) -> None: ...

class CChatRoom_DeleteInviteLink_Request(_message.Message):
    __slots__ = ("chat_group_id", "invite_code")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    INVITE_CODE_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    invite_code: str
    def __init__(self, chat_group_id: _Optional[int] = ..., invite_code: _Optional[str] = ...) -> None: ...

class CChatRoom_DeleteInviteLink_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_SetSessionActiveChatRoomGroups_Request(_message.Message):
    __slots__ = ("chat_group_ids", "chat_groups_data_requested", "virtualize_members_threshold")
    CHAT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUPS_DATA_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZE_MEMBERS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    chat_group_ids: _containers.RepeatedScalarFieldContainer[int]
    chat_groups_data_requested: _containers.RepeatedScalarFieldContainer[int]
    virtualize_members_threshold: int
    def __init__(self, chat_group_ids: _Optional[_Iterable[int]] = ..., chat_groups_data_requested: _Optional[_Iterable[int]] = ..., virtualize_members_threshold: _Optional[int] = ...) -> None: ...

class CChatRoom_SetSessionActiveChatRoomGroups_Response(_message.Message):
    __slots__ = ("chat_states", "virtualize_members_chat_group_ids")
    CHAT_STATES_FIELD_NUMBER: _ClassVar[int]
    VIRTUALIZE_MEMBERS_CHAT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_states: _containers.RepeatedCompositeFieldContainer[CChatRoomGroupState]
    virtualize_members_chat_group_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_states: _Optional[_Iterable[_Union[CChatRoomGroupState, _Mapping]]] = ..., virtualize_members_chat_group_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoom_SetUserChatGroupPreferences_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_group_preferences", "chat_room_preferences")
    class ChatGroupPreferences(_message.Message):
        __slots__ = ("desktop_notification_level", "mobile_notification_level", "unread_indicator_muted")
        DESKTOP_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        MOBILE_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        UNREAD_INDICATOR_MUTED_FIELD_NUMBER: _ClassVar[int]
        desktop_notification_level: EChatRoomNotificationLevel
        mobile_notification_level: EChatRoomNotificationLevel
        unread_indicator_muted: bool
        def __init__(self, desktop_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., mobile_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., unread_indicator_muted: bool = ...) -> None: ...
    class ChatRoomPreferences(_message.Message):
        __slots__ = ("chat_id", "desktop_notification_level", "mobile_notification_level", "unread_indicator_muted")
        CHAT_ID_FIELD_NUMBER: _ClassVar[int]
        DESKTOP_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        MOBILE_NOTIFICATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
        UNREAD_INDICATOR_MUTED_FIELD_NUMBER: _ClassVar[int]
        chat_id: int
        desktop_notification_level: EChatRoomNotificationLevel
        mobile_notification_level: EChatRoomNotificationLevel
        unread_indicator_muted: bool
        def __init__(self, chat_id: _Optional[int] = ..., desktop_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., mobile_notification_level: _Optional[_Union[EChatRoomNotificationLevel, str]] = ..., unread_indicator_muted: bool = ...) -> None: ...
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOM_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_group_preferences: CChatRoom_SetUserChatGroupPreferences_Request.ChatGroupPreferences
    chat_room_preferences: _containers.RepeatedCompositeFieldContainer[CChatRoom_SetUserChatGroupPreferences_Request.ChatRoomPreferences]
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_group_preferences: _Optional[_Union[CChatRoom_SetUserChatGroupPreferences_Request.ChatGroupPreferences, _Mapping]] = ..., chat_room_preferences: _Optional[_Iterable[_Union[CChatRoom_SetUserChatGroupPreferences_Request.ChatRoomPreferences, _Mapping]]] = ...) -> None: ...

class CChatRoom_SetUserChatGroupPreferences_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_DeleteChatMessages_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "messages")
    class Message(_message.Message):
        __slots__ = ("server_timestamp", "ordinal")
        SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ORDINAL_FIELD_NUMBER: _ClassVar[int]
        server_timestamp: int
        ordinal: int
        def __init__(self, server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ...) -> None: ...
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    messages: _containers.RepeatedCompositeFieldContainer[CChatRoom_DeleteChatMessages_Request.Message]
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., messages: _Optional[_Iterable[_Union[CChatRoom_DeleteChatMessages_Request.Message, _Mapping]]] = ...) -> None: ...

class CChatRoom_DeleteChatMessages_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CChatRoom_UpdateMemberListView_Notification(_message.Message):
    __slots__ = ("chat_group_id", "view_id", "start", "end", "client_changenumber", "delete_view", "persona_subscribe_accountids", "persona_unsubscribe_accountids")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CHANGENUMBER_FIELD_NUMBER: _ClassVar[int]
    DELETE_VIEW_FIELD_NUMBER: _ClassVar[int]
    PERSONA_SUBSCRIBE_ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    PERSONA_UNSUBSCRIBE_ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    view_id: int
    start: int
    end: int
    client_changenumber: int
    delete_view: bool
    persona_subscribe_accountids: _containers.RepeatedScalarFieldContainer[int]
    persona_unsubscribe_accountids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_group_id: _Optional[int] = ..., view_id: _Optional[int] = ..., start: _Optional[int] = ..., end: _Optional[int] = ..., client_changenumber: _Optional[int] = ..., delete_view: bool = ..., persona_subscribe_accountids: _Optional[_Iterable[int]] = ..., persona_unsubscribe_accountids: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoom_SearchMembers_Request(_message.Message):
    __slots__ = ("chat_group_id", "search_id", "search_text", "max_results")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TEXT_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    search_id: int
    search_text: str
    max_results: int
    def __init__(self, chat_group_id: _Optional[int] = ..., search_id: _Optional[int] = ..., search_text: _Optional[str] = ..., max_results: _Optional[int] = ...) -> None: ...

class CChatRoom_SearchMembers_Response(_message.Message):
    __slots__ = ("matching_members", "status_flags")
    class MemberMatch(_message.Message):
        __slots__ = ("accountid", "persona")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        persona: _steammessages_clientserver_friends_pb2.CMsgClientPersonaState.Friend
        def __init__(self, accountid: _Optional[int] = ..., persona: _Optional[_Union[_steammessages_clientserver_friends_pb2.CMsgClientPersonaState.Friend, _Mapping]] = ...) -> None: ...
    MATCHING_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FLAGS_FIELD_NUMBER: _ClassVar[int]
    matching_members: _containers.RepeatedCompositeFieldContainer[CChatRoom_SearchMembers_Response.MemberMatch]
    status_flags: int
    def __init__(self, matching_members: _Optional[_Iterable[_Union[CChatRoom_SearchMembers_Response.MemberMatch, _Mapping]]] = ..., status_flags: _Optional[int] = ...) -> None: ...

class CChatRoom_UpdateMessageReaction_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "server_timestamp", "ordinal", "reaction_type", "reaction", "is_add")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    server_timestamp: int
    ordinal: int
    reaction_type: EChatRoomMessageReactionType
    reaction: str
    is_add: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., reaction_type: _Optional[_Union[EChatRoomMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., is_add: bool = ...) -> None: ...

class CChatRoom_UpdateMessageReaction_Response(_message.Message):
    __slots__ = ("num_reactors",)
    NUM_REACTORS_FIELD_NUMBER: _ClassVar[int]
    num_reactors: int
    def __init__(self, num_reactors: _Optional[int] = ...) -> None: ...

class CChatRoom_GetMessageReactionReactors_Request(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "server_timestamp", "ordinal", "reaction_type", "reaction", "limit")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    server_timestamp: int
    ordinal: int
    reaction_type: EChatRoomMessageReactionType
    reaction: str
    limit: int
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., reaction_type: _Optional[_Union[EChatRoomMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class CChatRoom_GetMessageReactionReactors_Response(_message.Message):
    __slots__ = ("reactors",)
    REACTORS_FIELD_NUMBER: _ClassVar[int]
    reactors: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, reactors: _Optional[_Iterable[int]] = ...) -> None: ...

class CClanChatRooms_GetClanChatRoomInfo_Request(_message.Message):
    __slots__ = ("steamid", "autocreate")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTOCREATE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    autocreate: bool
    def __init__(self, steamid: _Optional[int] = ..., autocreate: bool = ...) -> None: ...

class CClanChatRooms_GetClanChatRoomInfo_Response(_message.Message):
    __slots__ = ("chat_group_summary",)
    CHAT_GROUP_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    chat_group_summary: CChatRoom_GetChatRoomGroupSummary_Response
    def __init__(self, chat_group_summary: _Optional[_Union[CChatRoom_GetChatRoomGroupSummary_Response, _Mapping]] = ...) -> None: ...

class CClanChatRooms_SetClanChatRoomPrivate_Request(_message.Message):
    __slots__ = ("steamid", "chat_room_private")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOM_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    chat_room_private: bool
    def __init__(self, steamid: _Optional[int] = ..., chat_room_private: bool = ...) -> None: ...

class CClanChatRooms_SetClanChatRoomPrivate_Response(_message.Message):
    __slots__ = ("chat_room_private",)
    CHAT_ROOM_PRIVATE_FIELD_NUMBER: _ClassVar[int]
    chat_room_private: bool
    def __init__(self, chat_room_private: bool = ...) -> None: ...

class CChatMentions(_message.Message):
    __slots__ = ("mention_all", "mention_here", "mention_accountids")
    MENTION_ALL_FIELD_NUMBER: _ClassVar[int]
    MENTION_HERE_FIELD_NUMBER: _ClassVar[int]
    MENTION_ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    mention_all: bool
    mention_here: bool
    mention_accountids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mention_all: bool = ..., mention_here: bool = ..., mention_accountids: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoom_IncomingChatMessage_Notification(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "steamid_sender", "message", "timestamp", "mentions", "ordinal", "server_message", "message_no_bbcode", "chat_name", "notification_key")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_SENDER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    SERVER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_NO_BBCODE_FIELD_NUMBER: _ClassVar[int]
    CHAT_NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_KEY_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    steamid_sender: int
    message: str
    timestamp: int
    mentions: CChatMentions
    ordinal: int
    server_message: ServerMessage
    message_no_bbcode: str
    chat_name: str
    notification_key: str
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., steamid_sender: _Optional[int] = ..., message: _Optional[str] = ..., timestamp: _Optional[int] = ..., mentions: _Optional[_Union[CChatMentions, _Mapping]] = ..., ordinal: _Optional[int] = ..., server_message: _Optional[_Union[ServerMessage, _Mapping]] = ..., message_no_bbcode: _Optional[str] = ..., chat_name: _Optional[str] = ..., notification_key: _Optional[str] = ...) -> None: ...

class CChatRoom_ChatMessageModified_Notification(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "messages")
    class ChatMessage(_message.Message):
        __slots__ = ("server_timestamp", "ordinal", "deleted")
        SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ORDINAL_FIELD_NUMBER: _ClassVar[int]
        DELETED_FIELD_NUMBER: _ClassVar[int]
        server_timestamp: int
        ordinal: int
        deleted: bool
        def __init__(self, server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., deleted: bool = ...) -> None: ...
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    messages: _containers.RepeatedCompositeFieldContainer[CChatRoom_ChatMessageModified_Notification.ChatMessage]
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., messages: _Optional[_Iterable[_Union[CChatRoom_ChatMessageModified_Notification.ChatMessage, _Mapping]]] = ...) -> None: ...

class CChatRoom_MemberStateChange_Notification(_message.Message):
    __slots__ = ("chat_group_id", "member", "change")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    member: CChatRoomMember
    change: EChatRoomMemberStateChange
    def __init__(self, chat_group_id: _Optional[int] = ..., member: _Optional[_Union[CChatRoomMember, _Mapping]] = ..., change: _Optional[_Union[EChatRoomMemberStateChange, str]] = ...) -> None: ...

class CChatRoom_ChatRoomHeaderState_Notification(_message.Message):
    __slots__ = ("header_state",)
    HEADER_STATE_FIELD_NUMBER: _ClassVar[int]
    header_state: CChatRoomGroupHeaderState
    def __init__(self, header_state: _Optional[_Union[CChatRoomGroupHeaderState, _Mapping]] = ...) -> None: ...

class CChatRoom_ChatRoomGroupRoomsChange_Notification(_message.Message):
    __slots__ = ("chat_group_id", "default_chat_id", "chat_rooms")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ROOMS_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    default_chat_id: int
    chat_rooms: _containers.RepeatedCompositeFieldContainer[CChatRoomState]
    def __init__(self, chat_group_id: _Optional[int] = ..., default_chat_id: _Optional[int] = ..., chat_rooms: _Optional[_Iterable[_Union[CChatRoomState, _Mapping]]] = ...) -> None: ...

class CChatRoom_NotifyShouldRejoinChatRoomVoiceChat_Notification(_message.Message):
    __slots__ = ("chat_id", "chat_group_id")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    chat_group_id: int
    def __init__(self, chat_id: _Optional[int] = ..., chat_group_id: _Optional[int] = ...) -> None: ...

class ChatRoomClient_NotifyChatGroupUserStateChanged_Notification(_message.Message):
    __slots__ = ("chat_group_id", "user_chat_group_state", "group_summary", "user_action")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    USER_CHAT_GROUP_STATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    USER_ACTION_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    user_chat_group_state: CUserChatRoomGroupState
    group_summary: CChatRoom_GetChatRoomGroupSummary_Response
    user_action: EChatRoomMemberStateChange
    def __init__(self, chat_group_id: _Optional[int] = ..., user_chat_group_state: _Optional[_Union[CUserChatRoomGroupState, _Mapping]] = ..., group_summary: _Optional[_Union[CChatRoom_GetChatRoomGroupSummary_Response, _Mapping]] = ..., user_action: _Optional[_Union[EChatRoomMemberStateChange, str]] = ...) -> None: ...

class ChatRoomClient_NotifyChatRoomDisconnect_Notification(_message.Message):
    __slots__ = ("chat_group_ids",)
    CHAT_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_group_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_group_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CChatRoomMemberListView(_message.Message):
    __slots__ = ("start", "end", "total_count", "client_changenumber", "server_changenumber")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CHANGENUMBER_FIELD_NUMBER: _ClassVar[int]
    SERVER_CHANGENUMBER_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    total_count: int
    client_changenumber: int
    server_changenumber: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ..., total_count: _Optional[int] = ..., client_changenumber: _Optional[int] = ..., server_changenumber: _Optional[int] = ...) -> None: ...

class CChatRoomMemberSummaryCounts(_message.Message):
    __slots__ = ("ingame", "online", "offline")
    INGAME_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    ingame: int
    online: int
    offline: int
    def __init__(self, ingame: _Optional[int] = ..., online: _Optional[int] = ..., offline: _Optional[int] = ...) -> None: ...

class CChatRoomClient_MemberListViewUpdated_Notification(_message.Message):
    __slots__ = ("chat_group_id", "view_id", "view", "members", "status_flags", "member_summary", "subscribed_personas")
    class MemberListViewEntry(_message.Message):
        __slots__ = ("rank", "accountid", "persona")
        RANK_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_FIELD_NUMBER: _ClassVar[int]
        rank: int
        accountid: int
        persona: _steammessages_clientserver_friends_pb2.CMsgClientPersonaState.Friend
        def __init__(self, rank: _Optional[int] = ..., accountid: _Optional[int] = ..., persona: _Optional[_Union[_steammessages_clientserver_friends_pb2.CMsgClientPersonaState.Friend, _Mapping]] = ...) -> None: ...
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FLAGS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_PERSONAS_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    view_id: int
    view: CChatRoomMemberListView
    members: _containers.RepeatedCompositeFieldContainer[CChatRoomClient_MemberListViewUpdated_Notification.MemberListViewEntry]
    status_flags: int
    member_summary: CChatRoomMemberSummaryCounts
    subscribed_personas: _containers.RepeatedCompositeFieldContainer[_steammessages_clientserver_friends_pb2.CMsgClientPersonaState.Friend]
    def __init__(self, chat_group_id: _Optional[int] = ..., view_id: _Optional[int] = ..., view: _Optional[_Union[CChatRoomMemberListView, _Mapping]] = ..., members: _Optional[_Iterable[_Union[CChatRoomClient_MemberListViewUpdated_Notification.MemberListViewEntry, _Mapping]]] = ..., status_flags: _Optional[int] = ..., member_summary: _Optional[_Union[CChatRoomMemberSummaryCounts, _Mapping]] = ..., subscribed_personas: _Optional[_Iterable[_Union[_steammessages_clientserver_friends_pb2.CMsgClientPersonaState.Friend, _Mapping]]] = ...) -> None: ...

class CChatRoom_MessageReaction_Notification(_message.Message):
    __slots__ = ("chat_group_id", "chat_id", "server_timestamp", "ordinal", "reactor", "reaction_type", "reaction", "is_add")
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    REACTOR_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    chat_group_id: int
    chat_id: int
    server_timestamp: int
    ordinal: int
    reactor: int
    reaction_type: EChatRoomMessageReactionType
    reaction: str
    is_add: bool
    def __init__(self, chat_group_id: _Optional[int] = ..., chat_id: _Optional[int] = ..., server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., reactor: _Optional[int] = ..., reaction_type: _Optional[_Union[EChatRoomMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., is_add: bool = ...) -> None: ...

class CChatUsability_ClientUsabilityMetrics_Notification(_message.Message):
    __slots__ = ("metrics_run_id", "client_build", "metrics_version", "in_web", "settings", "voice_settings", "ui_state", "metrics")
    class Settings(_message.Message):
        __slots__ = ("notifications_show_ingame", "notifications_show_online", "notifications_show_message", "notifications_events_and_announcements", "sounds_play_ingame", "sounds_play_online", "sounds_play_message", "sounds_events_and_announcements", "always_new_chat_window", "force_alphabetic_friend_sorting", "chat_flash_mode", "remember_open_chats", "compact_quick_access", "compact_friends_list", "notifications_show_chat_room_notification", "sounds_play_chat_room_notification", "hide_offline_friends_in_tag_groups", "hide_categorized_friends", "categorize_in_game_friends_by_game", "chat_font_size", "use24hour_clock", "do_not_disturb_mode", "disable_embed_inlining", "sign_into_friends", "animated_avatars")
        NOTIFICATIONS_SHOW_INGAME_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATIONS_SHOW_ONLINE_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATIONS_SHOW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATIONS_EVENTS_AND_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
        SOUNDS_PLAY_INGAME_FIELD_NUMBER: _ClassVar[int]
        SOUNDS_PLAY_ONLINE_FIELD_NUMBER: _ClassVar[int]
        SOUNDS_PLAY_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SOUNDS_EVENTS_AND_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
        ALWAYS_NEW_CHAT_WINDOW_FIELD_NUMBER: _ClassVar[int]
        FORCE_ALPHABETIC_FRIEND_SORTING_FIELD_NUMBER: _ClassVar[int]
        CHAT_FLASH_MODE_FIELD_NUMBER: _ClassVar[int]
        REMEMBER_OPEN_CHATS_FIELD_NUMBER: _ClassVar[int]
        COMPACT_QUICK_ACCESS_FIELD_NUMBER: _ClassVar[int]
        COMPACT_FRIENDS_LIST_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATIONS_SHOW_CHAT_ROOM_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        SOUNDS_PLAY_CHAT_ROOM_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        HIDE_OFFLINE_FRIENDS_IN_TAG_GROUPS_FIELD_NUMBER: _ClassVar[int]
        HIDE_CATEGORIZED_FRIENDS_FIELD_NUMBER: _ClassVar[int]
        CATEGORIZE_IN_GAME_FRIENDS_BY_GAME_FIELD_NUMBER: _ClassVar[int]
        CHAT_FONT_SIZE_FIELD_NUMBER: _ClassVar[int]
        USE24HOUR_CLOCK_FIELD_NUMBER: _ClassVar[int]
        DO_NOT_DISTURB_MODE_FIELD_NUMBER: _ClassVar[int]
        DISABLE_EMBED_INLINING_FIELD_NUMBER: _ClassVar[int]
        SIGN_INTO_FRIENDS_FIELD_NUMBER: _ClassVar[int]
        ANIMATED_AVATARS_FIELD_NUMBER: _ClassVar[int]
        notifications_show_ingame: bool
        notifications_show_online: bool
        notifications_show_message: bool
        notifications_events_and_announcements: bool
        sounds_play_ingame: bool
        sounds_play_online: bool
        sounds_play_message: bool
        sounds_events_and_announcements: bool
        always_new_chat_window: bool
        force_alphabetic_friend_sorting: bool
        chat_flash_mode: int
        remember_open_chats: bool
        compact_quick_access: bool
        compact_friends_list: bool
        notifications_show_chat_room_notification: bool
        sounds_play_chat_room_notification: bool
        hide_offline_friends_in_tag_groups: bool
        hide_categorized_friends: bool
        categorize_in_game_friends_by_game: bool
        chat_font_size: int
        use24hour_clock: bool
        do_not_disturb_mode: bool
        disable_embed_inlining: bool
        sign_into_friends: bool
        animated_avatars: bool
        def __init__(self, notifications_show_ingame: bool = ..., notifications_show_online: bool = ..., notifications_show_message: bool = ..., notifications_events_and_announcements: bool = ..., sounds_play_ingame: bool = ..., sounds_play_online: bool = ..., sounds_play_message: bool = ..., sounds_events_and_announcements: bool = ..., always_new_chat_window: bool = ..., force_alphabetic_friend_sorting: bool = ..., chat_flash_mode: _Optional[int] = ..., remember_open_chats: bool = ..., compact_quick_access: bool = ..., compact_friends_list: bool = ..., notifications_show_chat_room_notification: bool = ..., sounds_play_chat_room_notification: bool = ..., hide_offline_friends_in_tag_groups: bool = ..., hide_categorized_friends: bool = ..., categorize_in_game_friends_by_game: bool = ..., chat_font_size: _Optional[int] = ..., use24hour_clock: bool = ..., do_not_disturb_mode: bool = ..., disable_embed_inlining: bool = ..., sign_into_friends: bool = ..., animated_avatars: bool = ...) -> None: ...
    class VoiceSettings(_message.Message):
        __slots__ = ("voice_input_gain", "voice_output_gain", "noise_gate_level", "voice_use_echo_cancellation", "voice_use_noise_cancellation", "voice_use_auto_gain_control", "selected_non_default_mic", "selected_non_default_output", "push_to_talk_enabled", "push_to_mute_enabled", "play_ptt_sounds")
        VOICE_INPUT_GAIN_FIELD_NUMBER: _ClassVar[int]
        VOICE_OUTPUT_GAIN_FIELD_NUMBER: _ClassVar[int]
        NOISE_GATE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        VOICE_USE_ECHO_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
        VOICE_USE_NOISE_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
        VOICE_USE_AUTO_GAIN_CONTROL_FIELD_NUMBER: _ClassVar[int]
        SELECTED_NON_DEFAULT_MIC_FIELD_NUMBER: _ClassVar[int]
        SELECTED_NON_DEFAULT_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        PUSH_TO_TALK_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PUSH_TO_MUTE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PLAY_PTT_SOUNDS_FIELD_NUMBER: _ClassVar[int]
        voice_input_gain: float
        voice_output_gain: float
        noise_gate_level: int
        voice_use_echo_cancellation: bool
        voice_use_noise_cancellation: bool
        voice_use_auto_gain_control: bool
        selected_non_default_mic: bool
        selected_non_default_output: bool
        push_to_talk_enabled: bool
        push_to_mute_enabled: bool
        play_ptt_sounds: bool
        def __init__(self, voice_input_gain: _Optional[float] = ..., voice_output_gain: _Optional[float] = ..., noise_gate_level: _Optional[int] = ..., voice_use_echo_cancellation: bool = ..., voice_use_noise_cancellation: bool = ..., voice_use_auto_gain_control: bool = ..., selected_non_default_mic: bool = ..., selected_non_default_output: bool = ..., push_to_talk_enabled: bool = ..., push_to_mute_enabled: bool = ..., play_ptt_sounds: bool = ...) -> None: ...
    class UIState(_message.Message):
        __slots__ = ("friends_list_height", "friends_list_width", "friends_list_docked", "friends_list_collapsed", "friends_list_group_chats_height", "friends_list_visible", "chat_popups_opened", "group_chat_tabs_opened", "friend_chat_tabs_opened", "chat_window_width", "chat_window_height", "category_collapse", "group_chat_left_col_collapsed", "group_chat_right_col_collapsed", "in_one_on_one_voice_chat", "in_group_voice_chat")
        class CategoryCollapseState(_message.Message):
            __slots__ = ("in_game_collapsed", "online_collapsed", "offline_collapsed", "game_groups_collapsed", "categories_collapsed")
            IN_GAME_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
            ONLINE_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
            OFFLINE_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
            GAME_GROUPS_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
            CATEGORIES_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
            in_game_collapsed: bool
            online_collapsed: bool
            offline_collapsed: bool
            game_groups_collapsed: int
            categories_collapsed: int
            def __init__(self, in_game_collapsed: bool = ..., online_collapsed: bool = ..., offline_collapsed: bool = ..., game_groups_collapsed: _Optional[int] = ..., categories_collapsed: _Optional[int] = ...) -> None: ...
        FRIENDS_LIST_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_LIST_WIDTH_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_LIST_DOCKED_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_LIST_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_LIST_GROUP_CHATS_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_LIST_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        CHAT_POPUPS_OPENED_FIELD_NUMBER: _ClassVar[int]
        GROUP_CHAT_TABS_OPENED_FIELD_NUMBER: _ClassVar[int]
        FRIEND_CHAT_TABS_OPENED_FIELD_NUMBER: _ClassVar[int]
        CHAT_WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
        CHAT_WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_COLLAPSE_FIELD_NUMBER: _ClassVar[int]
        GROUP_CHAT_LEFT_COL_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
        GROUP_CHAT_RIGHT_COL_COLLAPSED_FIELD_NUMBER: _ClassVar[int]
        IN_ONE_ON_ONE_VOICE_CHAT_FIELD_NUMBER: _ClassVar[int]
        IN_GROUP_VOICE_CHAT_FIELD_NUMBER: _ClassVar[int]
        friends_list_height: int
        friends_list_width: int
        friends_list_docked: bool
        friends_list_collapsed: bool
        friends_list_group_chats_height: int
        friends_list_visible: bool
        chat_popups_opened: int
        group_chat_tabs_opened: int
        friend_chat_tabs_opened: int
        chat_window_width: int
        chat_window_height: int
        category_collapse: CChatUsability_ClientUsabilityMetrics_Notification.UIState.CategoryCollapseState
        group_chat_left_col_collapsed: int
        group_chat_right_col_collapsed: int
        in_one_on_one_voice_chat: bool
        in_group_voice_chat: bool
        def __init__(self, friends_list_height: _Optional[int] = ..., friends_list_width: _Optional[int] = ..., friends_list_docked: bool = ..., friends_list_collapsed: bool = ..., friends_list_group_chats_height: _Optional[int] = ..., friends_list_visible: bool = ..., chat_popups_opened: _Optional[int] = ..., group_chat_tabs_opened: _Optional[int] = ..., friend_chat_tabs_opened: _Optional[int] = ..., chat_window_width: _Optional[int] = ..., chat_window_height: _Optional[int] = ..., category_collapse: _Optional[_Union[CChatUsability_ClientUsabilityMetrics_Notification.UIState.CategoryCollapseState, _Mapping]] = ..., group_chat_left_col_collapsed: _Optional[int] = ..., group_chat_right_col_collapsed: _Optional[int] = ..., in_one_on_one_voice_chat: bool = ..., in_group_voice_chat: bool = ...) -> None: ...
    class Metrics(_message.Message):
        __slots__ = ("friends_count", "friends_category_count", "friends_categorized_count", "friends_online_count", "friends_in_game_count", "friends_in_game_singleton_count", "game_group_count", "friends_favorite_count", "group_chat_count", "group_chat_favorite_count")
        FRIENDS_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_CATEGORY_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_CATEGORIZED_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_ONLINE_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_IN_GAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_IN_GAME_SINGLETON_COUNT_FIELD_NUMBER: _ClassVar[int]
        GAME_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_FAVORITE_COUNT_FIELD_NUMBER: _ClassVar[int]
        GROUP_CHAT_COUNT_FIELD_NUMBER: _ClassVar[int]
        GROUP_CHAT_FAVORITE_COUNT_FIELD_NUMBER: _ClassVar[int]
        friends_count: int
        friends_category_count: int
        friends_categorized_count: int
        friends_online_count: int
        friends_in_game_count: int
        friends_in_game_singleton_count: int
        game_group_count: int
        friends_favorite_count: int
        group_chat_count: int
        group_chat_favorite_count: int
        def __init__(self, friends_count: _Optional[int] = ..., friends_category_count: _Optional[int] = ..., friends_categorized_count: _Optional[int] = ..., friends_online_count: _Optional[int] = ..., friends_in_game_count: _Optional[int] = ..., friends_in_game_singleton_count: _Optional[int] = ..., game_group_count: _Optional[int] = ..., friends_favorite_count: _Optional[int] = ..., group_chat_count: _Optional[int] = ..., group_chat_favorite_count: _Optional[int] = ...) -> None: ...
    METRICS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_BUILD_FIELD_NUMBER: _ClassVar[int]
    METRICS_VERSION_FIELD_NUMBER: _ClassVar[int]
    IN_WEB_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    VOICE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UI_STATE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    metrics_run_id: int
    client_build: int
    metrics_version: int
    in_web: bool
    settings: CChatUsability_ClientUsabilityMetrics_Notification.Settings
    voice_settings: CChatUsability_ClientUsabilityMetrics_Notification.VoiceSettings
    ui_state: CChatUsability_ClientUsabilityMetrics_Notification.UIState
    metrics: CChatUsability_ClientUsabilityMetrics_Notification.Metrics
    def __init__(self, metrics_run_id: _Optional[int] = ..., client_build: _Optional[int] = ..., metrics_version: _Optional[int] = ..., in_web: bool = ..., settings: _Optional[_Union[CChatUsability_ClientUsabilityMetrics_Notification.Settings, _Mapping]] = ..., voice_settings: _Optional[_Union[CChatUsability_ClientUsabilityMetrics_Notification.VoiceSettings, _Mapping]] = ..., ui_state: _Optional[_Union[CChatUsability_ClientUsabilityMetrics_Notification.UIState, _Mapping]] = ..., metrics: _Optional[_Union[CChatUsability_ClientUsabilityMetrics_Notification.Metrics, _Mapping]] = ...) -> None: ...

class CChatUsability_RequestClientUsabilityMetrics_Notification(_message.Message):
    __slots__ = ("metrics_run_id",)
    METRICS_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    metrics_run_id: int
    def __init__(self, metrics_run_id: _Optional[int] = ...) -> None: ...

class Chat(_service.service): ...

class Chat_Stub(Chat): ...

class ChatRoom(_service.service): ...

class ChatRoom_Stub(ChatRoom): ...

class ClanChatRooms(_service.service): ...

class ClanChatRooms_Stub(ClanChatRooms): ...

class ChatRoomClient(_service.service): ...

class ChatRoomClient_Stub(ChatRoomClient): ...

class ChatUsability(_service.service): ...

class ChatUsability_Stub(ChatUsability): ...

class ChatUsabilityClient(_service.service): ...

class ChatUsabilityClient_Stub(ChatUsabilityClient): ...
