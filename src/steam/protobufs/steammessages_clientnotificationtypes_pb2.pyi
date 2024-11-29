from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EClientNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EClientNotificationType_Invalid: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_DownloadCompleted: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FriendInvite: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FriendInGame: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FriendOnline: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_Achievement: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_LowBattery: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_SystemUpdate: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FriendMessage: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GroupChatMessage: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FriendInviteRollup: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FamilySharingDeviceAuthorizationChanged: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FamilySharingStopPlaying: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FamilySharingLibraryAvailable: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_Screenshot: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_CloudSyncFailure: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_CloudSyncConflict: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_IncomingVoiceChat: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ClaimSteamDeckRewards: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GiftReceived: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ItemAnnouncement: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_HardwareSurvey: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_LowDiskSpace: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_BatteryTemperature: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_DockUnsupportedFirmware: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_PeerContentUpload: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_CannotReadControllerGuideButton: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_Comment: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_Wishlist: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_TradeOffer: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_AsyncGame: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_General: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_HelpRequest: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_OverlaySplashScreen: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_BroadcastAvailableToWatch: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_TimedTrialRemaining: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_LoginRefresh: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_MajorSale: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_TimerExpired: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ModeratorMsg: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_SteamInputActionSetChanged: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_RemoteClientConnection: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_RemoteClientStartStream: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_StreamingClientConnection: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FamilyInvite: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_PlaytimeWarning: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FamilyPurchaseRequest: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_FamilyPurchaseRequestResponse: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ParentalFeatureRequest: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ParentalPlaytimeRequest: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GameRecordingError: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ParentalFeatureResponse: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ParentalPlaytimeResponse: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_RequestedGameAdded: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_ClipDownloaded: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GameRecordingStart: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GameRecordingStop: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GameRecordingUserMarkerAdded: _ClassVar[EClientNotificationType]
    k_EClientNotificationType_GameRecordingInstantClip: _ClassVar[EClientNotificationType]

class ESystemUpdateNotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESystemUpdateNotificationType_Invalid: _ClassVar[ESystemUpdateNotificationType]
    k_ESystemUpdateNotificationType_Available: _ClassVar[ESystemUpdateNotificationType]
    k_ESystemUpdateNotificationType_NeedsRestart: _ClassVar[ESystemUpdateNotificationType]

class EGameRecordingErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EGameRecordingErrorGeneral: _ClassVar[EGameRecordingErrorType]
    k_EGameRecordingErrorLowDiskSpace: _ClassVar[EGameRecordingErrorType]
