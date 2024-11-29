import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CDeviceAuth_GetOwnAuthorizedDevices_Request(_message.Message):
    __slots__ = ("steamid", "include_canceled")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CANCELED_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_canceled: bool
    def __init__(self, steamid: _Optional[int] = ..., include_canceled: bool = ...) -> None: ...

class CDeviceAuth_GetOwnAuthorizedDevices_Response(_message.Message):
    __slots__ = ("devices",)
    class Device(_message.Message):
        __slots__ = ("auth_device_token", "device_name", "is_pending", "is_canceled", "last_time_used", "last_borrower_id", "last_app_played", "is_limited")
        AUTH_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_CANCELED_FIELD_NUMBER: _ClassVar[int]
        LAST_TIME_USED_FIELD_NUMBER: _ClassVar[int]
        LAST_BORROWER_ID_FIELD_NUMBER: _ClassVar[int]
        LAST_APP_PLAYED_FIELD_NUMBER: _ClassVar[int]
        IS_LIMITED_FIELD_NUMBER: _ClassVar[int]
        auth_device_token: int
        device_name: str
        is_pending: bool
        is_canceled: bool
        last_time_used: int
        last_borrower_id: int
        last_app_played: int
        is_limited: bool
        def __init__(self, auth_device_token: _Optional[int] = ..., device_name: _Optional[str] = ..., is_pending: bool = ..., is_canceled: bool = ..., last_time_used: _Optional[int] = ..., last_borrower_id: _Optional[int] = ..., last_app_played: _Optional[int] = ..., is_limited: bool = ...) -> None: ...
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetOwnAuthorizedDevices_Response.Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[CDeviceAuth_GetOwnAuthorizedDevices_Response.Device, _Mapping]]] = ...) -> None: ...

class CDeviceAuth_AcceptAuthorizationRequest_Request(_message.Message):
    __slots__ = ("steamid", "auth_device_token", "auth_code", "from_steamid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTH_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AUTH_CODE_FIELD_NUMBER: _ClassVar[int]
    FROM_STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    auth_device_token: int
    auth_code: int
    from_steamid: int
    def __init__(self, steamid: _Optional[int] = ..., auth_device_token: _Optional[int] = ..., auth_code: _Optional[int] = ..., from_steamid: _Optional[int] = ...) -> None: ...

class CDeviceAuth_AcceptAuthorizationRequest_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDeviceAuth_AuthorizeRemoteDevice_Request(_message.Message):
    __slots__ = ("steamid", "auth_device_token")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTH_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    auth_device_token: int
    def __init__(self, steamid: _Optional[int] = ..., auth_device_token: _Optional[int] = ...) -> None: ...

class CDeviceAuth_AuthorizeRemoteDevice_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDeviceAuth_DeauthorizeRemoteDevice_Request(_message.Message):
    __slots__ = ("steamid", "auth_device_token")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTH_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    auth_device_token: int
    def __init__(self, steamid: _Optional[int] = ..., auth_device_token: _Optional[int] = ...) -> None: ...

class CDeviceAuth_DeauthorizeRemoteDevice_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDeviceAuth_GetUsedAuthorizedDevices_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CDeviceAuth_GetUsedAuthorizedDevices_Response(_message.Message):
    __slots__ = ("devices",)
    class Device(_message.Message):
        __slots__ = ("auth_device_token", "device_name", "owner_steamid", "last_time_used", "last_app_played")
        AUTH_DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
        LAST_TIME_USED_FIELD_NUMBER: _ClassVar[int]
        LAST_APP_PLAYED_FIELD_NUMBER: _ClassVar[int]
        auth_device_token: int
        device_name: str
        owner_steamid: int
        last_time_used: int
        last_app_played: int
        def __init__(self, auth_device_token: _Optional[int] = ..., device_name: _Optional[str] = ..., owner_steamid: _Optional[int] = ..., last_time_used: _Optional[int] = ..., last_app_played: _Optional[int] = ...) -> None: ...
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetUsedAuthorizedDevices_Response.Device]
    def __init__(self, devices: _Optional[_Iterable[_Union[CDeviceAuth_GetUsedAuthorizedDevices_Response.Device, _Mapping]]] = ...) -> None: ...

class CDeviceAuth_GetAuthorizedBorrowers_Request(_message.Message):
    __slots__ = ("steamid", "include_canceled", "include_pending")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CANCELED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PENDING_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_canceled: bool
    include_pending: bool
    def __init__(self, steamid: _Optional[int] = ..., include_canceled: bool = ..., include_pending: bool = ...) -> None: ...

class CDeviceAuth_GetAuthorizedBorrowers_Response(_message.Message):
    __slots__ = ("borrowers",)
    class Borrower(_message.Message):
        __slots__ = ("steamid", "is_pending", "is_canceled", "time_created")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_CANCELED_FIELD_NUMBER: _ClassVar[int]
        TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        is_pending: bool
        is_canceled: bool
        time_created: int
        def __init__(self, steamid: _Optional[int] = ..., is_pending: bool = ..., is_canceled: bool = ..., time_created: _Optional[int] = ...) -> None: ...
    BORROWERS_FIELD_NUMBER: _ClassVar[int]
    borrowers: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetAuthorizedBorrowers_Response.Borrower]
    def __init__(self, borrowers: _Optional[_Iterable[_Union[CDeviceAuth_GetAuthorizedBorrowers_Response.Borrower, _Mapping]]] = ...) -> None: ...

