import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EFamilyGroupRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EFamilyGroupRole_None: _ClassVar[EFamilyGroupRole]
    k_EFamilyGroupRole_Adult: _ClassVar[EFamilyGroupRole]
    k_EFamilyGroupRole_Child: _ClassVar[EFamilyGroupRole]
    k_EFamilyGroupRole_MAX: _ClassVar[EFamilyGroupRole]

class EFamilyGroupsTwoFactorMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EFamilyGroupsTwoFactorMethodNone: _ClassVar[EFamilyGroupsTwoFactorMethod]
    k_EFamilyGroupsTwoFactorMethodMobile: _ClassVar[EFamilyGroupsTwoFactorMethod]
    k_EFamilyGroupsTwoFactorMethodEmail: _ClassVar[EFamilyGroupsTwoFactorMethod]

class EPurchaseRequestAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EPurchaseRequestAction_None: _ClassVar[EPurchaseRequestAction]
    k_EPurchaseRequestAction_Decline: _ClassVar[EPurchaseRequestAction]
    k_EPurchaseRequestAction_Purchased: _ClassVar[EPurchaseRequestAction]
    k_EPurchaseRequestAction_Abandoned: _ClassVar[EPurchaseRequestAction]
    k_EPurchaseRequestAction_Cancel: _ClassVar[EPurchaseRequestAction]
    k_EPurchaseRequestAction_MAX: _ClassVar[EPurchaseRequestAction]

class EFamilyGroupChangeLogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_InvalidChangeType: _ClassVar[EFamilyGroupChangeLogType]
    k_FamilyGroupCreated: _ClassVar[EFamilyGroupChangeLogType]
    k_FamilyGroupModified: _ClassVar[EFamilyGroupChangeLogType]
    k_FamilyGroupDeleted: _ClassVar[EFamilyGroupChangeLogType]
    k_AccountInvited: _ClassVar[EFamilyGroupChangeLogType]
    k_InviteDeniedByGroupSize: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinedFamilyGroup: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinDeniedByRegionMismatch: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinDeniedByMissingIpAddress: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinDeniedByFamilyCooldown: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinDeniedByUserCooldown: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinDeniedByOtherGroup: _ClassVar[EFamilyGroupChangeLogType]
    k_AccountRemoved: _ClassVar[EFamilyGroupChangeLogType]
    k_InviteCanceled: _ClassVar[EFamilyGroupChangeLogType]
    k_PurchaseRequested: _ClassVar[EFamilyGroupChangeLogType]
    k_ParentalSettingsEnabled: _ClassVar[EFamilyGroupChangeLogType]
    k_ParentalSettingsDisabled: _ClassVar[EFamilyGroupChangeLogType]
    k_ParentalSettingsChanged: _ClassVar[EFamilyGroupChangeLogType]
    k_FamilyCooldownOverridesChanged: _ClassVar[EFamilyGroupChangeLogType]
    k_PurchaseRequestCanceled: _ClassVar[EFamilyGroupChangeLogType]
    k_PurchaseRequestApproved: _ClassVar[EFamilyGroupChangeLogType]
    k_PurchaseRequestDeclined: _ClassVar[EFamilyGroupChangeLogType]
    k_CooldownSkipConsumed: _ClassVar[EFamilyGroupChangeLogType]
    k_FamilyGroupRestored: _ClassVar[EFamilyGroupChangeLogType]
    k_JoinDenied: _ClassVar[EFamilyGroupChangeLogType]
    k_SupportForceAcceptedInvite: _ClassVar[EFamilyGroupChangeLogType]

class ESharedLibraryExcludeReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_ESharedLibrary_Included: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_AppExcluded_ByPartner: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_FreeGame: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicensePrivate: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_AppExcluded_WrongAppType: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_AppExcluded_NonrefundableDLC: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_AppExcluded_UnreleasedApp: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_AppExcluded_ParentAppExcluded: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_ByPartner: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_Special: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_Dev: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_FreeWeekend: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_Invalid: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_RecurringLicense: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_WrongLicenseType: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_MasterSub: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_PackageExcluded_NoShareableApps: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_PaymentMasterSub: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_PaymentFamilyGroup: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_PaymentAuthorizedDevice: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_PaymentAutoGrant: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_FlagPending: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_FlagPendingRefund: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_FlagBorrowed: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_FlagAutoGrant: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_FlagTimedTrial: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_FreeSub: _ClassVar[ESharedLibraryExcludeReason]
    k_ESharedLibrary_LicenseExcluded_Inactive: _ClassVar[ESharedLibraryExcludeReason]
