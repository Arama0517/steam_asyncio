# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: steammessages_parental.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'steammessages_parental.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2
import steam.protobufs.steammessages_parental_objects_pb2 as steammessages__parental__objects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csteammessages_parental.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\x1a$steammessages_parental_objects.proto\"\x99\x01\n(CParental_EnableParentalSettings_Request\x12\x10\n\x08password\x18\x01 \x01(\t\x12#\n\x08settings\x18\x02 \x01(\x0b\x32\x11.ParentalSettings\x12\x11\n\tsessionid\x18\x03 \x01(\t\x12\x12\n\nenablecode\x18\x04 \x01(\r\x12\x0f\n\x07steamid\x18\n \x01(\x06\"+\n)CParental_EnableParentalSettings_Response\"N\n)CParental_DisableParentalSettings_Request\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x0f\n\x07steamid\x18\n \x01(\x06\",\n*CParental_DisableParentalSettings_Response\"8\n%CParental_GetParentalSettings_Request\x12\x0f\n\x07steamid\x18\n \x01(\x06\"M\n&CParental_GetParentalSettings_Response\x12#\n\x08settings\x18\x01 \x01(\x0b\x32\x11.ParentalSettings\"?\n+CParental_GetSignedParentalSettings_Request\x12\x10\n\x08priority\x18\x01 \x01(\r\"^\n,CParental_GetSignedParentalSettings_Response\x12\x1b\n\x13serialized_settings\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\x98\x01\n%CParental_SetParentalSettings_Request\x12\x10\n\x08password\x18\x01 \x01(\t\x12#\n\x08settings\x18\x02 \x01(\x0b\x32\x11.ParentalSettings\x12\x14\n\x0cnew_password\x18\x03 \x01(\t\x12\x11\n\tsessionid\x18\x04 \x01(\t\x12\x0f\n\x07steamid\x18\n \x01(\x06\"(\n&CParental_SetParentalSettings_Response\"7\n\x1f\x43Parental_ValidateToken_Request\x12\x14\n\x0cunlock_token\x18\x01 \x01(\t\"\"\n CParental_ValidateToken_Response\"g\n\"CParental_ValidatePassword_Request\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x0f\n\x07session\x18\x02 \x01(\t\x12\x1e\n\x16send_unlock_on_success\x18\x03 \x01(\x08\"4\n#CParental_ValidatePassword_Response\x12\r\n\x05token\x18\x01 \x01(\t\"/\n\x1c\x43Parental_LockClient_Request\x12\x0f\n\x07session\x18\x01 \x01(\t\"\x1f\n\x1d\x43Parental_LockClient_Response\"\'\n%CParental_RequestRecoveryCode_Request\"(\n&CParental_RequestRecoveryCode_Response\"S\n)CParental_DisableWithRecoveryCode_Request\x12\x15\n\rrecovery_code\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\n \x01(\x06\",\n*CParental_DisableWithRecoveryCode_Response\"K\n&CParental_RequestFeatureAccess_Request\x12\x10\n\x08\x66\x65\x61tures\x18\x01 \x01(\r\x12\x0f\n\x07steamid\x18\n \x01(\x06\"<\n\'CParental_RequestFeatureAccess_Response\x12\x11\n\trequestid\x18\x01 \x01(\x06\"\x81\x01\n&CParental_ApproveFeatureAccess_Request\x12\x0f\n\x07\x61pprove\x18\x01 \x01(\x08\x12\x11\n\trequestid\x18\x02 \x01(\x06\x12\x10\n\x08\x66\x65\x61tures\x18\x03 \x01(\r\x12\x10\n\x08\x64uration\x18\x04 \x01(\r\x12\x0f\n\x07steamid\x18\n \x01(\x06\")\n\'CParental_ApproveFeatureAccess_Response\"\x87\x01\n!CParental_RequestPlaytime_Request\x12\x14\n\x0ctime_expires\x18\x01 \x01(\r\x12;\n\x1d\x63urrent_playtime_restrictions\x18\x02 \x01(\x0b\x32\x14.ParentalPlaytimeDay\x12\x0f\n\x07steamid\x18\n \x01(\x06\"7\n\"CParental_RequestPlaytime_Response\x12\x11\n\trequestid\x18\x01 \x01(\x06\"\x9f\x01\n!CParental_ApprovePlaytime_Request\x12\x0f\n\x07\x61pprove\x18\x01 \x01(\x08\x12\x11\n\trequestid\x18\x02 \x01(\x06\x12\x45\n\x15restrictions_approved\x18\x03 \x01(\x0b\x32&.ParentalTemporaryPlaytimeRestrictions\x12\x0f\n\x07steamid\x18\n \x01(\x06\"$\n\"CParental_ApprovePlaytime_Response\"[\n\x1d\x43Parental_GetRequests_Request\x12\"\n\x1art_include_completed_since\x18\x01 \x01(\r\x12\x16\n\x0e\x66\x61mily_groupid\x18\x02 \x01(\x06\"\x88\x01\n\x1e\x43Parental_GetRequests_Response\x12\x31\n\x10\x66\x65\x61ture_requests\x18\x01 \x03(\x0b\x32\x17.ParentalFeatureRequest\x12\x33\n\x11playtime_requests\x18\x02 \x03(\x0b\x32\x18.ParentalPlaytimeRequest\"g\n)CParental_ReportPlaytimeAndNotify_Request\x12\x13\n\x0b\x64\x61y_of_week\x18\x01 \x01(\r\x12\x14\n\x0cminutes_used\x18\x02 \x01(\r\x12\x0f\n\x07steamid\x18\n \x01(\x06\",\n*CParental_ReportPlaytimeAndNotify_Response\"\x84\x01\n-CParental_ParentalSettingsChange_Notification\x12\x1b\n\x13serialized_settings\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x11\n\tsessionid\x18\x04 \x01(\t\"L\n%CParental_ParentalUnlock_Notification\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x11\n\tsessionid\x18\x02 \x01(\t\"8\n#CParental_ParentalLock_Notification\x12\x11\n\tsessionid\x18\x01 \x01(\t\"P\n#CParental_PlaytimeUsed_Notification\x12\x13\n\x0b\x64\x61y_of_week\x18\x01 \x01(\r\x12\x14\n\x0cminutes_used\x18\x02 \x01(\r2\xe9\x0c\n\x08Parental\x12o\n\x16\x45nableParentalSettings\x12).CParental_EnableParentalSettings_Request\x1a*.CParental_EnableParentalSettings_Response\x12r\n\x17\x44isableParentalSettings\x12*.CParental_DisableParentalSettings_Request\x1a+.CParental_DisableParentalSettings_Response\x12\x66\n\x13GetParentalSettings\x12&.CParental_GetParentalSettings_Request\x1a\'.CParental_GetParentalSettings_Response\x12x\n\x19GetSignedParentalSettings\x12,.CParental_GetSignedParentalSettings_Request\x1a-.CParental_GetSignedParentalSettings_Response\x12\x66\n\x13SetParentalSettings\x12&.CParental_SetParentalSettings_Request\x1a\'.CParental_SetParentalSettings_Response\x12T\n\rValidateToken\x12 .CParental_ValidateToken_Request\x1a!.CParental_ValidateToken_Response\x12]\n\x10ValidatePassword\x12#.CParental_ValidatePassword_Request\x1a$.CParental_ValidatePassword_Response\x12K\n\nLockClient\x12\x1d.CParental_LockClient_Request\x1a\x1e.CParental_LockClient_Response\x12\x66\n\x13RequestRecoveryCode\x12&.CParental_RequestRecoveryCode_Request\x1a\'.CParental_RequestRecoveryCode_Response\x12r\n\x17\x44isableWithRecoveryCode\x12*.CParental_DisableWithRecoveryCode_Request\x1a+.CParental_DisableWithRecoveryCode_Response\x12i\n\x14RequestFeatureAccess\x12\'.CParental_RequestFeatureAccess_Request\x1a(.CParental_RequestFeatureAccess_Response\x12i\n\x14\x41pproveFeatureAccess\x12\'.CParental_ApproveFeatureAccess_Request\x1a(.CParental_ApproveFeatureAccess_Response\x12Z\n\x0fRequestPlaytime\x12\".CParental_RequestPlaytime_Request\x1a#.CParental_RequestPlaytime_Response\x12Z\n\x0f\x41pprovePlaytime\x12\".CParental_ApprovePlaytime_Request\x1a#.CParental_ApprovePlaytime_Response\x12N\n\x0bGetRequests\x12\x1e.CParental_GetRequests_Request\x1a\x1f.CParental_GetRequests_Response\x12r\n\x17ReportPlaytimeAndNotify\x12*.CParental_ReportPlaytimeAndNotify_Request\x1a+.CParental_ReportPlaytimeAndNotify_Response2\xba\x02\n\x0eParentalClient\x12S\n\x14NotifySettingsChange\x12..CParental_ParentalSettingsChange_Notification\x1a\x0b.NoResponse\x12\x43\n\x0cNotifyUnlock\x12&.CParental_ParentalUnlock_Notification\x1a\x0b.NoResponse\x12?\n\nNotifyLock\x12$.CParental_ParentalLock_Notification\x1a\x0b.NoResponse\x12G\n\x12NotifyPlaytimeUsed\x12$.CParental_PlaytimeUsed_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x42\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_parental_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_PARENTALCLIENT']._loaded_options = None
  _globals['_PARENTALCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_CPARENTAL_ENABLEPARENTALSETTINGS_REQUEST']._serialized_start=131
  _globals['_CPARENTAL_ENABLEPARENTALSETTINGS_REQUEST']._serialized_end=284
  _globals['_CPARENTAL_ENABLEPARENTALSETTINGS_RESPONSE']._serialized_start=286
  _globals['_CPARENTAL_ENABLEPARENTALSETTINGS_RESPONSE']._serialized_end=329
  _globals['_CPARENTAL_DISABLEPARENTALSETTINGS_REQUEST']._serialized_start=331
  _globals['_CPARENTAL_DISABLEPARENTALSETTINGS_REQUEST']._serialized_end=409
  _globals['_CPARENTAL_DISABLEPARENTALSETTINGS_RESPONSE']._serialized_start=411
  _globals['_CPARENTAL_DISABLEPARENTALSETTINGS_RESPONSE']._serialized_end=455
  _globals['_CPARENTAL_GETPARENTALSETTINGS_REQUEST']._serialized_start=457
  _globals['_CPARENTAL_GETPARENTALSETTINGS_REQUEST']._serialized_end=513
  _globals['_CPARENTAL_GETPARENTALSETTINGS_RESPONSE']._serialized_start=515
  _globals['_CPARENTAL_GETPARENTALSETTINGS_RESPONSE']._serialized_end=592
  _globals['_CPARENTAL_GETSIGNEDPARENTALSETTINGS_REQUEST']._serialized_start=594
  _globals['_CPARENTAL_GETSIGNEDPARENTALSETTINGS_REQUEST']._serialized_end=657
  _globals['_CPARENTAL_GETSIGNEDPARENTALSETTINGS_RESPONSE']._serialized_start=659
  _globals['_CPARENTAL_GETSIGNEDPARENTALSETTINGS_RESPONSE']._serialized_end=753
  _globals['_CPARENTAL_SETPARENTALSETTINGS_REQUEST']._serialized_start=756
  _globals['_CPARENTAL_SETPARENTALSETTINGS_REQUEST']._serialized_end=908
  _globals['_CPARENTAL_SETPARENTALSETTINGS_RESPONSE']._serialized_start=910
  _globals['_CPARENTAL_SETPARENTALSETTINGS_RESPONSE']._serialized_end=950
  _globals['_CPARENTAL_VALIDATETOKEN_REQUEST']._serialized_start=952
  _globals['_CPARENTAL_VALIDATETOKEN_REQUEST']._serialized_end=1007
  _globals['_CPARENTAL_VALIDATETOKEN_RESPONSE']._serialized_start=1009
  _globals['_CPARENTAL_VALIDATETOKEN_RESPONSE']._serialized_end=1043
  _globals['_CPARENTAL_VALIDATEPASSWORD_REQUEST']._serialized_start=1045
  _globals['_CPARENTAL_VALIDATEPASSWORD_REQUEST']._serialized_end=1148
  _globals['_CPARENTAL_VALIDATEPASSWORD_RESPONSE']._serialized_start=1150
  _globals['_CPARENTAL_VALIDATEPASSWORD_RESPONSE']._serialized_end=1202
  _globals['_CPARENTAL_LOCKCLIENT_REQUEST']._serialized_start=1204
  _globals['_CPARENTAL_LOCKCLIENT_REQUEST']._serialized_end=1251
  _globals['_CPARENTAL_LOCKCLIENT_RESPONSE']._serialized_start=1253
  _globals['_CPARENTAL_LOCKCLIENT_RESPONSE']._serialized_end=1284
  _globals['_CPARENTAL_REQUESTRECOVERYCODE_REQUEST']._serialized_start=1286
  _globals['_CPARENTAL_REQUESTRECOVERYCODE_REQUEST']._serialized_end=1325
  _globals['_CPARENTAL_REQUESTRECOVERYCODE_RESPONSE']._serialized_start=1327
  _globals['_CPARENTAL_REQUESTRECOVERYCODE_RESPONSE']._serialized_end=1367
  _globals['_CPARENTAL_DISABLEWITHRECOVERYCODE_REQUEST']._serialized_start=1369
  _globals['_CPARENTAL_DISABLEWITHRECOVERYCODE_REQUEST']._serialized_end=1452
  _globals['_CPARENTAL_DISABLEWITHRECOVERYCODE_RESPONSE']._serialized_start=1454
  _globals['_CPARENTAL_DISABLEWITHRECOVERYCODE_RESPONSE']._serialized_end=1498
  _globals['_CPARENTAL_REQUESTFEATUREACCESS_REQUEST']._serialized_start=1500
  _globals['_CPARENTAL_REQUESTFEATUREACCESS_REQUEST']._serialized_end=1575
  _globals['_CPARENTAL_REQUESTFEATUREACCESS_RESPONSE']._serialized_start=1577
  _globals['_CPARENTAL_REQUESTFEATUREACCESS_RESPONSE']._serialized_end=1637
  _globals['_CPARENTAL_APPROVEFEATUREACCESS_REQUEST']._serialized_start=1640
  _globals['_CPARENTAL_APPROVEFEATUREACCESS_REQUEST']._serialized_end=1769
  _globals['_CPARENTAL_APPROVEFEATUREACCESS_RESPONSE']._serialized_start=1771
  _globals['_CPARENTAL_APPROVEFEATUREACCESS_RESPONSE']._serialized_end=1812
  _globals['_CPARENTAL_REQUESTPLAYTIME_REQUEST']._serialized_start=1815
  _globals['_CPARENTAL_REQUESTPLAYTIME_REQUEST']._serialized_end=1950
  _globals['_CPARENTAL_REQUESTPLAYTIME_RESPONSE']._serialized_start=1952
  _globals['_CPARENTAL_REQUESTPLAYTIME_RESPONSE']._serialized_end=2007
  _globals['_CPARENTAL_APPROVEPLAYTIME_REQUEST']._serialized_start=2010
  _globals['_CPARENTAL_APPROVEPLAYTIME_REQUEST']._serialized_end=2169
  _globals['_CPARENTAL_APPROVEPLAYTIME_RESPONSE']._serialized_start=2171
  _globals['_CPARENTAL_APPROVEPLAYTIME_RESPONSE']._serialized_end=2207
  _globals['_CPARENTAL_GETREQUESTS_REQUEST']._serialized_start=2209
  _globals['_CPARENTAL_GETREQUESTS_REQUEST']._serialized_end=2300
  _globals['_CPARENTAL_GETREQUESTS_RESPONSE']._serialized_start=2303
  _globals['_CPARENTAL_GETREQUESTS_RESPONSE']._serialized_end=2439
  _globals['_CPARENTAL_REPORTPLAYTIMEANDNOTIFY_REQUEST']._serialized_start=2441
  _globals['_CPARENTAL_REPORTPLAYTIMEANDNOTIFY_REQUEST']._serialized_end=2544
  _globals['_CPARENTAL_REPORTPLAYTIMEANDNOTIFY_RESPONSE']._serialized_start=2546
  _globals['_CPARENTAL_REPORTPLAYTIMEANDNOTIFY_RESPONSE']._serialized_end=2590
  _globals['_CPARENTAL_PARENTALSETTINGSCHANGE_NOTIFICATION']._serialized_start=2593
  _globals['_CPARENTAL_PARENTALSETTINGSCHANGE_NOTIFICATION']._serialized_end=2725
  _globals['_CPARENTAL_PARENTALUNLOCK_NOTIFICATION']._serialized_start=2727
  _globals['_CPARENTAL_PARENTALUNLOCK_NOTIFICATION']._serialized_end=2803
  _globals['_CPARENTAL_PARENTALLOCK_NOTIFICATION']._serialized_start=2805
  _globals['_CPARENTAL_PARENTALLOCK_NOTIFICATION']._serialized_end=2861
  _globals['_CPARENTAL_PLAYTIMEUSED_NOTIFICATION']._serialized_start=2863
  _globals['_CPARENTAL_PLAYTIMEUSED_NOTIFICATION']._serialized_end=2943
  _globals['_PARENTAL']._serialized_start=2946
  _globals['_PARENTAL']._serialized_end=4587
  _globals['_PARENTALCLIENT']._serialized_start=4590
  _globals['_PARENTALCLIENT']._serialized_end=4904
_builder.BuildServices(DESCRIPTOR, 'steammessages_parental_pb2', _globals)
# @@protoc_insertion_point(module_scope)