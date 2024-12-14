import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EBroadcastWatchLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EBroadcastWatchLocation_Invalid: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_SteamTV_Tab: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_SteamTV_WatchParty: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_Chat_Tab: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_Chat_WatchParty: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_CommunityPage: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_StoreAppPage: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_InGame: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_BigPicture: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_SalesPage: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_CuratorPage: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_DeveloperPage: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_Chat_Friends: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_SteamTV_Web: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_DesktopUI_Overlay: _ClassVar[EBroadcastWatchLocation]
    k_EBroadcastWatchLocation_TrailerCarousel: _ClassVar[EBroadcastWatchLocation]

class EBroadcastChatPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EBroadcastChatPermissionPublic: _ClassVar[EBroadcastChatPermission]
    k_EBroadcastChatPermissionOwnsApp: _ClassVar[EBroadcastChatPermission]
k_EBroadcastWatchLocation_Invalid: EBroadcastWatchLocation
k_EBroadcastWatchLocation_SteamTV_Tab: EBroadcastWatchLocation
k_EBroadcastWatchLocation_SteamTV_WatchParty: EBroadcastWatchLocation
k_EBroadcastWatchLocation_Chat_Tab: EBroadcastWatchLocation
k_EBroadcastWatchLocation_Chat_WatchParty: EBroadcastWatchLocation
k_EBroadcastWatchLocation_CommunityPage: EBroadcastWatchLocation
k_EBroadcastWatchLocation_StoreAppPage: EBroadcastWatchLocation
k_EBroadcastWatchLocation_InGame: EBroadcastWatchLocation
k_EBroadcastWatchLocation_BigPicture: EBroadcastWatchLocation
k_EBroadcastWatchLocation_SalesPage: EBroadcastWatchLocation
k_EBroadcastWatchLocation_CuratorPage: EBroadcastWatchLocation
k_EBroadcastWatchLocation_DeveloperPage: EBroadcastWatchLocation
k_EBroadcastWatchLocation_Chat_Friends: EBroadcastWatchLocation
k_EBroadcastWatchLocation_SteamTV_Web: EBroadcastWatchLocation
k_EBroadcastWatchLocation_DesktopUI_Overlay: EBroadcastWatchLocation
k_EBroadcastWatchLocation_TrailerCarousel: EBroadcastWatchLocation
k_EBroadcastChatPermissionPublic: EBroadcastChatPermission
k_EBroadcastChatPermissionOwnsApp: EBroadcastChatPermission

class CBroadcast_BeginBroadcastSession_Request(_message.Message):
    __slots__ = ("permission", "gameid", "client_instance_id", "title", "cellid", "rtmp_token", "thumbnail_upload", "sysid", "allow_webrtc")
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CELLID_FIELD_NUMBER: _ClassVar[int]
    RTMP_TOKEN_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    SYSID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_WEBRTC_FIELD_NUMBER: _ClassVar[int]
    permission: int
    gameid: int
    client_instance_id: int
    title: str
    cellid: int
    rtmp_token: int
    thumbnail_upload: bool
    sysid: int
    allow_webrtc: bool
    def __init__(self, permission: _Optional[int] = ..., gameid: _Optional[int] = ..., client_instance_id: _Optional[int] = ..., title: _Optional[str] = ..., cellid: _Optional[int] = ..., rtmp_token: _Optional[int] = ..., thumbnail_upload: bool = ..., sysid: _Optional[int] = ..., allow_webrtc: bool = ...) -> None: ...

class CBroadcast_BeginBroadcastSession_Response(_message.Message):
    __slots__ = ("broadcast_id", "thumbnail_upload_address", "thumbnail_upload_token", "thumbnail_interval_seconds", "heartbeat_interval_seconds")
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_UPLOAD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    thumbnail_upload_address: str
    thumbnail_upload_token: str
    thumbnail_interval_seconds: int
    heartbeat_interval_seconds: int
    def __init__(self, broadcast_id: _Optional[int] = ..., thumbnail_upload_address: _Optional[str] = ..., thumbnail_upload_token: _Optional[str] = ..., thumbnail_interval_seconds: _Optional[int] = ..., heartbeat_interval_seconds: _Optional[int] = ...) -> None: ...

class CBroadcast_EndBroadcastSession_Request(_message.Message):
    __slots__ = ("broadcast_id",)
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    def __init__(self, broadcast_id: _Optional[int] = ...) -> None: ...

class CBroadcast_EndBroadcastSession_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_StartBroadcastUpload_Request(_message.Message):
    __slots__ = ("broadcast_id", "cellid", "as_rtmp", "delay_seconds", "rtmp_token", "upload_ip_address", "is_replay", "sysid")
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    CELLID_FIELD_NUMBER: _ClassVar[int]
    AS_RTMP_FIELD_NUMBER: _ClassVar[int]
    DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    RTMP_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    IS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    SYSID_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    cellid: int
    as_rtmp: bool
    delay_seconds: int
    rtmp_token: int
    upload_ip_address: int
    is_replay: bool
    sysid: int
    def __init__(self, broadcast_id: _Optional[int] = ..., cellid: _Optional[int] = ..., as_rtmp: bool = ..., delay_seconds: _Optional[int] = ..., rtmp_token: _Optional[int] = ..., upload_ip_address: _Optional[int] = ..., is_replay: bool = ..., sysid: _Optional[int] = ...) -> None: ...

