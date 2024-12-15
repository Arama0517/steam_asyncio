import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import steammessages_storebrowse_pb2 as _steammessages_storebrowse_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EMarketingMessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMarketingMessageInvalid: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageNowAvailable: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageWeekendDeal: _ClassVar[EMarketingMessageType]
    k_EMarketingMessagePrePurchase: _ClassVar[EMarketingMessageType]
    k_EMarketingMessagePlayNow: _ClassVar[EMarketingMessageType]
    k_EMarketingMessagePreloadNow: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageGeneral: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageDemoQuit: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageGifting: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageEJsKorner: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageUpdate: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageMidweekDeal: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageDailyDeal: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageNewDLC: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageFreeWeekend: _ClassVar[EMarketingMessageType]
    k_EMarketingMessageSalePages: _ClassVar[EMarketingMessageType]
    k_EMarketingMessagePlaytestAvailable: _ClassVar[EMarketingMessageType]

class EMarketingMessageVisibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMarketingMessageVisibleBeta: _ClassVar[EMarketingMessageVisibility]
    k_EMarketingMessageVisiblePublic: _ClassVar[EMarketingMessageVisibility]
    k_EMarketingMessageVisibleApprovedForPublish: _ClassVar[EMarketingMessageVisibility]

class EMarketingMessageAssociationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMarketingMessageNoAssociation: _ClassVar[EMarketingMessageAssociationType]
    k_EMarketingMessageAppAssociation: _ClassVar[EMarketingMessageAssociationType]
    k_EMarketingMessageSubscriptionAssociation: _ClassVar[EMarketingMessageAssociationType]
    k_EMarketingMessagePublisherAssociation: _ClassVar[EMarketingMessageAssociationType]
    k_EMarketingMessageGenreAssociation: _ClassVar[EMarketingMessageAssociationType]
    k_EMarketingMessageBundleAssociation: _ClassVar[EMarketingMessageAssociationType]

class EMarketingMessageTemplateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMarketingMessageTemplate_Unknown: _ClassVar[EMarketingMessageTemplateType]
    k_EMarketingMessageTemplate_Image: _ClassVar[EMarketingMessageTemplateType]
    k_EMarketingMessageTemplate_Animated: _ClassVar[EMarketingMessageTemplateType]
    k_EMarketingMessageTemplate_Featured_Video: _ClassVar[EMarketingMessageTemplateType]
    k_EMarketingMessageTemplate_DLC_Override: _ClassVar[EMarketingMessageTemplateType]
    k_EMarketingMessageTemplate_Replay: _ClassVar[EMarketingMessageTemplateType]
    k_EMarketingMessageTemplate_MAX: _ClassVar[EMarketingMessageTemplateType]

class EMarketingMessageLookupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMarketingMessageLookupInvalid: _ClassVar[EMarketingMessageLookupType]
    k_EMarketingMessageLookupByGID: _ClassVar[EMarketingMessageLookupType]
    k_EMarketingMessageLookupActive: _ClassVar[EMarketingMessageLookupType]
    k_EMarketingMessageLookupByTitleWithType: _ClassVar[EMarketingMessageLookupType]
    k_EMarketingMessageLookupByGIDList: _ClassVar[EMarketingMessageLookupType]
