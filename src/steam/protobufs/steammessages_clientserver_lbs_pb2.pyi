import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientLBSSetScore(_message.Message):
    __slots__ = ("app_id", "leaderboard_id", "score", "details", "upload_score_method")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_SCORE_METHOD_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    leaderboard_id: int
    score: int
    details: bytes
    upload_score_method: int
    def __init__(self, app_id: _Optional[int] = ..., leaderboard_id: _Optional[int] = ..., score: _Optional[int] = ..., details: _Optional[bytes] = ..., upload_score_method: _Optional[int] = ...) -> None: ...

class CMsgClientLBSSetScoreResponse(_message.Message):
    __slots__ = ("eresult", "leaderboard_entry_count", "score_changed", "global_rank_previous", "global_rank_new")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCORE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_RANK_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_RANK_NEW_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    leaderboard_entry_count: int
    score_changed: bool
    global_rank_previous: int
    global_rank_new: int
    def __init__(self, eresult: _Optional[int] = ..., leaderboard_entry_count: _Optional[int] = ..., score_changed: bool = ..., global_rank_previous: _Optional[int] = ..., global_rank_new: _Optional[int] = ...) -> None: ...

class CMsgClientLBSSetUGC(_message.Message):
    __slots__ = ("app_id", "leaderboard_id", "ugc_id")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    UGC_ID_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    leaderboard_id: int
    ugc_id: int
    def __init__(self, app_id: _Optional[int] = ..., leaderboard_id: _Optional[int] = ..., ugc_id: _Optional[int] = ...) -> None: ...

class CMsgClientLBSSetUGCResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientLBSFindOrCreateLB(_message.Message):
    __slots__ = ("app_id", "leaderboard_sort_method", "leaderboard_display_type", "create_if_not_found", "leaderboard_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_SORT_METHOD_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_DISPLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATE_IF_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    leaderboard_sort_method: int
    leaderboard_display_type: int
    create_if_not_found: bool
    leaderboard_name: str
    def __init__(self, app_id: _Optional[int] = ..., leaderboard_sort_method: _Optional[int] = ..., leaderboard_display_type: _Optional[int] = ..., create_if_not_found: bool = ..., leaderboard_name: _Optional[str] = ...) -> None: ...

class CMsgClientLBSFindOrCreateLBResponse(_message.Message):
    __slots__ = ("eresult", "leaderboard_id", "leaderboard_entry_count", "leaderboard_sort_method", "leaderboard_display_type", "leaderboard_name")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_SORT_METHOD_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_DISPLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_NAME_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    leaderboard_id: int
    leaderboard_entry_count: int
    leaderboard_sort_method: int
    leaderboard_display_type: int
    leaderboard_name: str
    def __init__(self, eresult: _Optional[int] = ..., leaderboard_id: _Optional[int] = ..., leaderboard_entry_count: _Optional[int] = ..., leaderboard_sort_method: _Optional[int] = ..., leaderboard_display_type: _Optional[int] = ..., leaderboard_name: _Optional[str] = ...) -> None: ...

class CMsgClientLBSGetLBEntries(_message.Message):
    __slots__ = ("app_id", "leaderboard_id", "range_start", "range_end", "leaderboard_data_request", "steamids")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    RANGE_START_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_DATA_REQUEST_FIELD_NUMBER: _ClassVar[int]
    STEAMIDS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    leaderboard_id: int
    range_start: int
    range_end: int
    leaderboard_data_request: int
    steamids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, app_id: _Optional[int] = ..., leaderboard_id: _Optional[int] = ..., range_start: _Optional[int] = ..., range_end: _Optional[int] = ..., leaderboard_data_request: _Optional[int] = ..., steamids: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientLBSGetLBEntriesResponse(_message.Message):
    __slots__ = ("eresult", "leaderboard_entry_count", "entries")
    class Entry(_message.Message):
        __slots__ = ("steam_id_user", "global_rank", "score", "details", "ugc_id")
        STEAM_ID_USER_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_RANK_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        UGC_ID_FIELD_NUMBER: _ClassVar[int]
        steam_id_user: int
        global_rank: int
        score: int
        details: bytes
        ugc_id: int
        def __init__(self, steam_id_user: _Optional[int] = ..., global_rank: _Optional[int] = ..., score: _Optional[int] = ..., details: _Optional[bytes] = ..., ugc_id: _Optional[int] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    LEADERBOARD_ENTRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    leaderboard_entry_count: int
    entries: _containers.RepeatedCompositeFieldContainer[CMsgClientLBSGetLBEntriesResponse.Entry]
    def __init__(self, eresult: _Optional[int] = ..., leaderboard_entry_count: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[CMsgClientLBSGetLBEntriesResponse.Entry, _Mapping]]] = ...) -> None: ...
