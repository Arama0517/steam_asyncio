import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CGameNotifications_Variable(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CGameNotifications_LocalizedText(_message.Message):
    __slots__ = ("token", "variables", "rendered_text")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    RENDERED_TEXT_FIELD_NUMBER: _ClassVar[int]
    token: str
    variables: _containers.RepeatedCompositeFieldContainer[CGameNotifications_Variable]
    rendered_text: str
    def __init__(self, token: _Optional[str] = ..., variables: _Optional[_Iterable[_Union[CGameNotifications_Variable, _Mapping]]] = ..., rendered_text: _Optional[str] = ...) -> None: ...

class CGameNotifications_UserStatus(_message.Message):
    __slots__ = ("steamid", "state", "title", "message")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    state: str
    title: CGameNotifications_LocalizedText
    message: CGameNotifications_LocalizedText
    def __init__(self, steamid: _Optional[int] = ..., state: _Optional[str] = ..., title: _Optional[_Union[CGameNotifications_LocalizedText, _Mapping]] = ..., message: _Optional[_Union[CGameNotifications_LocalizedText, _Mapping]] = ...) -> None: ...

class CGameNotifications_CreateSession_Request(_message.Message):
    __slots__ = ("appid", "context", "title", "users", "steamid")
    APPID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    context: int
    title: CGameNotifications_LocalizedText
    users: _containers.RepeatedCompositeFieldContainer[CGameNotifications_UserStatus]
    steamid: int
    def __init__(self, appid: _Optional[int] = ..., context: _Optional[int] = ..., title: _Optional[_Union[CGameNotifications_LocalizedText, _Mapping]] = ..., users: _Optional[_Iterable[_Union[CGameNotifications_UserStatus, _Mapping]]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CGameNotifications_CreateSession_Response(_message.Message):
    __slots__ = ("sessionid",)
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionid: int
    def __init__(self, sessionid: _Optional[int] = ...) -> None: ...

class CGameNotifications_DeleteSession_Request(_message.Message):
    __slots__ = ("sessionid", "appid", "steamid")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    sessionid: int
    appid: int
    steamid: int
    def __init__(self, sessionid: _Optional[int] = ..., appid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CGameNotifications_DeleteSession_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameNotifications_UpdateSession_Request(_message.Message):
    __slots__ = ("sessionid", "appid", "title", "users", "steamid")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    sessionid: int
    appid: int
    title: CGameNotifications_LocalizedText
    users: _containers.RepeatedCompositeFieldContainer[CGameNotifications_UserStatus]
    steamid: int
    def __init__(self, sessionid: _Optional[int] = ..., appid: _Optional[int] = ..., title: _Optional[_Union[CGameNotifications_LocalizedText, _Mapping]] = ..., users: _Optional[_Iterable[_Union[CGameNotifications_UserStatus, _Mapping]]] = ..., steamid: _Optional[int] = ...) -> None: ...

class CGameNotifications_UpdateSession_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameNotifications_EnumerateSessions_Request(_message.Message):
    __slots__ = ("appid", "include_all_user_messages", "include_auth_user_message", "language")
    APPID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_USER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AUTH_USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    include_all_user_messages: bool
    include_auth_user_message: bool
    language: str
    def __init__(self, appid: _Optional[int] = ..., include_all_user_messages: bool = ..., include_auth_user_message: bool = ..., language: _Optional[str] = ...) -> None: ...

class CGameNotifications_Session(_message.Message):
    __slots__ = ("sessionid", "appid", "context", "title", "time_created", "time_updated", "user_status")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TIME_CREATED_FIELD_NUMBER: _ClassVar[int]
    TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
    USER_STATUS_FIELD_NUMBER: _ClassVar[int]
    sessionid: int
    appid: int
    context: int
    title: CGameNotifications_LocalizedText
    time_created: int
    time_updated: int
    user_status: _containers.RepeatedCompositeFieldContainer[CGameNotifications_UserStatus]
    def __init__(self, sessionid: _Optional[int] = ..., appid: _Optional[int] = ..., context: _Optional[int] = ..., title: _Optional[_Union[CGameNotifications_LocalizedText, _Mapping]] = ..., time_created: _Optional[int] = ..., time_updated: _Optional[int] = ..., user_status: _Optional[_Iterable[_Union[CGameNotifications_UserStatus, _Mapping]]] = ...) -> None: ...

class CGameNotifications_EnumerateSessions_Response(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[CGameNotifications_Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[CGameNotifications_Session, _Mapping]]] = ...) -> None: ...

class CGameNotifications_GetSessionDetails_Request(_message.Message):
    __slots__ = ("sessions", "appid", "language")
    class RequestedSession(_message.Message):
        __slots__ = ("sessionid", "include_auth_user_message")
        SESSIONID_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_AUTH_USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        sessionid: int
        include_auth_user_message: bool
        def __init__(self, sessionid: _Optional[int] = ..., include_auth_user_message: bool = ...) -> None: ...
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[CGameNotifications_GetSessionDetails_Request.RequestedSession]
    appid: int
    language: str
    def __init__(self, sessions: _Optional[_Iterable[_Union[CGameNotifications_GetSessionDetails_Request.RequestedSession, _Mapping]]] = ..., appid: _Optional[int] = ..., language: _Optional[str] = ...) -> None: ...

class CGameNotifications_GetSessionDetails_Response(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[CGameNotifications_Session]
    def __init__(self, sessions: _Optional[_Iterable[_Union[CGameNotifications_Session, _Mapping]]] = ...) -> None: ...

class GameNotificationSettings(_message.Message):
    __slots__ = ("appid", "allow_notifications")
    APPID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    allow_notifications: bool
    def __init__(self, appid: _Optional[int] = ..., allow_notifications: bool = ...) -> None: ...

class CGameNotifications_UpdateNotificationSettings_Request(_message.Message):
    __slots__ = ("game_notification_settings",)
    GAME_NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    game_notification_settings: _containers.RepeatedCompositeFieldContainer[GameNotificationSettings]
    def __init__(self, game_notification_settings: _Optional[_Iterable[_Union[GameNotificationSettings, _Mapping]]] = ...) -> None: ...

class CGameNotifications_UpdateNotificationSettings_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CGameNotifications_OnNotificationsRequested_Notification(_message.Message):
    __slots__ = ("steamid", "appid")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ...) -> None: ...

class CGameNotifications_OnUserStatusChanged_Notification(_message.Message):
    __slots__ = ("steamid", "sessionid", "appid", "status", "removed")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    sessionid: int
    appid: int
    status: CGameNotifications_UserStatus
    removed: bool
    def __init__(self, steamid: _Optional[int] = ..., sessionid: _Optional[int] = ..., appid: _Optional[int] = ..., status: _Optional[_Union[CGameNotifications_UserStatus, _Mapping]] = ..., removed: bool = ...) -> None: ...

class GameNotifications(_service.service): ...

class GameNotifications_Stub(GameNotifications): ...

class GameNotificationsClient(_service.service): ...

class GameNotificationsClient_Stub(GameNotificationsClient): ...
