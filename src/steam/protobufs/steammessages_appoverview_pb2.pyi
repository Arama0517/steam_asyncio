import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EDisplayStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EDisplayStatusInvalid: _ClassVar[EDisplayStatus]
    k_EDisplayStatusLaunching: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUninstalling: _ClassVar[EDisplayStatus]
    k_EDisplayStatusInstalling: _ClassVar[EDisplayStatus]
    k_EDisplayStatusRunning: _ClassVar[EDisplayStatus]
    k_EDisplayStatusValidating: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUpdating: _ClassVar[EDisplayStatus]
    k_EDisplayStatusDownloading: _ClassVar[EDisplayStatus]
    k_EDisplayStatusSynchronizing: _ClassVar[EDisplayStatus]
    k_EDisplayStatusReadyToInstall: _ClassVar[EDisplayStatus]
    k_EDisplayStatusReadyToPreload: _ClassVar[EDisplayStatus]
    k_EDisplayStatusReadyToLaunch: _ClassVar[EDisplayStatus]
    k_EDisplayStatusRegionRestricted: _ClassVar[EDisplayStatus]
    k_EDisplayStatusPresaleOnly: _ClassVar[EDisplayStatus]
    k_EDisplayStatusInvalidPlatform: _ClassVar[EDisplayStatus]
    k_EDisplayStatusPreloadComplete: _ClassVar[EDisplayStatus]
    k_EDisplayStatusBorrowerLocked: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUpdatePaused: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUpdateQueued: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUpdateRequired: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUpdateDisabled: _ClassVar[EDisplayStatus]
    k_EDisplayStatusDownloadPaused: _ClassVar[EDisplayStatus]
    k_EDisplayStatusDownloadQueued: _ClassVar[EDisplayStatus]
    k_EDisplayStatusDownloadRequired: _ClassVar[EDisplayStatus]
    k_EDisplayStatusDownloadDisabled: _ClassVar[EDisplayStatus]
    k_EDisplayStatusLicensePending: _ClassVar[EDisplayStatus]
    k_EDisplayStatusLicenseExpired: _ClassVar[EDisplayStatus]
    k_EDisplayStatusAvailForFree: _ClassVar[EDisplayStatus]
    k_EDisplayStatusAvailToBorrow: _ClassVar[EDisplayStatus]
    k_EDisplayStatusAvailGuestPass: _ClassVar[EDisplayStatus]
    k_EDisplayStatusPurchase: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUnavailable: _ClassVar[EDisplayStatus]
    k_EDisplayStatusNotLaunchable: _ClassVar[EDisplayStatus]
    k_EDisplayStatusCloudError: _ClassVar[EDisplayStatus]
    k_EDisplayStatusCloudOutOfDate: _ClassVar[EDisplayStatus]
    k_EDisplayStatusTerminating: _ClassVar[EDisplayStatus]
    k_EDisplayStatusOwnerLocked: _ClassVar[EDisplayStatus]
    k_EDisplayStatusDownloadFailed: _ClassVar[EDisplayStatus]
    k_EDisplayStatusUpdateFailed: _ClassVar[EDisplayStatus]

class EAppCloudStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAppCloudStatusInvalid: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusDisabled: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusUnknown: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusSynchronized: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusChecking: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusOutOfSync: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusUploading: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusDownloading: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusSyncFailed: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusConflict: _ClassVar[EAppCloudStatus]
    k_EAppCloudStatusPendingElsewhere: _ClassVar[EAppCloudStatus]

class EAppControllerSupportLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAppControllerSupportLevelNone: _ClassVar[EAppControllerSupportLevel]
    k_EAppControllerSupportLevelPartial: _ClassVar[EAppControllerSupportLevel]
    k_EAppControllerSupportLevelFull: _ClassVar[EAppControllerSupportLevel]

class EAppGamepadGyroTrackpadSupportLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAppGamepadGyroTrackpadSupportLevelUnknown: _ClassVar[EAppGamepadGyroTrackpadSupportLevel]
    k_EAppGamepadGyroTrackpadSupportLevelNoGamepad: _ClassVar[EAppGamepadGyroTrackpadSupportLevel]
    k_EAppGamepadGyroTrackpadSupportLevelGamepad: _ClassVar[EAppGamepadGyroTrackpadSupportLevel]
    k_EAppGamepadGyroTrackpadSupportLevelSimultaneous: _ClassVar[EAppGamepadGyroTrackpadSupportLevel]

