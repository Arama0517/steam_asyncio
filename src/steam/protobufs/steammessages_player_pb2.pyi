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

class EProfileCustomizationStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EProfileCustomizationStyleDefault: _ClassVar[EProfileCustomizationStyle]
    k_EProfileCustomizationStyleSelected: _ClassVar[EProfileCustomizationStyle]
    k_EProfileCustomizationStyleRarest: _ClassVar[EProfileCustomizationStyle]
    k_EProfileCustomizationStyleMostRecent: _ClassVar[EProfileCustomizationStyle]
    k_EProfileCustomizationStyleRandom: _ClassVar[EProfileCustomizationStyle]
    k_EProfileCustomizationStyleHighestRated: _ClassVar[EProfileCustomizationStyle]

class EAgreementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAgreementType_Invalid: _ClassVar[EAgreementType]
    k_EAgreementType_GlobalSSA: _ClassVar[EAgreementType]
    k_EAgreementType_ChinaSSA: _ClassVar[EAgreementType]

class ENotificationSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ENotificationSettingNotifyUseDefault: _ClassVar[ENotificationSetting]
    k_ENotificationSettingAlways: _ClassVar[ENotificationSetting]
    k_ENotificationSettingNever: _ClassVar[ENotificationSetting]

class ETextFilterSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ETextFilterSettingSteamLabOptedOut: _ClassVar[ETextFilterSetting]
    k_ETextFilterSettingEnabled: _ClassVar[ETextFilterSetting]
    k_ETextFilterSettingEnabledAllowProfanity: _ClassVar[ETextFilterSetting]
    k_ETextFilterSettingDisabled: _ClassVar[ETextFilterSetting]
k_EProfileCustomizationStyleDefault: EProfileCustomizationStyle
k_EProfileCustomizationStyleSelected: EProfileCustomizationStyle
k_EProfileCustomizationStyleRarest: EProfileCustomizationStyle
k_EProfileCustomizationStyleMostRecent: EProfileCustomizationStyle
k_EProfileCustomizationStyleRandom: EProfileCustomizationStyle
k_EProfileCustomizationStyleHighestRated: EProfileCustomizationStyle
k_EAgreementType_Invalid: EAgreementType
k_EAgreementType_GlobalSSA: EAgreementType
k_EAgreementType_ChinaSSA: EAgreementType
k_ENotificationSettingNotifyUseDefault: ENotificationSetting
k_ENotificationSettingAlways: ENotificationSetting
k_ENotificationSettingNever: ENotificationSetting
k_ETextFilterSettingSteamLabOptedOut: ETextFilterSetting
k_ETextFilterSettingEnabled: ETextFilterSetting
k_ETextFilterSettingEnabledAllowProfanity: ETextFilterSetting
k_ETextFilterSettingDisabled: ETextFilterSetting

class CPlayer_GetRecentPlaytimeSessionsForChild_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CPlayer_GetRecentPlaytimeSessionsForChild_Response(_message.Message):
    __slots__ = ("sessions",)
    class PlaytimeSession(_message.Message):
        __slots__ = ("time_start", "time_end", "appid", "device_type", "disconnected")
        TIME_START_FIELD_NUMBER: _ClassVar[int]
        TIME_END_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
        time_start: int
        time_end: int
        appid: int
        device_type: int
        disconnected: bool
        def __init__(self, time_start: _Optional[int] = ..., time_end: _Optional[int] = ..., appid: _Optional[int] = ..., device_type: _Optional[int] = ..., disconnected: bool = ...) -> None: ...
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[CPlayer_GetRecentPlaytimeSessionsForChild_Response.PlaytimeSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[CPlayer_GetRecentPlaytimeSessionsForChild_Response.PlaytimeSession, _Mapping]]] = ...) -> None: ...

class CPlayer_GetPlayerLinkDetails_Request(_message.Message):
    __slots__ = ("steamids",)
    STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CPlayer_GetPlayerLinkDetails_Response(_message.Message):
    __slots__ = ("accounts",)
    class PlayerLinkDetails(_message.Message):
        __slots__ = ("public_data", "private_data")
        class AccountPublicData(_message.Message):
            __slots__ = ("steamid", "visibility_state", "privacy_state", "profile_state", "ban_expires_time", "account_flags", "sha_digest_avatar", "persona_name", "profile_url", "content_country_restricted")
            STEAMID_FIELD_NUMBER: _ClassVar[int]
            VISIBILITY_STATE_FIELD_NUMBER: _ClassVar[int]
            PRIVACY_STATE_FIELD_NUMBER: _ClassVar[int]
            PROFILE_STATE_FIELD_NUMBER: _ClassVar[int]
            BAN_EXPIRES_TIME_FIELD_NUMBER: _ClassVar[int]
            ACCOUNT_FLAGS_FIELD_NUMBER: _ClassVar[int]
            SHA_DIGEST_AVATAR_FIELD_NUMBER: _ClassVar[int]
            PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
            PROFILE_URL_FIELD_NUMBER: _ClassVar[int]
            CONTENT_COUNTRY_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
            steamid: int
            visibility_state: int
            privacy_state: int
            profile_state: int
            ban_expires_time: int
            account_flags: int
            sha_digest_avatar: bytes
            persona_name: str
            profile_url: str
            content_country_restricted: bool
            def __init__(self, steamid: _Optional[int] = ..., visibility_state: _Optional[int] = ..., privacy_state: _Optional[int] = ..., profile_state: _Optional[int] = ..., ban_expires_time: _Optional[int] = ..., account_flags: _Optional[int] = ..., sha_digest_avatar: _Optional[bytes] = ..., persona_name: _Optional[str] = ..., profile_url: _Optional[str] = ..., content_country_restricted: bool = ...) -> None: ...
        class AccountPrivateData(_message.Message):
            __slots__ = ("persona_state", "persona_state_flags", "time_created", "game_id", "game_server_steam_id", "game_server_ip_address", "game_server_port", "game_extra_info", "account_name", "lobby_steam_id", "rich_presence_kv", "broadcast_session_id", "watching_broadcast_accountid", "watching_broadcast_appid", "watching_broadcast_viewers", "watching_broadcast_title", "last_logoff_time", "last_seen_online", "game_os_type", "game_device_type", "game_device_name", "game_is_private")
            PERSONA_STATE_FIELD_NUMBER: _ClassVar[int]
            PERSONA_STATE_FLAGS_FIELD_NUMBER: _ClassVar[int]
            TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
            GAME_ID_FIELD_NUMBER: _ClassVar[int]
            GAME_SERVER_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
            GAME_SERVER_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
            GAME_SERVER_PORT_FIELD_NUMBER: _ClassVar[int]
            GAME_EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
            ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
            LOBBY_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
            RICH_PRESENCE_KV_FIELD_NUMBER: _ClassVar[int]
            BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
            WATCHING_BROADCAST_ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
            WATCHING_BROADCAST_APPID_FIELD_NUMBER: _ClassVar[int]
            WATCHING_BROADCAST_VIEWERS_FIELD_NUMBER: _ClassVar[int]
            WATCHING_BROADCAST_TITLE_FIELD_NUMBER: _ClassVar[int]
            LAST_LOGOFF_TIME_FIELD_NUMBER: _ClassVar[int]
            LAST_SEEN_ONLINE_FIELD_NUMBER: _ClassVar[int]
            GAME_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
            GAME_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
            GAME_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
            GAME_IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
            persona_state: int
            persona_state_flags: int
            time_created: int
            game_id: int
            game_server_steam_id: int
            game_server_ip_address: int
            game_server_port: int
            game_extra_info: str
            account_name: str
            lobby_steam_id: int
            rich_presence_kv: str
            broadcast_session_id: int
            watching_broadcast_accountid: int
            watching_broadcast_appid: int
            watching_broadcast_viewers: int
            watching_broadcast_title: str
            last_logoff_time: int
            last_seen_online: int
            game_os_type: int
            game_device_type: int
            game_device_name: str
            game_is_private: bool
            def __init__(self, persona_state: _Optional[int] = ..., persona_state_flags: _Optional[int] = ..., time_created: _Optional[int] = ..., game_id: _Optional[int] = ..., game_server_steam_id: _Optional[int] = ..., game_server_ip_address: _Optional[int] = ..., game_server_port: _Optional[int] = ..., game_extra_info: _Optional[str] = ..., account_name: _Optional[str] = ..., lobby_steam_id: _Optional[int] = ..., rich_presence_kv: _Optional[str] = ..., broadcast_session_id: _Optional[int] = ..., watching_broadcast_accountid: _Optional[int] = ..., watching_broadcast_appid: _Optional[int] = ..., watching_broadcast_viewers: _Optional[int] = ..., watching_broadcast_title: _Optional[str] = ..., last_logoff_time: _Optional[int] = ..., last_seen_online: _Optional[int] = ..., game_os_type: _Optional[int] = ..., game_device_type: _Optional[int] = ..., game_device_name: _Optional[str] = ..., game_is_private: bool = ...) -> None: ...
        PUBLIC_DATA_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_DATA_FIELD_NUMBER: _ClassVar[int]
        public_data: CPlayer_GetPlayerLinkDetails_Response.PlayerLinkDetails.AccountPublicData
        private_data: CPlayer_GetPlayerLinkDetails_Response.PlayerLinkDetails.AccountPrivateData
        def __init__(self, public_data: _Optional[_Union[CPlayer_GetPlayerLinkDetails_Response.PlayerLinkDetails.AccountPublicData, _Mapping]] = ..., private_data: _Optional[_Union[CPlayer_GetPlayerLinkDetails_Response.PlayerLinkDetails.AccountPrivateData, _Mapping]] = ...) -> None: ...
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[CPlayer_GetPlayerLinkDetails_Response.PlayerLinkDetails]
    def __init__(self, accounts: _Optional[_Iterable[_Union[CPlayer_GetPlayerLinkDetails_Response.PlayerLinkDetails, _Mapping]]] = ...) -> None: ...

