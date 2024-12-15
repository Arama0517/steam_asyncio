from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EStreamChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamChannelInvalid: _ClassVar[EStreamChannel]
    k_EStreamChannelDiscovery: _ClassVar[EStreamChannel]
    k_EStreamChannelControl: _ClassVar[EStreamChannel]
    k_EStreamChannelStats: _ClassVar[EStreamChannel]
    k_EStreamChannelDataChannelStart: _ClassVar[EStreamChannel]

class EStreamDiscoveryMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamDiscoveryPingRequest: _ClassVar[EStreamDiscoveryMessage]
    k_EStreamDiscoveryPingResponse: _ClassVar[EStreamDiscoveryMessage]

class EStreamControlMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamControlAuthenticationRequest: _ClassVar[EStreamControlMessage]
    k_EStreamControlAuthenticationResponse: _ClassVar[EStreamControlMessage]
    k_EStreamControlNegotiationInit: _ClassVar[EStreamControlMessage]
    k_EStreamControlNegotiationSetConfig: _ClassVar[EStreamControlMessage]
    k_EStreamControlNegotiationComplete: _ClassVar[EStreamControlMessage]
    k_EStreamControlClientHandshake: _ClassVar[EStreamControlMessage]
    k_EStreamControlServerHandshake: _ClassVar[EStreamControlMessage]
    k_EStreamControlStartNetworkTest: _ClassVar[EStreamControlMessage]
    k_EStreamControlKeepAlive: _ClassVar[EStreamControlMessage]
    k_EStreamControl_LAST_SETUP_MESSAGE: _ClassVar[EStreamControlMessage]
    k_EStreamControlStartAudioData: _ClassVar[EStreamControlMessage]
    k_EStreamControlStopAudioData: _ClassVar[EStreamControlMessage]
    k_EStreamControlStartVideoData: _ClassVar[EStreamControlMessage]
    k_EStreamControlStopVideoData: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputMouseMotion: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputMouseWheel: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputMouseDown: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputMouseUp: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputKeyDown: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputKeyUp: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputGamepadAttached_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputGamepadEvent_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputGamepadDetached_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlShowCursor: _ClassVar[EStreamControlMessage]
    k_EStreamControlHideCursor: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetCursor: _ClassVar[EStreamControlMessage]
    k_EStreamControlGetCursorImage: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetCursorImage: _ClassVar[EStreamControlMessage]
    k_EStreamControlDeleteCursor: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetTargetFramerate: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputLatencyTest: _ClassVar[EStreamControlMessage]
    k_EStreamControlGamepadRumble_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlOverlayEnabled: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputControllerAttached_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputControllerState_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlTriggerHapticPulse_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputControllerDetached_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlVideoDecoderInfo: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetTitle: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetIcon: _ClassVar[EStreamControlMessage]
    k_EStreamControlQuitRequest: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetQoS: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputControllerWirelessPresence_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetGammaRamp: _ClassVar[EStreamControlMessage]
    k_EStreamControlVideoEncoderInfo: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputControllerStateHID_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetTargetBitrate: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetControllerPairingEnabled_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetControllerPairingResult_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlTriggerControllerDisconnect_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetActivity: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetStreamingClientConfig: _ClassVar[EStreamControlMessage]
    k_EStreamControlSystemSuspend: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetControllerSettings_OBSOLETE: _ClassVar[EStreamControlMessage]
    k_EStreamControlVirtualHereRequest: _ClassVar[EStreamControlMessage]
    k_EStreamControlVirtualHereReady: _ClassVar[EStreamControlMessage]
    k_EStreamControlVirtualHereShareDevice: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetSpectatorMode: _ClassVar[EStreamControlMessage]
    k_EStreamControlRemoteHID: _ClassVar[EStreamControlMessage]
    k_EStreamControlStartMicrophoneData: _ClassVar[EStreamControlMessage]
    k_EStreamControlStopMicrophoneData: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputText: _ClassVar[EStreamControlMessage]
    k_EStreamControlTouchConfigActive: _ClassVar[EStreamControlMessage]
    k_EStreamControlGetTouchConfigData: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetTouchConfigData: _ClassVar[EStreamControlMessage]
    k_EStreamControlSaveTouchConfigLayout: _ClassVar[EStreamControlMessage]
    k_EStreamControlTouchActionSetActive: _ClassVar[EStreamControlMessage]
    k_EStreamControlGetTouchIconData: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetTouchIconData: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputTouchFingerDown: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputTouchFingerMotion: _ClassVar[EStreamControlMessage]
    k_EStreamControlInputTouchFingerUp: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetCaptureSize: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetFlashState: _ClassVar[EStreamControlMessage]
    k_EStreamControlPause: _ClassVar[EStreamControlMessage]
    k_EStreamControlResume: _ClassVar[EStreamControlMessage]
    k_EStreamControlEnableHighResCapture: _ClassVar[EStreamControlMessage]
    k_EStreamControlDisableHighResCapture: _ClassVar[EStreamControlMessage]
    k_EStreamControlToggleMagnification: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetCapslock: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetKeymap: _ClassVar[EStreamControlMessage]
    k_EStreamControlStopRequest: _ClassVar[EStreamControlMessage]
    k_EStreamControlTouchActionSetLayerAdded: _ClassVar[EStreamControlMessage]
    k_EStreamControlTouchActionSetLayerRemoved: _ClassVar[EStreamControlMessage]
    k_EStreamControlRemotePlayTogetherGroupUpdate: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetInputTemporarilyDisabled: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetQualityOverride: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetBitrateOverride: _ClassVar[EStreamControlMessage]
    k_EStreamControlShowOnScreenKeyboard: _ClassVar[EStreamControlMessage]
    k_EStreamControlControllerConfigMsg: _ClassVar[EStreamControlMessage]
    k_EStreamControlControllerPersonalizationUpdate: _ClassVar[EStreamControlMessage]
    k_EStreamControlEnableNeptuneData: _ClassVar[EStreamControlMessage]
    k_EStreamControlDisableNeptuneData: _ClassVar[EStreamControlMessage]
    k_EStreamControlStartNeptuneData: _ClassVar[EStreamControlMessage]
    k_EStreamControlStopNeptuneData: _ClassVar[EStreamControlMessage]
    k_EStreamControlPauseControllerInput: _ClassVar[EStreamControlMessage]
    k_EStreamControlResumeControllerInput: _ClassVar[EStreamControlMessage]
    k_EStreamControlVRConnectionReady: _ClassVar[EStreamControlMessage]
    k_EStreamControlSetCursorScale: _ClassVar[EStreamControlMessage]

class EStreamVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamVersionNone: _ClassVar[EStreamVersion]
    k_EStreamVersionCurrent: _ClassVar[EStreamVersion]

class EStreamAudioCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamAudioCodecNone: _ClassVar[EStreamAudioCodec]
    k_EStreamAudioCodecRaw: _ClassVar[EStreamAudioCodec]
    k_EStreamAudioCodecVorbis: _ClassVar[EStreamAudioCodec]
    k_EStreamAudioCodecOpus: _ClassVar[EStreamAudioCodec]
    k_EStreamAudioCodecMP3: _ClassVar[EStreamAudioCodec]
    k_EStreamAudioCodecAAC: _ClassVar[EStreamAudioCodec]

class EStreamVideoCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamVideoCodecNone: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecRaw: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecVP8: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecVP9: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecH264: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecHEVC: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecORBX1: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecORBX2: _ClassVar[EStreamVideoCodec]
    k_EStreamVideoCodecAV1: _ClassVar[EStreamVideoCodec]

class EStreamQualityPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamQualityAutomatic: _ClassVar[EStreamQualityPreference]
    k_EStreamQualityFast: _ClassVar[EStreamQualityPreference]
    k_EStreamQualityBalanced: _ClassVar[EStreamQualityPreference]
    k_EStreamQualityBeautiful: _ClassVar[EStreamQualityPreference]

class EStreamBitrate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamBitrateAutodetect: _ClassVar[EStreamBitrate]
    k_EStreamBitrateUnlimited: _ClassVar[EStreamBitrate]

class EStreamColorspace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamColorspace_Unknown: _ClassVar[EStreamColorspace]
    k_EStreamColorspace_BT601: _ClassVar[EStreamColorspace]
    k_EStreamColorspace_BT601_Full: _ClassVar[EStreamColorspace]
    k_EStreamColorspace_BT709: _ClassVar[EStreamColorspace]
    k_EStreamColorspace_BT709_Full: _ClassVar[EStreamColorspace]
    k_EStreamColorspace_HDR10: _ClassVar[EStreamColorspace]

class EStreamP2PScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamP2PScopeAutomatic: _ClassVar[EStreamP2PScope]
    k_EStreamP2PScopeDisabled: _ClassVar[EStreamP2PScope]
    k_EStreamP2PScopeOnlyMe: _ClassVar[EStreamP2PScope]
    k_EStreamP2PScopeFriends: _ClassVar[EStreamP2PScope]
    k_EStreamP2PScopeEveryone: _ClassVar[EStreamP2PScope]

