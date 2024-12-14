import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CEcon_GetInventoryItemsWithDescriptions_Request(_message.Message):
    __slots__ = ("steamid", "appid", "contextid", "get_descriptions", "for_trade_offer_verification", "language", "filters", "start_assetid", "count")
    class FilterOptions(_message.Message):
        __slots__ = ("assetids", "currencyids", "tradable_only", "marketable_only")
        ASSETIDS_FIELD_NUMBER: _ClassVar[int]
        CURRENCYIDS_FIELD_NUMBER: _ClassVar[int]
        TRADABLE_ONLY_FIELD_NUMBER: _ClassVar[int]
        MARKETABLE_ONLY_FIELD_NUMBER: _ClassVar[int]
        assetids: _containers.RepeatedScalarFieldContainer[int]
        currencyids: _containers.RepeatedScalarFieldContainer[int]
        tradable_only: bool
        marketable_only: bool
        def __init__(self, assetids: _Optional[_Iterable[int]] = ..., currencyids: _Optional[_Iterable[int]] = ..., tradable_only: bool = ..., marketable_only: bool = ...) -> None: ...
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    GET_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    FOR_TRADE_OFFER_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    START_ASSETID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    contextid: int
    get_descriptions: bool
    for_trade_offer_verification: bool
    language: str
    filters: CEcon_GetInventoryItemsWithDescriptions_Request.FilterOptions
    start_assetid: int
    count: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ..., contextid: _Optional[int] = ..., get_descriptions: bool = ..., for_trade_offer_verification: bool = ..., language: _Optional[str] = ..., filters: _Optional[_Union[CEcon_GetInventoryItemsWithDescriptions_Request.FilterOptions, _Mapping]] = ..., start_assetid: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class CEcon_Asset(_message.Message):
    __slots__ = ("appid", "contextid", "assetid", "classid", "instanceid", "currencyid", "amount", "missing", "est_usd")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CONTEXTID_FIELD_NUMBER: _ClassVar[int]
    ASSETID_FIELD_NUMBER: _ClassVar[int]
    CLASSID_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    CURRENCYID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    EST_USD_FIELD_NUMBER: _ClassVar[int]
    appid: int
    contextid: int
    assetid: int
    classid: int
    instanceid: int
    currencyid: int
    amount: int
    missing: bool
    est_usd: int
    def __init__(self, appid: _Optional[int] = ..., contextid: _Optional[int] = ..., assetid: _Optional[int] = ..., classid: _Optional[int] = ..., instanceid: _Optional[int] = ..., currencyid: _Optional[int] = ..., amount: _Optional[int] = ..., missing: bool = ..., est_usd: _Optional[int] = ...) -> None: ...

