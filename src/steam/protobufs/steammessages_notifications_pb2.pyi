import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ESteamNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESteamNotificationType_Invalid: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_Test: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_Gift: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_Comment: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_Item: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_FriendInvite: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_MajorSale: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_PreloadAvailable: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_Wishlist: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_TradeOffer: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_General: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_HelpRequest: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_AsyncGame: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ChatMsg: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ModeratorMsg: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ParentalFeatureAccessRequest: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_FamilyInvite: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_FamilyPurchaseRequest: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ParentalPlaytimeRequest: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_FamilyPurchaseRequestResponse: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ParentalFeatureAccessResponse: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ParentalPlaytimeResponse: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_RequestedGameAdded: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_SendToPhone: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_ClipDownloaded: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_2FAPrompt: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_MobileConfirmation: _ClassVar[ESteamNotificationType]
    k_ESteamNotificationType_PartnerEvent: _ClassVar[ESteamNotificationType]
k_ESteamNotificationType_Invalid: ESteamNotificationType
k_ESteamNotificationType_Test: ESteamNotificationType
k_ESteamNotificationType_Gift: ESteamNotificationType
k_ESteamNotificationType_Comment: ESteamNotificationType
k_ESteamNotificationType_Item: ESteamNotificationType
k_ESteamNotificationType_FriendInvite: ESteamNotificationType
k_ESteamNotificationType_MajorSale: ESteamNotificationType
k_ESteamNotificationType_PreloadAvailable: ESteamNotificationType
k_ESteamNotificationType_Wishlist: ESteamNotificationType
k_ESteamNotificationType_TradeOffer: ESteamNotificationType
k_ESteamNotificationType_General: ESteamNotificationType
k_ESteamNotificationType_HelpRequest: ESteamNotificationType
k_ESteamNotificationType_AsyncGame: ESteamNotificationType
k_ESteamNotificationType_ChatMsg: ESteamNotificationType
k_ESteamNotificationType_ModeratorMsg: ESteamNotificationType
k_ESteamNotificationType_ParentalFeatureAccessRequest: ESteamNotificationType
k_ESteamNotificationType_FamilyInvite: ESteamNotificationType
k_ESteamNotificationType_FamilyPurchaseRequest: ESteamNotificationType
k_ESteamNotificationType_ParentalPlaytimeRequest: ESteamNotificationType
k_ESteamNotificationType_FamilyPurchaseRequestResponse: ESteamNotificationType
k_ESteamNotificationType_ParentalFeatureAccessResponse: ESteamNotificationType
k_ESteamNotificationType_ParentalPlaytimeResponse: ESteamNotificationType
k_ESteamNotificationType_RequestedGameAdded: ESteamNotificationType
k_ESteamNotificationType_SendToPhone: ESteamNotificationType
k_ESteamNotificationType_ClipDownloaded: ESteamNotificationType
k_ESteamNotificationType_2FAPrompt: ESteamNotificationType
k_ESteamNotificationType_MobileConfirmation: ESteamNotificationType
k_ESteamNotificationType_PartnerEvent: ESteamNotificationType

class SteamNotificationData(_message.Message):
    __slots__ = ("notification_id", "notification_targets", "notification_type", "body_data", "read", "timestamp", "hidden", "expiry", "viewed")
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    BODY_DATA_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    VIEWED_FIELD_NUMBER: _ClassVar[int]
    notification_id: int
    notification_targets: int
    notification_type: ESteamNotificationType
    body_data: str
    read: bool
    timestamp: int
    hidden: bool
    expiry: int
    viewed: int
    def __init__(self, notification_id: _Optional[int] = ..., notification_targets: _Optional[int] = ..., notification_type: _Optional[_Union[ESteamNotificationType, str]] = ..., body_data: _Optional[str] = ..., read: bool = ..., timestamp: _Optional[int] = ..., hidden: bool = ..., expiry: _Optional[int] = ..., viewed: _Optional[int] = ...) -> None: ...

class CSteamNotification_NotificationsReceived_Notification(_message.Message):
    __slots__ = ("notifications", "pending_gift_count", "pending_friend_count", "pending_family_invite_count")
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    PENDING_GIFT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_FRIEND_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_FAMILY_INVITE_COUNT_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[SteamNotificationData]
    pending_gift_count: int
    pending_friend_count: int
    pending_family_invite_count: int
    def __init__(self, notifications: _Optional[_Iterable[_Union[SteamNotificationData, _Mapping]]] = ..., pending_gift_count: _Optional[int] = ..., pending_friend_count: _Optional[int] = ..., pending_family_invite_count: _Optional[int] = ...) -> None: ...

class SteamNotificationPreference(_message.Message):
    __slots__ = ("notification_type", "notification_targets")
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TARGETS_FIELD_NUMBER: _ClassVar[int]
    notification_type: ESteamNotificationType
    notification_targets: int
    def __init__(self, notification_type: _Optional[_Union[ESteamNotificationType, str]] = ..., notification_targets: _Optional[int] = ...) -> None: ...

class CSteamNotification_PreferencesUpdated_Notification(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: _containers.RepeatedCompositeFieldContainer[SteamNotificationPreference]
    def __init__(self, preferences: _Optional[_Iterable[_Union[SteamNotificationPreference, _Mapping]]] = ...) -> None: ...

class SteamNotificationClient(_service.service): ...

class SteamNotificationClient_Stub(SteamNotificationClient): ...