class CBroadcast_StartBroadcastUpload_Response(_message.Message):
    __slots__ = ("upload_token", "upload_address", "broadcast_upload_id", "enable_replay", "http_address")
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REPLAY_FIELD_NUMBER: _ClassVar[int]
    HTTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    upload_token: str
    upload_address: str
    broadcast_upload_id: int
    enable_replay: bool
    http_address: str
    def __init__(self, upload_token: _Optional[str] = ..., upload_address: _Optional[str] = ..., broadcast_upload_id: _Optional[int] = ..., enable_replay: bool = ..., http_address: _Optional[str] = ...) -> None: ...

class CBroadcast_NotifyBroadcastUploadStop_Notification(_message.Message):
    __slots__ = ("broadcast_upload_id", "upload_result")
    BROADCAST_UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_RESULT_FIELD_NUMBER: _ClassVar[int]
    broadcast_upload_id: int
    upload_result: int
    def __init__(self, broadcast_upload_id: _Optional[int] = ..., upload_result: _Optional[int] = ...) -> None: ...

class CBroadcast_WatchBroadcast_Request(_message.Message):
    __slots__ = ("steamid", "existing_broadcast_id", "viewer_token", "client_cell", "watch_location", "is_webrtc")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    EXISTING_BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CELL_FIELD_NUMBER: _ClassVar[int]
    WATCH_LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_WEBRTC_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    existing_broadcast_id: int
    viewer_token: int
    client_cell: int
    watch_location: EBroadcastWatchLocation
    is_webrtc: bool
    def __init__(self, steamid: _Optional[int] = ..., existing_broadcast_id: _Optional[int] = ..., viewer_token: _Optional[int] = ..., client_cell: _Optional[int] = ..., watch_location: _Optional[_Union[EBroadcastWatchLocation, str]] = ..., is_webrtc: bool = ...) -> None: ...

