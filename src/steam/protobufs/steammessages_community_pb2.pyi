import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EPartnerEventDisplayLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EPartnerEventDisplayLocation_Invalid: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_AppDetailsSpotlight: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_LibraryOverview: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_StoreAppPage: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_EventScroller: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_AppDetailsActivity: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_CommunityHub: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_StoreFrontPage: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_NewsHub: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_GamepadHome: _ClassVar[EPartnerEventDisplayLocation]
    k_EPartnerEventDisplayLocation_StoreHub: _ClassVar[EPartnerEventDisplayLocation]
k_EPartnerEventDisplayLocation_Invalid: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_AppDetailsSpotlight: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_LibraryOverview: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_StoreAppPage: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_EventScroller: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_AppDetailsActivity: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_CommunityHub: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_StoreFrontPage: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_NewsHub: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_GamepadHome: EPartnerEventDisplayLocation
k_EPartnerEventDisplayLocation_StoreHub: EPartnerEventDisplayLocation

class CCommunity_GetApps_Request(_message.Message):
    __slots__ = ("appids", "language")
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    language: int
    def __init__(self, appids: _Optional[_Iterable[int]] = ..., language: _Optional[int] = ...) -> None: ...

class CCommunity_GetApps_Response(_message.Message):
    __slots__ = ("apps",)
    APPS_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[_steammessages_base_pb2.CCDDBAppDetailCommon]
    def __init__(self, apps: _Optional[_Iterable[_Union[_steammessages_base_pb2.CCDDBAppDetailCommon, _Mapping]]] = ...) -> None: ...