k_EMarketingMessageInvalid: EMarketingMessageType
k_EMarketingMessageNowAvailable: EMarketingMessageType
k_EMarketingMessageWeekendDeal: EMarketingMessageType
k_EMarketingMessagePrePurchase: EMarketingMessageType
k_EMarketingMessagePlayNow: EMarketingMessageType
k_EMarketingMessagePreloadNow: EMarketingMessageType
k_EMarketingMessageGeneral: EMarketingMessageType
k_EMarketingMessageDemoQuit: EMarketingMessageType
k_EMarketingMessageGifting: EMarketingMessageType
k_EMarketingMessageEJsKorner: EMarketingMessageType
k_EMarketingMessageUpdate: EMarketingMessageType
k_EMarketingMessageMidweekDeal: EMarketingMessageType
k_EMarketingMessageDailyDeal: EMarketingMessageType
k_EMarketingMessageNewDLC: EMarketingMessageType
k_EMarketingMessageFreeWeekend: EMarketingMessageType
k_EMarketingMessageSalePages: EMarketingMessageType
k_EMarketingMessagePlaytestAvailable: EMarketingMessageType
k_EMarketingMessageVisibleBeta: EMarketingMessageVisibility
k_EMarketingMessageVisiblePublic: EMarketingMessageVisibility
k_EMarketingMessageVisibleApprovedForPublish: EMarketingMessageVisibility
k_EMarketingMessageNoAssociation: EMarketingMessageAssociationType
k_EMarketingMessageAppAssociation: EMarketingMessageAssociationType
k_EMarketingMessageSubscriptionAssociation: EMarketingMessageAssociationType
k_EMarketingMessagePublisherAssociation: EMarketingMessageAssociationType
k_EMarketingMessageGenreAssociation: EMarketingMessageAssociationType
k_EMarketingMessageBundleAssociation: EMarketingMessageAssociationType
k_EMarketingMessageTemplate_Unknown: EMarketingMessageTemplateType
k_EMarketingMessageTemplate_Image: EMarketingMessageTemplateType
k_EMarketingMessageTemplate_Animated: EMarketingMessageTemplateType
k_EMarketingMessageTemplate_Featured_Video: EMarketingMessageTemplateType
k_EMarketingMessageTemplate_DLC_Override: EMarketingMessageTemplateType
k_EMarketingMessageTemplate_Replay: EMarketingMessageTemplateType
k_EMarketingMessageTemplate_MAX: EMarketingMessageTemplateType
k_EMarketingMessageLookupInvalid: EMarketingMessageLookupType
k_EMarketingMessageLookupByGID: EMarketingMessageLookupType
k_EMarketingMessageLookupActive: EMarketingMessageLookupType
k_EMarketingMessageLookupByTitleWithType: EMarketingMessageLookupType
k_EMarketingMessageLookupByGIDList: EMarketingMessageLookupType

class CMarketingMessages_GetActiveMarketingMessages_Request(_message.Message):
    __slots__ = ("country", "anonymous_user")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ANONYMOUS_USER_FIELD_NUMBER: _ClassVar[int]
    country: str
    anonymous_user: bool
    def __init__(self, country: _Optional[str] = ..., anonymous_user: bool = ...) -> None: ...

class CMarketingMessageProto(_message.Message):
    __slots__ = ("gid", "title", "type", "visibility", "priority", "association_type", "associated_id", "associated_name", "start_date", "end_date", "country_allow", "country_deny", "ownership_restrictions_overridden", "must_own_appid", "must_not_own_appid", "must_own_packageid", "must_not_own_packageid", "must_have_launched_appid", "additional_restrictions", "template_type", "template_vars", "flags", "creator_name", "template_vars_json", "additional_restrictions_json")
    GID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_NAME_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ALLOW_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_DENY_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_RESTRICTIONS_OVERRIDDEN_FIELD_NUMBER: _ClassVar[int]
    MUST_OWN_APPID_FIELD_NUMBER: _ClassVar[int]
    MUST_NOT_OWN_APPID_FIELD_NUMBER: _ClassVar[int]
    MUST_OWN_PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    MUST_NOT_OWN_PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    MUST_HAVE_LAUNCHED_APPID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VARS_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VARS_JSON_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_RESTRICTIONS_JSON_FIELD_NUMBER: _ClassVar[int]
    gid: int
    title: str
    type: EMarketingMessageType
    visibility: EMarketingMessageVisibility
    priority: int
    association_type: EMarketingMessageAssociationType
    associated_id: int
    associated_name: str
    start_date: int
    end_date: int
    country_allow: str
    country_deny: str
    ownership_restrictions_overridden: bool
    must_own_appid: int
    must_not_own_appid: int
    must_own_packageid: int
    must_not_own_packageid: int
    must_have_launched_appid: int
    additional_restrictions: str
    template_type: str
    template_vars: str
    flags: int
    creator_name: str
    template_vars_json: str
    additional_restrictions_json: str
    def __init__(self, gid: _Optional[int] = ..., title: _Optional[str] = ..., type: _Optional[_Union[EMarketingMessageType, str]] = ..., visibility: _Optional[_Union[EMarketingMessageVisibility, str]] = ..., priority: _Optional[int] = ..., association_type: _Optional[_Union[EMarketingMessageAssociationType, str]] = ..., associated_id: _Optional[int] = ..., associated_name: _Optional[str] = ..., start_date: _Optional[int] = ..., end_date: _Optional[int] = ..., country_allow: _Optional[str] = ..., country_deny: _Optional[str] = ..., ownership_restrictions_overridden: bool = ..., must_own_appid: _Optional[int] = ..., must_not_own_appid: _Optional[int] = ..., must_own_packageid: _Optional[int] = ..., must_not_own_packageid: _Optional[int] = ..., must_have_launched_appid: _Optional[int] = ..., additional_restrictions: _Optional[str] = ..., template_type: _Optional[str] = ..., template_vars: _Optional[str] = ..., flags: _Optional[int] = ..., creator_name: _Optional[str] = ..., template_vars_json: _Optional[str] = ..., additional_restrictions_json: _Optional[str] = ...) -> None: ...

