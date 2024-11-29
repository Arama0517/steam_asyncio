import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EGameSearchAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EGameSearchAction_None: _ClassVar[EGameSearchAction]
    k_EGameSearchAction_Accept: _ClassVar[EGameSearchAction]
    k_EGameSearchAction_Decline: _ClassVar[EGameSearchAction]
    k_EGameSearchAction_Cancel: _ClassVar[EGameSearchAction]

class EGameSearchResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EGameSearchResult_Invalid: _ClassVar[EGameSearchResult]
    k_EGameSearchResult_SearchInProgress: _ClassVar[EGameSearchResult]
    k_EGameSearchResult_SearchFailedNoHosts: _ClassVar[EGameSearchResult]
    k_EGameSearchResult_SearchGameFound: _ClassVar[EGameSearchResult]
    k_EGameSearchResult_SearchCompleteAccepted: _ClassVar[EGameSearchResult]
    k_EGameSearchResult_SearchCompleteDeclined: _ClassVar[EGameSearchResult]
    k_EGameSearchResult_SearchCanceled: _ClassVar[EGameSearchResult]
k_EGameSearchAction_None: EGameSearchAction
k_EGameSearchAction_Accept: EGameSearchAction
k_EGameSearchAction_Decline: EGameSearchAction
k_EGameSearchAction_Cancel: EGameSearchAction
k_EGameSearchResult_Invalid: EGameSearchResult
k_EGameSearchResult_SearchInProgress: EGameSearchResult
k_EGameSearchResult_SearchFailedNoHosts: EGameSearchResult
k_EGameSearchResult_SearchGameFound: EGameSearchResult
k_EGameSearchResult_SearchCompleteAccepted: EGameSearchResult
k_EGameSearchResult_SearchCompleteDeclined: EGameSearchResult
k_EGameSearchResult_SearchCanceled: EGameSearchResult

class GameSearchParam(_message.Message):
    __slots__ = ("key_name", "value")
    KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key_name: str
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, key_name: _Optional[str] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...