class CPlayer_GetMutualFriendsForIncomingInvites_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_IncomingInviteMutualFriendList(_message.Message):
    __slots__ = ("steamid", "mutual_friend_account_ids")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_FRIEND_ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    mutual_friend_account_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid: _Optional[int] = ..., mutual_friend_account_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CPlayer_GetMutualFriendsForIncomingInvites_Response(_message.Message):
    __slots__ = ("incoming_invite_mutual_friends_lists",)
    INCOMING_INVITE_MUTUAL_FRIENDS_LISTS_FIELD_NUMBER: _ClassVar[int]
    incoming_invite_mutual_friends_lists: _containers.RepeatedCompositeFieldContainer[CPlayer_IncomingInviteMutualFriendList]
    def __init__(self, incoming_invite_mutual_friends_lists: _Optional[_Iterable[_Union[CPlayer_IncomingInviteMutualFriendList, _Mapping]]] = ...) -> None: ...

class CPlayer_GetOwnedGames_Request(_message.Message):
    __slots__ = ("steamid", "include_appinfo", "include_played_free_games", "appids_filter", "include_free_sub", "skip_unvetted_apps", "language", "include_extended_appinfo")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_APPINFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PLAYED_FREE_GAMES_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FILTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FREE_SUB_FIELD_NUMBER: _ClassVar[int]
    SKIP_UNVETTED_APPS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXTENDED_APPINFO_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_appinfo: bool
    include_played_free_games: bool
    appids_filter: _containers.RepeatedScalarFieldContainer[int]
    include_free_sub: bool
    skip_unvetted_apps: bool
    language: str
    include_extended_appinfo: bool
    def __init__(self, steamid: _Optional[int] = ..., include_appinfo: bool = ..., include_played_free_games: bool = ..., appids_filter: _Optional[_Iterable[int]] = ..., include_free_sub: bool = ..., skip_unvetted_apps: bool = ..., language: _Optional[str] = ..., include_extended_appinfo: bool = ...) -> None: ...

class CPlayer_GetOwnedGames_Response(_message.Message):
    __slots__ = ("game_count", "games")
    class Game(_message.Message):
        __slots__ = ("appid", "name", "playtime_2weeks", "playtime_forever", "img_icon_url", "has_community_visible_stats", "playtime_windows_forever", "playtime_mac_forever", "playtime_linux_forever", "playtime_deck_forever", "rtime_last_played", "capsule_filename", "sort_as", "has_workshop", "has_market", "has_dlc", "has_leaderboards", "content_descriptorids", "playtime_disconnected")
        APPID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_2WEEKS_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_FOREVER_FIELD_NUMBER: _ClassVar[int]
        IMG_ICON_URL_FIELD_NUMBER: _ClassVar[int]
        HAS_COMMUNITY_VISIBLE_STATS_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_WINDOWS_FOREVER_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_MAC_FOREVER_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_LINUX_FOREVER_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_DECK_FOREVER_FIELD_NUMBER: _ClassVar[int]
        RTIME_LAST_PLAYED_FIELD_NUMBER: _ClassVar[int]
        CAPSULE_FILENAME_FIELD_NUMBER: _ClassVar[int]
        SORT_AS_FIELD_NUMBER: _ClassVar[int]
        HAS_WORKSHOP_FIELD_NUMBER: _ClassVar[int]
        HAS_MARKET_FIELD_NUMBER: _ClassVar[int]
        HAS_DLC_FIELD_NUMBER: _ClassVar[int]
        HAS_LEADERBOARDS_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESCRIPTORIDS_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
        appid: int
        name: str
        playtime_2weeks: int
        playtime_forever: int
        img_icon_url: str
        has_community_visible_stats: bool
        playtime_windows_forever: int
        playtime_mac_forever: int
        playtime_linux_forever: int
        playtime_deck_forever: int
        rtime_last_played: int
        capsule_filename: str
        sort_as: str
        has_workshop: bool
        has_market: bool
        has_dlc: bool
        has_leaderboards: bool
        content_descriptorids: _containers.RepeatedScalarFieldContainer[int]
        playtime_disconnected: int
        def __init__(self, appid: _Optional[int] = ..., name: _Optional[str] = ..., playtime_2weeks: _Optional[int] = ..., playtime_forever: _Optional[int] = ..., img_icon_url: _Optional[str] = ..., has_community_visible_stats: bool = ..., playtime_windows_forever: _Optional[int] = ..., playtime_mac_forever: _Optional[int] = ..., playtime_linux_forever: _Optional[int] = ..., playtime_deck_forever: _Optional[int] = ..., rtime_last_played: _Optional[int] = ..., capsule_filename: _Optional[str] = ..., sort_as: _Optional[str] = ..., has_workshop: bool = ..., has_market: bool = ..., has_dlc: bool = ..., has_leaderboards: bool = ..., content_descriptorids: _Optional[_Iterable[int]] = ..., playtime_disconnected: _Optional[int] = ...) -> None: ...
    GAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    GAMES_FIELD_NUMBER: _ClassVar[int]
    game_count: int
    games: _containers.RepeatedCompositeFieldContainer[CPlayer_GetOwnedGames_Response.Game]
    def __init__(self, game_count: _Optional[int] = ..., games: _Optional[_Iterable[_Union[CPlayer_GetOwnedGames_Response.Game, _Mapping]]] = ...) -> None: ...