class EAppHDRSupport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EHDRSupport_Unknown: _ClassVar[EAppHDRSupport]
    k_EHDRSupport_SDR: _ClassVar[EAppHDRSupport]
    k_EHDRSupport_HDR: _ClassVar[EAppHDRSupport]
    k_EHDRSupport_HDR_Broken: _ClassVar[EAppHDRSupport]
    k_EHDRSupport_HDR_RequiresUserAction: _ClassVar[EAppHDRSupport]
k_EDisplayStatusInvalid: EDisplayStatus
k_EDisplayStatusLaunching: EDisplayStatus
k_EDisplayStatusUninstalling: EDisplayStatus
k_EDisplayStatusInstalling: EDisplayStatus
k_EDisplayStatusRunning: EDisplayStatus
k_EDisplayStatusValidating: EDisplayStatus
k_EDisplayStatusUpdating: EDisplayStatus
k_EDisplayStatusDownloading: EDisplayStatus
k_EDisplayStatusSynchronizing: EDisplayStatus
k_EDisplayStatusReadyToInstall: EDisplayStatus
k_EDisplayStatusReadyToPreload: EDisplayStatus
k_EDisplayStatusReadyToLaunch: EDisplayStatus
k_EDisplayStatusRegionRestricted: EDisplayStatus
k_EDisplayStatusPresaleOnly: EDisplayStatus
k_EDisplayStatusInvalidPlatform: EDisplayStatus
k_EDisplayStatusPreloadComplete: EDisplayStatus
k_EDisplayStatusBorrowerLocked: EDisplayStatus
k_EDisplayStatusUpdatePaused: EDisplayStatus
k_EDisplayStatusUpdateQueued: EDisplayStatus
k_EDisplayStatusUpdateRequired: EDisplayStatus
k_EDisplayStatusUpdateDisabled: EDisplayStatus
k_EDisplayStatusDownloadPaused: EDisplayStatus
k_EDisplayStatusDownloadQueued: EDisplayStatus
k_EDisplayStatusDownloadRequired: EDisplayStatus
k_EDisplayStatusDownloadDisabled: EDisplayStatus
k_EDisplayStatusLicensePending: EDisplayStatus
k_EDisplayStatusLicenseExpired: EDisplayStatus
k_EDisplayStatusAvailForFree: EDisplayStatus
k_EDisplayStatusAvailToBorrow: EDisplayStatus
k_EDisplayStatusAvailGuestPass: EDisplayStatus
k_EDisplayStatusPurchase: EDisplayStatus
k_EDisplayStatusUnavailable: EDisplayStatus
k_EDisplayStatusNotLaunchable: EDisplayStatus
k_EDisplayStatusCloudError: EDisplayStatus
k_EDisplayStatusCloudOutOfDate: EDisplayStatus
k_EDisplayStatusTerminating: EDisplayStatus
k_EDisplayStatusOwnerLocked: EDisplayStatus
k_EDisplayStatusDownloadFailed: EDisplayStatus
k_EDisplayStatusUpdateFailed: EDisplayStatus
k_EAppCloudStatusInvalid: EAppCloudStatus
k_EAppCloudStatusDisabled: EAppCloudStatus
k_EAppCloudStatusUnknown: EAppCloudStatus
k_EAppCloudStatusSynchronized: EAppCloudStatus
k_EAppCloudStatusChecking: EAppCloudStatus
k_EAppCloudStatusOutOfSync: EAppCloudStatus
k_EAppCloudStatusUploading: EAppCloudStatus
k_EAppCloudStatusDownloading: EAppCloudStatus
k_EAppCloudStatusSyncFailed: EAppCloudStatus
k_EAppCloudStatusConflict: EAppCloudStatus
k_EAppCloudStatusPendingElsewhere: EAppCloudStatus
k_EAppControllerSupportLevelNone: EAppControllerSupportLevel
k_EAppControllerSupportLevelPartial: EAppControllerSupportLevel
k_EAppControllerSupportLevelFull: EAppControllerSupportLevel
k_EAppGamepadGyroTrackpadSupportLevelUnknown: EAppGamepadGyroTrackpadSupportLevel
k_EAppGamepadGyroTrackpadSupportLevelNoGamepad: EAppGamepadGyroTrackpadSupportLevel
k_EAppGamepadGyroTrackpadSupportLevelGamepad: EAppGamepadGyroTrackpadSupportLevel
k_EAppGamepadGyroTrackpadSupportLevelSimultaneous: EAppGamepadGyroTrackpadSupportLevel
k_EHDRSupport_Unknown: EAppHDRSupport
k_EHDRSupport_SDR: EAppHDRSupport
k_EHDRSupport_HDR: EAppHDRSupport
k_EHDRSupport_HDR_Broken: EAppHDRSupport
k_EHDRSupport_HDR_RequiresUserAction: EAppHDRSupport