class CQueuedMatchmaking_SearchForGame_Request(_message.Message):
    __slots__ = ("appid", "action", "params", "player_min", "player_max", "steamidlobby", "searchid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MIN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MAX_FIELD_NUMBER: _ClassVar[int]
    STEAMIDLOBBY_FIELD_NUMBER: _ClassVar[int]
    SEARCHID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    action: EGameSearchAction
    params: _containers.RepeatedCompositeFieldContainer[GameSearchParam]
    player_min: int
    player_max: int
    steamidlobby: int
    searchid: int
    def __init__(self, appid: _Optional[int] = ..., action: _Optional[_Union[EGameSearchAction, str]] = ..., params: _Optional[_Iterable[_Union[GameSearchParam, _Mapping]]] = ..., player_min: _Optional[int] = ..., player_max: _Optional[int] = ..., steamidlobby: _Optional[int] = ..., searchid: _Optional[int] = ...) -> None: ...

class CQueuedMatchmaking_SearchForGame_Response(_message.Message):
    __slots__ = ("gamesearchresult", "searchid", "seconds_time_estimate", "poll_frequency", "count_searching", "players_in_match", "players_accepted", "connect_string", "steamidhost", "rtime_match_made", "rtime_now", "steamid_canceled_search")
    GAMESEARCHRESULT_FIELD_NUMBER: _ClassVar[int]
    SEARCHID_FIELD_NUMBER: _ClassVar[int]
    SECONDS_TIME_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    POLL_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    COUNT_SEARCHING_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_IN_MATCH_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    CONNECT_STRING_FIELD_NUMBER: _ClassVar[int]
    STEAMIDHOST_FIELD_NUMBER: _ClassVar[int]
    RTIME_MATCH_MADE_FIELD_NUMBER: _ClassVar[int]
    RTIME_NOW_FIELD_NUMBER: _ClassVar[int]
    STEAMID_CANCELED_SEARCH_FIELD_NUMBER: _ClassVar[int]
    gamesearchresult: EGameSearchResult
    searchid: int
    seconds_time_estimate: int
    poll_frequency: int
    count_searching: int
    players_in_match: int
    players_accepted: int
    connect_string: str
    steamidhost: int
    rtime_match_made: int
    rtime_now: int
    steamid_canceled_search: int
    def __init__(self, gamesearchresult: _Optional[_Union[EGameSearchResult, str]] = ..., searchid: _Optional[int] = ..., seconds_time_estimate: _Optional[int] = ..., poll_frequency: _Optional[int] = ..., count_searching: _Optional[int] = ..., players_in_match: _Optional[int] = ..., players_accepted: _Optional[int] = ..., connect_string: _Optional[str] = ..., steamidhost: _Optional[int] = ..., rtime_match_made: _Optional[int] = ..., rtime_now: _Optional[int] = ..., steamid_canceled_search: _Optional[int] = ...) -> None: ...

class CQueuedMatchmakingGameHost_SearchForPlayers_Request(_message.Message):
    __slots__ = ("appid", "action", "params", "player_min", "player_max", "player_max_team_size", "connection_string", "searchid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MIN_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MAX_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MAX_TEAM_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STRING_FIELD_NUMBER: _ClassVar[int]
    SEARCHID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    action: EGameSearchAction
    params: _containers.RepeatedCompositeFieldContainer[GameSearchParam]
    player_min: int
    player_max: int
    player_max_team_size: int
    connection_string: str
    searchid: int
    def __init__(self, appid: _Optional[int] = ..., action: _Optional[_Union[EGameSearchAction, str]] = ..., params: _Optional[_Iterable[_Union[GameSearchParam, _Mapping]]] = ..., player_min: _Optional[int] = ..., player_max: _Optional[int] = ..., player_max_team_size: _Optional[int] = ..., connection_string: _Optional[str] = ..., searchid: _Optional[int] = ...) -> None: ...

class PlayerFound(_message.Message):
    __slots__ = ("steamid", "action", "params", "team_number")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    TEAM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    action: EGameSearchAction
    params: _containers.RepeatedCompositeFieldContainer[GameSearchParam]
    team_number: int
    def __init__(self, steamid: _Optional[int] = ..., action: _Optional[_Union[EGameSearchAction, str]] = ..., params: _Optional[_Iterable[_Union[GameSearchParam, _Mapping]]] = ..., team_number: _Optional[int] = ...) -> None: ...

class CQueuedMatchmakingGameHost_SearchForPlayers_Response(_message.Message):
    __slots__ = ("gamesearchresult", "searchid", "poll_frequency", "matchid", "players", "rtime_match_made", "rtime_now")
    GAMESEARCHRESULT_FIELD_NUMBER: _ClassVar[int]
    SEARCHID_FIELD_NUMBER: _ClassVar[int]
    POLL_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    RTIME_MATCH_MADE_FIELD_NUMBER: _ClassVar[int]
    RTIME_NOW_FIELD_NUMBER: _ClassVar[int]
    gamesearchresult: EGameSearchResult
    searchid: int
    poll_frequency: int
    matchid: int
    players: _containers.RepeatedCompositeFieldContainer[PlayerFound]
    rtime_match_made: int
    rtime_now: int
    def __init__(self, gamesearchresult: _Optional[_Union[EGameSearchResult, str]] = ..., searchid: _Optional[int] = ..., poll_frequency: _Optional[int] = ..., matchid: _Optional[int] = ..., players: _Optional[_Iterable[_Union[PlayerFound, _Mapping]]] = ..., rtime_match_made: _Optional[int] = ..., rtime_now: _Optional[int] = ...) -> None: ...

class PlayerResult(_message.Message):
    __slots__ = ("steamid", "value")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    value: int
    def __init__(self, steamid: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class CQueuedMatchmakingGameHost_SubmitPlayerResult_Request(_message.Message):
    __slots__ = ("appid", "matchid", "player_results")
    APPID_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    PLAYER_RESULTS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    matchid: int
    player_results: _containers.RepeatedCompositeFieldContainer[PlayerResult]
    def __init__(self, appid: _Optional[int] = ..., matchid: _Optional[int] = ..., player_results: _Optional[_Iterable[_Union[PlayerResult, _Mapping]]] = ...) -> None: ...

class CQueuedMatchmakingGameHost_SubmitPlayerResult_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CQueuedMatchmakingGameHost_EndGame_Request(_message.Message):
    __slots__ = ("appid", "matchid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    MATCHID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    matchid: int
    def __init__(self, appid: _Optional[int] = ..., matchid: _Optional[int] = ...) -> None: ...

class CQueuedMatchmakingGameHost_EndGame_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueuedMatchmaking(_service.service): ...

class QueuedMatchmaking_Stub(QueuedMatchmaking): ...

class QueuedMatchmakingGameHost(_service.service): ...

class QueuedMatchmakingGameHost_Stub(QueuedMatchmakingGameHost): ...
