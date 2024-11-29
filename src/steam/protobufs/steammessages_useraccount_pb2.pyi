import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EInternalAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EInternalSteamAccountType: _ClassVar[EInternalAccountType]
    k_EInternalClanType: _ClassVar[EInternalAccountType]
    k_EInternalAppType: _ClassVar[EInternalAccountType]
    k_EInternalBroadcastChannelType: _ClassVar[EInternalAccountType]

class EExternalAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EExternalNone: _ClassVar[EExternalAccountType]
    k_EExternalSteamAccount: _ClassVar[EExternalAccountType]
    k_EExternalGoogleAccount: _ClassVar[EExternalAccountType]
    k_EExternalFacebookAccount: _ClassVar[EExternalAccountType]
    k_EExternalTwitterAccount: _ClassVar[EExternalAccountType]
    k_EExternalTwitchAccount: _ClassVar[EExternalAccountType]
    k_EExternalYouTubeChannelAccount: _ClassVar[EExternalAccountType]
    k_EExternalFacebookPage: _ClassVar[EExternalAccountType]
k_EInternalSteamAccountType: EInternalAccountType
k_EInternalClanType: EInternalAccountType
k_EInternalAppType: EInternalAccountType
k_EInternalBroadcastChannelType: EInternalAccountType
k_EExternalNone: EExternalAccountType
k_EExternalSteamAccount: EExternalAccountType
k_EExternalGoogleAccount: EExternalAccountType
k_EExternalFacebookAccount: EExternalAccountType
k_EExternalTwitterAccount: EExternalAccountType
k_EExternalTwitchAccount: EExternalAccountType
k_EExternalYouTubeChannelAccount: EExternalAccountType
k_EExternalFacebookPage: EExternalAccountType

class CUserAccount_GetAvailableValveDiscountPromotions_Request(_message.Message):
    __slots__ = ("country_code",)
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    def __init__(self, country_code: _Optional[str] = ...) -> None: ...

class CUserAccount_GetAvailableValveDiscountPromotions_Response(_message.Message):
    __slots__ = ("promotions",)
    class ValveDiscountPromotionDetails(_message.Message):
        __slots__ = ("promotionid", "promotion_description", "minimum_cart_amount", "minimum_cart_amount_for_display", "discount_amount", "currency_code", "available_use_count", "promotional_discount_type", "loyalty_reward_id", "localized_name_token", "max_use_count")
        PROMOTIONID_FIELD_NUMBER: _ClassVar[int]
        PROMOTION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_CART_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_CART_AMOUNT_FOR_DISPLAY_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_USE_COUNT_FIELD_NUMBER: _ClassVar[int]
        PROMOTIONAL_DISCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOYALTY_REWARD_ID_FIELD_NUMBER: _ClassVar[int]
        LOCALIZED_NAME_TOKEN_FIELD_NUMBER: _ClassVar[int]
        MAX_USE_COUNT_FIELD_NUMBER: _ClassVar[int]
        promotionid: int
        promotion_description: str
        minimum_cart_amount: int
        minimum_cart_amount_for_display: int
        discount_amount: int
        currency_code: int
        available_use_count: int
        promotional_discount_type: int
        loyalty_reward_id: int
        localized_name_token: str
        max_use_count: int
        def __init__(self, promotionid: _Optional[int] = ..., promotion_description: _Optional[str] = ..., minimum_cart_amount: _Optional[int] = ..., minimum_cart_amount_for_display: _Optional[int] = ..., discount_amount: _Optional[int] = ..., currency_code: _Optional[int] = ..., available_use_count: _Optional[int] = ..., promotional_discount_type: _Optional[int] = ..., loyalty_reward_id: _Optional[int] = ..., localized_name_token: _Optional[str] = ..., max_use_count: _Optional[int] = ...) -> None: ...
    PROMOTIONS_FIELD_NUMBER: _ClassVar[int]
    promotions: _containers.RepeatedCompositeFieldContainer[CUserAccount_GetAvailableValveDiscountPromotions_Response.ValveDiscountPromotionDetails]
    def __init__(self, promotions: _Optional[_Iterable[_Union[CUserAccount_GetAvailableValveDiscountPromotions_Response.ValveDiscountPromotionDetails, _Mapping]]] = ...) -> None: ...

class CUserAccount_GetClientWalletDetails_Request(_message.Message):
    __slots__ = ("include_balance_in_usd", "wallet_region", "include_formatted_balance")
    INCLUDE_BALANCE_IN_USD_FIELD_NUMBER: _ClassVar[int]
    WALLET_REGION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FORMATTED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    include_balance_in_usd: bool
    wallet_region: int
    include_formatted_balance: bool
    def __init__(self, include_balance_in_usd: bool = ..., wallet_region: _Optional[int] = ..., include_formatted_balance: bool = ...) -> None: ...

