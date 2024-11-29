import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CParties_JoinParty_Request(_message.Message):
    __slots__ = ("steamid", "beacon_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    beacon_id: int
    def __init__(self, steamid: _Optional[int] = ..., beacon_id: _Optional[int] = ...) -> None: ...

class CParties_JoinParty_Response(_message.Message):
    __slots__ = ("beacon_id", "connect_string")
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECT_STRING_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    connect_string: str
    def __init__(self, beacon_id: _Optional[int] = ..., connect_string: _Optional[str] = ...) -> None: ...

class CParties_BeaconLocation(_message.Message):
    __slots__ = ("location_type", "location_id")
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    location_type: int
    location_id: int
    def __init__(self, location_type: _Optional[int] = ..., location_id: _Optional[int] = ...) -> None: ...

class CParties_CreateBeacon_Request(_message.Message):
    __slots__ = ("appid", "num_open_slots", "locations", "connect_string", "metadata")
    APPID_FIELD_NUMBER: _ClassVar[int]
    NUM_OPEN_SLOTS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    CONNECT_STRING_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    appid: int
    num_open_slots: int
    locations: _containers.RepeatedCompositeFieldContainer[CParties_BeaconLocation]
    connect_string: str
    metadata: str
    def __init__(self, appid: _Optional[int] = ..., num_open_slots: _Optional[int] = ..., locations: _Optional[_Iterable[_Union[CParties_BeaconLocation, _Mapping]]] = ..., connect_string: _Optional[str] = ..., metadata: _Optional[str] = ...) -> None: ...

class CParties_CreateBeacon_Response(_message.Message):
    __slots__ = ("beacon_id",)
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    def __init__(self, beacon_id: _Optional[int] = ...) -> None: ...

class CParties_OnReservationCompleted_Request(_message.Message):
    __slots__ = ("beacon_id", "user_steamid")
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    USER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    user_steamid: int
    def __init__(self, beacon_id: _Optional[int] = ..., user_steamid: _Optional[int] = ...) -> None: ...

class CParties_OnReservationCompleted_Response(_message.Message):
    __slots__ = ("beacon_id",)
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    def __init__(self, beacon_id: _Optional[int] = ...) -> None: ...

class CParties_CancelReservation_Request(_message.Message):
    __slots__ = ("beacon_id", "user_steamid")
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    USER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    user_steamid: int
    def __init__(self, beacon_id: _Optional[int] = ..., user_steamid: _Optional[int] = ...) -> None: ...

class CParties_CancelReservation_Response(_message.Message):
    __slots__ = ("beacon_id",)
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    def __init__(self, beacon_id: _Optional[int] = ...) -> None: ...

class CParties_ChangeNumOpenSlots_Request(_message.Message):
    __slots__ = ("beacon_id", "num_open_slots")
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_OPEN_SLOTS_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    num_open_slots: int
    def __init__(self, beacon_id: _Optional[int] = ..., num_open_slots: _Optional[int] = ...) -> None: ...

class CParties_ChangeNumOpenSlots_Response(_message.Message):
    __slots__ = ("beacon_id",)
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    def __init__(self, beacon_id: _Optional[int] = ...) -> None: ...

class CParties_DestroyBeacon_Request(_message.Message):
    __slots__ = ("beacon_id",)
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    def __init__(self, beacon_id: _Optional[int] = ...) -> None: ...

class CParties_DestroyBeacon_Response(_message.Message):
    __slots__ = ("beacon_id",)
    BEACON_ID_FIELD_NUMBER: _ClassVar[int]
    beacon_id: int
    def __init__(self, beacon_id: _Optional[int] = ...) -> None: ...

class Parties(_service.service): ...

class Parties_Stub(Parties): ...
