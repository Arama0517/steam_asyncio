import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CContentBuilder_InitDepotBuild_Request(_message.Message):
    __slots__ = ("appid", "depotid", "workshop_itemid", "for_local_cs", "target_branch", "shader_depot")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOTID_FIELD_NUMBER: _ClassVar[int]
    WORKSHOP_ITEMID_FIELD_NUMBER: _ClassVar[int]
    FOR_LOCAL_CS_FIELD_NUMBER: _ClassVar[int]
    TARGET_BRANCH_FIELD_NUMBER: _ClassVar[int]
    SHADER_DEPOT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depotid: int
    workshop_itemid: int
    for_local_cs: bool
    target_branch: str
    shader_depot: bool
    def __init__(self, appid: _Optional[int] = ..., depotid: _Optional[int] = ..., workshop_itemid: _Optional[int] = ..., for_local_cs: bool = ..., target_branch: _Optional[str] = ..., shader_depot: bool = ...) -> None: ...

class CContentBuilder_InitDepotBuild_Response(_message.Message):
    __slots__ = ("baseline_manifestid", "chunk_size", "aes_key", "rsa_key", "url_host", "offset_detection_enabled", "offset_detection_min_clean_chunk", "offset_detection_blast_radius_pre", "offset_detection_blast_radius_post", "offset_detection_max_distance_pre", "offset_detection_max_distance_post")
    BASELINE_MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    AES_KEY_FIELD_NUMBER: _ClassVar[int]
    RSA_KEY_FIELD_NUMBER: _ClassVar[int]
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DETECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DETECTION_MIN_CLEAN_CHUNK_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DETECTION_BLAST_RADIUS_PRE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DETECTION_BLAST_RADIUS_POST_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DETECTION_MAX_DISTANCE_PRE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DETECTION_MAX_DISTANCE_POST_FIELD_NUMBER: _ClassVar[int]
    baseline_manifestid: int
    chunk_size: int
    aes_key: bytes
    rsa_key: bytes
    url_host: str
    offset_detection_enabled: bool
    offset_detection_min_clean_chunk: int
    offset_detection_blast_radius_pre: int
    offset_detection_blast_radius_post: int
    offset_detection_max_distance_pre: int
    offset_detection_max_distance_post: int
    def __init__(self, baseline_manifestid: _Optional[int] = ..., chunk_size: _Optional[int] = ..., aes_key: _Optional[bytes] = ..., rsa_key: _Optional[bytes] = ..., url_host: _Optional[str] = ..., offset_detection_enabled: bool = ..., offset_detection_min_clean_chunk: _Optional[int] = ..., offset_detection_blast_radius_pre: _Optional[int] = ..., offset_detection_blast_radius_post: _Optional[int] = ..., offset_detection_max_distance_pre: _Optional[int] = ..., offset_detection_max_distance_post: _Optional[int] = ...) -> None: ...

class CContentBuilder_StartDepotUpload_Request(_message.Message):
    __slots__ = ("appid", "depotid", "workshop_itemid", "for_local_cs", "baseline_manifestid", "manifest_size")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOTID_FIELD_NUMBER: _ClassVar[int]
    WORKSHOP_ITEMID_FIELD_NUMBER: _ClassVar[int]
    FOR_LOCAL_CS_FIELD_NUMBER: _ClassVar[int]
    BASELINE_MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_SIZE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depotid: int
    workshop_itemid: int
    for_local_cs: bool
    baseline_manifestid: int
    manifest_size: int
    def __init__(self, appid: _Optional[int] = ..., depotid: _Optional[int] = ..., workshop_itemid: _Optional[int] = ..., for_local_cs: bool = ..., baseline_manifestid: _Optional[int] = ..., manifest_size: _Optional[int] = ...) -> None: ...

class CContentBuilder_StartDepotUpload_Response(_message.Message):
    __slots__ = ("depot_build_handle",)
    DEPOT_BUILD_HANDLE_FIELD_NUMBER: _ClassVar[int]
    depot_build_handle: int
    def __init__(self, depot_build_handle: _Optional[int] = ...) -> None: ...

