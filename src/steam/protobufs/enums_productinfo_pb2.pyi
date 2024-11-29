import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EContentDescriptorID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EContentDescriptor_NudityOrSexualContent: _ClassVar[EContentDescriptorID]
    k_EContentDescriptor_FrequentViolenceOrGore: _ClassVar[EContentDescriptorID]
    k_EContentDescriptor_AdultOnlySexualContent: _ClassVar[EContentDescriptorID]
    k_EContentDescriptor_GratuitousSexualContent: _ClassVar[EContentDescriptorID]
    k_EContentDescriptor_AnyMatureContent: _ClassVar[EContentDescriptorID]
    k_EContentDescriptorMAX: _ClassVar[EContentDescriptorID]
k_EContentDescriptor_NudityOrSexualContent: EContentDescriptorID
k_EContentDescriptor_FrequentViolenceOrGore: EContentDescriptorID
k_EContentDescriptor_AdultOnlySexualContent: EContentDescriptorID
k_EContentDescriptor_GratuitousSexualContent: EContentDescriptorID
k_EContentDescriptor_AnyMatureContent: EContentDescriptorID
k_EContentDescriptorMAX: EContentDescriptorID