k_EFamilyGroupRole_None: EFamilyGroupRole
k_EFamilyGroupRole_Adult: EFamilyGroupRole
k_EFamilyGroupRole_Child: EFamilyGroupRole
k_EFamilyGroupRole_MAX: EFamilyGroupRole
k_EFamilyGroupsTwoFactorMethodNone: EFamilyGroupsTwoFactorMethod
k_EFamilyGroupsTwoFactorMethodMobile: EFamilyGroupsTwoFactorMethod
k_EFamilyGroupsTwoFactorMethodEmail: EFamilyGroupsTwoFactorMethod
k_EPurchaseRequestAction_None: EPurchaseRequestAction
k_EPurchaseRequestAction_Decline: EPurchaseRequestAction
k_EPurchaseRequestAction_Purchased: EPurchaseRequestAction
k_EPurchaseRequestAction_Abandoned: EPurchaseRequestAction
k_EPurchaseRequestAction_Cancel: EPurchaseRequestAction
k_EPurchaseRequestAction_MAX: EPurchaseRequestAction
k_InvalidChangeType: EFamilyGroupChangeLogType
k_FamilyGroupCreated: EFamilyGroupChangeLogType
k_FamilyGroupModified: EFamilyGroupChangeLogType
k_FamilyGroupDeleted: EFamilyGroupChangeLogType
k_AccountInvited: EFamilyGroupChangeLogType
k_InviteDeniedByGroupSize: EFamilyGroupChangeLogType
k_JoinedFamilyGroup: EFamilyGroupChangeLogType
k_JoinDeniedByRegionMismatch: EFamilyGroupChangeLogType
k_JoinDeniedByMissingIpAddress: EFamilyGroupChangeLogType
k_JoinDeniedByFamilyCooldown: EFamilyGroupChangeLogType
k_JoinDeniedByUserCooldown: EFamilyGroupChangeLogType
k_JoinDeniedByOtherGroup: EFamilyGroupChangeLogType
k_AccountRemoved: EFamilyGroupChangeLogType
k_InviteCanceled: EFamilyGroupChangeLogType
k_PurchaseRequested: EFamilyGroupChangeLogType
k_ParentalSettingsEnabled: EFamilyGroupChangeLogType
k_ParentalSettingsDisabled: EFamilyGroupChangeLogType
k_ParentalSettingsChanged: EFamilyGroupChangeLogType
k_FamilyCooldownOverridesChanged: EFamilyGroupChangeLogType
k_PurchaseRequestCanceled: EFamilyGroupChangeLogType
k_PurchaseRequestApproved: EFamilyGroupChangeLogType
k_PurchaseRequestDeclined: EFamilyGroupChangeLogType
k_CooldownSkipConsumed: EFamilyGroupChangeLogType
k_FamilyGroupRestored: EFamilyGroupChangeLogType
k_JoinDenied: EFamilyGroupChangeLogType
k_SupportForceAcceptedInvite: EFamilyGroupChangeLogType
k_ESharedLibrary_Included: ESharedLibraryExcludeReason
k_ESharedLibrary_AppExcluded_ByPartner: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded: ESharedLibraryExcludeReason
k_ESharedLibrary_FreeGame: ESharedLibraryExcludeReason
k_ESharedLibrary_LicensePrivate: ESharedLibraryExcludeReason
k_ESharedLibrary_AppExcluded_WrongAppType: ESharedLibraryExcludeReason
k_ESharedLibrary_AppExcluded_NonrefundableDLC: ESharedLibraryExcludeReason
k_ESharedLibrary_AppExcluded_UnreleasedApp: ESharedLibraryExcludeReason
k_ESharedLibrary_AppExcluded_ParentAppExcluded: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_ByPartner: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_Special: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_Dev: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_FreeWeekend: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_Invalid: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_RecurringLicense: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_WrongLicenseType: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_MasterSub: ESharedLibraryExcludeReason
k_ESharedLibrary_PackageExcluded_NoShareableApps: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_PaymentMasterSub: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_PaymentFamilyGroup: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_PaymentAuthorizedDevice: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_PaymentAutoGrant: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_FlagPending: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_FlagPendingRefund: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_FlagBorrowed: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_FlagAutoGrant: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_FlagTimedTrial: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_FreeSub: ESharedLibraryExcludeReason
k_ESharedLibrary_LicenseExcluded_Inactive: ESharedLibraryExcludeReason