class CContentBuilder_GetMissingDepotChunks_Request(_message.Message):
    __slots__ = ("appid", "depot_build_handle")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_BUILD_HANDLE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depot_build_handle: int
    def __init__(self, appid: _Optional[int] = ..., depot_build_handle: _Optional[int] = ...) -> None: ...

class CContentBuilder_GetMissingDepotChunks_Response(_message.Message):
    __slots__ = ("missing_chunks", "total_missing_chunks", "total_missing_bytes")
    class Chunks(_message.Message):
        __slots__ = ("sha",)
        SHA_FIELD_NUMBER: _ClassVar[int]
        sha: bytes
        def __init__(self, sha: _Optional[bytes] = ...) -> None: ...
    MISSING_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MISSING_CHUNKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MISSING_BYTES_FIELD_NUMBER: _ClassVar[int]
    missing_chunks: _containers.RepeatedCompositeFieldContainer[CContentBuilder_GetMissingDepotChunks_Response.Chunks]
    total_missing_chunks: int
    total_missing_bytes: int
    def __init__(self, missing_chunks: _Optional[_Iterable[_Union[CContentBuilder_GetMissingDepotChunks_Response.Chunks, _Mapping]]] = ..., total_missing_chunks: _Optional[int] = ..., total_missing_bytes: _Optional[int] = ...) -> None: ...

class CContentBuilder_FinishDepotUpload_Request(_message.Message):
    __slots__ = ("appid", "depot_build_handle")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_BUILD_HANDLE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depot_build_handle: int
    def __init__(self, appid: _Optional[int] = ..., depot_build_handle: _Optional[int] = ...) -> None: ...

class CContentBuilder_FinishDepotUpload_Response(_message.Message):
    __slots__ = ("manifestid", "prev_reused")
    MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    PREV_REUSED_FIELD_NUMBER: _ClassVar[int]
    manifestid: int
    prev_reused: bool
    def __init__(self, manifestid: _Optional[int] = ..., prev_reused: bool = ...) -> None: ...

class CContentBuilder_CommitAppBuild_Request(_message.Message):
    __slots__ = ("appid", "depot_manifests", "build_notes", "live_branch", "for_local_cs")
    class Depots(_message.Message):
        __slots__ = ("depotid", "manifestid")
        DEPOTID_FIELD_NUMBER: _ClassVar[int]
        MANIFESTID_FIELD_NUMBER: _ClassVar[int]
        depotid: int
        manifestid: int
        def __init__(self, depotid: _Optional[int] = ..., manifestid: _Optional[int] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOT_MANIFESTS_FIELD_NUMBER: _ClassVar[int]
    BUILD_NOTES_FIELD_NUMBER: _ClassVar[int]
    LIVE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    FOR_LOCAL_CS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depot_manifests: _containers.RepeatedCompositeFieldContainer[CContentBuilder_CommitAppBuild_Request.Depots]
    build_notes: str
    live_branch: str
    for_local_cs: bool
    def __init__(self, appid: _Optional[int] = ..., depot_manifests: _Optional[_Iterable[_Union[CContentBuilder_CommitAppBuild_Request.Depots, _Mapping]]] = ..., build_notes: _Optional[str] = ..., live_branch: _Optional[str] = ..., for_local_cs: bool = ...) -> None: ...

class CContentBuilder_CommitAppBuild_Response(_message.Message):
    __slots__ = ("buildid",)
    BUILDID_FIELD_NUMBER: _ClassVar[int]
    buildid: int
    def __init__(self, buildid: _Optional[int] = ...) -> None: ...

class CContentBuilder_SignInstallScript_Request(_message.Message):
    __slots__ = ("appid", "depotid", "install_script")
    APPID_FIELD_NUMBER: _ClassVar[int]
    DEPOTID_FIELD_NUMBER: _ClassVar[int]
    INSTALL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    appid: int
    depotid: int
    install_script: str
    def __init__(self, appid: _Optional[int] = ..., depotid: _Optional[int] = ..., install_script: _Optional[str] = ...) -> None: ...

class CContentBuilder_SignInstallScript_Response(_message.Message):
    __slots__ = ("signed_install_script",)
    SIGNED_INSTALL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    signed_install_script: str
    def __init__(self, signed_install_script: _Optional[str] = ...) -> None: ...

class ContentBuilder(_service.service): ...

class ContentBuilder_Stub(ContentBuilder): ...