k_EClientNotificationType_Invalid: EClientNotificationType
k_EClientNotificationType_DownloadCompleted: EClientNotificationType
k_EClientNotificationType_FriendInvite: EClientNotificationType
k_EClientNotificationType_FriendInGame: EClientNotificationType
k_EClientNotificationType_FriendOnline: EClientNotificationType
k_EClientNotificationType_Achievement: EClientNotificationType
k_EClientNotificationType_LowBattery: EClientNotificationType
k_EClientNotificationType_SystemUpdate: EClientNotificationType
k_EClientNotificationType_FriendMessage: EClientNotificationType
k_EClientNotificationType_GroupChatMessage: EClientNotificationType
k_EClientNotificationType_FriendInviteRollup: EClientNotificationType
k_EClientNotificationType_FamilySharingDeviceAuthorizationChanged: EClientNotificationType
k_EClientNotificationType_FamilySharingStopPlaying: EClientNotificationType
k_EClientNotificationType_FamilySharingLibraryAvailable: EClientNotificationType
k_EClientNotificationType_Screenshot: EClientNotificationType
k_EClientNotificationType_CloudSyncFailure: EClientNotificationType
k_EClientNotificationType_CloudSyncConflict: EClientNotificationType
k_EClientNotificationType_IncomingVoiceChat: EClientNotificationType
k_EClientNotificationType_ClaimSteamDeckRewards: EClientNotificationType
k_EClientNotificationType_GiftReceived: EClientNotificationType
k_EClientNotificationType_ItemAnnouncement: EClientNotificationType
k_EClientNotificationType_HardwareSurvey: EClientNotificationType
k_EClientNotificationType_LowDiskSpace: EClientNotificationType
k_EClientNotificationType_BatteryTemperature: EClientNotificationType
k_EClientNotificationType_DockUnsupportedFirmware: EClientNotificationType
k_EClientNotificationType_PeerContentUpload: EClientNotificationType
k_EClientNotificationType_CannotReadControllerGuideButton: EClientNotificationType
k_EClientNotificationType_Comment: EClientNotificationType
k_EClientNotificationType_Wishlist: EClientNotificationType
k_EClientNotificationType_TradeOffer: EClientNotificationType
k_EClientNotificationType_AsyncGame: EClientNotificationType
k_EClientNotificationType_General: EClientNotificationType
k_EClientNotificationType_HelpRequest: EClientNotificationType
k_EClientNotificationType_OverlaySplashScreen: EClientNotificationType
k_EClientNotificationType_BroadcastAvailableToWatch: EClientNotificationType
k_EClientNotificationType_TimedTrialRemaining: EClientNotificationType
k_EClientNotificationType_LoginRefresh: EClientNotificationType
k_EClientNotificationType_MajorSale: EClientNotificationType
k_EClientNotificationType_TimerExpired: EClientNotificationType
k_EClientNotificationType_ModeratorMsg: EClientNotificationType
k_EClientNotificationType_SteamInputActionSetChanged: EClientNotificationType
k_EClientNotificationType_RemoteClientConnection: EClientNotificationType
k_EClientNotificationType_RemoteClientStartStream: EClientNotificationType
k_EClientNotificationType_StreamingClientConnection: EClientNotificationType
k_EClientNotificationType_FamilyInvite: EClientNotificationType
k_EClientNotificationType_PlaytimeWarning: EClientNotificationType
k_EClientNotificationType_FamilyPurchaseRequest: EClientNotificationType
k_EClientNotificationType_FamilyPurchaseRequestResponse: EClientNotificationType
k_EClientNotificationType_ParentalFeatureRequest: EClientNotificationType
k_EClientNotificationType_ParentalPlaytimeRequest: EClientNotificationType
k_EClientNotificationType_GameRecordingError: EClientNotificationType
k_EClientNotificationType_ParentalFeatureResponse: EClientNotificationType
k_EClientNotificationType_ParentalPlaytimeResponse: EClientNotificationType
k_EClientNotificationType_RequestedGameAdded: EClientNotificationType
k_EClientNotificationType_ClipDownloaded: EClientNotificationType
k_EClientNotificationType_GameRecordingStart: EClientNotificationType
k_EClientNotificationType_GameRecordingStop: EClientNotificationType
k_EClientNotificationType_GameRecordingUserMarkerAdded: EClientNotificationType
k_EClientNotificationType_GameRecordingInstantClip: EClientNotificationType
k_ESystemUpdateNotificationType_Invalid: ESystemUpdateNotificationType
k_ESystemUpdateNotificationType_Available: ESystemUpdateNotificationType
k_ESystemUpdateNotificationType_NeedsRestart: ESystemUpdateNotificationType
k_EGameRecordingErrorGeneral: EGameRecordingErrorType
k_EGameRecordingErrorLowDiskSpace: EGameRecordingErrorType