class CFamilyGroups_CreateFamilyGroup_Request(_message.Message):
    __slots__ = ("name", "steamid")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    name: str
    steamid: int
    def __init__(self, name: _Optional[str] = ..., steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_CreateFamilyGroup_Response(_message.Message):
    __slots__ = ("family_groupid", "cooldown_skip_granted")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_SKIP_GRANTED_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    cooldown_skip_granted: bool
    def __init__(self, family_groupid: _Optional[int] = ..., cooldown_skip_granted: bool = ...) -> None: ...

class CFamilyGroups_GetFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "send_running_apps")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    SEND_RUNNING_APPS_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    send_running_apps: bool
    def __init__(self, family_groupid: _Optional[int] = ..., send_running_apps: bool = ...) -> None: ...

class FamilyGroupMember(_message.Message):
    __slots__ = ("steamid", "role", "time_joined", "cooldown_seconds_remaining")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    TIME_JOINED_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    role: EFamilyGroupRole
    time_joined: int
    cooldown_seconds_remaining: int
    def __init__(self, steamid: _Optional[int] = ..., role: _Optional[_Union[EFamilyGroupRole, str]] = ..., time_joined: _Optional[int] = ..., cooldown_seconds_remaining: _Optional[int] = ...) -> None: ...

class FamilyGroupPendingInvite(_message.Message):
    __slots__ = ("steamid", "role")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    role: EFamilyGroupRole
    def __init__(self, steamid: _Optional[int] = ..., role: _Optional[_Union[EFamilyGroupRole, str]] = ...) -> None: ...

class FamilyGroupFormerMember(_message.Message):
    __slots__ = ("steamid",)
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    def __init__(self, steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetFamilyGroup_Response(_message.Message):
    __slots__ = ("name", "members", "pending_invites", "free_spots", "country", "slot_cooldown_remaining_seconds", "former_members", "slot_cooldown_overrides")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    PENDING_INVITES_FIELD_NUMBER: _ClassVar[int]
    FREE_SPOTS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SLOT_COOLDOWN_REMAINING_SECONDS_FIELD_NUMBER: _ClassVar[int]
    FORMER_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    SLOT_COOLDOWN_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    name: str
    members: _containers.RepeatedCompositeFieldContainer[FamilyGroupMember]
    pending_invites: _containers.RepeatedCompositeFieldContainer[FamilyGroupPendingInvite]
    free_spots: int
    country: str
    slot_cooldown_remaining_seconds: int
    former_members: _containers.RepeatedCompositeFieldContainer[FamilyGroupFormerMember]
    slot_cooldown_overrides: int
    def __init__(self, name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[FamilyGroupMember, _Mapping]]] = ..., pending_invites: _Optional[_Iterable[_Union[FamilyGroupPendingInvite, _Mapping]]] = ..., free_spots: _Optional[int] = ..., country: _Optional[str] = ..., slot_cooldown_remaining_seconds: _Optional[int] = ..., former_members: _Optional[_Iterable[_Union[FamilyGroupFormerMember, _Mapping]]] = ..., slot_cooldown_overrides: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetFamilyGroupForUser_Request(_message.Message):
    __slots__ = ("steamid", "include_family_group_response")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FAMILY_GROUP_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    include_family_group_response: bool
    def __init__(self, steamid: _Optional[int] = ..., include_family_group_response: bool = ...) -> None: ...

