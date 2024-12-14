import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import contenthubs_pb2 as _contenthubs_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EStoreDiscoveryQueueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStoreDiscoveryQueueTypeNew: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeComingSoon: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeRecommended: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeEveryNewRelease: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeMLRecommender: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeWishlistOnSale: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeDLC: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeDLCOnSale: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeRecommendedComingSoon: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeRecommendedFree: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeRecommendedOnSale: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeRecommendedDemos: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeDLCNewReleases: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeDLCTopSellers: _ClassVar[EStoreDiscoveryQueueType]
    k_EStoreDiscoveryQueueTypeMAX: _ClassVar[EStoreDiscoveryQueueType]

class EPlaytestStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ETesterStatusNone: _ClassVar[EPlaytestStatus]
    k_ETesterStatusPending: _ClassVar[EPlaytestStatus]
    k_ETesterStatusInvited: _ClassVar[EPlaytestStatus]
    k_ETesterStatusGranted: _ClassVar[EPlaytestStatus]

class EAppReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAppReportType_Invalid: _ClassVar[EAppReportType]
    k_EAppReportType_Scam: _ClassVar[EAppReportType]
    k_EAppReportType_Malware: _ClassVar[EAppReportType]
    k_EAppReportType_HateSpeech: _ClassVar[EAppReportType]
    k_EAppReportType_Pornography: _ClassVar[EAppReportType]
    k_EAppReportType_NonLabeledAdultContent: _ClassVar[EAppReportType]
    k_EAppReportType_Libelous: _ClassVar[EAppReportType]
    k_EAppReportType_Offensive: _ClassVar[EAppReportType]
    k_EAppReportType_ExploitsChildren: _ClassVar[EAppReportType]
    k_EAppReportType_MtxWithNonSteamWalletPaymentMethods: _ClassVar[EAppReportType]
    k_EAppReportType_CopyrightViolation: _ClassVar[EAppReportType]
    k_EAppReportType_ViolatesLaws: _ClassVar[EAppReportType]
    k_EAppReportType_Other: _ClassVar[EAppReportType]
    k_EAppReportType_Broken: _ClassVar[EAppReportType]
    k_EAppReportType_AIContentReport: _ClassVar[EAppReportType]

class EUserReviewScorePreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EUserReviewScorePreference_Unset: _ClassVar[EUserReviewScorePreference]
    k_EUserReviewScorePreference_IncludeAll: _ClassVar[EUserReviewScorePreference]
    k_EUserReviewScorePreference_ExcludeBombs: _ClassVar[EUserReviewScorePreference]

class EPartnerLinkTrackingBackfillSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EPartnerLinkTrackingBackfillSource_None: _ClassVar[EPartnerLinkTrackingBackfillSource]
    k_EPartnerLinkTrackingBackfillSource_Web: _ClassVar[EPartnerLinkTrackingBackfillSource]
    k_EPartnerLinkTrackingBackfillSource_Mobile: _ClassVar[EPartnerLinkTrackingBackfillSource]
    k_EPartnerLinkTrackingBackfillSource_Desktop: _ClassVar[EPartnerLinkTrackingBackfillSource]
k_EStoreDiscoveryQueueTypeNew: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeComingSoon: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeRecommended: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeEveryNewRelease: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeMLRecommender: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeWishlistOnSale: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeDLC: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeDLCOnSale: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeRecommendedComingSoon: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeRecommendedFree: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeRecommendedOnSale: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeRecommendedDemos: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeDLCNewReleases: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeDLCTopSellers: EStoreDiscoveryQueueType
k_EStoreDiscoveryQueueTypeMAX: EStoreDiscoveryQueueType
k_ETesterStatusNone: EPlaytestStatus
k_ETesterStatusPending: EPlaytestStatus
k_ETesterStatusInvited: EPlaytestStatus
k_ETesterStatusGranted: EPlaytestStatus
k_EAppReportType_Invalid: EAppReportType
k_EAppReportType_Scam: EAppReportType
k_EAppReportType_Malware: EAppReportType
k_EAppReportType_HateSpeech: EAppReportType
k_EAppReportType_Pornography: EAppReportType
k_EAppReportType_NonLabeledAdultContent: EAppReportType
k_EAppReportType_Libelous: EAppReportType
k_EAppReportType_Offensive: EAppReportType
k_EAppReportType_ExploitsChildren: EAppReportType
k_EAppReportType_MtxWithNonSteamWalletPaymentMethods: EAppReportType
k_EAppReportType_CopyrightViolation: EAppReportType
k_EAppReportType_ViolatesLaws: EAppReportType
k_EAppReportType_Other: EAppReportType
k_EAppReportType_Broken: EAppReportType
k_EAppReportType_AIContentReport: EAppReportType
k_EUserReviewScorePreference_Unset: EUserReviewScorePreference
k_EUserReviewScorePreference_IncludeAll: EUserReviewScorePreference
k_EUserReviewScorePreference_ExcludeBombs: EUserReviewScorePreference
k_EPartnerLinkTrackingBackfillSource_None: EPartnerLinkTrackingBackfillSource
k_EPartnerLinkTrackingBackfillSource_Web: EPartnerLinkTrackingBackfillSource
k_EPartnerLinkTrackingBackfillSource_Mobile: EPartnerLinkTrackingBackfillSource
k_EPartnerLinkTrackingBackfillSource_Desktop: EPartnerLinkTrackingBackfillSource