class CBroadcast_WatchBroadcast_Response(_message.Message):
    __slots__ = ("response", "mpd_url", "broadcast_id", "gameid", "title", "num_viewers", "permission", "is_rtmp", "seconds_delay", "viewer_token", "hls_m3u8_master_url", "heartbeat_interval", "thumbnail_url", "is_webrtc", "webrtc_session_id", "webrtc_offer_sdp", "webrtc_turn_server", "is_replay", "duration", "cdn_auth_url_parameters")
    class EWatchResponse(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        k_EWatchResponseReady: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseNotAvailable: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseWaitingForApproval: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseWaitingForStart: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseInvalidSession: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseTooManyBroadcasts: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseWaitingForReconnect: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseSystemNotSupported: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseUserRestricted: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseClientOutOfDate: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponsePoorUploadQuality: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseMissingSubscription: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
        k_EWatchResponseTooManyViewers: _ClassVar[CBroadcast_WatchBroadcast_Response.EWatchResponse]
    k_EWatchResponseReady: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseNotAvailable: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseWaitingForApproval: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseWaitingForStart: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseInvalidSession: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseTooManyBroadcasts: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseWaitingForReconnect: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseSystemNotSupported: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseUserRestricted: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseClientOutOfDate: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponsePoorUploadQuality: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseMissingSubscription: CBroadcast_WatchBroadcast_Response.EWatchResponse
    k_EWatchResponseTooManyViewers: CBroadcast_WatchBroadcast_Response.EWatchResponse
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MPD_URL_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    IS_RTMP_FIELD_NUMBER: _ClassVar[int]
    SECONDS_DELAY_FIELD_NUMBER: _ClassVar[int]
    VIEWER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HLS_M3U8_MASTER_URL_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    IS_WEBRTC_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_OFFER_SDP_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_TURN_SERVER_FIELD_NUMBER: _ClassVar[int]
    IS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    CDN_AUTH_URL_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    response: CBroadcast_WatchBroadcast_Response.EWatchResponse
    mpd_url: str
    broadcast_id: int
    gameid: int
    title: str
    num_viewers: int
    permission: int
    is_rtmp: bool
    seconds_delay: int
    viewer_token: int
    hls_m3u8_master_url: str
    heartbeat_interval: int
    thumbnail_url: str
    is_webrtc: bool
    webrtc_session_id: int
    webrtc_offer_sdp: str
    webrtc_turn_server: str
    is_replay: bool
    duration: int
    cdn_auth_url_parameters: str
    def __init__(self, response: _Optional[_Union[CBroadcast_WatchBroadcast_Response.EWatchResponse, str]] = ..., mpd_url: _Optional[str] = ..., broadcast_id: _Optional[int] = ..., gameid: _Optional[int] = ..., title: _Optional[str] = ..., num_viewers: _Optional[int] = ..., permission: _Optional[int] = ..., is_rtmp: bool = ..., seconds_delay: _Optional[int] = ..., viewer_token: _Optional[int] = ..., hls_m3u8_master_url: _Optional[str] = ..., heartbeat_interval: _Optional[int] = ..., thumbnail_url: _Optional[str] = ..., is_webrtc: bool = ..., webrtc_session_id: _Optional[int] = ..., webrtc_offer_sdp: _Optional[str] = ..., webrtc_turn_server: _Optional[str] = ..., is_replay: bool = ..., duration: _Optional[int] = ..., cdn_auth_url_parameters: _Optional[str] = ...) -> None: ...

class CBroadcast_HeartbeatBroadcast_Notification(_message.Message):
    __slots__ = ("steamid", "broadcast_id", "viewer_token", "representation")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    broadcast_id: int
    viewer_token: int
    representation: int
    def __init__(self, steamid: _Optional[int] = ..., broadcast_id: _Optional[int] = ..., viewer_token: _Optional[int] = ..., representation: _Optional[int] = ...) -> None: ...

class CBroadcast_StopWatchingBroadcast_Notification(_message.Message):
    __slots__ = ("steamid", "broadcast_id", "viewer_token")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    broadcast_id: int
    viewer_token: int
    def __init__(self, steamid: _Optional[int] = ..., broadcast_id: _Optional[int] = ..., viewer_token: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastStatus_Request(_message.Message):
    __slots__ = ("steamid", "broadcast_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    broadcast_id: int
    def __init__(self, steamid: _Optional[int] = ..., broadcast_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastStatus_Response(_message.Message):
    __slots__ = ("gameid", "title", "num_viewers", "permission", "is_rtmp", "seconds_delay", "is_publisher", "thumbnail_url", "update_interval", "is_uploading", "duration", "is_replay", "is_capturing_vod", "is_store_whitelisted")
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    IS_RTMP_FIELD_NUMBER: _ClassVar[int]
    SECONDS_DELAY_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    IS_UPLOADING_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_REPLAY_FIELD_NUMBER: _ClassVar[int]
    IS_CAPTURING_VOD_FIELD_NUMBER: _ClassVar[int]
    IS_STORE_WHITELISTED_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    title: str
    num_viewers: int
    permission: int
    is_rtmp: bool
    seconds_delay: int
    is_publisher: bool
    thumbnail_url: str
    update_interval: int
    is_uploading: bool
    duration: int
    is_replay: bool
    is_capturing_vod: bool
    is_store_whitelisted: bool
    def __init__(self, gameid: _Optional[int] = ..., title: _Optional[str] = ..., num_viewers: _Optional[int] = ..., permission: _Optional[int] = ..., is_rtmp: bool = ..., seconds_delay: _Optional[int] = ..., is_publisher: bool = ..., thumbnail_url: _Optional[str] = ..., update_interval: _Optional[int] = ..., is_uploading: bool = ..., duration: _Optional[int] = ..., is_replay: bool = ..., is_capturing_vod: bool = ..., is_store_whitelisted: bool = ...) -> None: ...

class CBroadcast_GetBroadcastThumbnail_Request(_message.Message):
    __slots__ = ("steamid", "broadcast_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    broadcast_id: int
    def __init__(self, steamid: _Optional[int] = ..., broadcast_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastThumbnail_Response(_message.Message):
    __slots__ = ("thumbnail_url", "update_interval", "num_viewers", "duration")
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    thumbnail_url: str
    update_interval: int
    num_viewers: int
    duration: int
    def __init__(self, thumbnail_url: _Optional[str] = ..., update_interval: _Optional[int] = ..., num_viewers: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class CBroadcast_InviteToBroadcast_Request(_message.Message):
    __slots__ = ("steamid", "approval_response")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    approval_response: bool
    def __init__(self, steamid: _Optional[int] = ..., approval_response: bool = ...) -> None: ...

class CBroadcast_InviteToBroadcast_Response(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CBroadcast_SendBroadcastStateToServer_Request(_message.Message):
    __slots__ = ("permission", "gameid", "title", "game_data_config")
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GAME_DATA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    permission: int
    gameid: int
    title: str
    game_data_config: str
    def __init__(self, permission: _Optional[int] = ..., gameid: _Optional[int] = ..., title: _Optional[str] = ..., game_data_config: _Optional[str] = ...) -> None: ...

class CBroadcast_SendBroadcastStateToServer_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_NotifyBroadcastSessionHeartbeat_Notification(_message.Message):
    __slots__ = ("broadcast_id",)
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    def __init__(self, broadcast_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastChatInfo_Request(_message.Message):
    __slots__ = ("steamid", "broadcast_id", "client_ip", "client_cell")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IP_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CELL_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    broadcast_id: int
    client_ip: int
    client_cell: int
    def __init__(self, steamid: _Optional[int] = ..., broadcast_id: _Optional[int] = ..., client_ip: _Optional[int] = ..., client_cell: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastChatInfo_Response(_message.Message):
    __slots__ = ("chat_id", "view_url_template", "flair_group_ids")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    VIEW_URL_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FLAIR_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    view_url_template: str
    flair_group_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_id: _Optional[int] = ..., view_url_template: _Optional[str] = ..., flair_group_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CBroadcast_PostChatMessage_Request(_message.Message):
    __slots__ = ("chat_id", "message", "instance_id", "language", "country_code")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    message: str
    instance_id: int
    language: int
    country_code: str
    def __init__(self, chat_id: _Optional[int] = ..., message: _Optional[str] = ..., instance_id: _Optional[int] = ..., language: _Optional[int] = ..., country_code: _Optional[str] = ...) -> None: ...

class CBroadcast_PostChatMessage_Response(_message.Message):
    __slots__ = ("persona_name", "in_game", "result", "cooldown_time_seconds")
    PERSONA_NAME_FIELD_NUMBER: _ClassVar[int]
    IN_GAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    persona_name: str
    in_game: bool
    result: int
    cooldown_time_seconds: int
    def __init__(self, persona_name: _Optional[str] = ..., in_game: bool = ..., result: _Optional[int] = ..., cooldown_time_seconds: _Optional[int] = ...) -> None: ...

class CBroadcast_UpdateChatMessageFlair_Request(_message.Message):
    __slots__ = ("chat_id", "flair")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    FLAIR_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    flair: str
    def __init__(self, chat_id: _Optional[int] = ..., flair: _Optional[str] = ...) -> None: ...

class CBroadcast_UpdateChatMessageFlair_Response(_message.Message):
    __slots__ = ("result", "chat_id", "flair")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    FLAIR_FIELD_NUMBER: _ClassVar[int]
    result: int
    chat_id: int
    flair: str
    def __init__(self, result: _Optional[int] = ..., chat_id: _Optional[int] = ..., flair: _Optional[str] = ...) -> None: ...

class CBroadcast_MuteBroadcastChatUser_Request(_message.Message):
    __slots__ = ("chat_id", "user_steamid", "muted")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    MUTED_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    user_steamid: int
    muted: bool
    def __init__(self, chat_id: _Optional[int] = ..., user_steamid: _Optional[int] = ..., muted: bool = ...) -> None: ...

class CBroadcast_MuteBroadcastChatUser_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_RemoveUserChatText_Request(_message.Message):
    __slots__ = ("chat_id", "user_steamid")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    user_steamid: int
    def __init__(self, chat_id: _Optional[int] = ..., user_steamid: _Optional[int] = ...) -> None: ...

class CBroadcast_RemoveUserChatText_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_GetBroadcastChatUserNames_Request(_message.Message):
    __slots__ = ("chat_id", "user_steamid")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    chat_id: int
    user_steamid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, chat_id: _Optional[int] = ..., user_steamid: _Optional[_Iterable[int]] = ...) -> None: ...

class CBroadcast_GetBroadcastChatUserNames_Response(_message.Message):
    __slots__ = ("persona_names",)
    class PersonaName(_message.Message):
        __slots__ = ("steam_id", "persona")
        STEAM_ID_FIELD_NUMBER: _ClassVar[int]
        PERSONA_FIELD_NUMBER: _ClassVar[int]
        steam_id: int
        persona: str
        def __init__(self, steam_id: _Optional[int] = ..., persona: _Optional[str] = ...) -> None: ...
    PERSONA_NAMES_FIELD_NUMBER: _ClassVar[int]
    persona_names: _containers.RepeatedCompositeFieldContainer[CBroadcast_GetBroadcastChatUserNames_Response.PersonaName]
    def __init__(self, persona_names: _Optional[_Iterable[_Union[CBroadcast_GetBroadcastChatUserNames_Response.PersonaName, _Mapping]]] = ...) -> None: ...

class CBroadcast_StartBuildClip_Request(_message.Message):
    __slots__ = ("steamid", "broadcast_session_id", "first_segment", "num_segments", "clip_description")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    NUM_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    CLIP_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    broadcast_session_id: int
    first_segment: int
    num_segments: int
    clip_description: str
    def __init__(self, steamid: _Optional[int] = ..., broadcast_session_id: _Optional[int] = ..., first_segment: _Optional[int] = ..., num_segments: _Optional[int] = ..., clip_description: _Optional[str] = ...) -> None: ...

class CBroadcast_StartBuildClip_Response(_message.Message):
    __slots__ = ("broadcast_clip_id",)
    BROADCAST_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_clip_id: int
    def __init__(self, broadcast_clip_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBuildClipStatus_Request(_message.Message):
    __slots__ = ("broadcast_clip_id",)
    BROADCAST_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_clip_id: int
    def __init__(self, broadcast_clip_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBuildClipStatus_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_SetClipDetails_Request(_message.Message):
    __slots__ = ("broadcast_clip_id", "start_time", "end_time", "video_description")
    BROADCAST_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    broadcast_clip_id: int
    start_time: int
    end_time: int
    video_description: str
    def __init__(self, broadcast_clip_id: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., video_description: _Optional[str] = ...) -> None: ...

class CBroadcast_SetClipDetails_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_GetClipDetails_Request(_message.Message):
    __slots__ = ("broadcast_clip_id",)
    BROADCAST_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_clip_id: int
    def __init__(self, broadcast_clip_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetClipDetails_Response(_message.Message):
    __slots__ = ("broadcast_clip_id", "video_id", "channel_id", "app_id", "accountid_broadcaster", "accountid_clipmaker", "video_description", "start_time", "length_milliseconds", "thumbnail_path")
    BROADCAST_CLIP_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_BROADCASTER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_CLIPMAKER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    LENGTH_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_PATH_FIELD_NUMBER: _ClassVar[int]
    broadcast_clip_id: int
    video_id: int
    channel_id: int
    app_id: int
    accountid_broadcaster: int
    accountid_clipmaker: int
    video_description: str
    start_time: int
    length_milliseconds: int
    thumbnail_path: str
    def __init__(self, broadcast_clip_id: _Optional[int] = ..., video_id: _Optional[int] = ..., channel_id: _Optional[int] = ..., app_id: _Optional[int] = ..., accountid_broadcaster: _Optional[int] = ..., accountid_clipmaker: _Optional[int] = ..., video_description: _Optional[str] = ..., start_time: _Optional[int] = ..., length_milliseconds: _Optional[int] = ..., thumbnail_path: _Optional[str] = ...) -> None: ...

class CBroadcast_SetRTMPInfo_Request(_message.Message):
    __slots__ = ("broadcast_permission", "update_token", "broadcast_delay", "app_id", "required_app_id", "broadcast_chat_permission", "broadcast_buffer", "steamid", "chat_rate_limit", "enable_replay", "is_partner_chat_only", "wordban_list")
    BROADCAST_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_DELAY_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APP_ID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_CHAT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_BUFFER_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHAT_RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REPLAY_FIELD_NUMBER: _ClassVar[int]
    IS_PARTNER_CHAT_ONLY_FIELD_NUMBER: _ClassVar[int]
    WORDBAN_LIST_FIELD_NUMBER: _ClassVar[int]
    broadcast_permission: int
    update_token: bool
    broadcast_delay: int
    app_id: int
    required_app_id: int
    broadcast_chat_permission: EBroadcastChatPermission
    broadcast_buffer: int
    steamid: int
    chat_rate_limit: int
    enable_replay: bool
    is_partner_chat_only: bool
    wordban_list: str
    def __init__(self, broadcast_permission: _Optional[int] = ..., update_token: bool = ..., broadcast_delay: _Optional[int] = ..., app_id: _Optional[int] = ..., required_app_id: _Optional[int] = ..., broadcast_chat_permission: _Optional[_Union[EBroadcastChatPermission, str]] = ..., broadcast_buffer: _Optional[int] = ..., steamid: _Optional[int] = ..., chat_rate_limit: _Optional[int] = ..., enable_replay: bool = ..., is_partner_chat_only: bool = ..., wordban_list: _Optional[str] = ...) -> None: ...

class CBroadcast_SetRTMPInfo_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_GetRTMPInfo_Request(_message.Message):
    __slots__ = ("ip", "steamid")
    IP_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ip: int
    steamid: int
    def __init__(self, ip: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CBroadcast_GetRTMPInfo_Response(_message.Message):
    __slots__ = ("broadcast_permission", "rtmp_host", "rtmp_token", "broadcast_delay", "app_id", "required_app_id", "broadcast_chat_permission", "broadcast_buffer", "steamid", "chat_rate_limit", "enable_replay", "is_partner_chat_only", "wordban_list")
    BROADCAST_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    RTMP_HOST_FIELD_NUMBER: _ClassVar[int]
    RTMP_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_DELAY_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APP_ID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_CHAT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_BUFFER_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CHAT_RATE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REPLAY_FIELD_NUMBER: _ClassVar[int]
    IS_PARTNER_CHAT_ONLY_FIELD_NUMBER: _ClassVar[int]
    WORDBAN_LIST_FIELD_NUMBER: _ClassVar[int]
    broadcast_permission: int
    rtmp_host: str
    rtmp_token: str
    broadcast_delay: int
    app_id: int
    required_app_id: int
    broadcast_chat_permission: EBroadcastChatPermission
    broadcast_buffer: int
    steamid: int
    chat_rate_limit: int
    enable_replay: bool
    is_partner_chat_only: bool
    wordban_list: str
    def __init__(self, broadcast_permission: _Optional[int] = ..., rtmp_host: _Optional[str] = ..., rtmp_token: _Optional[str] = ..., broadcast_delay: _Optional[int] = ..., app_id: _Optional[int] = ..., required_app_id: _Optional[int] = ..., broadcast_chat_permission: _Optional[_Union[EBroadcastChatPermission, str]] = ..., broadcast_buffer: _Optional[int] = ..., steamid: _Optional[int] = ..., chat_rate_limit: _Optional[int] = ..., enable_replay: bool = ..., is_partner_chat_only: bool = ..., wordban_list: _Optional[str] = ...) -> None: ...

class CBroadcast_WebRTCHaveTURNServer_Notification(_message.Message):
    __slots__ = ("broadcast_session_id", "turn_server")
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TURN_SERVER_FIELD_NUMBER: _ClassVar[int]
    broadcast_session_id: int
    turn_server: str
    def __init__(self, broadcast_session_id: _Optional[int] = ..., turn_server: _Optional[str] = ...) -> None: ...

class CBroadcast_WebRTCStartResult_Request(_message.Message):
    __slots__ = ("webrtc_session_id", "started", "offer", "resolution_x", "resolution_y", "fps")
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_X_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_Y_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    webrtc_session_id: int
    started: bool
    offer: str
    resolution_x: int
    resolution_y: int
    fps: int
    def __init__(self, webrtc_session_id: _Optional[int] = ..., started: bool = ..., offer: _Optional[str] = ..., resolution_x: _Optional[int] = ..., resolution_y: _Optional[int] = ..., fps: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCStartResult_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_WebRTCStopped_Request(_message.Message):
    __slots__ = ("webrtc_session_id",)
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    webrtc_session_id: int
    def __init__(self, webrtc_session_id: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCStopped_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_WebRTCSetAnswer_Request(_message.Message):
    __slots__ = ("broadcaster_steamid", "webrtc_session_id", "answer")
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    broadcaster_steamid: int
    webrtc_session_id: int
    answer: str
    def __init__(self, broadcaster_steamid: _Optional[int] = ..., webrtc_session_id: _Optional[int] = ..., answer: _Optional[str] = ...) -> None: ...

class CBroadcast_WebRTCSetAnswer_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_WebRTCLookupTURNServer_Request(_message.Message):
    __slots__ = ("cellid",)
    CELLID_FIELD_NUMBER: _ClassVar[int]
    cellid: int
    def __init__(self, cellid: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCLookupTURNServer_Response(_message.Message):
    __slots__ = ("turn_server",)
    TURN_SERVER_FIELD_NUMBER: _ClassVar[int]
    turn_server: str
    def __init__(self, turn_server: _Optional[str] = ...) -> None: ...

class CBroadcast_WebRTC_Candidate(_message.Message):
    __slots__ = ("sdp_mid", "sdp_mline_index", "candidate")
    SDP_MID_FIELD_NUMBER: _ClassVar[int]
    SDP_MLINE_INDEX_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    sdp_mid: str
    sdp_mline_index: int
    candidate: str
    def __init__(self, sdp_mid: _Optional[str] = ..., sdp_mline_index: _Optional[int] = ..., candidate: _Optional[str] = ...) -> None: ...

class CBroadcast_WebRTCAddHostCandidate_Request(_message.Message):
    __slots__ = ("webrtc_session_id", "candidate")
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    webrtc_session_id: int
    candidate: CBroadcast_WebRTC_Candidate
    def __init__(self, webrtc_session_id: _Optional[int] = ..., candidate: _Optional[_Union[CBroadcast_WebRTC_Candidate, _Mapping]] = ...) -> None: ...

class CBroadcast_WebRTCAddHostCandidate_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_WebRTCAddViewerCandidate_Request(_message.Message):
    __slots__ = ("broadcaster_steamid", "webrtc_session_id", "candidate")
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    broadcaster_steamid: int
    webrtc_session_id: int
    candidate: CBroadcast_WebRTC_Candidate
    def __init__(self, broadcaster_steamid: _Optional[int] = ..., webrtc_session_id: _Optional[int] = ..., candidate: _Optional[_Union[CBroadcast_WebRTC_Candidate, _Mapping]] = ...) -> None: ...

class CBroadcast_WebRTCAddViewerCandidate_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CBroadcast_WebRTCGetHostCandidates_Request(_message.Message):
    __slots__ = ("broadcaster_steamid", "webrtc_session_id", "candidate_generation")
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    broadcaster_steamid: int
    webrtc_session_id: int
    candidate_generation: int
    def __init__(self, broadcaster_steamid: _Optional[int] = ..., webrtc_session_id: _Optional[int] = ..., candidate_generation: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCGetHostCandidates_Response(_message.Message):
    __slots__ = ("candidate_generation", "candidates")
    CANDIDATE_GENERATION_FIELD_NUMBER: _ClassVar[int]
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    candidate_generation: int
    candidates: _containers.RepeatedCompositeFieldContainer[CBroadcast_WebRTC_Candidate]
    def __init__(self, candidate_generation: _Optional[int] = ..., candidates: _Optional[_Iterable[_Union[CBroadcast_WebRTC_Candidate, _Mapping]]] = ...) -> None: ...

class CBroadcast_GetBroadcastUploadStats_Request(_message.Message):
    __slots__ = ("row_limit", "start_time", "upload_id", "steamid", "session_id")
    ROW_LIMIT_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    row_limit: int
    start_time: int
    upload_id: int
    steamid: int
    session_id: int
    def __init__(self, row_limit: _Optional[int] = ..., start_time: _Optional[int] = ..., upload_id: _Optional[int] = ..., steamid: _Optional[int] = ..., session_id: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastUploadStats_Response(_message.Message):
    __slots__ = ("upload_stats",)
    class UploadStats(_message.Message):
        __slots__ = ("upload_result", "time_stopped", "seconds_uploaded", "max_viewers", "resolution_x", "resolution_y", "avg_bandwidth", "total_bytes", "app_id", "total_unique_viewers", "total_seconds_watched", "time_started", "upload_id", "local_address", "remote_address", "frames_per_second", "num_representations", "app_name", "is_replay", "session_id")
        UPLOAD_RESULT_FIELD_NUMBER: _ClassVar[int]
        TIME_STOPPED_FIELD_NUMBER: _ClassVar[int]
        SECONDS_UPLOADED_FIELD_NUMBER: _ClassVar[int]
        MAX_VIEWERS_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_X_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_Y_FIELD_NUMBER: _ClassVar[int]
        AVG_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
        TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
        APP_ID_FIELD_NUMBER: _ClassVar[int]
        TOTAL_UNIQUE_VIEWERS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SECONDS_WATCHED_FIELD_NUMBER: _ClassVar[int]
        TIME_STARTED_FIELD_NUMBER: _ClassVar[int]
        UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
        LOCAL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        REMOTE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        FRAMES_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
        NUM_REPRESENTATIONS_FIELD_NUMBER: _ClassVar[int]
        APP_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_REPLAY_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        upload_result: int
        time_stopped: int
        seconds_uploaded: int
        max_viewers: int
        resolution_x: int
        resolution_y: int
        avg_bandwidth: int
        total_bytes: int
        app_id: int
        total_unique_viewers: int
        total_seconds_watched: int
        time_started: int
        upload_id: int
        local_address: str
        remote_address: str
        frames_per_second: int
        num_representations: int
        app_name: str
        is_replay: bool
        session_id: int
        def __init__(self, upload_result: _Optional[int] = ..., time_stopped: _Optional[int] = ..., seconds_uploaded: _Optional[int] = ..., max_viewers: _Optional[int] = ..., resolution_x: _Optional[int] = ..., resolution_y: _Optional[int] = ..., avg_bandwidth: _Optional[int] = ..., total_bytes: _Optional[int] = ..., app_id: _Optional[int] = ..., total_unique_viewers: _Optional[int] = ..., total_seconds_watched: _Optional[int] = ..., time_started: _Optional[int] = ..., upload_id: _Optional[int] = ..., local_address: _Optional[str] = ..., remote_address: _Optional[str] = ..., frames_per_second: _Optional[int] = ..., num_representations: _Optional[int] = ..., app_name: _Optional[str] = ..., is_replay: bool = ..., session_id: _Optional[int] = ...) -> None: ...
    UPLOAD_STATS_FIELD_NUMBER: _ClassVar[int]
    upload_stats: _containers.RepeatedCompositeFieldContainer[CBroadcast_GetBroadcastUploadStats_Response.UploadStats]
    def __init__(self, upload_stats: _Optional[_Iterable[_Union[CBroadcast_GetBroadcastUploadStats_Response.UploadStats, _Mapping]]] = ...) -> None: ...

class CBroadcast_GetBroadcastViewerStats_Request(_message.Message):
    __slots__ = ("upload_id", "steamid")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    upload_id: int
    steamid: int
    def __init__(self, upload_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CBroadcast_GetBroadcastViewerStats_Response(_message.Message):
    __slots__ = ("viewer_stats", "country_stats")
    class ViewerStats(_message.Message):
        __slots__ = ("time", "num_viewers")
        TIME_FIELD_NUMBER: _ClassVar[int]
        NUM_VIEWERS_FIELD_NUMBER: _ClassVar[int]
        time: int
        num_viewers: int
        def __init__(self, time: _Optional[int] = ..., num_viewers: _Optional[int] = ...) -> None: ...
    class CountryStats(_message.Message):
        __slots__ = ("country_code", "num_viewers")
        COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
        NUM_VIEWERS_FIELD_NUMBER: _ClassVar[int]
        country_code: str
        num_viewers: int
        def __init__(self, country_code: _Optional[str] = ..., num_viewers: _Optional[int] = ...) -> None: ...
    VIEWER_STATS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_STATS_FIELD_NUMBER: _ClassVar[int]
    viewer_stats: _containers.RepeatedCompositeFieldContainer[CBroadcast_GetBroadcastViewerStats_Response.ViewerStats]
    country_stats: _containers.RepeatedCompositeFieldContainer[CBroadcast_GetBroadcastViewerStats_Response.CountryStats]
    def __init__(self, viewer_stats: _Optional[_Iterable[_Union[CBroadcast_GetBroadcastViewerStats_Response.ViewerStats, _Mapping]]] = ..., country_stats: _Optional[_Iterable[_Union[CBroadcast_GetBroadcastViewerStats_Response.CountryStats, _Mapping]]] = ...) -> None: ...

class CBroadcast_BroadcastViewerState_Notification(_message.Message):
    __slots__ = ("steamid", "state")
    class EViewerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        k_EViewerNeedsApproval: _ClassVar[CBroadcast_BroadcastViewerState_Notification.EViewerState]
        k_EViewerWatching: _ClassVar[CBroadcast_BroadcastViewerState_Notification.EViewerState]
        k_EViewerLeft: _ClassVar[CBroadcast_BroadcastViewerState_Notification.EViewerState]
    k_EViewerNeedsApproval: CBroadcast_BroadcastViewerState_Notification.EViewerState
    k_EViewerWatching: CBroadcast_BroadcastViewerState_Notification.EViewerState
    k_EViewerLeft: CBroadcast_BroadcastViewerState_Notification.EViewerState
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    state: CBroadcast_BroadcastViewerState_Notification.EViewerState
    def __init__(self, steamid: _Optional[int] = ..., state: _Optional[_Union[CBroadcast_BroadcastViewerState_Notification.EViewerState, str]] = ...) -> None: ...

class CBroadcast_WaitingBroadcastViewer_Notification(_message.Message):
    __slots__ = ("broadcast_id",)
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    def __init__(self, broadcast_id: _Optional[int] = ...) -> None: ...

class CBroadcast_BroadcastUploadStarted_Notification(_message.Message):
    __slots__ = ("broadcast_id", "upload_token", "upload_address", "http_address", "broadcast_upload_id", "heartbeat_interval_seconds", "is_rtmp")
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HTTP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_INTERVAL_SECONDS_FIELD_NUMBER: _ClassVar[int]
    IS_RTMP_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    upload_token: str
    upload_address: str
    http_address: str
    broadcast_upload_id: int
    heartbeat_interval_seconds: int
    is_rtmp: bool
    def __init__(self, broadcast_id: _Optional[int] = ..., upload_token: _Optional[str] = ..., upload_address: _Optional[str] = ..., http_address: _Optional[str] = ..., broadcast_upload_id: _Optional[int] = ..., heartbeat_interval_seconds: _Optional[int] = ..., is_rtmp: bool = ...) -> None: ...

class CBroadcast_StopBroadcastUpload_Notification(_message.Message):
    __slots__ = ("broadcast_id", "broadcast_relay_id", "upload_result", "too_many_poor_uploads")
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_RELAY_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOO_MANY_POOR_UPLOADS_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    broadcast_relay_id: int
    upload_result: int
    too_many_poor_uploads: bool
    def __init__(self, broadcast_id: _Optional[int] = ..., broadcast_relay_id: _Optional[int] = ..., upload_result: _Optional[int] = ..., too_many_poor_uploads: bool = ...) -> None: ...

class CBroadcast_SessionClosed_Notification(_message.Message):
    __slots__ = ("broadcast_id",)
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    def __init__(self, broadcast_id: _Optional[int] = ...) -> None: ...

class CBroadcast_ViewerBroadcastInvite_Notification(_message.Message):
    __slots__ = ("broadcaster_steamid",)
    BROADCASTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    broadcaster_steamid: int
    def __init__(self, broadcaster_steamid: _Optional[int] = ...) -> None: ...

class CBroadcast_BroadcastStatus_Notification(_message.Message):
    __slots__ = ("broadcast_id", "num_viewers")
    BROADCAST_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_VIEWERS_FIELD_NUMBER: _ClassVar[int]
    broadcast_id: int
    num_viewers: int
    def __init__(self, broadcast_id: _Optional[int] = ..., num_viewers: _Optional[int] = ...) -> None: ...

class CBroadcast_BroadcastChannelLive_Notification(_message.Message):
    __slots__ = ("broadcast_channel_id", "broadcast_channel_name", "broadcast_channel_avatar")
    BROADCAST_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_CHANNEL_AVATAR_FIELD_NUMBER: _ClassVar[int]
    broadcast_channel_id: int
    broadcast_channel_name: str
    broadcast_channel_avatar: str
    def __init__(self, broadcast_channel_id: _Optional[int] = ..., broadcast_channel_name: _Optional[str] = ..., broadcast_channel_avatar: _Optional[str] = ...) -> None: ...

class CBroadcast_SendThumbnailToRelay_Notification(_message.Message):
    __slots__ = ("thumbnail_upload_token", "thumbnail_broadcast_session_id", "thumbnail_data", "thumbnail_width", "thumbnail_height")
    THUMBNAIL_UPLOAD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_DATA_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    thumbnail_upload_token: str
    thumbnail_broadcast_session_id: int
    thumbnail_data: bytes
    thumbnail_width: int
    thumbnail_height: int
    def __init__(self, thumbnail_upload_token: _Optional[str] = ..., thumbnail_broadcast_session_id: _Optional[int] = ..., thumbnail_data: _Optional[bytes] = ..., thumbnail_width: _Optional[int] = ..., thumbnail_height: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCNeedTURNServer_Notification(_message.Message):
    __slots__ = ("broadcast_session_id",)
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    broadcast_session_id: int
    def __init__(self, broadcast_session_id: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCStart_Notification(_message.Message):
    __slots__ = ("broadcast_session_id", "webrtc_session_id", "viewer_steamid", "viewer_token")
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    VIEWER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    VIEWER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    broadcast_session_id: int
    webrtc_session_id: int
    viewer_steamid: int
    viewer_token: int
    def __init__(self, broadcast_session_id: _Optional[int] = ..., webrtc_session_id: _Optional[int] = ..., viewer_steamid: _Optional[int] = ..., viewer_token: _Optional[int] = ...) -> None: ...

class CBroadcast_WebRTCSetAnswer_Notification(_message.Message):
    __slots__ = ("broadcast_session_id", "webrtc_session_id", "answer")
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    broadcast_session_id: int
    webrtc_session_id: int
    answer: str
    def __init__(self, broadcast_session_id: _Optional[int] = ..., webrtc_session_id: _Optional[int] = ..., answer: _Optional[str] = ...) -> None: ...

class CBroadcast_WebRTCAddViewerCandidate_Notification(_message.Message):
    __slots__ = ("broadcast_session_id", "webrtc_session_id", "candidate")
    BROADCAST_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    broadcast_session_id: int
    webrtc_session_id: int
    candidate: CBroadcast_WebRTC_Candidate
    def __init__(self, broadcast_session_id: _Optional[int] = ..., webrtc_session_id: _Optional[int] = ..., candidate: _Optional[_Union[CBroadcast_WebRTC_Candidate, _Mapping]] = ...) -> None: ...

class Broadcast(_service.service): ...

class Broadcast_Stub(Broadcast): ...

class BroadcastClient(_service.service): ...

class BroadcastClient_Stub(BroadcastClient): ...