class FamilyGroupPendingInviteForUser(_message.Message):
    __slots__ = ("family_groupid", "role", "inviter_steamid", "awaiting_2fa")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    INVITER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    AWAITING_2FA_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    role: EFamilyGroupRole
    inviter_steamid: int
    awaiting_2fa: bool
    def __init__(self, family_groupid: _Optional[int] = ..., role: _Optional[_Union[EFamilyGroupRole, str]] = ..., inviter_steamid: _Optional[int] = ..., awaiting_2fa: bool = ...) -> None: ...

class CFamilyGroups_GetFamilyGroupForUser_Response(_message.Message):
    __slots__ = ("family_groupid", "is_not_member_of_any_group", "latest_time_joined", "latest_joined_family_groupid", "pending_group_invites", "role", "cooldown_seconds_remaining", "family_group", "can_undelete_last_joined_family")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    IS_NOT_MEMBER_OF_ANY_GROUP_FIELD_NUMBER: _ClassVar[int]
    LATEST_TIME_JOINED_FIELD_NUMBER: _ClassVar[int]
    LATEST_JOINED_FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    PENDING_GROUP_INVITES_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_SECONDS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    FAMILY_GROUP_FIELD_NUMBER: _ClassVar[int]
    CAN_UNDELETE_LAST_JOINED_FAMILY_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    is_not_member_of_any_group: bool
    latest_time_joined: int
    latest_joined_family_groupid: int
    pending_group_invites: _containers.RepeatedCompositeFieldContainer[FamilyGroupPendingInviteForUser]
    role: int
    cooldown_seconds_remaining: int
    family_group: CFamilyGroups_GetFamilyGroup_Response
    can_undelete_last_joined_family: bool
    def __init__(self, family_groupid: _Optional[int] = ..., is_not_member_of_any_group: bool = ..., latest_time_joined: _Optional[int] = ..., latest_joined_family_groupid: _Optional[int] = ..., pending_group_invites: _Optional[_Iterable[_Union[FamilyGroupPendingInviteForUser, _Mapping]]] = ..., role: _Optional[int] = ..., cooldown_seconds_remaining: _Optional[int] = ..., family_group: _Optional[_Union[CFamilyGroups_GetFamilyGroup_Response, _Mapping]] = ..., can_undelete_last_joined_family: bool = ...) -> None: ...

class CFamilyGroups_ModifyFamilyGroupDetails_Request(_message.Message):
    __slots__ = ("family_groupid", "name")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    name: str
    def __init__(self, family_groupid: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CFamilyGroups_ModifyFamilyGroupDetails_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_InviteToFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "receiver_steamid", "receiver_role")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_ROLE_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    receiver_steamid: int
    receiver_role: EFamilyGroupRole
    def __init__(self, family_groupid: _Optional[int] = ..., receiver_steamid: _Optional[int] = ..., receiver_role: _Optional[_Union[EFamilyGroupRole, str]] = ...) -> None: ...

class CFamilyGroups_InviteToFamilyGroup_Response(_message.Message):
    __slots__ = ("invite_id", "two_factor_method")
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    TWO_FACTOR_METHOD_FIELD_NUMBER: _ClassVar[int]
    invite_id: int
    two_factor_method: EFamilyGroupsTwoFactorMethod
    def __init__(self, invite_id: _Optional[int] = ..., two_factor_method: _Optional[_Union[EFamilyGroupsTwoFactorMethod, str]] = ...) -> None: ...

class CFamilyGroups_ConfirmInviteToFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "invite_id", "nonce")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    invite_id: int
    nonce: int
    def __init__(self, family_groupid: _Optional[int] = ..., invite_id: _Optional[int] = ..., nonce: _Optional[int] = ...) -> None: ...

class CFamilyGroups_ConfirmInviteToFamilyGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_ResendInvitationToFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "steamid")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    steamid: int
    def __init__(self, family_groupid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_ResendInvitationToFamilyGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_JoinFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "nonce")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    nonce: int
    def __init__(self, family_groupid: _Optional[int] = ..., nonce: _Optional[int] = ...) -> None: ...

