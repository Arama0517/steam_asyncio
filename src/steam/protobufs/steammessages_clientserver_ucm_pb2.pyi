import steammessages_base_pb2 as _steammessages_base_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CMsgClientUCMAddScreenshot(_message.Message):
    __slots__ = ("appid", "filename", "thumbname", "vr_filename", "rtime32_created", "width", "height", "permissions", "caption", "shortcut_name", "tag", "tagged_steamid", "spoiler_tag", "tagged_publishedfileid")
    class Tag(_message.Message):
        __slots__ = ("tag_name", "tag_value")
        TAG_NAME_FIELD_NUMBER: _ClassVar[int]
        TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
        tag_name: str
        tag_value: str
        def __init__(self, tag_name: _Optional[str] = ..., tag_value: _Optional[str] = ...) -> None: ...
    APPID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    THUMBNAME_FIELD_NUMBER: _ClassVar[int]
    VR_FILENAME_FIELD_NUMBER: _ClassVar[int]
    RTIME32_CREATED_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    SHORTCUT_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TAGGED_STEAMID_FIELD_NUMBER: _ClassVar[int]
    SPOILER_TAG_FIELD_NUMBER: _ClassVar[int]
    TAGGED_PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    appid: int
    filename: str
    thumbname: str
    vr_filename: str
    rtime32_created: int
    width: int
    height: int
    permissions: int
    caption: str
    shortcut_name: str
    tag: _containers.RepeatedCompositeFieldContainer[CMsgClientUCMAddScreenshot.Tag]
    tagged_steamid: _containers.RepeatedScalarFieldContainer[int]
    spoiler_tag: bool
    tagged_publishedfileid: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, appid: _Optional[int] = ..., filename: _Optional[str] = ..., thumbname: _Optional[str] = ..., vr_filename: _Optional[str] = ..., rtime32_created: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., permissions: _Optional[int] = ..., caption: _Optional[str] = ..., shortcut_name: _Optional[str] = ..., tag: _Optional[_Iterable[_Union[CMsgClientUCMAddScreenshot.Tag, _Mapping]]] = ..., tagged_steamid: _Optional[_Iterable[int]] = ..., spoiler_tag: bool = ..., tagged_publishedfileid: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgClientUCMAddScreenshotResponse(_message.Message):
    __slots__ = ("eresult", "screenshotid", "publishedfileid")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    SCREENSHOTID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDFILEID_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    screenshotid: int
    publishedfileid: int
    def __init__(self, eresult: _Optional[int] = ..., screenshotid: _Optional[int] = ..., publishedfileid: _Optional[int] = ...) -> None: ...

class CMsgClientUCMDeleteScreenshot(_message.Message):
    __slots__ = ("screenshotid",)
    SCREENSHOTID_FIELD_NUMBER: _ClassVar[int]
    screenshotid: int
    def __init__(self, screenshotid: _Optional[int] = ...) -> None: ...

class CMsgClientUCMDeleteScreenshotResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientUCMPublishFile(_message.Message):
    __slots__ = ("app_id", "file_name", "preview_file_name", "consumer_app_id", "title", "description", "tags", "workshop_file", "visibility", "file_type", "url", "video_provider", "video_account_name", "video_identifier", "in_progress")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_APP_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    WORKSHOP_FILE_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    FILE_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    file_name: str
    preview_file_name: str
    consumer_app_id: int
    title: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    workshop_file: bool
    visibility: int
    file_type: int
    url: str
    video_provider: int
    video_account_name: str
    video_identifier: str
    in_progress: bool
    def __init__(self, app_id: _Optional[int] = ..., file_name: _Optional[str] = ..., preview_file_name: _Optional[str] = ..., consumer_app_id: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., workshop_file: bool = ..., visibility: _Optional[int] = ..., file_type: _Optional[int] = ..., url: _Optional[str] = ..., video_provider: _Optional[int] = ..., video_account_name: _Optional[str] = ..., video_identifier: _Optional[str] = ..., in_progress: bool = ...) -> None: ...

