from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ERemoteClientBroadcastMsg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ERemoteClientBroadcastMsgDiscovery: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteClientBroadcastMsgStatus: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteClientBroadcastMsgOffline: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceAuthorizationRequest: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceAuthorizationResponse: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceStreamingRequest: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceStreamingResponse: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceProofRequest: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceProofResponse: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceAuthorizationCancelRequest: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceStreamingCancelRequest: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteClientBroadcastMsgClientIDDeconflict: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceStreamTransportSignal: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceStreamingProgress: _ClassVar[ERemoteClientBroadcastMsg]
    k_ERemoteDeviceAuthorizationConfirmed: _ClassVar[ERemoteClientBroadcastMsg]

class ERemoteClientService(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ERemoteClientServiceNone: _ClassVar[ERemoteClientService]
    k_ERemoteClientServiceRemoteControl: _ClassVar[ERemoteClientService]
    k_ERemoteClientServiceGameStreaming: _ClassVar[ERemoteClientService]
    k_ERemoteClientServiceSiteLicense: _ClassVar[ERemoteClientService]
    k_ERemoteClientServiceContentCache: _ClassVar[ERemoteClientService]
    k_ERemoteClientServiceContentServer: _ClassVar[ERemoteClientService]

class EVRLinkCaps(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EVRLinkCapsUnknown: _ClassVar[EVRLinkCaps]
    k_EVRLinkCapsAvailable: _ClassVar[EVRLinkCaps]
    k_EVRLinkCapsUnimplemented: _ClassVar[EVRLinkCaps]
    k_EVRLinkCapsMissingHardwareEncoding: _ClassVar[EVRLinkCaps]

class ERemoteDeviceAuthorizationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ERemoteDeviceAuthorizationSuccess: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationDenied: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationNotLoggedIn: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationOffline: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationBusy: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationInProgress: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationTimedOut: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationFailed: _ClassVar[ERemoteDeviceAuthorizationResult]
    k_ERemoteDeviceAuthorizationCanceled: _ClassVar[ERemoteDeviceAuthorizationResult]

class EStreamDeviceFormFactor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamDeviceFormFactorUnknown: _ClassVar[EStreamDeviceFormFactor]
    k_EStreamDeviceFormFactorPhone: _ClassVar[EStreamDeviceFormFactor]
    k_EStreamDeviceFormFactorTablet: _ClassVar[EStreamDeviceFormFactor]
    k_EStreamDeviceFormFactorComputer: _ClassVar[EStreamDeviceFormFactor]
    k_EStreamDeviceFormFactorTV: _ClassVar[EStreamDeviceFormFactor]
    k_EStreamDeviceFormFactorVRHeadset: _ClassVar[EStreamDeviceFormFactor]

class EStreamTransport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamTransportNone: _ClassVar[EStreamTransport]
    k_EStreamTransportUDP: _ClassVar[EStreamTransport]
    k_EStreamTransportUDPRelay: _ClassVar[EStreamTransport]
    k_EStreamTransportWebRTC_OBSOLETE: _ClassVar[EStreamTransport]
    k_EStreamTransportSDR: _ClassVar[EStreamTransport]
    k_EStreamTransportUDP_SNS: _ClassVar[EStreamTransport]
    k_EStreamTransportUDPRelay_SNS: _ClassVar[EStreamTransport]

class EStreamInterface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamInterfaceDefault: _ClassVar[EStreamInterface]
    k_EStreamInterfaceRecentGames: _ClassVar[EStreamInterface]
    k_EStreamInterfaceBigPicture: _ClassVar[EStreamInterface]
    k_EStreamInterfaceDesktop: _ClassVar[EStreamInterface]
    k_EStreamInterfaceSteamVR: _ClassVar[EStreamInterface]

class ERemoteDeviceStreamingResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ERemoteDeviceStreamingSuccess: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingUnauthorized: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingScreenLocked: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingFailed: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingBusy: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingInProgress: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingCanceled: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingDriversNotInstalled: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingDisabled: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingBroadcastingActive: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingVRActive: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingPINRequired: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingTransportUnavailable: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingInvisible: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingGameLaunchFailed: _ClassVar[ERemoteDeviceStreamingResult]
    k_ERemoteDeviceStreamingSteamVRNotInstalled: _ClassVar[ERemoteDeviceStreamingResult]
k_ERemoteClientBroadcastMsgDiscovery: ERemoteClientBroadcastMsg
k_ERemoteClientBroadcastMsgStatus: ERemoteClientBroadcastMsg
k_ERemoteClientBroadcastMsgOffline: ERemoteClientBroadcastMsg
k_ERemoteDeviceAuthorizationRequest: ERemoteClientBroadcastMsg
k_ERemoteDeviceAuthorizationResponse: ERemoteClientBroadcastMsg
k_ERemoteDeviceStreamingRequest: ERemoteClientBroadcastMsg
k_ERemoteDeviceStreamingResponse: ERemoteClientBroadcastMsg
k_ERemoteDeviceProofRequest: ERemoteClientBroadcastMsg
k_ERemoteDeviceProofResponse: ERemoteClientBroadcastMsg
k_ERemoteDeviceAuthorizationCancelRequest: ERemoteClientBroadcastMsg
k_ERemoteDeviceStreamingCancelRequest: ERemoteClientBroadcastMsg
k_ERemoteClientBroadcastMsgClientIDDeconflict: ERemoteClientBroadcastMsg
k_ERemoteDeviceStreamTransportSignal: ERemoteClientBroadcastMsg
k_ERemoteDeviceStreamingProgress: ERemoteClientBroadcastMsg
k_ERemoteDeviceAuthorizationConfirmed: ERemoteClientBroadcastMsg
k_ERemoteClientServiceNone: ERemoteClientService
k_ERemoteClientServiceRemoteControl: ERemoteClientService
k_ERemoteClientServiceGameStreaming: ERemoteClientService
k_ERemoteClientServiceSiteLicense: ERemoteClientService
k_ERemoteClientServiceContentCache: ERemoteClientService
k_ERemoteClientServiceContentServer: ERemoteClientService
k_EVRLinkCapsUnknown: EVRLinkCaps
k_EVRLinkCapsAvailable: EVRLinkCaps
k_EVRLinkCapsUnimplemented: EVRLinkCaps
k_EVRLinkCapsMissingHardwareEncoding: EVRLinkCaps
k_ERemoteDeviceAuthorizationSuccess: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationDenied: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationNotLoggedIn: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationOffline: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationBusy: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationInProgress: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationTimedOut: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationFailed: ERemoteDeviceAuthorizationResult
k_ERemoteDeviceAuthorizationCanceled: ERemoteDeviceAuthorizationResult
k_EStreamDeviceFormFactorUnknown: EStreamDeviceFormFactor
k_EStreamDeviceFormFactorPhone: EStreamDeviceFormFactor
k_EStreamDeviceFormFactorTablet: EStreamDeviceFormFactor
k_EStreamDeviceFormFactorComputer: EStreamDeviceFormFactor
k_EStreamDeviceFormFactorTV: EStreamDeviceFormFactor
k_EStreamDeviceFormFactorVRHeadset: EStreamDeviceFormFactor
k_EStreamTransportNone: EStreamTransport
k_EStreamTransportUDP: EStreamTransport
k_EStreamTransportUDPRelay: EStreamTransport
k_EStreamTransportWebRTC_OBSOLETE: EStreamTransport
k_EStreamTransportSDR: EStreamTransport
k_EStreamTransportUDP_SNS: EStreamTransport
k_EStreamTransportUDPRelay_SNS: EStreamTransport
k_EStreamInterfaceDefault: EStreamInterface
k_EStreamInterfaceRecentGames: EStreamInterface
k_EStreamInterfaceBigPicture: EStreamInterface
k_EStreamInterfaceDesktop: EStreamInterface
k_EStreamInterfaceSteamVR: EStreamInterface
k_ERemoteDeviceStreamingSuccess: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingUnauthorized: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingScreenLocked: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingFailed: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingBusy: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingInProgress: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingCanceled: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingDriversNotInstalled: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingDisabled: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingBroadcastingActive: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingVRActive: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingPINRequired: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingTransportUnavailable: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingInvisible: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingGameLaunchFailed: ERemoteDeviceStreamingResult
k_ERemoteDeviceStreamingSteamVRNotInstalled: ERemoteDeviceStreamingResult

class CMsgRemoteClientBroadcastHeader(_message.Message):
    __slots__ = ("client_id", "msg_type", "instance_id", "device_id_OBSOLETE", "device_token")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    client_id: int
    msg_type: ERemoteClientBroadcastMsg
    instance_id: int
    device_id_OBSOLETE: int
    device_token: bytes
    def __init__(self, client_id: _Optional[int] = ..., msg_type: _Optional[_Union[ERemoteClientBroadcastMsg, str]] = ..., instance_id: _Optional[int] = ..., device_id_OBSOLETE: _Optional[int] = ..., device_token: _Optional[bytes] = ...) -> None: ...

class CMsgRemoteClientBroadcastStatus(_message.Message):
    __slots__ = ("version", "min_version", "connect_port", "hostname", "enabled_services", "ostype", "is64bit", "users", "euniverse", "timestamp", "screen_locked", "games_running", "mac_addresses", "download_lan_peer_group", "broadcasting_active", "vr_active", "content_cache_port", "ip_addresses", "public_ip_address", "remoteplay_active", "supported_services", "steam_deck", "steam_version", "vr_link_caps")
    class User(_message.Message):
        __slots__ = ("steamid", "auth_key_id")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        AUTH_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        auth_key_id: int
        def __init__(self, steamid: _Optional[int] = ..., auth_key_id: _Optional[int] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    MIN_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONNECT_PORT_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    OSTYPE_FIELD_NUMBER: _ClassVar[int]
    IS64BIT_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    EUNIVERSE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCREEN_LOCKED_FIELD_NUMBER: _ClassVar[int]
    GAMES_RUNNING_FIELD_NUMBER: _ClassVar[int]
    MAC_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LAN_PEER_GROUP_FIELD_NUMBER: _ClassVar[int]
    BROADCASTING_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    VR_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CACHE_PORT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REMOTEPLAY_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    STEAM_DECK_FIELD_NUMBER: _ClassVar[int]
    STEAM_VERSION_FIELD_NUMBER: _ClassVar[int]
    VR_LINK_CAPS_FIELD_NUMBER: _ClassVar[int]
    version: int
    min_version: int
    connect_port: int
    hostname: str
    enabled_services: int
    ostype: int
    is64bit: bool
    users: _containers.RepeatedCompositeFieldContainer[CMsgRemoteClientBroadcastStatus.User]
    euniverse: int
    timestamp: int
    screen_locked: bool
    games_running: bool
    mac_addresses: _containers.RepeatedScalarFieldContainer[str]
    download_lan_peer_group: int
    broadcasting_active: bool
    vr_active: bool
    content_cache_port: int
    ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    public_ip_address: str
    remoteplay_active: bool
    supported_services: int
    steam_deck: bool
    steam_version: int
    vr_link_caps: EVRLinkCaps
    def __init__(self, version: _Optional[int] = ..., min_version: _Optional[int] = ..., connect_port: _Optional[int] = ..., hostname: _Optional[str] = ..., enabled_services: _Optional[int] = ..., ostype: _Optional[int] = ..., is64bit: bool = ..., users: _Optional[_Iterable[_Union[CMsgRemoteClientBroadcastStatus.User, _Mapping]]] = ..., euniverse: _Optional[int] = ..., timestamp: _Optional[int] = ..., screen_locked: bool = ..., games_running: bool = ..., mac_addresses: _Optional[_Iterable[str]] = ..., download_lan_peer_group: _Optional[int] = ..., broadcasting_active: bool = ..., vr_active: bool = ..., content_cache_port: _Optional[int] = ..., ip_addresses: _Optional[_Iterable[str]] = ..., public_ip_address: _Optional[str] = ..., remoteplay_active: bool = ..., supported_services: _Optional[int] = ..., steam_deck: bool = ..., steam_version: _Optional[int] = ..., vr_link_caps: _Optional[_Union[EVRLinkCaps, str]] = ...) -> None: ...

class CMsgRemoteClientBroadcastDiscovery(_message.Message):
    __slots__ = ("seq_num", "client_ids")
    SEQ_NUM_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    seq_num: int
    client_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, seq_num: _Optional[int] = ..., client_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgRemoteClientBroadcastClientIDDeconflict(_message.Message):
    __slots__ = ("client_ids",)
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    client_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, client_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgRemoteDeviceAuthorizationRequest(_message.Message):
    __slots__ = ("device_token", "device_name", "encrypted_request", "auth_key", "request_id")
    class EKeyEscrowUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        k_EKeyEscrowUsageStreamingDevice: _ClassVar[CMsgRemoteDeviceAuthorizationRequest.EKeyEscrowUsage]
    k_EKeyEscrowUsageStreamingDevice: CMsgRemoteDeviceAuthorizationRequest.EKeyEscrowUsage
    class CKeyEscrow_Ticket(_message.Message):
        __slots__ = ("password", "identifier", "payload", "timestamp", "usage", "device_name", "device_model", "device_serial", "device_provisioning_id")
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        USAGE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SERIAL_FIELD_NUMBER: _ClassVar[int]
        DEVICE_PROVISIONING_ID_FIELD_NUMBER: _ClassVar[int]
        password: bytes
        identifier: int
        payload: bytes
        timestamp: int
        usage: CMsgRemoteDeviceAuthorizationRequest.EKeyEscrowUsage
        device_name: str
        device_model: str
        device_serial: str
        device_provisioning_id: int
        def __init__(self, password: _Optional[bytes] = ..., identifier: _Optional[int] = ..., payload: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., usage: _Optional[_Union[CMsgRemoteDeviceAuthorizationRequest.EKeyEscrowUsage, str]] = ..., device_name: _Optional[str] = ..., device_model: _Optional[str] = ..., device_serial: _Optional[str] = ..., device_provisioning_id: _Optional[int] = ...) -> None: ...
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_REQUEST_FIELD_NUMBER: _ClassVar[int]
    AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    device_token: bytes
    device_name: str
    encrypted_request: bytes
    auth_key: bytes
    request_id: int
    def __init__(self, device_token: _Optional[bytes] = ..., device_name: _Optional[str] = ..., encrypted_request: _Optional[bytes] = ..., auth_key: _Optional[bytes] = ..., request_id: _Optional[int] = ...) -> None: ...

class CMsgRemoteDeviceAuthorizationCancelRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CMsgRemoteDeviceAuthorizationResponse(_message.Message):
    __slots__ = ("result", "steamid", "auth_key", "device_token")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    AUTH_KEY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    result: ERemoteDeviceAuthorizationResult
    steamid: int
    auth_key: bytes
    device_token: bytes
    def __init__(self, result: _Optional[_Union[ERemoteDeviceAuthorizationResult, str]] = ..., steamid: _Optional[int] = ..., auth_key: _Optional[bytes] = ..., device_token: _Optional[bytes] = ...) -> None: ...

class CMsgRemoteDeviceAuthorizationConfirmed(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: ERemoteDeviceAuthorizationResult
    def __init__(self, result: _Optional[_Union[ERemoteDeviceAuthorizationResult, str]] = ...) -> None: ...

class CMsgRemoteDeviceStreamingRequest(_message.Message):
    __slots__ = ("request_id", "maximum_resolution_x", "maximum_resolution_y", "audio_channel_count", "device_version", "stream_desktop", "device_token", "pin", "enable_video_streaming", "enable_audio_streaming", "enable_input_streaming", "network_test", "client_id", "supported_transport", "restricted", "form_factor", "gamepad_count", "gamepads", "gameid", "stream_interface")
    class ReservedGamepad(_message.Message):
        __slots__ = ("controller_type", "controller_subtype")
        CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_SUBTYPE_FIELD_NUMBER: _ClassVar[int]
        controller_type: int
        controller_subtype: int
        def __init__(self, controller_type: _Optional[int] = ..., controller_subtype: _Optional[int] = ...) -> None: ...
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_RESOLUTION_X_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_RESOLUTION_Y_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_VERSION_FIELD_NUMBER: _ClassVar[int]
    STREAM_DESKTOP_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VIDEO_STREAMING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIO_STREAMING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INPUT_STREAMING_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TEST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    GAMEPAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    GAMEPADS_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    STREAM_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    maximum_resolution_x: int
    maximum_resolution_y: int
    audio_channel_count: int
    device_version: str
    stream_desktop: bool
    device_token: bytes
    pin: bytes
    enable_video_streaming: bool
    enable_audio_streaming: bool
    enable_input_streaming: bool
    network_test: bool
    client_id: int
    supported_transport: _containers.RepeatedScalarFieldContainer[EStreamTransport]
    restricted: bool
    form_factor: EStreamDeviceFormFactor
    gamepad_count: int
    gamepads: _containers.RepeatedCompositeFieldContainer[CMsgRemoteDeviceStreamingRequest.ReservedGamepad]
    gameid: int
    stream_interface: EStreamInterface
    def __init__(self, request_id: _Optional[int] = ..., maximum_resolution_x: _Optional[int] = ..., maximum_resolution_y: _Optional[int] = ..., audio_channel_count: _Optional[int] = ..., device_version: _Optional[str] = ..., stream_desktop: bool = ..., device_token: _Optional[bytes] = ..., pin: _Optional[bytes] = ..., enable_video_streaming: bool = ..., enable_audio_streaming: bool = ..., enable_input_streaming: bool = ..., network_test: bool = ..., client_id: _Optional[int] = ..., supported_transport: _Optional[_Iterable[_Union[EStreamTransport, str]]] = ..., restricted: bool = ..., form_factor: _Optional[_Union[EStreamDeviceFormFactor, str]] = ..., gamepad_count: _Optional[int] = ..., gamepads: _Optional[_Iterable[_Union[CMsgRemoteDeviceStreamingRequest.ReservedGamepad, _Mapping]]] = ..., gameid: _Optional[int] = ..., stream_interface: _Optional[_Union[EStreamInterface, str]] = ...) -> None: ...

class CMsgRemoteDeviceStreamingCancelRequest(_message.Message):
    __slots__ = ("request_id",)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    def __init__(self, request_id: _Optional[int] = ...) -> None: ...

class CMsgRemoteDeviceStreamingProgress(_message.Message):
    __slots__ = ("request_id", "progress")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    progress: float
    def __init__(self, request_id: _Optional[int] = ..., progress: _Optional[float] = ...) -> None: ...

class CMsgRemoteDeviceStreamingResponse(_message.Message):
    __slots__ = ("request_id", "result", "port", "encrypted_session_key", "transport", "relay_server", "cert")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_FIELD_NUMBER: _ClassVar[int]
    RELAY_SERVER_FIELD_NUMBER: _ClassVar[int]
    CERT_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    result: ERemoteDeviceStreamingResult
    port: int
    encrypted_session_key: bytes
    transport: EStreamTransport
    relay_server: str
    cert: str
    def __init__(self, request_id: _Optional[int] = ..., result: _Optional[_Union[ERemoteDeviceStreamingResult, str]] = ..., port: _Optional[int] = ..., encrypted_session_key: _Optional[bytes] = ..., transport: _Optional[_Union[EStreamTransport, str]] = ..., relay_server: _Optional[str] = ..., cert: _Optional[str] = ...) -> None: ...

class CMsgRemoteDeviceProofRequest(_message.Message):
    __slots__ = ("challenge", "request_id", "update_secret")
    CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_SECRET_FIELD_NUMBER: _ClassVar[int]
    challenge: bytes
    request_id: int
    update_secret: bool
    def __init__(self, challenge: _Optional[bytes] = ..., request_id: _Optional[int] = ..., update_secret: bool = ...) -> None: ...

class CMsgRemoteDeviceProofResponse(_message.Message):
    __slots__ = ("response", "request_id", "updated_secret")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_SECRET_FIELD_NUMBER: _ClassVar[int]
    response: bytes
    request_id: int
    updated_secret: bool
    def __init__(self, response: _Optional[bytes] = ..., request_id: _Optional[int] = ..., updated_secret: bool = ...) -> None: ...

class CMsgRemoteDeviceStreamTransportSignal(_message.Message):
    __slots__ = ("token", "payload")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    token: bytes
    payload: bytes
    def __init__(self, token: _Optional[bytes] = ..., payload: _Optional[bytes] = ...) -> None: ...
