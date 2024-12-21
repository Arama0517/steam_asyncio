import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import enums_productinfo_pb2 as _enums_productinfo_pb2
import enums_pb2 as _enums_pb2
import contenthubs_pb2 as _contenthubs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EStoreItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStoreItemType_Invalid: _ClassVar[EStoreItemType]
    k_EStoreItemType_App: _ClassVar[EStoreItemType]
    k_EStoreItemType_Package: _ClassVar[EStoreItemType]
    k_EStoreItemType_Bundle: _ClassVar[EStoreItemType]
    k_EStoreItemType_Mtx: _ClassVar[EStoreItemType]
    k_EStoreItemType_Tag: _ClassVar[EStoreItemType]
    k_EStoreItemType_Creator: _ClassVar[EStoreItemType]
    k_EStoreItemType_HubCategory: _ClassVar[EStoreItemType]

class EStoreAppType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStoreAppType_Game: _ClassVar[EStoreAppType]
    k_EStoreAppType_Demo: _ClassVar[EStoreAppType]
    k_EStoreAppType_Mod: _ClassVar[EStoreAppType]
    k_EStoreAppType_Movie: _ClassVar[EStoreAppType]
    k_EStoreAppType_DLC: _ClassVar[EStoreAppType]
    k_EStoreAppType_Guide: _ClassVar[EStoreAppType]
    k_EStoreAppType_Software: _ClassVar[EStoreAppType]
    k_EStoreAppType_Video: _ClassVar[EStoreAppType]
    k_EStoreAppType_Series: _ClassVar[EStoreAppType]
    k_EStoreAppType_Episode: _ClassVar[EStoreAppType]
    k_EStoreAppType_Hardware: _ClassVar[EStoreAppType]
    k_EStoreAppType_Music: _ClassVar[EStoreAppType]
    k_EStoreAppType_Beta: _ClassVar[EStoreAppType]
    k_EStoreAppType_Tool: _ClassVar[EStoreAppType]
    k_EStoreAppType_Advertising: _ClassVar[EStoreAppType]