class CStore_RegisterCDKey_Request(_message.Message):
    __slots__ = ("activation_code", "purchase_platform", "is_request_from_client")
    ACTIVATION_CODE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    IS_REQUEST_FROM_CLIENT_FIELD_NUMBER: _ClassVar[int]
    activation_code: str
    purchase_platform: int
    is_request_from_client: bool
    def __init__(self, activation_code: _Optional[str] = ..., purchase_platform: _Optional[int] = ..., is_request_from_client: bool = ...) -> None: ...

class CStore_PurchaseReceiptInfo(_message.Message):
    __slots__ = ("transactionid", "packageid", "purchase_status", "result_detail", "transaction_time", "payment_method", "base_price", "total_discount", "tax", "shipping", "currency_code", "country_code", "error_headline", "error_string", "error_link_text", "error_link_url", "error_appid", "line_items")
    class LineItem(_message.Message):
        __slots__ = ("packageid", "appid", "line_item_description")
        PACKAGEID_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        LINE_ITEM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        packageid: int
        appid: int
        line_item_description: str
        def __init__(self, packageid: _Optional[int] = ..., appid: _Optional[int] = ..., line_item_description: _Optional[str] = ...) -> None: ...
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    PACKAGEID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_DETAIL_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_TIME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    BASE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_HEADLINE_FIELD_NUMBER: _ClassVar[int]
    ERROR_STRING_FIELD_NUMBER: _ClassVar[int]
    ERROR_LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
    ERROR_LINK_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_APPID_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    transactionid: int
    packageid: int
    purchase_status: int
    result_detail: int
    transaction_time: int
    payment_method: int
    base_price: int
    total_discount: int
    tax: int
    shipping: int
    currency_code: int
    country_code: str
    error_headline: str
    error_string: str
    error_link_text: str
    error_link_url: str
    error_appid: int
    line_items: _containers.RepeatedCompositeFieldContainer[CStore_PurchaseReceiptInfo.LineItem]
    def __init__(self, transactionid: _Optional[int] = ..., packageid: _Optional[int] = ..., purchase_status: _Optional[int] = ..., result_detail: _Optional[int] = ..., transaction_time: _Optional[int] = ..., payment_method: _Optional[int] = ..., base_price: _Optional[int] = ..., total_discount: _Optional[int] = ..., tax: _Optional[int] = ..., shipping: _Optional[int] = ..., currency_code: _Optional[int] = ..., country_code: _Optional[str] = ..., error_headline: _Optional[str] = ..., error_string: _Optional[str] = ..., error_link_text: _Optional[str] = ..., error_link_url: _Optional[str] = ..., error_appid: _Optional[int] = ..., line_items: _Optional[_Iterable[_Union[CStore_PurchaseReceiptInfo.LineItem, _Mapping]]] = ...) -> None: ...

class CStore_RegisterCDKey_Response(_message.Message):
    __slots__ = ("purchase_result_details", "purchase_receipt_info")
    PURCHASE_RESULT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_RECEIPT_INFO_FIELD_NUMBER: _ClassVar[int]
    purchase_result_details: int
    purchase_receipt_info: CStore_PurchaseReceiptInfo
    def __init__(self, purchase_result_details: _Optional[int] = ..., purchase_receipt_info: _Optional[_Union[CStore_PurchaseReceiptInfo, _Mapping]] = ...) -> None: ...