class CFamilyGroups_JoinFamilyGroup_Response(_message.Message):
    __slots__ = ("two_factor_method", "cooldown_skip_granted", "invite_already_accepted")
    TWO_FACTOR_METHOD_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_SKIP_GRANTED_FIELD_NUMBER: _ClassVar[int]
    INVITE_ALREADY_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    two_factor_method: EFamilyGroupsTwoFactorMethod
    cooldown_skip_granted: bool
    invite_already_accepted: bool
    def __init__(self, two_factor_method: _Optional[_Union[EFamilyGroupsTwoFactorMethod, str]] = ..., cooldown_skip_granted: bool = ..., invite_already_accepted: bool = ...) -> None: ...

class CFamilyGroups_ConfirmJoinFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "invite_id", "nonce")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    invite_id: int
    nonce: int
    def __init__(self, family_groupid: _Optional[int] = ..., invite_id: _Optional[int] = ..., nonce: _Optional[int] = ...) -> None: ...

class CFamilyGroups_ConfirmJoinFamilyGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_RemoveFromFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid", "steamid_to_remove")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    steamid_to_remove: int
    def __init__(self, family_groupid: _Optional[int] = ..., steamid_to_remove: _Optional[int] = ...) -> None: ...

class CFamilyGroups_RemoveFromFamilyGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_CancelFamilyGroupInvite_Request(_message.Message):
    __slots__ = ("family_groupid", "steamid_to_cancel")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_TO_CANCEL_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    steamid_to_cancel: int
    def __init__(self, family_groupid: _Optional[int] = ..., steamid_to_cancel: _Optional[int] = ...) -> None: ...