class CUserAccount_GetWalletDetails_Response(_message.Message):
    __slots__ = ("has_wallet", "user_country_code", "wallet_country_code", "wallet_state", "balance", "delayed_balance", "currency_code", "time_most_recent_txn", "most_recent_txnid", "balance_in_usd", "delayed_balance_in_usd", "has_wallet_in_other_regions", "other_regions", "formatted_balance", "formatted_delayed_balance", "delayed_balance_available_min_time", "delayed_balance_available_max_time", "delayed_balance_newest_source")
    HAS_WALLET_FIELD_NUMBER: _ClassVar[int]
    USER_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    WALLET_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    WALLET_STATE_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    DELAYED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_MOST_RECENT_TXN_FIELD_NUMBER: _ClassVar[int]
    MOST_RECENT_TXNID_FIELD_NUMBER: _ClassVar[int]
    BALANCE_IN_USD_FIELD_NUMBER: _ClassVar[int]
    DELAYED_BALANCE_IN_USD_FIELD_NUMBER: _ClassVar[int]
    HAS_WALLET_IN_OTHER_REGIONS_FIELD_NUMBER: _ClassVar[int]
    OTHER_REGIONS_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_DELAYED_BALANCE_FIELD_NUMBER: _ClassVar[int]
    DELAYED_BALANCE_AVAILABLE_MIN_TIME_FIELD_NUMBER: _ClassVar[int]
    DELAYED_BALANCE_AVAILABLE_MAX_TIME_FIELD_NUMBER: _ClassVar[int]
    DELAYED_BALANCE_NEWEST_SOURCE_FIELD_NUMBER: _ClassVar[int]
    has_wallet: bool
    user_country_code: str
    wallet_country_code: str
    wallet_state: str
    balance: int
    delayed_balance: int
    currency_code: int
    time_most_recent_txn: int
    most_recent_txnid: int
    balance_in_usd: int
    delayed_balance_in_usd: int
    has_wallet_in_other_regions: bool
    other_regions: _containers.RepeatedScalarFieldContainer[int]
    formatted_balance: str
    formatted_delayed_balance: str
    delayed_balance_available_min_time: int
    delayed_balance_available_max_time: int
    delayed_balance_newest_source: int
    def __init__(self, has_wallet: bool = ..., user_country_code: _Optional[str] = ..., wallet_country_code: _Optional[str] = ..., wallet_state: _Optional[str] = ..., balance: _Optional[int] = ..., delayed_balance: _Optional[int] = ..., currency_code: _Optional[int] = ..., time_most_recent_txn: _Optional[int] = ..., most_recent_txnid: _Optional[int] = ..., balance_in_usd: _Optional[int] = ..., delayed_balance_in_usd: _Optional[int] = ..., has_wallet_in_other_regions: bool = ..., other_regions: _Optional[_Iterable[int]] = ..., formatted_balance: _Optional[str] = ..., formatted_delayed_balance: _Optional[str] = ..., delayed_balance_available_min_time: _Optional[int] = ..., delayed_balance_available_max_time: _Optional[int] = ..., delayed_balance_newest_source: _Optional[int] = ...) -> None: ...

class CUserAccount_GetAccountLinkStatus_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CUserAccount_GetAccountLinkStatus_Response(_message.Message):
    __slots__ = ("pwid", "identity_verification", "performed_age_verification")
    PWID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    PERFORMED_AGE_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    pwid: int
    identity_verification: int
    performed_age_verification: bool
    def __init__(self, pwid: _Optional[int] = ..., identity_verification: _Optional[int] = ..., performed_age_verification: bool = ...) -> None: ...

class CUserAccount_CancelLicenseForApp_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CUserAccount_CancelLicenseForApp_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CUserAccount_GetUserCountry_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CUserAccount_GetUserCountry_Response(_message.Message):
    __slots__ = ("country",)
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: str
    def __init__(self, country: _Optional[str] = ...) -> None: ...

class CUserAccount_CreateFriendInviteToken_Request(_message.Message):
    __slots__ = ("invite_limit", "invite_duration", "invite_note")
    INVITE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INVITE_DURATION_FIELD_NUMBER: _ClassVar[int]
    INVITE_NOTE_FIELD_NUMBER: _ClassVar[int]
    invite_limit: int
    invite_duration: int
    invite_note: str
    def __init__(self, invite_limit: _Optional[int] = ..., invite_duration: _Optional[int] = ..., invite_note: _Optional[str] = ...) -> None: ...

class CUserAccount_CreateFriendInviteToken_Response(_message.Message):
    __slots__ = ("invite_token", "invite_limit", "invite_duration", "time_created", "valid")
    INVITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INVITE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    INVITE_DURATION_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    invite_token: str
    invite_limit: int
    invite_duration: int
    time_created: int
    valid: bool
    def __init__(self, invite_token: _Optional[str] = ..., invite_limit: _Optional[int] = ..., invite_duration: _Optional[int] = ..., time_created: _Optional[int] = ..., valid: bool = ...) -> None: ...

