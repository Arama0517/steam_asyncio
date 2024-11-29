import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EValveIndexComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EValveIndexComponentUnknown: _ClassVar[EValveIndexComponent]
    k_EValveIndexComponentHMD: _ClassVar[EValveIndexComponent]
    k_EValveIndexComponentLeftKnuckle: _ClassVar[EValveIndexComponent]
    k_EValveIndexComponentRightKnuckle: _ClassVar[EValveIndexComponent]
    k_ETempDTst1: _ClassVar[EValveIndexComponent]
    k_ETempDTst2: _ClassVar[EValveIndexComponent]
    k_ETempDTst3: _ClassVar[EValveIndexComponent]
k_EValveIndexComponentUnknown: EValveIndexComponent
k_EValveIndexComponentHMD: EValveIndexComponent
k_EValveIndexComponentLeftKnuckle: EValveIndexComponent
k_EValveIndexComponentRightKnuckle: EValveIndexComponent
k_ETempDTst1: EValveIndexComponent
k_ETempDTst2: EValveIndexComponent
k_ETempDTst3: EValveIndexComponent

class CAccountHardware_RegisterSteamController_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ...) -> None: ...

class CAccountHardware_RegisterSteamController_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountHardware_CompleteSteamControllerRegistration_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ...) -> None: ...

class CAccountHardware_CompleteSteamControllerRegistration_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountHardware_QueryAccountsRegisteredToSerial_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ...) -> None: ...

class CAccountHardware_QueryAccountsRegisteredToSerial_Accounts(_message.Message):
    __slots__ = ("accountid", "registration_complete")
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    accountid: int
    registration_complete: bool
    def __init__(self, accountid: _Optional[int] = ..., registration_complete: bool = ...) -> None: ...

class CAccountHardware_QueryAccountsRegisteredToSerial_Response(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[CAccountHardware_QueryAccountsRegisteredToSerial_Accounts]
    def __init__(self, accounts: _Optional[_Iterable[_Union[CAccountHardware_QueryAccountsRegisteredToSerial_Accounts, _Mapping]]] = ...) -> None: ...

class CAccountHardware_SteamControllerSetConfig_ControllerConfig(_message.Message):
    __slots__ = ("appidorname", "publishedfileid", "templatename")
    APPIDORNAME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATENAME_FIELD_NUMBER: _ClassVar[int]
    appidorname: str
    publishedfileid: int
    templatename: str
    def __init__(self, appidorname: _Optional[str] = ..., publishedfileid: _Optional[int] = ..., templatename: _Optional[str] = ...) -> None: ...

class CAccountHardware_SteamControllerSetConfig_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code", "accountid", "configurations", "controller_type", "only_for_this_serial")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ONLY_FOR_THIS_SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    accountid: int
    configurations: _containers.RepeatedCompositeFieldContainer[CAccountHardware_SteamControllerSetConfig_ControllerConfig]
    controller_type: int
    only_for_this_serial: bool
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ..., accountid: _Optional[int] = ..., configurations: _Optional[_Iterable[_Union[CAccountHardware_SteamControllerSetConfig_ControllerConfig, _Mapping]]] = ..., controller_type: _Optional[int] = ..., only_for_this_serial: bool = ...) -> None: ...

class CAccountHardware_SteamControllerSetConfig_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountHardware_SteamControllerGetConfig_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code", "accountid", "appidorname", "controller_type", "only_for_this_serial")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    APPIDORNAME_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ONLY_FOR_THIS_SERIAL_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    accountid: int
    appidorname: str
    controller_type: int
    only_for_this_serial: bool
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ..., accountid: _Optional[int] = ..., appidorname: _Optional[str] = ..., controller_type: _Optional[int] = ..., only_for_this_serial: bool = ...) -> None: ...

class CAccountHardware_SteamControllerGetConfig_ControllerConfig(_message.Message):
    __slots__ = ("appidorname", "publishedfileid", "templatename", "serial_number", "autosave")
    APPIDORNAME_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATENAME_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTOSAVE_FIELD_NUMBER: _ClassVar[int]
    appidorname: str
    publishedfileid: int
    templatename: str
    serial_number: str
    autosave: bool
    def __init__(self, appidorname: _Optional[str] = ..., publishedfileid: _Optional[int] = ..., templatename: _Optional[str] = ..., serial_number: _Optional[str] = ..., autosave: bool = ...) -> None: ...