class CStore_GetMostPopularTags_Request(_message.Message):
    __slots__ = ("language",)
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: str
    def __init__(self, language: _Optional[str] = ...) -> None: ...

class CStore_GetMostPopularTags_Response(_message.Message):
    __slots__ = ("tags",)
    class Tag(_message.Message):
        __slots__ = ("tagid", "name")
        TAGID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        tagid: int
        name: str
        def __init__(self, tagid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[CStore_GetMostPopularTags_Response.Tag]
    def __init__(self, tags: _Optional[_Iterable[_Union[CStore_GetMostPopularTags_Response.Tag, _Mapping]]] = ...) -> None: ...

class CStore_GetLocalizedNameForTags_Request(_message.Message):
    __slots__ = ("language", "tagids")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TAGIDS_FIELD_NUMBER: _ClassVar[int]
    language: str
    tagids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, language: _Optional[str] = ..., tagids: _Optional[_Iterable[int]] = ...) -> None: ...

class CStore_GetLocalizedNameForTags_Response(_message.Message):
    __slots__ = ("tags",)
    class Tag(_message.Message):
        __slots__ = ("tagid", "english_name", "name", "normalized_name")
        TAGID_FIELD_NUMBER: _ClassVar[int]
        ENGLISH_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        NORMALIZED_NAME_FIELD_NUMBER: _ClassVar[int]
        tagid: int
        english_name: str
        name: str
        normalized_name: str
        def __init__(self, tagid: _Optional[int] = ..., english_name: _Optional[str] = ..., name: _Optional[str] = ..., normalized_name: _Optional[str] = ...) -> None: ...
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[CStore_GetLocalizedNameForTags_Response.Tag]
    def __init__(self, tags: _Optional[_Iterable[_Union[CStore_GetLocalizedNameForTags_Response.Tag, _Mapping]]] = ...) -> None: ...

class CStore_GetTagList_Request(_message.Message):
    __slots__ = ("language", "have_version_hash")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    HAVE_VERSION_HASH_FIELD_NUMBER: _ClassVar[int]
    language: str
    have_version_hash: str
    def __init__(self, language: _Optional[str] = ..., have_version_hash: _Optional[str] = ...) -> None: ...

class CStore_GetTagList_Response(_message.Message):
    __slots__ = ("version_hash", "tags")
    class Tag(_message.Message):
        __slots__ = ("tagid", "name")
        TAGID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        tagid: int
        name: str
        def __init__(self, tagid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    VERSION_HASH_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    version_hash: str
    tags: _containers.RepeatedCompositeFieldContainer[CStore_GetTagList_Response.Tag]
    def __init__(self, version_hash: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[CStore_GetTagList_Response.Tag, _Mapping]]] = ...) -> None: ...

class CStoreDiscoveryQueueSettings(_message.Message):
    __slots__ = ("os_win", "os_mac", "os_linux", "full_controller_support", "native_steam_controller", "include_coming_soon", "excluded_tagids", "exclude_early_access", "exclude_videos", "exclude_software", "exclude_dlc", "exclude_soundtracks", "featured_tagids")
    OS_WIN_FIELD_NUMBER: _ClassVar[int]
    OS_MAC_FIELD_NUMBER: _ClassVar[int]
    OS_LINUX_FIELD_NUMBER: _ClassVar[int]
    FULL_CONTROLLER_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    NATIVE_STEAM_CONTROLLER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_COMING_SOON_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_TAGIDS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_EARLY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOFTWARE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_DLC_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SOUNDTRACKS_FIELD_NUMBER: _ClassVar[int]
    FEATURED_TAGIDS_FIELD_NUMBER: _ClassVar[int]
    os_win: bool
    os_mac: bool
    os_linux: bool
    full_controller_support: bool
    native_steam_controller: bool
    include_coming_soon: bool
    excluded_tagids: _containers.RepeatedScalarFieldContainer[int]
    exclude_early_access: bool
    exclude_videos: bool
    exclude_software: bool
    exclude_dlc: bool
    exclude_soundtracks: bool
    featured_tagids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, os_win: bool = ..., os_mac: bool = ..., os_linux: bool = ..., full_controller_support: bool = ..., native_steam_controller: bool = ..., include_coming_soon: bool = ..., excluded_tagids: _Optional[_Iterable[int]] = ..., exclude_early_access: bool = ..., exclude_videos: bool = ..., exclude_software: bool = ..., exclude_dlc: bool = ..., exclude_soundtracks: bool = ..., featured_tagids: _Optional[_Iterable[int]] = ...) -> None: ...

