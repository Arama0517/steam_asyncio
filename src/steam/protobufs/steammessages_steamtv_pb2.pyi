import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EBroadcastImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EBroadcastImageType_None: _ClassVar[EBroadcastImageType]
    k_EBroadcastImageType_Offline: _ClassVar[EBroadcastImageType]
    k_EBroadcastImageType_Standby: _ClassVar[EBroadcastImageType]
    k_EBroadcastImageType_Avatar: _ClassVar[EBroadcastImageType]
    k_EBroadcastImageType_Summary: _ClassVar[EBroadcastImageType]
    k_EBroadcastImageType_Background: _ClassVar[EBroadcastImageType]
    k_EBroadcastImageType_Emoticon: _ClassVar[EBroadcastImageType]

class EGetGamesAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EGetGamesAlgorithm_Default: _ClassVar[EGetGamesAlgorithm]
    k_EGetGamesAlgorithm_MostPlayed: _ClassVar[EGetGamesAlgorithm]
    k_EGetGamesAlgorithm_PopularNew: _ClassVar[EGetGamesAlgorithm]

class EGetChannelsAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EGetChannelsAlgorithm_Default: _ClassVar[EGetChannelsAlgorithm]
    k_EGetChannelsAlgorithm_Friends: _ClassVar[EGetChannelsAlgorithm]
    k_EGetChannelsAlgorithm_Featured: _ClassVar[EGetChannelsAlgorithm]
    k_EGetChannelsAlgorithm_Developer: _ClassVar[EGetChannelsAlgorithm]
    k_EGetChannelsAlgorithm_Following: _ClassVar[EGetChannelsAlgorithm]

class ESteamTVContentTemplate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESteamTVContentTemplate_Invalid: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_Takeover: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_SingleGame: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_GameList: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_QuickExplore: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_ConveyorBelt: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_WatchParty: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_Developer: _ClassVar[ESteamTVContentTemplate]
    k_ESteamTVContentTemplate_Event: _ClassVar[ESteamTVContentTemplate]
k_EBroadcastImageType_None: EBroadcastImageType
k_EBroadcastImageType_Offline: EBroadcastImageType
k_EBroadcastImageType_Standby: EBroadcastImageType
k_EBroadcastImageType_Avatar: EBroadcastImageType
k_EBroadcastImageType_Summary: EBroadcastImageType
k_EBroadcastImageType_Background: EBroadcastImageType
k_EBroadcastImageType_Emoticon: EBroadcastImageType
k_EGetGamesAlgorithm_Default: EGetGamesAlgorithm
k_EGetGamesAlgorithm_MostPlayed: EGetGamesAlgorithm
k_EGetGamesAlgorithm_PopularNew: EGetGamesAlgorithm
k_EGetChannelsAlgorithm_Default: EGetChannelsAlgorithm
k_EGetChannelsAlgorithm_Friends: EGetChannelsAlgorithm
k_EGetChannelsAlgorithm_Featured: EGetChannelsAlgorithm
k_EGetChannelsAlgorithm_Developer: EGetChannelsAlgorithm
k_EGetChannelsAlgorithm_Following: EGetChannelsAlgorithm
k_ESteamTVContentTemplate_Invalid: ESteamTVContentTemplate
k_ESteamTVContentTemplate_Takeover: ESteamTVContentTemplate
k_ESteamTVContentTemplate_SingleGame: ESteamTVContentTemplate
k_ESteamTVContentTemplate_GameList: ESteamTVContentTemplate
k_ESteamTVContentTemplate_QuickExplore: ESteamTVContentTemplate
k_ESteamTVContentTemplate_ConveyorBelt: ESteamTVContentTemplate
k_ESteamTVContentTemplate_WatchParty: ESteamTVContentTemplate
k_ESteamTVContentTemplate_Developer: ESteamTVContentTemplate
k_ESteamTVContentTemplate_Event: ESteamTVContentTemplate

class CSteamTV_CreateBroadcastChannel_Request(_message.Message):
    __slots__ = ("unique_name",)
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    unique_name: str
    def __init__(self, unique_name: _Optional[str] = ...) -> None: ...