class CAppOverview_PerClientData(_message.Message):
    __slots__ = ("clientid", "client_name", "display_status", "status_percentage", "active_beta", "installed", "bytes_downloaded", "bytes_total", "streaming_to_local_client", "is_available_on_current_platform", "is_invalid_os_type", "playtime_left", "update_available_but_disabled_by_app")
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_BETA_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_FIELD_NUMBER: _ClassVar[int]
    BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    BYTES_TOTAL_FIELD_NUMBER: _ClassVar[int]
    STREAMING_TO_LOCAL_CLIENT_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_ON_CURRENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_INVALID_OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_LEFT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_AVAILABLE_BUT_DISABLED_BY_APP_FIELD_NUMBER: _ClassVar[int]
    clientid: int
    client_name: str
    display_status: EDisplayStatus
    status_percentage: int
    active_beta: str
    installed: bool
    bytes_downloaded: int
    bytes_total: int
    streaming_to_local_client: bool
    is_available_on_current_platform: bool
    is_invalid_os_type: bool
    playtime_left: int
    update_available_but_disabled_by_app: bool
    def __init__(self, clientid: _Optional[int] = ..., client_name: _Optional[str] = ..., display_status: _Optional[_Union[EDisplayStatus, str]] = ..., status_percentage: _Optional[int] = ..., active_beta: _Optional[str] = ..., installed: bool = ..., bytes_downloaded: _Optional[int] = ..., bytes_total: _Optional[int] = ..., streaming_to_local_client: bool = ..., is_available_on_current_platform: bool = ..., is_invalid_os_type: bool = ..., playtime_left: _Optional[int] = ..., update_available_but_disabled_by_app: bool = ...) -> None: ...