class CAccountHardware_SteamControllerGetConfig_Response(_message.Message):
    __slots__ = ("configurations",)
    CONFIGURATIONS_FIELD_NUMBER: _ClassVar[int]
    configurations: _containers.RepeatedCompositeFieldContainer[CAccountHardware_SteamControllerGetConfig_ControllerConfig]
    def __init__(self, configurations: _Optional[_Iterable[_Union[CAccountHardware_SteamControllerGetConfig_ControllerConfig, _Mapping]]] = ...) -> None: ...

class CAccountHardware_DeRegisterSteamController_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code", "accountid")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    accountid: int
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ..., accountid: _Optional[int] = ...) -> None: ...

class CAccountHardware_DeRegisterSteamController_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountHardware_SetPersonalizationFile_Request(_message.Message):
    __slots__ = ("serial_number", "publishedfileid", "accountid")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    publishedfileid: int
    accountid: int
    def __init__(self, serial_number: _Optional[str] = ..., publishedfileid: _Optional[int] = ..., accountid: _Optional[int] = ...) -> None: ...

class CAccountHardware_SetPersonalizationFile_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountHardware_GetPersonalizationFile_Request(_message.Message):
    __slots__ = ("serial_number", "accountid")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    accountid: int
    def __init__(self, serial_number: _Optional[str] = ..., accountid: _Optional[int] = ...) -> None: ...

class CAccountHardware_GetPersonalizationFile_Response(_message.Message):
    __slots__ = ("publishedfileid",)
    PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    publishedfileid: int
    def __init__(self, publishedfileid: _Optional[int] = ...) -> None: ...

class CAccountHardware_VRCompatibilityCheck_Request(_message.Message):
    __slots__ = ("product_name", "values")
    class Pair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    values: _containers.RepeatedCompositeFieldContainer[CAccountHardware_VRCompatibilityCheck_Request.Pair]
    def __init__(self, product_name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[CAccountHardware_VRCompatibilityCheck_Request.Pair, _Mapping]]] = ...) -> None: ...

class CAccountHardware_VRCompatibilityCheck_Response(_message.Message):
    __slots__ = ("values", "components")
    class Pair(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ComponentDisplay(_message.Message):
        __slots__ = ("name", "image", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        image: str
        value: str
        def __init__(self, name: _Optional[str] = ..., image: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CAccountHardware_VRCompatibilityCheck_Response.Pair]
    components: _containers.RepeatedCompositeFieldContainer[CAccountHardware_VRCompatibilityCheck_Response.ComponentDisplay]
    def __init__(self, values: _Optional[_Iterable[_Union[CAccountHardware_VRCompatibilityCheck_Response.Pair, _Mapping]]] = ..., components: _Optional[_Iterable[_Union[CAccountHardware_VRCompatibilityCheck_Response.ComponentDisplay, _Mapping]]] = ...) -> None: ...

class CAccountHardware_RegisterValveIndexComponent_Request(_message.Message):
    __slots__ = ("serial_number", "manufacturer_serial_number", "component_code", "component_type", "estimated_time_registered")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_CODE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TIME_REGISTERED_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    manufacturer_serial_number: str
    component_code: str
    component_type: EValveIndexComponent
    estimated_time_registered: int
    def __init__(self, serial_number: _Optional[str] = ..., manufacturer_serial_number: _Optional[str] = ..., component_code: _Optional[str] = ..., component_type: _Optional[_Union[EValveIndexComponent, str]] = ..., estimated_time_registered: _Optional[int] = ...) -> None: ...

class CAccountHardware_RegisterValveIndexComponent_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CAccountHardware_GetSteamDeckComponents_Request(_message.Message):
    __slots__ = ("serial_number", "controller_code")
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CODE_FIELD_NUMBER: _ClassVar[int]
    serial_number: str
    controller_code: str
    def __init__(self, serial_number: _Optional[str] = ..., controller_code: _Optional[str] = ...) -> None: ...

class CAccountHardware_GetSteamDeckComponents_Response(_message.Message):
    __slots__ = ("json_components",)
    JSON_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    json_components: str
    def __init__(self, json_components: _Optional[str] = ...) -> None: ...

class AccountHardware(_service.service): ...

class AccountHardware_Stub(AccountHardware): ...