class EUserReviewScore(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EUserReviewScore_None: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_OverwhelminglyNegative: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_VeryNegative: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_Negative: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_MostlyNegative: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_Mixed: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_MostlyPositive: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_Positive: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_VeryPositive: _ClassVar[EUserReviewScore]
    k_EUserReviewScore_OverwhelminglyPositive: _ClassVar[EUserReviewScore]

class ETrailerCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ETrailerCategory_Invalid: _ClassVar[ETrailerCategory]
    k_ETrailerCategory_Gameplay: _ClassVar[ETrailerCategory]
    k_ETrailerCategory_Teaser: _ClassVar[ETrailerCategory]
    k_ETrailerCategory_Cinematic: _ClassVar[ETrailerCategory]
    k_ETrailerCategory_Update: _ClassVar[ETrailerCategory]
    k_ETrailerCategory_Accolades: _ClassVar[ETrailerCategory]
    k_ETrailerCategory_Interview: _ClassVar[ETrailerCategory]

class EStoreBrowseFilterFailure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStoreBrowseFilterFailure_None: _ClassVar[EStoreBrowseFilterFailure]
    k_EStoreBrowseFilterFailure_Redundant: _ClassVar[EStoreBrowseFilterFailure]
    k_EStoreBrowseFilterFailure_NotPreferred: _ClassVar[EStoreBrowseFilterFailure]
    k_EStoreBrowseFilterFailure_NotInterested: _ClassVar[EStoreBrowseFilterFailure]
    k_EStoreBrowseFilterFailure_UnwantedContent: _ClassVar[EStoreBrowseFilterFailure]
    k_EStoreBrowseFilterFailure_Unavailable: _ClassVar[EStoreBrowseFilterFailure]

class EStoreLinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStoreLinkType_None: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_YouTube: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Facebook: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Twitter: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Twitch: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Discord: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_QQ: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_VK: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Bilibili: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Weibo: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Reddit: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Instagram: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Tumblr: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Tieba: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Tiktok: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Telegram: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_LinkedIn: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_WeChat: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_QQLink: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Douyin: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Bluesky: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Mastodon: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_Threads: _ClassVar[EStoreLinkType]
    k_EStoreLinkType_MAX: _ClassVar[EStoreLinkType]

class EStoreCategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStoreCategoryType_Category: _ClassVar[EStoreCategoryType]
    k_EStoreCategoryType_SupportedPlayers: _ClassVar[EStoreCategoryType]
    k_EStoreCategoryType_Feature: _ClassVar[EStoreCategoryType]
    k_EStoreCategoryType_ControllerSupport: _ClassVar[EStoreCategoryType]
    k_EStoreCategoryType_CloudGaming: _ClassVar[EStoreCategoryType]
    k_EStoreCategoryType_MAX: _ClassVar[EStoreCategoryType]
k_EStoreItemType_Invalid: EStoreItemType
k_EStoreItemType_App: EStoreItemType
k_EStoreItemType_Package: EStoreItemType
k_EStoreItemType_Bundle: EStoreItemType
k_EStoreItemType_Mtx: EStoreItemType
k_EStoreItemType_Tag: EStoreItemType
k_EStoreItemType_Creator: EStoreItemType
k_EStoreItemType_HubCategory: EStoreItemType
k_EStoreAppType_Game: EStoreAppType
k_EStoreAppType_Demo: EStoreAppType
k_EStoreAppType_Mod: EStoreAppType
k_EStoreAppType_Movie: EStoreAppType
k_EStoreAppType_DLC: EStoreAppType
k_EStoreAppType_Guide: EStoreAppType
k_EStoreAppType_Software: EStoreAppType
k_EStoreAppType_Video: EStoreAppType
k_EStoreAppType_Series: EStoreAppType
k_EStoreAppType_Episode: EStoreAppType
k_EStoreAppType_Hardware: EStoreAppType
k_EStoreAppType_Music: EStoreAppType
k_EStoreAppType_Beta: EStoreAppType
k_EStoreAppType_Tool: EStoreAppType
k_EStoreAppType_Advertising: EStoreAppType
k_EUserReviewScore_None: EUserReviewScore
k_EUserReviewScore_OverwhelminglyNegative: EUserReviewScore
k_EUserReviewScore_VeryNegative: EUserReviewScore
k_EUserReviewScore_Negative: EUserReviewScore
k_EUserReviewScore_MostlyNegative: EUserReviewScore
k_EUserReviewScore_Mixed: EUserReviewScore
k_EUserReviewScore_MostlyPositive: EUserReviewScore
k_EUserReviewScore_Positive: EUserReviewScore
k_EUserReviewScore_VeryPositive: EUserReviewScore
k_EUserReviewScore_OverwhelminglyPositive: EUserReviewScore
k_ETrailerCategory_Invalid: ETrailerCategory
k_ETrailerCategory_Gameplay: ETrailerCategory
k_ETrailerCategory_Teaser: ETrailerCategory
k_ETrailerCategory_Cinematic: ETrailerCategory
k_ETrailerCategory_Update: ETrailerCategory
k_ETrailerCategory_Accolades: ETrailerCategory
k_ETrailerCategory_Interview: ETrailerCategory
k_EStoreBrowseFilterFailure_None: EStoreBrowseFilterFailure
k_EStoreBrowseFilterFailure_Redundant: EStoreBrowseFilterFailure
k_EStoreBrowseFilterFailure_NotPreferred: EStoreBrowseFilterFailure
k_EStoreBrowseFilterFailure_NotInterested: EStoreBrowseFilterFailure
k_EStoreBrowseFilterFailure_UnwantedContent: EStoreBrowseFilterFailure
k_EStoreBrowseFilterFailure_Unavailable: EStoreBrowseFilterFailure
k_EStoreLinkType_None: EStoreLinkType
k_EStoreLinkType_YouTube: EStoreLinkType
k_EStoreLinkType_Facebook: EStoreLinkType
k_EStoreLinkType_Twitter: EStoreLinkType
k_EStoreLinkType_Twitch: EStoreLinkType
k_EStoreLinkType_Discord: EStoreLinkType
k_EStoreLinkType_QQ: EStoreLinkType
k_EStoreLinkType_VK: EStoreLinkType
k_EStoreLinkType_Bilibili: EStoreLinkType
k_EStoreLinkType_Weibo: EStoreLinkType
k_EStoreLinkType_Reddit: EStoreLinkType
k_EStoreLinkType_Instagram: EStoreLinkType
k_EStoreLinkType_Tumblr: EStoreLinkType
k_EStoreLinkType_Tieba: EStoreLinkType
k_EStoreLinkType_Tiktok: EStoreLinkType
k_EStoreLinkType_Telegram: EStoreLinkType
k_EStoreLinkType_LinkedIn: EStoreLinkType
k_EStoreLinkType_WeChat: EStoreLinkType
k_EStoreLinkType_QQLink: EStoreLinkType
k_EStoreLinkType_Douyin: EStoreLinkType
k_EStoreLinkType_Bluesky: EStoreLinkType
k_EStoreLinkType_Mastodon: EStoreLinkType
k_EStoreLinkType_Threads: EStoreLinkType
k_EStoreLinkType_MAX: EStoreLinkType
k_EStoreCategoryType_Category: EStoreCategoryType
k_EStoreCategoryType_SupportedPlayers: EStoreCategoryType
k_EStoreCategoryType_Feature: EStoreCategoryType
k_EStoreCategoryType_ControllerSupport: EStoreCategoryType
k_EStoreCategoryType_CloudGaming: EStoreCategoryType
k_EStoreCategoryType_MAX: EStoreCategoryType

class StoreItemID(_message.Message):
    __slots__ = ("appid", "packageid", "bundleid", "tagid", "creatorid", "hubcategoryid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    BUNDLEID_FIELD_NUMBER: _ClassVar[int]
    TAGID_FIELD_NUMBER: _ClassVar[int]
    CREATORID_FIELD_NUMBER: _ClassVar[int]
    HUBCATEGORYID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    packageid: int
    bundleid: int
    tagid: int
    creatorid: int
    hubcategoryid: int
    def __init__(self, appid: _Optional[int] = ..., packageid: _Optional[int] = ..., bundleid: _Optional[int] = ..., tagid: _Optional[int] = ..., creatorid: _Optional[int] = ..., hubcategoryid: _Optional[int] = ...) -> None: ...

class StoreBrowseContext(_message.Message):
    __slots__ = ("language", "elanguage", "country_code", "steam_realm")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ELANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    STEAM_REALM_FIELD_NUMBER: _ClassVar[int]
    language: str
    elanguage: int
    country_code: str
    steam_realm: int
    def __init__(self, language: _Optional[str] = ..., elanguage: _Optional[int] = ..., country_code: _Optional[str] = ..., steam_realm: _Optional[int] = ...) -> None: ...

class StoreBrowseItemDataRequest(_message.Message):
    __slots__ = ("include_assets", "include_release", "include_platforms", "include_all_purchase_options", "include_screenshots", "include_trailers", "include_ratings", "include_tag_count", "include_reviews", "include_basic_info", "include_supported_languages", "include_full_description", "include_included_items", "included_item_data_request", "include_assets_without_overrides", "apply_user_filters", "include_links")
    INCLUDE_ASSETS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RELEASE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_PURCHASE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCREENSHOTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TRAILERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_RATINGS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SUPPORTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FULL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INCLUDED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_ITEM_DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ASSETS_WITHOUT_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    APPLY_USER_FILTERS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_LINKS_FIELD_NUMBER: _ClassVar[int]
    include_assets: bool
    include_release: bool
    include_platforms: bool
    include_all_purchase_options: bool
    include_screenshots: bool
    include_trailers: bool
    include_ratings: bool
    include_tag_count: int
    include_reviews: bool
    include_basic_info: bool
    include_supported_languages: bool
    include_full_description: bool
    include_included_items: bool
    included_item_data_request: StoreBrowseItemDataRequest
    include_assets_without_overrides: bool
    apply_user_filters: bool
    include_links: bool
    def __init__(self, include_assets: bool = ..., include_release: bool = ..., include_platforms: bool = ..., include_all_purchase_options: bool = ..., include_screenshots: bool = ..., include_trailers: bool = ..., include_ratings: bool = ..., include_tag_count: _Optional[int] = ..., include_reviews: bool = ..., include_basic_info: bool = ..., include_supported_languages: bool = ..., include_full_description: bool = ..., include_included_items: bool = ..., included_item_data_request: _Optional[_Union[StoreBrowseItemDataRequest, _Mapping]] = ..., include_assets_without_overrides: bool = ..., apply_user_filters: bool = ..., include_links: bool = ...) -> None: ...

class CStoreBrowse_GetItems_Request(_message.Message):
    __slots__ = ("ids", "context", "data_request")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedCompositeFieldContainer[StoreItemID]
    context: StoreBrowseContext
    data_request: StoreBrowseItemDataRequest
    def __init__(self, ids: _Optional[_Iterable[_Union[StoreItemID, _Mapping]]] = ..., context: _Optional[_Union[StoreBrowseContext, _Mapping]] = ..., data_request: _Optional[_Union[StoreBrowseItemDataRequest, _Mapping]] = ...) -> None: ...

class StoreItem(_message.Message):
    __slots__ = ("item_type", "id", "success", "visible", "unvailable_for_country_restriction", "name", "store_url_path", "appid", "type", "included_types", "included_appids", "is_free", "is_early_access", "related_items", "included_items", "content_descriptorids", "tagids", "categories", "reviews", "basic_info", "tags", "assets", "release", "platforms", "game_rating", "is_coming_soon", "best_purchase_option", "purchase_options", "accessories", "self_purchase_option", "screenshots", "trailers", "supported_languages", "store_url_path_override", "free_weekend", "unlisted", "game_count", "internal_name", "full_description", "is_free_temporarily", "assets_without_overrides", "user_filter_failure", "links")
    class RelatedItems(_message.Message):
        __slots__ = ("parent_appid", "demo_appid", "standalone_demo_appid")
        PARENT_APPID_FIELD_NUMBER: _ClassVar[int]
        DEMO_APPID_FIELD_NUMBER: _ClassVar[int]
        STANDALONE_DEMO_APPID_FIELD_NUMBER: _ClassVar[int]
        parent_appid: int
        demo_appid: _containers.RepeatedScalarFieldContainer[int]
        standalone_demo_appid: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, parent_appid: _Optional[int] = ..., demo_appid: _Optional[_Iterable[int]] = ..., standalone_demo_appid: _Optional[_Iterable[int]] = ...) -> None: ...
    class IncludedItems(_message.Message):
        __slots__ = ("included_apps", "included_packages")
        INCLUDED_APPS_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_PACKAGES_FIELD_NUMBER: _ClassVar[int]
        included_apps: _containers.RepeatedCompositeFieldContainer[StoreItem]
        included_packages: _containers.RepeatedCompositeFieldContainer[StoreItem]
        def __init__(self, included_apps: _Optional[_Iterable[_Union[StoreItem, _Mapping]]] = ..., included_packages: _Optional[_Iterable[_Union[StoreItem, _Mapping]]] = ...) -> None: ...
    class Categories(_message.Message):
        __slots__ = ("supported_player_categoryids", "feature_categoryids", "controller_categoryids")
        SUPPORTED_PLAYER_CATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
        FEATURE_CATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_CATEGORYIDS_FIELD_NUMBER: _ClassVar[int]
        supported_player_categoryids: _containers.RepeatedScalarFieldContainer[int]
        feature_categoryids: _containers.RepeatedScalarFieldContainer[int]
        controller_categoryids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, supported_player_categoryids: _Optional[_Iterable[int]] = ..., feature_categoryids: _Optional[_Iterable[int]] = ..., controller_categoryids: _Optional[_Iterable[int]] = ...) -> None: ...
    class Reviews(_message.Message):
        __slots__ = ("summary_filtered", "summary_unfiltered")
        class StoreReviewSummary(_message.Message):
            __slots__ = ("review_count", "percent_positive", "review_score", "review_score_label")
            REVIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
            PERCENT_POSITIVE_FIELD_NUMBER: _ClassVar[int]
            REVIEW_SCORE_FIELD_NUMBER: _ClassVar[int]
            REVIEW_SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
            review_count: int
            percent_positive: int
            review_score: EUserReviewScore
            review_score_label: str
            def __init__(self, review_count: _Optional[int] = ..., percent_positive: _Optional[int] = ..., review_score: _Optional[_Union[EUserReviewScore, str]] = ..., review_score_label: _Optional[str] = ...) -> None: ...
        SUMMARY_FILTERED_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_UNFILTERED_FIELD_NUMBER: _ClassVar[int]
        summary_filtered: StoreItem.Reviews.StoreReviewSummary
        summary_unfiltered: StoreItem.Reviews.StoreReviewSummary
        def __init__(self, summary_filtered: _Optional[_Union[StoreItem.Reviews.StoreReviewSummary, _Mapping]] = ..., summary_unfiltered: _Optional[_Union[StoreItem.Reviews.StoreReviewSummary, _Mapping]] = ...) -> None: ...
    class BasicInfo(_message.Message):
        __slots__ = ("short_description", "publishers", "developers", "franchises", "capsule_headline")
        class CreatorHomeLink(_message.Message):
            __slots__ = ("name", "creator_clan_account_id")
            NAME_FIELD_NUMBER: _ClassVar[int]
            CREATOR_CLAN_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
            name: str
            creator_clan_account_id: int
            def __init__(self, name: _Optional[str] = ..., creator_clan_account_id: _Optional[int] = ...) -> None: ...
        SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PUBLISHERS_FIELD_NUMBER: _ClassVar[int]
        DEVELOPERS_FIELD_NUMBER: _ClassVar[int]
        FRANCHISES_FIELD_NUMBER: _ClassVar[int]
        CAPSULE_HEADLINE_FIELD_NUMBER: _ClassVar[int]
        short_description: str
        publishers: _containers.RepeatedCompositeFieldContainer[StoreItem.BasicInfo.CreatorHomeLink]
        developers: _containers.RepeatedCompositeFieldContainer[StoreItem.BasicInfo.CreatorHomeLink]
        franchises: _containers.RepeatedCompositeFieldContainer[StoreItem.BasicInfo.CreatorHomeLink]
        capsule_headline: str
        def __init__(self, short_description: _Optional[str] = ..., publishers: _Optional[_Iterable[_Union[StoreItem.BasicInfo.CreatorHomeLink, _Mapping]]] = ..., developers: _Optional[_Iterable[_Union[StoreItem.BasicInfo.CreatorHomeLink, _Mapping]]] = ..., franchises: _Optional[_Iterable[_Union[StoreItem.BasicInfo.CreatorHomeLink, _Mapping]]] = ..., capsule_headline: _Optional[str] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("tagid", "weight")
        TAGID_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        tagid: int
        weight: int
        def __init__(self, tagid: _Optional[int] = ..., weight: _Optional[int] = ...) -> None: ...
    class Assets(_message.Message):
        __slots__ = ("asset_url_format", "main_capsule", "small_capsule", "header", "package_header", "page_background", "hero_capsule", "hero_capsule_2x", "library_capsule", "library_capsule_2x", "library_hero", "library_hero_2x", "community_icon", "clan_avatar")
        ASSET_URL_FORMAT_FIELD_NUMBER: _ClassVar[int]
        MAIN_CAPSULE_FIELD_NUMBER: _ClassVar[int]
        SMALL_CAPSULE_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_HEADER_FIELD_NUMBER: _ClassVar[int]
        PAGE_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
        HERO_CAPSULE_FIELD_NUMBER: _ClassVar[int]
        HERO_CAPSULE_2X_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_CAPSULE_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_CAPSULE_2X_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_HERO_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_HERO_2X_FIELD_NUMBER: _ClassVar[int]
        COMMUNITY_ICON_FIELD_NUMBER: _ClassVar[int]
        CLAN_AVATAR_FIELD_NUMBER: _ClassVar[int]
        asset_url_format: str
        main_capsule: str
        small_capsule: str
        header: str
        package_header: str
        page_background: str
        hero_capsule: str
        hero_capsule_2x: str
        library_capsule: str
        library_capsule_2x: str
        library_hero: str
        library_hero_2x: str
        community_icon: str
        clan_avatar: str
        def __init__(self, asset_url_format: _Optional[str] = ..., main_capsule: _Optional[str] = ..., small_capsule: _Optional[str] = ..., header: _Optional[str] = ..., package_header: _Optional[str] = ..., page_background: _Optional[str] = ..., hero_capsule: _Optional[str] = ..., hero_capsule_2x: _Optional[str] = ..., library_capsule: _Optional[str] = ..., library_capsule_2x: _Optional[str] = ..., library_hero: _Optional[str] = ..., library_hero_2x: _Optional[str] = ..., community_icon: _Optional[str] = ..., clan_avatar: _Optional[str] = ...) -> None: ...
    class ReleaseInfo(_message.Message):
        __slots__ = ("steam_release_date", "original_release_date", "original_steam_release_date", "is_coming_soon", "is_preload", "custom_release_date_message", "is_abridged_release_date", "coming_soon_display", "is_early_access", "mac_release_date", "linux_release_date")
        STEAM_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_STEAM_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        IS_COMING_SOON_FIELD_NUMBER: _ClassVar[int]
        IS_PRELOAD_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_RELEASE_DATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        IS_ABRIDGED_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        COMING_SOON_DISPLAY_FIELD_NUMBER: _ClassVar[int]
        IS_EARLY_ACCESS_FIELD_NUMBER: _ClassVar[int]
        MAC_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        LINUX_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        steam_release_date: int
        original_release_date: int
        original_steam_release_date: int
        is_coming_soon: bool
        is_preload: bool
        custom_release_date_message: str
        is_abridged_release_date: bool
        coming_soon_display: str
        is_early_access: bool
        mac_release_date: int
        linux_release_date: int
        def __init__(self, steam_release_date: _Optional[int] = ..., original_release_date: _Optional[int] = ..., original_steam_release_date: _Optional[int] = ..., is_coming_soon: bool = ..., is_preload: bool = ..., custom_release_date_message: _Optional[str] = ..., is_abridged_release_date: bool = ..., coming_soon_display: _Optional[str] = ..., is_early_access: bool = ..., mac_release_date: _Optional[int] = ..., linux_release_date: _Optional[int] = ...) -> None: ...
    class Platforms(_message.Message):
        __slots__ = ("windows", "mac", "steamos_linux", "vr_support", "steam_deck_compat_category")
        class VRSupport(_message.Message):
            __slots__ = ("vrhmd", "vrhmd_only", "htc_vive", "oculus_rift", "windows_mr", "valve_index")
            VRHMD_FIELD_NUMBER: _ClassVar[int]
            VRHMD_ONLY_FIELD_NUMBER: _ClassVar[int]
            HTC_VIVE_FIELD_NUMBER: _ClassVar[int]
            OCULUS_RIFT_FIELD_NUMBER: _ClassVar[int]
            WINDOWS_MR_FIELD_NUMBER: _ClassVar[int]
            VALVE_INDEX_FIELD_NUMBER: _ClassVar[int]
            vrhmd: bool
            vrhmd_only: bool
            htc_vive: bool
            oculus_rift: bool
            windows_mr: bool
            valve_index: bool
            def __init__(self, vrhmd: bool = ..., vrhmd_only: bool = ..., htc_vive: bool = ..., oculus_rift: bool = ..., windows_mr: bool = ..., valve_index: bool = ...) -> None: ...
        WINDOWS_FIELD_NUMBER: _ClassVar[int]
        MAC_FIELD_NUMBER: _ClassVar[int]
        STEAMOS_LINUX_FIELD_NUMBER: _ClassVar[int]
        VR_SUPPORT_FIELD_NUMBER: _ClassVar[int]
        STEAM_DECK_COMPAT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        windows: bool
        mac: bool
        steamos_linux: bool
        vr_support: StoreItem.Platforms.VRSupport
        steam_deck_compat_category: _enums_pb2.ESteamDeckCompatibilityCategory
        def __init__(self, windows: bool = ..., mac: bool = ..., steamos_linux: bool = ..., vr_support: _Optional[_Union[StoreItem.Platforms.VRSupport, _Mapping]] = ..., steam_deck_compat_category: _Optional[_Union[_enums_pb2.ESteamDeckCompatibilityCategory, str]] = ...) -> None: ...
    class PurchaseOption(_message.Message):
        __slots__ = ("packageid", "bundleid", "purchase_option_name", "final_price_in_cents", "original_price_in_cents", "formatted_final_price", "formatted_original_price", "discount_pct", "bundle_discount_pct", "is_free_to_keep", "price_before_bundle_discount", "formatted_price_before_bundle_discount", "active_discounts", "user_can_purchase_as_gift", "is_commercial_license", "should_suppress_discount_pct", "hide_discount_pct_for_compliance", "included_game_count", "lowest_recent_price_in_cents", "requires_shipping", "recurrence_info", "free_to_keep_ends")
        class Discount(_message.Message):
            __slots__ = ("discount_amount", "discount_description", "discount_end_date")
            DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
            DISCOUNT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            DISCOUNT_END_DATE_FIELD_NUMBER: _ClassVar[int]
            discount_amount: int
            discount_description: str
            discount_end_date: int
            def __init__(self, discount_amount: _Optional[int] = ..., discount_description: _Optional[str] = ..., discount_end_date: _Optional[int] = ...) -> None: ...
        class RecurrenceInfo(_message.Message):
            __slots__ = ("packageid", "billing_agreement_type", "renewal_time_unit", "renewal_time_period", "renewal_price_in_cents", "formatted_renewal_price")
            PACKAGEID_FIELD_NUMBER: _ClassVar[int]
            BILLING_AGREEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
            RENEWAL_TIME_UNIT_FIELD_NUMBER: _ClassVar[int]
            RENEWAL_TIME_PERIOD_FIELD_NUMBER: _ClassVar[int]
            RENEWAL_PRICE_IN_CENTS_FIELD_NUMBER: _ClassVar[int]
            FORMATTED_RENEWAL_PRICE_FIELD_NUMBER: _ClassVar[int]
            packageid: int
            billing_agreement_type: int
            renewal_time_unit: int
            renewal_time_period: int
            renewal_price_in_cents: int
            formatted_renewal_price: str
            def __init__(self, packageid: _Optional[int] = ..., billing_agreement_type: _Optional[int] = ..., renewal_time_unit: _Optional[int] = ..., renewal_time_period: _Optional[int] = ..., renewal_price_in_cents: _Optional[int] = ..., formatted_renewal_price: _Optional[str] = ...) -> None: ...
        PACKAGEID_FIELD_NUMBER: _ClassVar[int]
        BUNDLEID_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_OPTION_NAME_FIELD_NUMBER: _ClassVar[int]
        FINAL_PRICE_IN_CENTS_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_PRICE_IN_CENTS_FIELD_NUMBER: _ClassVar[int]
        FORMATTED_FINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        FORMATTED_ORIGINAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_PCT_FIELD_NUMBER: _ClassVar[int]
        BUNDLE_DISCOUNT_PCT_FIELD_NUMBER: _ClassVar[int]
        IS_FREE_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
        PRICE_BEFORE_BUNDLE_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
        FORMATTED_PRICE_BEFORE_BUNDLE_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_DISCOUNTS_FIELD_NUMBER: _ClassVar[int]
        USER_CAN_PURCHASE_AS_GIFT_FIELD_NUMBER: _ClassVar[int]
        IS_COMMERCIAL_LICENSE_FIELD_NUMBER: _ClassVar[int]
        SHOULD_SUPPRESS_DISCOUNT_PCT_FIELD_NUMBER: _ClassVar[int]
        HIDE_DISCOUNT_PCT_FOR_COMPLIANCE_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_GAME_COUNT_FIELD_NUMBER: _ClassVar[int]
        LOWEST_RECENT_PRICE_IN_CENTS_FIELD_NUMBER: _ClassVar[int]
        REQUIRES_SHIPPING_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_INFO_FIELD_NUMBER: _ClassVar[int]
        FREE_TO_KEEP_ENDS_FIELD_NUMBER: _ClassVar[int]
        packageid: int
        bundleid: int
        purchase_option_name: str
        final_price_in_cents: int
        original_price_in_cents: int
        formatted_final_price: str
        formatted_original_price: str
        discount_pct: int
        bundle_discount_pct: int
        is_free_to_keep: bool
        price_before_bundle_discount: int
        formatted_price_before_bundle_discount: str
        active_discounts: _containers.RepeatedCompositeFieldContainer[StoreItem.PurchaseOption.Discount]
        user_can_purchase_as_gift: bool
        is_commercial_license: bool
        should_suppress_discount_pct: bool
        hide_discount_pct_for_compliance: bool
        included_game_count: int
        lowest_recent_price_in_cents: int
        requires_shipping: bool
        recurrence_info: StoreItem.PurchaseOption.RecurrenceInfo
        free_to_keep_ends: int
        def __init__(self, packageid: _Optional[int] = ..., bundleid: _Optional[int] = ..., purchase_option_name: _Optional[str] = ..., final_price_in_cents: _Optional[int] = ..., original_price_in_cents: _Optional[int] = ..., formatted_final_price: _Optional[str] = ..., formatted_original_price: _Optional[str] = ..., discount_pct: _Optional[int] = ..., bundle_discount_pct: _Optional[int] = ..., is_free_to_keep: bool = ..., price_before_bundle_discount: _Optional[int] = ..., formatted_price_before_bundle_discount: _Optional[str] = ..., active_discounts: _Optional[_Iterable[_Union[StoreItem.PurchaseOption.Discount, _Mapping]]] = ..., user_can_purchase_as_gift: bool = ..., is_commercial_license: bool = ..., should_suppress_discount_pct: bool = ..., hide_discount_pct_for_compliance: bool = ..., included_game_count: _Optional[int] = ..., lowest_recent_price_in_cents: _Optional[int] = ..., requires_shipping: bool = ..., recurrence_info: _Optional[_Union[StoreItem.PurchaseOption.RecurrenceInfo, _Mapping]] = ..., free_to_keep_ends: _Optional[int] = ...) -> None: ...
    class Screenshots(_message.Message):
        __slots__ = ("all_ages_screenshots", "mature_content_screenshots")
        class Screenshot(_message.Message):
            __slots__ = ("filename", "ordinal")
            FILENAME_FIELD_NUMBER: _ClassVar[int]
            ORDINAL_FIELD_NUMBER: _ClassVar[int]
            filename: str
            ordinal: int
            def __init__(self, filename: _Optional[str] = ..., ordinal: _Optional[int] = ...) -> None: ...
        ALL_AGES_SCREENSHOTS_FIELD_NUMBER: _ClassVar[int]
        MATURE_CONTENT_SCREENSHOTS_FIELD_NUMBER: _ClassVar[int]
        all_ages_screenshots: _containers.RepeatedCompositeFieldContainer[StoreItem.Screenshots.Screenshot]
        mature_content_screenshots: _containers.RepeatedCompositeFieldContainer[StoreItem.Screenshots.Screenshot]
        def __init__(self, all_ages_screenshots: _Optional[_Iterable[_Union[StoreItem.Screenshots.Screenshot, _Mapping]]] = ..., mature_content_screenshots: _Optional[_Iterable[_Union[StoreItem.Screenshots.Screenshot, _Mapping]]] = ...) -> None: ...
    class Trailers(_message.Message):
        __slots__ = ("highlights", "other_trailers")
        class VideoSource(_message.Message):
            __slots__ = ("filename", "type")
            FILENAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            filename: str
            type: str
            def __init__(self, filename: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
        class Trailer(_message.Message):
            __slots__ = ("trailer_name", "trailer_url_format", "trailer_category", "trailer_480p", "trailer_max", "microtrailer", "screenshot_medium", "screenshot_full", "trailer_base_id")
            TRAILER_NAME_FIELD_NUMBER: _ClassVar[int]
            TRAILER_URL_FORMAT_FIELD_NUMBER: _ClassVar[int]
            TRAILER_CATEGORY_FIELD_NUMBER: _ClassVar[int]
            TRAILER_480P_FIELD_NUMBER: _ClassVar[int]
            TRAILER_MAX_FIELD_NUMBER: _ClassVar[int]
            MICROTRAILER_FIELD_NUMBER: _ClassVar[int]
            SCREENSHOT_MEDIUM_FIELD_NUMBER: _ClassVar[int]
            SCREENSHOT_FULL_FIELD_NUMBER: _ClassVar[int]
            TRAILER_BASE_ID_FIELD_NUMBER: _ClassVar[int]
            trailer_name: str
            trailer_url_format: str
            trailer_category: ETrailerCategory
            trailer_480p: _containers.RepeatedCompositeFieldContainer[StoreItem.Trailers.VideoSource]
            trailer_max: _containers.RepeatedCompositeFieldContainer[StoreItem.Trailers.VideoSource]
            microtrailer: _containers.RepeatedCompositeFieldContainer[StoreItem.Trailers.VideoSource]
            screenshot_medium: str
            screenshot_full: str
            trailer_base_id: int
            def __init__(self, trailer_name: _Optional[str] = ..., trailer_url_format: _Optional[str] = ..., trailer_category: _Optional[_Union[ETrailerCategory, str]] = ..., trailer_480p: _Optional[_Iterable[_Union[StoreItem.Trailers.VideoSource, _Mapping]]] = ..., trailer_max: _Optional[_Iterable[_Union[StoreItem.Trailers.VideoSource, _Mapping]]] = ..., microtrailer: _Optional[_Iterable[_Union[StoreItem.Trailers.VideoSource, _Mapping]]] = ..., screenshot_medium: _Optional[str] = ..., screenshot_full: _Optional[str] = ..., trailer_base_id: _Optional[int] = ...) -> None: ...
        HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
        OTHER_TRAILERS_FIELD_NUMBER: _ClassVar[int]
        highlights: _containers.RepeatedCompositeFieldContainer[StoreItem.Trailers.Trailer]
        other_trailers: _containers.RepeatedCompositeFieldContainer[StoreItem.Trailers.Trailer]
        def __init__(self, highlights: _Optional[_Iterable[_Union[StoreItem.Trailers.Trailer, _Mapping]]] = ..., other_trailers: _Optional[_Iterable[_Union[StoreItem.Trailers.Trailer, _Mapping]]] = ...) -> None: ...
    class SupportedLanguage(_message.Message):
        __slots__ = ("elanguage", "eadditionallanguage", "supported", "full_audio", "subtitles")
        ELANGUAGE_FIELD_NUMBER: _ClassVar[int]
        EADDITIONALLANGUAGE_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        FULL_AUDIO_FIELD_NUMBER: _ClassVar[int]
        SUBTITLES_FIELD_NUMBER: _ClassVar[int]
        elanguage: int
        eadditionallanguage: int
        supported: bool
        full_audio: bool
        subtitles: bool
        def __init__(self, elanguage: _Optional[int] = ..., eadditionallanguage: _Optional[int] = ..., supported: bool = ..., full_audio: bool = ..., subtitles: bool = ...) -> None: ...
    class FreeWeekend(_message.Message):
        __slots__ = ("start_time", "end_time", "text")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        start_time: int
        end_time: int
        text: str
        def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("link_type", "url", "text")
        LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        link_type: EStoreLinkType
        url: str
        text: str
        def __init__(self, link_type: _Optional[_Union[EStoreLinkType, str]] = ..., url: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    UNVAILABLE_FOR_COUNTRY_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STORE_URL_PATH_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TYPES_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_APPIDS_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_FIELD_NUMBER: _ClassVar[int]
    IS_EARLY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    RELATED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTORIDS_FIELD_NUMBER: _ClassVar[int]
    TAGIDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    REVIEWS_FIELD_NUMBER: _ClassVar[int]
    BASIC_INFO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    GAME_RATING_FIELD_NUMBER: _ClassVar[int]
    IS_COMING_SOON_FIELD_NUMBER: _ClassVar[int]
    BEST_PURCHASE_OPTION_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ACCESSORIES_FIELD_NUMBER: _ClassVar[int]
    SELF_PURCHASE_OPTION_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOTS_FIELD_NUMBER: _ClassVar[int]
    TRAILERS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    STORE_URL_PATH_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    FREE_WEEKEND_FIELD_NUMBER: _ClassVar[int]
    UNLISTED_FIELD_NUMBER: _ClassVar[int]
    GAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_TEMPORARILY_FIELD_NUMBER: _ClassVar[int]
    ASSETS_WITHOUT_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    USER_FILTER_FAILURE_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    item_type: EStoreItemType
    id: int
    success: int
    visible: bool
    unvailable_for_country_restriction: bool
    name: str
    store_url_path: str
    appid: int
    type: EStoreAppType
    included_types: _containers.RepeatedScalarFieldContainer[EStoreAppType]
    included_appids: _containers.RepeatedScalarFieldContainer[int]
    is_free: bool
    is_early_access: bool
    related_items: StoreItem.RelatedItems
    included_items: StoreItem.IncludedItems
    content_descriptorids: _containers.RepeatedScalarFieldContainer[_enums_productinfo_pb2.EContentDescriptorID]
    tagids: _containers.RepeatedScalarFieldContainer[int]
    categories: StoreItem.Categories
    reviews: StoreItem.Reviews
    basic_info: StoreItem.BasicInfo
    tags: _containers.RepeatedCompositeFieldContainer[StoreItem.Tag]
    assets: StoreItem.Assets
    release: StoreItem.ReleaseInfo
    platforms: StoreItem.Platforms
    game_rating: StoreGameRating
    is_coming_soon: bool
    best_purchase_option: StoreItem.PurchaseOption
    purchase_options: _containers.RepeatedCompositeFieldContainer[StoreItem.PurchaseOption]
    accessories: _containers.RepeatedCompositeFieldContainer[StoreItem.PurchaseOption]
    self_purchase_option: StoreItem.PurchaseOption
    screenshots: StoreItem.Screenshots
    trailers: StoreItem.Trailers
    supported_languages: _containers.RepeatedCompositeFieldContainer[StoreItem.SupportedLanguage]
    store_url_path_override: str
    free_weekend: StoreItem.FreeWeekend
    unlisted: bool
    game_count: int
    internal_name: str
    full_description: str
    is_free_temporarily: bool
    assets_without_overrides: StoreItem.Assets
    user_filter_failure: StoreBrowseFilterFailure
    links: _containers.RepeatedCompositeFieldContainer[StoreItem.Link]
    def __init__(self, item_type: _Optional[_Union[EStoreItemType, str]] = ..., id: _Optional[int] = ..., success: _Optional[int] = ..., visible: bool = ..., unvailable_for_country_restriction: bool = ..., name: _Optional[str] = ..., store_url_path: _Optional[str] = ..., appid: _Optional[int] = ..., type: _Optional[_Union[EStoreAppType, str]] = ..., included_types: _Optional[_Iterable[_Union[EStoreAppType, str]]] = ..., included_appids: _Optional[_Iterable[int]] = ..., is_free: bool = ..., is_early_access: bool = ..., related_items: _Optional[_Union[StoreItem.RelatedItems, _Mapping]] = ..., included_items: _Optional[_Union[StoreItem.IncludedItems, _Mapping]] = ..., content_descriptorids: _Optional[_Iterable[_Union[_enums_productinfo_pb2.EContentDescriptorID, str]]] = ..., tagids: _Optional[_Iterable[int]] = ..., categories: _Optional[_Union[StoreItem.Categories, _Mapping]] = ..., reviews: _Optional[_Union[StoreItem.Reviews, _Mapping]] = ..., basic_info: _Optional[_Union[StoreItem.BasicInfo, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[StoreItem.Tag, _Mapping]]] = ..., assets: _Optional[_Union[StoreItem.Assets, _Mapping]] = ..., release: _Optional[_Union[StoreItem.ReleaseInfo, _Mapping]] = ..., platforms: _Optional[_Union[StoreItem.Platforms, _Mapping]] = ..., game_rating: _Optional[_Union[StoreGameRating, _Mapping]] = ..., is_coming_soon: bool = ..., best_purchase_option: _Optional[_Union[StoreItem.PurchaseOption, _Mapping]] = ..., purchase_options: _Optional[_Iterable[_Union[StoreItem.PurchaseOption, _Mapping]]] = ..., accessories: _Optional[_Iterable[_Union[StoreItem.PurchaseOption, _Mapping]]] = ..., self_purchase_option: _Optional[_Union[StoreItem.PurchaseOption, _Mapping]] = ..., screenshots: _Optional[_Union[StoreItem.Screenshots, _Mapping]] = ..., trailers: _Optional[_Union[StoreItem.Trailers, _Mapping]] = ..., supported_languages: _Optional[_Iterable[_Union[StoreItem.SupportedLanguage, _Mapping]]] = ..., store_url_path_override: _Optional[str] = ..., free_weekend: _Optional[_Union[StoreItem.FreeWeekend, _Mapping]] = ..., unlisted: bool = ..., game_count: _Optional[int] = ..., internal_name: _Optional[str] = ..., full_description: _Optional[str] = ..., is_free_temporarily: bool = ..., assets_without_overrides: _Optional[_Union[StoreItem.Assets, _Mapping]] = ..., user_filter_failure: _Optional[_Union[StoreBrowseFilterFailure, _Mapping]] = ..., links: _Optional[_Iterable[_Union[StoreItem.Link, _Mapping]]] = ...) -> None: ...

class StoreGameRating(_message.Message):
    __slots__ = ("type", "rating", "descriptors", "interactive_elements", "required_age", "use_age_gate", "image_url", "image_target")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_AGE_FIELD_NUMBER: _ClassVar[int]
    USE_AGE_GATE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TARGET_FIELD_NUMBER: _ClassVar[int]
    type: str
    rating: str
    descriptors: _containers.RepeatedScalarFieldContainer[str]
    interactive_elements: str
    required_age: int
    use_age_gate: bool
    image_url: str
    image_target: str
    def __init__(self, type: _Optional[str] = ..., rating: _Optional[str] = ..., descriptors: _Optional[_Iterable[str]] = ..., interactive_elements: _Optional[str] = ..., required_age: _Optional[int] = ..., use_age_gate: bool = ..., image_url: _Optional[str] = ..., image_target: _Optional[str] = ...) -> None: ...

class StoreBrowseFilterFailure(_message.Message):
    __slots__ = ("filter_failure", "already_owned", "on_wishlist", "ignored", "not_in_users_language", "not_on_users_platform", "demo_for_owned_game", "dlc_for_unowned_game", "nonpreferred_product_type", "excluded_tagids", "excluded_content_descriptorids")
    FILTER_FAILURE_FIELD_NUMBER: _ClassVar[int]
    ALREADY_OWNED_FIELD_NUMBER: _ClassVar[int]
    ON_WISHLIST_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_USERS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NOT_ON_USERS_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DEMO_FOR_OWNED_GAME_FIELD_NUMBER: _ClassVar[int]
    DLC_FOR_UNOWNED_GAME_FIELD_NUMBER: _ClassVar[int]
    NONPREFERRED_PRODUCT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_TAGIDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_CONTENT_DESCRIPTORIDS_FIELD_NUMBER: _ClassVar[int]
    filter_failure: EStoreBrowseFilterFailure
    already_owned: bool
    on_wishlist: bool
    ignored: bool
    not_in_users_language: bool
    not_on_users_platform: bool
    demo_for_owned_game: bool
    dlc_for_unowned_game: bool
    nonpreferred_product_type: bool
    excluded_tagids: _containers.RepeatedScalarFieldContainer[int]
    excluded_content_descriptorids: _containers.RepeatedScalarFieldContainer[_enums_productinfo_pb2.EContentDescriptorID]
    def __init__(self, filter_failure: _Optional[_Union[EStoreBrowseFilterFailure, str]] = ..., already_owned: bool = ..., on_wishlist: bool = ..., ignored: bool = ..., not_in_users_language: bool = ..., not_on_users_platform: bool = ..., demo_for_owned_game: bool = ..., dlc_for_unowned_game: bool = ..., nonpreferred_product_type: bool = ..., excluded_tagids: _Optional[_Iterable[int]] = ..., excluded_content_descriptorids: _Optional[_Iterable[_Union[_enums_productinfo_pb2.EContentDescriptorID, str]]] = ...) -> None: ...

class CStoreBrowse_GetItems_Response(_message.Message):
    __slots__ = ("store_items",)
    STORE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    store_items: _containers.RepeatedCompositeFieldContainer[StoreItem]
    def __init__(self, store_items: _Optional[_Iterable[_Union[StoreItem, _Mapping]]] = ...) -> None: ...

class CStoreBrowse_GetStoreCategories_Request(_message.Message):
    __slots__ = ("language", "elanguage")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ELANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: str
    elanguage: int
    def __init__(self, language: _Optional[str] = ..., elanguage: _Optional[int] = ...) -> None: ...

class CStoreBrowse_GetStoreCategories_Response(_message.Message):
    __slots__ = ("categories",)
    class Category(_message.Message):
        __slots__ = ("categoryid", "type", "internal_name", "display_name", "image_url", "show_in_search", "computed", "edit_url", "edit_sort_order")
        CATEGORYID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        SHOW_IN_SEARCH_FIELD_NUMBER: _ClassVar[int]
        COMPUTED_FIELD_NUMBER: _ClassVar[int]
        EDIT_URL_FIELD_NUMBER: _ClassVar[int]
        EDIT_SORT_ORDER_FIELD_NUMBER: _ClassVar[int]
        categoryid: int
        type: EStoreCategoryType
        internal_name: str
        display_name: str
        image_url: str
        show_in_search: bool
        computed: bool
        edit_url: str
        edit_sort_order: int
        def __init__(self, categoryid: _Optional[int] = ..., type: _Optional[_Union[EStoreCategoryType, str]] = ..., internal_name: _Optional[str] = ..., display_name: _Optional[str] = ..., image_url: _Optional[str] = ..., show_in_search: bool = ..., computed: bool = ..., edit_url: _Optional[str] = ..., edit_sort_order: _Optional[int] = ...) -> None: ...
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[CStoreBrowse_GetStoreCategories_Response.Category]
    def __init__(self, categories: _Optional[_Iterable[_Union[CStoreBrowse_GetStoreCategories_Response.Category, _Mapping]]] = ...) -> None: ...

class CStoreBrowse_GetPriceStops_Request(_message.Message):
    __slots__ = ("country_code", "currency_code")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    currency_code: str
    def __init__(self, country_code: _Optional[str] = ..., currency_code: _Optional[str] = ...) -> None: ...

class CStoreBrowse_GetPriceStops_Response(_message.Message):
    __slots__ = ("price_stops", "currency_code")
    class PriceStop(_message.Message):
        __slots__ = ("formatted_amount", "amount_in_cents")
        FORMATTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_IN_CENTS_FIELD_NUMBER: _ClassVar[int]
        formatted_amount: str
        amount_in_cents: int
        def __init__(self, formatted_amount: _Optional[str] = ..., amount_in_cents: _Optional[int] = ...) -> None: ...
    PRICE_STOPS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    price_stops: _containers.RepeatedCompositeFieldContainer[CStoreBrowse_GetPriceStops_Response.PriceStop]
    currency_code: str
    def __init__(self, price_stops: _Optional[_Iterable[_Union[CStoreBrowse_GetPriceStops_Response.PriceStop, _Mapping]]] = ..., currency_code: _Optional[str] = ...) -> None: ...

class CStoreBrowse_GetDLCForApps_Request(_message.Message):
    __slots__ = ("context", "store_page_filter", "appids", "steamid")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    STORE_PAGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    context: StoreBrowseContext
    store_page_filter: _contenthubs_pb2.CStorePageFilter
    appids: _containers.RepeatedCompositeFieldContainer[StoreItemID]
    steamid: int
    def __init__(self, context: _Optional[_Union[StoreBrowseContext, _Mapping]] = ..., store_page_filter: _Optional[_Union[_contenthubs_pb2.CStorePageFilter, _Mapping]] = ..., appids: _Optional[_Iterable[_Union[StoreItemID, _Mapping]]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CStoreBrowse_GetDLCForApps_Response(_message.Message):
    __slots__ = ("dlc_data", "playtime")
    class DLCData(_message.Message):
        __slots__ = ("appid", "parentappid", "release_date", "coming_soon", "price", "discount", "free")
        APPID_FIELD_NUMBER: _ClassVar[int]
        PARENTAPPID_FIELD_NUMBER: _ClassVar[int]
        RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
        COMING_SOON_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_FIELD_NUMBER: _ClassVar[int]
        FREE_FIELD_NUMBER: _ClassVar[int]
        appid: int
        parentappid: int
        release_date: int
        coming_soon: bool
        price: int
        discount: int
        free: bool
        def __init__(self, appid: _Optional[int] = ..., parentappid: _Optional[int] = ..., release_date: _Optional[int] = ..., coming_soon: bool = ..., price: _Optional[int] = ..., discount: _Optional[int] = ..., free: bool = ...) -> None: ...
    class PlaytimeForApp(_message.Message):
        __slots__ = ("appid", "playtime", "last_played")
        APPID_FIELD_NUMBER: _ClassVar[int]
        PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        LAST_PLAYED_FIELD_NUMBER: _ClassVar[int]
        appid: int
        playtime: int
        last_played: int
        def __init__(self, appid: _Optional[int] = ..., playtime: _Optional[int] = ..., last_played: _Optional[int] = ...) -> None: ...
    DLC_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAYTIME_FIELD_NUMBER: _ClassVar[int]
    dlc_data: _containers.RepeatedCompositeFieldContainer[CStoreBrowse_GetDLCForApps_Response.DLCData]
    playtime: _containers.RepeatedCompositeFieldContainer[CStoreBrowse_GetDLCForApps_Response.PlaytimeForApp]
    def __init__(self, dlc_data: _Optional[_Iterable[_Union[CStoreBrowse_GetDLCForApps_Response.DLCData, _Mapping]]] = ..., playtime: _Optional[_Iterable[_Union[CStoreBrowse_GetDLCForApps_Response.PlaytimeForApp, _Mapping]]] = ...) -> None: ...

class CStoreBrowse_GetDLCForAppsSolr_Request(_message.Message):
    __slots__ = ("context", "appids", "flavor", "count", "store_page_filter")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    STORE_PAGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    context: StoreBrowseContext
    appids: _containers.RepeatedScalarFieldContainer[int]
    flavor: str
    count: int
    store_page_filter: _contenthubs_pb2.CStorePageFilter
    def __init__(self, context: _Optional[_Union[StoreBrowseContext, _Mapping]] = ..., appids: _Optional[_Iterable[int]] = ..., flavor: _Optional[str] = ..., count: _Optional[int] = ..., store_page_filter: _Optional[_Union[_contenthubs_pb2.CStorePageFilter, _Mapping]] = ...) -> None: ...

class CStoreBrowse_GetDLCForAppsSolr_Response(_message.Message):
    __slots__ = ("dlc_lists",)
    class DLCList(_message.Message):
        __slots__ = ("parent_appid", "dlc_appids")
        PARENT_APPID_FIELD_NUMBER: _ClassVar[int]
        DLC_APPIDS_FIELD_NUMBER: _ClassVar[int]
        parent_appid: int
        dlc_appids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, parent_appid: _Optional[int] = ..., dlc_appids: _Optional[_Iterable[int]] = ...) -> None: ...
    DLC_LISTS_FIELD_NUMBER: _ClassVar[int]
    dlc_lists: _containers.RepeatedCompositeFieldContainer[CStoreBrowse_GetDLCForAppsSolr_Response.DLCList]
    def __init__(self, dlc_lists: _Optional[_Iterable[_Union[CStoreBrowse_GetDLCForAppsSolr_Response.DLCList, _Mapping]]] = ...) -> None: ...

class CStoreBrowse_GetHardwareItems_Request(_message.Message):
    __slots__ = ("packageid", "context")
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    packageid: _containers.RepeatedScalarFieldContainer[int]
    context: StoreBrowseContext
    def __init__(self, packageid: _Optional[_Iterable[int]] = ..., context: _Optional[_Union[StoreBrowseContext, _Mapping]] = ...) -> None: ...

class CHardwarePackageDetails(_message.Message):
    __slots__ = ("packageid", "inventory_available", "high_pending_orders", "account_restricted_from_purchasing", "requires_reservation", "rtime_estimated_notification", "notificaton_token", "reservation_state", "expired", "time_expires", "time_reserved", "allow_quantity_purchase", "max_quantity_per_purchase", "allow_purchase_in_country", "estimated_delivery_soonest_business_days", "estimated_delivery_latest_business_days")
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    HIGH_PENDING_ORDERS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_RESTRICTED_FROM_PURCHASING_FIELD_NUMBER: _ClassVar[int]
    REQUIRES_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    RTIME_ESTIMATED_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATON_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_STATE_FIELD_NUMBER: _ClassVar[int]
    EXPIRED_FIELD_NUMBER: _ClassVar[int]
    TIME_EXPIRES_FIELD_NUMBER: _ClassVar[int]
    TIME_RESERVED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_QUANTITY_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    MAX_QUANTITY_PER_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_PURCHASE_IN_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DELIVERY_SOONEST_BUSINESS_DAYS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DELIVERY_LATEST_BUSINESS_DAYS_FIELD_NUMBER: _ClassVar[int]
    packageid: int
    inventory_available: bool
    high_pending_orders: bool
    account_restricted_from_purchasing: bool
    requires_reservation: bool
    rtime_estimated_notification: int
    notificaton_token: str
    reservation_state: int
    expired: bool
    time_expires: int
    time_reserved: int
    allow_quantity_purchase: bool
    max_quantity_per_purchase: int
    allow_purchase_in_country: bool
    estimated_delivery_soonest_business_days: int
    estimated_delivery_latest_business_days: int
    def __init__(self, packageid: _Optional[int] = ..., inventory_available: bool = ..., high_pending_orders: bool = ..., account_restricted_from_purchasing: bool = ..., requires_reservation: bool = ..., rtime_estimated_notification: _Optional[int] = ..., notificaton_token: _Optional[str] = ..., reservation_state: _Optional[int] = ..., expired: bool = ..., time_expires: _Optional[int] = ..., time_reserved: _Optional[int] = ..., allow_quantity_purchase: bool = ..., max_quantity_per_purchase: _Optional[int] = ..., allow_purchase_in_country: bool = ..., estimated_delivery_soonest_business_days: _Optional[int] = ..., estimated_delivery_latest_business_days: _Optional[int] = ...) -> None: ...

class CStoreBrowse_GetHardwareItems_Response(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[CHardwarePackageDetails]
    def __init__(self, details: _Optional[_Iterable[_Union[CHardwarePackageDetails, _Mapping]]] = ...) -> None: ...

class StoreBrowse(_service.service): ...

class StoreBrowse_Stub(StoreBrowse): ...