class CAppOverview(_message.Message):
    __slots__ = ("appid", "display_name", "visible_in_game_list", "subscribed_to", "sort_as", "app_type", "mru_index", "rt_recent_activity_time", "minutes_playtime_forever", "minutes_playtime_last_two_weeks", "rt_last_time_played", "store_tag", "store_category", "rt_original_release_date", "rt_steam_release_date", "icon_hash", "xbox_controller_support", "vr_supported", "metacritic_score", "size_on_disk", "third_party_mod", "icon_data", "icon_data_format", "gameid", "library_capsule_filename", "per_client_data", "most_available_clientid", "selected_clientid", "rt_store_asset_mtime", "rt_custom_image_mtime", "optional_parent_app_id", "owner_account_id", "review_score_with_bombs", "review_percentage_with_bombs", "review_score_without_bombs", "review_percentage_without_bombs", "library_id", "vr_only", "mastersub_appid", "mastersub_includedwith_logo", "site_license_site_name", "shortcut_override_appid", "rt_last_time_locally_played", "rt_purchased_time", "header_filename", "local_cache_version", "number_of_copies", "steam_hw_compat_category_packed")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_IN_GAME_LIST_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_TO_FIELD_NUMBER: _ClassVar[int]
    SORT_AS_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MRU_INDEX_FIELD_NUMBER: _ClassVar[int]
    RT_RECENT_ACTIVITY_TIME_FIELD_NUMBER: _ClassVar[int]
    MINUTES_PLAYTIME_FOREVER_FIELD_NUMBER: _ClassVar[int]
    MINUTES_PLAYTIME_LAST_TWO_WEEKS_FIELD_NUMBER: _ClassVar[int]
    RT_LAST_TIME_PLAYED_FIELD_NUMBER: _ClassVar[int]
    STORE_TAG_FIELD_NUMBER: _ClassVar[int]
    STORE_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    RT_ORIGINAL_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    RT_STEAM_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    ICON_HASH_FIELD_NUMBER: _ClassVar[int]
    XBOX_CONTROLLER_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    VR_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    METACRITIC_SCORE_FIELD_NUMBER: _ClassVar[int]
    SIZE_ON_DISK_FIELD_NUMBER: _ClassVar[int]
    THIRD_PARTY_MOD_FIELD_NUMBER: _ClassVar[int]
    ICON_DATA_FIELD_NUMBER: _ClassVar[int]
    ICON_DATA_FORMAT_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_CAPSULE_FILENAME_FIELD_NUMBER: _ClassVar[int]
    PER_CLIENT_DATA_FIELD_NUMBER: _ClassVar[int]
    MOST_AVAILABLE_CLIENTID_FIELD_NUMBER: _ClassVar[int]
    SELECTED_CLIENTID_FIELD_NUMBER: _ClassVar[int]
    RT_STORE_ASSET_MTIME_FIELD_NUMBER: _ClassVar[int]
    RT_CUSTOM_IMAGE_MTIME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PARENT_APP_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SCORE_WITH_BOMBS_FIELD_NUMBER: _ClassVar[int]
    REVIEW_PERCENTAGE_WITH_BOMBS_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SCORE_WITHOUT_BOMBS_FIELD_NUMBER: _ClassVar[int]
    REVIEW_PERCENTAGE_WITHOUT_BOMBS_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
    VR_ONLY_FIELD_NUMBER: _ClassVar[int]
    MASTERSUB_APPID_FIELD_NUMBER: _ClassVar[int]
    MASTERSUB_INCLUDEDWITH_LOGO_FIELD_NUMBER: _ClassVar[int]
    SITE_LICENSE_SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHORTCUT_OVERRIDE_APPID_FIELD_NUMBER: _ClassVar[int]
    RT_LAST_TIME_LOCALLY_PLAYED_FIELD_NUMBER: _ClassVar[int]
    RT_PURCHASED_TIME_FIELD_NUMBER: _ClassVar[int]
    HEADER_FILENAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_CACHE_VERSION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_COPIES_FIELD_NUMBER: _ClassVar[int]
    STEAM_HW_COMPAT_CATEGORY_PACKED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    display_name: str
    visible_in_game_list: bool
    subscribed_to: bool
    sort_as: str
    app_type: _enums_pb2.EProtoAppType
    mru_index: int
    rt_recent_activity_time: int
    minutes_playtime_forever: int
    minutes_playtime_last_two_weeks: int
    rt_last_time_played: int
    store_tag: _containers.RepeatedScalarFieldContainer[int]
    store_category: _containers.RepeatedScalarFieldContainer[int]
    rt_original_release_date: int
    rt_steam_release_date: int
    icon_hash: str
    xbox_controller_support: EAppControllerSupportLevel
    vr_supported: bool
    metacritic_score: int
    size_on_disk: int
    third_party_mod: bool
    icon_data: str
    icon_data_format: str
    gameid: str
    library_capsule_filename: str
    per_client_data: _containers.RepeatedCompositeFieldContainer[CAppOverview_PerClientData]
    most_available_clientid: int
    selected_clientid: int
    rt_store_asset_mtime: int
    rt_custom_image_mtime: int
    optional_parent_app_id: int
    owner_account_id: int
    review_score_with_bombs: int
    review_percentage_with_bombs: int
    review_score_without_bombs: int
    review_percentage_without_bombs: int
    library_id: str
    vr_only: bool
    mastersub_appid: int
    mastersub_includedwith_logo: str
    site_license_site_name: str
    shortcut_override_appid: int
    rt_last_time_locally_played: int
    rt_purchased_time: int
    header_filename: str
    local_cache_version: int
    number_of_copies: int
    steam_hw_compat_category_packed: int
    def __init__(self, appid: _Optional[int] = ..., display_name: _Optional[str] = ..., visible_in_game_list: bool = ..., subscribed_to: bool = ..., sort_as: _Optional[str] = ..., app_type: _Optional[_Union[_enums_pb2.EProtoAppType, str]] = ..., mru_index: _Optional[int] = ..., rt_recent_activity_time: _Optional[int] = ..., minutes_playtime_forever: _Optional[int] = ..., minutes_playtime_last_two_weeks: _Optional[int] = ..., rt_last_time_played: _Optional[int] = ..., store_tag: _Optional[_Iterable[int]] = ..., store_category: _Optional[_Iterable[int]] = ..., rt_original_release_date: _Optional[int] = ..., rt_steam_release_date: _Optional[int] = ..., icon_hash: _Optional[str] = ..., xbox_controller_support: _Optional[_Union[EAppControllerSupportLevel, str]] = ..., vr_supported: bool = ..., metacritic_score: _Optional[int] = ..., size_on_disk: _Optional[int] = ..., third_party_mod: bool = ..., icon_data: _Optional[str] = ..., icon_data_format: _Optional[str] = ..., gameid: _Optional[str] = ..., library_capsule_filename: _Optional[str] = ..., per_client_data: _Optional[_Iterable[_Union[CAppOverview_PerClientData, _Mapping]]] = ..., most_available_clientid: _Optional[int] = ..., selected_clientid: _Optional[int] = ..., rt_store_asset_mtime: _Optional[int] = ..., rt_custom_image_mtime: _Optional[int] = ..., optional_parent_app_id: _Optional[int] = ..., owner_account_id: _Optional[int] = ..., review_score_with_bombs: _Optional[int] = ..., review_percentage_with_bombs: _Optional[int] = ..., review_score_without_bombs: _Optional[int] = ..., review_percentage_without_bombs: _Optional[int] = ..., library_id: _Optional[str] = ..., vr_only: bool = ..., mastersub_appid: _Optional[int] = ..., mastersub_includedwith_logo: _Optional[str] = ..., site_license_site_name: _Optional[str] = ..., shortcut_override_appid: _Optional[int] = ..., rt_last_time_locally_played: _Optional[int] = ..., rt_purchased_time: _Optional[int] = ..., header_filename: _Optional[str] = ..., local_cache_version: _Optional[int] = ..., number_of_copies: _Optional[int] = ..., steam_hw_compat_category_packed: _Optional[int] = ...) -> None: ...