class CPlayer_GetPlayNext_Request(_message.Message):
    __slots__ = ("max_age_seconds", "ignore_appids")
    MAX_AGE_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_APPIDS_FIELD_NUMBER: _ClassVar[int]
    max_age_seconds: int
    ignore_appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, max_age_seconds: _Optional[int] = ..., ignore_appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CPlayer_GetPlayNext_Response(_message.Message):
    __slots__ = ("last_update_time", "appids")
    LAST_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    last_update_time: int
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, last_update_time: _Optional[int] = ..., appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CPlayer_GetFriendsGameplayInfo_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CPlayer_GetFriendsGameplayInfo_Response(_message.Message):
    __slots__ = ("your_info", "in_game", "played_recently", "played_ever", "owns", "in_wishlist")
    class FriendsGameplayInfo(_message.Message):
        __slots__ = ("steamid", "minutes_played", "minutes_played_forever")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        MINUTES_PLAYED_FIELD_NUMBER: _ClassVar[int]
        MINUTES_PLAYED_FOREVER_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        minutes_played: int
        minutes_played_forever: int
        def __init__(self, steamid: _Optional[int] = ..., minutes_played: _Optional[int] = ..., minutes_played_forever: _Optional[int] = ...) -> None: ...
    class OwnGameplayInfo(_message.Message):
        __slots__ = ("steamid", "minutes_played", "minutes_played_forever", "in_wishlist", "owned")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        MINUTES_PLAYED_FIELD_NUMBER: _ClassVar[int]
        MINUTES_PLAYED_FOREVER_FIELD_NUMBER: _ClassVar[int]
        IN_WISHLIST_FIELD_NUMBER: _ClassVar[int]
        OWNED_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        minutes_played: int
        minutes_played_forever: int
        in_wishlist: bool
        owned: bool
        def __init__(self, steamid: _Optional[int] = ..., minutes_played: _Optional[int] = ..., minutes_played_forever: _Optional[int] = ..., in_wishlist: bool = ..., owned: bool = ...) -> None: ...
    YOUR_INFO_FIELD_NUMBER: _ClassVar[int]
    IN_GAME_FIELD_NUMBER: _ClassVar[int]
    PLAYED_RECENTLY_FIELD_NUMBER: _ClassVar[int]
    PLAYED_EVER_FIELD_NUMBER: _ClassVar[int]
    OWNS_FIELD_NUMBER: _ClassVar[int]
    IN_WISHLIST_FIELD_NUMBER: _ClassVar[int]
    your_info: CPlayer_GetFriendsGameplayInfo_Response.OwnGameplayInfo
    in_game: _containers.RepeatedCompositeFieldContainer[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo]
    played_recently: _containers.RepeatedCompositeFieldContainer[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo]
    played_ever: _containers.RepeatedCompositeFieldContainer[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo]
    owns: _containers.RepeatedCompositeFieldContainer[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo]
    in_wishlist: _containers.RepeatedCompositeFieldContainer[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo]
    def __init__(self, your_info: _Optional[_Union[CPlayer_GetFriendsGameplayInfo_Response.OwnGameplayInfo, _Mapping]] = ..., in_game: _Optional[_Iterable[_Union[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo, _Mapping]]] = ..., played_recently: _Optional[_Iterable[_Union[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo, _Mapping]]] = ..., played_ever: _Optional[_Iterable[_Union[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo, _Mapping]]] = ..., owns: _Optional[_Iterable[_Union[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo, _Mapping]]] = ..., in_wishlist: _Optional[_Iterable[_Union[CPlayer_GetFriendsGameplayInfo_Response.FriendsGameplayInfo, _Mapping]]] = ...) -> None: ...

class CPlayer_GetGameBadgeLevels_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CPlayer_GetGameBadgeLevels_Response(_message.Message):
    __slots__ = ("player_level", "badges")
    class Badge(_message.Message):
        __slots__ = ("level", "series", "border_color")
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        SERIES_FIELD_NUMBER: _ClassVar[int]
        BORDER_COLOR_FIELD_NUMBER: _ClassVar[int]
        level: int
        series: int
        border_color: int
        def __init__(self, level: _Optional[int] = ..., series: _Optional[int] = ..., border_color: _Optional[int] = ...) -> None: ...
    PLAYER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    BADGES_FIELD_NUMBER: _ClassVar[int]
    player_level: int
    badges: _containers.RepeatedCompositeFieldContainer[CPlayer_GetGameBadgeLevels_Response.Badge]
    def __init__(self, player_level: _Optional[int] = ..., badges: _Optional[_Iterable[_Union[CPlayer_GetGameBadgeLevels_Response.Badge, _Mapping]]] = ...) -> None: ...