class EStreamHostPlayAudioPreference(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamHostPlayAudioDefault: _ClassVar[EStreamHostPlayAudioPreference]
    k_EStreamHostPlayAudioAlways: _ClassVar[EStreamHostPlayAudioPreference]

class EStreamingDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamingAudioData: _ClassVar[EStreamingDataType]
    k_EStreamingVideoData: _ClassVar[EStreamingDataType]
    k_EStreamingMicrophoneData: _ClassVar[EStreamingDataType]
    k_EStreamingNeptuneData: _ClassVar[EStreamingDataType]

class EStreamMouseButton(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamMouseButtonLeft: _ClassVar[EStreamMouseButton]
    k_EStreamMouseButtonRight: _ClassVar[EStreamMouseButton]
    k_EStreamMouseButtonMiddle: _ClassVar[EStreamMouseButton]
    k_EStreamMouseButtonX1: _ClassVar[EStreamMouseButton]
    k_EStreamMouseButtonX2: _ClassVar[EStreamMouseButton]
    k_EStreamMouseButtonUnknown: _ClassVar[EStreamMouseButton]

class EStreamMouseWheelDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamMouseWheelUp: _ClassVar[EStreamMouseWheelDirection]
    k_EStreamMouseWheelDown: _ClassVar[EStreamMouseWheelDirection]
    k_EStreamMouseWheelLeft: _ClassVar[EStreamMouseWheelDirection]
    k_EStreamMouseWheelRight: _ClassVar[EStreamMouseWheelDirection]

class EStreamFramerateLimiter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamFramerateSlowCapture: _ClassVar[EStreamFramerateLimiter]
    k_EStreamFramerateSlowConvert: _ClassVar[EStreamFramerateLimiter]
    k_EStreamFramerateSlowEncode: _ClassVar[EStreamFramerateLimiter]
    k_EStreamFramerateSlowNetwork: _ClassVar[EStreamFramerateLimiter]
    k_EStreamFramerateSlowDecode: _ClassVar[EStreamFramerateLimiter]
    k_EStreamFramerateSlowGame: _ClassVar[EStreamFramerateLimiter]
    k_EStreamFramerateSlowDisplay: _ClassVar[EStreamFramerateLimiter]

class EStreamActivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamActivityIdle: _ClassVar[EStreamActivity]
    k_EStreamActivityGame: _ClassVar[EStreamActivity]
    k_EStreamActivityDesktop: _ClassVar[EStreamActivity]
    k_EStreamActivitySecureDesktop: _ClassVar[EStreamActivity]
    k_EStreamActivityMusic: _ClassVar[EStreamActivity]

class EStreamDataMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamDataPacket: _ClassVar[EStreamDataMessage]
    k_EStreamDataLost: _ClassVar[EStreamDataMessage]

class EAudioFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EAudioFormatNone: _ClassVar[EAudioFormat]
    k_EAudioFormat16BitLittleEndian: _ClassVar[EAudioFormat]
    k_EAudioFormatFloat: _ClassVar[EAudioFormat]

class EVideoFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EVideoFormatNone: _ClassVar[EVideoFormat]
    k_EVideoFormatYV12: _ClassVar[EVideoFormat]
    k_EVideoFormatAccel: _ClassVar[EVideoFormat]

class EStreamStatsMessage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamStatsFrameEvents: _ClassVar[EStreamStatsMessage]
    k_EStreamStatsDebugDump: _ClassVar[EStreamStatsMessage]
    k_EStreamStatsLogMessage: _ClassVar[EStreamStatsMessage]
    k_EStreamStatsLogUploadBegin: _ClassVar[EStreamStatsMessage]
    k_EStreamStatsLogUploadData: _ClassVar[EStreamStatsMessage]
    k_EStreamStatsLogUploadComplete: _ClassVar[EStreamStatsMessage]

class EStreamFrameEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamInputEventStart: _ClassVar[EStreamFrameEvent]
    k_EStreamInputEventSend: _ClassVar[EStreamFrameEvent]
    k_EStreamInputEventRecv: _ClassVar[EStreamFrameEvent]
    k_EStreamInputEventQueued: _ClassVar[EStreamFrameEvent]
    k_EStreamInputEventHandled: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventStart: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventCaptureBegin: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventCaptureEnd: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventConvertBegin: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventConvertEnd: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventEncodeBegin: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventEncodeEnd: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventSend: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventRecv: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventDecodeBegin: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventDecodeEnd: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventUploadBegin: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventUploadEnd: _ClassVar[EStreamFrameEvent]
    k_EStreamFrameEventComplete: _ClassVar[EStreamFrameEvent]

class EStreamFrameResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamFrameResultPending: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDisplayed: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDroppedNetworkSlow: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDroppedNetworkLost: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDroppedDecodeSlow: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDroppedDecodeCorrupt: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDroppedLate: _ClassVar[EStreamFrameResult]
    k_EStreamFrameResultDroppedReset: _ClassVar[EStreamFrameResult]

class EFrameAccumulatedStat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EFrameStatFPS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatCaptureDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatConvertDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatEncodeDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatSteamDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatServerDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatNetworkDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatDecodeDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatDisplayDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatClientDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatFrameDurationMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatInputLatencyMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatGameLatencyMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatRoundTripLatencyMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatPingTimeMS: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatServerBitrateKbitPerSec: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatClientBitrateKbitPerSec: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatLinkBandwidthKbitPerSec: _ClassVar[EFrameAccumulatedStat]
    k_EFrameStatPacketLossPercentage: _ClassVar[EFrameAccumulatedStat]

class ELogFileType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ELogFileSystemBoot: _ClassVar[ELogFileType]
    k_ELogFileSystemReset: _ClassVar[ELogFileType]
    k_ELogFileSystemDebug: _ClassVar[ELogFileType]

class EStreamControllerConfigMsg(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EStreamControllerConfigMsg_RequestConfigsForApp: _ClassVar[EStreamControllerConfigMsg]
    k_EStreamControllerConfigMsg_ConfigResponse: _ClassVar[EStreamControllerConfigMsg]
    k_EStreamControllerConfigMsg_PersonalizationResponse: _ClassVar[EStreamControllerConfigMsg]
    k_EStreamControllerConfigMsg_ActiveConfigChange: _ClassVar[EStreamControllerConfigMsg]
    k_EStreamControllerConfigMsg_RequestActiveConfig: _ClassVar[EStreamControllerConfigMsg]
k_EStreamChannelInvalid: EStreamChannel
k_EStreamChannelDiscovery: EStreamChannel
k_EStreamChannelControl: EStreamChannel
k_EStreamChannelStats: EStreamChannel
k_EStreamChannelDataChannelStart: EStreamChannel
k_EStreamDiscoveryPingRequest: EStreamDiscoveryMessage
k_EStreamDiscoveryPingResponse: EStreamDiscoveryMessage
k_EStreamControlAuthenticationRequest: EStreamControlMessage
k_EStreamControlAuthenticationResponse: EStreamControlMessage
k_EStreamControlNegotiationInit: EStreamControlMessage
k_EStreamControlNegotiationSetConfig: EStreamControlMessage
k_EStreamControlNegotiationComplete: EStreamControlMessage
k_EStreamControlClientHandshake: EStreamControlMessage
k_EStreamControlServerHandshake: EStreamControlMessage
k_EStreamControlStartNetworkTest: EStreamControlMessage
k_EStreamControlKeepAlive: EStreamControlMessage
k_EStreamControl_LAST_SETUP_MESSAGE: EStreamControlMessage
k_EStreamControlStartAudioData: EStreamControlMessage
k_EStreamControlStopAudioData: EStreamControlMessage
k_EStreamControlStartVideoData: EStreamControlMessage
k_EStreamControlStopVideoData: EStreamControlMessage
k_EStreamControlInputMouseMotion: EStreamControlMessage
k_EStreamControlInputMouseWheel: EStreamControlMessage
k_EStreamControlInputMouseDown: EStreamControlMessage
k_EStreamControlInputMouseUp: EStreamControlMessage
k_EStreamControlInputKeyDown: EStreamControlMessage
k_EStreamControlInputKeyUp: EStreamControlMessage
k_EStreamControlInputGamepadAttached_OBSOLETE: EStreamControlMessage
k_EStreamControlInputGamepadEvent_OBSOLETE: EStreamControlMessage
k_EStreamControlInputGamepadDetached_OBSOLETE: EStreamControlMessage
k_EStreamControlShowCursor: EStreamControlMessage
k_EStreamControlHideCursor: EStreamControlMessage
k_EStreamControlSetCursor: EStreamControlMessage
k_EStreamControlGetCursorImage: EStreamControlMessage
k_EStreamControlSetCursorImage: EStreamControlMessage
k_EStreamControlDeleteCursor: EStreamControlMessage
k_EStreamControlSetTargetFramerate: EStreamControlMessage
k_EStreamControlInputLatencyTest: EStreamControlMessage
k_EStreamControlGamepadRumble_OBSOLETE: EStreamControlMessage
k_EStreamControlOverlayEnabled: EStreamControlMessage
k_EStreamControlInputControllerAttached_OBSOLETE: EStreamControlMessage
k_EStreamControlInputControllerState_OBSOLETE: EStreamControlMessage
k_EStreamControlTriggerHapticPulse_OBSOLETE: EStreamControlMessage
k_EStreamControlInputControllerDetached_OBSOLETE: EStreamControlMessage
k_EStreamControlVideoDecoderInfo: EStreamControlMessage
k_EStreamControlSetTitle: EStreamControlMessage
k_EStreamControlSetIcon: EStreamControlMessage
k_EStreamControlQuitRequest: EStreamControlMessage
k_EStreamControlSetQoS: EStreamControlMessage
k_EStreamControlInputControllerWirelessPresence_OBSOLETE: EStreamControlMessage
k_EStreamControlSetGammaRamp: EStreamControlMessage
k_EStreamControlVideoEncoderInfo: EStreamControlMessage
k_EStreamControlInputControllerStateHID_OBSOLETE: EStreamControlMessage
k_EStreamControlSetTargetBitrate: EStreamControlMessage
k_EStreamControlSetControllerPairingEnabled_OBSOLETE: EStreamControlMessage
k_EStreamControlSetControllerPairingResult_OBSOLETE: EStreamControlMessage
k_EStreamControlTriggerControllerDisconnect_OBSOLETE: EStreamControlMessage
k_EStreamControlSetActivity: EStreamControlMessage
k_EStreamControlSetStreamingClientConfig: EStreamControlMessage
k_EStreamControlSystemSuspend: EStreamControlMessage
k_EStreamControlSetControllerSettings_OBSOLETE: EStreamControlMessage
k_EStreamControlVirtualHereRequest: EStreamControlMessage
k_EStreamControlVirtualHereReady: EStreamControlMessage
k_EStreamControlVirtualHereShareDevice: EStreamControlMessage
k_EStreamControlSetSpectatorMode: EStreamControlMessage
k_EStreamControlRemoteHID: EStreamControlMessage
k_EStreamControlStartMicrophoneData: EStreamControlMessage
k_EStreamControlStopMicrophoneData: EStreamControlMessage
k_EStreamControlInputText: EStreamControlMessage
k_EStreamControlTouchConfigActive: EStreamControlMessage
k_EStreamControlGetTouchConfigData: EStreamControlMessage
k_EStreamControlSetTouchConfigData: EStreamControlMessage
k_EStreamControlSaveTouchConfigLayout: EStreamControlMessage
k_EStreamControlTouchActionSetActive: EStreamControlMessage
k_EStreamControlGetTouchIconData: EStreamControlMessage
k_EStreamControlSetTouchIconData: EStreamControlMessage
k_EStreamControlInputTouchFingerDown: EStreamControlMessage
k_EStreamControlInputTouchFingerMotion: EStreamControlMessage
k_EStreamControlInputTouchFingerUp: EStreamControlMessage
k_EStreamControlSetCaptureSize: EStreamControlMessage
k_EStreamControlSetFlashState: EStreamControlMessage
k_EStreamControlPause: EStreamControlMessage
k_EStreamControlResume: EStreamControlMessage
k_EStreamControlEnableHighResCapture: EStreamControlMessage
k_EStreamControlDisableHighResCapture: EStreamControlMessage
k_EStreamControlToggleMagnification: EStreamControlMessage
k_EStreamControlSetCapslock: EStreamControlMessage
k_EStreamControlSetKeymap: EStreamControlMessage
k_EStreamControlStopRequest: EStreamControlMessage
k_EStreamControlTouchActionSetLayerAdded: EStreamControlMessage
k_EStreamControlTouchActionSetLayerRemoved: EStreamControlMessage
k_EStreamControlRemotePlayTogetherGroupUpdate: EStreamControlMessage
k_EStreamControlSetInputTemporarilyDisabled: EStreamControlMessage
k_EStreamControlSetQualityOverride: EStreamControlMessage
k_EStreamControlSetBitrateOverride: EStreamControlMessage
k_EStreamControlShowOnScreenKeyboard: EStreamControlMessage
k_EStreamControlControllerConfigMsg: EStreamControlMessage
k_EStreamControlControllerPersonalizationUpdate: EStreamControlMessage
k_EStreamControlEnableNeptuneData: EStreamControlMessage
k_EStreamControlDisableNeptuneData: EStreamControlMessage
k_EStreamControlStartNeptuneData: EStreamControlMessage
k_EStreamControlStopNeptuneData: EStreamControlMessage
k_EStreamControlPauseControllerInput: EStreamControlMessage
k_EStreamControlResumeControllerInput: EStreamControlMessage
k_EStreamControlVRConnectionReady: EStreamControlMessage
k_EStreamControlSetCursorScale: EStreamControlMessage
k_EStreamVersionNone: EStreamVersion
k_EStreamVersionCurrent: EStreamVersion
k_EStreamAudioCodecNone: EStreamAudioCodec
k_EStreamAudioCodecRaw: EStreamAudioCodec
k_EStreamAudioCodecVorbis: EStreamAudioCodec
k_EStreamAudioCodecOpus: EStreamAudioCodec
k_EStreamAudioCodecMP3: EStreamAudioCodec
k_EStreamAudioCodecAAC: EStreamAudioCodec
k_EStreamVideoCodecNone: EStreamVideoCodec
k_EStreamVideoCodecRaw: EStreamVideoCodec
k_EStreamVideoCodecVP8: EStreamVideoCodec
k_EStreamVideoCodecVP9: EStreamVideoCodec
k_EStreamVideoCodecH264: EStreamVideoCodec
k_EStreamVideoCodecHEVC: EStreamVideoCodec
k_EStreamVideoCodecORBX1: EStreamVideoCodec
k_EStreamVideoCodecORBX2: EStreamVideoCodec
k_EStreamVideoCodecAV1: EStreamVideoCodec
k_EStreamQualityAutomatic: EStreamQualityPreference
k_EStreamQualityFast: EStreamQualityPreference
k_EStreamQualityBalanced: EStreamQualityPreference
k_EStreamQualityBeautiful: EStreamQualityPreference
k_EStreamBitrateAutodetect: EStreamBitrate
k_EStreamBitrateUnlimited: EStreamBitrate
k_EStreamColorspace_Unknown: EStreamColorspace
k_EStreamColorspace_BT601: EStreamColorspace
k_EStreamColorspace_BT601_Full: EStreamColorspace
k_EStreamColorspace_BT709: EStreamColorspace
k_EStreamColorspace_BT709_Full: EStreamColorspace
k_EStreamColorspace_HDR10: EStreamColorspace
k_EStreamP2PScopeAutomatic: EStreamP2PScope
k_EStreamP2PScopeDisabled: EStreamP2PScope
k_EStreamP2PScopeOnlyMe: EStreamP2PScope
k_EStreamP2PScopeFriends: EStreamP2PScope
k_EStreamP2PScopeEveryone: EStreamP2PScope
k_EStreamHostPlayAudioDefault: EStreamHostPlayAudioPreference
k_EStreamHostPlayAudioAlways: EStreamHostPlayAudioPreference
k_EStreamingAudioData: EStreamingDataType
k_EStreamingVideoData: EStreamingDataType
k_EStreamingMicrophoneData: EStreamingDataType
k_EStreamingNeptuneData: EStreamingDataType
k_EStreamMouseButtonLeft: EStreamMouseButton
k_EStreamMouseButtonRight: EStreamMouseButton
k_EStreamMouseButtonMiddle: EStreamMouseButton
k_EStreamMouseButtonX1: EStreamMouseButton
k_EStreamMouseButtonX2: EStreamMouseButton
k_EStreamMouseButtonUnknown: EStreamMouseButton
k_EStreamMouseWheelUp: EStreamMouseWheelDirection
k_EStreamMouseWheelDown: EStreamMouseWheelDirection
k_EStreamMouseWheelLeft: EStreamMouseWheelDirection
k_EStreamMouseWheelRight: EStreamMouseWheelDirection
k_EStreamFramerateSlowCapture: EStreamFramerateLimiter
k_EStreamFramerateSlowConvert: EStreamFramerateLimiter
k_EStreamFramerateSlowEncode: EStreamFramerateLimiter
k_EStreamFramerateSlowNetwork: EStreamFramerateLimiter
k_EStreamFramerateSlowDecode: EStreamFramerateLimiter
k_EStreamFramerateSlowGame: EStreamFramerateLimiter
k_EStreamFramerateSlowDisplay: EStreamFramerateLimiter
k_EStreamActivityIdle: EStreamActivity
k_EStreamActivityGame: EStreamActivity
k_EStreamActivityDesktop: EStreamActivity
k_EStreamActivitySecureDesktop: EStreamActivity
k_EStreamActivityMusic: EStreamActivity
k_EStreamDataPacket: EStreamDataMessage
k_EStreamDataLost: EStreamDataMessage
k_EAudioFormatNone: EAudioFormat
k_EAudioFormat16BitLittleEndian: EAudioFormat
k_EAudioFormatFloat: EAudioFormat
k_EVideoFormatNone: EVideoFormat
k_EVideoFormatYV12: EVideoFormat
k_EVideoFormatAccel: EVideoFormat
k_EStreamStatsFrameEvents: EStreamStatsMessage
k_EStreamStatsDebugDump: EStreamStatsMessage
k_EStreamStatsLogMessage: EStreamStatsMessage
k_EStreamStatsLogUploadBegin: EStreamStatsMessage
k_EStreamStatsLogUploadData: EStreamStatsMessage
k_EStreamStatsLogUploadComplete: EStreamStatsMessage
k_EStreamInputEventStart: EStreamFrameEvent
k_EStreamInputEventSend: EStreamFrameEvent
k_EStreamInputEventRecv: EStreamFrameEvent
k_EStreamInputEventQueued: EStreamFrameEvent
k_EStreamInputEventHandled: EStreamFrameEvent
k_EStreamFrameEventStart: EStreamFrameEvent
k_EStreamFrameEventCaptureBegin: EStreamFrameEvent
k_EStreamFrameEventCaptureEnd: EStreamFrameEvent
k_EStreamFrameEventConvertBegin: EStreamFrameEvent
k_EStreamFrameEventConvertEnd: EStreamFrameEvent
k_EStreamFrameEventEncodeBegin: EStreamFrameEvent
k_EStreamFrameEventEncodeEnd: EStreamFrameEvent
k_EStreamFrameEventSend: EStreamFrameEvent
k_EStreamFrameEventRecv: EStreamFrameEvent
k_EStreamFrameEventDecodeBegin: EStreamFrameEvent
k_EStreamFrameEventDecodeEnd: EStreamFrameEvent
k_EStreamFrameEventUploadBegin: EStreamFrameEvent
k_EStreamFrameEventUploadEnd: EStreamFrameEvent
k_EStreamFrameEventComplete: EStreamFrameEvent
k_EStreamFrameResultPending: EStreamFrameResult
k_EStreamFrameResultDisplayed: EStreamFrameResult
k_EStreamFrameResultDroppedNetworkSlow: EStreamFrameResult
k_EStreamFrameResultDroppedNetworkLost: EStreamFrameResult
k_EStreamFrameResultDroppedDecodeSlow: EStreamFrameResult
k_EStreamFrameResultDroppedDecodeCorrupt: EStreamFrameResult
k_EStreamFrameResultDroppedLate: EStreamFrameResult
k_EStreamFrameResultDroppedReset: EStreamFrameResult
k_EFrameStatFPS: EFrameAccumulatedStat
k_EFrameStatCaptureDurationMS: EFrameAccumulatedStat
k_EFrameStatConvertDurationMS: EFrameAccumulatedStat
k_EFrameStatEncodeDurationMS: EFrameAccumulatedStat
k_EFrameStatSteamDurationMS: EFrameAccumulatedStat
k_EFrameStatServerDurationMS: EFrameAccumulatedStat
k_EFrameStatNetworkDurationMS: EFrameAccumulatedStat
k_EFrameStatDecodeDurationMS: EFrameAccumulatedStat
k_EFrameStatDisplayDurationMS: EFrameAccumulatedStat
k_EFrameStatClientDurationMS: EFrameAccumulatedStat
k_EFrameStatFrameDurationMS: EFrameAccumulatedStat
k_EFrameStatInputLatencyMS: EFrameAccumulatedStat
k_EFrameStatGameLatencyMS: EFrameAccumulatedStat
k_EFrameStatRoundTripLatencyMS: EFrameAccumulatedStat
k_EFrameStatPingTimeMS: EFrameAccumulatedStat
k_EFrameStatServerBitrateKbitPerSec: EFrameAccumulatedStat
k_EFrameStatClientBitrateKbitPerSec: EFrameAccumulatedStat
k_EFrameStatLinkBandwidthKbitPerSec: EFrameAccumulatedStat
k_EFrameStatPacketLossPercentage: EFrameAccumulatedStat
k_ELogFileSystemBoot: ELogFileType
k_ELogFileSystemReset: ELogFileType
k_ELogFileSystemDebug: ELogFileType
k_EStreamControllerConfigMsg_RequestConfigsForApp: EStreamControllerConfigMsg
k_EStreamControllerConfigMsg_ConfigResponse: EStreamControllerConfigMsg
k_EStreamControllerConfigMsg_PersonalizationResponse: EStreamControllerConfigMsg
k_EStreamControllerConfigMsg_ActiveConfigChange: EStreamControllerConfigMsg
k_EStreamControllerConfigMsg_RequestActiveConfig: EStreamControllerConfigMsg

class CDiscoveryPingRequest(_message.Message):
    __slots__ = ("sequence", "packet_size_requested")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PACKET_SIZE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    packet_size_requested: int
    def __init__(self, sequence: _Optional[int] = ..., packet_size_requested: _Optional[int] = ...) -> None: ...

class CDiscoveryPingResponse(_message.Message):
    __slots__ = ("sequence", "packet_size_received")
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    PACKET_SIZE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    sequence: int
    packet_size_received: int
    def __init__(self, sequence: _Optional[int] = ..., packet_size_received: _Optional[int] = ...) -> None: ...

class CStreamingClientHandshakeInfo(_message.Message):
    __slots__ = ("network_test",)
    NETWORK_TEST_FIELD_NUMBER: _ClassVar[int]
    network_test: int
    def __init__(self, network_test: _Optional[int] = ...) -> None: ...

class CClientHandshakeMsg(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: CStreamingClientHandshakeInfo
    def __init__(self, info: _Optional[_Union[CStreamingClientHandshakeInfo, _Mapping]] = ...) -> None: ...

class CStreamingServerHandshakeInfo(_message.Message):
    __slots__ = ("mtu",)
    MTU_FIELD_NUMBER: _ClassVar[int]
    mtu: int
    def __init__(self, mtu: _Optional[int] = ...) -> None: ...

class CServerHandshakeMsg(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: CStreamingServerHandshakeInfo
    def __init__(self, info: _Optional[_Union[CStreamingServerHandshakeInfo, _Mapping]] = ...) -> None: ...

class CAuthenticationRequestMsg(_message.Message):
    __slots__ = ("token", "version", "steamid")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    token: bytes
    version: EStreamVersion
    steamid: int
    def __init__(self, token: _Optional[bytes] = ..., version: _Optional[_Union[EStreamVersion, str]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CAuthenticationResponseMsg(_message.Message):
    __slots__ = ("result", "version")
    class AuthenticationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCEEDED: _ClassVar[CAuthenticationResponseMsg.AuthenticationResult]
        FAILED: _ClassVar[CAuthenticationResponseMsg.AuthenticationResult]
    SUCCEEDED: CAuthenticationResponseMsg.AuthenticationResult
    FAILED: CAuthenticationResponseMsg.AuthenticationResult
    RESULT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    result: CAuthenticationResponseMsg.AuthenticationResult
    version: EStreamVersion
    def __init__(self, result: _Optional[_Union[CAuthenticationResponseMsg.AuthenticationResult, str]] = ..., version: _Optional[_Union[EStreamVersion, str]] = ...) -> None: ...

class CKeepAliveMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStartNetworkTestMsg(_message.Message):
    __slots__ = ("frames", "framerate", "bitrate_kbps", "burst_bitrate_kbps", "bandwidth_test")
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    BURST_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_TEST_FIELD_NUMBER: _ClassVar[int]
    frames: int
    framerate: int
    bitrate_kbps: int
    burst_bitrate_kbps: int
    bandwidth_test: bool
    def __init__(self, frames: _Optional[int] = ..., framerate: _Optional[int] = ..., bitrate_kbps: _Optional[int] = ..., burst_bitrate_kbps: _Optional[int] = ..., bandwidth_test: bool = ...) -> None: ...

class CStreamVideoMode(_message.Message):
    __slots__ = ("width", "height", "refresh_rate", "refresh_rate_numerator", "refresh_rate_denominator")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RATE_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RATE_NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    REFRESH_RATE_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    refresh_rate: int
    refresh_rate_numerator: int
    refresh_rate_denominator: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., refresh_rate: _Optional[int] = ..., refresh_rate_numerator: _Optional[int] = ..., refresh_rate_denominator: _Optional[int] = ...) -> None: ...

class CStreamVideoLimit(_message.Message):
    __slots__ = ("codec", "mode", "bitrate_kbps", "burst_bitrate_kbps")
    CODEC_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    BURST_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    codec: EStreamVideoCodec
    mode: CStreamVideoMode
    bitrate_kbps: int
    burst_bitrate_kbps: int
    def __init__(self, codec: _Optional[_Union[EStreamVideoCodec, str]] = ..., mode: _Optional[_Union[CStreamVideoMode, _Mapping]] = ..., bitrate_kbps: _Optional[int] = ..., burst_bitrate_kbps: _Optional[int] = ...) -> None: ...

class CStreamingClientCaps(_message.Message):
    __slots__ = ("system_info", "system_can_suspend", "maximum_decode_bitrate_kbps", "maximum_burst_bitrate_kbps", "supports_video_hevc_OBSOLETE", "disable_steam_store", "disable_client_cursor", "disable_intel_hardware_encoding", "disable_amd_hardware_encoding", "disable_nvidia_hardware_encoding", "form_factor", "has_on_screen_keyboard", "supported_colorspaces", "supported_audio_codecs", "supported_video_codecs")
    SYSTEM_INFO_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CAN_SUSPEND_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_DECODE_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_BURST_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_VIDEO_HEVC_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STEAM_STORE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CLIENT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    DISABLE_INTEL_HARDWARE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AMD_HARDWARE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    DISABLE_NVIDIA_HARDWARE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    FORM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    HAS_ON_SCREEN_KEYBOARD_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_COLORSPACES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_AUDIO_CODECS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VIDEO_CODECS_FIELD_NUMBER: _ClassVar[int]
    system_info: str
    system_can_suspend: bool
    maximum_decode_bitrate_kbps: int
    maximum_burst_bitrate_kbps: int
    supports_video_hevc_OBSOLETE: bool
    disable_steam_store: bool
    disable_client_cursor: bool
    disable_intel_hardware_encoding: bool
    disable_amd_hardware_encoding: bool
    disable_nvidia_hardware_encoding: bool
    form_factor: int
    has_on_screen_keyboard: bool
    supported_colorspaces: _containers.RepeatedScalarFieldContainer[EStreamColorspace]
    supported_audio_codecs: _containers.RepeatedScalarFieldContainer[EStreamAudioCodec]
    supported_video_codecs: _containers.RepeatedScalarFieldContainer[EStreamVideoCodec]
    def __init__(self, system_info: _Optional[str] = ..., system_can_suspend: bool = ..., maximum_decode_bitrate_kbps: _Optional[int] = ..., maximum_burst_bitrate_kbps: _Optional[int] = ..., supports_video_hevc_OBSOLETE: bool = ..., disable_steam_store: bool = ..., disable_client_cursor: bool = ..., disable_intel_hardware_encoding: bool = ..., disable_amd_hardware_encoding: bool = ..., disable_nvidia_hardware_encoding: bool = ..., form_factor: _Optional[int] = ..., has_on_screen_keyboard: bool = ..., supported_colorspaces: _Optional[_Iterable[_Union[EStreamColorspace, str]]] = ..., supported_audio_codecs: _Optional[_Iterable[_Union[EStreamAudioCodec, str]]] = ..., supported_video_codecs: _Optional[_Iterable[_Union[EStreamVideoCodec, str]]] = ...) -> None: ...

class CStreamingClientConfig(_message.Message):
    __slots__ = ("quality", "desired_resolution_x", "desired_resolution_y", "desired_framerate_numerator", "desired_framerate_denominator", "desired_bitrate_kbps", "enable_hardware_decoding", "enable_performance_overlay", "enable_video_streaming", "enable_audio_streaming", "enable_input_streaming", "audio_channels", "enable_video_hevc", "enable_performance_icons", "enable_microphone_streaming", "controller_overlay_hotkey", "enable_touch_controller_OBSOLETE", "p2p_scope", "enable_audio_uncompressed", "display_limit", "quality_limit", "runtime_limit", "decoder_limit", "enable_unreliable_fec", "enable_video_av1")
    QUALITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RESOLUTION_X_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RESOLUTION_Y_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FRAMERATE_NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    DESIRED_FRAMERATE_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_DECODING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PERFORMANCE_OVERLAY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VIDEO_STREAMING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIO_STREAMING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INPUT_STREAMING_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VIDEO_HEVC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_PERFORMANCE_ICONS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MICROPHONE_STREAMING_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_OVERLAY_HOTKEY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TOUCH_CONTROLLER_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    P2P_SCOPE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIO_UNCOMPRESSED_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    QUALITY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DECODER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_UNRELIABLE_FEC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VIDEO_AV1_FIELD_NUMBER: _ClassVar[int]
    quality: EStreamQualityPreference
    desired_resolution_x: int
    desired_resolution_y: int
    desired_framerate_numerator: int
    desired_framerate_denominator: int
    desired_bitrate_kbps: int
    enable_hardware_decoding: bool
    enable_performance_overlay: bool
    enable_video_streaming: bool
    enable_audio_streaming: bool
    enable_input_streaming: bool
    audio_channels: int
    enable_video_hevc: bool
    enable_performance_icons: bool
    enable_microphone_streaming: bool
    controller_overlay_hotkey: str
    enable_touch_controller_OBSOLETE: bool
    p2p_scope: EStreamP2PScope
    enable_audio_uncompressed: bool
    display_limit: CStreamVideoLimit
    quality_limit: CStreamVideoLimit
    runtime_limit: CStreamVideoLimit
    decoder_limit: _containers.RepeatedCompositeFieldContainer[CStreamVideoLimit]
    enable_unreliable_fec: bool
    enable_video_av1: bool
    def __init__(self, quality: _Optional[_Union[EStreamQualityPreference, str]] = ..., desired_resolution_x: _Optional[int] = ..., desired_resolution_y: _Optional[int] = ..., desired_framerate_numerator: _Optional[int] = ..., desired_framerate_denominator: _Optional[int] = ..., desired_bitrate_kbps: _Optional[int] = ..., enable_hardware_decoding: bool = ..., enable_performance_overlay: bool = ..., enable_video_streaming: bool = ..., enable_audio_streaming: bool = ..., enable_input_streaming: bool = ..., audio_channels: _Optional[int] = ..., enable_video_hevc: bool = ..., enable_performance_icons: bool = ..., enable_microphone_streaming: bool = ..., controller_overlay_hotkey: _Optional[str] = ..., enable_touch_controller_OBSOLETE: bool = ..., p2p_scope: _Optional[_Union[EStreamP2PScope, str]] = ..., enable_audio_uncompressed: bool = ..., display_limit: _Optional[_Union[CStreamVideoLimit, _Mapping]] = ..., quality_limit: _Optional[_Union[CStreamVideoLimit, _Mapping]] = ..., runtime_limit: _Optional[_Union[CStreamVideoLimit, _Mapping]] = ..., decoder_limit: _Optional[_Iterable[_Union[CStreamVideoLimit, _Mapping]]] = ..., enable_unreliable_fec: bool = ..., enable_video_av1: bool = ...) -> None: ...

class CStreamingServerConfig(_message.Message):
    __slots__ = ("change_desktop_resolution", "dynamically_adjust_resolution_OBSOLETE", "enable_capture_nvfbc", "enable_hardware_encoding_nvidia_OBSOLETE", "enable_hardware_encoding_amd_OBSOLETE", "enable_hardware_encoding_intel_OBSOLETE", "software_encoding_threads", "enable_traffic_priority", "host_play_audio", "enable_hardware_encoding")
    CHANGE_DESKTOP_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    DYNAMICALLY_ADJUST_RESOLUTION_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CAPTURE_NVFBC_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_ENCODING_NVIDIA_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_ENCODING_AMD_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_ENCODING_INTEL_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    SOFTWARE_ENCODING_THREADS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TRAFFIC_PRIORITY_FIELD_NUMBER: _ClassVar[int]
    HOST_PLAY_AUDIO_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HARDWARE_ENCODING_FIELD_NUMBER: _ClassVar[int]
    change_desktop_resolution: bool
    dynamically_adjust_resolution_OBSOLETE: bool
    enable_capture_nvfbc: bool
    enable_hardware_encoding_nvidia_OBSOLETE: bool
    enable_hardware_encoding_amd_OBSOLETE: bool
    enable_hardware_encoding_intel_OBSOLETE: bool
    software_encoding_threads: int
    enable_traffic_priority: bool
    host_play_audio: EStreamHostPlayAudioPreference
    enable_hardware_encoding: bool
    def __init__(self, change_desktop_resolution: bool = ..., dynamically_adjust_resolution_OBSOLETE: bool = ..., enable_capture_nvfbc: bool = ..., enable_hardware_encoding_nvidia_OBSOLETE: bool = ..., enable_hardware_encoding_amd_OBSOLETE: bool = ..., enable_hardware_encoding_intel_OBSOLETE: bool = ..., software_encoding_threads: _Optional[int] = ..., enable_traffic_priority: bool = ..., host_play_audio: _Optional[_Union[EStreamHostPlayAudioPreference, str]] = ..., enable_hardware_encoding: bool = ...) -> None: ...

class CNegotiatedConfig(_message.Message):
    __slots__ = ("reliable_data", "selected_audio_codec", "selected_video_codec", "available_video_modes_OBSOLETE", "enable_remote_hid", "enable_touch_input", "disable_client_cursor")
    RELIABLE_DATA_FIELD_NUMBER: _ClassVar[int]
    SELECTED_AUDIO_CODEC_FIELD_NUMBER: _ClassVar[int]
    SELECTED_VIDEO_CODEC_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_VIDEO_MODES_OBSOLETE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_REMOTE_HID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TOUCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CLIENT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    reliable_data: bool
    selected_audio_codec: EStreamAudioCodec
    selected_video_codec: EStreamVideoCodec
    available_video_modes_OBSOLETE: _containers.RepeatedCompositeFieldContainer[CStreamVideoMode]
    enable_remote_hid: bool
    enable_touch_input: bool
    disable_client_cursor: bool
    def __init__(self, reliable_data: bool = ..., selected_audio_codec: _Optional[_Union[EStreamAudioCodec, str]] = ..., selected_video_codec: _Optional[_Union[EStreamVideoCodec, str]] = ..., available_video_modes_OBSOLETE: _Optional[_Iterable[_Union[CStreamVideoMode, _Mapping]]] = ..., enable_remote_hid: bool = ..., enable_touch_input: bool = ..., disable_client_cursor: bool = ...) -> None: ...

class CNegotiationInitMsg(_message.Message):
    __slots__ = ("reliable_data", "supported_audio_codecs", "supported_video_codecs", "supports_remote_hid", "supports_touch_input")
    RELIABLE_DATA_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_AUDIO_CODECS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VIDEO_CODECS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_REMOTE_HID_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_TOUCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    reliable_data: bool
    supported_audio_codecs: _containers.RepeatedScalarFieldContainer[EStreamAudioCodec]
    supported_video_codecs: _containers.RepeatedScalarFieldContainer[EStreamVideoCodec]
    supports_remote_hid: bool
    supports_touch_input: bool
    def __init__(self, reliable_data: bool = ..., supported_audio_codecs: _Optional[_Iterable[_Union[EStreamAudioCodec, str]]] = ..., supported_video_codecs: _Optional[_Iterable[_Union[EStreamVideoCodec, str]]] = ..., supports_remote_hid: bool = ..., supports_touch_input: bool = ...) -> None: ...

class CNegotiationSetConfigMsg(_message.Message):
    __slots__ = ("config", "streaming_client_config", "streaming_client_caps")
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    STREAMING_CLIENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STREAMING_CLIENT_CAPS_FIELD_NUMBER: _ClassVar[int]
    config: CNegotiatedConfig
    streaming_client_config: CStreamingClientConfig
    streaming_client_caps: CStreamingClientCaps
    def __init__(self, config: _Optional[_Union[CNegotiatedConfig, _Mapping]] = ..., streaming_client_config: _Optional[_Union[CStreamingClientConfig, _Mapping]] = ..., streaming_client_caps: _Optional[_Union[CStreamingClientCaps, _Mapping]] = ...) -> None: ...

class CNegotiationCompleteMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStartAudioDataMsg(_message.Message):
    __slots__ = ("channel", "codec", "codec_data", "frequency", "channels")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    CODEC_DATA_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channel: int
    codec: EStreamAudioCodec
    codec_data: bytes
    frequency: int
    channels: int
    def __init__(self, channel: _Optional[int] = ..., codec: _Optional[_Union[EStreamAudioCodec, str]] = ..., codec_data: _Optional[bytes] = ..., frequency: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class CStopAudioDataMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStartVideoDataMsg(_message.Message):
    __slots__ = ("channel", "codec", "codec_data", "width", "height")
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    CODEC_DATA_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    channel: int
    codec: EStreamVideoCodec
    codec_data: bytes
    width: int
    height: int
    def __init__(self, channel: _Optional[int] = ..., codec: _Optional[_Union[EStreamVideoCodec, str]] = ..., codec_data: _Optional[bytes] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class CStopVideoDataMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CStartNeptuneDataMsg(_message.Message):
    __slots__ = ("channel",)
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    channel: int
    def __init__(self, channel: _Optional[int] = ...) -> None: ...

class CStopNeptuneDataMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CRecordedInput(_message.Message):
    __slots__ = ("type", "timestamp", "finger_down", "finger_motion", "finger_up", "mouse_motion", "mouse_wheel", "mouse_down", "mouse_up", "key_down", "key_up", "text", "hid")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FINGER_DOWN_FIELD_NUMBER: _ClassVar[int]
    FINGER_MOTION_FIELD_NUMBER: _ClassVar[int]
    FINGER_UP_FIELD_NUMBER: _ClassVar[int]
    MOUSE_MOTION_FIELD_NUMBER: _ClassVar[int]
    MOUSE_WHEEL_FIELD_NUMBER: _ClassVar[int]
    MOUSE_DOWN_FIELD_NUMBER: _ClassVar[int]
    MOUSE_UP_FIELD_NUMBER: _ClassVar[int]
    KEY_DOWN_FIELD_NUMBER: _ClassVar[int]
    KEY_UP_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    type: EStreamControlMessage
    timestamp: int
    finger_down: CInputTouchFingerDownMsg
    finger_motion: CInputTouchFingerMotionMsg
    finger_up: CInputTouchFingerUpMsg
    mouse_motion: CInputMouseMotionMsg
    mouse_wheel: CInputMouseWheelMsg
    mouse_down: CInputMouseDownMsg
    mouse_up: CInputMouseUpMsg
    key_down: CInputKeyDownMsg
    key_up: CInputKeyUpMsg
    text: CInputTextMsg
    hid: CRemoteHIDMsg
    def __init__(self, type: _Optional[_Union[EStreamControlMessage, str]] = ..., timestamp: _Optional[int] = ..., finger_down: _Optional[_Union[CInputTouchFingerDownMsg, _Mapping]] = ..., finger_motion: _Optional[_Union[CInputTouchFingerMotionMsg, _Mapping]] = ..., finger_up: _Optional[_Union[CInputTouchFingerUpMsg, _Mapping]] = ..., mouse_motion: _Optional[_Union[CInputMouseMotionMsg, _Mapping]] = ..., mouse_wheel: _Optional[_Union[CInputMouseWheelMsg, _Mapping]] = ..., mouse_down: _Optional[_Union[CInputMouseDownMsg, _Mapping]] = ..., mouse_up: _Optional[_Union[CInputMouseUpMsg, _Mapping]] = ..., key_down: _Optional[_Union[CInputKeyDownMsg, _Mapping]] = ..., key_up: _Optional[_Union[CInputKeyUpMsg, _Mapping]] = ..., text: _Optional[_Union[CInputTextMsg, _Mapping]] = ..., hid: _Optional[_Union[CRemoteHIDMsg, _Mapping]] = ...) -> None: ...

class CRecordedInputStream(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CRecordedInput]
    def __init__(self, entries: _Optional[_Iterable[_Union[CRecordedInput, _Mapping]]] = ...) -> None: ...

class CInputLatencyTestMsg(_message.Message):
    __slots__ = ("input_mark", "color")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    color: int
    def __init__(self, input_mark: _Optional[int] = ..., color: _Optional[int] = ...) -> None: ...

class CInputTouchFingerDownMsg(_message.Message):
    __slots__ = ("input_mark", "fingerid", "x_normalized", "y_normalized")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    FINGERID_FIELD_NUMBER: _ClassVar[int]
    X_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    Y_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    fingerid: int
    x_normalized: float
    y_normalized: float
    def __init__(self, input_mark: _Optional[int] = ..., fingerid: _Optional[int] = ..., x_normalized: _Optional[float] = ..., y_normalized: _Optional[float] = ...) -> None: ...

class CInputTouchFingerMotionMsg(_message.Message):
    __slots__ = ("input_mark", "fingerid", "x_normalized", "y_normalized")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    FINGERID_FIELD_NUMBER: _ClassVar[int]
    X_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    Y_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    fingerid: int
    x_normalized: float
    y_normalized: float
    def __init__(self, input_mark: _Optional[int] = ..., fingerid: _Optional[int] = ..., x_normalized: _Optional[float] = ..., y_normalized: _Optional[float] = ...) -> None: ...

class CInputTouchFingerUpMsg(_message.Message):
    __slots__ = ("input_mark", "fingerid", "x_normalized", "y_normalized")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    FINGERID_FIELD_NUMBER: _ClassVar[int]
    X_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    Y_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    fingerid: int
    x_normalized: float
    y_normalized: float
    def __init__(self, input_mark: _Optional[int] = ..., fingerid: _Optional[int] = ..., x_normalized: _Optional[float] = ..., y_normalized: _Optional[float] = ...) -> None: ...

class CInputMouseMotionMsg(_message.Message):
    __slots__ = ("input_mark", "x_normalized", "y_normalized", "dx", "dy")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    X_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    Y_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    DX_FIELD_NUMBER: _ClassVar[int]
    DY_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    x_normalized: float
    y_normalized: float
    dx: int
    dy: int
    def __init__(self, input_mark: _Optional[int] = ..., x_normalized: _Optional[float] = ..., y_normalized: _Optional[float] = ..., dx: _Optional[int] = ..., dy: _Optional[int] = ...) -> None: ...

class CInputMouseWheelMsg(_message.Message):
    __slots__ = ("input_mark", "direction", "amount")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    direction: EStreamMouseWheelDirection
    amount: float
    def __init__(self, input_mark: _Optional[int] = ..., direction: _Optional[_Union[EStreamMouseWheelDirection, str]] = ..., amount: _Optional[float] = ...) -> None: ...

class CInputMouseDownMsg(_message.Message):
    __slots__ = ("input_mark", "button")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    button: EStreamMouseButton
    def __init__(self, input_mark: _Optional[int] = ..., button: _Optional[_Union[EStreamMouseButton, str]] = ...) -> None: ...

class CInputMouseUpMsg(_message.Message):
    __slots__ = ("input_mark", "button")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    button: EStreamMouseButton
    def __init__(self, input_mark: _Optional[int] = ..., button: _Optional[_Union[EStreamMouseButton, str]] = ...) -> None: ...

class CInputKeyDownMsg(_message.Message):
    __slots__ = ("input_mark", "scancode", "modifiers", "keycode")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    SCANCODE_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    KEYCODE_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    scancode: int
    modifiers: int
    keycode: int
    def __init__(self, input_mark: _Optional[int] = ..., scancode: _Optional[int] = ..., modifiers: _Optional[int] = ..., keycode: _Optional[int] = ...) -> None: ...

class CInputKeyUpMsg(_message.Message):
    __slots__ = ("input_mark", "scancode", "modifiers", "keycode")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    SCANCODE_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    KEYCODE_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    scancode: int
    modifiers: int
    keycode: int
    def __init__(self, input_mark: _Optional[int] = ..., scancode: _Optional[int] = ..., modifiers: _Optional[int] = ..., keycode: _Optional[int] = ...) -> None: ...

class CInputTextMsg(_message.Message):
    __slots__ = ("input_mark", "text_utf8")
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    TEXT_UTF8_FIELD_NUMBER: _ClassVar[int]
    input_mark: int
    text_utf8: str
    def __init__(self, input_mark: _Optional[int] = ..., text_utf8: _Optional[str] = ...) -> None: ...

class CSetTitleMsg(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class CSetCaptureSizeMsg(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class CSetIconMsg(_message.Message):
    __slots__ = ("width", "height", "image")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    image: bytes
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., image: _Optional[bytes] = ...) -> None: ...

class CSetFlashStateMsg(_message.Message):
    __slots__ = ("flags", "count", "timeout_ms")
    FLAGS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    flags: int
    count: int
    timeout_ms: int
    def __init__(self, flags: _Optional[int] = ..., count: _Optional[int] = ..., timeout_ms: _Optional[int] = ...) -> None: ...

class CShowCursorMsg(_message.Message):
    __slots__ = ("x_normalized", "y_normalized")
    X_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    Y_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    x_normalized: float
    y_normalized: float
    def __init__(self, x_normalized: _Optional[float] = ..., y_normalized: _Optional[float] = ...) -> None: ...

class CHideCursorMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSetCursorMsg(_message.Message):
    __slots__ = ("cursor_id",)
    CURSOR_ID_FIELD_NUMBER: _ClassVar[int]
    cursor_id: int
    def __init__(self, cursor_id: _Optional[int] = ...) -> None: ...

class CGetCursorImageMsg(_message.Message):
    __slots__ = ("cursor_id",)
    CURSOR_ID_FIELD_NUMBER: _ClassVar[int]
    cursor_id: int
    def __init__(self, cursor_id: _Optional[int] = ...) -> None: ...

class CSetCursorImageMsg(_message.Message):
    __slots__ = ("cursor_id", "width", "height", "hot_x", "hot_y", "image")
    CURSOR_ID_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    HOT_X_FIELD_NUMBER: _ClassVar[int]
    HOT_Y_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    cursor_id: int
    width: int
    height: int
    hot_x: int
    hot_y: int
    image: bytes
    def __init__(self, cursor_id: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., hot_x: _Optional[int] = ..., hot_y: _Optional[int] = ..., image: _Optional[bytes] = ...) -> None: ...

class CSetCursorScaleMsg(_message.Message):
    __slots__ = ("scale",)
    SCALE_FIELD_NUMBER: _ClassVar[int]
    scale: float
    def __init__(self, scale: _Optional[float] = ...) -> None: ...

class CVideoDecoderInfoMsg(_message.Message):
    __slots__ = ("info", "threads")
    INFO_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    info: str
    threads: int
    def __init__(self, info: _Optional[str] = ..., threads: _Optional[int] = ...) -> None: ...

class CVideoEncoderInfoMsg(_message.Message):
    __slots__ = ("info",)
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: str
    def __init__(self, info: _Optional[str] = ...) -> None: ...

class CPauseMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CResumeMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CEnableHighResCaptureMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDisableHighResCaptureMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CEnableNeptuneDataMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDisableNeptuneDataMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CPauseControllerInputMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CResumeControllerInputMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CToggleMagnificationMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CSetCapslockMsg(_message.Message):
    __slots__ = ("pressed",)
    PRESSED_FIELD_NUMBER: _ClassVar[int]
    pressed: bool
    def __init__(self, pressed: bool = ...) -> None: ...

class CStreamingKeymapEntry(_message.Message):
    __slots__ = ("scancode", "normal_keycode", "shift_keycode", "capslock_keycode", "shift_capslock_keycode", "altgr_keycode", "altgr_shift_keycode", "altgr_capslock_keycode", "altgr_shift_capslock_keycode")
    SCANCODE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    CAPSLOCK_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_CAPSLOCK_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    ALTGR_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    ALTGR_SHIFT_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    ALTGR_CAPSLOCK_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    ALTGR_SHIFT_CAPSLOCK_KEYCODE_FIELD_NUMBER: _ClassVar[int]
    scancode: int
    normal_keycode: int
    shift_keycode: int
    capslock_keycode: int
    shift_capslock_keycode: int
    altgr_keycode: int
    altgr_shift_keycode: int
    altgr_capslock_keycode: int
    altgr_shift_capslock_keycode: int
    def __init__(self, scancode: _Optional[int] = ..., normal_keycode: _Optional[int] = ..., shift_keycode: _Optional[int] = ..., capslock_keycode: _Optional[int] = ..., shift_capslock_keycode: _Optional[int] = ..., altgr_keycode: _Optional[int] = ..., altgr_shift_keycode: _Optional[int] = ..., altgr_capslock_keycode: _Optional[int] = ..., altgr_shift_capslock_keycode: _Optional[int] = ...) -> None: ...

class CStreamingKeymap(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CStreamingKeymapEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CStreamingKeymapEntry, _Mapping]]] = ...) -> None: ...

class CSetKeymapMsg(_message.Message):
    __slots__ = ("keymap",)
    KEYMAP_FIELD_NUMBER: _ClassVar[int]
    keymap: CStreamingKeymap
    def __init__(self, keymap: _Optional[_Union[CStreamingKeymap, _Mapping]] = ...) -> None: ...

class CStopRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CQuitRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CDeleteCursorMsg(_message.Message):
    __slots__ = ("cursor_id",)
    CURSOR_ID_FIELD_NUMBER: _ClassVar[int]
    cursor_id: int
    def __init__(self, cursor_id: _Optional[int] = ...) -> None: ...

class CSetStreamingClientConfig(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: CStreamingClientConfig
    def __init__(self, config: _Optional[_Union[CStreamingClientConfig, _Mapping]] = ...) -> None: ...

class CSetQoSMsg(_message.Message):
    __slots__ = ("use_qos",)
    USE_QOS_FIELD_NUMBER: _ClassVar[int]
    use_qos: bool
    def __init__(self, use_qos: bool = ...) -> None: ...

class CSetTargetFramerateMsg(_message.Message):
    __slots__ = ("framerate", "reasons", "framerate_numerator", "framerate_denominator")
    FRAMERATE_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    FRAMERATE_NUMERATOR_FIELD_NUMBER: _ClassVar[int]
    FRAMERATE_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    framerate: int
    reasons: int
    framerate_numerator: int
    framerate_denominator: int
    def __init__(self, framerate: _Optional[int] = ..., reasons: _Optional[int] = ..., framerate_numerator: _Optional[int] = ..., framerate_denominator: _Optional[int] = ...) -> None: ...

class CSetTargetBitrateMsg(_message.Message):
    __slots__ = ("bitrate",)
    BITRATE_FIELD_NUMBER: _ClassVar[int]
    bitrate: int
    def __init__(self, bitrate: _Optional[int] = ...) -> None: ...

class COverlayEnabledMsg(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CSetGammaRampMsg(_message.Message):
    __slots__ = ("gamma_ramp",)
    GAMMA_RAMP_FIELD_NUMBER: _ClassVar[int]
    gamma_ramp: bytes
    def __init__(self, gamma_ramp: _Optional[bytes] = ...) -> None: ...

class CSetActivityMsg(_message.Message):
    __slots__ = ("activity", "appid", "gameid", "game_name")
    ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    GAME_NAME_FIELD_NUMBER: _ClassVar[int]
    activity: EStreamActivity
    appid: int
    gameid: int
    game_name: str
    def __init__(self, activity: _Optional[_Union[EStreamActivity, str]] = ..., appid: _Optional[int] = ..., gameid: _Optional[int] = ..., game_name: _Optional[str] = ...) -> None: ...

class CSystemSuspendMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CVirtualHereRequestMsg(_message.Message):
    __slots__ = ("hostname",)
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    def __init__(self, hostname: _Optional[str] = ...) -> None: ...

class CVirtualHereReadyMsg(_message.Message):
    __slots__ = ("licensed_device_count",)
    LICENSED_DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    licensed_device_count: int
    def __init__(self, licensed_device_count: _Optional[int] = ...) -> None: ...

class CVirtualHereShareDeviceMsg(_message.Message):
    __slots__ = ("device_address",)
    DEVICE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    device_address: str
    def __init__(self, device_address: _Optional[str] = ...) -> None: ...

class CSetSpectatorModeMsg(_message.Message):
    __slots__ = ("enabled",)
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    def __init__(self, enabled: bool = ...) -> None: ...

class CRemoteHIDMsg(_message.Message):
    __slots__ = ("data", "active_input")
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_INPUT_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    active_input: bool
    def __init__(self, data: _Optional[bytes] = ..., active_input: bool = ...) -> None: ...

class CTouchConfigActiveMsg(_message.Message):
    __slots__ = ("appid", "revision", "creator")
    APPID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    appid: int
    revision: int
    creator: int
    def __init__(self, appid: _Optional[int] = ..., revision: _Optional[int] = ..., creator: _Optional[int] = ...) -> None: ...

class CGetTouchConfigDataMsg(_message.Message):
    __slots__ = ("appid",)
    APPID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    def __init__(self, appid: _Optional[int] = ...) -> None: ...

class CSetTouchConfigDataMsg(_message.Message):
    __slots__ = ("appid", "revision", "data", "layout", "creator")
    APPID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    appid: int
    revision: int
    data: bytes
    layout: bytes
    creator: int
    def __init__(self, appid: _Optional[int] = ..., revision: _Optional[int] = ..., data: _Optional[bytes] = ..., layout: _Optional[bytes] = ..., creator: _Optional[int] = ...) -> None: ...

class CSaveTouchConfigLayoutMsg(_message.Message):
    __slots__ = ("appid", "layout")
    APPID_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    layout: bytes
    def __init__(self, appid: _Optional[int] = ..., layout: _Optional[bytes] = ...) -> None: ...

class CTouchActionSetActiveMsg(_message.Message):
    __slots__ = ("appid", "actionset_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACTIONSET_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    actionset_id: int
    def __init__(self, appid: _Optional[int] = ..., actionset_id: _Optional[int] = ...) -> None: ...

class CTouchActionSetLayerAddedMsg(_message.Message):
    __slots__ = ("appid", "actionset_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACTIONSET_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    actionset_id: int
    def __init__(self, appid: _Optional[int] = ..., actionset_id: _Optional[int] = ...) -> None: ...

class CTouchActionSetLayerRemovedMsg(_message.Message):
    __slots__ = ("appid", "actionset_id")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACTIONSET_ID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    actionset_id: int
    def __init__(self, appid: _Optional[int] = ..., actionset_id: _Optional[int] = ...) -> None: ...

class CGetTouchIconDataMsg(_message.Message):
    __slots__ = ("appid", "icon")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    appid: int
    icon: str
    def __init__(self, appid: _Optional[int] = ..., icon: _Optional[str] = ...) -> None: ...

class CSetTouchIconDataMsg(_message.Message):
    __slots__ = ("appid", "icon", "data")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    appid: int
    icon: str
    data: bytes
    def __init__(self, appid: _Optional[int] = ..., icon: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class CRemotePlayTogetherGroupUpdateMsg(_message.Message):
    __slots__ = ("players", "player_index", "miniprofile_location", "game_name", "avatar_location", "direct_input")
    class Player(_message.Message):
        __slots__ = ("accountid", "guestid", "keyboard_enabled", "mouse_enabled", "controller_enabled", "controller_slots", "avatar_hash")
        ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
        GUESTID_FIELD_NUMBER: _ClassVar[int]
        KEYBOARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MOUSE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CONTROLLER_SLOTS_FIELD_NUMBER: _ClassVar[int]
        AVATAR_HASH_FIELD_NUMBER: _ClassVar[int]
        accountid: int
        guestid: int
        keyboard_enabled: bool
        mouse_enabled: bool
        controller_enabled: bool
        controller_slots: _containers.RepeatedScalarFieldContainer[int]
        avatar_hash: bytes
        def __init__(self, accountid: _Optional[int] = ..., guestid: _Optional[int] = ..., keyboard_enabled: bool = ..., mouse_enabled: bool = ..., controller_enabled: bool = ..., controller_slots: _Optional[_Iterable[int]] = ..., avatar_hash: _Optional[bytes] = ...) -> None: ...
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    MINIPROFILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    GAME_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DIRECT_INPUT_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[CRemotePlayTogetherGroupUpdateMsg.Player]
    player_index: int
    miniprofile_location: str
    game_name: str
    avatar_location: str
    direct_input: bool
    def __init__(self, players: _Optional[_Iterable[_Union[CRemotePlayTogetherGroupUpdateMsg.Player, _Mapping]]] = ..., player_index: _Optional[int] = ..., miniprofile_location: _Optional[str] = ..., game_name: _Optional[str] = ..., avatar_location: _Optional[str] = ..., direct_input: bool = ...) -> None: ...

class CSetInputTemporarilyDisabledMsg(_message.Message):
    __slots__ = ("disabled",)
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    def __init__(self, disabled: bool = ...) -> None: ...

class CSetQualityOverrideMsg(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class CSetBitrateOverrideMsg(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class CShowOnScreenKeyboardMsg(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CControllerPersonalizationUpdateMsg(_message.Message):
    __slots__ = ("controller_path", "controller_name", "reverse_diamond_button_layout")
    CONTROLLER_PATH_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_NAME_FIELD_NUMBER: _ClassVar[int]
    REVERSE_DIAMOND_BUTTON_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    controller_path: str
    controller_name: str
    reverse_diamond_button_layout: bool
    def __init__(self, controller_path: _Optional[str] = ..., controller_name: _Optional[str] = ..., reverse_diamond_button_layout: bool = ...) -> None: ...

class CVRConnectionReady(_message.Message):
    __slots__ = ("connect_params",)
    CONNECT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    connect_params: str
    def __init__(self, connect_params: _Optional[str] = ...) -> None: ...

class CStreamDataLostMsg(_message.Message):
    __slots__ = ("packets",)
    PACKETS_FIELD_NUMBER: _ClassVar[int]
    packets: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, packets: _Optional[_Iterable[int]] = ...) -> None: ...

class CAudioFormat(_message.Message):
    __slots__ = ("format", "frequency", "channels")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    format: EAudioFormat
    frequency: int
    channels: int
    def __init__(self, format: _Optional[_Union[EAudioFormat, str]] = ..., frequency: _Optional[int] = ..., channels: _Optional[int] = ...) -> None: ...

class CVideoFormat(_message.Message):
    __slots__ = ("format", "width", "height")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    format: EVideoFormat
    width: int
    height: int
    def __init__(self, format: _Optional[_Union[EVideoFormat, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class CFrameEvent(_message.Message):
    __slots__ = ("event_id", "timestamp")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    event_id: EStreamFrameEvent
    timestamp: int
    def __init__(self, event_id: _Optional[_Union[EStreamFrameEvent, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class CFrameStats(_message.Message):
    __slots__ = ("frame_id", "input_mark", "events", "result", "frame_start_delta", "frame_display_delta", "ping_time", "server_bitrate", "client_bitrate", "link_bandwidth", "packet_loss", "frame_size")
    FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_MARK_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    FRAME_START_DELTA_FIELD_NUMBER: _ClassVar[int]
    FRAME_DISPLAY_DELTA_FIELD_NUMBER: _ClassVar[int]
    PING_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_BITRATE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_BITRATE_FIELD_NUMBER: _ClassVar[int]
    LINK_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    PACKET_LOSS_FIELD_NUMBER: _ClassVar[int]
    FRAME_SIZE_FIELD_NUMBER: _ClassVar[int]
    frame_id: int
    input_mark: int
    events: _containers.RepeatedCompositeFieldContainer[CFrameEvent]
    result: EStreamFrameResult
    frame_start_delta: float
    frame_display_delta: float
    ping_time: float
    server_bitrate: float
    client_bitrate: float
    link_bandwidth: float
    packet_loss: float
    frame_size: int
    def __init__(self, frame_id: _Optional[int] = ..., input_mark: _Optional[int] = ..., events: _Optional[_Iterable[_Union[CFrameEvent, _Mapping]]] = ..., result: _Optional[_Union[EStreamFrameResult, str]] = ..., frame_start_delta: _Optional[float] = ..., frame_display_delta: _Optional[float] = ..., ping_time: _Optional[float] = ..., server_bitrate: _Optional[float] = ..., client_bitrate: _Optional[float] = ..., link_bandwidth: _Optional[float] = ..., packet_loss: _Optional[float] = ..., frame_size: _Optional[int] = ...) -> None: ...

class CFrameStatAccumulatedValue(_message.Message):
    __slots__ = ("stat_type", "count", "average", "stddev")
    STAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_FIELD_NUMBER: _ClassVar[int]
    STDDEV_FIELD_NUMBER: _ClassVar[int]
    stat_type: EFrameAccumulatedStat
    count: int
    average: float
    stddev: float
    def __init__(self, stat_type: _Optional[_Union[EFrameAccumulatedStat, str]] = ..., count: _Optional[int] = ..., average: _Optional[float] = ..., stddev: _Optional[float] = ...) -> None: ...

class CFrameStatsListMsg(_message.Message):
    __slots__ = ("data_type", "stats", "accumulated_stats", "latest_frame_id")
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ACCUMULATED_STATS_FIELD_NUMBER: _ClassVar[int]
    LATEST_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    data_type: EStreamingDataType
    stats: _containers.RepeatedCompositeFieldContainer[CFrameStats]
    accumulated_stats: _containers.RepeatedCompositeFieldContainer[CFrameStatAccumulatedValue]
    latest_frame_id: int
    def __init__(self, data_type: _Optional[_Union[EStreamingDataType, str]] = ..., stats: _Optional[_Iterable[_Union[CFrameStats, _Mapping]]] = ..., accumulated_stats: _Optional[_Iterable[_Union[CFrameStatAccumulatedValue, _Mapping]]] = ..., latest_frame_id: _Optional[int] = ...) -> None: ...

class CStreamingSessionStats(_message.Message):
    __slots__ = ("frame_loss_percentage", "average_network_time_ms", "stddev_network_time_ms", "test_data")
    FRAME_LOSS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_NETWORK_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    STDDEV_NETWORK_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TEST_DATA_FIELD_NUMBER: _ClassVar[int]
    frame_loss_percentage: float
    average_network_time_ms: float
    stddev_network_time_ms: float
    test_data: str
    def __init__(self, frame_loss_percentage: _Optional[float] = ..., average_network_time_ms: _Optional[float] = ..., stddev_network_time_ms: _Optional[float] = ..., test_data: _Optional[str] = ...) -> None: ...

class CDebugDumpMsg(_message.Message):
    __slots__ = ("screenshot",)
    SCREENSHOT_FIELD_NUMBER: _ClassVar[int]
    screenshot: bytes
    def __init__(self, screenshot: _Optional[bytes] = ...) -> None: ...

class CLogMsg(_message.Message):
    __slots__ = ("type", "message")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    type: int
    message: str
    def __init__(self, type: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CLogUploadMsg(_message.Message):
    __slots__ = ("type", "data")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    type: ELogFileType
    data: bytes
    def __init__(self, type: _Optional[_Union[ELogFileType, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class CTransportSignalMsg(_message.Message):
    __slots__ = ("webrtc", "sdr")
    class WebRTCMessage(_message.Message):
        __slots__ = ("greeting", "offer", "answer", "candidate")
        class Candidate(_message.Message):
            __slots__ = ("sdp_mid", "sdp_mline_index", "candidate")
            SDP_MID_FIELD_NUMBER: _ClassVar[int]
            SDP_MLINE_INDEX_FIELD_NUMBER: _ClassVar[int]
            CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            sdp_mid: str
            sdp_mline_index: int
            candidate: str
            def __init__(self, sdp_mid: _Optional[str] = ..., sdp_mline_index: _Optional[int] = ..., candidate: _Optional[str] = ...) -> None: ...
        GREETING_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        greeting: bool
        offer: str
        answer: str
        candidate: CTransportSignalMsg.WebRTCMessage.Candidate
        def __init__(self, greeting: bool = ..., offer: _Optional[str] = ..., answer: _Optional[str] = ..., candidate: _Optional[_Union[CTransportSignalMsg.WebRTCMessage.Candidate, _Mapping]] = ...) -> None: ...
    WEBRTC_FIELD_NUMBER: _ClassVar[int]
    SDR_FIELD_NUMBER: _ClassVar[int]
    webrtc: CTransportSignalMsg.WebRTCMessage
    sdr: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, webrtc: _Optional[_Union[CTransportSignalMsg.WebRTCMessage, _Mapping]] = ..., sdr: _Optional[_Iterable[bytes]] = ...) -> None: ...

class CControllerConfigMsg(_message.Message):
    __slots__ = ("type", "controllerPath", "appid", "personalizationResponse", "configResponse", "activeConfigChangeMsg")
    class ControllerConfigResponse(_message.Message):
        __slots__ = ("appid", "configURL", "controllerType", "controllerData", "selectionOrder", "actionBlock")
        APPID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURL_FIELD_NUMBER: _ClassVar[int]
        CONTROLLERTYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROLLERDATA_FIELD_NUMBER: _ClassVar[int]
        SELECTIONORDER_FIELD_NUMBER: _ClassVar[int]
        ACTIONBLOCK_FIELD_NUMBER: _ClassVar[int]
        appid: int
        configURL: str
        controllerType: int
        controllerData: str
        selectionOrder: int
        actionBlock: bool
        def __init__(self, appid: _Optional[int] = ..., configURL: _Optional[str] = ..., controllerType: _Optional[int] = ..., controllerData: _Optional[str] = ..., selectionOrder: _Optional[int] = ..., actionBlock: bool = ...) -> None: ...
    class ControllerPersonalizationResponse(_message.Message):
        __slots__ = ("personalizationData",)
        PERSONALIZATIONDATA_FIELD_NUMBER: _ClassVar[int]
        personalizationData: str
        def __init__(self, personalizationData: _Optional[str] = ...) -> None: ...
    class ControllerActiveConfigChangeResponse(_message.Message):
        __slots__ = ("configURL", "controllerType", "controllerData", "selectionOrder")
        CONFIGURL_FIELD_NUMBER: _ClassVar[int]
        CONTROLLERTYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROLLERDATA_FIELD_NUMBER: _ClassVar[int]
        SELECTIONORDER_FIELD_NUMBER: _ClassVar[int]
        configURL: str
        controllerType: int
        controllerData: str
        selectionOrder: int
        def __init__(self, configURL: _Optional[str] = ..., controllerType: _Optional[int] = ..., controllerData: _Optional[str] = ..., selectionOrder: _Optional[int] = ...) -> None: ...
    class ControllerActiveConfigMsg(_message.Message):
        __slots__ = ("appid", "configURL", "controllerType", "controllerData")
        APPID_FIELD_NUMBER: _ClassVar[int]
        CONFIGURL_FIELD_NUMBER: _ClassVar[int]
        CONTROLLERTYPE_FIELD_NUMBER: _ClassVar[int]
        CONTROLLERDATA_FIELD_NUMBER: _ClassVar[int]
        appid: int
        configURL: str
        controllerType: int
        controllerData: str
        def __init__(self, appid: _Optional[int] = ..., configURL: _Optional[str] = ..., controllerType: _Optional[int] = ..., controllerData: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTROLLERPATH_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    PERSONALIZATIONRESPONSE_FIELD_NUMBER: _ClassVar[int]
    CONFIGRESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACTIVECONFIGCHANGEMSG_FIELD_NUMBER: _ClassVar[int]
    type: EStreamControllerConfigMsg
    controllerPath: str
    appid: int
    personalizationResponse: CControllerConfigMsg.ControllerPersonalizationResponse
    configResponse: _containers.RepeatedCompositeFieldContainer[CControllerConfigMsg.ControllerConfigResponse]
    activeConfigChangeMsg: CControllerConfigMsg.ControllerActiveConfigMsg
    def __init__(self, type: _Optional[_Union[EStreamControllerConfigMsg, str]] = ..., controllerPath: _Optional[str] = ..., appid: _Optional[int] = ..., personalizationResponse: _Optional[_Union[CControllerConfigMsg.ControllerPersonalizationResponse, _Mapping]] = ..., configResponse: _Optional[_Iterable[_Union[CControllerConfigMsg.ControllerConfigResponse, _Mapping]]] = ..., activeConfigChangeMsg: _Optional[_Union[CControllerConfigMsg.ControllerActiveConfigMsg, _Mapping]] = ...) -> None: ...
