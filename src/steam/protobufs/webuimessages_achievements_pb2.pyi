import steammessages_base_pb2 as _steammessages_base_pb2
import webuimessages_base_pb2 as _webuimessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CAchievements_GetInfo_Request(_message.Message):
    __slots__ = ("gameid",)
    GAMEID_FIELD_NUMBER: _ClassVar[int]
    gameid: int
    def __init__(self, gameid: _Optional[int] = ...) -> None: ...

class CAchievements_GetInfo_Response(_message.Message):
    __slots__ = ("achievements",)
    class Info(_message.Message):
        __slots__ = ("id", "name", "desc", "image_url_achieved", "image_url_not_achieved", "achieved", "unlock_time")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_NOT_ACHIEVED_FIELD_NUMBER: _ClassVar[int]
        ACHIEVED_FIELD_NUMBER: _ClassVar[int]
        UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        desc: str
        image_url_achieved: str
        image_url_not_achieved: str
        achieved: bool
        unlock_time: int
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., desc: _Optional[str] = ..., image_url_achieved: _Optional[str] = ..., image_url_not_achieved: _Optional[str] = ..., achieved: bool = ..., unlock_time: _Optional[int] = ...) -> None: ...
    ACHIEVEMENTS_FIELD_NUMBER: _ClassVar[int]
    achievements: _containers.RepeatedCompositeFieldContainer[CAchievements_GetInfo_Response.Info]
    def __init__(self, achievements: _Optional[_Iterable[_Union[CAchievements_GetInfo_Response.Info, _Mapping]]] = ...) -> None: ...

class Achievements(_service.service): ...

class Achievements_Stub(Achievements): ...
