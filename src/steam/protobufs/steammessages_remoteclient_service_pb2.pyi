import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import steammessages_remoteclient_service_messages_pb2 as _steammessages_remoteclient_service_messages_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class RemoteClient(_service.service): ...

class RemoteClient_Stub(RemoteClient): ...

class RemoteClientSteamClient(_service.service): ...

class RemoteClientSteamClient_Stub(RemoteClientSteamClient): ...
