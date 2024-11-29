import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CSteamInputService_ControllerButtonStateChanged_Notification(_message.Message):
    __slots__ = ("controller_index", "dpad_up", "dpad_down", "dpad_left", "dpad_right", "button_south", "button_east", "button_west", "button_north", "button_back_view", "button_start_options", "button_steam", "button_quick_access", "button_mute_capture", "left_stick_click", "left_stick_touch", "left_stick_deflect", "right_stick_click", "right_stick_touch", "right_stick_deflect", "center_trackpad_touch", "center_trackpad_click", "left_trackpad_touch", "left_trackpad_click", "right_trackpad_touch", "right_trackpad_click", "left_bumper", "left_trigger", "l4", "l5", "left_aux", "right_bumper", "right_trigger", "r4", "r5", "right_aux")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    DPAD_UP_FIELD_NUMBER: _ClassVar[int]
    DPAD_DOWN_FIELD_NUMBER: _ClassVar[int]
    DPAD_LEFT_FIELD_NUMBER: _ClassVar[int]
    DPAD_RIGHT_FIELD_NUMBER: _ClassVar[int]
    BUTTON_SOUTH_FIELD_NUMBER: _ClassVar[int]
    BUTTON_EAST_FIELD_NUMBER: _ClassVar[int]
    BUTTON_WEST_FIELD_NUMBER: _ClassVar[int]
    BUTTON_NORTH_FIELD_NUMBER: _ClassVar[int]
    BUTTON_BACK_VIEW_FIELD_NUMBER: _ClassVar[int]
    BUTTON_START_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    BUTTON_STEAM_FIELD_NUMBER: _ClassVar[int]
    BUTTON_QUICK_ACCESS_FIELD_NUMBER: _ClassVar[int]
    BUTTON_MUTE_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    LEFT_STICK_CLICK_FIELD_NUMBER: _ClassVar[int]
    LEFT_STICK_TOUCH_FIELD_NUMBER: _ClassVar[int]
    LEFT_STICK_DEFLECT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_STICK_CLICK_FIELD_NUMBER: _ClassVar[int]
    RIGHT_STICK_TOUCH_FIELD_NUMBER: _ClassVar[int]
    RIGHT_STICK_DEFLECT_FIELD_NUMBER: _ClassVar[int]
    CENTER_TRACKPAD_TOUCH_FIELD_NUMBER: _ClassVar[int]
    CENTER_TRACKPAD_CLICK_FIELD_NUMBER: _ClassVar[int]
    LEFT_TRACKPAD_TOUCH_FIELD_NUMBER: _ClassVar[int]
    LEFT_TRACKPAD_CLICK_FIELD_NUMBER: _ClassVar[int]
    RIGHT_TRACKPAD_TOUCH_FIELD_NUMBER: _ClassVar[int]
    RIGHT_TRACKPAD_CLICK_FIELD_NUMBER: _ClassVar[int]
    LEFT_BUMPER_FIELD_NUMBER: _ClassVar[int]
    LEFT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    L4_FIELD_NUMBER: _ClassVar[int]
    L5_FIELD_NUMBER: _ClassVar[int]
    LEFT_AUX_FIELD_NUMBER: _ClassVar[int]
    RIGHT_BUMPER_FIELD_NUMBER: _ClassVar[int]
    RIGHT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    R4_FIELD_NUMBER: _ClassVar[int]
    R5_FIELD_NUMBER: _ClassVar[int]
    RIGHT_AUX_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    dpad_up: bool
    dpad_down: bool
    dpad_left: bool
    dpad_right: bool
    button_south: bool
    button_east: bool
    button_west: bool
    button_north: bool
    button_back_view: bool
    button_start_options: bool
    button_steam: bool
    button_quick_access: bool
    button_mute_capture: bool
    left_stick_click: bool
    left_stick_touch: bool
    left_stick_deflect: bool
    right_stick_click: bool
    right_stick_touch: bool
    right_stick_deflect: bool
    center_trackpad_touch: bool
    center_trackpad_click: bool
    left_trackpad_touch: bool
    left_trackpad_click: bool
    right_trackpad_touch: bool
    right_trackpad_click: bool
    left_bumper: bool
    left_trigger: bool
    l4: bool
    l5: bool
    left_aux: bool
    right_bumper: bool
    right_trigger: bool
    r4: bool
    r5: bool
    right_aux: bool
    def __init__(self, controller_index: _Optional[int] = ..., dpad_up: bool = ..., dpad_down: bool = ..., dpad_left: bool = ..., dpad_right: bool = ..., button_south: bool = ..., button_east: bool = ..., button_west: bool = ..., button_north: bool = ..., button_back_view: bool = ..., button_start_options: bool = ..., button_steam: bool = ..., button_quick_access: bool = ..., button_mute_capture: bool = ..., left_stick_click: bool = ..., left_stick_touch: bool = ..., left_stick_deflect: bool = ..., right_stick_click: bool = ..., right_stick_touch: bool = ..., right_stick_deflect: bool = ..., center_trackpad_touch: bool = ..., center_trackpad_click: bool = ..., left_trackpad_touch: bool = ..., left_trackpad_click: bool = ..., right_trackpad_touch: bool = ..., right_trackpad_click: bool = ..., left_bumper: bool = ..., left_trigger: bool = ..., l4: bool = ..., l5: bool = ..., left_aux: bool = ..., right_bumper: bool = ..., right_trigger: bool = ..., r4: bool = ..., r5: bool = ..., right_aux: bool = ...) -> None: ...