class CEconItem_DescriptionLine(_message.Message):
    __slots__ = ("type", "value", "color", "label", "name")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    type: str
    value: str
    color: str
    label: str
    name: str
    def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ..., color: _Optional[str] = ..., label: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CEconItem_Action(_message.Message):
    __slots__ = ("link", "name")
    LINK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    link: str
    name: str
    def __init__(self, link: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CEconItem_Description(_message.Message):
    __slots__ = ("appid", "classid", "instanceid", "currency", "background_color", "icon_url", "icon_url_large", "descriptions", "tradable", "actions", "owner_descriptions", "owner_actions", "fraudwarnings", "name", "name_color", "type", "market_name", "market_hash_name", "market_fee", "market_fee_app", "contained_item", "market_actions", "commodity", "market_tradable_restriction", "market_marketable_restriction", "marketable", "tags", "item_expiration", "market_buy_country_restriction", "market_sell_country_restriction", "sealed")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLASSID_FIELD_NUMBER: _ClassVar[int]
    INSTANCEID_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_LARGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRADABLE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    OWNER_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    OWNER_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FRAUDWARNINGS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_COLOR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MARKET_NAME_FIELD_NUMBER: _ClassVar[int]
    MARKET_HASH_NAME_FIELD_NUMBER: _ClassVar[int]
    MARKET_FEE_FIELD_NUMBER: _ClassVar[int]
    MARKET_FEE_APP_FIELD_NUMBER: _ClassVar[int]
    CONTAINED_ITEM_FIELD_NUMBER: _ClassVar[int]
    MARKET_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    COMMODITY_FIELD_NUMBER: _ClassVar[int]
    MARKET_TRADABLE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    MARKET_MARKETABLE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    MARKETABLE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ITEM_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    MARKET_BUY_COUNTRY_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    MARKET_SELL_COUNTRY_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    SEALED_FIELD_NUMBER: _ClassVar[int]
    appid: int
    classid: int
    instanceid: int
    currency: bool
    background_color: str
    icon_url: str
    icon_url_large: str
    descriptions: _containers.RepeatedCompositeFieldContainer[CEconItem_DescriptionLine]
    tradable: bool
    actions: _containers.RepeatedCompositeFieldContainer[CEconItem_Action]
    owner_descriptions: _containers.RepeatedCompositeFieldContainer[CEconItem_DescriptionLine]
    owner_actions: _containers.RepeatedCompositeFieldContainer[CEconItem_Action]
    fraudwarnings: _containers.RepeatedScalarFieldContainer[str]
    name: str
    name_color: str
    type: str
    market_name: str
    market_hash_name: str
    market_fee: str
    market_fee_app: int
    contained_item: CEconItem_Description
    market_actions: _containers.RepeatedCompositeFieldContainer[CEconItem_Action]
    commodity: bool
    market_tradable_restriction: int
    market_marketable_restriction: int
    marketable: bool
    tags: _containers.RepeatedCompositeFieldContainer[CEconItem_Tag]
    item_expiration: str
    market_buy_country_restriction: str
    market_sell_country_restriction: str
    sealed: bool
    def __init__(self, appid: _Optional[int] = ..., classid: _Optional[int] = ..., instanceid: _Optional[int] = ..., currency: bool = ..., background_color: _Optional[str] = ..., icon_url: _Optional[str] = ..., icon_url_large: _Optional[str] = ..., descriptions: _Optional[_Iterable[_Union[CEconItem_DescriptionLine, _Mapping]]] = ..., tradable: bool = ..., actions: _Optional[_Iterable[_Union[CEconItem_Action, _Mapping]]] = ..., owner_descriptions: _Optional[_Iterable[_Union[CEconItem_DescriptionLine, _Mapping]]] = ..., owner_actions: _Optional[_Iterable[_Union[CEconItem_Action, _Mapping]]] = ..., fraudwarnings: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., name_color: _Optional[str] = ..., type: _Optional[str] = ..., market_name: _Optional[str] = ..., market_hash_name: _Optional[str] = ..., market_fee: _Optional[str] = ..., market_fee_app: _Optional[int] = ..., contained_item: _Optional[_Union[CEconItem_Description, _Mapping]] = ..., market_actions: _Optional[_Iterable[_Union[CEconItem_Action, _Mapping]]] = ..., commodity: bool = ..., market_tradable_restriction: _Optional[int] = ..., market_marketable_restriction: _Optional[int] = ..., marketable: bool = ..., tags: _Optional[_Iterable[_Union[CEconItem_Tag, _Mapping]]] = ..., item_expiration: _Optional[str] = ..., market_buy_country_restriction: _Optional[str] = ..., market_sell_country_restriction: _Optional[str] = ..., sealed: bool = ...) -> None: ...

class CEconItem_Tag(_message.Message):
    __slots__ = ("appid", "category", "internal_name", "localized_category_name", "localized_tag_name", "color")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCALIZED_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    appid: int
    category: str
    internal_name: str
    localized_category_name: str
    localized_tag_name: str
    color: str
    def __init__(self, appid: _Optional[int] = ..., category: _Optional[str] = ..., internal_name: _Optional[str] = ..., localized_category_name: _Optional[str] = ..., localized_tag_name: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class CEcon_GetInventoryItemsWithDescriptions_Response(_message.Message):
    __slots__ = ("assets", "descriptions", "missing_assets", "more_items", "last_assetid", "total_inventory_count")
    ASSETS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    MISSING_ASSETS_FIELD_NUMBER: _ClassVar[int]
    MORE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    LAST_ASSETID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INVENTORY_COUNT_FIELD_NUMBER: _ClassVar[int]
    assets: _containers.RepeatedCompositeFieldContainer[CEcon_Asset]
    descriptions: _containers.RepeatedCompositeFieldContainer[CEconItem_Description]
    missing_assets: _containers.RepeatedCompositeFieldContainer[CEcon_Asset]
    more_items: bool
    last_assetid: int
    total_inventory_count: int
    def __init__(self, assets: _Optional[_Iterable[_Union[CEcon_Asset, _Mapping]]] = ..., descriptions: _Optional[_Iterable[_Union[CEconItem_Description, _Mapping]]] = ..., missing_assets: _Optional[_Iterable[_Union[CEcon_Asset, _Mapping]]] = ..., more_items: bool = ..., last_assetid: _Optional[int] = ..., total_inventory_count: _Optional[int] = ...) -> None: ...

class CEcon_GetTradeOfferAccessToken_Request(_message.Message):
    __slots__ = ("generate_new_token",)
    GENERATE_NEW_TOKEN_FIELD_NUMBER: _ClassVar[int]
    generate_new_token: bool
    def __init__(self, generate_new_token: bool = ...) -> None: ...

class CEcon_GetTradeOfferAccessToken_Response(_message.Message):
    __slots__ = ("trade_offer_access_token",)
    TRADE_OFFER_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    trade_offer_access_token: str
    def __init__(self, trade_offer_access_token: _Optional[str] = ...) -> None: ...

class CEcon_ClientGetItemShopOverlayAuthURL_Request(_message.Message):
    __slots__ = ("return_url",)
    RETURN_URL_FIELD_NUMBER: _ClassVar[int]
    return_url: str
    def __init__(self, return_url: _Optional[str] = ...) -> None: ...

class CEcon_ClientGetItemShopOverlayAuthURL_Response(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CEcon_GetAssetClassInfo_Request(_message.Message):
    __slots__ = ("language", "appid", "classes", "high_pri")
    class Class(_message.Message):
        __slots__ = ("classid", "instanceid")
        CLASSID_FIELD_NUMBER: _ClassVar[int]
        INSTANCEID_FIELD_NUMBER: _ClassVar[int]
        classid: int
        instanceid: int
        def __init__(self, classid: _Optional[int] = ..., instanceid: _Optional[int] = ...) -> None: ...
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    CLASSES_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRI_FIELD_NUMBER: _ClassVar[int]
    language: str
    appid: int
    classes: _containers.RepeatedCompositeFieldContainer[CEcon_GetAssetClassInfo_Request.Class]
    high_pri: bool
    def __init__(self, language: _Optional[str] = ..., appid: _Optional[int] = ..., classes: _Optional[_Iterable[_Union[CEcon_GetAssetClassInfo_Request.Class, _Mapping]]] = ..., high_pri: bool = ...) -> None: ...

class CEcon_GetAssetClassInfo_Response(_message.Message):
    __slots__ = ("descriptions",)
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    descriptions: _containers.RepeatedCompositeFieldContainer[CEconItem_Description]
    def __init__(self, descriptions: _Optional[_Iterable[_Union[CEconItem_Description, _Mapping]]] = ...) -> None: ...

class Econ(_service.service): ...

class Econ_Stub(Econ): ...