class CStore_GetDiscoveryQueue_Request(_message.Message):
    __slots__ = ("queue_type", "country_code", "rebuild_queue", "settings_changed", "settings", "rebuild_queue_if_stale", "ignore_user_preferences", "no_experimental_results", "experimental_cohort", "debug_get_solr_query", "store_page_filter")
    QUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    REBUILD_QUEUE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_CHANGED_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    REBUILD_QUEUE_IF_STALE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_USER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    NO_EXPERIMENTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_COHORT_FIELD_NUMBER: _ClassVar[int]
    DEBUG_GET_SOLR_QUERY_FIELD_NUMBER: _ClassVar[int]
    STORE_PAGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    queue_type: EStoreDiscoveryQueueType
    country_code: str
    rebuild_queue: bool
    settings_changed: bool
    settings: CStoreDiscoveryQueueSettings
    rebuild_queue_if_stale: bool
    ignore_user_preferences: bool
    no_experimental_results: bool
    experimental_cohort: int
    debug_get_solr_query: bool
    store_page_filter: _contenthubs_pb2.CStorePageFilter
    def __init__(self, queue_type: _Optional[_Union[EStoreDiscoveryQueueType, str]] = ..., country_code: _Optional[str] = ..., rebuild_queue: bool = ..., settings_changed: bool = ..., settings: _Optional[_Union[CStoreDiscoveryQueueSettings, _Mapping]] = ..., rebuild_queue_if_stale: bool = ..., ignore_user_preferences: bool = ..., no_experimental_results: bool = ..., experimental_cohort: _Optional[int] = ..., debug_get_solr_query: bool = ..., store_page_filter: _Optional[_Union[_contenthubs_pb2.CStorePageFilter, _Mapping]] = ...) -> None: ...

class CStore_GetDiscoveryQueue_Response(_message.Message):
    __slots__ = ("appids", "country_code", "settings", "skipped", "exhausted", "experimental_cohort", "debug_solr_query")
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    EXHAUSTED_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_COHORT_FIELD_NUMBER: _ClassVar[int]
    DEBUG_SOLR_QUERY_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    country_code: str
    settings: CStoreDiscoveryQueueSettings
    skipped: int
    exhausted: bool
    experimental_cohort: int
    debug_solr_query: str
    def __init__(self, appids: _Optional[_Iterable[int]] = ..., country_code: _Optional[str] = ..., settings: _Optional[_Union[CStoreDiscoveryQueueSettings, _Mapping]] = ..., skipped: _Optional[int] = ..., exhausted: bool = ..., experimental_cohort: _Optional[int] = ..., debug_solr_query: _Optional[str] = ...) -> None: ...

class CStore_GetDiscoveryQueueSettings_Request(_message.Message):
    __slots__ = ("queue_type", "store_page_filter")
    QUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORE_PAGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    queue_type: EStoreDiscoveryQueueType
    store_page_filter: _contenthubs_pb2.CStorePageFilter
    def __init__(self, queue_type: _Optional[_Union[EStoreDiscoveryQueueType, str]] = ..., store_page_filter: _Optional[_Union[_contenthubs_pb2.CStorePageFilter, _Mapping]] = ...) -> None: ...

class CStore_GetDiscoveryQueueSettings_Response(_message.Message):
    __slots__ = ("country_code", "settings")
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    settings: CStoreDiscoveryQueueSettings
    def __init__(self, country_code: _Optional[str] = ..., settings: _Optional[_Union[CStoreDiscoveryQueueSettings, _Mapping]] = ...) -> None: ...

class CStore_SkipDiscoveryQueueItem_Request(_message.Message):
    __slots__ = ("queue_type", "appid", "store_page_filter")
    QUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    STORE_PAGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    queue_type: EStoreDiscoveryQueueType
    appid: int
    store_page_filter: _contenthubs_pb2.CStorePageFilter
    def __init__(self, queue_type: _Optional[_Union[EStoreDiscoveryQueueType, str]] = ..., appid: _Optional[int] = ..., store_page_filter: _Optional[_Union[_contenthubs_pb2.CStorePageFilter, _Mapping]] = ...) -> None: ...

