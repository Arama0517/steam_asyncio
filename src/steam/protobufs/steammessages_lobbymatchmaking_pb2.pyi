import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ELobbyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ELobbyStatusInvalid: _ClassVar[ELobbyStatus]
    k_ELobbyStatusExists: _ClassVar[ELobbyStatus]
    k_ELobbyStatusDoesNotExist: _ClassVar[ELobbyStatus]
    k_ELobbyStatusNotAMember: _ClassVar[ELobbyStatus]
k_ELobbyStatusInvalid: ELobbyStatus
k_ELobbyStatusExists: ELobbyStatus
k_ELobbyStatusDoesNotExist: ELobbyStatus
k_ELobbyStatusNotAMember: ELobbyStatus

class LobbyMatchmakingLegacy_GetLobbyStatus_Request(_message.Message):
    __slots__ = ("app_id", "steamid_lobby", "claim_ownership", "claim_membership", "version_num")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    CLAIM_OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    CLAIM_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    VERSION_NUM_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steamid_lobby: int
    claim_ownership: bool
    claim_membership: bool
    version_num: int
    def __init__(self, app_id: _Optional[int] = ..., steamid_lobby: _Optional[int] = ..., claim_ownership: bool = ..., claim_membership: bool = ..., version_num: _Optional[int] = ...) -> None: ...

class LobbyMatchmakingLegacy_GetLobbyStatus_Response(_message.Message):
    __slots__ = ("app_id", "steamid_lobby", "lobby_status")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_LOBBY_FIELD_NUMBER: _ClassVar[int]
    LOBBY_STATUS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    steamid_lobby: int
    lobby_status: ELobbyStatus
    def __init__(self, app_id: _Optional[int] = ..., steamid_lobby: _Optional[int] = ..., lobby_status: _Optional[_Union[ELobbyStatus, str]] = ...) -> None: ...

class LobbyMatchmakingLegacy(_service.service): ...

class LobbyMatchmakingLegacy_Stub(LobbyMatchmakingLegacy): ...
