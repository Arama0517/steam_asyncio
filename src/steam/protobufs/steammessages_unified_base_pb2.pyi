from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EProtoExecutionSite(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EProtoExecutionSiteUnknown: _ClassVar[EProtoExecutionSite]
    k_EProtoExecutionSiteSteamClient: _ClassVar[EProtoExecutionSite]

class EProtoServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EProtoServiceTypeSteamMessages: _ClassVar[EProtoServiceType]
    k_EProtoServiceTypeVRGamepadUIMessages: _ClassVar[EProtoServiceType]
k_EProtoExecutionSiteUnknown: EProtoExecutionSite
k_EProtoExecutionSiteSteamClient: EProtoExecutionSite
k_EProtoServiceTypeSteamMessages: EProtoServiceType
k_EProtoServiceTypeVRGamepadUIMessages: EProtoServiceType
MESSAGE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
message_description: _descriptor.FieldDescriptor
FORCE_EMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
force_emit_message: _descriptor.FieldDescriptor
DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
description: _descriptor.FieldDescriptor
SERVICE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
service_description: _descriptor.FieldDescriptor
SERVICE_EXECUTION_SITE_FIELD_NUMBER: _ClassVar[int]
service_execution_site: _descriptor.FieldDescriptor
SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
service_type: _descriptor.FieldDescriptor
FORCE_EMIT_SERVICE_FIELD_NUMBER: _ClassVar[int]
force_emit_service: _descriptor.FieldDescriptor
METHOD_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
method_description: _descriptor.FieldDescriptor
ENUM_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
enum_description: _descriptor.FieldDescriptor
ENUM_VALUE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
enum_value_description: _descriptor.FieldDescriptor

class NoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
