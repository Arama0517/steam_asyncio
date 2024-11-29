import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EMessageReactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMessageReactionType_Invalid: _ClassVar[EMessageReactionType]
    k_EMessageReactionType_Emoticon: _ClassVar[EMessageReactionType]
    k_EMessageReactionType_Sticker: _ClassVar[EMessageReactionType]
k_EMessageReactionType_Invalid: EMessageReactionType
k_EMessageReactionType_Emoticon: EMessageReactionType
k_EMessageReactionType_Sticker: EMessageReactionType

class CFriendMessages_GetRecentMessages_Request(_message.Message):
    __slots__ = ("steamid1", "steamid2", "count", "most_recent_conversation", "rtime32_start_time", "bbcode_format", "start_ordinal", "time_last", "ordinal_last")
    STEAMID1_FIELD_NUMBER: _ClassVar[int]
    STEAMID2_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    MOST_RECENT_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    RTIME32_START_TIME_FIELD_NUMBER: _ClassVar[int]
    BBCODE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    START_ORDINAL_FIELD_NUMBER: _ClassVar[int]
    TIME_LAST_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_LAST_FIELD_NUMBER: _ClassVar[int]
    steamid1: int
    steamid2: int
    count: int
    most_recent_conversation: bool
    rtime32_start_time: int
    bbcode_format: bool
    start_ordinal: int
    time_last: int
    ordinal_last: int
    def __init__(self, steamid1: _Optional[int] = ..., steamid2: _Optional[int] = ..., count: _Optional[int] = ..., most_recent_conversation: bool = ..., rtime32_start_time: _Optional[int] = ..., bbcode_format: bool = ..., start_ordinal: _Optional[int] = ..., time_last: _Optional[int] = ..., ordinal_last: _Optional[int] = ...) -> None: ...

