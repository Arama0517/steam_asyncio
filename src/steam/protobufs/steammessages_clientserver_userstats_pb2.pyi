import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientGetUserStats(_message.Message):
    __slots__ = ("game_id", "crc_stats", "schema_local_version", "steam_id_for_user")
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    CRC_STATS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_LOCAL_VERSION_FIELD_NUMBER: _ClassVar[int]
    STEAM_ID_FOR_USER_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    crc_stats: int
    schema_local_version: int
    steam_id_for_user: int
    def __init__(self, game_id: _Optional[int] = ..., crc_stats: _Optional[int] = ..., schema_local_version: _Optional[int] = ..., steam_id_for_user: _Optional[int] = ...) -> None: ...

class CMsgClientGetUserStatsResponse(_message.Message):
    __slots__ = ("game_id", "eresult", "crc_stats", "schema", "stats", "achievement_blocks")
    class Stats(_message.Message):
        __slots__ = ("stat_id", "stat_value")
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., stat_value: _Optional[int] = ...) -> None: ...
    class Achievement_Blocks(_message.Message):
        __slots__ = ("achievement_id", "unlock_time")
        ACHIEVEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        UNLOCK_TIME_FIELD_NUMBER: _ClassVar[int]
        achievement_id: int
        unlock_time: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, achievement_id: _Optional[int] = ..., unlock_time: _Optional[_Iterable[int]] = ...) -> None: ...
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    CRC_STATS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    ACHIEVEMENT_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    eresult: int
    crc_stats: int
    schema: bytes
    stats: _containers.RepeatedCompositeFieldContainer[CMsgClientGetUserStatsResponse.Stats]
    achievement_blocks: _containers.RepeatedCompositeFieldContainer[CMsgClientGetUserStatsResponse.Achievement_Blocks]
    def __init__(self, game_id: _Optional[int] = ..., eresult: _Optional[int] = ..., crc_stats: _Optional[int] = ..., schema: _Optional[bytes] = ..., stats: _Optional[_Iterable[_Union[CMsgClientGetUserStatsResponse.Stats, _Mapping]]] = ..., achievement_blocks: _Optional[_Iterable[_Union[CMsgClientGetUserStatsResponse.Achievement_Blocks, _Mapping]]] = ...) -> None: ...

class CMsgClientStoreUserStatsResponse(_message.Message):
    __slots__ = ("game_id", "eresult", "crc_stats", "stats_failed_validation", "stats_out_of_date")
    class Stats_Failed_Validation(_message.Message):
        __slots__ = ("stat_id", "reverted_stat_value")
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        REVERTED_STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        reverted_stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., reverted_stat_value: _Optional[int] = ...) -> None: ...
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    CRC_STATS_FIELD_NUMBER: _ClassVar[int]
    STATS_FAILED_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    STATS_OUT_OF_DATE_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    eresult: int
    crc_stats: int
    stats_failed_validation: _containers.RepeatedCompositeFieldContainer[CMsgClientStoreUserStatsResponse.Stats_Failed_Validation]
    stats_out_of_date: bool
    def __init__(self, game_id: _Optional[int] = ..., eresult: _Optional[int] = ..., crc_stats: _Optional[int] = ..., stats_failed_validation: _Optional[_Iterable[_Union[CMsgClientStoreUserStatsResponse.Stats_Failed_Validation, _Mapping]]] = ..., stats_out_of_date: bool = ...) -> None: ...

class CMsgClientStoreUserStats2(_message.Message):
    __slots__ = ("game_id", "settor_steam_id", "settee_steam_id", "crc_stats", "explicit_reset", "stats")
    class Stats(_message.Message):
        __slots__ = ("stat_id", "stat_value")
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., stat_value: _Optional[int] = ...) -> None: ...
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    SETTOR_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    SETTEE_STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    CRC_STATS_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_RESET_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    settor_steam_id: int
    settee_steam_id: int
    crc_stats: int
    explicit_reset: bool
    stats: _containers.RepeatedCompositeFieldContainer[CMsgClientStoreUserStats2.Stats]
    def __init__(self, game_id: _Optional[int] = ..., settor_steam_id: _Optional[int] = ..., settee_steam_id: _Optional[int] = ..., crc_stats: _Optional[int] = ..., explicit_reset: bool = ..., stats: _Optional[_Iterable[_Union[CMsgClientStoreUserStats2.Stats, _Mapping]]] = ...) -> None: ...

class CMsgClientStatsUpdated(_message.Message):
    __slots__ = ("steam_id", "game_id", "crc_stats", "updated_stats")
    class Updated_Stats(_message.Message):
        __slots__ = ("stat_id", "stat_value")
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., stat_value: _Optional[int] = ...) -> None: ...
    STEAM_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    CRC_STATS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_STATS_FIELD_NUMBER: _ClassVar[int]
    steam_id: int
    game_id: int
    crc_stats: int
    updated_stats: _containers.RepeatedCompositeFieldContainer[CMsgClientStatsUpdated.Updated_Stats]
    def __init__(self, steam_id: _Optional[int] = ..., game_id: _Optional[int] = ..., crc_stats: _Optional[int] = ..., updated_stats: _Optional[_Iterable[_Union[CMsgClientStatsUpdated.Updated_Stats, _Mapping]]] = ...) -> None: ...

class CMsgClientStoreUserStats(_message.Message):
    __slots__ = ("game_id", "explicit_reset", "stats_to_store")
    class Stats_To_Store(_message.Message):
        __slots__ = ("stat_id", "stat_value")
        STAT_ID_FIELD_NUMBER: _ClassVar[int]
        STAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        stat_id: int
        stat_value: int
        def __init__(self, stat_id: _Optional[int] = ..., stat_value: _Optional[int] = ...) -> None: ...
    GAME_ID_FIELD_NUMBER: _ClassVar[int]
    EXPLICIT_RESET_FIELD_NUMBER: _ClassVar[int]
    STATS_TO_STORE_FIELD_NUMBER: _ClassVar[int]
    game_id: int
    explicit_reset: bool
    stats_to_store: _containers.RepeatedCompositeFieldContainer[CMsgClientStoreUserStats.Stats_To_Store]
    def __init__(self, game_id: _Optional[int] = ..., explicit_reset: bool = ..., stats_to_store: _Optional[_Iterable[_Union[CMsgClientStoreUserStats.Stats_To_Store, _Mapping]]] = ...) -> None: ...