class CUserAccount_GetFriendInviteTokens_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CUserAccount_GetFriendInviteTokens_Response(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[CUserAccount_CreateFriendInviteToken_Response]
    def __init__(self, tokens: _Optional[_Iterable[_Union[CUserAccount_CreateFriendInviteToken_Response, _Mapping]]] = ...) -> None: ...

class CUserAccount_ViewFriendInviteToken_Request(_message.Message):
    __slots__ = ("steamid", "invite_token")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INVITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    invite_token: str
    def __init__(self, steamid: _Optional[int] = ..., invite_token: _Optional[str] = ...) -> None: ...

class CUserAccount_ViewFriendInviteToken_Response(_message.Message):
    __slots__ = ("valid", "steamid", "invite_duration")
    VALID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INVITE_DURATION_FIELD_NUMBER: _ClassVar[int]
    valid: bool
    steamid: int
    invite_duration: int
    def __init__(self, valid: bool = ..., steamid: _Optional[int] = ..., invite_duration: _Optional[int] = ...) -> None: ...

class CUserAccount_RedeemFriendInviteToken_Request(_message.Message):
    __slots__ = ("steamid", "invite_token")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INVITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    invite_token: str
    def __init__(self, steamid: _Optional[int] = ..., invite_token: _Optional[str] = ...) -> None: ...

class CUserAccount_RedeemFriendInviteToken_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CUserAccount_RevokeFriendInviteToken_Request(_message.Message):
    __slots__ = ("invite_token",)
    INVITE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    invite_token: str
    def __init__(self, invite_token: _Optional[str] = ...) -> None: ...

class CUserAccount_RevokeFriendInviteToken_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CUserAccount_RegisterCompatTool_Request(_message.Message):
    __slots__ = ("compat_tool",)
    COMPAT_TOOL_FIELD_NUMBER: _ClassVar[int]
    compat_tool: int
    def __init__(self, compat_tool: _Optional[int] = ...) -> None: ...

class CUserAccount_RegisterCompatTool_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountLinking_GetLinkedAccountInfo_Request(_message.Message):
    __slots__ = ("account_type", "account_id", "filter", "return_access_token")
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    RETURN_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_type: EInternalAccountType
    account_id: int
    filter: EExternalAccountType
    return_access_token: bool
    def __init__(self, account_type: _Optional[_Union[EInternalAccountType, str]] = ..., account_id: _Optional[int] = ..., filter: _Optional[_Union[EExternalAccountType, str]] = ..., return_access_token: bool = ...) -> None: ...

class CAccountLinking_GetLinkedAccountInfo_Response(_message.Message):
    __slots__ = ("external_accounts",)
    class CExternalAccountTuple_Response(_message.Message):
        __slots__ = ("external_type", "external_id", "external_user_name", "external_url", "access_token", "access_token_secret", "is_valid")
        EXTERNAL_TYPE_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_USER_NAME_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_URL_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        ACCESS_TOKEN_SECRET_FIELD_NUMBER: _ClassVar[int]
        IS_VALID_FIELD_NUMBER: _ClassVar[int]
        external_type: EExternalAccountType
        external_id: str
        external_user_name: str
        external_url: str
        access_token: str
        access_token_secret: str
        is_valid: bool
        def __init__(self, external_type: _Optional[_Union[EExternalAccountType, str]] = ..., external_id: _Optional[str] = ..., external_user_name: _Optional[str] = ..., external_url: _Optional[str] = ..., access_token: _Optional[str] = ..., access_token_secret: _Optional[str] = ..., is_valid: bool = ...) -> None: ...
    EXTERNAL_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    external_accounts: _containers.RepeatedCompositeFieldContainer[CAccountLinking_GetLinkedAccountInfo_Response.CExternalAccountTuple_Response]
    def __init__(self, external_accounts: _Optional[_Iterable[_Union[CAccountLinking_GetLinkedAccountInfo_Response.CExternalAccountTuple_Response, _Mapping]]] = ...) -> None: ...

class CEmbeddedClient_AuthorizeCurrentDevice_Request(_message.Message):
    __slots__ = ("steamid", "appid", "device_info", "deviceid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    device_info: str
    deviceid: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ..., device_info: _Optional[str] = ..., deviceid: _Optional[int] = ...) -> None: ...

class CEmbeddedClient_Token(_message.Message):
    __slots__ = ("steamid", "client_token", "expiry", "deviceid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    client_token: bytes
    expiry: int
    deviceid: int
    def __init__(self, steamid: _Optional[int] = ..., client_token: _Optional[bytes] = ..., expiry: _Optional[int] = ..., deviceid: _Optional[int] = ...) -> None: ...

class CEmbeddedClient_AuthorizeDevice_Response(_message.Message):
    __slots__ = ("result", "token")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    result: int
    token: CEmbeddedClient_Token
    def __init__(self, result: _Optional[int] = ..., token: _Optional[_Union[CEmbeddedClient_Token, _Mapping]] = ...) -> None: ...

class UserAccount(_service.service): ...

class UserAccount_Stub(UserAccount): ...

class AccountLinking(_service.service): ...

class AccountLinking_Stub(AccountLinking): ...

class EmbeddedClient(_service.service): ...

class EmbeddedClient_Stub(EmbeddedClient): ...