class CFamilyGroups_CancelFamilyGroupInvite_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_GetUsersSharingDevice_Request(_message.Message):
    __slots__ = ("family_groupid", "client_instance_id")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    client_instance_id: int
    def __init__(self, family_groupid: _Optional[int] = ..., client_instance_id: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetUsersSharingDevice_Response(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, users: _Optional[_Iterable[int]] = ...) -> None: ...

class CFamilyGroups_DeleteFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid",)
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    def __init__(self, family_groupid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_DeleteFamilyGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_UndeleteFamilyGroup_Request(_message.Message):
    __slots__ = ("family_groupid",)
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    def __init__(self, family_groupid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_UndeleteFamilyGroup_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_GetPlaytimeSummary_Request(_message.Message):
    __slots__ = ("family_groupid",)
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    def __init__(self, family_groupid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_PlaytimeEntry(_message.Message):
    __slots__ = ("steamid", "appid", "first_played", "latest_played", "seconds_played")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    FIRST_PLAYED_FIELD_NUMBER: _ClassVar[int]
    LATEST_PLAYED_FIELD_NUMBER: _ClassVar[int]
    SECONDS_PLAYED_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    appid: int
    first_played: int
    latest_played: int
    seconds_played: int
    def __init__(self, steamid: _Optional[int] = ..., appid: _Optional[int] = ..., first_played: _Optional[int] = ..., latest_played: _Optional[int] = ..., seconds_played: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetPlaytimeSummary_Response(_message.Message):
    __slots__ = ("entries", "entries_by_owner")
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_BY_OWNER_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[CFamilyGroups_PlaytimeEntry]
    entries_by_owner: _containers.RepeatedCompositeFieldContainer[CFamilyGroups_PlaytimeEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[CFamilyGroups_PlaytimeEntry, _Mapping]]] = ..., entries_by_owner: _Optional[_Iterable[_Union[CFamilyGroups_PlaytimeEntry, _Mapping]]] = ...) -> None: ...

class CFamilyGroups_RequestPurchase_Request(_message.Message):
    __slots__ = ("family_groupid", "gidshoppingcart", "store_country_code", "use_account_cart")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    GIDSHOPPINGCART_FIELD_NUMBER: _ClassVar[int]
    STORE_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    USE_ACCOUNT_CART_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    gidshoppingcart: int
    store_country_code: str
    use_account_cart: bool
    def __init__(self, family_groupid: _Optional[int] = ..., gidshoppingcart: _Optional[int] = ..., store_country_code: _Optional[str] = ..., use_account_cart: bool = ...) -> None: ...

class CFamilyGroups_RequestPurchase_Response(_message.Message):
    __slots__ = ("gidshoppingcart", "request_id")
    GIDSHOPPINGCART_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    gidshoppingcart: int
    request_id: int
    def __init__(self, gidshoppingcart: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetPurchaseRequests_Request(_message.Message):
    __slots__ = ("family_groupid", "request_ids", "rt_include_completed_since")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_IDS_FIELD_NUMBER: _ClassVar[int]
    RT_INCLUDE_COMPLETED_SINCE_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    request_ids: _containers.RepeatedScalarFieldContainer[int]
    rt_include_completed_since: int
    def __init__(self, family_groupid: _Optional[int] = ..., request_ids: _Optional[_Iterable[int]] = ..., rt_include_completed_since: _Optional[int] = ...) -> None: ...

class PurchaseRequest(_message.Message):
    __slots__ = ("requester_steamid", "gidshoppingcart", "time_requested", "time_responded", "responder_steamid", "response_action", "is_completed", "request_id", "requested_packageids", "purchased_packageids", "requested_bundleids", "purchased_bundleids")
    REQUESTER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    GIDSHOPPINGCART_FIELD_NUMBER: _ClassVar[int]
    TIME_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    TIME_RESPONDED_FIELD_NUMBER: _ClassVar[int]
    RESPONDER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ACTION_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PACKAGEIDS_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_PACKAGEIDS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BUNDLEIDS_FIELD_NUMBER: _ClassVar[int]
    PURCHASED_BUNDLEIDS_FIELD_NUMBER: _ClassVar[int]
    requester_steamid: int
    gidshoppingcart: int
    time_requested: int
    time_responded: int
    responder_steamid: int
    response_action: EPurchaseRequestAction
    is_completed: bool
    request_id: int
    requested_packageids: _containers.RepeatedScalarFieldContainer[int]
    purchased_packageids: _containers.RepeatedScalarFieldContainer[int]
    requested_bundleids: _containers.RepeatedScalarFieldContainer[int]
    purchased_bundleids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, requester_steamid: _Optional[int] = ..., gidshoppingcart: _Optional[int] = ..., time_requested: _Optional[int] = ..., time_responded: _Optional[int] = ..., responder_steamid: _Optional[int] = ..., response_action: _Optional[_Union[EPurchaseRequestAction, str]] = ..., is_completed: bool = ..., request_id: _Optional[int] = ..., requested_packageids: _Optional[_Iterable[int]] = ..., purchased_packageids: _Optional[_Iterable[int]] = ..., requested_bundleids: _Optional[_Iterable[int]] = ..., purchased_bundleids: _Optional[_Iterable[int]] = ...) -> None: ...

class CFamilyGroups_GetPurchaseRequests_Response(_message.Message):
    __slots__ = ("requests",)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[PurchaseRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[PurchaseRequest, _Mapping]]] = ...) -> None: ...

class CFamilyGroups_RespondToRequestedPurchase_Request(_message.Message):
    __slots__ = ("family_groupid", "action", "request_id")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    action: EPurchaseRequestAction
    request_id: int
    def __init__(self, family_groupid: _Optional[int] = ..., action: _Optional[_Union[EPurchaseRequestAction, str]] = ..., request_id: _Optional[int] = ...) -> None: ...

class CFamilyGroups_RespondToRequestedPurchase_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_GetChangeLog_Request(_message.Message):
    __slots__ = ("family_groupid",)
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    def __init__(self, family_groupid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetChangeLog_Response(_message.Message):
    __slots__ = ("changes",)
    class Change(_message.Message):
        __slots__ = ("timestamp", "actor_steamid", "type", "body", "by_support")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ACTOR_STEAMID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        BY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        actor_steamid: int
        type: EFamilyGroupChangeLogType
        body: str
        by_support: bool
        def __init__(self, timestamp: _Optional[int] = ..., actor_steamid: _Optional[int] = ..., type: _Optional[_Union[EFamilyGroupChangeLogType, str]] = ..., body: _Optional[str] = ..., by_support: bool = ...) -> None: ...
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    changes: _containers.RepeatedCompositeFieldContainer[CFamilyGroups_GetChangeLog_Response.Change]
    def __init__(self, changes: _Optional[_Iterable[_Union[CFamilyGroups_GetChangeLog_Response.Change, _Mapping]]] = ...) -> None: ...

class CFamilyGroups_SetFamilyCooldownOverrides_Request(_message.Message):
    __slots__ = ("family_groupid", "cooldown_count")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_COUNT_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    cooldown_count: int
    def __init__(self, family_groupid: _Optional[int] = ..., cooldown_count: _Optional[int] = ...) -> None: ...

class CFamilyGroups_SetFamilyCooldownOverrides_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_GetSharedLibraryApps_Request(_message.Message):
    __slots__ = ("family_groupid", "include_own", "include_excluded", "language", "max_apps", "include_non_games", "steamid")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_OWN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MAX_APPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NON_GAMES_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    include_own: bool
    include_excluded: bool
    language: str
    max_apps: int
    include_non_games: bool
    steamid: int
    def __init__(self, family_groupid: _Optional[int] = ..., include_own: bool = ..., include_excluded: bool = ..., language: _Optional[str] = ..., max_apps: _Optional[int] = ..., include_non_games: bool = ..., steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetSharedLibraryApps_Response(_message.Message):
    __slots__ = ("apps", "owner_steamid")
    class SharedApp(_message.Message):
        __slots__ = ("appid", "owner_steamids", "name", "sort_as", "capsule_filename", "img_icon_hash", "exclude_reason", "rt_time_acquired", "rt_last_played", "rt_playtime", "app_type", "content_descriptors")
        APPID_FIELD_NUMBER: _ClassVar[int]
        OWNER_STEAMIDS_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SORT_AS_FIELD_NUMBER: _ClassVar[int]
        CAPSULE_FILENAME_FIELD_NUMBER: _ClassVar[int]
        IMG_ICON_HASH_FIELD_NUMBER: _ClassVar[int]
        EXCLUDE_REASON_FIELD_NUMBER: _ClassVar[int]
        RT_TIME_ACQUIRED_FIELD_NUMBER: _ClassVar[int]
        RT_LAST_PLAYED_FIELD_NUMBER: _ClassVar[int]
        RT_PLAYTIME_FIELD_NUMBER: _ClassVar[int]
        APP_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
        appid: int
        owner_steamids: _containers.RepeatedScalarFieldContainer[int]
        name: str
        sort_as: str
        capsule_filename: str
        img_icon_hash: str
        exclude_reason: ESharedLibraryExcludeReason
        rt_time_acquired: int
        rt_last_played: int
        rt_playtime: int
        app_type: _enums_pb2.EProtoAppType
        content_descriptors: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, appid: _Optional[int] = ..., owner_steamids: _Optional[_Iterable[int]] = ..., name: _Optional[str] = ..., sort_as: _Optional[str] = ..., capsule_filename: _Optional[str] = ..., img_icon_hash: _Optional[str] = ..., exclude_reason: _Optional[_Union[ESharedLibraryExcludeReason, str]] = ..., rt_time_acquired: _Optional[int] = ..., rt_last_played: _Optional[int] = ..., rt_playtime: _Optional[int] = ..., app_type: _Optional[_Union[_enums_pb2.EProtoAppType, str]] = ..., content_descriptors: _Optional[_Iterable[int]] = ...) -> None: ...
    APPS_FIELD_NUMBER: _ClassVar[int]
    OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    apps: _containers.RepeatedCompositeFieldContainer[CFamilyGroups_GetSharedLibraryApps_Response.SharedApp]
    owner_steamid: int
    def __init__(self, apps: _Optional[_Iterable[_Union[CFamilyGroups_GetSharedLibraryApps_Response.SharedApp, _Mapping]]] = ..., owner_steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_SetPreferredLender_Request(_message.Message):
    __slots__ = ("family_groupid", "appid", "lender_steamid")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    LENDER_STEAMID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    appid: int
    lender_steamid: int
    def __init__(self, family_groupid: _Optional[int] = ..., appid: _Optional[int] = ..., lender_steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_SetPreferredLender_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_GetPreferredLenders_Request(_message.Message):
    __slots__ = ("family_groupid",)
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    def __init__(self, family_groupid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetPreferredLenders_Response(_message.Message):
    __slots__ = ("members",)
    class FamilyMember(_message.Message):
        __slots__ = ("steamid", "preferred_appids")
        STEAMID_FIELD_NUMBER: _ClassVar[int]
        PREFERRED_APPIDS_FIELD_NUMBER: _ClassVar[int]
        steamid: int
        preferred_appids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, steamid: _Optional[int] = ..., preferred_appids: _Optional[_Iterable[int]] = ...) -> None: ...
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[CFamilyGroups_GetPreferredLenders_Response.FamilyMember]
    def __init__(self, members: _Optional[_Iterable[_Union[CFamilyGroups_GetPreferredLenders_Response.FamilyMember, _Mapping]]] = ...) -> None: ...

class CFamilyGroups_ForceAcceptInvite_Request(_message.Message):
    __slots__ = ("family_groupid", "steamid")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    steamid: int
    def __init__(self, family_groupid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_ForceAcceptInvite_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroups_GetInviteCheckResults_Request(_message.Message):
    __slots__ = ("family_groupid", "steamid")
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    steamid: int
    def __init__(self, family_groupid: _Optional[int] = ..., steamid: _Optional[int] = ...) -> None: ...

class CFamilyGroups_GetInviteCheckResults_Response(_message.Message):
    __slots__ = ("wallet_country_matches", "ip_match", "join_restriction")
    WALLET_COUNTRY_MATCHES_FIELD_NUMBER: _ClassVar[int]
    IP_MATCH_FIELD_NUMBER: _ClassVar[int]
    JOIN_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    wallet_country_matches: bool
    ip_match: bool
    join_restriction: int
    def __init__(self, wallet_country_matches: bool = ..., ip_match: bool = ..., join_restriction: _Optional[int] = ...) -> None: ...

class CFamilyGroups_ClearCooldownSkip_Request(_message.Message):
    __slots__ = ("steamid", "invite_id")
    STEAMID_FIELD_NUMBER: _ClassVar[int]
    INVITE_ID_FIELD_NUMBER: _ClassVar[int]
    steamid: int
    invite_id: int
    def __init__(self, steamid: _Optional[int] = ..., invite_id: _Optional[int] = ...) -> None: ...

class CFamilyGroups_ClearCooldownSkip_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroupsClient_NotifyRunningApps_Notification(_message.Message):
    __slots__ = ("family_groupid", "running_apps")
    class PlayingMember(_message.Message):
        __slots__ = ("member_steamid", "owner_steamid")
        MEMBER_STEAMID_FIELD_NUMBER: _ClassVar[int]
        OWNER_STEAMID_FIELD_NUMBER: _ClassVar[int]
        member_steamid: int
        owner_steamid: int
        def __init__(self, member_steamid: _Optional[int] = ..., owner_steamid: _Optional[int] = ...) -> None: ...
    class RunningApp(_message.Message):
        __slots__ = ("appid", "playing_members")
        APPID_FIELD_NUMBER: _ClassVar[int]
        PLAYING_MEMBERS_FIELD_NUMBER: _ClassVar[int]
        appid: int
        playing_members: _containers.RepeatedCompositeFieldContainer[CFamilyGroupsClient_NotifyRunningApps_Notification.PlayingMember]
        def __init__(self, appid: _Optional[int] = ..., playing_members: _Optional[_Iterable[_Union[CFamilyGroupsClient_NotifyRunningApps_Notification.PlayingMember, _Mapping]]] = ...) -> None: ...
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    RUNNING_APPS_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    running_apps: _containers.RepeatedCompositeFieldContainer[CFamilyGroupsClient_NotifyRunningApps_Notification.RunningApp]
    def __init__(self, family_groupid: _Optional[int] = ..., running_apps: _Optional[_Iterable[_Union[CFamilyGroupsClient_NotifyRunningApps_Notification.RunningApp, _Mapping]]] = ...) -> None: ...

class CFamilyGroupsClient_InviteStatus_Notification(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CFamilyGroupsClient_GroupChanged_Notification(_message.Message):
    __slots__ = ("family_groupid",)
    FAMILY_GROUPID_FIELD_NUMBER: _ClassVar[int]
    family_groupid: int
    def __init__(self, family_groupid: _Optional[int] = ...) -> None: ...

class FamilyGroups(_service.service): ...

class FamilyGroups_Stub(FamilyGroups): ...

class FamilyGroupsClient(_service.service): ...

class FamilyGroupsClient_Stub(FamilyGroupsClient): ...