class CMarketingMessages_GetActiveMarketingMessages_Response(_message.Message):
    __slots__ = ("messages", "time_next_message_age")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TIME_NEXT_MESSAGE_AGE_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CMarketingMessageProto]
    time_next_message_age: int
    def __init__(self, messages: _Optional[_Iterable[_Union[CMarketingMessageProto, _Mapping]]] = ..., time_next_message_age: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetPastMarketingMessages_Request(_message.Message):
    __slots__ = ("start_past_days", "upto_past_days")
    START_PAST_DAYS_FIELD_NUMBER: _ClassVar[int]
    UPTO_PAST_DAYS_FIELD_NUMBER: _ClassVar[int]
    start_past_days: int
    upto_past_days: int
    def __init__(self, start_past_days: _Optional[int] = ..., upto_past_days: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetPastMarketingMessages_Response(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CMarketingMessageProto]
    def __init__(self, messages: _Optional[_Iterable[_Union[CMarketingMessageProto, _Mapping]]] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessagesForUser_Request(_message.Message):
    __slots__ = ("include_seen_messages", "country_code", "elanguage", "operating_system", "client_package_version", "context", "data_request")
    INCLUDE_SEEN_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ELANGUAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    include_seen_messages: bool
    country_code: str
    elanguage: int
    operating_system: int
    client_package_version: int
    context: _steammessages_storebrowse_pb2.StoreBrowseContext
    data_request: _steammessages_storebrowse_pb2.StoreBrowseItemDataRequest
    def __init__(self, include_seen_messages: bool = ..., country_code: _Optional[str] = ..., elanguage: _Optional[int] = ..., operating_system: _Optional[int] = ..., client_package_version: _Optional[int] = ..., context: _Optional[_Union[_steammessages_storebrowse_pb2.StoreBrowseContext, _Mapping]] = ..., data_request: _Optional[_Union[_steammessages_storebrowse_pb2.StoreBrowseItemDataRequest, _Mapping]] = ...) -> None: ...

class CDisplayMarketingMessage(_message.Message):
    __slots__ = ("gid", "title", "type", "associated_item_id", "associated_item", "associated_name", "template_type", "template_vars_json")
    GID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_ITEM_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_VARS_JSON_FIELD_NUMBER: _ClassVar[int]
    gid: int
    title: str
    type: EMarketingMessageType
    associated_item_id: _steammessages_storebrowse_pb2.StoreItemID
    associated_item: _steammessages_storebrowse_pb2.StoreItem
    associated_name: str
    template_type: str
    template_vars_json: str
    def __init__(self, gid: _Optional[int] = ..., title: _Optional[str] = ..., type: _Optional[_Union[EMarketingMessageType, str]] = ..., associated_item_id: _Optional[_Union[_steammessages_storebrowse_pb2.StoreItemID, _Mapping]] = ..., associated_item: _Optional[_Union[_steammessages_storebrowse_pb2.StoreItem, _Mapping]] = ..., associated_name: _Optional[str] = ..., template_type: _Optional[str] = ..., template_vars_json: _Optional[str] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessagesForUser_Response(_message.Message):
    __slots__ = ("messages",)
    class MarketingMessageForUser(_message.Message):
        __slots__ = ("already_seen", "message")
        ALREADY_SEEN_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        already_seen: bool
        message: CDisplayMarketingMessage
        def __init__(self, already_seen: bool = ..., message: _Optional[_Union[CDisplayMarketingMessage, _Mapping]] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CMarketingMessages_GetMarketingMessagesForUser_Response.MarketingMessageForUser]
    def __init__(self, messages: _Optional[_Iterable[_Union[CMarketingMessages_GetMarketingMessagesForUser_Response.MarketingMessageForUser, _Mapping]]] = ...) -> None: ...

class CMarketingMessages_DoesUserHavePendingMarketingMessages_Request(_message.Message):
    __slots__ = ("country_code", "elanguage", "operating_system", "client_package_version")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ELANGUAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PACKAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    elanguage: int
    operating_system: int
    client_package_version: int
    def __init__(self, country_code: _Optional[str] = ..., elanguage: _Optional[int] = ..., operating_system: _Optional[int] = ..., client_package_version: _Optional[int] = ...) -> None: ...

class CMarketingMessages_DoesUserHavePendingMarketingMessages_Response(_message.Message):
    __slots__ = ("has_pending_messages", "pending_message_count")
    HAS_PENDING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PENDING_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    has_pending_messages: bool
    pending_message_count: int
    def __init__(self, has_pending_messages: bool = ..., pending_message_count: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetDisplayMarketingMessage_Request(_message.Message):
    __slots__ = ("gid", "context", "data_request")
    GID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    gid: int
    context: _steammessages_storebrowse_pb2.StoreBrowseContext
    data_request: _steammessages_storebrowse_pb2.StoreBrowseItemDataRequest
    def __init__(self, gid: _Optional[int] = ..., context: _Optional[_Union[_steammessages_storebrowse_pb2.StoreBrowseContext, _Mapping]] = ..., data_request: _Optional[_Union[_steammessages_storebrowse_pb2.StoreBrowseItemDataRequest, _Mapping]] = ...) -> None: ...

class CMarketingMessages_GetDisplayMarketingMessage_Response(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: CDisplayMarketingMessage
    def __init__(self, message: _Optional[_Union[CDisplayMarketingMessage, _Mapping]] = ...) -> None: ...

class CMarketingMessages_MarkMessageSeen_Notification(_message.Message):
    __slots__ = ("gid", "display_index", "template_type")
    GID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    gid: int
    display_index: int
    template_type: EMarketingMessageTemplateType
    def __init__(self, gid: _Optional[int] = ..., display_index: _Optional[int] = ..., template_type: _Optional[_Union[EMarketingMessageTemplateType, str]] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessage_Request(_message.Message):
    __slots__ = ("gid",)
    GID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    def __init__(self, gid: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessage_Response(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: CMarketingMessageProto
    def __init__(self, message: _Optional[_Union[CMarketingMessageProto, _Mapping]] = ...) -> None: ...

class CMarketingMessages_CreateMarketingMessage_Request(_message.Message):
    __slots__ = ("message", "from_json")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_JSON_FIELD_NUMBER: _ClassVar[int]
    message: CMarketingMessageProto
    from_json: bool
    def __init__(self, message: _Optional[_Union[CMarketingMessageProto, _Mapping]] = ..., from_json: bool = ...) -> None: ...

class CMarketingMessages_CreateMarketingMessage_Response(_message.Message):
    __slots__ = ("gid",)
    GID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    def __init__(self, gid: _Optional[int] = ...) -> None: ...

class CMarketingMessages_UpdateMarketingMessage_Request(_message.Message):
    __slots__ = ("gid", "message", "from_json")
    GID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FROM_JSON_FIELD_NUMBER: _ClassVar[int]
    gid: int
    message: CMarketingMessageProto
    from_json: bool
    def __init__(self, gid: _Optional[int] = ..., message: _Optional[_Union[CMarketingMessageProto, _Mapping]] = ..., from_json: bool = ...) -> None: ...

class CMarketingMessages_UpdateMarketingMessage_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMarketingMessages_DeleteMarketingMessage_Request(_message.Message):
    __slots__ = ("gid",)
    GID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    def __init__(self, gid: _Optional[int] = ...) -> None: ...

class CMarketingMessages_DeleteMarketingMessage_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMarketingMessages_FindMarketingMessages_Request(_message.Message):
    __slots__ = ("lookup_type", "gid", "message_type", "gidlist", "title")
    LOOKUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    GID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GIDLIST_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    lookup_type: EMarketingMessageLookupType
    gid: int
    message_type: EMarketingMessageType
    gidlist: _containers.RepeatedScalarFieldContainer[int]
    title: str
    def __init__(self, lookup_type: _Optional[_Union[EMarketingMessageLookupType, str]] = ..., gid: _Optional[int] = ..., message_type: _Optional[_Union[EMarketingMessageType, str]] = ..., gidlist: _Optional[_Iterable[int]] = ..., title: _Optional[str] = ...) -> None: ...

class CMarketingMessages_FindMarketingMessages_Response(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CMarketingMessageProto]
    def __init__(self, messages: _Optional[_Iterable[_Union[CMarketingMessageProto, _Mapping]]] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessageViewerStats_Request(_message.Message):
    __slots__ = ("gid",)
    GID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    def __init__(self, gid: _Optional[int] = ...) -> None: ...

class CMarketingMessageHourlyStats(_message.Message):
    __slots__ = ("rt_time_hour", "seen_count", "template_type", "display_index")
    RT_TIME_HOUR_FIELD_NUMBER: _ClassVar[int]
    SEEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_INDEX_FIELD_NUMBER: _ClassVar[int]
    rt_time_hour: int
    seen_count: int
    template_type: EMarketingMessageTemplateType
    display_index: int
    def __init__(self, rt_time_hour: _Optional[int] = ..., seen_count: _Optional[int] = ..., template_type: _Optional[_Union[EMarketingMessageTemplateType, str]] = ..., display_index: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessageViewerStats_Response(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[CMarketingMessageHourlyStats]
    def __init__(self, stats: _Optional[_Iterable[_Union[CMarketingMessageHourlyStats, _Mapping]]] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessagesViewerRangeStats_Request(_message.Message):
    __slots__ = ("rt_start_time", "rt_end_time")
    RT_START_TIME_FIELD_NUMBER: _ClassVar[int]
    RT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    rt_start_time: int
    rt_end_time: int
    def __init__(self, rt_start_time: _Optional[int] = ..., rt_end_time: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetMarketingMessagesViewerRangeStats_Response(_message.Message):
    __slots__ = ("stats",)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[CMarketingMessageHourlyStats]
    def __init__(self, stats: _Optional[_Iterable[_Union[CMarketingMessageHourlyStats, _Mapping]]] = ...) -> None: ...

class CMarketingMessages_GetPartnerReadyToPublishMessages_Request(_message.Message):
    __slots__ = ("partnerid",)
    PARTNERID_FIELD_NUMBER: _ClassVar[int]
    partnerid: int
    def __init__(self, partnerid: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetPartnerReadyToPublishMessages_Response(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CDisplayMarketingMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[CDisplayMarketingMessage, _Mapping]]] = ...) -> None: ...

class CMarketingMessages_PartnerPublishMessage_Request(_message.Message):
    __slots__ = ("gid", "partnerid")
    GID_FIELD_NUMBER: _ClassVar[int]
    PARTNERID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    partnerid: int
    def __init__(self, gid: _Optional[int] = ..., partnerid: _Optional[int] = ...) -> None: ...

class CMarketingMessages_PartnerPublishMessage_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMarketingMessages_GetPartnerMessagePreview_Request(_message.Message):
    __slots__ = ("gid", "partnerid")
    GID_FIELD_NUMBER: _ClassVar[int]
    PARTNERID_FIELD_NUMBER: _ClassVar[int]
    gid: int
    partnerid: int
    def __init__(self, gid: _Optional[int] = ..., partnerid: _Optional[int] = ...) -> None: ...

class CMarketingMessages_GetPartnerMessagePreview_Response(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: CMarketingMessageProto
    def __init__(self, message: _Optional[_Union[CMarketingMessageProto, _Mapping]] = ...) -> None: ...

class CMarketingMessage_GetMarketingMessagesForPartner_Request(_message.Message):
    __slots__ = ("partnerid",)
    PARTNERID_FIELD_NUMBER: _ClassVar[int]
    partnerid: int
    def __init__(self, partnerid: _Optional[int] = ...) -> None: ...

class CMarketingMessage_GetMarketingMessagesForPartner_Response(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CMarketingMessageProto]
    def __init__(self, messages: _Optional[_Iterable[_Union[CMarketingMessageProto, _Mapping]]] = ...) -> None: ...

class CMarketingMessage_GetMarketingMessagesForApps_Request(_message.Message):
    __slots__ = ("appids",)
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMarketingMessage_GetMarketingMessagesForApps_Response(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[CMarketingMessageProto]
    def __init__(self, messages: _Optional[_Iterable[_Union[CMarketingMessageProto, _Mapping]]] = ...) -> None: ...

class MarketingMessages(_service.service): ...

class MarketingMessages_Stub(MarketingMessages): ...