class CFriendMessages_GetRecentMessages_Response(_message.Message):
    __slots__ = ("messages", "more_available")
    class FriendMessage(_message.Message):
        __slots__ = ("accountid", "timestamp", "message", "ordinal", "reactions")
        class MessageReaction(_message.Message):
            __slots__ = ("reaction_type", "reaction", "reactors")
            REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
            REACTION_FIELD_NUMBER: _ClassVar[int]
            REACTORS_FIELD_NUMBER: _ClassVar[int]
            reaction_type: EMessageReactionType
            reaction: str
            reactors: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, reaction_type: _Optional[_Union[EMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., reactors: _Optional[_Iterable[int]] = ...) -> None: ...
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ORDINAL_FIELD_NUMBER: _ClassVar[int]
        REACTIONS_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        timestamp: int
        message: str
        ordinal: int
        reactions: _containers.RepeatedCompositeFieldContainer[CFriendMessages_GetRecentMessages_Response.FriendMessage.MessageReaction]
        def __init__(self, accountid: _Optional[int] = ..., timestamp: _Optional[int] = ..., message: _Optional[str] = ..., ordinal: _Optional[int] = ..., reactions: _Optional[_Iterable[_Union[CFriendMessages_GetRecentMessages_Response.FriendMessage.MessageReaction, _Mapping]]] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MORE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CFriendMessages_GetRecentMessages_Response.FriendMessage]
    more_available: bool
    def __init__(self, messages: _Optional[_Iterable[_Union[CFriendMessages_GetRecentMessages_Response.FriendMessage, _Mapping]]] = ..., more_available: bool = ...) -> None: ...

class CFriendsMessages_GetActiveMessageSessions_Request(_message.Message):
    __slots__ = ("lastmessage_since", "only_sessions_with_messages")
    LASTMESSAGE_SINCE_FIELD_NUMBER: _ClassVar[int]
    ONLY_SESSIONS_WITH_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    lastmessage_since: int
    only_sessions_with_messages: bool
    def __init__(self, lastmessage_since: _Optional[int] = ..., only_sessions_with_messages: bool = ...) -> None: ...

class CFriendsMessages_GetActiveMessageSessions_Response(_message.Message):
    __slots__ = ("message_sessions", "timestamp")
    class FriendMessageSession(_message.Message):
        __slots__ = ("accountid_friend", "last_message", "last_view", "unread_message_count")
        ACCOUNTID_FRIEND_FIELD_NUMBER: _ClassVar[int]
        LAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        LAST_VIEW_FIELD_NUMBER: _ClassVar[int]
        UNREAD_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
        accountid_friend: int
        last_message: int
        last_view: int
        unread_message_count: int
        def __init__(self, accountid_friend: _Optional[int] = ..., last_message: _Optional[int] = ..., last_view: _Optional[int] = ..., unread_message_count: _Optional[int] = ...) -> None: ...
    MESSAGE_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    message_sessions: _containers.RepeatedCompositeFieldContainer[CFriendsMessages_GetActiveMessageSessions_Response.FriendMessageSession]
    timestamp: int
    def __init__(self, message_sessions: _Optional[_Iterable[_Union[CFriendsMessages_GetActiveMessageSessions_Response.FriendMessageSession, _Mapping]]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CFriendMessages_SendMessage_Request(_message.Message):
    __slots__ = ("steamid", "chat_entry_type", "message", "contains_bbcode", "echo_to_sender", "low_priority", "client_message_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTAINS_BBCODE_FIELD_NUMBER: _ClassVar[int]
    ECHO_TO_SENDER_FIELD_NUMBER: _ClassVar[int]
    LOW_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CLIENT_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    chat_entry_type: int
    message: str
    contains_bbcode: bool
    echo_to_sender: bool
    low_priority: bool
    client_message_id: str
    def __init__(self, steamid: _Optional[int] = ..., chat_entry_type: _Optional[int] = ..., message: _Optional[str] = ..., contains_bbcode: bool = ..., echo_to_sender: bool = ..., low_priority: bool = ..., client_message_id: _Optional[str] = ...) -> None: ...

class CFriendMessages_SendMessage_Response(_message.Message):
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

class CFriendMessages_AckMessage_Notification(_message.Message):
    __slots__ = ("steamid_partner", "timestamp")
    STEAMID_PARTNER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    steamid_partner: int
    timestamp: int
    def __init__(self, steamid_partner: _Optional[int] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CFriendMessages_IsInFriendsUIBeta_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CFriendMessages_IsInFriendsUIBeta_Response(_message.Message):
    __slots__ = ("online_in_friendsui", "has_used_friendsui")
    ONLINE_IN_FRIENDSUI_FIELD_NUMBER: _ClassVar[int]
    HAS_USED_FRIENDSUI_FIELD_NUMBER: _ClassVar[int]
    online_in_friendsui: bool
    has_used_friendsui: bool
    def __init__(self, online_in_friendsui: bool = ..., has_used_friendsui: bool = ...) -> None: ...

class CFriendMessages_UpdateMessageReaction_Request(_message.Message):
    __slots__ = ("steamid", "server_timestamp", "ordinal", "reaction_type", "reaction", "is_add")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    server_timestamp: int
    ordinal: int
    reaction_type: EMessageReactionType
    reaction: str
    is_add: bool
    def __init__(self, steamid: _Optional[int] = ..., server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., reaction_type: _Optional[_Union[EMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., is_add: bool = ...) -> None: ...

class CFriendMessages_UpdateMessageReaction_Response(_message.Message):
    __slots__ = ("reactors",)
    REACTORS_FIELD_NUMBER: _ClassVar[int]
    reactors: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, reactors: _Optional[_Iterable[int]] = ...) -> None: ...

class CFriendMessages_IncomingMessage_Notification(_message.Message):
    __slots__ = ("steamid_friend", "chat_entry_type", "from_limited_account", "message", "rtime32_server_timestamp", "ordinal", "local_echo", "message_no_bbcode", "low_priority")
    STEAMID_FRIEND_FIELD_NUMBER: _ClassVar[int]
    CHAT_ENTRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    FROM_LIMITED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RTIME32_SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ECHO_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_NO_BBCODE_FIELD_NUMBER: _ClassVar[int]
    LOW_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    steamid_friend: int
    chat_entry_type: int
    from_limited_account: bool
    message: str
    rtime32_server_timestamp: int
    ordinal: int
    local_echo: bool
    message_no_bbcode: str
    low_priority: bool
    def __init__(self, steamid_friend: _Optional[int] = ..., chat_entry_type: _Optional[int] = ..., from_limited_account: bool = ..., message: _Optional[str] = ..., rtime32_server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., local_echo: bool = ..., message_no_bbcode: _Optional[str] = ..., low_priority: bool = ...) -> None: ...

class CFriendMessages_MessageReaction_Notification(_message.Message):
    __slots__ = ("steamid_friend", "server_timestamp", "ordinal", "reactor", "reaction_type", "reaction", "is_add")
    STEAMID_FRIEND_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    REACTOR_FIELD_NUMBER: _ClassVar[int]
    REACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    IS_ADD_FIELD_NUMBER: _ClassVar[int]
    steamid_friend: int
    server_timestamp: int
    ordinal: int
    reactor: int
    reaction_type: EMessageReactionType
    reaction: str
    is_add: bool
    def __init__(self, steamid_friend: _Optional[int] = ..., server_timestamp: _Optional[int] = ..., ordinal: _Optional[int] = ..., reactor: _Optional[int] = ..., reaction_type: _Optional[_Union[EMessageReactionType, str]] = ..., reaction: _Optional[str] = ..., is_add: bool = ...) -> None: ...

class FriendMessages(_service.service): ...

class FriendMessages_Stub(FriendMessages): ...

class FriendMessagesClient(_service.service): ...

class FriendMessagesClient_Stub(FriendMessagesClient): ...
