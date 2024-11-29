from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EInputMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EInputModeUnknown: _ClassVar[EInputMode]
    k_EInputModeMouse: _ClassVar[EInputMode]
    k_EInputModeController: _ClassVar[EInputMode]
    k_EInputModeMouseAndController: _ClassVar[EInputMode]

class EMouseMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EMouseModeUnknown: _ClassVar[EMouseMode]
    k_EMouseModeRelativeCursor: _ClassVar[EMouseMode]
    k_EMouseModeAbsoluteCursor: _ClassVar[EMouseMode]
    k_EMouseModeTouch: _ClassVar[EMouseMode]
    k_EMouseModeRelative: _ClassVar[EMouseMode]

class EControllerElementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EControllerElementTypeNone: _ClassVar[EControllerElementType]
    k_EControllerElementTypeThumb: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonSteam: _ClassVar[EControllerElementType]
    k_EControllerElementTypeJoystickLeft: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonJoystickLeft: _ClassVar[EControllerElementType]
    k_EControllerElementTypeJoystickRight: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonJoystickRight: _ClassVar[EControllerElementType]
    k_EControllerElementTypeDPad: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonA: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonB: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonX: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonY: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonSelect: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonStart: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonTriggerLeft: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonTriggerRight: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonBumperLeft: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonBumperRight: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro0: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro1: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro2: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro3: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro4: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro5: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro6: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro7: _ClassVar[EControllerElementType]
    k_EControllerElementTypeTrackpadCenter: _ClassVar[EControllerElementType]
    k_EControllerElementTypeTrackpadLeft: _ClassVar[EControllerElementType]
    k_EControllerElementTypeTrackpadRight: _ClassVar[EControllerElementType]
    k_EControllerElementTypeKeyboard: _ClassVar[EControllerElementType]
    k_EControllerElementTypeMagnifyingGlass: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro1Finger: _ClassVar[EControllerElementType]
    k_EControllerElementTypeButtonMacro2Finger: _ClassVar[EControllerElementType]
    k_EControllerElementTypeRecordInput: _ClassVar[EControllerElementType]
    k_EControllerElementTypePlaybackInput: _ClassVar[EControllerElementType]
    k_EControllerElementTypePaste: _ClassVar[EControllerElementType]
    k_EControllerElementTypeMax: _ClassVar[EControllerElementType]
k_EInputModeUnknown: EInputMode
k_EInputModeMouse: EInputMode
k_EInputModeController: EInputMode
k_EInputModeMouseAndController: EInputMode
k_EMouseModeUnknown: EMouseMode
k_EMouseModeRelativeCursor: EMouseMode
k_EMouseModeAbsoluteCursor: EMouseMode
k_EMouseModeTouch: EMouseMode
k_EMouseModeRelative: EMouseMode
k_EControllerElementTypeNone: EControllerElementType
k_EControllerElementTypeThumb: EControllerElementType
k_EControllerElementTypeButtonSteam: EControllerElementType
k_EControllerElementTypeJoystickLeft: EControllerElementType
k_EControllerElementTypeButtonJoystickLeft: EControllerElementType
k_EControllerElementTypeJoystickRight: EControllerElementType
k_EControllerElementTypeButtonJoystickRight: EControllerElementType
k_EControllerElementTypeDPad: EControllerElementType
k_EControllerElementTypeButtonA: EControllerElementType
k_EControllerElementTypeButtonB: EControllerElementType
k_EControllerElementTypeButtonX: EControllerElementType
k_EControllerElementTypeButtonY: EControllerElementType
k_EControllerElementTypeButtonSelect: EControllerElementType
k_EControllerElementTypeButtonStart: EControllerElementType
k_EControllerElementTypeButtonTriggerLeft: EControllerElementType
k_EControllerElementTypeButtonTriggerRight: EControllerElementType
k_EControllerElementTypeButtonBumperLeft: EControllerElementType
k_EControllerElementTypeButtonBumperRight: EControllerElementType
k_EControllerElementTypeButtonMacro0: EControllerElementType
k_EControllerElementTypeButtonMacro1: EControllerElementType
k_EControllerElementTypeButtonMacro2: EControllerElementType
k_EControllerElementTypeButtonMacro3: EControllerElementType
k_EControllerElementTypeButtonMacro4: EControllerElementType
k_EControllerElementTypeButtonMacro5: EControllerElementType
k_EControllerElementTypeButtonMacro6: EControllerElementType
k_EControllerElementTypeButtonMacro7: EControllerElementType
k_EControllerElementTypeTrackpadCenter: EControllerElementType
k_EControllerElementTypeTrackpadLeft: EControllerElementType
k_EControllerElementTypeTrackpadRight: EControllerElementType
k_EControllerElementTypeKeyboard: EControllerElementType
k_EControllerElementTypeMagnifyingGlass: EControllerElementType
k_EControllerElementTypeButtonMacro1Finger: EControllerElementType
k_EControllerElementTypeButtonMacro2Finger: EControllerElementType
k_EControllerElementTypeRecordInput: EControllerElementType
k_EControllerElementTypePlaybackInput: EControllerElementType
k_EControllerElementTypePaste: EControllerElementType
k_EControllerElementTypeMax: EControllerElementType