class CMsgClientUCMPublishFileResponse(_message.Message):
    __slots__ = ("eresult", "published_file_id", "needs_workshop_legal_agreement_acceptance")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    NEEDS_WORKSHOP_LEGAL_AGREEMENT_ACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    published_file_id: int
    needs_workshop_legal_agreement_acceptance: bool
    def __init__(self, eresult: _Optional[int] = ..., published_file_id: _Optional[int] = ..., needs_workshop_legal_agreement_acceptance: bool = ...) -> None: ...

class CMsgClientUCMUpdatePublishedFile(_message.Message):
    __slots__ = ("app_id", "published_file_id", "file_name", "preview_file_name", "title", "description", "tags", "visibility", "update_file", "update_preview_file", "update_title", "update_description", "update_tags", "update_visibility", "change_description", "update_url", "url", "update_content_manifest", "content_manifest", "metadata", "update_metadata", "language", "removed_kvtags", "kvtags", "previews", "previews_to_remove", "clear_in_progress", "remove_all_kvtags", "content_descriptors_to_add", "content_descriptors_to_remove", "allow_admin_tags", "external_asset_id", "game_branch_min", "game_branch_max")
    class KeyValueTag(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class AdditionalPreview(_message.Message):
        __slots__ = ("original_file_name", "internal_file_name", "videoid", "preview_type", "update_index")
        ORIGINAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        VIDEOID_FIELD_NUMBER: _ClassVar[int]
        PREVIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        original_file_name: str
        internal_file_name: str
        videoid: str
        preview_type: int
        update_index: int
        def __init__(self, original_file_name: _Optional[str] = ..., internal_file_name: _Optional[str] = ..., videoid: _Optional[str] = ..., preview_type: _Optional[int] = ..., update_index: _Optional[int] = ...) -> None: ...
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PREVIEW_FILE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TITLE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TAGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    CHANGE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_URL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CONTENT_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MANIFEST_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    REMOVED_KVTAGS_FIELD_NUMBER: _ClassVar[int]
    KVTAGS_FIELD_NUMBER: _ClassVar[int]
    PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    PREVIEWS_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_ALL_KVTAGS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTORS_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    CONTENT_DESCRIPTORS_TO_REMOVE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ADMIN_TAGS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ASSET_ID_FIELD_NUMBER: _ClassVar[int]
    GAME_BRANCH_MIN_FIELD_NUMBER: _ClassVar[int]
    GAME_BRANCH_MAX_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    published_file_id: int
    file_name: str
    preview_file_name: str
    title: str
    description: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    visibility: int
    update_file: bool
    update_preview_file: bool
    update_title: bool
    update_description: bool
    update_tags: bool
    update_visibility: bool
    change_description: str
    update_url: bool
    url: str
    update_content_manifest: bool
    content_manifest: int
    metadata: str
    update_metadata: bool
    language: int
    removed_kvtags: _containers.RepeatedScalarFieldContainer[str]
    kvtags: _containers.RepeatedCompositeFieldContainer[CMsgClientUCMUpdatePublishedFile.KeyValueTag]
    previews: _containers.RepeatedCompositeFieldContainer[CMsgClientUCMUpdatePublishedFile.AdditionalPreview]
    previews_to_remove: _containers.RepeatedScalarFieldContainer[int]
    clear_in_progress: bool
    remove_all_kvtags: bool
    content_descriptors_to_add: _containers.RepeatedScalarFieldContainer[int]
    content_descriptors_to_remove: _containers.RepeatedScalarFieldContainer[int]
    allow_admin_tags: bool
    external_asset_id: int
    game_branch_min: str
    game_branch_max: str
    def __init__(self, app_id: _Optional[int] = ..., published_file_id: _Optional[int] = ..., file_name: _Optional[str] = ..., preview_file_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., visibility: _Optional[int] = ..., update_file: bool = ..., update_preview_file: bool = ..., update_title: bool = ..., update_description: bool = ..., update_tags: bool = ..., update_visibility: bool = ..., change_description: _Optional[str] = ..., update_url: bool = ..., url: _Optional[str] = ..., update_content_manifest: bool = ..., content_manifest: _Optional[int] = ..., metadata: _Optional[str] = ..., update_metadata: bool = ..., language: _Optional[int] = ..., removed_kvtags: _Optional[_Iterable[str]] = ..., kvtags: _Optional[_Iterable[_Union[CMsgClientUCMUpdatePublishedFile.KeyValueTag, _Mapping]]] = ..., previews: _Optional[_Iterable[_Union[CMsgClientUCMUpdatePublishedFile.AdditionalPreview, _Mapping]]] = ..., previews_to_remove: _Optional[_Iterable[int]] = ..., clear_in_progress: bool = ..., remove_all_kvtags: bool = ..., content_descriptors_to_add: _Optional[_Iterable[int]] = ..., content_descriptors_to_remove: _Optional[_Iterable[int]] = ..., allow_admin_tags: bool = ..., external_asset_id: _Optional[int] = ..., game_branch_min: _Optional[str] = ..., game_branch_max: _Optional[str] = ...) -> None: ...

class CMsgClientUCMUpdatePublishedFileResponse(_message.Message):
    __slots__ = ("eresult", "needs_workshop_legal_agreement_acceptance")
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    NEEDS_WORKSHOP_LEGAL_AGREEMENT_ACCEPTANCE_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    needs_workshop_legal_agreement_acceptance: bool
    def __init__(self, eresult: _Optional[int] = ..., needs_workshop_legal_agreement_acceptance: bool = ...) -> None: ...

class CMsgClientUCMDeletePublishedFile(_message.Message):
    __slots__ = ("published_file_id", "app_id")
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    published_file_id: int
    app_id: int
    def __init__(self, published_file_id: _Optional[int] = ..., app_id: _Optional[int] = ...) -> None: ...

class CMsgClientUCMDeletePublishedFileResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientUCMEnumerateUserSubscribedFilesWithUpdates(_message.Message):
    __slots__ = ("app_id", "start_index", "start_time", "desired_revision")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_REVISION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    start_index: int
    start_time: int
    desired_revision: int
    def __init__(self, app_id: _Optional[int] = ..., start_index: _Optional[int] = ..., start_time: _Optional[int] = ..., desired_revision: _Optional[int] = ...) -> None: ...

class CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse(_message.Message):
    __slots__ = ("eresult", "subscribed_files", "total_results")
    class AuthorSnapshot(_message.Message):
        __slots__ = ("timestamp", "game_branch_min", "game_branch_max", "manifestid")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        GAME_BRANCH_MIN_FIELD_NUMBER: _ClassVar[int]
        GAME_BRANCH_MAX_FIELD_NUMBER: _ClassVar[int]
        MANIFESTID_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        game_branch_min: str
        game_branch_max: str
        manifestid: int
        def __init__(self, timestamp: _Optional[int] = ..., game_branch_min: _Optional[str] = ..., game_branch_max: _Optional[str] = ..., manifestid: _Optional[int] = ...) -> None: ...
    class PublishedFileId(_message.Message):
        __slots__ = ("published_file_id", "rtime32_subscribed", "appid", "file_hcontent", "file_size", "rtime32_last_updated", "is_depot_content", "author_snapshots")
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        RTIME32_SUBSCRIBED_FIELD_NUMBER: _ClassVar[int]
        APPID_FIELD_NUMBER: _ClassVar[int]
        FILE_HCONTENT_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
        RTIME32_LAST_UPDATED_FIELD_NUMBER: _ClassVar[int]
        IS_DEPOT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        AUTHOR_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        rtime32_subscribed: int
        appid: int
        file_hcontent: int
        file_size: int
        rtime32_last_updated: int
        is_depot_content: bool
        author_snapshots: _containers.RepeatedCompositeFieldContainer[CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse.AuthorSnapshot]
        def __init__(self, published_file_id: _Optional[int] = ..., rtime32_subscribed: _Optional[int] = ..., appid: _Optional[int] = ..., file_hcontent: _Optional[int] = ..., file_size: _Optional[int] = ..., rtime32_last_updated: _Optional[int] = ..., is_depot_content: bool = ..., author_snapshots: _Optional[_Iterable[_Union[CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse.AuthorSnapshot, _Mapping]]] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBED_FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    subscribed_files: _containers.RepeatedCompositeFieldContainer[CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse.PublishedFileId]
    total_results: int
    def __init__(self, eresult: _Optional[int] = ..., subscribed_files: _Optional[_Iterable[_Union[CMsgClientUCMEnumerateUserSubscribedFilesWithUpdatesResponse.PublishedFileId, _Mapping]]] = ..., total_results: _Optional[int] = ...) -> None: ...

class CMsgClientUCMPublishedFileUpdated(_message.Message):
    __slots__ = ("published_file_id", "app_id", "time_updated", "hcontent", "file_size", "is_depot_content", "revision")
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
    HCONTENT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    IS_DEPOT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    published_file_id: int
    app_id: int
    time_updated: int
    hcontent: int
    file_size: int
    is_depot_content: bool
    revision: int
    def __init__(self, published_file_id: _Optional[int] = ..., app_id: _Optional[int] = ..., time_updated: _Optional[int] = ..., hcontent: _Optional[int] = ..., file_size: _Optional[int] = ..., is_depot_content: bool = ..., revision: _Optional[int] = ...) -> None: ...

class CMsgClientWorkshopItemChangesRequest(_message.Message):
    __slots__ = ("app_id", "last_time_updated", "num_items_needed")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
    NUM_ITEMS_NEEDED_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    last_time_updated: int
    num_items_needed: int
    def __init__(self, app_id: _Optional[int] = ..., last_time_updated: _Optional[int] = ..., num_items_needed: _Optional[int] = ...) -> None: ...

class CMsgClientWorkshopItemChangesResponse(_message.Message):
    __slots__ = ("eresult", "update_time", "workshop_items")
    class WorkshopItemInfo(_message.Message):
        __slots__ = ("published_file_id", "time_updated", "manifest_id")
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_UPDATED_FIELD_NUMBER: _ClassVar[int]
        MANIFEST_ID_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        time_updated: int
        manifest_id: int
        def __init__(self, published_file_id: _Optional[int] = ..., time_updated: _Optional[int] = ..., manifest_id: _Optional[int] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    WORKSHOP_ITEMS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    update_time: int
    workshop_items: _containers.RepeatedCompositeFieldContainer[CMsgClientWorkshopItemChangesResponse.WorkshopItemInfo]
    def __init__(self, eresult: _Optional[int] = ..., update_time: _Optional[int] = ..., workshop_items: _Optional[_Iterable[_Union[CMsgClientWorkshopItemChangesResponse.WorkshopItemInfo, _Mapping]]] = ...) -> None: ...

class CMsgClientUCMSetUserPublishedFileAction(_message.Message):
    __slots__ = ("published_file_id", "app_id", "action")
    PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    published_file_id: int
    app_id: int
    action: int
    def __init__(self, published_file_id: _Optional[int] = ..., app_id: _Optional[int] = ..., action: _Optional[int] = ...) -> None: ...

class CMsgClientUCMSetUserPublishedFileActionResponse(_message.Message):
    __slots__ = ("eresult",)
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    def __init__(self, eresult: _Optional[int] = ...) -> None: ...

class CMsgClientUCMEnumeratePublishedFilesByUserAction(_message.Message):
    __slots__ = ("app_id", "start_index", "action")
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    START_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    app_id: int
    start_index: int
    action: int
    def __init__(self, app_id: _Optional[int] = ..., start_index: _Optional[int] = ..., action: _Optional[int] = ...) -> None: ...

class CMsgClientUCMEnumeratePublishedFilesByUserActionResponse(_message.Message):
    __slots__ = ("eresult", "published_files", "total_results")
    class PublishedFileId(_message.Message):
        __slots__ = ("published_file_id", "rtime_time_stamp")
        PUBLISHED_FILE_ID_FIELD_NUMBER: _ClassVar[int]
        RTIME_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
        published_file_id: int
        rtime_time_stamp: int
        def __init__(self, published_file_id: _Optional[int] = ..., rtime_time_stamp: _Optional[int] = ...) -> None: ...
    ERESULT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_FILES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    eresult: int
    published_files: _containers.RepeatedCompositeFieldContainer[CMsgClientUCMEnumeratePublishedFilesByUserActionResponse.PublishedFileId]
    total_results: int
    def __init__(self, eresult: _Optional[int] = ..., published_files: _Optional[_Iterable[_Union[CMsgClientUCMEnumeratePublishedFilesByUserActionResponse.PublishedFileId, _Mapping]]] = ..., total_results: _Optional[int] = ...) -> None: ...

class CMsgClientScreenshotsChanged(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