class CStore_SkipDiscoveryQueueItem_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStore_GetUserGameInterestState_Request(_message.Message):
    __slots__ = ("appid", "store_appid", "beta_appid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    STORE_APPID_FIELD_NUMBER: _ClassVar[int]
    BETA_APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    store_appid: int
    beta_appid: int
    def __init__(self, appid: _Optional[int] = ..., store_appid: _Optional[int] = ..., beta_appid: _Optional[int] = ...) -> None: ...

class CStore_GetUserGameInterestState_Response(_message.Message):
    __slots__ = ("owned", "wishlist", "ignored", "following", "in_queues", "queues_with_skip", "queue_items_remaining", "queue_items_next_appid", "temporarily_owned", "queues", "ignored_reason", "beta_status")
    class InQueue(_message.Message):
        __slots__ = ("type", "skipped", "items_remaining", "next_appid", "experimental_cohort")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SKIPPED_FIELD_NUMBER: _ClassVar[int]
        ITEMS_REMAINING_FIELD_NUMBER: _ClassVar[int]
        NEXT_APPID_FIELD_NUMBER: _ClassVar[int]
        EXPERIMENTAL_COHORT_FIELD_NUMBER: _ClassVar[int]
        type: EStoreDiscoveryQueueType
        skipped: bool
        items_remaining: int
        next_appid: int
        experimental_cohort: int
        def __init__(self, type: _Optional[_Union[EStoreDiscoveryQueueType, str]] = ..., skipped: bool = ..., items_remaining: _Optional[int] = ..., next_appid: _Optional[int] = ..., experimental_cohort: _Optional[int] = ...) -> None: ...
    OWNED_FIELD_NUMBER: _ClassVar[int]
    WISHLIST_FIELD_NUMBER: _ClassVar[int]
    IGNORED_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_FIELD_NUMBER: _ClassVar[int]
    IN_QUEUES_FIELD_NUMBER: _ClassVar[int]
    QUEUES_WITH_SKIP_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ITEMS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    QUEUE_ITEMS_NEXT_APPID_FIELD_NUMBER: _ClassVar[int]
    TEMPORARILY_OWNED_FIELD_NUMBER: _ClassVar[int]
    QUEUES_FIELD_NUMBER: _ClassVar[int]
    IGNORED_REASON_FIELD_NUMBER: _ClassVar[int]
    BETA_STATUS_FIELD_NUMBER: _ClassVar[int]
    owned: bool
    wishlist: bool
    ignored: bool
    following: bool
    in_queues: _containers.RepeatedScalarFieldContainer[EStoreDiscoveryQueueType]
    queues_with_skip: _containers.RepeatedScalarFieldContainer[EStoreDiscoveryQueueType]
    queue_items_remaining: _containers.RepeatedScalarFieldContainer[int]
    queue_items_next_appid: _containers.RepeatedScalarFieldContainer[int]
    temporarily_owned: bool
    queues: _containers.RepeatedCompositeFieldContainer[CStore_GetUserGameInterestState_Response.InQueue]
    ignored_reason: int
    beta_status: EPlaytestStatus
    def __init__(self, owned: bool = ..., wishlist: bool = ..., ignored: bool = ..., following: bool = ..., in_queues: _Optional[_Iterable[_Union[EStoreDiscoveryQueueType, str]]] = ..., queues_with_skip: _Optional[_Iterable[_Union[EStoreDiscoveryQueueType, str]]] = ..., queue_items_remaining: _Optional[_Iterable[int]] = ..., queue_items_next_appid: _Optional[_Iterable[int]] = ..., temporarily_owned: bool = ..., queues: _Optional[_Iterable[_Union[CStore_GetUserGameInterestState_Response.InQueue, _Mapping]]] = ..., ignored_reason: _Optional[int] = ..., beta_status: _Optional[_Union[EPlaytestStatus, str]] = ...) -> None: ...

class CStore_GetDiscoveryQueueSkippedApps_Request(_message.Message):
    __slots__ = ("steamid", "queue_type", "store_page_filter")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    QUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORE_PAGE_FILTER_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    queue_type: EStoreDiscoveryQueueType
    store_page_filter: _contenthubs_pb2.CStorePageFilter
    def __init__(self, steamid: _Optional[int] = ..., queue_type: _Optional[_Union[EStoreDiscoveryQueueType, str]] = ..., store_page_filter: _Optional[_Union[_contenthubs_pb2.CStorePageFilter, _Mapping]] = ...) -> None: ...

class CStore_GetDiscoveryQueueSkippedApps_Response(_message.Message):
    __slots__ = ("appids",)
    APPIDS_FIELD_NUMBER: _ClassVar[int]
    appids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, appids: _Optional[_Iterable[int]] = ...) -> None: ...