class ControllerVector2(_message.Message):
    __slots__ = ("x", "y")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class ControllerVector3(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class ControllerQuaternion(_message.Message):
    __slots__ = ("w", "x", "y", "z")
    W_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(self, w: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class ControllerGyroEulerAngles(_message.Message):
    __slots__ = ("pitch", "yaw", "roll")
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    pitch: float
    yaw: float
    roll: float
    def __init__(self, pitch: _Optional[float] = ..., yaw: _Optional[float] = ..., roll: _Optional[float] = ...) -> None: ...

class CSteamInputService_ControllerAxesStateChange_Notification(_message.Message):
    __slots__ = ("controller_index", "joystick_left", "joystick_right", "trackpad_left", "trackpad_right", "trackpad_center", "trackpad_pressure_left", "trackpad_pressure_right", "trigger_left", "trigger_right")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    JOYSTICK_LEFT_FIELD_NUMBER: _ClassVar[int]
    JOYSTICK_RIGHT_FIELD_NUMBER: _ClassVar[int]
    TRACKPAD_LEFT_FIELD_NUMBER: _ClassVar[int]
    TRACKPAD_RIGHT_FIELD_NUMBER: _ClassVar[int]
    TRACKPAD_CENTER_FIELD_NUMBER: _ClassVar[int]
    TRACKPAD_PRESSURE_LEFT_FIELD_NUMBER: _ClassVar[int]
    TRACKPAD_PRESSURE_RIGHT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_LEFT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_RIGHT_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    joystick_left: ControllerVector2
    joystick_right: ControllerVector2
    trackpad_left: ControllerVector2
    trackpad_right: ControllerVector2
    trackpad_center: ControllerVector2
    trackpad_pressure_left: float
    trackpad_pressure_right: float
    trigger_left: float
    trigger_right: float
    def __init__(self, controller_index: _Optional[int] = ..., joystick_left: _Optional[_Union[ControllerVector2, _Mapping]] = ..., joystick_right: _Optional[_Union[ControllerVector2, _Mapping]] = ..., trackpad_left: _Optional[_Union[ControllerVector2, _Mapping]] = ..., trackpad_right: _Optional[_Union[ControllerVector2, _Mapping]] = ..., trackpad_center: _Optional[_Union[ControllerVector2, _Mapping]] = ..., trackpad_pressure_left: _Optional[float] = ..., trackpad_pressure_right: _Optional[float] = ..., trigger_left: _Optional[float] = ..., trigger_right: _Optional[float] = ...) -> None: ...

class CSteamInputService_GyroQuaternionChanged_Notification(_message.Message):
    __slots__ = ("controller_index", "imu_index", "gyro_raw_quaternion", "gyro_filtered_quaternion", "imu_sensor_delta_time")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    IMU_INDEX_FIELD_NUMBER: _ClassVar[int]
    GYRO_RAW_QUATERNION_FIELD_NUMBER: _ClassVar[int]
    GYRO_FILTERED_QUATERNION_FIELD_NUMBER: _ClassVar[int]
    IMU_SENSOR_DELTA_TIME_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    imu_index: int
    gyro_raw_quaternion: ControllerQuaternion
    gyro_filtered_quaternion: ControllerQuaternion
    imu_sensor_delta_time: int
    def __init__(self, controller_index: _Optional[int] = ..., imu_index: _Optional[int] = ..., gyro_raw_quaternion: _Optional[_Union[ControllerQuaternion, _Mapping]] = ..., gyro_filtered_quaternion: _Optional[_Union[ControllerQuaternion, _Mapping]] = ..., imu_sensor_delta_time: _Optional[int] = ...) -> None: ...

class CSteamInputService_GyroSpeedChanged_Notification(_message.Message):
    __slots__ = ("controller_index", "imu_index", "gyro_raw_speed", "gyro_filtered_speed")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    IMU_INDEX_FIELD_NUMBER: _ClassVar[int]
    GYRO_RAW_SPEED_FIELD_NUMBER: _ClassVar[int]
    GYRO_FILTERED_SPEED_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    imu_index: int
    gyro_raw_speed: ControllerGyroEulerAngles
    gyro_filtered_speed: ControllerGyroEulerAngles
    def __init__(self, controller_index: _Optional[int] = ..., imu_index: _Optional[int] = ..., gyro_raw_speed: _Optional[_Union[ControllerGyroEulerAngles, _Mapping]] = ..., gyro_filtered_speed: _Optional[_Union[ControllerGyroEulerAngles, _Mapping]] = ...) -> None: ...

class CSteamInputService_GyroAccelerometerChanged_Notification(_message.Message):
    __slots__ = ("controller_index", "imu_index", "acceleromter_1g", "trusted_gravity_1g")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    IMU_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMTER_1G_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_GRAVITY_1G_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    imu_index: int
    acceleromter_1g: ControllerVector3
    trusted_gravity_1g: ControllerVector3
    def __init__(self, controller_index: _Optional[int] = ..., imu_index: _Optional[int] = ..., acceleromter_1g: _Optional[_Union[ControllerVector3, _Mapping]] = ..., trusted_gravity_1g: _Optional[_Union[ControllerVector3, _Mapping]] = ...) -> None: ...

class CSteamInputService_GyroCalibration_Notification(_message.Message):
    __slots__ = ("controller_index", "imu_index", "acceleromter_noise", "gyroscope_noise", "calibration_progress")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    IMU_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACCELEROMTER_NOISE_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_NOISE_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    imu_index: int
    acceleromter_noise: float
    gyroscope_noise: float
    calibration_progress: float
    def __init__(self, controller_index: _Optional[int] = ..., imu_index: _Optional[int] = ..., acceleromter_noise: _Optional[float] = ..., gyroscope_noise: _Optional[float] = ..., calibration_progress: _Optional[float] = ...) -> None: ...

class CSteamInputService_ControllerStateFlow_Request(_message.Message):
    __slots__ = ("controller_index", "flow_mode")
    CONTROLLER_INDEX_FIELD_NUMBER: _ClassVar[int]
    FLOW_MODE_FIELD_NUMBER: _ClassVar[int]
    controller_index: int
    flow_mode: int
    def __init__(self, controller_index: _Optional[int] = ..., flow_mode: _Optional[int] = ...) -> None: ...

class CSteamInputService_ControllerStateFlow_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SteamInputManager(_service.service): ...

class SteamInputManager_Stub(SteamInputManager): ...
