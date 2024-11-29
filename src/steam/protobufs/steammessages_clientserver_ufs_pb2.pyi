import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientUFSGetUGCDetails(_message.Message):
    __slots__ = ("hcontent",)
    HCONTENT_FIELD_NUMBER: _ClassVar[int]
    hcontent: int
    def __init__(self, hcontent: _Optional[int] = ...) -> None: ...

class CMsgClientUFSGetUGCDetailsResponse(_message.Message):
    __slots__ = ("eresult", "url", "app_id", "filename", "steamid_creator", "file_size", "compressed_file_size", "rangecheck_host", "file_encoded_sha1")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    STEAMID_CREATOR_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    RANGECHECK_HOST_FIELD_NUMBER: _ClassVar[int]
    FILE_ENCODED_SHA1_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    url: str
    app_id: int
    filename: str
    steamid_creator: int
    file_size: int
    compressed_file_size: int
    rangecheck_host: str
    file_encoded_sha1: str
    def __init__(self, eresult: _Optional[int] = ..., url: _Optional[str] = ..., app_id: _Optional[int] = ..., filename: _Optional[str] = ..., steamid_creator: _Optional[int] = ..., file_size: _Optional[int] = ..., compressed_file_size: _Optional[int] = ..., rangecheck_host: _Optional[str] = ..., file_encoded_sha1: _Optional[str] = ...) -> None: ...

class CMsgClientUFSGetSingleFileInfo(_message.Message):
    __slots__ = ("app_id", "file_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    file_name: str
    def __init__(self, app_id: _Optional[int] = ..., file_name: _Optional[str] = ...) -> None: ...

class CMsgClientUFSGetSingleFileInfoResponse(_message.Message):
    __slots__ = ("eresult", "app_id", "file_name", "sha_file", "time_stamp", "raw_file_size", "is_explicit_delete")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHA_FILE_FIELD_NUMBER: _ClassVar[int]
    TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    RAW_FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_EXPLICIT_DELETE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    app_id: int
    file_name: str
    sha_file: bytes
    time_stamp: int
    raw_file_size: int
    is_explicit_delete: bool
    def __init__(self, eresult: _Optional[int] = ..., app_id: _Optional[int] = ..., file_name: _Optional[str] = ..., sha_file: _Optional[bytes] = ..., time_stamp: _Optional[int] = ..., raw_file_size: _Optional[int] = ..., is_explicit_delete: bool = ...) -> None: ...

class CMsgClientUFSShareFile(_message.Message):
    __slots__ = ("app_id", "file_name")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    file_name: str
    def __init__(self, app_id: _Optional[int] = ..., file_name: _Optional[str] = ...) -> None: ...

class CMsgClientUFSShareFileResponse(_message.Message):
    __slots__ = ("eresult", "hcontent")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    HCONTENT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    hcontent: int
    def __init__(self, eresult: _Optional[int] = ..., hcontent: _Optional[int] = ...) -> None: ...