class CDeviceAuth_AddAuthorizedBorrowers_Request(_message.Message):
    __slots__ = ("steamid", "steamid_borrower")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_BORROWER_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    steamid_borrower: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid: _Optional[int] = ..., steamid_borrower: _Optional[_Iterable[int]] = ...) -> None: ...

class CDeviceAuth_AddAuthorizedBorrowers_Response(_message.Message):
    __slots__ = ("seconds_to_wait",)
    SECONDS_TO_WAIT_FIELD_NUMBER: _ClassVar[int]
    seconds_to_wait: int
    def __init__(self, seconds_to_wait: _Optional[int] = ...) -> None: ...

class CDeviceAuth_RemoveAuthorizedBorrowers_Request(_message.Message):
    __slots__ = ("steamid", "steamid_borrower")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_BORROWER_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    steamid_borrower: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, steamid: _Optional[int] = ..., steamid_borrower: _Optional[_Iterable[int]] = ...) -> None: ...

class CDeviceAuth_RemoveAuthorizedBorrowers_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDeviceAuth_GetAuthorizedAsBorrower_Request(_message.Message):
    __slots__ = ("steamid", "include_canceled", "include_pending")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CANCELED_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PENDING_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_canceled: bool
    include_pending: bool
    def __init__(self, steamid: _Optional[int] = ..., include_canceled: bool = ..., include_pending: bool = ...) -> None: ...

class CDeviceAuth_GetAuthorizedAsBorrower_Response(_message.Message):
    __slots__ = ("lenders",)
    class Lender(_message.Message):
        __slots__ = ("steamid", "time_created", "is_pending", "is_canceled", "is_used", "time_removed", "time_first")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
        IS_PENDING_FIELD_NUMBER: _ClassVar[int]
        IS_CANCELED_FIELD_NUMBER: _ClassVar[int]
        IS_USED_FIELD_NUMBER: _ClassVar[int]
        TIME_REMOVED_FIELD_NUMBER: _ClassVar[int]
        TIME_FIRST_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        time_created: int
        is_pending: bool
        is_canceled: bool
        is_used: bool
        time_removed: int
        time_first: int
        def __init__(self, steamid: _Optional[int] = ..., time_created: _Optional[int] = ..., is_pending: bool = ..., is_canceled: bool = ..., is_used: bool = ..., time_removed: _Optional[int] = ..., time_first: _Optional[int] = ...) -> None: ...
    LENDERS_FIELD_NUMBER: _ClassVar[int]
    lenders: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetAuthorizedAsBorrower_Response.Lender]
    def __init__(self, lenders: _Optional[_Iterable[_Union[CDeviceAuth_GetAuthorizedAsBorrower_Response.Lender, _Mapping]]] = ...) -> None: ...

class CDeviceAuth_GetExcludedGamesInLibrary_Request(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CDeviceAuth_GetExcludedGamesInLibrary_Response(_message.Message):
    __slots__ = ("excluded_games",)
    class ExcludedGame(_message.Message):
        __slots__ = ("appid", "game_name", "vac_banned", "package_excluded")
        APPID_FIELD_NUMBER: _ClassVar[int]
        GAME_NAME_FIELD_NUMBER: _ClassVar[int]
        VAC_BANNED_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
        appid: int
        game_name: str
        vac_banned: bool
        package_excluded: bool
        def __init__(self, appid: _Optional[int] = ..., game_name: _Optional[str] = ..., vac_banned: bool = ..., package_excluded: bool = ...) -> None: ...
    EXCLUDED_GAMES_FIELD_NUMBER: _ClassVar[int]
    excluded_games: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetExcludedGamesInLibrary_Response.ExcludedGame]
    def __init__(self, excluded_games: _Optional[_Iterable[_Union[CDeviceAuth_GetExcludedGamesInLibrary_Response.ExcludedGame, _Mapping]]] = ...) -> None: ...

class CDeviceAuth_GetBorrowerPlayHistory_Request(_message.Message):
    __slots__ = ("steamid", "appid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CDeviceAuth_GetBorrowerPlayHistory_Response(_message.Message):
    __slots__ = ("lender_history",)
    class GameHistory(_message.Message):
        __slots__ = ("appid", "time_last", "time_total")
        APPID_FIELD_NUMBER: _ClassVar[int]
        TIME_LAST_FIELD_NUMBER: _ClassVar[int]
        TIME_TOTAL_FIELD_NUMBER: _ClassVar[int]
        appid: int
        time_last: int
        time_total: int
        def __init__(self, appid: _Optional[int] = ..., time_last: _Optional[int] = ..., time_total: _Optional[int] = ...) -> None: ...
    class LenderHistory(_message.Message):
        __slots__ = ("steamid", "game_history")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        GAME_HISTORY_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        game_history: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetBorrowerPlayHistory_Response.GameHistory]
        def __init__(self, steamid: _Optional[int] = ..., game_history: _Optional[_Iterable[_Union[CDeviceAuth_GetBorrowerPlayHistory_Response.GameHistory, _Mapping]]] = ...) -> None: ...
    LENDER_HISTORY_FIELD_NUMBER: _ClassVar[int]
    lender_history: _containers.RepeatedCompositeFieldContainer[CDeviceAuth_GetBorrowerPlayHistory_Response.LenderHistory]
    def __init__(self, lender_history: _Optional[_Iterable[_Union[CDeviceAuth_GetBorrowerPlayHistory_Response.LenderHistory, _Mapping]]] = ...) -> None: ...

class DeviceAuth(_service.service): ...

class DeviceAuth_Stub(DeviceAuth): ...
