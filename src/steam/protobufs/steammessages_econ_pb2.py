# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_econ.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'steammessages_econ.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18steammessages_econ.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"\x95\x03\n/CEcon_GetInventoryItemsWithDescriptions_Request\x12\x0f\n\x07steamid\x18\x01 \x01(\x06\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x11\n\tcontextid\x18\x03 \x01(\x04\x12\x18\n\x10get_descriptions\x18\x04 \x01(\x08\x12$\n\x1c\x66or_trade_offer_verification\x18\n \x01(\x08\x12\x10\n\x08language\x18\x05 \x01(\t\x12O\n\x07\x66ilters\x18\x06 \x01(\x0b\x32>.CEcon_GetInventoryItemsWithDescriptions_Request.FilterOptions\x12\x15\n\rstart_assetid\x18\x08 \x01(\x04\x12\r\n\x05\x63ount\x18\t \x01(\x05\x1a\x66\n\rFilterOptions\x12\x10\n\x08\x61ssetids\x18\x01 \x03(\x04\x12\x13\n\x0b\x63urrencyids\x18\x02 \x03(\r\x12\x15\n\rtradable_only\x18\x03 \x01(\x08\x12\x17\n\x0fmarketable_only\x18\x04 \x01(\x08\"\xab\x01\n\x0b\x43\x45\x63on_Asset\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x11\n\tcontextid\x18\x02 \x01(\x04\x12\x0f\n\x07\x61ssetid\x18\x03 \x01(\x04\x12\x0f\n\x07\x63lassid\x18\x04 \x01(\x04\x12\x12\n\ninstanceid\x18\x05 \x01(\x04\x12\x12\n\ncurrencyid\x18\x06 \x01(\r\x12\x0e\n\x06\x61mount\x18\x07 \x01(\x03\x12\x0f\n\x07missing\x18\x08 \x01(\x08\x12\x0f\n\x07\x65st_usd\x18\t \x01(\x03\"V\n\x19\x43\x45\x63onItem_DescriptionLine\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\".\n\x10\x43\x45\x63onItem_Action\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xe3\x06\n\x15\x43\x45\x63onItem_Description\x12\r\n\x05\x61ppid\x18\x01 \x01(\x05\x12\x0f\n\x07\x63lassid\x18\x02 \x01(\x04\x12\x12\n\ninstanceid\x18\x03 \x01(\x04\x12\x10\n\x08\x63urrency\x18\x04 \x01(\x08\x12\x18\n\x10\x62\x61\x63kground_color\x18\x05 \x01(\t\x12\x10\n\x08icon_url\x18\x06 \x01(\t\x12\x16\n\x0eicon_url_large\x18\x07 \x01(\t\x12\x30\n\x0c\x64\x65scriptions\x18\x08 \x03(\x0b\x32\x1a.CEconItem_DescriptionLine\x12\x10\n\x08tradable\x18\t \x01(\x08\x12\"\n\x07\x61\x63tions\x18\n \x03(\x0b\x32\x11.CEconItem_Action\x12\x36\n\x12owner_descriptions\x18\x0b \x03(\x0b\x32\x1a.CEconItem_DescriptionLine\x12(\n\rowner_actions\x18\x0c \x03(\x0b\x32\x11.CEconItem_Action\x12\x15\n\rfraudwarnings\x18\r \x03(\t\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x12\n\nname_color\x18\x0f \x01(\t\x12\x0c\n\x04type\x18\x10 \x01(\t\x12\x13\n\x0bmarket_name\x18\x11 \x01(\t\x12\x18\n\x10market_hash_name\x18\x12 \x01(\t\x12\x12\n\nmarket_fee\x18\x13 \x01(\t\x12\x16\n\x0emarket_fee_app\x18\x1c \x01(\x05\x12.\n\x0e\x63ontained_item\x18\x14 \x01(\x0b\x32\x16.CEconItem_Description\x12)\n\x0emarket_actions\x18\x15 \x03(\x0b\x32\x11.CEconItem_Action\x12\x11\n\tcommodity\x18\x16 \x01(\x08\x12#\n\x1bmarket_tradable_restriction\x18\x17 \x01(\x05\x12%\n\x1dmarket_marketable_restriction\x18\x18 \x01(\x05\x12\x12\n\nmarketable\x18\x19 \x01(\x08\x12\x1c\n\x04tags\x18\x1a \x03(\x0b\x32\x0e.CEconItem_Tag\x12\x17\n\x0fitem_expiration\x18\x1b \x01(\t\x12&\n\x1emarket_buy_country_restriction\x18\x1e \x01(\t\x12\'\n\x1fmarket_sell_country_restriction\x18\x1f \x01(\t\"\x93\x01\n\rCEconItem_Tag\x12\r\n\x05\x61ppid\x18\x01 \x01(\r\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12\x15\n\rinternal_name\x18\x03 \x01(\t\x12\x1f\n\x17localized_category_name\x18\x04 \x01(\t\x12\x1a\n\x12localized_tag_name\x18\x05 \x01(\t\x12\r\n\x05\x63olor\x18\x06 \x01(\t\"\xed\x01\n0CEcon_GetInventoryItemsWithDescriptions_Response\x12\x1c\n\x06\x61ssets\x18\x01 \x03(\x0b\x32\x0c.CEcon_Asset\x12,\n\x0c\x64\x65scriptions\x18\x02 \x03(\x0b\x32\x16.CEconItem_Description\x12$\n\x0emissing_assets\x18\x03 \x03(\x0b\x32\x0c.CEcon_Asset\x12\x12\n\nmore_items\x18\x04 \x01(\x08\x12\x14\n\x0clast_assetid\x18\x05 \x01(\x04\x12\x1d\n\x15total_inventory_count\x18\x06 \x01(\r\"D\n&CEcon_GetTradeOfferAccessToken_Request\x12\x1a\n\x12generate_new_token\x18\x01 \x01(\x08\"K\n\'CEcon_GetTradeOfferAccessToken_Response\x12 \n\x18trade_offer_access_token\x18\x01 \x01(\t\"C\n-CEcon_ClientGetItemShopOverlayAuthURL_Request\x12\x12\n\nreturn_url\x18\x01 \x01(\t\"=\n.CEcon_ClientGetItemShopOverlayAuthURL_Response\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xbb\x01\n\x1f\x43\x45\x63on_GetAssetClassInfo_Request\x12\x10\n\x08language\x18\x01 \x01(\t\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x37\n\x07\x63lasses\x18\x03 \x03(\x0b\x32&.CEcon_GetAssetClassInfo_Request.Class\x12\x10\n\x08high_pri\x18\x04 \x01(\x08\x1a,\n\x05\x43lass\x12\x0f\n\x07\x63lassid\x18\x01 \x01(\x04\x12\x12\n\ninstanceid\x18\x02 \x01(\x04\"P\n CEcon_GetAssetClassInfo_Response\x12,\n\x0c\x64\x65scriptions\x18\x01 \x03(\x0b\x32\x16.CEconItem_Description2\xdf\x03\n\x04\x45\x63on\x12\x88\x01\n!GetInventoryItemsWithDescriptions\x12\x30.CEcon_GetInventoryItemsWithDescriptions_Request\x1a\x31.CEcon_GetInventoryItemsWithDescriptions_Response\x12m\n\x18GetTradeOfferAccessToken\x12\'.CEcon_GetTradeOfferAccessToken_Request\x1a(.CEcon_GetTradeOfferAccessToken_Response\x12\x82\x01\n\x1f\x43lientGetItemShopOverlayAuthURL\x12..CEcon_ClientGetItemShopOverlayAuthURL_Request\x1a/.CEcon_ClientGetItemShopOverlayAuthURL_Response\x12X\n\x11GetAssetClassInfo\x12 .CEcon_GetAssetClassInfo_Request\x1a!.CEcon_GetAssetClassInfo_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_econ_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_CECON_GETINVENTORYITEMSWITHDESCRIPTIONS_REQUEST']._serialized_start=89
  _globals['_CECON_GETINVENTORYITEMSWITHDESCRIPTIONS_REQUEST']._serialized_end=494
  _globals['_CECON_GETINVENTORYITEMSWITHDESCRIPTIONS_REQUEST_FILTEROPTIONS']._serialized_start=392
  _globals['_CECON_GETINVENTORYITEMSWITHDESCRIPTIONS_REQUEST_FILTEROPTIONS']._serialized_end=494
  _globals['_CECON_ASSET']._serialized_start=497
  _globals['_CECON_ASSET']._serialized_end=668
  _globals['_CECONITEM_DESCRIPTIONLINE']._serialized_start=670
  _globals['_CECONITEM_DESCRIPTIONLINE']._serialized_end=756
  _globals['_CECONITEM_ACTION']._serialized_start=758
  _globals['_CECONITEM_ACTION']._serialized_end=804
  _globals['_CECONITEM_DESCRIPTION']._serialized_start=807
  _globals['_CECONITEM_DESCRIPTION']._serialized_end=1674
  _globals['_CECONITEM_TAG']._serialized_start=1677
  _globals['_CECONITEM_TAG']._serialized_end=1824
  _globals['_CECON_GETINVENTORYITEMSWITHDESCRIPTIONS_RESPONSE']._serialized_start=1827
  _globals['_CECON_GETINVENTORYITEMSWITHDESCRIPTIONS_RESPONSE']._serialized_end=2064
  _globals['_CECON_GETTRADEOFFERACCESSTOKEN_REQUEST']._serialized_start=2066
  _globals['_CECON_GETTRADEOFFERACCESSTOKEN_REQUEST']._serialized_end=2134
  _globals['_CECON_GETTRADEOFFERACCESSTOKEN_RESPONSE']._serialized_start=2136
  _globals['_CECON_GETTRADEOFFERACCESSTOKEN_RESPONSE']._serialized_end=2211
  _globals['_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_REQUEST']._serialized_start=2213
  _globals['_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_REQUEST']._serialized_end=2280
  _globals['_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_RESPONSE']._serialized_start=2282
  _globals['_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_RESPONSE']._serialized_end=2343
  _globals['_CECON_GETASSETCLASSINFO_REQUEST']._serialized_start=2346
  _globals['_CECON_GETASSETCLASSINFO_REQUEST']._serialized_end=2533
  _globals['_CECON_GETASSETCLASSINFO_REQUEST_CLASS']._serialized_start=2489
  _globals['_CECON_GETASSETCLASSINFO_REQUEST_CLASS']._serialized_end=2533
  _globals['_CECON_GETASSETCLASSINFO_RESPONSE']._serialized_start=2535
  _globals['_CECON_GETASSETCLASSINFO_RESPONSE']._serialized_end=2615
  _globals['_ECON']._serialized_start=2618
  _globals['_ECON']._serialized_end=3097
_builder.BuildServices(DESCRIPTOR, 'steammessages_econ_pb2', _globals)
# @@protoc_insertion_point(module_scope)