class CStore_ReportApp_Request(_message.Message):
    __slots__ = ("appid", "report_type", "report")
    APPID_FIELD_NUMBER: _ClassVar[int]
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    report_type: EAppReportType
    report: str
    def __init__(self, appid: _Optional[int] = ..., report_type: _Optional[_Union[EAppReportType, str]] = ..., report: _Optional[str] = ...) -> None: ...

class CStore_ReportApp_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStore_GetStorePreferences_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStore_UserPreferences(_message.Message):
    __slots__ = ("primary_language", "secondary_languages", "platform_windows", "platform_mac", "platform_linux", "timestamp_updated", "hide_store_broadcast", "review_score_preference", "timestamp_content_descriptor_preferences_updated", "provide_deck_feedback", "additional_languages")
    PRIMARY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_WINDOWS_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_MAC_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_LINUX_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UPDATED_FIELD_NUMBER: _ClassVar[int]
    HIDE_STORE_BROADCAST_FIELD_NUMBER: _ClassVar[int]
    REVIEW_SCORE_PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_CONTENT_DESCRIPTOR_PREFERENCES_UPDATED_FIELD_NUMBER: _ClassVar[int]
    PROVIDE_DECK_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    primary_language: int
    secondary_languages: int
    platform_windows: bool
    platform_mac: bool
    platform_linux: bool
    timestamp_updated: int
    hide_store_broadcast: bool
    review_score_preference: EUserReviewScorePreference
    timestamp_content_descriptor_preferences_updated: int
    provide_deck_feedback: _enums_pb2.EProvideDeckFeedbackPreference
    additional_languages: str
    def __init__(self, primary_language: _Optional[int] = ..., secondary_languages: _Optional[int] = ..., platform_windows: bool = ..., platform_mac: bool = ..., platform_linux: bool = ..., timestamp_updated: _Optional[int] = ..., hide_store_broadcast: bool = ..., review_score_preference: _Optional[_Union[EUserReviewScorePreference, str]] = ..., timestamp_content_descriptor_preferences_updated: _Optional[int] = ..., provide_deck_feedback: _Optional[_Union[_enums_pb2.EProvideDeckFeedbackPreference, str]] = ..., additional_languages: _Optional[str] = ...) -> None: ...

class CStore_UserTagPreferences(_message.Message):
    __slots__ = ("tags_to_exclude",)
    class Tag(_message.Message):
        __slots__ = ("tagid", "name", "timestamp_added")
        TAGID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_ADDED_FIELD_NUMBER: _ClassVar[int]
        tagid: int
        name: str
        timestamp_added: int
        def __init__(self, tagid: _Optional[int] = ..., name: _Optional[str] = ..., timestamp_added: _Optional[int] = ...) -> None: ...
    TAGS_TO_EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    tags_to_exclude: _containers.RepeatedCompositeFieldContainer[CStore_UserTagPreferences.Tag]
    def __init__(self, tags_to_exclude: _Optional[_Iterable[_Union[CStore_UserTagPreferences.Tag, _Mapping]]] = ...) -> None: ...

class CStore_GetStorePreferences_Response(_message.Message):
    __slots__ = ("preferences", "tag_preferences", "content_descriptor_preferences")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    TAG_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTOR_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: CStore_UserPreferences
    tag_preferences: CStore_UserTagPreferences
    content_descriptor_preferences: _steammessages_base_pb2.UserContentDescriptorPreferences
    def __init__(self, preferences: _Optional[_Union[CStore_UserPreferences, _Mapping]] = ..., tag_preferences: _Optional[_Union[CStore_UserTagPreferences, _Mapping]] = ..., content_descriptor_preferences: _Optional[_Union[_steammessages_base_pb2.UserContentDescriptorPreferences, _Mapping]] = ...) -> None: ...

