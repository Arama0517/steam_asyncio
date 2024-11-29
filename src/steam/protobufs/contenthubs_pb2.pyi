import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EContentHubDiscountFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EContentHubDiscountFilterType_None: _ClassVar[EContentHubDiscountFilterType]
    k_EContentHubDiscountFilterType_DiscountsOnly: _ClassVar[EContentHubDiscountFilterType]
    k_EContentHubDiscountFilterType_PrioritizeDiscounts: _ClassVar[EContentHubDiscountFilterType]
k_EContentHubDiscountFilterType_None: EContentHubDiscountFilterType
k_EContentHubDiscountFilterType_DiscountsOnly: EContentHubDiscountFilterType
k_EContentHubDiscountFilterType_PrioritizeDiscounts: EContentHubDiscountFilterType

class CStorePageFilter(_message.Message):
    __slots__ = ("sale_filter", "content_hub_filter", "store_filters")
    class SalePageFilter(_message.Message):
        __slots__ = ("sale_tagid",)
        SALE_TAGID_FIELD_NUMBER: _ClassVar[int]
        sale_tagid: int
        def __init__(self, sale_tagid: _Optional[int] = ...) -> None: ...
    class ContentHubFilter(_message.Message):
        __slots__ = ("hub_type", "hub_category", "hub_tagid", "discount_filter", "optin")
        class OptInInfo(_message.Message):
            __slots__ = ("name", "optin_tagid", "prune_tagid", "optin_only")
            NAME_FIELD_NUMBER: _ClassVar[int]
            OPTIN_TAGID_FIELD_NUMBER: _ClassVar[int]
            PRUNE_TAGID_FIELD_NUMBER: _ClassVar[int]
            OPTIN_ONLY_FIELD_NUMBER: _ClassVar[int]
            name: str
            optin_tagid: int
            prune_tagid: int
            optin_only: bool
            def __init__(self, name: _Optional[str] = ..., optin_tagid: _Optional[int] = ..., prune_tagid: _Optional[int] = ..., optin_only: bool = ...) -> None: ...
        HUB_TYPE_FIELD_NUMBER: _ClassVar[int]
        HUB_CATEGORY_FIELD_NUMBER: _ClassVar[int]
        HUB_TAGID_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_FILTER_FIELD_NUMBER: _ClassVar[int]
        OPTIN_FIELD_NUMBER: _ClassVar[int]
        hub_type: str
        hub_category: str
        hub_tagid: int
        discount_filter: EContentHubDiscountFilterType
        optin: CStorePageFilter.ContentHubFilter.OptInInfo
        def __init__(self, hub_type: _Optional[str] = ..., hub_category: _Optional[str] = ..., hub_tagid: _Optional[int] = ..., discount_filter: _Optional[_Union[EContentHubDiscountFilterType, str]] = ..., optin: _Optional[_Union[CStorePageFilter.ContentHubFilter.OptInInfo, _Mapping]] = ...) -> None: ...
    class StoreFilter(_message.Message):
        __slots__ = ("filter_json", "cache_key")
        FILTER_JSON_FIELD_NUMBER: _ClassVar[int]
        CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
        filter_json: str
        cache_key: str
        def __init__(self, filter_json: _Optional[str] = ..., cache_key: _Optional[str] = ...) -> None: ...
    SALE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HUB_FILTER_FIELD_NUMBER: _ClassVar[int]
    STORE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    sale_filter: CStorePageFilter.SalePageFilter
    content_hub_filter: CStorePageFilter.ContentHubFilter
    store_filters: _containers.RepeatedCompositeFieldContainer[CStorePageFilter.StoreFilter]
    def __init__(self, sale_filter: _Optional[_Union[CStorePageFilter.SalePageFilter, _Mapping]] = ..., content_hub_filter: _Optional[_Union[CStorePageFilter.ContentHubFilter, _Mapping]] = ..., store_filters: _Optional[_Iterable[_Union[CStorePageFilter.StoreFilter, _Mapping]]] = ...) -> None: ...