class CCommunity_GetAppRichPresenceLocalization_Request(_message.Message):
    __slots__ = ("appid", "language")
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    language: str
    def __init__(self, appid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CCommunity_GetAppRichPresenceLocalization_Response(_message.Message):
    __slots__ = ("appid", "token_lists")
    class Token(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: str
        def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TokenList(_message.Message):
        __slots__ = ("language", "tokens")
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        TOKENS_FIELD_NUMBER: _ClassVar[int]
        language: str
        tokens: _containers.RepeatedCompositeFieldContainer[CCommunity_GetAppRichPresenceLocalization_Response.Token]
        def __init__(self, language: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[CCommunity_GetAppRichPresenceLocalization_Response.Token, _Mapping]]] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_LISTS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    token_lists: _containers.RepeatedCompositeFieldContainer[CCommunity_GetAppRichPresenceLocalization_Response.TokenList]
    def __init__(self, appid: _Optional[int] = ..., token_lists: _Optional[_Iterable[_Union[CCommunity_GetAppRichPresenceLocalization_Response.TokenList, _Mapping]]] = ...) -> None: ...

class CCommunity_GetCommentThread_Request(_message.Message):
    __slots__ = ("steamid", "comment_thread_type", "gidfeature", "gidfeature2", "commentthreadid", "start", "count", "upvoters", "include_deleted", "gidcomment", "time_oldest", "oldest_first")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_THREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE2_FIELD_NUMBER: _ClassVar[int]
    COMMENTTHREADID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UPVOTERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_FIELD_NUMBER: _ClassVar[int]
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    TIME_OLDEST_FIELD_NUMBER: _ClassVar[int]
    OLDEST_FIRST_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    comment_thread_type: _enums_pb2.ECommentThreadType
    gidfeature: int
    gidfeature2: int
    commentthreadid: int
    start: int
    count: int
    upvoters: int
    include_deleted: bool
    gidcomment: int
    time_oldest: int
    oldest_first: bool
    def __init__(self, steamid: _Optional[int] = ..., comment_thread_type: _Optional[_Union[_enums_pb2.ECommentThreadType, str]] = ..., gidfeature: _Optional[int] = ..., gidfeature2: _Optional[int] = ..., commentthreadid: _Optional[int] = ..., start: _Optional[int] = ..., count: _Optional[int] = ..., upvoters: _Optional[int] = ..., include_deleted: bool = ..., gidcomment: _Optional[int] = ..., time_oldest: _Optional[int] = ..., oldest_first: bool = ...) -> None: ...

class CCommunity_Comment(_message.Message):
    __slots__ = ("gidcomment", "steamid", "timestamp", "text", "upvotes", "hidden", "hidden_by_user", "deleted", "ipaddress", "total_hidden", "upvoted_by_user", "reactions", "gidparentcomment")
    class Reaction(_message.Message):
        __slots__ = ("reactionid", "count")
        REACTIONID_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        reactionid: int
        count: int
        def __init__(self, reactionid: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    UPVOTES_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_BY_USER_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    IPADDRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    UPVOTED_BY_USER_FIELD_NUMBER: _ClassVar[int]
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    GIDPARENTCOMMENT_FIELD_NUMBER: _ClassVar[int]
    gidcomment: int
    steamid: int
    timestamp: int
    text: str
    upvotes: int
    hidden: bool
    hidden_by_user: bool
    deleted: bool
    ipaddress: _steammessages_base_pb2.CMsgIPAddress
    total_hidden: int
    upvoted_by_user: bool
    reactions: _containers.RepeatedCompositeFieldContainer[CCommunity_Comment.Reaction]
    gidparentcomment: int
    def __init__(self, gidcomment: _Optional[int] = ..., steamid: _Optional[int] = ..., timestamp: _Optional[int] = ..., text: _Optional[str] = ..., upvotes: _Optional[int] = ..., hidden: bool = ..., hidden_by_user: bool = ..., deleted: bool = ..., ipaddress: _Optional[_Union[_steammessages_base_pb2.CMsgIPAddress, _Mapping]] = ..., total_hidden: _Optional[int] = ..., upvoted_by_user: bool = ..., reactions: _Optional[_Iterable[_Union[CCommunity_Comment.Reaction, _Mapping]]] = ..., gidparentcomment: _Optional[int] = ...) -> None: ...

class CCommunity_GetCommentThread_Response(_message.Message):
    __slots__ = ("comments", "deleted_comments", "steamid", "commentthreadid", "start", "count", "total_count", "upvotes", "upvoters", "user_subscribed", "user_upvoted", "answer_commentid", "answer_actor", "answer_actor_rank", "can_post", "comment_thread_type", "gidfeature", "gidfeature2")
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    DELETED_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    COMMENTTHREADID_FIELD_NUMBER: _ClassVar[int]
    START_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPVOTES_FIELD_NUMBER: _ClassVar[int]
    UPVOTERS_FIELD_NUMBER: _ClassVar[int]
    USER_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    USER_UPVOTED_FIELD_NUMBER: _ClassVar[int]
    ANSWER_COMMENTID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_ACTOR_FIELD_NUMBER: _ClassVar[int]
    ANSWER_ACTOR_RANK_FIELD_NUMBER: _ClassVar[int]
    CAN_POST_FIELD_NUMBER: _ClassVar[int]
    COMMENT_THREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE2_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[CCommunity_Comment]
    deleted_comments: _containers.RepeatedCompositeFieldContainer[CCommunity_Comment]
    steamid: int
    commentthreadid: int
    start: int
    count: int
    total_count: int
    upvotes: int
    upvoters: _containers.RepeatedScalarFieldContainer[int]
    user_subscribed: bool
    user_upvoted: bool
    answer_commentid: int
    answer_actor: int
    answer_actor_rank: int
    can_post: bool
    comment_thread_type: int
    gidfeature: int
    gidfeature2: int
    def __init__(self, comments: _Optional[_Iterable[_Union[CCommunity_Comment, _Mapping]]] = ..., deleted_comments: _Optional[_Iterable[_Union[CCommunity_Comment, _Mapping]]] = ..., steamid: _Optional[int] = ..., commentthreadid: _Optional[int] = ..., start: _Optional[int] = ..., count: _Optional[int] = ..., total_count: _Optional[int] = ..., upvotes: _Optional[int] = ..., upvoters: _Optional[_Iterable[int]] = ..., user_subscribed: bool = ..., user_upvoted: bool = ..., answer_commentid: _Optional[int] = ..., answer_actor: _Optional[int] = ..., answer_actor_rank: _Optional[int] = ..., can_post: bool = ..., comment_thread_type: _Optional[int] = ..., gidfeature: _Optional[int] = ..., gidfeature2: _Optional[int] = ...) -> None: ...

class CCommunity_PostCommentToThread_Request(_message.Message):
    __slots__ = ("steamid", "comment_thread_type", "gidfeature", "gidfeature2", "text", "gidparentcomment", "suppress_notifications", "is_report", "start_hidden")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_THREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE2_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    GIDPARENTCOMMENT_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    IS_REPORT_FIELD_NUMBER: _ClassVar[int]
    START_HIDDEN_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    comment_thread_type: _enums_pb2.ECommentThreadType
    gidfeature: int
    gidfeature2: int
    text: str
    gidparentcomment: int
    suppress_notifications: bool
    is_report: bool
    start_hidden: bool
    def __init__(self, steamid: _Optional[int] = ..., comment_thread_type: _Optional[_Union[_enums_pb2.ECommentThreadType, str]] = ..., gidfeature: _Optional[int] = ..., gidfeature2: _Optional[int] = ..., text: _Optional[str] = ..., gidparentcomment: _Optional[int] = ..., suppress_notifications: bool = ..., is_report: bool = ..., start_hidden: bool = ...) -> None: ...

class CCommunity_PostCommentToThread_Response(_message.Message):
    __slots__ = ("gidcomment", "commentthreadid", "count", "upvotes")
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENTTHREADID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UPVOTES_FIELD_NUMBER: _ClassVar[int]
    gidcomment: int
    commentthreadid: int
    count: int
    upvotes: int
    def __init__(self, gidcomment: _Optional[int] = ..., commentthreadid: _Optional[int] = ..., count: _Optional[int] = ..., upvotes: _Optional[int] = ...) -> None: ...

class CCommunity_DeleteCommentFromThread_Request(_message.Message):
    __slots__ = ("steamid", "comment_thread_type", "gidfeature", "gidfeature2", "gidcomment", "undelete")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_THREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE2_FIELD_NUMBER: _ClassVar[int]
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    UNDELETE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    comment_thread_type: _enums_pb2.ECommentThreadType
    gidfeature: int
    gidfeature2: int
    gidcomment: int
    undelete: bool
    def __init__(self, steamid: _Optional[int] = ..., comment_thread_type: _Optional[_Union[_enums_pb2.ECommentThreadType, str]] = ..., gidfeature: _Optional[int] = ..., gidfeature2: _Optional[int] = ..., gidcomment: _Optional[int] = ..., undelete: bool = ...) -> None: ...

class CCommunity_DeleteCommentFromThread_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_RateCommentThread_Request(_message.Message):
    __slots__ = ("commentthreadtype", "steamid", "gidfeature", "gidfeature2", "gidcomment", "rate_up", "suppress_notifications")
    COMMENTTHREADTYPE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE2_FIELD_NUMBER: _ClassVar[int]
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    RATE_UP_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    commentthreadtype: str
    steamid: int
    gidfeature: int
    gidfeature2: int
    gidcomment: int
    rate_up: bool
    suppress_notifications: bool
    def __init__(self, commentthreadtype: _Optional[str] = ..., steamid: _Optional[int] = ..., gidfeature: _Optional[int] = ..., gidfeature2: _Optional[int] = ..., gidcomment: _Optional[int] = ..., rate_up: bool = ..., suppress_notifications: bool = ...) -> None: ...

class CCommunity_RateCommentThread_Response(_message.Message):
    __slots__ = ("gidcomment", "commentthreadid", "count", "upvotes", "has_upvoted")
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENTTHREADID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    UPVOTES_FIELD_NUMBER: _ClassVar[int]
    HAS_UPVOTED_FIELD_NUMBER: _ClassVar[int]
    gidcomment: int
    commentthreadid: int
    count: int
    upvotes: int
    has_upvoted: bool
    def __init__(self, gidcomment: _Optional[int] = ..., commentthreadid: _Optional[int] = ..., count: _Optional[int] = ..., upvotes: _Optional[int] = ..., has_upvoted: bool = ...) -> None: ...

class CCommunity_GetCommentThreadRatings_Request(_message.Message):
    __slots__ = ("commentthreadtype", "steamid", "gidfeature", "gidfeature2", "gidcomment", "max_results")
    COMMENTTHREADTYPE_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE_FIELD_NUMBER: _ClassVar[int]
    GIDFEATURE2_FIELD_NUMBER: _ClassVar[int]
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_RESULTS_FIELD_NUMBER: _ClassVar[int]
    commentthreadtype: str
    steamid: int
    gidfeature: int
    gidfeature2: int
    gidcomment: int
    max_results: int
    def __init__(self, commentthreadtype: _Optional[str] = ..., steamid: _Optional[int] = ..., gidfeature: _Optional[int] = ..., gidfeature2: _Optional[int] = ..., gidcomment: _Optional[int] = ..., max_results: _Optional[int] = ...) -> None: ...

class CCommunity_GetCommentThreadRatings_Response(_message.Message):
    __slots__ = ("commentthreadid", "gidcomment", "upvotes", "has_upvoted", "upvoter_accountids")
    COMMENTTHREADID_FIELD_NUMBER: _ClassVar[int]
    GIDCOMMENT_FIELD_NUMBER: _ClassVar[int]
    UPVOTES_FIELD_NUMBER: _ClassVar[int]
    HAS_UPVOTED_FIELD_NUMBER: _ClassVar[int]
    UPVOTER_ACCOUNTIDS_FIELD_NUMBER: _ClassVar[int]
    commentthreadid: int
    gidcomment: int
    upvotes: int
    has_upvoted: bool
    upvoter_accountids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, commentthreadid: _Optional[int] = ..., gidcomment: _Optional[int] = ..., upvotes: _Optional[int] = ..., has_upvoted: bool = ..., upvoter_accountids: _Optional[_Iterable[int]] = ...) -> None: ...

class CCommunity_RateClanAnnouncement_Request(_message.Message):
    __slots__ = ("announcementid", "vote_up", "clan_accountid")
    ANNOUNCEMENTID_FIELD_NUMBER: _ClassVar[int]
    VOTE_UP_FIELD_NUMBER: _ClassVar[int]
    CLAN_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    announcementid: int
    vote_up: bool
    clan_accountid: int
    def __init__(self, announcementid: _Optional[int] = ..., vote_up: bool = ..., clan_accountid: _Optional[int] = ...) -> None: ...

class CCommunity_RateClanAnnouncement_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_GetClanAnnouncementVoteForUser_Request(_message.Message):
    __slots__ = ("announcementid",)
    ANNOUNCEMENTID_FIELD_NUMBER: _ClassVar[int]
    announcementid: int
    def __init__(self, announcementid: _Optional[int] = ...) -> None: ...

class CCommunity_GetClanAnnouncementVoteForUser_Response(_message.Message):
    __slots__ = ("voted_up", "voted_down")
    VOTED_UP_FIELD_NUMBER: _ClassVar[int]
    VOTED_DOWN_FIELD_NUMBER: _ClassVar[int]
    voted_up: bool
    voted_down: bool
    def __init__(self, voted_up: bool = ..., voted_down: bool = ...) -> None: ...

class CCommunity_GetAvatarHistory_Request(_message.Message):
    __slots__ = ("steamid", "filter_user_uploaded_only")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    FILTER_USER_UPLOADED_ONLY_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    filter_user_uploaded_only: bool
    def __init__(self, steamid: _Optional[int] = ..., filter_user_uploaded_only: bool = ...) -> None: ...

class CCommunity_GetAvatarHistory_Response(_message.Message):
    __slots__ = ("avatars",)
    class AvatarData(_message.Message):
        __slots__ = ("avatar_sha1", "user_uploaded", "timestamp")
        AVATAR_SHA1_FIELD_NUMBER: _ClassVar[int]
        USER_UPLOADED_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        avatar_sha1: str
        user_uploaded: bool
        timestamp: int
        def __init__(self, avatar_sha1: _Optional[str] = ..., user_uploaded: bool = ..., timestamp: _Optional[int] = ...) -> None: ...
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    avatars: _containers.RepeatedCompositeFieldContainer[CCommunity_GetAvatarHistory_Response.AvatarData]
    def __init__(self, avatars: _Optional[_Iterable[_Union[CCommunity_GetAvatarHistory_Response.AvatarData, _Mapping]]] = ...) -> None: ...

class CCommunity_GetClanEventCrowdInMetadata_Request(_message.Message):
    __slots__ = ("steamid", "itemid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    itemid: int
    def __init__(self, steamid: _Optional[int] = ..., itemid: _Optional[int] = ...) -> None: ...

class CCommunity_GetClanEventCrowdInMetadata_Response(_message.Message):
    __slots__ = ("crowdin_project_id", "crowdin_file_id")
    CROWDIN_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CROWDIN_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    crowdin_project_id: int
    crowdin_file_id: int
    def __init__(self, crowdin_project_id: _Optional[int] = ..., crowdin_file_id: _Optional[int] = ...) -> None: ...

class CCommunity_GetClanCrowdInMetadata_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CCommunity_GetClanCrowdInMetadata_Response(_message.Message):
    __slots__ = ("crowdin_project_id", "crowdin_directory_id", "push_by_default")
    CROWDIN_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CROWDIN_DIRECTORY_ID_FIELD_NUMBER: _ClassVar[int]
    PUSH_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    crowdin_project_id: int
    crowdin_directory_id: int
    push_by_default: bool
    def __init__(self, crowdin_project_id: _Optional[int] = ..., crowdin_directory_id: _Optional[int] = ..., push_by_default: bool = ...) -> None: ...

class CCommunity_FetchTranslationFromCrowdIn_Request(_message.Message):
    __slots__ = ("steamid", "itemid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    itemid: int
    language: int
    def __init__(self, steamid: _Optional[int] = ..., itemid: _Optional[int] = ..., language: _Optional[int] = ...) -> None: ...

class CCommunity_FetchTranslationFromCrowdIn_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAppPriority(_message.Message):
    __slots__ = ("priority", "appid")
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    priority: int
    appid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, priority: _Optional[int] = ..., appid: _Optional[_Iterable[int]] = ...) -> None: ...

class CCommunity_GetUserPartnerEventNews_Request(_message.Message):
    __slots__ = ("count", "offset", "rtime32_start_time", "rtime32_end_time", "language_preference", "filter_event_type", "filter_to_appid", "app_list", "count_after", "count_before")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RTIME32_START_TIME_FIELD_NUMBER: _ClassVar[int]
    RTIME32_END_TIME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    FILTER_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FILTER_TO_APPID_FIELD_NUMBER: _ClassVar[int]
    APP_LIST_FIELD_NUMBER: _ClassVar[int]
    COUNT_AFTER_FIELD_NUMBER: _ClassVar[int]
    COUNT_BEFORE_FIELD_NUMBER: _ClassVar[int]
    count: int
    offset: int
    rtime32_start_time: int
    rtime32_end_time: int
    language_preference: _containers.RepeatedScalarFieldContainer[int]
    filter_event_type: _containers.RepeatedScalarFieldContainer[_steammessages_base_pb2.EProtoClanEventType]
    filter_to_appid: bool
    app_list: _containers.RepeatedCompositeFieldContainer[CAppPriority]
    count_after: int
    count_before: int
    def __init__(self, count: _Optional[int] = ..., offset: _Optional[int] = ..., rtime32_start_time: _Optional[int] = ..., rtime32_end_time: _Optional[int] = ..., language_preference: _Optional[_Iterable[int]] = ..., filter_event_type: _Optional[_Iterable[_Union[_steammessages_base_pb2.EProtoClanEventType, str]]] = ..., filter_to_appid: bool = ..., app_list: _Optional[_Iterable[_Union[CAppPriority, _Mapping]]] = ..., count_after: _Optional[int] = ..., count_before: _Optional[int] = ...) -> None: ...

class CCommunity_GetUserPartnerEventNews_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[_steammessages_base_pb2.CClanMatchEventByRange]
    def __init__(self, results: _Optional[_Iterable[_Union[_steammessages_base_pb2.CClanMatchEventByRange, _Mapping]]] = ...) -> None: ...

class CCommunity_GetBestEventsForUser_Request(_message.Message):
    __slots__ = ("include_steam_blog", "filter_to_played_within_days", "include_only_game_updates")
    INCLUDE_STEAM_BLOG_FIELD_NUMBER: _ClassVar[int]
    FILTER_TO_PLAYED_WITHIN_DAYS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ONLY_GAME_UPDATES_FIELD_NUMBER: _ClassVar[int]
    include_steam_blog: bool
    filter_to_played_within_days: int
    include_only_game_updates: bool
    def __init__(self, include_steam_blog: bool = ..., filter_to_played_within_days: _Optional[int] = ..., include_only_game_updates: bool = ...) -> None: ...

class CCommunity_PartnerEventResult(_message.Message):
    __slots__ = ("clanid", "event_gid", "announcement_gid", "appid", "possible_takeover", "rtime32_last_modified", "user_app_priority")
    CLANID_FIELD_NUMBER: _ClassVar[int]
    EVENT_GID_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_GID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_TAKEOVER_FIELD_NUMBER: _ClassVar[int]
    RTIME32_LAST_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    USER_APP_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    clanid: int
    event_gid: int
    announcement_gid: int
    appid: int
    possible_takeover: bool
    rtime32_last_modified: int
    user_app_priority: int
    def __init__(self, clanid: _Optional[int] = ..., event_gid: _Optional[int] = ..., announcement_gid: _Optional[int] = ..., appid: _Optional[int] = ..., possible_takeover: bool = ..., rtime32_last_modified: _Optional[int] = ..., user_app_priority: _Optional[int] = ...) -> None: ...

class CCommunity_GetBestEventsForUser_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CCommunity_PartnerEventResult]
    def __init__(self, results: _Optional[_Iterable[_Union[CCommunity_PartnerEventResult, _Mapping]]] = ...) -> None: ...

class CCommunity_MarkPartnerEventsForUser_Request(_message.Message):
    __slots__ = ("markings",)
    class PartnerEventMarking(_message.Message):
        __slots__ = ("clanid", "event_gid", "display_location", "mark_shown", "mark_read")
        CLANID_FIELD_NUMBER: _ClassVar[int]
        EVENT_GID_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_LOCATION_FIELD_NUMBER: _ClassVar[int]
        MARK_SHOWN_FIELD_NUMBER: _ClassVar[int]
        MARK_READ_FIELD_NUMBER: _ClassVar[int]
        clanid: int
        event_gid: int
        display_location: EPartnerEventDisplayLocation
        mark_shown: bool
        mark_read: bool
        def __init__(self, clanid: _Optional[int] = ..., event_gid: _Optional[int] = ..., display_location: _Optional[_Union[EPartnerEventDisplayLocation, str]] = ..., mark_shown: bool = ..., mark_read: bool = ...) -> None: ...
    MARKINGS_FIELD_NUMBER: _ClassVar[int]
    markings: _containers.RepeatedCompositeFieldContainer[CCommunity_MarkPartnerEventsForUser_Request.PartnerEventMarking]
    def __init__(self, markings: _Optional[_Iterable[_Union[CCommunity_MarkPartnerEventsForUser_Request.PartnerEventMarking, _Mapping]]] = ...) -> None: ...

class CCommunity_MarkPartnerEventsForUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_GetUserPartnerEventViewStatus_Request(_message.Message):
    __slots__ = ("event_gids", "include_read_events_only")
    EVENT_GIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_READ_EVENTS_ONLY_FIELD_NUMBER: _ClassVar[int]
    event_gids: _containers.RepeatedScalarFieldContainer[int]
    include_read_events_only: bool
    def __init__(self, event_gids: _Optional[_Iterable[int]] = ..., include_read_events_only: bool = ...) -> None: ...

class CCommunity_GetUserPartnerEventViewStatus_Response(_message.Message):
    __slots__ = ("events",)
    class PartnerEvent(_message.Message):
        __slots__ = ("event_gid", "last_shown_time", "last_read_time", "clan_account_id")
        EVENT_GID_FIELD_NUMBER: _ClassVar[int]
        LAST_SHOWN_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_READ_TIME_FIELD_NUMBER: _ClassVar[int]
        CLAN_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
        event_gid: int
        last_shown_time: int
        last_read_time: int
        clan_account_id: int
        def __init__(self, event_gid: _Optional[int] = ..., last_shown_time: _Optional[int] = ..., last_read_time: _Optional[int] = ..., clan_account_id: _Optional[int] = ...) -> None: ...
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[CCommunity_GetUserPartnerEventViewStatus_Response.PartnerEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[CCommunity_GetUserPartnerEventViewStatus_Response.PartnerEvent, _Mapping]]] = ...) -> None: ...