class CVirtualControllerElement(_message.Message):
    __slots__ = ("type", "visible", "x_position", "y_position", "x_scale", "y_scale")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    X_POSITION_FIELD_NUMBER: _ClassVar[int]
    Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    X_SCALE_FIELD_NUMBER: _ClassVar[int]
    Y_SCALE_FIELD_NUMBER: _ClassVar[int]
    type: EControllerElementType
    visible: bool
    x_position: float
    y_position: float
    x_scale: float
    y_scale: float
    def __init__(self, type: _Optional[_Union[EControllerElementType, str]] = ..., visible: bool = ..., x_position: _Optional[float] = ..., y_position: _Optional[float] = ..., x_scale: _Optional[float] = ..., y_scale: _Optional[float] = ...) -> None: ...

class CVirtualControllerColor(_message.Message):
    __slots__ = ("r", "g", "b", "a")
    R_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    r: float
    g: float
    b: float
    a: float
    def __init__(self, r: _Optional[float] = ..., g: _Optional[float] = ..., b: _Optional[float] = ..., a: _Optional[float] = ...) -> None: ...

class CVirtualControllerLayout(_message.Message):
    __slots__ = ("layout_version", "actionset_id", "elements", "color")
    LAYOUT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ACTIONSET_ID_FIELD_NUMBER: _ClassVar[int]
    ELEMENTS_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    layout_version: int
    actionset_id: int
    elements: _containers.RepeatedCompositeFieldContainer[CVirtualControllerElement]
    color: CVirtualControllerColor
    def __init__(self, layout_version: _Optional[int] = ..., actionset_id: _Optional[int] = ..., elements: _Optional[_Iterable[_Union[CVirtualControllerElement, _Mapping]]] = ..., color: _Optional[_Union[CVirtualControllerColor, _Mapping]] = ...) -> None: ...

class CVirtualControllerLayouts(_message.Message):
    __slots__ = ("layouts", "input_mode", "mouse_mode", "trackpad_sensitivity", "pinch_zoom_enabled", "pinch_zoom_x", "pinch_zoom_y", "pinch_zoom_scale", "shaken", "mouse_offscreen")
    LAYOUTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_MODE_FIELD_NUMBER: _ClassVar[int]
    MOUSE_MODE_FIELD_NUMBER: _ClassVar[int]
    TRACKPAD_SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    PINCH_ZOOM_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PINCH_ZOOM_X_FIELD_NUMBER: _ClassVar[int]
    PINCH_ZOOM_Y_FIELD_NUMBER: _ClassVar[int]
    PINCH_ZOOM_SCALE_FIELD_NUMBER: _ClassVar[int]
    SHAKEN_FIELD_NUMBER: _ClassVar[int]
    MOUSE_OFFSCREEN_FIELD_NUMBER: _ClassVar[int]
    layouts: _containers.RepeatedCompositeFieldContainer[CVirtualControllerLayout]
    input_mode: EInputMode
    mouse_mode: EMouseMode
    trackpad_sensitivity: float
    pinch_zoom_enabled: bool
    pinch_zoom_x: float
    pinch_zoom_y: float
    pinch_zoom_scale: float
    shaken: bool
    mouse_offscreen: bool
    def __init__(self, layouts: _Optional[_Iterable[_Union[CVirtualControllerLayout, _Mapping]]] = ..., input_mode: _Optional[_Union[EInputMode, str]] = ..., mouse_mode: _Optional[_Union[EMouseMode, str]] = ..., trackpad_sensitivity: _Optional[float] = ..., pinch_zoom_enabled: bool = ..., pinch_zoom_x: _Optional[float] = ..., pinch_zoom_y: _Optional[float] = ..., pinch_zoom_scale: _Optional[float] = ..., shaken: bool = ..., mouse_offscreen: bool = ...) -> None: ...

