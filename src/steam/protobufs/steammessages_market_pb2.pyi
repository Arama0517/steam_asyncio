import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CEconMarket_IsMarketplaceAllowed_Request(_message.Message):
    __slots__ = ("webcookie",)
    WEBCOOKIE_FIELD_NUMBER: _ClassVar[int]
    webcookie: str
    def __init__(self, webcookie: _Optional[str] = ...) -> None: ...

class CEconMarket_IsMarketplaceAllowed_Response(_message.Message):
    __slots__ = ("allowed", "reason", "allowed_at_time", "steamguard_required_days", "forms_requested", "forms_require_verification", "new_device_cooldown_days")
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_AT_TIME_FIELD_NUMBER: _ClassVar[int]
    STEAMGUARD_REQUIRED_DAYS_FIELD_NUMBER: _ClassVar[int]
    FORMS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    FORMS_REQUIRE_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    NEW_DEVICE_COOLDOWN_DAYS_FIELD_NUMBER: _ClassVar[int]
    allowed: bool
    reason: int
    allowed_at_time: int
    steamguard_required_days: int
    forms_requested: bool
    forms_require_verification: bool
    new_device_cooldown_days: int
    def __init__(self, allowed: bool = ..., reason: _Optional[int] = ..., allowed_at_time: _Optional[int] = ..., steamguard_required_days: _Optional[int] = ..., forms_requested: bool = ..., forms_require_verification: bool = ..., new_device_cooldown_days: _Optional[int] = ...) -> None: ...

class EconMarket(_service.service): ...

class EconMarket_Stub(EconMarket): ...
