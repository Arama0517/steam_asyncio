import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CInventory_GetInventory_Request(_message.Message):
    __slots__ = ("appid", "steamid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CInventory_Response(_message.Message):
    __slots__ = ("etag", "removeditemids", "item_json", "itemdef_json", "ticket", "replayed")
    ETAG_FIELD_NUMBER: _ClassVar[int]
    REMOVEDITEMIDS_FIELD_NUMBER: _ClassVar[int]
    ITEM_JSON_FIELD_NUMBER: _ClassVar[int]
    ITEMDEF_JSON_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    REPLAYED_FIELD_NUMBER: _ClassVar[int]
    etag: str
    removeditemids: _containers.RepeatedScalarFieldContainer[int]
    item_json: str
    itemdef_json: str
    ticket: bytes
    replayed: bool
    def __init__(self, etag: _Optional[str] = ..., removeditemids: _Optional[_Iterable[int]] = ..., item_json: _Optional[str] = ..., itemdef_json: _Optional[str] = ..., ticket: _Optional[bytes] = ..., replayed: bool = ...) -> None: ...

class CInventory_ExchangeItem_Request(_message.Message):
    __slots__ = ("appid", "steamid", "materialsitemid", "materialsquantity", "outputitemdefid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    MATERIALSITEMID_FIELD_NUMBER: _ClassVar[int]
    MATERIALSQUANTITY_FIELD_NUMBER: _ClassVar[int]
    OUTPUTITEMDEFID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    steamid: int
    materialsitemid: _containers.RepeatedScalarFieldContainer[int]
    materialsquantity: _containers.RepeatedScalarFieldContainer[int]
    outputitemdefid: int
    def __init__(self, appid: _Optional[int] = ..., steamid: _Optional[int] = ..., materialsitemid: _Optional[_Iterable[int]] = ..., materialsquantity: _Optional[_Iterable[int]] = ..., outputitemdefid: _Optional[int] = ...) -> None: ...

class CInventory_GetEligiblePromoItemDefIDs_Request(_message.Message):
    __slots__ = ("appid", "steamid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CInventory_GetEligiblePromoItemDefIDs_Response(_message.Message):
    __slots__ = ("itemdefids",)
    ITEMDEFIDS_FIELD_NUMBER: _ClassVar[int]
    itemdefids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, itemdefids: _Optional[_Iterable[int]] = ...) -> None: ...

class CInventory_AddItem_Request(_message.Message):
    __slots__ = ("appid", "itemdefid", "itempropsjson", "itemquantity", "steamid", "notify", "requestid", "trade_restriction", "is_purchase")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFID_FIELD_NUMBER: _ClassVar[int]
    ITEMPROPSJSON_FIELD_NUMBER: _ClassVar[int]
    ITEMQUANTITY_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    NOTIFY_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    TRADE_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    IS_PURCHASE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    itemdefid: _containers.RepeatedScalarFieldContainer[int]
    itempropsjson: _containers.RepeatedScalarFieldContainer[str]
    itemquantity: _containers.RepeatedScalarFieldContainer[int]
    steamid: int
    notify: bool
    requestid: int
    trade_restriction: bool
    is_purchase: bool
    def __init__(self, appid: _Optional[int] = ..., itemdefid: _Optional[_Iterable[int]] = ..., itempropsjson: _Optional[_Iterable[str]] = ..., itemquantity: _Optional[_Iterable[int]] = ..., steamid: _Optional[int] = ..., notify: bool = ..., requestid: _Optional[int] = ..., trade_restriction: bool = ..., is_purchase: bool = ...) -> None: ...

class CInventory_ModifyItems_Request(_message.Message):
    __slots__ = ("appid", "steamid", "updates", "timestamp")
    class ItemPropertyUpdate(_message.Message):
        __slots__ = ("itemid", "remove_property", "property_name", "property_value_bool", "property_value_int", "property_value_string", "property_value_float")
        ITEMID_FIELD_NUMBER: _ClassVar[int]
        REMOVE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_NAME_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_VALUE_BOOL_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_VALUE_INT_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_VALUE_STRING_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_VALUE_FLOAT_FIELD_NUMBER: _ClassVar[int]
        itemid: int
        remove_property: bool
        property_name: str
        property_value_bool: bool
        property_value_int: int
        property_value_string: str
        property_value_float: float
        def __init__(self, itemid: _Optional[int] = ..., remove_property: bool = ..., property_name: _Optional[str] = ..., property_value_bool: bool = ..., property_value_int: _Optional[int] = ..., property_value_string: _Optional[str] = ..., property_value_float: _Optional[float] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    appid: int
    steamid: int
    updates: _containers.RepeatedCompositeFieldContainer[CInventory_ModifyItems_Request.ItemPropertyUpdate]
    timestamp: int
    def __init__(self, appid: _Optional[int] = ..., steamid: _Optional[int] = ..., updates: _Optional[_Iterable[_Union[CInventory_ModifyItems_Request.ItemPropertyUpdate, _Mapping]]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CInventory_ConsumePlaytime_Request(_message.Message):
    __slots__ = ("appid", "itemdefid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    itemdefid: int
    def __init__(self, appid: _Optional[int] = ..., itemdefid: _Optional[int] = ...) -> None: ...

class CInventory_ConsumeItem_Request(_message.Message):
    __slots__ = ("appid", "itemid", "quantity", "timestamp", "steamid", "requestid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    itemid: int
    quantity: int
    timestamp: str
    steamid: int
    requestid: int
    def __init__(self, appid: _Optional[int] = ..., itemid: _Optional[int] = ..., quantity: _Optional[int] = ..., timestamp: _Optional[str] = ..., steamid: _Optional[int] = ..., requestid: _Optional[int] = ...) -> None: ...

class CInventory_DevSetNextDrop_Request(_message.Message):
    __slots__ = ("appid", "itemdefid", "droptime")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ITEMDEFID_FIELD_NUMBER: _ClassVar[int]
    DROPTIME_FIELD_NUMBER: _ClassVar[int]
    appid: int
    itemdefid: int
    droptime: str
    def __init__(self, appid: _Optional[int] = ..., itemdefid: _Optional[int] = ..., droptime: _Optional[str] = ...) -> None: ...

class CInventory_SplitItemStack_Request(_message.Message):
    __slots__ = ("appid", "itemid", "quantity", "steamid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    itemid: int
    quantity: int
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., itemid: _Optional[int] = ..., quantity: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CInventory_CombineItemStacks_Request(_message.Message):
    __slots__ = ("appid", "fromitemid", "destitemid", "quantity", "steamid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    FROMITEMID_FIELD_NUMBER: _ClassVar[int]
    DESTITEMID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    fromitemid: int
    destitemid: int
    quantity: int
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., fromitemid: _Optional[int] = ..., destitemid: _Optional[int] = ..., quantity: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CInventory_GetItemDefMeta_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CInventory_GetItemDefMeta_Response(_message.Message):
    __slots__ = ("modified", "digest")
    MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    modified: int
    digest: str
    def __init__(self, modified: _Optional[int] = ..., digest: _Optional[str] = ...) -> None: ...

class CInventory_GetUserPurchaseInfo_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CInventory_GetUserPurchaseInfo_Response(_message.Message):
    __slots__ = ("ecurrency",)
    ECURRENCY_FIELD_NUMBER: _ClassVar[int]
    ecurrency: int
    def __init__(self, ecurrency: _Optional[int] = ...) -> None: ...

class CInventory_PurchaseInit_Request(_message.Message):
    __slots__ = ("appid", "language", "line_items")
    class LineItem(_message.Message):
        __slots__ = ("itemdefid", "quantity")
        ITEMDEFID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        itemdefid: int
        quantity: int
        def __init__(self, itemdefid: _Optional[int] = ..., quantity: _Optional[int] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    language: int
    line_items: _containers.RepeatedCompositeFieldContainer[CInventory_PurchaseInit_Request.LineItem]
    def __init__(self, appid: _Optional[int] = ..., language: _Optional[int] = ..., line_items: _Optional[_Iterable[_Union[CInventory_PurchaseInit_Request.LineItem, _Mapping]]] = ...) -> None: ...

class CInventory_PurchaseInit_Response(_message.Message):
    __slots__ = ("orderid", "transid")
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    TRANSID_FIELD_NUMBER: _ClassVar[int]
    orderid: int
    transid: int
    def __init__(self, orderid: _Optional[int] = ..., transid: _Optional[int] = ...) -> None: ...

class CInventory_PurchaseFinalize_Request(_message.Message):
    __slots__ = ("appid", "language", "orderid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ORDERID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    language: int
    orderid: int
    def __init__(self, appid: _Optional[int] = ..., language: _Optional[int] = ..., orderid: _Optional[int] = ...) -> None: ...

class CInventory_InspectItem_Request(_message.Message):
    __slots__ = ("itemdefid", "itemid", "tags")
    ITEMDEFID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    itemdefid: int
    itemid: int
    tags: str
    def __init__(self, itemdefid: _Optional[int] = ..., itemid: _Optional[int] = ..., tags: _Optional[str] = ...) -> None: ...

class CInventoryClient_NewItems_Notification(_message.Message):
    __slots__ = ("appid", "inventory_response")
    APPID_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    inventory_response: CInventory_Response
    def __init__(self, appid: _Optional[int] = ..., inventory_response: _Optional[_Union[CInventory_Response, _Mapping]] = ...) -> None: ...

class Inventory(_service.service): ...

class Inventory_Stub(Inventory): ...

class InventoryClient(_service.service): ...

class InventoryClient_Stub(InventoryClient): ...