class CSteamTV_CreateBroadcastChannel_Response(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelID_Request(_message.Message):
    __slots__ = ("unique_name",)
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    unique_name: str
    def __init__(self, unique_name: _Optional[str] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelID_Response(_message.Message):
    __slots__ = ("broadcast_channel_id", "unique_name", "steamid")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    unique_name: str
    steamid: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., unique_name: _Optional[str] = ..., steamid: _Optional[int] = ...) -> None: ...

class CSteamTV_SetBroadcastChannelProfile_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "name", "language", "headline", "summary", "avatar_hash", "schedule", "rules", "panels")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_HASH_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    PANELS_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    name: str
    language: str
    headline: str
    summary: str
    avatar_hash: str
    schedule: str
    rules: str
    panels: str
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., name: _Optional[str] = ..., language: _Optional[str] = ..., headline: _Optional[str] = ..., summary: _Optional[str] = ..., avatar_hash: _Optional[str] = ..., schedule: _Optional[str] = ..., rules: _Optional[str] = ..., panels: _Optional[str] = ...) -> None: ...

class CSteamTV_SetBroadcastChannelProfile_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetBroadcastChannelProfile_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelProfile_Response(_message.Message):
    __slots__ = ("unique_name", "owner_steamid", "name", "language", "headline", "summary", "schedule", "rules", "panels", "is_partnered")
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    PANELS_FIELD_NUMBER: _ClassVar[int]
    IS_PARTNERED_FIELD_NUMBER: _ClassVar[int]
    unique_name: str
    owner_steamid: int
    name: str
    language: str
    headline: str
    summary: str
    schedule: str
    rules: str
    panels: str
    is_partnered: bool
    def __init__(self, unique_name: _Optional[str] = ..., owner_steamid: _Optional[int] = ..., name: _Optional[str] = ..., language: _Optional[str] = ..., headline: _Optional[str] = ..., summary: _Optional[str] = ..., schedule: _Optional[str] = ..., rules: _Optional[str] = ..., panels: _Optional[str] = ..., is_partnered: bool = ...) -> None: ...

class CSteamTV_SetBroadcastChannelImage_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "image_type", "image_index", "image_width", "image_height", "file_size", "file_extension", "file_hash", "undo")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
    IMAGE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    IMAGE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    UNDO_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    image_type: EBroadcastImageType
    image_index: int
    image_width: int
    image_height: int
    file_size: int
    file_extension: str
    file_hash: str
    undo: bool
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., image_type: _Optional[_Union[EBroadcastImageType, str]] = ..., image_index: _Optional[int] = ..., image_width: _Optional[int] = ..., image_height: _Optional[int] = ..., file_size: _Optional[int] = ..., file_extension: _Optional[str] = ..., file_hash: _Optional[str] = ..., undo: bool = ...) -> None: ...

class CSteamTV_SetBroadcastChannelImage_Response(_message.Message):
    __slots__ = ("replace_image_hash",)
    REPLACE_IMAGE_HASH_FIELD_NUMBER: _ClassVar[int]
    replace_image_hash: str
    def __init__(self, replace_image_hash: _Optional[str] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelImages_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "image_types")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    image_types: _containers.RepeatedScalarFieldContainer[EBroadcastImageType]
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., image_types: _Optional[_Iterable[_Union[EBroadcastImageType, str]]] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelImages_Response(_message.Message):
    __slots__ = ("images",)
    class Images(_message.Message):
        __slots__ = ("image_type", "image_path", "image_index")
        IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
        IMAGE_INDEX_FIELD_NUMBER: _ClassVar[int]
        image_type: EBroadcastImageType
        image_path: str
        image_index: int
        def __init__(self, image_type: _Optional[_Union[EBroadcastImageType, str]] = ..., image_path: _Optional[str] = ..., image_index: _Optional[int] = ...) -> None: ...
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    images: _containers.RepeatedCompositeFieldContainer[CSteamTV_GetBroadcastChannelImages_Response.Images]
    def __init__(self, images: _Optional[_Iterable[_Union[CSteamTV_GetBroadcastChannelImages_Response.Images, _Mapping]]] = ...) -> None: ...