class CClientNotificationCloudSyncFailure(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CClientNotificationCloudSyncConflict(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CClientNotificationScreenshot(_message.Message):
    __slots__ = ("screenshot_handle", "description", "local_url")
    SCREENSHOT_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_URL_FIELD_NUMBER: _ClassVar[int]
    screenshot_handle: str
    description: str
    local_url: str
    def __init__(self, screenshot_handle: _Optional[str] = ..., description: _Optional[str] = ..., local_url: _Optional[str] = ...) -> None: ...

class CClientNotificationDownloadCompleted(_message.Message):
    __slots__ = ("appid", "dlc_appid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DLC_APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    dlc_appid: int
    def __init__(self, appid: _Optional[int] = ..., dlc_appid: _Optional[int] = ...) -> None: ...

class CClientNotificationFriendInvite(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CClientNotificationFriendInviteRollup(_message.Message):
    __slots__ = ("new_invite_count",)
    NEW_INVITE_COUNT_FIELD_NUMBER: _ClassVar[int]
    new_invite_count: int
    def __init__(self, new_invite_count: _Optional[int] = ...) -> None: ...

class CClientNotificationFriendInGame(_message.Message):
    __slots__ = ("steamid", "game_name")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GAME_NAME_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    game_name: str
    def __init__(self, steamid: _Optional[int] = ..., game_name: _Optional[str] = ...) -> None: ...

class CClientNotificationFriendOnline(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CClientNotificationAchievement(_message.Message):
    __slots__ = ("achievement_id", "appid", "name", "description", "image_url", "achieved", "rtime_unlocked", "min_progress", "current_progress", "max_progress", "global_achieved_pct")
    ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    ACHIEVED_FIELD_NUMBER: _ClassVar[int]
    RTIME_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    MIN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_ACHIEVED_PCT_FIELD_NUMBER: _ClassVar[int]
    achievement_id: str
    appid: int
    name: str
    description: str
    image_url: str
    achieved: bool
    rtime_unlocked: int
    min_progress: float
    current_progress: float
    max_progress: float
    global_achieved_pct: float
    def __init__(self, achievement_id: _Optional[str] = ..., appid: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., image_url: _Optional[str] = ..., achieved: bool = ..., rtime_unlocked: _Optional[int] = ..., min_progress: _Optional[float] = ..., current_progress: _Optional[float] = ..., max_progress: _Optional[float] = ..., global_achieved_pct: _Optional[float] = ...) -> None: ...

class CClientNotificationLowBattery(_message.Message):
    __slots__ = ("pct_remaining",)
    PCT_REMAINING_FIELD_NUMBER: _ClassVar[int]
    pct_remaining: float
    def __init__(self, pct_remaining: _Optional[float] = ...) -> None: ...

class CClientNotificationSystemUpdate(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: ESystemUpdateNotificationType
    def __init__(self, type: _Optional[_Union[ESystemUpdateNotificationType, str]] = ...) -> None: ...

class CClientNotificationFriendMessage(_message.Message):
    __slots__ = ("tag", "steamid", "title", "body", "icon", "notificationid", "response_steamurl")
    TAG_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STEAMURL_FIELD_NUMBER: _ClassVar[int]
    tag: str
    steamid: str
    title: str
    body: str
    icon: str
    notificationid: int
    response_steamurl: str
    def __init__(self, tag: _Optional[str] = ..., steamid: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., icon: _Optional[str] = ..., notificationid: _Optional[int] = ..., response_steamurl: _Optional[str] = ...) -> None: ...

class CClientNotificationGroupChatMessage(_message.Message):
    __slots__ = ("tag", "steamid_sender", "chat_group_id", "chat_id", "title", "body", "rawbody", "icon", "notificationid")
    TAG_FIELD_NUMBER: _ClassVar[int]
    STEAMID_SENDER_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    RAWBODY_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONID_FIELD_NUMBER: _ClassVar[int]
    tag: str
    steamid_sender: str
    chat_group_id: str
    chat_id: str
    title: str
    body: str
    rawbody: str
    icon: str
    notificationid: int
    def __init__(self, tag: _Optional[str] = ..., steamid_sender: _Optional[str] = ..., chat_group_id: _Optional[str] = ..., chat_id: _Optional[str] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., rawbody: _Optional[str] = ..., icon: _Optional[str] = ..., notificationid: _Optional[int] = ...) -> None: ...

class CClientNotificationFamilySharingDeviceAuthorizationChanged(_message.Message):
    __slots__ = ("accountid_owner", "authorized")
    ACCOUNTID_OWNER_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZED_FIELD_NUMBER: _ClassVar[int]
    accountid_owner: int
    authorized: bool
    def __init__(self, accountid_owner: _Optional[int] = ..., authorized: bool = ...) -> None: ...

class CClientNotificationFamilySharingStopPlaying(_message.Message):
    __slots__ = ("accountid_owner", "seconds_remaining", "appid")
    ACCOUNTID_OWNER_FIELD_NUMBER: _ClassVar[int]
    SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    accountid_owner: int
    seconds_remaining: int
    appid: int
    def __init__(self, accountid_owner: _Optional[int] = ..., seconds_remaining: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CClientNotificationFamilySharingLibraryAvailable(_message.Message):
    __slots__ = ("accountid_owner",)
    ACCOUNTID_OWNER_FIELD_NUMBER: _ClassVar[int]
    accountid_owner: int
    def __init__(self, accountid_owner: _Optional[int] = ...) -> None: ...

class CClientNotificationIncomingVoiceChat(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CClientNotificationClaimSteamDeckRewards(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CClientNotificationGiftReceived(_message.Message):
    __slots__ = ("sender_name",)
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    sender_name: str
    def __init__(self, sender_name: _Optional[str] = ...) -> None: ...

class CClientNotificationItemAnnouncement(_message.Message):
    __slots__ = ("new_item_count", "new_backpack_items")
    NEW_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEW_BACKPACK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    new_item_count: int
    new_backpack_items: bool
    def __init__(self, new_item_count: _Optional[int] = ..., new_backpack_items: bool = ...) -> None: ...

class CClientNotificationHardwareSurveyPending(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CClientNotificationLowDiskSpace(_message.Message):
    __slots__ = ("folder_index",)
    FOLDER_INDEX_FIELD_NUMBER: _ClassVar[int]
    folder_index: int
    def __init__(self, folder_index: _Optional[int] = ...) -> None: ...

class CClientNotificationBatteryTemperature(_message.Message):
    __slots__ = ("temperature", "notification_type")
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    temperature: int
    notification_type: str
    def __init__(self, temperature: _Optional[int] = ..., notification_type: _Optional[str] = ...) -> None: ...

class CClientNotificationDockUnsupportedFirmware(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CClientNotificationPeerContentUpload(_message.Message):
    __slots__ = ("appid", "peer_name")
    APPID_FIELD_NUMBER: _ClassVar[int]
    PEER_NAME_FIELD_NUMBER: _ClassVar[int]
    appid: int
    peer_name: str
    def __init__(self, appid: _Optional[int] = ..., peer_name: _Optional[str] = ...) -> None: ...

class CClientNotificationCannotReadControllerGuideButton(_message.Message):
    __slots__ = ("controller_index",)
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    def __init__(self, controller_index: _Optional[int] = ...) -> None: ...

class CClientNotificationOverlaySplashScreen(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CClientNotificationBroadcastAvailableToWatch(_message.Message):
    __slots__ = ("broadcast_permission",)
    BROADCAST_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    broadcast_permission: int
    def __init__(self, broadcast_permission: _Optional[int] = ...) -> None: ...

class CClientNotificationTimedTrialRemaining(_message.Message):
    __slots__ = ("appid", "icon", "offline", "allowed_seconds", "played_seconds")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    PLAYED_SECONDS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    icon: str
    offline: bool
    allowed_seconds: int
    played_seconds: int
    def __init__(self, appid: _Optional[int] = ..., icon: _Optional[str] = ..., offline: bool = ..., allowed_seconds: _Optional[int] = ..., played_seconds: _Optional[int] = ...) -> None: ...

class CClientNotificationLoginRefresh(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CClientNotificationTimerExpired(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CClientNotificationSteamInputActionSetChanged(_message.Message):
    __slots__ = ("controller_index", "action_set_name")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACTION_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    action_set_name: str
    def __init__(self, controller_index: _Optional[int] = ..., action_set_name: _Optional[str] = ...) -> None: ...

class CClientNotificationRemoteClientConnection(_message.Message):
    __slots__ = ("machine", "connected")
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    machine: str
    connected: bool
    def __init__(self, machine: _Optional[str] = ..., connected: bool = ...) -> None: ...

class CClientNotificationRemoteClientStartStream(_message.Message):
    __slots__ = ("machine", "game_name")
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    GAME_NAME_FIELD_NUMBER: _ClassVar[int]
    machine: str
    game_name: str
    def __init__(self, machine: _Optional[str] = ..., game_name: _Optional[str] = ...) -> None: ...

class CClientNotificationStreamingClientConnection(_message.Message):
    __slots__ = ("hostname", "machine", "connected")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    machine: str
    connected: bool
    def __init__(self, hostname: _Optional[str] = ..., machine: _Optional[str] = ..., connected: bool = ...) -> None: ...

class CClientNotificationPlaytimeWarning(_message.Message):
    __slots__ = ("type", "playtime_remaining")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    type: str
    playtime_remaining: int
    def __init__(self, type: _Optional[str] = ..., playtime_remaining: _Optional[int] = ...) -> None: ...

class CClientNotificationGameRecordingError(_message.Message):
    __slots__ = ("game_id", "error_type")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    error_type: EGameRecordingErrorType
    def __init__(self, game_id: _Optional[int] = ..., error_type: _Optional[_Union[EGameRecordingErrorType, str]] = ...) -> None: ...

class CClientNotificationGameRecordingStart(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CClientNotificationGameRecordingStop(_message.Message):
    __slots__ = ("game_id", "clip_id", "duration_secs")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    clip_id: str
    duration_secs: float
    def __init__(self, game_id: _Optional[int] = ..., clip_id: _Optional[str] = ..., duration_secs: _Optional[float] = ...) -> None: ...

class CClientNotificationGameRecordingUserMarkerAdded(_message.Message):
    __slots__ = ("game_id",)
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    def __init__(self, game_id: _Optional[int] = ...) -> None: ...

class CClientNotificationGameRecordingInstantClip(_message.Message):
    __slots__ = ("game_id", "clip_id", "duration_secs")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    clip_id: str
    duration_secs: float
    def __init__(self, game_id: _Optional[int] = ..., clip_id: _Optional[str] = ..., duration_secs: _Optional[float] = ...) -> None: ...
