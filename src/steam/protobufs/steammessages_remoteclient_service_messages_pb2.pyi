from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ECLientTaskListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EClientTask_DownloadClip: _ClassVar[ECLientTaskListType]
k_EClientTask_DownloadClip: ECLientTaskListType

class CRemoteClient_CreateSession_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_CreateSession_Response(_message.Message):
    __slots__ = ("session_id", "euniverse")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    EUNIVERSE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    euniverse: int
    def __init__(self, session_id: _Optional[int] = ..., euniverse: _Optional[int] = ...) -> None: ...

class CRemoteClient_DeleteSession_Notification(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class CRemoteClient_StartPairing_Request(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class CRemoteClient_StartPairing_Response(_message.Message):
    __slots__ = ("pin",)
    PIN_FIELD_NUMBER: _ClassVar[int]
    pin: int
    def __init__(self, pin: _Optional[int] = ...) -> None: ...

class CRemoteClient_SetPairingInfo_Request(_message.Message):
    __slots__ = ("session_id", "device_id", "request")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    device_id: int
    request: bytes
    def __init__(self, session_id: _Optional[int] = ..., device_id: _Optional[int] = ..., request: _Optional[bytes] = ...) -> None: ...

class CRemoteClient_SetPairingInfo_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_GetPairingInfo_Request(_message.Message):
    __slots__ = ("pin",)
    PIN_FIELD_NUMBER: _ClassVar[int]
    pin: int
    def __init__(self, pin: _Optional[int] = ...) -> None: ...

class CRemoteClient_GetPairingInfo_Response(_message.Message):
    __slots__ = ("session_id", "device_id", "request")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    device_id: int
    request: bytes
    def __init__(self, session_id: _Optional[int] = ..., device_id: _Optional[int] = ..., request: _Optional[bytes] = ...) -> None: ...

class CRemoteClient_CancelPairing_Request(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class CRemoteClient_CancelPairing_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_RegisterStatusUpdate_Notification(_message.Message):
    __slots__ = ("session_id", "steamid", "device_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    steamid: int
    device_id: int
    def __init__(self, session_id: _Optional[int] = ..., steamid: _Optional[int] = ..., device_id: _Optional[int] = ...) -> None: ...

class CRemoteClient_UnregisterStatusUpdate_Notification(_message.Message):
    __slots__ = ("session_id", "steamid")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    steamid: int
    def __init__(self, session_id: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CRemoteClient_DeviceDetails(_message.Message):
    __slots__ = ("device_friendly_name", "os_type", "gaming_device_type")
    DEVICE_FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    OS_TYPE_FIELD_NUMBER: _ClassVar[int]
    GAMING_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    device_friendly_name: str
    os_type: int
    gaming_device_type: int
    def __init__(self, device_friendly_name: _Optional[str] = ..., os_type: _Optional[int] = ..., gaming_device_type: _Optional[int] = ...) -> None: ...

class CRemoteClient_Online_Notification(_message.Message):
    __slots__ = ("steamid", "remote_client_id", "device_details")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    remote_client_id: int
    device_details: CRemoteClient_DeviceDetails
    def __init__(self, steamid: _Optional[int] = ..., remote_client_id: _Optional[int] = ..., device_details: _Optional[_Union[CRemoteClient_DeviceDetails, _Mapping]] = ...) -> None: ...

class CRemoteClient_GetRecentClients_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_ClientLogin(_message.Message):
    __slots__ = ("remote_client_id", "token_id", "device_details")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    token_id: int
    device_details: CRemoteClient_DeviceDetails
    def __init__(self, remote_client_id: _Optional[int] = ..., token_id: _Optional[int] = ..., device_details: _Optional[_Union[CRemoteClient_DeviceDetails, _Mapping]] = ...) -> None: ...

class CRemoteClient_ClientDetails(_message.Message):
    __slots__ = ("remote_client_id", "device_details", "last_seen", "city", "state", "country", "is_online")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    device_details: CRemoteClient_DeviceDetails
    last_seen: int
    city: str
    state: str
    country: str
    is_online: bool
    def __init__(self, remote_client_id: _Optional[int] = ..., device_details: _Optional[_Union[CRemoteClient_DeviceDetails, _Mapping]] = ..., last_seen: _Optional[int] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., is_online: bool = ...) -> None: ...

class CRemoteClient_GetRecentClients_Response(_message.Message):
    __slots__ = ("clients",)
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[CRemoteClient_ClientDetails]
    def __init__(self, clients: _Optional[_Iterable[_Union[CRemoteClient_ClientDetails, _Mapping]]] = ...) -> None: ...

class CRemoteClient_Task(_message.Message):
    __slots__ = ("type", "task_id", "url", "file_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    type: ECLientTaskListType
    task_id: int
    url: str
    file_id: int
    def __init__(self, type: _Optional[_Union[ECLientTaskListType, str]] = ..., task_id: _Optional[int] = ..., url: _Optional[str] = ..., file_id: _Optional[int] = ...) -> None: ...

class CRemoteClient_AddClientTask_Request(_message.Message):
    __slots__ = ("remote_client_id", "task")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    task: CRemoteClient_Task
    def __init__(self, remote_client_id: _Optional[int] = ..., task: _Optional[_Union[CRemoteClient_Task, _Mapping]] = ...) -> None: ...

class CRemoteClient_AddClientTask_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_TaskList_Notification(_message.Message):
    __slots__ = ("remote_client_id", "tasklist")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TASKLIST_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    tasklist: _containers.RepeatedCompositeFieldContainer[CRemoteClient_Task]
    def __init__(self, remote_client_id: _Optional[int] = ..., tasklist: _Optional[_Iterable[_Union[CRemoteClient_Task, _Mapping]]] = ...) -> None: ...

class CRemoteClient_MarkTaskComplete_Request(_message.Message):
    __slots__ = ("remote_client_id", "task_id", "content_id")
    REMOTE_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    remote_client_id: int
    task_id: int
    content_id: str
    def __init__(self, remote_client_id: _Optional[int] = ..., task_id: _Optional[int] = ..., content_id: _Optional[str] = ...) -> None: ...

class CRemoteClient_MarkTaskComplete_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_RemotePacket_Notification(_message.Message):
    __slots__ = ("session_id", "steamid", "payload")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    steamid: int
    payload: bytes
    def __init__(self, session_id: _Optional[int] = ..., steamid: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CRemoteClient_ReplyPacket_Notification(_message.Message):
    __slots__ = ("session_id", "payload")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    payload: bytes
    def __init__(self, session_id: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CRemoteClient_GetReplies_Request(_message.Message):
    __slots__ = ("session_id",)
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    def __init__(self, session_id: _Optional[int] = ...) -> None: ...

class CRemoteClient_GetReplies_Response(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, payload: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CRemoteClient_AllocateRelayServer_Request(_message.Message):
    __slots__ = ("cellid", "credentials")
    CELLID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    cellid: int
    credentials: str
    def __init__(self, cellid: _Optional[int] = ..., credentials: _Optional[str] = ...) -> None: ...

class CRemoteClient_AllocateRelayServer_Response(_message.Message):
    __slots__ = ("relay_server",)
    RELAY_SERVER_FIELD_NUMBER: _ClassVar[int]
    relay_server: str
    def __init__(self, relay_server: _Optional[str] = ...) -> None: ...

class CRemoteClient_AllocateSDR_Request(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CRemoteClient_AllocateSDR_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_SteamBroadcast_Notification(_message.Message):
    __slots__ = ("steamid", "clientid", "payload")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    CLIENTID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    clientid: int
    payload: bytes
    def __init__(self, steamid: _Optional[int] = ..., clientid: _Optional[int] = ..., payload: _Optional[bytes] = ...) -> None: ...

class CRemoteClient_SteamToSteam_Notification(_message.Message):
    __slots__ = ("steamid", "src_clientid", "dst_clientid", "secretid", "encrypted_payload")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SRC_CLIENTID_FIELD_NUMBER: _ClassVar[int]
    DST_CLIENTID_FIELD_NUMBER: _ClassVar[int]
    SECRETID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    src_clientid: int
    dst_clientid: int
    secretid: int
    encrypted_payload: bytes
    def __init__(self, steamid: _Optional[int] = ..., src_clientid: _Optional[int] = ..., dst_clientid: _Optional[int] = ..., secretid: _Optional[int] = ..., encrypted_payload: _Optional[bytes] = ...) -> None: ...

class CRemotePlay_SessionStarted_Request(_message.Message):
    __slots__ = ("host_account_id", "client_account_id", "appid", "device_form_factor", "remote_play_together", "guest_session")
    HOST_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PLAY_TOGETHER_FIELD_NUMBER: _ClassVar[int]
    GUEST_SESSION_FIELD_NUMBER: _ClassVar[int]
    host_account_id: int
    client_account_id: int
    appid: int
    device_form_factor: int
    remote_play_together: bool
    guest_session: bool
    def __init__(self, host_account_id: _Optional[int] = ..., client_account_id: _Optional[int] = ..., appid: _Optional[int] = ..., device_form_factor: _Optional[int] = ..., remote_play_together: bool = ..., guest_session: bool = ...) -> None: ...

class CRemotePlay_SessionStarted_Response(_message.Message):
    __slots__ = ("record_id",)
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    record_id: int
    def __init__(self, record_id: _Optional[int] = ...) -> None: ...

class CRemotePlay_SessionStopped_Notification(_message.Message):
    __slots__ = ("record_id", "used_x264", "used_h264", "used_hevc")
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    USED_X264_FIELD_NUMBER: _ClassVar[int]
    USED_H264_FIELD_NUMBER: _ClassVar[int]
    USED_HEVC_FIELD_NUMBER: _ClassVar[int]
    record_id: int
    used_x264: bool
    used_h264: bool
    used_hevc: bool
    def __init__(self, record_id: _Optional[int] = ..., used_x264: bool = ..., used_h264: bool = ..., used_hevc: bool = ...) -> None: ...

class CRemotePlayTogether_Notification(_message.Message):
    __slots__ = ("steamid", "group_updated")
    class Player(_message.Message):
        __slots__ = ("steamid", "guestid", "avatar_hash", "keyboard_enabled", "mouse_enabled", "controller_enabled")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        GUESTID_FIELD_NUMBER: _ClassVar[int]
        AVATAR_HASH_FIELD_NUMBER: _ClassVar[int]
        KEYBOARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MOUSE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        guestid: int
        avatar_hash: bytes
        keyboard_enabled: bool
        mouse_enabled: bool
        controller_enabled: bool
        def __init__(self, steamid: _Optional[int] = ..., guestid: _Optional[int] = ..., avatar_hash: _Optional[bytes] = ..., keyboard_enabled: bool = ..., mouse_enabled: bool = ..., controller_enabled: bool = ...) -> None: ...
    class ControllerSlot_obsolete(_message.Message):
        __slots__ = ("slotid", "steamid")
        SLOTID_FIELD_NUMBER: _ClassVar[int]
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        slotid: int
        steamid: int
        def __init__(self, slotid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...
    class ControllerSlot(_message.Message):
        __slots__ = ("slotid", "player", "controller_type")
        SLOTID_FIELD_NUMBER: _ClassVar[int]
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
        slotid: int
        player: CRemotePlayTogether_Notification.Player
        controller_type: int
        def __init__(self, slotid: _Optional[int] = ..., player: _Optional[_Union[CRemotePlayTogether_Notification.Player, _Mapping]] = ..., controller_type: _Optional[int] = ...) -> None: ...
    class GroupUpdated(_message.Message):
        __slots__ = ("host_steamid", "host_clientid", "players_obsolete", "host_gameid", "controller_slots_obsolete", "has_new_players", "player_slots", "controller_slots")
        HOST_STEAMID_FIELD_NUMBER: _ClassVar[int]
        HOST_CLIENTID_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
        HOST_GAMEID_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_SLOTS_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
        HAS_NEW_PLAYERS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SLOTS_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_SLOTS_FIELD_NUMBER: _ClassVar[int]
        host_steamid: int
        host_clientid: int
        players_obsolete: _containers.RepeatedScalarFieldContainer[int]
        host_gameid: int
        controller_slots_obsolete: _containers.RepeatedCompositeFieldContainer[CRemotePlayTogether_Notification.ControllerSlot_obsolete]
        has_new_players: bool
        player_slots: _containers.RepeatedCompositeFieldContainer[CRemotePlayTogether_Notification.Player]
        controller_slots: _containers.RepeatedCompositeFieldContainer[CRemotePlayTogether_Notification.ControllerSlot]
        def __init__(self, host_steamid: _Optional[int] = ..., host_clientid: _Optional[int] = ..., players_obsolete: _Optional[_Iterable[int]] = ..., host_gameid: _Optional[int] = ..., controller_slots_obsolete: _Optional[_Iterable[_Union[CRemotePlayTogether_Notification.ControllerSlot_obsolete, _Mapping]]] = ..., has_new_players: bool = ..., player_slots: _Optional[_Iterable[_Union[CRemotePlayTogether_Notification.Player, _Mapping]]] = ..., controller_slots: _Optional[_Iterable[_Union[CRemotePlayTogether_Notification.ControllerSlot, _Mapping]]] = ...) -> None: ...
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    GROUP_UPDATED_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    group_updated: CRemotePlayTogether_Notification.GroupUpdated
    def __init__(self, steamid: _Optional[int] = ..., group_updated: _Optional[_Union[CRemotePlayTogether_Notification.GroupUpdated, _Mapping]] = ...) -> None: ...

class CRemoteClient_CreateRemotePlayTogetherInvitation_Request(_message.Message):
    __slots__ = ("appid", "launch_parameters")
    APPID_FIELD_NUMBER: _ClassVar[int]
    LAUNCH_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    launch_parameters: str
    def __init__(self, appid: _Optional[int] = ..., launch_parameters: _Optional[str] = ...) -> None: ...

class CRemoteClient_CreateRemotePlayTogetherInvitation_Response(_message.Message):
    __slots__ = ("invitation_code",)
    INVITATION_CODE_FIELD_NUMBER: _ClassVar[int]
    invitation_code: str
    def __init__(self, invitation_code: _Optional[str] = ...) -> None: ...

class CRemoteClient_DeleteRemotePlayTogetherInvitation_Request(_message.Message):
    __slots__ = ("invitation_code",)
    INVITATION_CODE_FIELD_NUMBER: _ClassVar[int]
    invitation_code: str
    def __init__(self, invitation_code: _Optional[str] = ...) -> None: ...

class CRemoteClient_DeleteRemotePlayTogetherInvitation_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRemoteClient_LookupRemotePlayTogetherInvitation_Request(_message.Message):
    __slots__ = ("invitation_code",)
    INVITATION_CODE_FIELD_NUMBER: _ClassVar[int]
    invitation_code: str
    def __init__(self, invitation_code: _Optional[str] = ...) -> None: ...

class CRemoteClient_LookupRemotePlayTogetherInvitation_Response(_message.Message):
    __slots__ = ("invitation_url",)
    INVITATION_URL_FIELD_NUMBER: _ClassVar[int]
    invitation_url: str
    def __init__(self, invitation_url: _Optional[str] = ...) -> None: ...

class CCMRemoteClient_ClientMessage(_message.Message):
    __slots__ = ("create_session_request", "start_pairing_request", "set_pairing_info_request", "cancel_pairing_request", "register_status_update", "unregister_status_update", "remote_packet")
    CREATE_SESSION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    START_PAIRING_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SET_PAIRING_INFO_REQUEST_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PAIRING_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REGISTER_STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UNREGISTER_STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PACKET_FIELD_NUMBER: _ClassVar[int]
    create_session_request: CRemoteClient_CreateSession_Request
    start_pairing_request: CRemoteClient_StartPairing_Request
    set_pairing_info_request: CRemoteClient_SetPairingInfo_Request
    cancel_pairing_request: CRemoteClient_CancelPairing_Request
    register_status_update: CRemoteClient_RegisterStatusUpdate_Notification
    unregister_status_update: CRemoteClient_UnregisterStatusUpdate_Notification
    remote_packet: CRemoteClient_RemotePacket_Notification
    def __init__(self, create_session_request: _Optional[_Union[CRemoteClient_CreateSession_Request, _Mapping]] = ..., start_pairing_request: _Optional[_Union[CRemoteClient_StartPairing_Request, _Mapping]] = ..., set_pairing_info_request: _Optional[_Union[CRemoteClient_SetPairingInfo_Request, _Mapping]] = ..., cancel_pairing_request: _Optional[_Union[CRemoteClient_CancelPairing_Request, _Mapping]] = ..., register_status_update: _Optional[_Union[CRemoteClient_RegisterStatusUpdate_Notification, _Mapping]] = ..., unregister_status_update: _Optional[_Union[CRemoteClient_UnregisterStatusUpdate_Notification, _Mapping]] = ..., remote_packet: _Optional[_Union[CRemoteClient_RemotePacket_Notification, _Mapping]] = ...) -> None: ...

class CCMRemoteClient_ServerMessage(_message.Message):
    __slots__ = ("result", "create_session_response", "start_pairing_response", "set_pairing_info_response", "cancel_pairing_response", "reply_packet")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CREATE_SESSION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    START_PAIRING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SET_PAIRING_INFO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PAIRING_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REPLY_PACKET_FIELD_NUMBER: _ClassVar[int]
    result: int
    create_session_response: CRemoteClient_CreateSession_Response
    start_pairing_response: CRemoteClient_StartPairing_Response
    set_pairing_info_response: CRemoteClient_SetPairingInfo_Response
    cancel_pairing_response: CRemoteClient_CancelPairing_Response
    reply_packet: CRemoteClient_GetReplies_Response
    def __init__(self, result: _Optional[int] = ..., create_session_response: _Optional[_Union[CRemoteClient_CreateSession_Response, _Mapping]] = ..., start_pairing_response: _Optional[_Union[CRemoteClient_StartPairing_Response, _Mapping]] = ..., set_pairing_info_response: _Optional[_Union[CRemoteClient_SetPairingInfo_Response, _Mapping]] = ..., cancel_pairing_response: _Optional[_Union[CRemoteClient_CancelPairing_Response, _Mapping]] = ..., reply_packet: _Optional[_Union[CRemoteClient_GetReplies_Response, _Mapping]] = ...) -> None: ...