class CAppOverview_Change(_message.Message):
    __slots__ = ("app_overview", "removed_appid", "full_update", "update_complete")
    APP_OVERVIEW_FIELD_NUMBER: _ClassVar[int]
    REMOVED_APPID_FIELD_NUMBER: _ClassVar[int]
    FULL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    app_overview: _containers.RepeatedCompositeFieldContainer[CAppOverview]
    removed_appid: _containers.RepeatedScalarFieldContainer[int]
    full_update: bool
    update_complete: bool
    def __init__(self, app_overview: _Optional[_Iterable[_Union[CAppOverview, _Mapping]]] = ..., removed_appid: _Optional[_Iterable[int]] = ..., full_update: bool = ..., update_complete: bool = ...) -> None: ...

class CAppBootstrapData(_message.Message):
    __slots__ = ("appid", "hidden", "user_tag")
    APPID_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    USER_TAG_FIELD_NUMBER: _ClassVar[int]
    appid: int
    hidden: bool
    user_tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, appid: _Optional[int] = ..., hidden: bool = ..., user_tag: _Optional[_Iterable[str]] = ...) -> None: ...

class CLibraryBootstrapData(_message.Message):
    __slots__ = ("app_data",)
    APP_DATA_FIELD_NUMBER: _ClassVar[int]
    app_data: _containers.RepeatedCompositeFieldContainer[CAppBootstrapData]
    def __init__(self, app_data: _Optional[_Iterable[_Union[CAppBootstrapData, _Mapping]]] = ...) -> None: ...