class CPlayer_GetProfileBackground_Request(_message.Message):
    __slots__ = ("steamid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class ProfileItem(_message.Message):
    __slots__ = ("communityitemid", "image_small", "image_large", "name", "item_title", "item_description", "appid", "item_type", "item_class", "movie_webm", "movie_mp4", "movie_webm_small", "movie_mp4_small", "equipped_flags", "profile_colors")
    class ProfileColor(_message.Message):
        __slots__ = ("style_name", "color")
        STYLE_NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        style_name: str
        color: str
        def __init__(self, style_name: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_SMALL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LARGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_TITLE_FIELD_NUMBER: _ClassVar[int]
    ITEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_CLASS_FIELD_NUMBER: _ClassVar[int]
    MOVIE_WEBM_FIELD_NUMBER: _ClassVar[int]
    MOVIE_MP4_FIELD_NUMBER: _ClassVar[int]
    MOVIE_WEBM_SMALL_FIELD_NUMBER: _ClassVar[int]
    MOVIE_MP4_SMALL_FIELD_NUMBER: _ClassVar[int]
    EQUIPPED_FLAGS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_COLORS_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    image_small: str
    image_large: str
    name: str
    item_title: str
    item_description: str
    appid: int
    item_type: int
    item_class: int
    movie_webm: str
    movie_mp4: str
    movie_webm_small: str
    movie_mp4_small: str
    equipped_flags: int
    profile_colors: _containers.RepeatedCompositeFieldContainer[ProfileItem.ProfileColor]
    def __init__(self, communityitemid: _Optional[int] = ..., image_small: _Optional[str] = ..., image_large: _Optional[str] = ..., name: _Optional[str] = ..., item_title: _Optional[str] = ..., item_description: _Optional[str] = ..., appid: _Optional[int] = ..., item_type: _Optional[int] = ..., item_class: _Optional[int] = ..., movie_webm: _Optional[str] = ..., movie_mp4: _Optional[str] = ..., movie_webm_small: _Optional[str] = ..., movie_mp4_small: _Optional[str] = ..., equipped_flags: _Optional[int] = ..., profile_colors: _Optional[_Iterable[_Union[ProfileItem.ProfileColor, _Mapping]]] = ...) -> None: ...

class CPlayer_GetProfileBackground_Response(_message.Message):
    __slots__ = ("profile_background",)
    PROFILE_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    profile_background: ProfileItem
    def __init__(self, profile_background: _Optional[_Union[ProfileItem, _Mapping]] = ...) -> None: ...

class CPlayer_SetProfileBackground_Request(_message.Message):
    __slots__ = ("communityitemid",)
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    def __init__(self, communityitemid: _Optional[int] = ...) -> None: ...

class CPlayer_SetProfileBackground_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetMiniProfileBackground_Request(_message.Message):
    __slots__ = ("steamid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CPlayer_GetMiniProfileBackground_Response(_message.Message):
    __slots__ = ("profile_background",)
    PROFILE_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    profile_background: ProfileItem
    def __init__(self, profile_background: _Optional[_Union[ProfileItem, _Mapping]] = ...) -> None: ...

class CPlayer_SetMiniProfileBackground_Request(_message.Message):
    __slots__ = ("communityitemid",)
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    def __init__(self, communityitemid: _Optional[int] = ...) -> None: ...

class CPlayer_SetMiniProfileBackground_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetAvatarFrame_Request(_message.Message):
    __slots__ = ("steamid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CPlayer_GetAvatarFrame_Response(_message.Message):
    __slots__ = ("avatar_frame",)
    AVATAR_FRAME_FIELD_NUMBER: _ClassVar[int]
    avatar_frame: ProfileItem
    def __init__(self, avatar_frame: _Optional[_Union[ProfileItem, _Mapping]] = ...) -> None: ...

class CPlayer_SetAvatarFrame_Request(_message.Message):
    __slots__ = ("communityitemid",)
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    def __init__(self, communityitemid: _Optional[int] = ...) -> None: ...

class CPlayer_SetAvatarFrame_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetAnimatedAvatar_Request(_message.Message):
    __slots__ = ("steamid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CPlayer_GetAnimatedAvatar_Response(_message.Message):
    __slots__ = ("avatar",)
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    avatar: ProfileItem
    def __init__(self, avatar: _Optional[_Union[ProfileItem, _Mapping]] = ...) -> None: ...

class CPlayer_SetAnimatedAvatar_Request(_message.Message):
    __slots__ = ("communityitemid",)
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    def __init__(self, communityitemid: _Optional[int] = ...) -> None: ...

class CPlayer_SetAnimatedAvatar_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetSteamDeckKeyboardSkin_Request(_message.Message):
    __slots__ = ("steamid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CPlayer_GetSteamDeckKeyboardSkin_Response(_message.Message):
    __slots__ = ("steam_deck_keyboard_skin",)
    STEAM_DECK_KEYBOARD_SKIN_FIELD_NUMBER: _ClassVar[int]
    steam_deck_keyboard_skin: ProfileItem
    def __init__(self, steam_deck_keyboard_skin: _Optional[_Union[ProfileItem, _Mapping]] = ...) -> None: ...

class CPlayer_SetSteamDeckKeyboardSkin_Request(_message.Message):
    __slots__ = ("communityitemid",)
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    def __init__(self, communityitemid: _Optional[int] = ...) -> None: ...

class CPlayer_SetSteamDeckKeyboardSkin_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetProfileItemsOwned_Request(_message.Message):
    __slots__ = ("language", "filters")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    language: str
    filters: _containers.RepeatedScalarFieldContainer[_enums_pb2.ECommunityItemClass]
    def __init__(self, language: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[_enums_pb2.ECommunityItemClass, str]]] = ...) -> None: ...

class CPlayer_GetProfileItemsOwned_Response(_message.Message):
    __slots__ = ("profile_backgrounds", "mini_profile_backgrounds", "avatar_frames", "animated_avatars", "profile_modifiers", "steam_deck_keyboard_skins", "steam_deck_startup_movies")
    PROFILE_BACKGROUNDS_FIELD_NUMBER: _ClassVar[int]
    MINI_PROFILE_BACKGROUNDS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FRAMES_FIELD_NUMBER: _ClassVar[int]
    ANIMATED_AVATARS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    STEAM_DECK_KEYBOARD_SKINS_FIELD_NUMBER: _ClassVar[int]
    STEAM_DECK_STARTUP_MOVIES_FIELD_NUMBER: _ClassVar[int]
    profile_backgrounds: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    mini_profile_backgrounds: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    avatar_frames: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    animated_avatars: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    profile_modifiers: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    steam_deck_keyboard_skins: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    steam_deck_startup_movies: _containers.RepeatedCompositeFieldContainer[ProfileItem]
    def __init__(self, profile_backgrounds: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ..., mini_profile_backgrounds: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ..., avatar_frames: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ..., animated_avatars: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ..., profile_modifiers: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ..., steam_deck_keyboard_skins: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ..., steam_deck_startup_movies: _Optional[_Iterable[_Union[ProfileItem, _Mapping]]] = ...) -> None: ...

class CPlayer_GetProfileItemsEquipped_Request(_message.Message):
    __slots__ = ("steamid", "language")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CPlayer_GetProfileItemsEquipped_Response(_message.Message):
    __slots__ = ("profile_background", "mini_profile_background", "avatar_frame", "animated_avatar", "profile_modifier", "steam_deck_keyboard_skin")
    PROFILE_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    MINI_PROFILE_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FRAME_FIELD_NUMBER: _ClassVar[int]
    ANIMATED_AVATAR_FIELD_NUMBER: _ClassVar[int]
    PROFILE_MODIFIER_FIELD_NUMBER: _ClassVar[int]
    STEAM_DECK_KEYBOARD_SKIN_FIELD_NUMBER: _ClassVar[int]
    profile_background: ProfileItem
    mini_profile_background: ProfileItem
    avatar_frame: ProfileItem
    animated_avatar: ProfileItem
    profile_modifier: ProfileItem
    steam_deck_keyboard_skin: ProfileItem
    def __init__(self, profile_background: _Optional[_Union[ProfileItem, _Mapping]] = ..., mini_profile_background: _Optional[_Union[ProfileItem, _Mapping]] = ..., avatar_frame: _Optional[_Union[ProfileItem, _Mapping]] = ..., animated_avatar: _Optional[_Union[ProfileItem, _Mapping]] = ..., profile_modifier: _Optional[_Union[ProfileItem, _Mapping]] = ..., steam_deck_keyboard_skin: _Optional[_Union[ProfileItem, _Mapping]] = ...) -> None: ...

class CPlayer_SetEquippedProfileItemFlags_Request(_message.Message):
    __slots__ = ("communityitemid", "flags")
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    flags: int
    def __init__(self, communityitemid: _Optional[int] = ..., flags: _Optional[int] = ...) -> None: ...

class CPlayer_SetEquippedProfileItemFlags_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetEmoticonList_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetEmoticonList_Response(_message.Message):
    __slots__ = ("emoticons",)
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
    EMOTICONS_FIELD_NUMBER: _ClassVar[int]
    emoticons: _containers.RepeatedCompositeFieldContainer[CPlayer_GetEmoticonList_Response.Emoticon]
    def __init__(self, emoticons: _Optional[_Iterable[_Union[CPlayer_GetEmoticonList_Response.Emoticon, _Mapping]]] = ...) -> None: ...

class CPlayer_GetCommunityBadgeProgress_Request(_message.Message):
    __slots__ = ("steamid", "badgeid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BADGEID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    badgeid: int
    def __init__(self, steamid: _Optional[int] = ..., badgeid: _Optional[int] = ...) -> None: ...

class CPlayer_GetCommunityBadgeProgress_Response(_message.Message):
    __slots__ = ("quests",)
    class Quest(_message.Message):
        __slots__ = ("questid", "completed")
        QUESTID_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        questid: int
        completed: bool
        def __init__(self, questid: _Optional[int] = ..., completed: bool = ...) -> None: ...
    QUESTS_FIELD_NUMBER: _ClassVar[int]
    quests: _containers.RepeatedCompositeFieldContainer[CPlayer_GetCommunityBadgeProgress_Response.Quest]
    def __init__(self, quests: _Optional[_Iterable[_Union[CPlayer_GetCommunityBadgeProgress_Response.Quest, _Mapping]]] = ...) -> None: ...

class CPlayer_GetTopAchievementsForGames_Request(_message.Message):
    __slots__ = ("steamid", "language", "max_achievements", "appids")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    max_achievements: int
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ..., max_achievements: _Optional[int] = ..., appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CPlayer_GetTopAchievementsForGames_Response(_message.Message):
    __slots__ = ("games",)
    class Achievement(_message.Message):
        __slots__ = ("statid", "bit", "name", "desc", "icon", "icon_gray", "hidden", "player_percent_unlocked")
        STATID_FIELD_NUMBER: _ClassVar[int]
        BIT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ICON_GRAY_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_PERCENT_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
        statid: int
        bit: int
        name: str
        desc: str
        icon: str
        icon_gray: str
        hidden: bool
        player_percent_unlocked: str
        def __init__(self, statid: _Optional[int] = ..., bit: _Optional[int] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., icon: _Optional[str] = ..., icon_gray: _Optional[str] = ..., hidden: bool = ..., player_percent_unlocked: _Optional[str] = ...) -> None: ...
    class Game(_message.Message):
        __slots__ = ("appid", "total_achievements", "achievements")
        APPID_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
        appid: int
        total_achievements: int
        achievements: _containers.RepeatedCompositeFieldContainer[CPlayer_GetTopAchievementsForGames_Response.Achievement]
        def __init__(self, appid: _Optional[int] = ..., total_achievements: _Optional[int] = ..., achievements: _Optional[_Iterable[_Union[CPlayer_GetTopAchievementsForGames_Response.Achievement, _Mapping]]] = ...) -> None: ...
    GAMES_FIELD_NUMBER: _ClassVar[int]
    games: _containers.RepeatedCompositeFieldContainer[CPlayer_GetTopAchievementsForGames_Response.Game]
    def __init__(self, games: _Optional[_Iterable[_Union[CPlayer_GetTopAchievementsForGames_Response.Game, _Mapping]]] = ...) -> None: ...

class CPlayer_GetAchievementsProgress_Request(_message.Message):
    __slots__ = ("steamid", "language", "appids", "include_unvetted_apps")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNVETTED_APPS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    language: str
    appids: _containers.RepeatedScalarFieldContainer[int]
    include_unvetted_apps: bool
    def __init__(self, steamid: _Optional[int] = ..., language: _Optional[str] = ..., appids: _Optional[_Iterable[int]] = ..., include_unvetted_apps: bool = ...) -> None: ...

class CPlayer_GetAchievementsProgress_Response(_message.Message):
    __slots__ = ("achievement_progress",)
    class AchievementProgress(_message.Message):
        __slots__ = ("appid", "unlocked", "total", "percentage", "all_unlocked", "cache_time", "vetted")
        APPID_FIELD_NUMBER: _ClassVar[int]
        UNLOCKED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        ALL_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
        CACHE_TIME_FIELD_NUMBER: _ClassVar[int]
        VETTED_FIELD_NUMBER: _ClassVar[int]
        appid: int
        unlocked: int
        total: int
        percentage: float
        all_unlocked: bool
        cache_time: int
        vetted: bool
        def __init__(self, appid: _Optional[int] = ..., unlocked: _Optional[int] = ..., total: _Optional[int] = ..., percentage: _Optional[float] = ..., all_unlocked: bool = ..., cache_time: _Optional[int] = ..., vetted: bool = ...) -> None: ...
    ACHIEVEMENT_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    achievement_progress: _containers.RepeatedCompositeFieldContainer[CPlayer_GetAchievementsProgress_Response.AchievementProgress]
    def __init__(self, achievement_progress: _Optional[_Iterable[_Union[CPlayer_GetAchievementsProgress_Response.AchievementProgress, _Mapping]]] = ...) -> None: ...

class CPlayer_GetGameAchievements_Request(_message.Message):
    __slots__ = ("appid", "language")
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    language: str
    def __init__(self, appid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CPlayer_GetGameAchievements_Response(_message.Message):
    __slots__ = ("achievements",)
    class Achievement(_message.Message):
        __slots__ = ("internal_name", "localized_name", "localized_desc", "icon", "icon_gray", "hidden", "player_percent_unlocked")
        INTERNAL_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCALIZED_NAME_FIELD_NUMBER: _ClassVar[int]
        LOCALIZED_DESC_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ICON_GRAY_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        PLAYER_PERCENT_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
        internal_name: str
        localized_name: str
        localized_desc: str
        icon: str
        icon_gray: str
        hidden: bool
        player_percent_unlocked: str
        def __init__(self, internal_name: _Optional[str] = ..., localized_name: _Optional[str] = ..., localized_desc: _Optional[str] = ..., icon: _Optional[str] = ..., icon_gray: _Optional[str] = ..., hidden: bool = ..., player_percent_unlocked: _Optional[str] = ...) -> None: ...
    ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    achievements: _containers.RepeatedCompositeFieldContainer[CPlayer_GetGameAchievements_Response.Achievement]
    def __init__(self, achievements: _Optional[_Iterable[_Union[CPlayer_GetGameAchievements_Response.Achievement, _Mapping]]] = ...) -> None: ...

class CPlayer_GetFavoriteBadge_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CPlayer_GetFavoriteBadge_Response(_message.Message):
    __slots__ = ("has_favorite_badge", "badgeid", "communityitemid", "item_type", "border_color", "appid", "level")
    HAS_FAVORITE_BADGE_FIELD_NUMBER: _ClassVar[int]
    BADGEID_FIELD_NUMBER: _ClassVar[int]
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    BORDER_COLOR_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    has_favorite_badge: bool
    badgeid: int
    communityitemid: int
    item_type: int
    border_color: int
    appid: int
    level: int
    def __init__(self, has_favorite_badge: bool = ..., badgeid: _Optional[int] = ..., communityitemid: _Optional[int] = ..., item_type: _Optional[int] = ..., border_color: _Optional[int] = ..., appid: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...

class CPlayer_SetFavoriteBadge_Request(_message.Message):
    __slots__ = ("communityitemid", "badgeid")
    COMMUNITYITEMID_FIELD_NUMBER: _ClassVar[int]
    BADGEID_FIELD_NUMBER: _ClassVar[int]
    communityitemid: int
    badgeid: int
    def __init__(self, communityitemid: _Optional[int] = ..., badgeid: _Optional[int] = ...) -> None: ...

class CPlayer_SetFavoriteBadge_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetProfileCustomization_Request(_message.Message):
    __slots__ = ("steamid", "include_inactive_customizations", "include_purchased_customizations")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PURCHASED_CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_inactive_customizations: bool
    include_purchased_customizations: bool
    def __init__(self, steamid: _Optional[int] = ..., include_inactive_customizations: bool = ..., include_purchased_customizations: bool = ...) -> None: ...

class ProfileCustomizationSlot(_message.Message):
    __slots__ = ("slot", "appid", "publishedfileid", "item_assetid", "item_contextid", "notes", "title", "accountid", "badgeid", "border_color", "item_classid", "item_instanceid", "ban_check_result", "replay_year")
    SLOT_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ASSETID_FIELD_NUMBER: _ClassVar[int]
    ITEM_CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    BADGEID_FIELD_NUMBER: _ClassVar[int]
    BORDER_COLOR_FIELD_NUMBER: _ClassVar[int]
    ITEM_CLASSID_FIELD_NUMBER: _ClassVar[int]
    ITEM_INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    BAN_CHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_YEAR_FIELD_NUMBER: _ClassVar[int]
    slot: int
    appid: int
    publishedfileid: int
    item_assetid: int
    item_contextid: int
    notes: str
    title: str
    accountid: int
    badgeid: int
    border_color: int
    item_classid: int
    item_instanceid: int
    ban_check_result: _steammessages_base_pb2.EBanContentCheckResult
    replay_year: int
    def __init__(self, slot: _Optional[int] = ..., appid: _Optional[int] = ..., publishedfileid: _Optional[int] = ..., item_assetid: _Optional[int] = ..., item_contextid: _Optional[int] = ..., notes: _Optional[str] = ..., title: _Optional[str] = ..., accountid: _Optional[int] = ..., badgeid: _Optional[int] = ..., border_color: _Optional[int] = ..., item_classid: _Optional[int] = ..., item_instanceid: _Optional[int] = ..., ban_check_result: _Optional[_Union[_steammessages_base_pb2.EBanContentCheckResult, str]] = ..., replay_year: _Optional[int] = ...) -> None: ...

class ProfileCustomization(_message.Message):
    __slots__ = ("customization_type", "large", "slots", "active", "customization_style", "purchaseid", "level")
    CUSTOMIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LARGE_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZATION_STYLE_FIELD_NUMBER: _ClassVar[int]
    PURCHASEID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    customization_type: _enums_pb2.EProfileCustomizationType
    large: bool
    slots: _containers.RepeatedCompositeFieldContainer[ProfileCustomizationSlot]
    active: bool
    customization_style: EProfileCustomizationStyle
    purchaseid: int
    level: int
    def __init__(self, customization_type: _Optional[_Union[_enums_pb2.EProfileCustomizationType, str]] = ..., large: bool = ..., slots: _Optional[_Iterable[_Union[ProfileCustomizationSlot, _Mapping]]] = ..., active: bool = ..., customization_style: _Optional[_Union[EProfileCustomizationStyle, str]] = ..., purchaseid: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...

class ProfileTheme(_message.Message):
    __slots__ = ("theme_id", "title")
    THEME_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    theme_id: str
    title: str
    def __init__(self, theme_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class ProfilePreferences(_message.Message):
    __slots__ = ("hide_profile_awards",)
    HIDE_PROFILE_AWARDS_FIELD_NUMBER: _ClassVar[int]
    hide_profile_awards: bool
    def __init__(self, hide_profile_awards: bool = ...) -> None: ...

class CPlayer_GetProfileCustomization_Response(_message.Message):
    __slots__ = ("customizations", "slots_available", "profile_theme", "purchased_customizations", "profile_preferences")
    class PurchasedCustomization(_message.Message):
        __slots__ = ("purchaseid", "customization_type", "level")
        PURCHASEID_FIELD_NUMBER: _ClassVar[int]
        CUSTOMIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        purchaseid: int
        customization_type: _enums_pb2.EProfileCustomizationType
        level: int
        def __init__(self, purchaseid: _Optional[int] = ..., customization_type: _Optional[_Union[_enums_pb2.EProfileCustomizationType, str]] = ..., level: _Optional[int] = ...) -> None: ...
    CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_THEME_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    customizations: _containers.RepeatedCompositeFieldContainer[ProfileCustomization]
    slots_available: int
    profile_theme: ProfileTheme
    purchased_customizations: _containers.RepeatedCompositeFieldContainer[CPlayer_GetProfileCustomization_Response.PurchasedCustomization]
    profile_preferences: ProfilePreferences
    def __init__(self, customizations: _Optional[_Iterable[_Union[ProfileCustomization, _Mapping]]] = ..., slots_available: _Optional[int] = ..., profile_theme: _Optional[_Union[ProfileTheme, _Mapping]] = ..., purchased_customizations: _Optional[_Iterable[_Union[CPlayer_GetProfileCustomization_Response.PurchasedCustomization, _Mapping]]] = ..., profile_preferences: _Optional[_Union[ProfilePreferences, _Mapping]] = ...) -> None: ...

class CPlayer_GetPurchasedProfileCustomizations_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CPlayer_GetPurchasedProfileCustomizations_Response(_message.Message):
    __slots__ = ("purchased_customizations",)
    class PurchasedCustomization(_message.Message):
        __slots__ = ("purchaseid", "customization_type")
        PURCHASEID_FIELD_NUMBER: _ClassVar[int]
        CUSTOMIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        purchaseid: int
        customization_type: _enums_pb2.EProfileCustomizationType
        def __init__(self, purchaseid: _Optional[int] = ..., customization_type: _Optional[_Union[_enums_pb2.EProfileCustomizationType, str]] = ...) -> None: ...
    PURCHASED_CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    purchased_customizations: _containers.RepeatedCompositeFieldContainer[CPlayer_GetPurchasedProfileCustomizations_Response.PurchasedCustomization]
    def __init__(self, purchased_customizations: _Optional[_Iterable[_Union[CPlayer_GetPurchasedProfileCustomizations_Response.PurchasedCustomization, _Mapping]]] = ...) -> None: ...

class CPlayer_GetPurchasedAndUpgradedProfileCustomizations_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CPlayer_GetPurchasedAndUpgradedProfileCustomizations_Response(_message.Message):
    __slots__ = ("purchased_customizations", "upgraded_customizations")
    class PurchasedCustomization(_message.Message):
        __slots__ = ("customization_type", "count")
        CUSTOMIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        customization_type: _enums_pb2.EProfileCustomizationType
        count: int
        def __init__(self, customization_type: _Optional[_Union[_enums_pb2.EProfileCustomizationType, str]] = ..., count: _Optional[int] = ...) -> None: ...
    class UpgradedCustomization(_message.Message):
        __slots__ = ("customization_type", "level")
        CUSTOMIZATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        customization_type: _enums_pb2.EProfileCustomizationType
        level: int
        def __init__(self, customization_type: _Optional[_Union[_enums_pb2.EProfileCustomizationType, str]] = ..., level: _Optional[int] = ...) -> None: ...
    PURCHASED_CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    UPGRADED_CUSTOMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    purchased_customizations: _containers.RepeatedCompositeFieldContainer[CPlayer_GetPurchasedAndUpgradedProfileCustomizations_Response.PurchasedCustomization]
    upgraded_customizations: _containers.RepeatedCompositeFieldContainer[CPlayer_GetPurchasedAndUpgradedProfileCustomizations_Response.UpgradedCustomization]
    def __init__(self, purchased_customizations: _Optional[_Iterable[_Union[CPlayer_GetPurchasedAndUpgradedProfileCustomizations_Response.PurchasedCustomization, _Mapping]]] = ..., upgraded_customizations: _Optional[_Iterable[_Union[CPlayer_GetPurchasedAndUpgradedProfileCustomizations_Response.UpgradedCustomization, _Mapping]]] = ...) -> None: ...

class CPlayer_GetProfileThemesAvailable_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetProfileThemesAvailable_Response(_message.Message):
    __slots__ = ("profile_themes",)
    PROFILE_THEMES_FIELD_NUMBER: _ClassVar[int]
    profile_themes: _containers.RepeatedCompositeFieldContainer[ProfileTheme]
    def __init__(self, profile_themes: _Optional[_Iterable[_Union[ProfileTheme, _Mapping]]] = ...) -> None: ...

class CPlayer_SetProfileTheme_Request(_message.Message):
    __slots__ = ("theme_id",)
    THEME_ID_FIELD_NUMBER: _ClassVar[int]
    theme_id: str
    def __init__(self, theme_id: _Optional[str] = ...) -> None: ...

class CPlayer_SetProfileTheme_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_SetProfilePreferences_Request(_message.Message):
    __slots__ = ("profile_preferences",)
    PROFILE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    profile_preferences: ProfilePreferences
    def __init__(self, profile_preferences: _Optional[_Union[ProfilePreferences, _Mapping]] = ...) -> None: ...

class CPlayer_SetProfilePreferences_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_PostStatusToFriends_Request(_message.Message):
    __slots__ = ("appid", "status_text")
    APPID_FIELD_NUMBER: _ClassVar[int]
    STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    status_text: str
    def __init__(self, appid: _Optional[int] = ..., status_text: _Optional[str] = ...) -> None: ...

class CPlayer_PostStatusToFriends_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetPostedStatus_Request(_message.Message):
    __slots__ = ("steamid", "postid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    postid: int
    def __init__(self, steamid: _Optional[int] = ..., postid: _Optional[int] = ...) -> None: ...

class CPlayer_GetPostedStatus_Response(_message.Message):
    __slots__ = ("accountid", "postid", "status_text", "deleted", "appid")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    POSTID_FIELD_NUMBER: _ClassVar[int]
    STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    postid: int
    status_text: str
    deleted: bool
    appid: int
    def __init__(self, accountid: _Optional[int] = ..., postid: _Optional[int] = ..., status_text: _Optional[str] = ..., deleted: bool = ..., appid: _Optional[int] = ...) -> None: ...

class CPlayer_DeletePostedStatus_Request(_message.Message):
    __slots__ = ("postid",)
    POSTID_FIELD_NUMBER: _ClassVar[int]
    postid: int
    def __init__(self, postid: _Optional[int] = ...) -> None: ...

class CPlayer_DeletePostedStatus_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetLastPlayedTimes_Request(_message.Message):
    __slots__ = ("min_last_played",)
    MIN_LAST_PLAYED_FIELD_NUMBER: _ClassVar[int]
    min_last_played: int
    def __init__(self, min_last_played: _Optional[int] = ...) -> None: ...

class CPlayer_GetLastPlayedTimes_Response(_message.Message):
    __slots__ = ("games",)
    class Game(_message.Message):
        __slots__ = ("appid", "last_playtime", "playtime_2weeks", "playtime_forever", "first_playtime", "playtime_windows_forever", "playtime_mac_forever", "playtime_linux_forever", "playtime_deck_forever", "first_windows_playtime", "first_mac_playtime", "first_linux_playtime", "first_deck_playtime", "last_windows_playtime", "last_mac_playtime", "last_linux_playtime", "last_deck_playtime", "playtime_disconnected")
        APPID_FIELD_NUMBER: _ClassVar[int]
        LAST_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_2WEEKS_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_FOREVER_FIELD_NUMBER: _ClassVar[int]
        FIRST_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_WINDOWS_FOREVER_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_MAC_FOREVER_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_LINUX_FOREVER_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_DECK_FOREVER_FIELD_NUMBER: _ClassVar[int]
        FIRST_WINDOWS_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        FIRST_MAC_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        FIRST_LINUX_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        FIRST_DECK_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        LAST_WINDOWS_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        LAST_MAC_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        LAST_LINUX_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        LAST_DECK_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
        appid: int
        last_playtime: int
        playtime_2weeks: int
        playtime_forever: int
        first_playtime: int
        playtime_windows_forever: int
        playtime_mac_forever: int
        playtime_linux_forever: int
        playtime_deck_forever: int
        first_windows_playtime: int
        first_mac_playtime: int
        first_linux_playtime: int
        first_deck_playtime: int
        last_windows_playtime: int
        last_mac_playtime: int
        last_linux_playtime: int
        last_deck_playtime: int
        playtime_disconnected: int
        def __init__(self, appid: _Optional[int] = ..., last_playtime: _Optional[int] = ..., playtime_2weeks: _Optional[int] = ..., playtime_forever: _Optional[int] = ..., first_playtime: _Optional[int] = ..., playtime_windows_forever: _Optional[int] = ..., playtime_mac_forever: _Optional[int] = ..., playtime_linux_forever: _Optional[int] = ..., playtime_deck_forever: _Optional[int] = ..., first_windows_playtime: _Optional[int] = ..., first_mac_playtime: _Optional[int] = ..., first_linux_playtime: _Optional[int] = ..., first_deck_playtime: _Optional[int] = ..., last_windows_playtime: _Optional[int] = ..., last_mac_playtime: _Optional[int] = ..., last_linux_playtime: _Optional[int] = ..., last_deck_playtime: _Optional[int] = ..., playtime_disconnected: _Optional[int] = ...) -> None: ...
    GAMES_FIELD_NUMBER: _ClassVar[int]
    games: _containers.RepeatedCompositeFieldContainer[CPlayer_GetLastPlayedTimes_Response.Game]
    def __init__(self, games: _Optional[_Iterable[_Union[CPlayer_GetLastPlayedTimes_Response.Game, _Mapping]]] = ...) -> None: ...

class CPlayer_GetTimeSSAAccepted_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetTimeSSAAccepted_Response(_message.Message):
    __slots__ = ("time_ssa_accepted", "time_ssa_updated", "time_chinassa_accepted")
    TIME_SSA_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    TIME_SSA_UPDATED_FIELD_NUMBER: _ClassVar[int]
    TIME_CHINASSA_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    time_ssa_accepted: int
    time_ssa_updated: int
    time_chinassa_accepted: int
    def __init__(self, time_ssa_accepted: _Optional[int] = ..., time_ssa_updated: _Optional[int] = ..., time_chinassa_accepted: _Optional[int] = ...) -> None: ...

class CPlayer_AcceptSSA_Request(_message.Message):
    __slots__ = ("agreement_type", "time_signed_utc")
    AGREEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIME_SIGNED_UTC_FIELD_NUMBER: _ClassVar[int]
    agreement_type: EAgreementType
    time_signed_utc: int
    def __init__(self, agreement_type: _Optional[_Union[EAgreementType, str]] = ..., time_signed_utc: _Optional[int] = ...) -> None: ...

class CPlayer_AcceptSSA_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetNicknameList_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetNicknameList_Response(_message.Message):
    __slots__ = ("nicknames",)
    class PlayerNickname(_message.Message):
        __slots__ = ("accountid", "nickname")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        NICKNAME_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        nickname: str
        def __init__(self, accountid: _Optional[int] = ..., nickname: _Optional[str] = ...) -> None: ...
    NICKNAMES_FIELD_NUMBER: _ClassVar[int]
    nicknames: _containers.RepeatedCompositeFieldContainer[CPlayer_GetNicknameList_Response.PlayerNickname]
    def __init__(self, nicknames: _Optional[_Iterable[_Union[CPlayer_GetNicknameList_Response.PlayerNickname, _Mapping]]] = ...) -> None: ...

class CPlayer_GetPerFriendPreferences_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PerFriendPreferences(_message.Message):
    __slots__ = ("accountid", "nickname", "notifications_showingame", "notifications_showonline", "notifications_showmessages", "sounds_showingame", "sounds_showonline", "sounds_showmessages", "notifications_sendmobile")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_SHOWINGAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_SHOWONLINE_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_SHOWMESSAGES_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_SHOWINGAME_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_SHOWONLINE_FIELD_NUMBER: _ClassVar[int]
    SOUNDS_SHOWMESSAGES_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_SENDMOBILE_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    nickname: str
    notifications_showingame: ENotificationSetting
    notifications_showonline: ENotificationSetting
    notifications_showmessages: ENotificationSetting
    sounds_showingame: ENotificationSetting
    sounds_showonline: ENotificationSetting
    sounds_showmessages: ENotificationSetting
    notifications_sendmobile: ENotificationSetting
    def __init__(self, accountid: _Optional[int] = ..., nickname: _Optional[str] = ..., notifications_showingame: _Optional[_Union[ENotificationSetting, str]] = ..., notifications_showonline: _Optional[_Union[ENotificationSetting, str]] = ..., notifications_showmessages: _Optional[_Union[ENotificationSetting, str]] = ..., sounds_showingame: _Optional[_Union[ENotificationSetting, str]] = ..., sounds_showonline: _Optional[_Union[ENotificationSetting, str]] = ..., sounds_showmessages: _Optional[_Union[ENotificationSetting, str]] = ..., notifications_sendmobile: _Optional[_Union[ENotificationSetting, str]] = ...) -> None: ...

class CPlayer_GetPerFriendPreferences_Response(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: _containers.RepeatedCompositeFieldContainer[PerFriendPreferences]
    def __init__(self, preferences: _Optional[_Iterable[_Union[PerFriendPreferences, _Mapping]]] = ...) -> None: ...

class CPlayer_SetPerFriendPreferences_Request(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: PerFriendPreferences
    def __init__(self, preferences: _Optional[_Union[PerFriendPreferences, _Mapping]] = ...) -> None: ...

class CPlayer_SetPerFriendPreferences_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_AddFriend_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CPlayer_AddFriend_Response(_message.Message):
    __slots__ = ("invite_sent", "friend_relationship", "result")
    INVITE_SENT_FIELD_NUMBER: _ClassVar[int]
    FRIEND_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    invite_sent: bool
    friend_relationship: int
    result: int
    def __init__(self, invite_sent: bool = ..., friend_relationship: _Optional[int] = ..., result: _Optional[int] = ...) -> None: ...

class CPlayer_RemoveFriend_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CPlayer_RemoveFriend_Response(_message.Message):
    __slots__ = ("friend_relationship",)
    FRIEND_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    friend_relationship: int
    def __init__(self, friend_relationship: _Optional[int] = ...) -> None: ...

class CPlayer_IgnoreFriend_Request(_message.Message):
    __slots__ = ("steamid", "unignore")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    UNIGNORE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    unignore: bool
    def __init__(self, steamid: _Optional[int] = ..., unignore: bool = ...) -> None: ...

class CPlayer_IgnoreFriend_Response(_message.Message):
    __slots__ = ("friend_relationship",)
    FRIEND_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    friend_relationship: int
    def __init__(self, friend_relationship: _Optional[int] = ...) -> None: ...

class CPlayer_GetCommunityPreferences_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_CommunityPreferences(_message.Message):
    __slots__ = ("parenthesize_nicknames", "text_filter_setting", "text_filter_ignore_friends", "text_filter_words_revision", "timestamp_updated")
    PARENTHESIZE_NICKNAMES_FIELD_NUMBER: _ClassVar[int]
    TEXT_FILTER_SETTING_FIELD_NUMBER: _ClassVar[int]
    TEXT_FILTER_IGNORE_FRIENDS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FILTER_WORDS_REVISION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UPDATED_FIELD_NUMBER: _ClassVar[int]
    parenthesize_nicknames: bool
    text_filter_setting: ETextFilterSetting
    text_filter_ignore_friends: bool
    text_filter_words_revision: int
    timestamp_updated: int
    def __init__(self, parenthesize_nicknames: bool = ..., text_filter_setting: _Optional[_Union[ETextFilterSetting, str]] = ..., text_filter_ignore_friends: bool = ..., text_filter_words_revision: _Optional[int] = ..., timestamp_updated: _Optional[int] = ...) -> None: ...

class CPlayer_GetCommunityPreferences_Response(_message.Message):
    __slots__ = ("preferences", "content_descriptor_preferences")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTOR_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: CPlayer_CommunityPreferences
    content_descriptor_preferences: _steammessages_base_pb2.UserContentDescriptorPreferences
    def __init__(self, preferences: _Optional[_Union[CPlayer_CommunityPreferences, _Mapping]] = ..., content_descriptor_preferences: _Optional[_Union[_steammessages_base_pb2.UserContentDescriptorPreferences, _Mapping]] = ...) -> None: ...

class CPlayer_SetCommunityPreferences_Request(_message.Message):
    __slots__ = ("preferences",)
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: CPlayer_CommunityPreferences
    def __init__(self, preferences: _Optional[_Union[CPlayer_CommunityPreferences, _Mapping]] = ...) -> None: ...

class CPlayer_SetCommunityPreferences_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetTextFilterWords_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_TextFilterWords(_message.Message):
    __slots__ = ("text_filter_custom_banned_words", "text_filter_custom_clean_words", "text_filter_words_revision")
    TEXT_FILTER_CUSTOM_BANNED_WORDS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FILTER_CUSTOM_CLEAN_WORDS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FILTER_WORDS_REVISION_FIELD_NUMBER: _ClassVar[int]
    text_filter_custom_banned_words: _containers.RepeatedScalarFieldContainer[str]
    text_filter_custom_clean_words: _containers.RepeatedScalarFieldContainer[str]
    text_filter_words_revision: int
    def __init__(self, text_filter_custom_banned_words: _Optional[_Iterable[str]] = ..., text_filter_custom_clean_words: _Optional[_Iterable[str]] = ..., text_filter_words_revision: _Optional[int] = ...) -> None: ...

class CPlayer_GetTextFilterWords_Response(_message.Message):
    __slots__ = ("words",)
    WORDS_FIELD_NUMBER: _ClassVar[int]
    words: CPlayer_TextFilterWords
    def __init__(self, words: _Optional[_Union[CPlayer_TextFilterWords, _Mapping]] = ...) -> None: ...

class CPlayer_GetNewSteamAnnouncementState_Request(_message.Message):
    __slots__ = ("language",)
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: int
    def __init__(self, language: _Optional[int] = ...) -> None: ...

class CPlayer_GetNewSteamAnnouncementState_Response(_message.Message):
    __slots__ = ("state", "announcement_headline", "announcement_url", "time_posted", "announcement_gid")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_URL_FIELD_NUMBER: _ClassVar[int]
    TIME_POSTED_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_GID_FIELD_NUMBER: _ClassVar[int]
    state: _enums_pb2.ENewSteamAnnouncementState
    announcement_headline: str
    announcement_url: str
    time_posted: int
    announcement_gid: int
    def __init__(self, state: _Optional[_Union[_enums_pb2.ENewSteamAnnouncementState, str]] = ..., announcement_headline: _Optional[str] = ..., announcement_url: _Optional[str] = ..., time_posted: _Optional[int] = ..., announcement_gid: _Optional[int] = ...) -> None: ...

class CPlayer_UpdateSteamAnnouncementLastRead_Request(_message.Message):
    __slots__ = ("announcement_gid", "time_posted")
    ANNOUNCEMENT_GID_FIELD_NUMBER: _ClassVar[int]
    TIME_POSTED_FIELD_NUMBER: _ClassVar[int]
    announcement_gid: int
    time_posted: int
    def __init__(self, announcement_gid: _Optional[int] = ..., time_posted: _Optional[int] = ...) -> None: ...

class CPlayer_UpdateSteamAnnouncementLastRead_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_GetPrivacySettings_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPrivacySettings(_message.Message):
    __slots__ = ("privacy_state", "privacy_state_inventory", "privacy_state_gifts", "privacy_state_ownedgames", "privacy_state_playtime", "privacy_state_friendslist")
    PRIVACY_STATE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_STATE_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_STATE_GIFTS_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_STATE_OWNEDGAMES_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_STATE_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_STATE_FRIENDSLIST_FIELD_NUMBER: _ClassVar[int]
    privacy_state: int
    privacy_state_inventory: int
    privacy_state_gifts: int
    privacy_state_ownedgames: int
    privacy_state_playtime: int
    privacy_state_friendslist: int
    def __init__(self, privacy_state: _Optional[int] = ..., privacy_state_inventory: _Optional[int] = ..., privacy_state_gifts: _Optional[int] = ..., privacy_state_ownedgames: _Optional[int] = ..., privacy_state_playtime: _Optional[int] = ..., privacy_state_friendslist: _Optional[int] = ...) -> None: ...

class CPlayer_GetPrivacySettings_Response(_message.Message):
    __slots__ = ("privacy_settings",)
    PRIVACY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    privacy_settings: CPrivacySettings
    def __init__(self, privacy_settings: _Optional[_Union[CPrivacySettings, _Mapping]] = ...) -> None: ...

class CPlayer_GetDurationControl_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CPlayer_GetDurationControl_Response(_message.Message):
    __slots__ = ("is_enabled", "seconds", "seconds_today", "is_steamchina_account", "is_age_verified", "seconds_allowed_today", "age_verification_pending", "block_minors")
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_TODAY_FIELD_NUMBER: _ClassVar[int]
    IS_STEAMCHINA_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    IS_AGE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    SECONDS_ALLOWED_TODAY_FIELD_NUMBER: _ClassVar[int]
    AGE_VERIFICATION_PENDING_FIELD_NUMBER: _ClassVar[int]
    BLOCK_MINORS_FIELD_NUMBER: _ClassVar[int]
    is_enabled: bool
    seconds: int
    seconds_today: int
    is_steamchina_account: bool
    is_age_verified: bool
    seconds_allowed_today: int
    age_verification_pending: bool
    block_minors: bool
    def __init__(self, is_enabled: bool = ..., seconds: _Optional[int] = ..., seconds_today: _Optional[int] = ..., is_steamchina_account: bool = ..., is_age_verified: bool = ..., seconds_allowed_today: _Optional[int] = ..., age_verification_pending: bool = ..., block_minors: bool = ...) -> None: ...

class CPlayer_RecordDisconnectedPlaytime_Request(_message.Message):
    __slots__ = ("play_sessions",)
    class PlayHistory(_message.Message):
        __slots__ = ("appid", "session_time_start", "seconds", "offline", "owner")
        APPID_FIELD_NUMBER: _ClassVar[int]
        SESSION_TIME_START_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        OFFLINE_FIELD_NUMBER: _ClassVar[int]
        OWNER_FIELD_NUMBER: _ClassVar[int]
        appid: int
        session_time_start: int
        seconds: int
        offline: bool
        owner: int
        def __init__(self, appid: _Optional[int] = ..., session_time_start: _Optional[int] = ..., seconds: _Optional[int] = ..., offline: bool = ..., owner: _Optional[int] = ...) -> None: ...
    PLAY_SESSIONS_FIELD_NUMBER: _ClassVar[int]
    play_sessions: _containers.RepeatedCompositeFieldContainer[CPlayer_RecordDisconnectedPlaytime_Request.PlayHistory]
    def __init__(self, play_sessions: _Optional[_Iterable[_Union[CPlayer_RecordDisconnectedPlaytime_Request.PlayHistory, _Mapping]]] = ...) -> None: ...

class CPlayer_RecordDisconnectedPlaytime_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPlayer_LastPlayedTimes_Notification(_message.Message):
    __slots__ = ("games",)
    GAMES_FIELD_NUMBER: _ClassVar[int]
    games: _containers.RepeatedCompositeFieldContainer[CPlayer_GetLastPlayedTimes_Response.Game]
    def __init__(self, games: _Optional[_Iterable[_Union[CPlayer_GetLastPlayedTimes_Response.Game, _Mapping]]] = ...) -> None: ...

class CPlayer_FriendNicknameChanged_Notification(_message.Message):
    __slots__ = ("accountid", "nickname", "is_echo_to_self")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    IS_ECHO_TO_SELF_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    nickname: str
    is_echo_to_self: bool
    def __init__(self, accountid: _Optional[int] = ..., nickname: _Optional[str] = ..., is_echo_to_self: bool = ...) -> None: ...

class CPlayer_FriendEquippedProfileItemsChanged_Notification(_message.Message):
    __slots__ = ("accountid",)
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    def __init__(self, accountid: _Optional[int] = ...) -> None: ...

class CPlayer_NewSteamAnnouncementState_Notification(_message.Message):
    __slots__ = ("state", "announcement_headline", "announcement_url", "time_posted", "announcement_gid")
    STATE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_URL_FIELD_NUMBER: _ClassVar[int]
    TIME_POSTED_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_GID_FIELD_NUMBER: _ClassVar[int]
    state: _enums_pb2.ENewSteamAnnouncementState
    announcement_headline: str
    announcement_url: str
    time_posted: int
    announcement_gid: int
    def __init__(self, state: _Optional[_Union[_enums_pb2.ENewSteamAnnouncementState, str]] = ..., announcement_headline: _Optional[str] = ..., announcement_url: _Optional[str] = ..., time_posted: _Optional[int] = ..., announcement_gid: _Optional[int] = ...) -> None: ...

class CPlayer_CommunityPreferencesChanged_Notification(_message.Message):
    __slots__ = ("preferences", "content_descriptor_preferences")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTOR_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: CPlayer_CommunityPreferences
    content_descriptor_preferences: _steammessages_base_pb2.UserContentDescriptorPreferences
    def __init__(self, preferences: _Optional[_Union[CPlayer_CommunityPreferences, _Mapping]] = ..., content_descriptor_preferences: _Optional[_Union[_steammessages_base_pb2.UserContentDescriptorPreferences, _Mapping]] = ...) -> None: ...

class CPlayer_TextFilterWordsChanged_Notification(_message.Message):
    __slots__ = ("words",)
    WORDS_FIELD_NUMBER: _ClassVar[int]
    words: CPlayer_TextFilterWords
    def __init__(self, words: _Optional[_Union[CPlayer_TextFilterWords, _Mapping]] = ...) -> None: ...

class CPlayer_PerFriendPreferencesChanged_Notification(_message.Message):
    __slots__ = ("accountid", "preferences")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    preferences: PerFriendPreferences
    def __init__(self, accountid: _Optional[int] = ..., preferences: _Optional[_Union[PerFriendPreferences, _Mapping]] = ...) -> None: ...

class CPlayer_PrivacySettingsChanged_Notification(_message.Message):
    __slots__ = ("privacy_settings",)
    PRIVACY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    privacy_settings: CPrivacySettings
    def __init__(self, privacy_settings: _Optional[_Union[CPrivacySettings, _Mapping]] = ...) -> None: ...

class Player(_service.service): ...

class Player_Stub(Player): ...

class PlayerClient(_service.service): ...

class PlayerClient_Stub(PlayerClient): ...