class CVirtualControllerConfig(_message.Message):
    __slots__ = ("name", "actionsets", "default_mouse_mode")
    class Control(_message.Message):
        __slots__ = ("name", "icon", "input_source", "input_mode", "input_element", "output_gamepad", "output_keyboard", "output_mouse", "icon_foreground", "icon_background", "input_toggle", "input_activate_stick_or_trackpad", "activation_type", "long_press_ms", "double_press_ms")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        INPUT_SOURCE_FIELD_NUMBER: _ClassVar[int]
        INPUT_MODE_FIELD_NUMBER: _ClassVar[int]
        INPUT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_GAMEPAD_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_KEYBOARD_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_MOUSE_FIELD_NUMBER: _ClassVar[int]
        ICON_FOREGROUND_FIELD_NUMBER: _ClassVar[int]
        ICON_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
        INPUT_TOGGLE_FIELD_NUMBER: _ClassVar[int]
        INPUT_ACTIVATE_STICK_OR_TRACKPAD_FIELD_NUMBER: _ClassVar[int]
        ACTIVATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        LONG_PRESS_MS_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_PRESS_MS_FIELD_NUMBER: _ClassVar[int]
        name: str
        icon: str
        input_source: int
        input_mode: int
        input_element: int
        output_gamepad: int
        output_keyboard: int
        output_mouse: int
        icon_foreground: str
        icon_background: str
        input_toggle: bool
        input_activate_stick_or_trackpad: int
        activation_type: int
        long_press_ms: int
        double_press_ms: int
        def __init__(self, name: _Optional[str] = ..., icon: _Optional[str] = ..., input_source: _Optional[int] = ..., input_mode: _Optional[int] = ..., input_element: _Optional[int] = ..., output_gamepad: _Optional[int] = ..., output_keyboard: _Optional[int] = ..., output_mouse: _Optional[int] = ..., icon_foreground: _Optional[str] = ..., icon_background: _Optional[str] = ..., input_toggle: bool = ..., input_activate_stick_or_trackpad: _Optional[int] = ..., activation_type: _Optional[int] = ..., long_press_ms: _Optional[int] = ..., double_press_ms: _Optional[int] = ...) -> None: ...
    class ActionSet(_message.Message):
        __slots__ = ("id", "parent_id", "name", "controls")
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        CONTROLS_FIELD_NUMBER: _ClassVar[int]
        id: int
        parent_id: int
        name: str
        controls: _containers.RepeatedCompositeFieldContainer[CVirtualControllerConfig.Control]
        def __init__(self, id: _Optional[int] = ..., parent_id: _Optional[int] = ..., name: _Optional[str] = ..., controls: _Optional[_Iterable[_Union[CVirtualControllerConfig.Control, _Mapping]]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIONSETS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MOUSE_MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    actionsets: _containers.RepeatedCompositeFieldContainer[CVirtualControllerConfig.ActionSet]
    default_mouse_mode: EMouseMode
    def __init__(self, name: _Optional[str] = ..., actionsets: _Optional[_Iterable[_Union[CVirtualControllerConfig.ActionSet, _Mapping]]] = ..., default_mouse_mode: _Optional[_Union[EMouseMode, str]] = ...) -> None: ...

class CVirtualControllerLayoutPackage(_message.Message):
    __slots__ = ("appid", "creator", "initial_revision", "saved_revision", "config", "layouts")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CREATOR_FIELD_NUMBER: _ClassVar[int]
    INITIAL_REVISION_FIELD_NUMBER: _ClassVar[int]
    SAVED_REVISION_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    LAYOUTS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    creator: int
    initial_revision: int
    saved_revision: int
    config: CVirtualControllerConfig
    layouts: CVirtualControllerLayouts
    def __init__(self, appid: _Optional[int] = ..., creator: _Optional[int] = ..., initial_revision: _Optional[int] = ..., saved_revision: _Optional[int] = ..., config: _Optional[_Union[CVirtualControllerConfig, _Mapping]] = ..., layouts: _Optional[_Union[CVirtualControllerLayouts, _Mapping]] = ...) -> None: ...

class CVirtualControllerGlobalConfig(_message.Message):
    __slots__ = ("feedback_enabled", "gyroscope_enabled", "auto_fade_enabled", "rumble_enabled", "shake_fade_enabled")
    FEEDBACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_FADE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RUMBLE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHAKE_FADE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    feedback_enabled: bool
    gyroscope_enabled: bool
    auto_fade_enabled: bool
    rumble_enabled: bool
    shake_fade_enabled: bool
    def __init__(self, feedback_enabled: bool = ..., gyroscope_enabled: bool = ..., auto_fade_enabled: bool = ..., rumble_enabled: bool = ..., shake_fade_enabled: bool = ...) -> None: ...