class CStore_GetTrendingAppsAmongFriends_Request(_message.Message):
    __slots__ = ("num_apps", "num_top_friends")
    NUM_APPS_FIELD_NUMBER: _ClassVar[int]
    NUM_TOP_FRIENDS_FIELD_NUMBER: _ClassVar[int]
    num_apps: int
    num_top_friends: int
    def __init__(self, num_apps: _Optional[int] = ..., num_top_friends: _Optional[int] = ...) -> None: ...

class CStore_GetTrendingAppsAmongFriends_Response(_message.Message):
    __slots__ = ("trending_apps",)
    class TrendingAppData(_message.Message):
        __slots__ = ("appid", "steamids_top_friends", "total_friends")
        APPID_FIELD_NUMBER: _ClassVar[int]
        STEAMIDS_TOP_FRIENDS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FRIENDS_FIELD_NUMBER: _ClassVar[int]
        appid: int
        steamids_top_friends: _containers.RepeatedScalarFieldContainer[int]
        total_friends: int
        def __init__(self, appid: _Optional[int] = ..., steamids_top_friends: _Optional[_Iterable[int]] = ..., total_friends: _Optional[int] = ...) -> None: ...
    TRENDING_APPS_FIELD_NUMBER: _ClassVar[int]
    trending_apps: _containers.RepeatedCompositeFieldContainer[CStore_GetTrendingAppsAmongFriends_Response.TrendingAppData]
    def __init__(self, trending_apps: _Optional[_Iterable[_Union[CStore_GetTrendingAppsAmongFriends_Response.TrendingAppData, _Mapping]]] = ...) -> None: ...

class CStore_MigratePartnerLinkTracking_Notification(_message.Message):
    __slots__ = ("accountid", "browserid", "backfill_source")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    BROWSERID_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    browserid: int
    backfill_source: EPartnerLinkTrackingBackfillSource
    def __init__(self, accountid: _Optional[int] = ..., browserid: _Optional[int] = ..., backfill_source: _Optional[_Union[EPartnerLinkTrackingBackfillSource, str]] = ...) -> None: ...

class CStore_UpdatePackageReservations_Request(_message.Message):
    __slots__ = ("packages_to_reserve", "packages_to_unreserve", "country_code")
    PACKAGES_TO_RESERVE_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_TO_UNRESERVE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    packages_to_reserve: _containers.RepeatedScalarFieldContainer[int]
    packages_to_unreserve: _containers.RepeatedScalarFieldContainer[int]
    country_code: str
    def __init__(self, packages_to_reserve: _Optional[_Iterable[int]] = ..., packages_to_unreserve: _Optional[_Iterable[int]] = ..., country_code: _Optional[str] = ...) -> None: ...

class CStore_UpdatePackageReservations_Response(_message.Message):
    __slots__ = ("reservation_status",)
    RESERVATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    reservation_status: _containers.RepeatedCompositeFieldContainer[_steammessages_base_pb2.CPackageReservationStatus]
    def __init__(self, reservation_status: _Optional[_Iterable[_Union[_steammessages_base_pb2.CPackageReservationStatus, _Mapping]]] = ...) -> None: ...

class CStore_GetWishlistDemoEmailStatus_Request(_message.Message):
    __slots__ = ("appid", "demo_appid", "allow_late_firing")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEMO_APPID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LATE_FIRING_FIELD_NUMBER: _ClassVar[int]
    appid: int
    demo_appid: int
    allow_late_firing: bool
    def __init__(self, appid: _Optional[int] = ..., demo_appid: _Optional[int] = ..., allow_late_firing: bool = ...) -> None: ...

class CStore_GetWishlistDemoEmailStatus_Response(_message.Message):
    __slots__ = ("can_fire", "time_staged", "demo_release_date")
    CAN_FIRE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAGED_FIELD_NUMBER: _ClassVar[int]
    DEMO_RELEASE_DATE_FIELD_NUMBER: _ClassVar[int]
    can_fire: bool
    time_staged: int
    demo_release_date: int
    def __init__(self, can_fire: bool = ..., time_staged: _Optional[int] = ..., demo_release_date: _Optional[int] = ...) -> None: ...