class CCommunity_PartnerEventsShowMoreForApp_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CCommunity_PartnerEventsShowMoreForApp_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_PartnerEventsShowLessForApp_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CCommunity_PartnerEventsShowLessForApp_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_ClearUserPartnerEventsAppPriorities_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_ClearUserPartnerEventsAppPriorities_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_GetUserPartnerEventsAppPriorities_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CCommunity_PartnerEventsAppPriority(_message.Message):
    __slots__ = ("appid", "user_app_priority")
    APPID_FIELD_NUMBER: _ClassVar[int]
    USER_APP_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    appid: int
    user_app_priority: int
    def __init__(self, appid: _Optional[int] = ..., user_app_priority: _Optional[int] = ...) -> None: ...

class CCommunity_GetUserPartnerEventsAppPriorities_Response(_message.Message):
    __slots__ = ("priorities",)
    PRIORITIES_FIELD_NUMBER: _ClassVar[int]
    priorities: _containers.RepeatedCompositeFieldContainer[CCommunity_PartnerEventsAppPriority]
    def __init__(self, priorities: _Optional[_Iterable[_Union[CCommunity_PartnerEventsAppPriority, _Mapping]]] = ...) -> None: ...

class CCommunity_ClearSinglePartnerEventsAppPriority_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CCommunity_ClearSinglePartnerEventsAppPriority_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Community(_service.service): ...

class Community_Stub(Community): ...