class CSteamTV_SetBroadcastChannelLinkRegions_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "links")
    class Links(_message.Message):
        __slots__ = ("link_index", "url", "link_description", "left", "top", "width", "height")
        LINK_INDEX_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        LINK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        TOP_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        link_index: int
        url: str
        link_description: str
        left: int
        top: int
        width: int
        height: int
        def __init__(self, link_index: _Optional[int] = ..., url: _Optional[str] = ..., link_description: _Optional[str] = ..., left: _Optional[int] = ..., top: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    links: _containers.RepeatedCompositeFieldContainer[CSteamTV_SetBroadcastChannelLinkRegions_Request.Links]
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., links: _Optional[_Iterable[_Union[CSteamTV_SetBroadcastChannelLinkRegions_Request.Links, _Mapping]]] = ...) -> None: ...

class CSteamTV_SetBroadcastChannelLinkRegions_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetBroadcastChannelLinks_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelLinks_Response(_message.Message):
    __slots__ = ("links",)
    class Links(_message.Message):
        __slots__ = ("link_index", "url", "link_description", "left", "top", "width", "height")
        LINK_INDEX_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        LINK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        TOP_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        link_index: int
        url: str
        link_description: str
        left: int
        top: int
        width: int
        height: int
        def __init__(self, link_index: _Optional[int] = ..., url: _Optional[str] = ..., link_description: _Optional[str] = ..., left: _Optional[int] = ..., top: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[CSteamTV_GetBroadcastChannelLinks_Response.Links]
    def __init__(self, links: _Optional[_Iterable[_Union[CSteamTV_GetBroadcastChannelLinks_Response.Links, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelBroadcasters_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelBroadcasters_Response(_message.Message):
    __slots__ = ("broadcasters",)
    class Broadcaster(_message.Message):
        __slots__ = ("steamid", "name", "rtmp_token")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RTMP_TOKEN_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        name: str
        rtmp_token: str
        def __init__(self, steamid: _Optional[int] = ..., name: _Optional[str] = ..., rtmp_token: _Optional[str] = ...) -> None: ...
    BROADCASTERS_FIELD_NUMBER: _ClassVar[int]
    broadcasters: _containers.RepeatedCompositeFieldContainer[CSteamTV_GetBroadcastChannelBroadcasters_Response.Broadcaster]
    def __init__(self, broadcasters: _Optional[_Iterable[_Union[CSteamTV_GetBroadcastChannelBroadcasters_Response.Broadcaster, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetFollowedChannels_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetBroadcastChannelEntry(_message.Message):
    __slots__ = ("broadcast_channel_id", "unique_name", "name", "appid", "viewers", "views", "thumbnail_url", "followers", "headline", "avatar_url", "broadcaster_steamid", "subscribers", "background_url", "is_featured", "is_disabled", "is_live", "language", "reports", "is_partnered")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    FOLLOWERS_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERS_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_URL_FIELD_NUMBER: _ClassVar[int]
    IS_FEATURED_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    IS_LIVE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    IS_PARTNERED_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    unique_name: str
    name: str
    appid: int
    viewers: int
    views: int
    thumbnail_url: str
    followers: int
    headline: str
    avatar_url: str
    broadcaster_steamid: int
    subscribers: int
    background_url: str
    is_featured: bool
    is_disabled: bool
    is_live: bool
    language: str
    reports: int
    is_partnered: bool
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., unique_name: _Optional[str] = ..., name: _Optional[str] = ..., appid: _Optional[int] = ..., viewers: _Optional[int] = ..., views: _Optional[int] = ..., thumbnail_url: _Optional[str] = ..., followers: _Optional[int] = ..., headline: _Optional[str] = ..., avatar_url: _Optional[str] = ..., broadcaster_steamid: _Optional[int] = ..., subscribers: _Optional[int] = ..., background_url: _Optional[str] = ..., is_featured: bool = ..., is_disabled: bool = ..., is_live: bool = ..., language: _Optional[str] = ..., reports: _Optional[int] = ..., is_partnered: bool = ...) -> None: ...

class CSteamTV_GetFollowedChannels_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    def __init__(self, results: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetSubscribedChannels_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetSubscribedChannels_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    def __init__(self, results: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelStatus_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelStatus_Response(_message.Message):
    __slots__ = ("is_live", "is_disabled", "appid", "viewers", "views", "broadcaster_steamid", "thumbnail_url", "followers", "subscribers", "unique_name", "broadcast_session_id")
    IS_LIVE_FIELD_NUMBER: _ClassVar[int]
    IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    FOLLOWERS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    is_live: bool
    is_disabled: bool
    appid: int
    viewers: int
    views: int
    broadcaster_steamid: int
    thumbnail_url: str
    followers: int
    subscribers: int
    unique_name: str
    broadcast_session_id: int
    def __init__(self, is_live: bool = ..., is_disabled: bool = ..., appid: _Optional[int] = ..., viewers: _Optional[int] = ..., views: _Optional[int] = ..., broadcaster_steamid: _Optional[int] = ..., thumbnail_url: _Optional[str] = ..., followers: _Optional[int] = ..., subscribers: _Optional[int] = ..., unique_name: _Optional[str] = ..., broadcast_session_id: _Optional[int] = ...) -> None: ...

class CSteamTV_FollowBroadcastChannel_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "undo")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    UNDO_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    undo: bool
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., undo: bool = ...) -> None: ...

class CSteamTV_FollowBroadcastChannel_Response(_message.Message):
    __slots__ = ("is_followed",)
    IS_FOLLOWED_FIELD_NUMBER: _ClassVar[int]
    is_followed: bool
    def __init__(self, is_followed: bool = ...) -> None: ...

class CSteamTV_SubscribeBroadcastChannel_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_SubscribeBroadcastChannel_Response(_message.Message):
    __slots__ = ("is_subscribed",)
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    is_subscribed: bool
    def __init__(self, is_subscribed: bool = ...) -> None: ...

class CSteamTV_GetBroadcastChannelClips_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_BroadcastClipInfo(_message.Message):
    __slots__ = ("broadcast_clip_id", "channel_id", "app_id", "broadcaster_steamid", "creator_steamid", "video_description", "live_time", "length_ms", "thumbnail_path")
    BROADCAST_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_STEAMID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LIVE_TIME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_PATH_FIELD_NUMBER: _ClassVar[int]
    broadcast_clip_id: int
    channel_id: int
    app_id: int
    broadcaster_steamid: int
    creator_steamid: int
    video_description: str
    live_time: int
    length_ms: int
    thumbnail_path: str
    def __init__(self, broadcast_clip_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., app_id: _Optional[int] = ..., broadcaster_steamid: _Optional[int] = ..., creator_steamid: _Optional[int] = ..., video_description: _Optional[str] = ..., live_time: _Optional[int] = ..., length_ms: _Optional[int] = ..., thumbnail_path: _Optional[str] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelClips_Response(_message.Message):
    __slots__ = ("clips", "thumbnail_host")
    CLIPS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_HOST_FIELD_NUMBER: _ClassVar[int]
    clips: _containers.RepeatedCompositeFieldContainer[CSteamTV_BroadcastClipInfo]
    thumbnail_host: str
    def __init__(self, clips: _Optional[_Iterable[_Union[CSteamTV_BroadcastClipInfo, _Mapping]]] = ..., thumbnail_host: _Optional[str] = ...) -> None: ...

class CSteamTV_ReportBroadcastChannel_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "reason")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    reason: str
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class CSteamTV_ReportBroadcastChannel_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetBroadcastChannelInteraction_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetBroadcastChannelInteraction_Response(_message.Message):
    __slots__ = ("is_followed", "is_subscribed")
    IS_FOLLOWED_FIELD_NUMBER: _ClassVar[int]
    IS_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
    is_followed: bool
    is_subscribed: bool
    def __init__(self, is_followed: bool = ..., is_subscribed: bool = ...) -> None: ...

class CSteamTV_GetGames_Request(_message.Message):
    __slots__ = ("appid", "algorithm", "count")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    algorithm: EGetGamesAlgorithm
    count: int
    def __init__(self, appid: _Optional[int] = ..., algorithm: _Optional[_Union[EGetGamesAlgorithm, str]] = ..., count: _Optional[int] = ...) -> None: ...

class CSteamTV_Game(_message.Message):
    __slots__ = ("appid", "name", "image", "viewers", "channels", "release_date", "developer", "publisher")
    APPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    VIEWERS_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    appid: int
    name: str
    image: str
    viewers: int
    channels: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    release_date: str
    developer: str
    publisher: str
    def __init__(self, appid: _Optional[int] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., viewers: _Optional[int] = ..., channels: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ..., release_date: _Optional[str] = ..., developer: _Optional[str] = ..., publisher: _Optional[str] = ...) -> None: ...

class CSteamTV_GetGames_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CSteamTV_Game]
    def __init__(self, results: _Optional[_Iterable[_Union[CSteamTV_Game, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetChannels_Request(_message.Message):
    __slots__ = ("algorithm", "count", "appid")
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    algorithm: EGetChannelsAlgorithm
    count: int
    appid: int
    def __init__(self, algorithm: _Optional[_Union[EGetChannelsAlgorithm, str]] = ..., count: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CSteamTV_GetChannels_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    def __init__(self, results: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ...) -> None: ...

class CSteamTV_AddChatBan_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "chatter_steamid", "duration", "permanent", "undo")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHATTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    UNDO_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    chatter_steamid: int
    duration: int
    permanent: bool
    undo: bool
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., chatter_steamid: _Optional[int] = ..., duration: _Optional[int] = ..., permanent: bool = ..., undo: bool = ...) -> None: ...

class CSteamTV_AddChatBan_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetChatBans_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_ChatBan(_message.Message):
    __slots__ = ("issuer_steamid", "chatter_steamid", "time_expires", "permanent", "name")
    ISSUER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHATTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    issuer_steamid: int
    chatter_steamid: int
    time_expires: str
    permanent: bool
    name: str
    def __init__(self, issuer_steamid: _Optional[int] = ..., chatter_steamid: _Optional[int] = ..., time_expires: _Optional[str] = ..., permanent: bool = ..., name: _Optional[str] = ...) -> None: ...

class CSteamTV_GetChatBans_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CSteamTV_ChatBan]
    def __init__(self, results: _Optional[_Iterable[_Union[CSteamTV_ChatBan, _Mapping]]] = ...) -> None: ...

class CSteamTV_AddChatModerator_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "moderator_steamid", "undo")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODERATOR_STEAMID_FIELD_NUMBER: _ClassVar[int]
    UNDO_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    moderator_steamid: int
    undo: bool
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., moderator_steamid: _Optional[int] = ..., undo: bool = ...) -> None: ...

class CSteamTV_AddChatModerator_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetChatModerators_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_ChatModerator(_message.Message):
    __slots__ = ("steamid", "name")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    name: str
    def __init__(self, steamid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CSteamTV_GetChatModerators_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[CSteamTV_ChatModerator]
    def __init__(self, results: _Optional[_Iterable[_Union[CSteamTV_ChatModerator, _Mapping]]] = ...) -> None: ...

class CSteamTV_AddWordBan_Request(_message.Message):
    __slots__ = ("broadcast_channel_id", "word", "undo")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    WORD_FIELD_NUMBER: _ClassVar[int]
    UNDO_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    word: str
    undo: bool
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., word: _Optional[str] = ..., undo: bool = ...) -> None: ...

class CSteamTV_AddWordBan_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetWordBans_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_GetWordBans_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, results: _Optional[_Iterable[str]] = ...) -> None: ...

class CSteamTV_JoinChat_Request(_message.Message):
    __slots__ = ("broadcast_channel_id",)
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    def __init__(self, broadcast_channel_id: _Optional[int] = ...) -> None: ...

class CSteamTV_JoinChat_Response(_message.Message):
    __slots__ = ("chat_id", "view_url_template", "flair_group_ids")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FLAIR_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    view_url_template: str
    flair_group_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_id: _Optional[int] = ..., view_url_template: _Optional[str] = ..., flair_group_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CSteamTV_Search_Request(_message.Message):
    __slots__ = ("term",)
    TERM_FIELD_NUMBER: _ClassVar[int]
    term: str
    def __init__(self, term: _Optional[str] = ...) -> None: ...

class CSteamTV_Search_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    def __init__(self, results: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetSteamTVUserSettings_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetSteamTVUserSettings_Response(_message.Message):
    __slots__ = ("stream_live_email", "stream_live_notification")
    STREAM_LIVE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STREAM_LIVE_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    stream_live_email: bool
    stream_live_notification: bool
    def __init__(self, stream_live_email: bool = ..., stream_live_notification: bool = ...) -> None: ...

class CSteamTV_SetSteamTVUserSettings_Request(_message.Message):
    __slots__ = ("stream_live_email", "stream_live_notification")
    STREAM_LIVE_EMAIL_FIELD_NUMBER: _ClassVar[int]
    STREAM_LIVE_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    stream_live_email: bool
    stream_live_notification: bool
    def __init__(self, stream_live_email: bool = ..., stream_live_notification: bool = ...) -> None: ...

class CSteamTV_SetSteamTVUserSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetMyBroadcastChannels_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_GetMyBroadcastChannels_Response(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    def __init__(self, results: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ...) -> None: ...

class CSteamTV_GetHomePageContents_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamTV_HomePageTemplate_Takeover(_message.Message):
    __slots__ = ("broadcasts",)
    BROADCASTS_FIELD_NUMBER: _ClassVar[int]
    broadcasts: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    def __init__(self, broadcasts: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ...) -> None: ...

class CSteamTV_HomePageTemplate_SingleGame(_message.Message):
    __slots__ = ("broadcasts", "appid", "title")
    BROADCASTS_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    broadcasts: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    appid: int
    title: str
    def __init__(self, broadcasts: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ..., appid: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...

class GameListEntry(_message.Message):
    __slots__ = ("appid", "game_name", "broadcast")
    APPID_FIELD_NUMBER: _ClassVar[int]
    GAME_NAME_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    appid: int
    game_name: str
    broadcast: GetBroadcastChannelEntry
    def __init__(self, appid: _Optional[int] = ..., game_name: _Optional[str] = ..., broadcast: _Optional[_Union[GetBroadcastChannelEntry, _Mapping]] = ...) -> None: ...

class CSteamTV_HomePageTemplate_GameList(_message.Message):
    __slots__ = ("entries", "title")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[GameListEntry]
    title: str
    def __init__(self, entries: _Optional[_Iterable[_Union[GameListEntry, _Mapping]]] = ..., title: _Optional[str] = ...) -> None: ...

class CSteamTV_HomePageTemplate_QuickExplore(_message.Message):
    __slots__ = ("broadcasts", "title")
    BROADCASTS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    broadcasts: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    title: str
    def __init__(self, broadcasts: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ..., title: _Optional[str] = ...) -> None: ...

class CSteamTV_HomePageTemplate_ConveyorBelt(_message.Message):
    __slots__ = ("broadcasts", "title")
    BROADCASTS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    broadcasts: _containers.RepeatedCompositeFieldContainer[GetBroadcastChannelEntry]
    title: str
    def __init__(self, broadcasts: _Optional[_Iterable[_Union[GetBroadcastChannelEntry, _Mapping]]] = ..., title: _Optional[str] = ...) -> None: ...

class CSteamTV_HomePageTemplate_WatchParty(_message.Message):
    __slots__ = ("broadcast", "title", "chat_group_id")
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CHAT_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast: GetBroadcastChannelEntry
    title: str
    chat_group_id: int
    def __init__(self, broadcast: _Optional[_Union[GetBroadcastChannelEntry, _Mapping]] = ..., title: _Optional[str] = ..., chat_group_id: _Optional[int] = ...) -> None: ...

class CSteamTV_HomePageTemplate_Developer(_message.Message):
    __slots__ = ("broadcast", "title")
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    broadcast: GetBroadcastChannelEntry
    title: str
    def __init__(self, broadcast: _Optional[_Union[GetBroadcastChannelEntry, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...

class CSteamTV_HomePageTemplate_Event(_message.Message):
    __slots__ = ("title",)
    TITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    def __init__(self, title: _Optional[str] = ...) -> None: ...

class CSteamTV_HomePageContentRow(_message.Message):
    __slots__ = ("template_type", "takeover", "single_game", "game_list", "quick_explore", "conveyor_belt", "watch_party", "developer", "event")
    TEMPLATE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAKEOVER_FIELD_NUMBER: _ClassVar[int]
    SINGLE_GAME_FIELD_NUMBER: _ClassVar[int]
    GAME_LIST_FIELD_NUMBER: _ClassVar[int]
    QUICK_EXPLORE_FIELD_NUMBER: _ClassVar[int]
    CONVEYOR_BELT_FIELD_NUMBER: _ClassVar[int]
    WATCH_PARTY_FIELD_NUMBER: _ClassVar[int]
    DEVELOPER_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    template_type: ESteamTVContentTemplate
    takeover: CSteamTV_HomePageTemplate_Takeover
    single_game: CSteamTV_HomePageTemplate_SingleGame
    game_list: CSteamTV_HomePageTemplate_GameList
    quick_explore: CSteamTV_HomePageTemplate_QuickExplore
    conveyor_belt: CSteamTV_HomePageTemplate_ConveyorBelt
    watch_party: CSteamTV_HomePageTemplate_WatchParty
    developer: CSteamTV_HomePageTemplate_Developer
    event: CSteamTV_HomePageTemplate_Event
    def __init__(self, template_type: _Optional[_Union[ESteamTVContentTemplate, str]] = ..., takeover: _Optional[_Union[CSteamTV_HomePageTemplate_Takeover, _Mapping]] = ..., single_game: _Optional[_Union[CSteamTV_HomePageTemplate_SingleGame, _Mapping]] = ..., game_list: _Optional[_Union[CSteamTV_HomePageTemplate_GameList, _Mapping]] = ..., quick_explore: _Optional[_Union[CSteamTV_HomePageTemplate_QuickExplore, _Mapping]] = ..., conveyor_belt: _Optional[_Union[CSteamTV_HomePageTemplate_ConveyorBelt, _Mapping]] = ..., watch_party: _Optional[_Union[CSteamTV_HomePageTemplate_WatchParty, _Mapping]] = ..., developer: _Optional[_Union[CSteamTV_HomePageTemplate_Developer, _Mapping]] = ..., event: _Optional[_Union[CSteamTV_HomePageTemplate_Event, _Mapping]] = ...) -> None: ...

class CSteamTV_GetHomePageContents_Response(_message.Message):
    __slots__ = ("rows",)
    ROWS_FIELD_NUMBER: _ClassVar[int]
    rows: _containers.RepeatedCompositeFieldContainer[CSteamTV_HomePageContentRow]
    def __init__(self, rows: _Optional[_Iterable[_Union[CSteamTV_HomePageContentRow, _Mapping]]] = ...) -> None: ...

class CSteamTV_AppCheer_SingleCheerType(_message.Message):
    __slots__ = ("cheer_type", "cheer_amount")
    CHEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHEER_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    cheer_type: int
    cheer_amount: int
    def __init__(self, cheer_type: _Optional[int] = ..., cheer_amount: _Optional[int] = ...) -> None: ...

class CSteamTV_AppCheer_Request(_message.Message):
    __slots__ = ("app_id", "cheer_target_id", "cheers")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    CHEER_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    CHEERS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    cheer_target_id: int
    cheers: _containers.RepeatedCompositeFieldContainer[CSteamTV_AppCheer_SingleCheerType]
    def __init__(self, app_id: _Optional[int] = ..., cheer_target_id: _Optional[int] = ..., cheers: _Optional[_Iterable[_Union[CSteamTV_AppCheer_SingleCheerType, _Mapping]]] = ...) -> None: ...

class CSteamTV_AppCheer_Response(_message.Message):
    __slots__ = ("aggregation_delay_ms",)
    AGGREGATION_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    aggregation_delay_ms: int
    def __init__(self, aggregation_delay_ms: _Optional[int] = ...) -> None: ...

class SteamTV(_service.service): ...

class SteamTV_Stub(SteamTV): ...