class CStore_QueueWishlistDemoEmailToFire_Request(_message.Message):
    __slots__ = ("appid", "demo_appid", "allow_late_firing")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEMO_APPID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LATE_FIRING_FIELD_NUMBER: _ClassVar[int]
    appid: int
    demo_appid: int
    allow_late_firing: bool
    def __init__(self, appid: _Optional[int] = ..., demo_appid: _Optional[int] = ..., allow_late_firing: bool = ...) -> None: ...

class CStore_QueueWishlistDemoEmailToFire_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CReservationPositionMessage(_message.Message):
    __slots__ = ("edistributor", "product_identifier", "start_queue_position", "rtime_estimated_notification", "localization_token", "accountid", "rtime_created")
    EDISTRIBUTOR_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    START_QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
    RTIME_ESTIMATED_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    RTIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    edistributor: int
    product_identifier: str
    start_queue_position: int
    rtime_estimated_notification: int
    localization_token: str
    accountid: int
    rtime_created: int
    def __init__(self, edistributor: _Optional[int] = ..., product_identifier: _Optional[str] = ..., start_queue_position: _Optional[int] = ..., rtime_estimated_notification: _Optional[int] = ..., localization_token: _Optional[str] = ..., accountid: _Optional[int] = ..., rtime_created: _Optional[int] = ...) -> None: ...

class CStore_SetReservationPositionMessage_Request(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[CReservationPositionMessage]
    def __init__(self, settings: _Optional[_Iterable[_Union[CReservationPositionMessage, _Mapping]]] = ...) -> None: ...

class CStore_SetReservationPositionMessage_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStore_DeleteReservationPositionMessage_Request(_message.Message):
    __slots__ = ("edistributor", "product_identifier", "start_queue_position")
    EDISTRIBUTOR_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    START_QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
    edistributor: int
    product_identifier: str
    start_queue_position: int
    def __init__(self, edistributor: _Optional[int] = ..., product_identifier: _Optional[str] = ..., start_queue_position: _Optional[int] = ...) -> None: ...

class CStore_DeleteReservationPositionMessage_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStore_GetAllReservationPositionMessages_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStore_GetAllReservationPositionMessages_Response(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _containers.RepeatedCompositeFieldContainer[CReservationPositionMessage]
    def __init__(self, settings: _Optional[_Iterable[_Union[CReservationPositionMessage, _Mapping]]] = ...) -> None: ...

class CStore_ReloadAllReservationPositionMessages_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamDeckCompatibility_SetFeedback_Request(_message.Message):
    __slots__ = ("appid", "feedback")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    appid: int
    feedback: _enums_pb2.ESteamDeckCompatibilityFeedback
    def __init__(self, appid: _Optional[int] = ..., feedback: _Optional[_Union[_enums_pb2.ESteamDeckCompatibilityFeedback, str]] = ...) -> None: ...

class CSteamDeckCompatibility_SetFeedback_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSteamDeckCompatibility_ShouldPrompt_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CSteamDeckCompatibility_ShouldPrompt_Response(_message.Message):
    __slots__ = ("prompt", "feedback_eligible", "existing_feedback")
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_ELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    EXISTING_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    prompt: bool
    feedback_eligible: bool
    existing_feedback: _enums_pb2.ESteamDeckCompatibilityFeedback
    def __init__(self, prompt: bool = ..., feedback_eligible: bool = ..., existing_feedback: _Optional[_Union[_enums_pb2.ESteamDeckCompatibilityFeedback, str]] = ...) -> None: ...

class CStore_StorePreferencesChanged_Notification(_message.Message):
    __slots__ = ("preferences", "tag_preferences", "content_descriptor_preferences")
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    TAG_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTOR_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    preferences: CStore_UserPreferences
    tag_preferences: CStore_UserTagPreferences
    content_descriptor_preferences: _steammessages_base_pb2.UserContentDescriptorPreferences
    def __init__(self, preferences: _Optional[_Union[CStore_UserPreferences, _Mapping]] = ..., tag_preferences: _Optional[_Union[CStore_UserTagPreferences, _Mapping]] = ..., content_descriptor_preferences: _Optional[_Union[_steammessages_base_pb2.UserContentDescriptorPreferences, _Mapping]] = ...) -> None: ...

class Store(_service.service): ...

class Store_Stub(Store): ...

class StoreClient(_service.service): ...

class StoreClient_Stub(StoreClient): ...
