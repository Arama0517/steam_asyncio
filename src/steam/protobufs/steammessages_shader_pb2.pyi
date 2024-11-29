import steammessages_base_pb2 as _steammessages_base_pb2
import steammessages_unified_base_pb2 as _steammessages_unified_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import service as _service
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CShader_GetShaderReportingCadence_Request(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CShader_GetShaderReportingCadence_Response(_message.Message):
    __slots__ = ("rereport_time_threshold", "percent_to_rereport")
    REREPORT_TIME_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PERCENT_TO_REREPORT_FIELD_NUMBER: _ClassVar[int]
    rereport_time_threshold: int
    percent_to_rereport: int
    def __init__(self, rereport_time_threshold: _Optional[int] = ..., percent_to_rereport: _Optional[int] = ...) -> None: ...

class CShader_RegisterShader_Request(_message.Message):
    __slots__ = ("appid", "gpu_desc", "driver_desc", "shaders")
    class Shader(_message.Message):
        __slots__ = ("cache_key_sha", "shader_code_sha")
        CACHE_KEY_SHA_FIELD_NUMBER: _ClassVar[int]
        SHADER_CODE_SHA_FIELD_NUMBER: _ClassVar[int]
        cache_key_sha: bytes
        shader_code_sha: bytes
        def __init__(self, cache_key_sha: _Optional[bytes] = ..., shader_code_sha: _Optional[bytes] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    GPU_DESC_FIELD_NUMBER: _ClassVar[int]
    DRIVER_DESC_FIELD_NUMBER: _ClassVar[int]
    SHADERS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    gpu_desc: str
    driver_desc: str
    shaders: _containers.RepeatedCompositeFieldContainer[CShader_RegisterShader_Request.Shader]
    def __init__(self, appid: _Optional[int] = ..., gpu_desc: _Optional[str] = ..., driver_desc: _Optional[str] = ..., shaders: _Optional[_Iterable[_Union[CShader_RegisterShader_Request.Shader, _Mapping]]] = ...) -> None: ...

class CShader_RegisterShader_Response(_message.Message):
    __slots__ = ("requested_codeids",)
    REQUESTED_CODEIDS_FIELD_NUMBER: _ClassVar[int]
    requested_codeids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, requested_codeids: _Optional[_Iterable[int]] = ...) -> None: ...

class CShader_SendShader_Request(_message.Message):
    __slots__ = ("appid", "shaders")
    class ShaderCode(_message.Message):
        __slots__ = ("shader_code_sha", "shader_code")
        SHADER_CODE_SHA_FIELD_NUMBER: _ClassVar[int]
        SHADER_CODE_FIELD_NUMBER: _ClassVar[int]
        shader_code_sha: bytes
        shader_code: bytes
        def __init__(self, shader_code_sha: _Optional[bytes] = ..., shader_code: _Optional[bytes] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    SHADERS_FIELD_NUMBER: _ClassVar[int]
    appid: int
    shaders: _containers.RepeatedCompositeFieldContainer[CShader_SendShader_Request.ShaderCode]
    def __init__(self, appid: _Optional[int] = ..., shaders: _Optional[_Iterable[_Union[CShader_SendShader_Request.ShaderCode, _Mapping]]] = ...) -> None: ...

class CShader_SendShader_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CShader_GetBucketManifest_Request(_message.Message):
    __slots__ = ("appid", "gpu_desc", "driver_desc")
    APPID_FIELD_NUMBER: _ClassVar[int]
    GPU_DESC_FIELD_NUMBER: _ClassVar[int]
    DRIVER_DESC_FIELD_NUMBER: _ClassVar[int]
    appid: int
    gpu_desc: str
    driver_desc: str
    def __init__(self, appid: _Optional[int] = ..., gpu_desc: _Optional[str] = ..., driver_desc: _Optional[str] = ...) -> None: ...

class CShader_GetBucketManifest_Response(_message.Message):
    __slots__ = ("manifestid", "depotsize", "bucketid")
    MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    DEPOTSIZE_FIELD_NUMBER: _ClassVar[int]
    BUCKETID_FIELD_NUMBER: _ClassVar[int]
    manifestid: int
    depotsize: int
    bucketid: int
    def __init__(self, manifestid: _Optional[int] = ..., depotsize: _Optional[int] = ..., bucketid: _Optional[int] = ...) -> None: ...

class CShader_GetStaleBucket_Request(_message.Message):
    __slots__ = ("gpu_desc", "driver_desc")
    GPU_DESC_FIELD_NUMBER: _ClassVar[int]
    DRIVER_DESC_FIELD_NUMBER: _ClassVar[int]
    gpu_desc: str
    driver_desc: str
    def __init__(self, gpu_desc: _Optional[str] = ..., driver_desc: _Optional[str] = ...) -> None: ...

class CShader_GetStaleBucket_Response(_message.Message):
    __slots__ = ("bucketid", "appid", "manifestid", "gpu_desc", "driver_desc", "depot_encryption_key")
    BUCKETID_FIELD_NUMBER: _ClassVar[int]
    APPID_FIELD_NUMBER: _ClassVar[int]
    MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    GPU_DESC_FIELD_NUMBER: _ClassVar[int]
    DRIVER_DESC_FIELD_NUMBER: _ClassVar[int]
    DEPOT_ENCRYPTION_KEY_FIELD_NUMBER: _ClassVar[int]
    bucketid: int
    appid: int
    manifestid: int
    gpu_desc: str
    driver_desc: str
    depot_encryption_key: bytes
    def __init__(self, bucketid: _Optional[int] = ..., appid: _Optional[int] = ..., manifestid: _Optional[int] = ..., gpu_desc: _Optional[str] = ..., driver_desc: _Optional[str] = ..., depot_encryption_key: _Optional[bytes] = ...) -> None: ...

class CShader_ReportExternalBuild_Request(_message.Message):
    __slots__ = ("appid", "gpu_desc", "driver_desc", "manifestid", "source_gpu_desc", "source_driver_desc", "depotsize")
    APPID_FIELD_NUMBER: _ClassVar[int]
    GPU_DESC_FIELD_NUMBER: _ClassVar[int]
    DRIVER_DESC_FIELD_NUMBER: _ClassVar[int]
    MANIFESTID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GPU_DESC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DRIVER_DESC_FIELD_NUMBER: _ClassVar[int]
    DEPOTSIZE_FIELD_NUMBER: _ClassVar[int]
    appid: int
    gpu_desc: str
    driver_desc: str
    manifestid: int
    source_gpu_desc: str
    source_driver_desc: str
    depotsize: int
    def __init__(self, appid: _Optional[int] = ..., gpu_desc: _Optional[str] = ..., driver_desc: _Optional[str] = ..., manifestid: _Optional[int] = ..., source_gpu_desc: _Optional[str] = ..., source_driver_desc: _Optional[str] = ..., depotsize: _Optional[int] = ...) -> None: ...

class CShader_ReportExternalBuild_Response(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Shader(_service.service): ...

class Shader_Stub(Shader): ...
