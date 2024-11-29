import enums_pb2 as _enums_pb2
import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EClientExecutionSite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EClientExecutionSiteInvalid: _ClassVar[EClientExecutionSite]
    k_EClientExecutionSiteSteamUI: _ClassVar[EClientExecutionSite]
    k_EClientExecutionSiteClientdll: _ClassVar[EClientExecutionSite]
    k_EClientExecutionSiteAny: _ClassVar[EClientExecutionSite]
k_EClientExecutionSiteInvalid: EClientExecutionSite
k_EClientExecutionSiteSteamUI: EClientExecutionSite
k_EClientExecutionSiteClientdll: EClientExecutionSite
k_EClientExecutionSiteAny: EClientExecutionSite
WEBUI_SERVICE_EXECUTION_SITE_FIELD_NUMBER: _ClassVar[int]
webui_service_execution_site: _descriptor.FieldDescriptor
WEBUI_METHOD_EXECUTION_SITE_FIELD_NUMBER: _ClassVar[int]
webui_method_execution_site: _descriptor.FieldDescriptor

class WebUINoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
