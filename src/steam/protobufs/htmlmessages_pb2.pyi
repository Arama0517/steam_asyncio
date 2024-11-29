import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EJSRegisterMethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    k_EJSRegisterMethodType_Invalid: _ClassVar[EJSRegisterMethodType]
    k_EJSRegisterMethodType_Function: _ClassVar[EJSRegisterMethodType]
    k_EJSRegisterMethodType_Callback: _ClassVar[EJSRegisterMethodType]
    k_EJSRegisterMethodType_Promise: _ClassVar[EJSRegisterMethodType]
k_EJSRegisterMethodType_Invalid: EJSRegisterMethodType
k_EJSRegisterMethodType_Function: EJSRegisterMethodType
k_EJSRegisterMethodType_Callback: EJSRegisterMethodType
k_EJSRegisterMethodType_Promise: EJSRegisterMethodType

class CMsgKeyUp(_message.Message):
    __slots__ = ("browser_handle", "keyCode", "modifiers", "nativeKeyCode")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    KEYCODE_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    NATIVEKEYCODE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    keyCode: int
    modifiers: int
    nativeKeyCode: int
    def __init__(self, browser_handle: _Optional[int] = ..., keyCode: _Optional[int] = ..., modifiers: _Optional[int] = ..., nativeKeyCode: _Optional[int] = ...) -> None: ...

class CMsgKeyDown(_message.Message):
    __slots__ = ("browser_handle", "keyCode", "modifiers", "is_system_key", "nativeKeyCode")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    KEYCODE_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_KEY_FIELD_NUMBER: _ClassVar[int]
    NATIVEKEYCODE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    keyCode: int
    modifiers: int
    is_system_key: bool
    nativeKeyCode: int
    def __init__(self, browser_handle: _Optional[int] = ..., keyCode: _Optional[int] = ..., modifiers: _Optional[int] = ..., is_system_key: bool = ..., nativeKeyCode: _Optional[int] = ...) -> None: ...

class CMsgKeyChar(_message.Message):
    __slots__ = ("browser_handle", "unichar", "modifiers", "keyCode", "nativeKeyCode")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    UNICHAR_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    KEYCODE_FIELD_NUMBER: _ClassVar[int]
    NATIVEKEYCODE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    unichar: int
    modifiers: int
    keyCode: int
    nativeKeyCode: int
    def __init__(self, browser_handle: _Optional[int] = ..., unichar: _Optional[int] = ..., modifiers: _Optional[int] = ..., keyCode: _Optional[int] = ..., nativeKeyCode: _Optional[int] = ...) -> None: ...

class CMsgMouseDown(_message.Message):
    __slots__ = ("browser_handle", "mouse_button", "modifiers")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MOUSE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    mouse_button: int
    modifiers: int
    def __init__(self, browser_handle: _Optional[int] = ..., mouse_button: _Optional[int] = ..., modifiers: _Optional[int] = ...) -> None: ...

class CMsgMouseUp(_message.Message):
    __slots__ = ("browser_handle", "mouse_button", "modifiers", "is_off_panel", "x", "y")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MOUSE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    IS_OFF_PANEL_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    mouse_button: int
    modifiers: int
    is_off_panel: bool
    x: int
    y: int
    def __init__(self, browser_handle: _Optional[int] = ..., mouse_button: _Optional[int] = ..., modifiers: _Optional[int] = ..., is_off_panel: bool = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class CMsgMouseDblClick(_message.Message):
    __slots__ = ("browser_handle", "mouse_button", "modifiers")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MOUSE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    mouse_button: int
    modifiers: int
    def __init__(self, browser_handle: _Optional[int] = ..., mouse_button: _Optional[int] = ..., modifiers: _Optional[int] = ...) -> None: ...

class CMsgMouseWheel(_message.Message):
    __slots__ = ("browser_handle", "deltax", "deltay", "modifiers")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DELTAX_FIELD_NUMBER: _ClassVar[int]
    DELTAY_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    deltax: int
    deltay: int
    modifiers: int
    def __init__(self, browser_handle: _Optional[int] = ..., deltax: _Optional[int] = ..., deltay: _Optional[int] = ..., modifiers: _Optional[int] = ...) -> None: ...

class CMsgMouseMove(_message.Message):
    __slots__ = ("browser_handle", "x", "y", "modifiers")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    MODIFIERS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    modifiers: int
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., modifiers: _Optional[int] = ...) -> None: ...

class CMsgMouseLeave(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgBrowserCreate(_message.Message):
    __slots__ = ("request_id", "useragent", "user_css", "native_dropdowns", "dpi_scaling", "offscreen", "initial_width", "initial_height", "window_icon", "borderless", "vroverlay_key", "browser_type", "initial_top", "initial_left", "only_allow_trusted_popups", "initial_url", "hwnd_parent", "creation_flags")
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    USERAGENT_FIELD_NUMBER: _ClassVar[int]
    USER_CSS_FIELD_NUMBER: _ClassVar[int]
    NATIVE_DROPDOWNS_FIELD_NUMBER: _ClassVar[int]
    DPI_SCALING_FIELD_NUMBER: _ClassVar[int]
    OFFSCREEN_FIELD_NUMBER: _ClassVar[int]
    INITIAL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    INITIAL_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_ICON_FIELD_NUMBER: _ClassVar[int]
    BORDERLESS_FIELD_NUMBER: _ClassVar[int]
    VROVERLAY_KEY_FIELD_NUMBER: _ClassVar[int]
    BROWSER_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_TOP_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LEFT_FIELD_NUMBER: _ClassVar[int]
    ONLY_ALLOW_TRUSTED_POPUPS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_URL_FIELD_NUMBER: _ClassVar[int]
    HWND_PARENT_FIELD_NUMBER: _ClassVar[int]
    CREATION_FLAGS_FIELD_NUMBER: _ClassVar[int]
    request_id: int
    useragent: str
    user_css: str
    native_dropdowns: bool
    dpi_scaling: float
    offscreen: bool
    initial_width: int
    initial_height: int
    window_icon: str
    borderless: bool
    vroverlay_key: str
    browser_type: int
    initial_top: int
    initial_left: int
    only_allow_trusted_popups: bool
    initial_url: str
    hwnd_parent: int
    creation_flags: int
    def __init__(self, request_id: _Optional[int] = ..., useragent: _Optional[str] = ..., user_css: _Optional[str] = ..., native_dropdowns: bool = ..., dpi_scaling: _Optional[float] = ..., offscreen: bool = ..., initial_width: _Optional[int] = ..., initial_height: _Optional[int] = ..., window_icon: _Optional[str] = ..., borderless: bool = ..., vroverlay_key: _Optional[str] = ..., browser_type: _Optional[int] = ..., initial_top: _Optional[int] = ..., initial_left: _Optional[int] = ..., only_allow_trusted_popups: bool = ..., initial_url: _Optional[str] = ..., hwnd_parent: _Optional[int] = ..., creation_flags: _Optional[int] = ...) -> None: ...

class CMsgBrowserCreateResponse(_message.Message):
    __slots__ = ("browser_handle", "request_id")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    request_id: int
    def __init__(self, browser_handle: _Optional[int] = ..., request_id: _Optional[int] = ...) -> None: ...

class CMsgBrowserRemove(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetLocalFileRequestMapping(_message.Message):
    __slots__ = ("browser_handle", "request_url", "default_local_path", "routes")
    class AdditionalRoute(_message.Message):
        __slots__ = ("relative_url", "local_path", "allowed_extensions", "url_rewrite")
        RELATIVE_URL_FIELD_NUMBER: _ClassVar[int]
        LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
        URL_REWRITE_FIELD_NUMBER: _ClassVar[int]
        relative_url: str
        local_path: str
        allowed_extensions: str
        url_rewrite: bool
        def __init__(self, relative_url: _Optional[str] = ..., local_path: _Optional[str] = ..., allowed_extensions: _Optional[str] = ..., url_rewrite: bool = ...) -> None: ...
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
    ROUTES_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    request_url: str
    default_local_path: str
    routes: _containers.RepeatedCompositeFieldContainer[CMsgSetLocalFileRequestMapping.AdditionalRoute]
    def __init__(self, browser_handle: _Optional[int] = ..., request_url: _Optional[str] = ..., default_local_path: _Optional[str] = ..., routes: _Optional[_Iterable[_Union[CMsgSetLocalFileRequestMapping.AdditionalRoute, _Mapping]]] = ...) -> None: ...

class CMsgBrowserErrorStrings(_message.Message):
    __slots__ = ("browser_handle", "title", "header", "cache_miss", "bad_url", "connection_problem", "proxy_problem", "unknown")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    CACHE_MISS_FIELD_NUMBER: _ClassVar[int]
    BAD_URL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    PROXY_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    title: str
    header: str
    cache_miss: str
    bad_url: str
    connection_problem: str
    proxy_problem: str
    unknown: str
    def __init__(self, browser_handle: _Optional[int] = ..., title: _Optional[str] = ..., header: _Optional[str] = ..., cache_miss: _Optional[str] = ..., bad_url: _Optional[str] = ..., connection_problem: _Optional[str] = ..., proxy_problem: _Optional[str] = ..., unknown: _Optional[str] = ...) -> None: ...

class CMsgBrowserSetName(_message.Message):
    __slots__ = ("browser_handle", "name")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    name: str
    def __init__(self, browser_handle: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class CMsgBrowserSize(_message.Message):
    __slots__ = ("browser_handle", "width", "height")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    width: float
    height: float
    def __init__(self, browser_handle: _Optional[int] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class CMsgBrowserSetMinSize(_message.Message):
    __slots__ = ("browser_handle", "width", "height")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    width: float
    height: float
    def __init__(self, browser_handle: _Optional[int] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class CMsgBrowserPosition(_message.Message):
    __slots__ = ("browser_handle", "x", "y", "x_local", "y_local")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    X_LOCAL_FIELD_NUMBER: _ClassVar[int]
    Y_LOCAL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: float
    y: float
    x_local: float
    y_local: float
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., x_local: _Optional[float] = ..., y_local: _Optional[float] = ...) -> None: ...

class CMsgBrowserResized(_message.Message):
    __slots__ = ("browser_handle", "x", "y", "width", "height", "dpi_horizontal", "dpi_vertical", "display_name")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DPI_HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
    DPI_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: float
    y: float
    width: float
    height: float
    dpi_horizontal: float
    dpi_vertical: float
    display_name: str
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., dpi_horizontal: _Optional[float] = ..., dpi_vertical: _Optional[float] = ..., display_name: _Optional[str] = ...) -> None: ...

class CMsgPostURL(_message.Message):
    __slots__ = ("browser_handle", "url", "post", "pageserial", "replace_entry")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    PAGESERIAL_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ENTRY_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    post: str
    pageserial: int
    replace_entry: bool
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., post: _Optional[str] = ..., pageserial: _Optional[int] = ..., replace_entry: bool = ...) -> None: ...

class CMsgAddHeader(_message.Message):
    __slots__ = ("browser_handle", "key", "value")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    key: str
    value: str
    def __init__(self, browser_handle: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CMsgStopLoad(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgReload(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgGoForward(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgGoBack(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgWasHidden(_message.Message):
    __slots__ = ("browser_handle", "hidden")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    hidden: bool
    def __init__(self, browser_handle: _Optional[int] = ..., hidden: bool = ...) -> None: ...

class CMsgSetWindowVisibility(_message.Message):
    __slots__ = ("browser_handle", "visible")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    visible: bool
    def __init__(self, browser_handle: _Optional[int] = ..., visible: bool = ...) -> None: ...

class CMsgClearHistory(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgClearAllBrowsingData(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgCopy(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgPaste(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgExecuteJavaScript(_message.Message):
    __slots__ = ("browser_handle", "script")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    script: str
    def __init__(self, browser_handle: _Optional[int] = ..., script: _Optional[str] = ...) -> None: ...

class CMsgSetFocus(_message.Message):
    __slots__ = ("browser_handle", "focus")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FOCUS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    focus: bool
    def __init__(self, browser_handle: _Optional[int] = ..., focus: bool = ...) -> None: ...

class CMsgHorizontalScrollBarSize(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgHorizontalScrollBarSizeResponse(_message.Message):
    __slots__ = ("browser_handle", "scroll_max", "scroll", "zoom", "visible", "page_size")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCROLL_MAX_FIELD_NUMBER: _ClassVar[int]
    SCROLL_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scroll_max: int
    scroll: int
    zoom: float
    visible: bool
    page_size: int
    def __init__(self, browser_handle: _Optional[int] = ..., scroll_max: _Optional[int] = ..., scroll: _Optional[int] = ..., zoom: _Optional[float] = ..., visible: bool = ..., page_size: _Optional[int] = ...) -> None: ...

class CMsgVerticalScrollBarSize(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgVerticalScrollBarSizeResponse(_message.Message):
    __slots__ = ("browser_handle", "scroll_max", "scroll", "zoom", "visible", "page_size")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCROLL_MAX_FIELD_NUMBER: _ClassVar[int]
    SCROLL_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scroll_max: int
    scroll: int
    zoom: float
    visible: bool
    page_size: int
    def __init__(self, browser_handle: _Optional[int] = ..., scroll_max: _Optional[int] = ..., scroll: _Optional[int] = ..., zoom: _Optional[float] = ..., visible: bool = ..., page_size: _Optional[int] = ...) -> None: ...

class CMsgFind(_message.Message):
    __slots__ = ("browser_handle", "find", "infind", "reverse")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FIND_FIELD_NUMBER: _ClassVar[int]
    INFIND_FIELD_NUMBER: _ClassVar[int]
    REVERSE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    find: str
    infind: bool
    reverse: bool
    def __init__(self, browser_handle: _Optional[int] = ..., find: _Optional[str] = ..., infind: bool = ..., reverse: bool = ...) -> None: ...

class CMsgStopFind(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetHorizontalScroll(_message.Message):
    __slots__ = ("browser_handle", "scroll")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCROLL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scroll: int
    def __init__(self, browser_handle: _Optional[int] = ..., scroll: _Optional[int] = ...) -> None: ...

class CMsgSetVerticalScroll(_message.Message):
    __slots__ = ("browser_handle", "scroll")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCROLL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scroll: int
    def __init__(self, browser_handle: _Optional[int] = ..., scroll: _Optional[int] = ...) -> None: ...

class CMsgSetZoomLevel(_message.Message):
    __slots__ = ("browser_handle", "zoom")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    zoom: float
    def __init__(self, browser_handle: _Optional[int] = ..., zoom: _Optional[float] = ...) -> None: ...

class CMsgViewSource(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgBrowserReady(_message.Message):
    __slots__ = ("browser_handle", "vr_overlay_key", "hwnd_browser")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VR_OVERLAY_KEY_FIELD_NUMBER: _ClassVar[int]
    HWND_BROWSER_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    vr_overlay_key: str
    hwnd_browser: int
    def __init__(self, browser_handle: _Optional[int] = ..., vr_overlay_key: _Optional[str] = ..., hwnd_browser: _Optional[int] = ...) -> None: ...

class CMsgURLChanged(_message.Message):
    __slots__ = ("browser_handle", "url", "postData", "bIsRedirect", "pagetitle", "bNewNavigation")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    POSTDATA_FIELD_NUMBER: _ClassVar[int]
    BISREDIRECT_FIELD_NUMBER: _ClassVar[int]
    PAGETITLE_FIELD_NUMBER: _ClassVar[int]
    BNEWNAVIGATION_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    postData: str
    bIsRedirect: bool
    pagetitle: str
    bNewNavigation: bool
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., postData: _Optional[str] = ..., bIsRedirect: bool = ..., pagetitle: _Optional[str] = ..., bNewNavigation: bool = ...) -> None: ...

class CHistoryEntry(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class CMsgHistoryChanged(_message.Message):
    __slots__ = ("browser_handle", "index", "entries")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    index: int
    entries: _containers.RepeatedCompositeFieldContainer[CHistoryEntry]
    def __init__(self, browser_handle: _Optional[int] = ..., index: _Optional[int] = ..., entries: _Optional[_Iterable[_Union[CHistoryEntry, _Mapping]]] = ...) -> None: ...

class CMsgLoadError(_message.Message):
    __slots__ = ("browser_handle", "error_code", "url", "error_description")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    error_code: int
    url: str
    error_description: str
    def __init__(self, browser_handle: _Optional[int] = ..., error_code: _Optional[int] = ..., url: _Optional[str] = ..., error_description: _Optional[str] = ...) -> None: ...

class CHTMLHeader(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class CHTMLPageSecurityInfo(_message.Message):
    __slots__ = ("bIsSecure", "bHasCertError", "issuerName", "certName", "certExpiry", "nCertBits", "bIsEVCert")
    BISSECURE_FIELD_NUMBER: _ClassVar[int]
    BHASCERTERROR_FIELD_NUMBER: _ClassVar[int]
    ISSUERNAME_FIELD_NUMBER: _ClassVar[int]
    CERTNAME_FIELD_NUMBER: _ClassVar[int]
    CERTEXPIRY_FIELD_NUMBER: _ClassVar[int]
    NCERTBITS_FIELD_NUMBER: _ClassVar[int]
    BISEVCERT_FIELD_NUMBER: _ClassVar[int]
    bIsSecure: bool
    bHasCertError: bool
    issuerName: str
    certName: str
    certExpiry: int
    nCertBits: int
    bIsEVCert: bool
    def __init__(self, bIsSecure: bool = ..., bHasCertError: bool = ..., issuerName: _Optional[str] = ..., certName: _Optional[str] = ..., certExpiry: _Optional[int] = ..., nCertBits: _Optional[int] = ..., bIsEVCert: bool = ...) -> None: ...

class CMsgFinishedRequest(_message.Message):
    __slots__ = ("browser_handle", "url", "pageTitle")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PAGETITLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    pageTitle: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., pageTitle: _Optional[str] = ...) -> None: ...

class CMsgLoadedRequest(_message.Message):
    __slots__ = ("browser_handle", "url", "pageTitle", "headers")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    PAGETITLE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    pageTitle: str
    headers: _containers.RepeatedCompositeFieldContainer[CHTMLHeader]
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., pageTitle: _Optional[str] = ..., headers: _Optional[_Iterable[_Union[CHTMLHeader, _Mapping]]] = ...) -> None: ...

class CMsgFavIconURLChanged(_message.Message):
    __slots__ = ("browser_handle", "urls")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URLS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    urls: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, browser_handle: _Optional[int] = ..., urls: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgPageSecurity(_message.Message):
    __slots__ = ("browser_handle", "url", "security_info")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    SECURITY_INFO_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    security_info: CHTMLPageSecurityInfo
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., security_info: _Optional[_Union[CHTMLPageSecurityInfo, _Mapping]] = ...) -> None: ...

class CMsgStartRequest(_message.Message):
    __slots__ = ("browser_handle", "url", "target", "postData", "bIsRedirect")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    POSTDATA_FIELD_NUMBER: _ClassVar[int]
    BISREDIRECT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    target: str
    postData: str
    bIsRedirect: bool
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., target: _Optional[str] = ..., postData: _Optional[str] = ..., bIsRedirect: bool = ...) -> None: ...

class CMsgStartRequestResponse(_message.Message):
    __slots__ = ("browser_handle", "bAllow")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BALLOW_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    bAllow: bool
    def __init__(self, browser_handle: _Optional[int] = ..., bAllow: bool = ...) -> None: ...

class CMsgShowPopup(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgHidePopup(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSizePopup(_message.Message):
    __slots__ = ("browser_handle", "x", "y", "wide", "tall")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDE_FIELD_NUMBER: _ClassVar[int]
    TALL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    wide: int
    tall: int
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., wide: _Optional[int] = ..., tall: _Optional[int] = ...) -> None: ...

class CMsgOpenNewTab(_message.Message):
    __slots__ = ("browser_handle", "url", "bForeground")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BFOREGROUND_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    bForeground: bool
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., bForeground: bool = ...) -> None: ...

class CMsgPopupHTMLWindow(_message.Message):
    __slots__ = ("browser_handle", "url", "x", "y", "wide", "tall", "popup_index", "trusted_creator", "name", "hwnd", "parent_popup_index")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDE_FIELD_NUMBER: _ClassVar[int]
    TALL_FIELD_NUMBER: _ClassVar[int]
    POPUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_CREATOR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HWND_FIELD_NUMBER: _ClassVar[int]
    PARENT_POPUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    x: int
    y: int
    wide: int
    tall: int
    popup_index: int
    trusted_creator: bool
    name: str
    hwnd: int
    parent_popup_index: int
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., wide: _Optional[int] = ..., tall: _Optional[int] = ..., popup_index: _Optional[int] = ..., trusted_creator: bool = ..., name: _Optional[str] = ..., hwnd: _Optional[int] = ..., parent_popup_index: _Optional[int] = ...) -> None: ...

class CMsgPopupHTMLWindowResponse(_message.Message):
    __slots__ = ("browser_handle", "bAllow")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BALLOW_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    bAllow: bool
    def __init__(self, browser_handle: _Optional[int] = ..., bAllow: bool = ...) -> None: ...

class CMsgSetHTMLTitle(_message.Message):
    __slots__ = ("browser_handle", "title")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    title: str
    def __init__(self, browser_handle: _Optional[int] = ..., title: _Optional[str] = ...) -> None: ...

class CMsgLoadingResource(_message.Message):
    __slots__ = ("browser_handle", "url")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class CMsgStatusText(_message.Message):
    __slots__ = ("browser_handle", "text")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    text: str
    def __init__(self, browser_handle: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgSetCursor(_message.Message):
    __slots__ = ("browser_handle", "cursor", "custom_data", "wide", "tall", "xhotspot", "yhotspot")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_DATA_FIELD_NUMBER: _ClassVar[int]
    WIDE_FIELD_NUMBER: _ClassVar[int]
    TALL_FIELD_NUMBER: _ClassVar[int]
    XHOTSPOT_FIELD_NUMBER: _ClassVar[int]
    YHOTSPOT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    cursor: int
    custom_data: bytes
    wide: int
    tall: int
    xhotspot: int
    yhotspot: int
    def __init__(self, browser_handle: _Optional[int] = ..., cursor: _Optional[int] = ..., custom_data: _Optional[bytes] = ..., wide: _Optional[int] = ..., tall: _Optional[int] = ..., xhotspot: _Optional[int] = ..., yhotspot: _Optional[int] = ...) -> None: ...

class CMsgFileLoadDialog(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "title", "initialFile", "accept_types", "is_save", "choose_directory", "filters")
    class Filter(_message.Message):
        __slots__ = ("name", "patterns", "is_default")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PATTERNS_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        name: str
        patterns: _containers.RepeatedScalarFieldContainer[str]
        is_default: bool
        def __init__(self, name: _Optional[str] = ..., patterns: _Optional[_Iterable[str]] = ..., is_default: bool = ...) -> None: ...
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    INITIALFILE_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_TYPES_FIELD_NUMBER: _ClassVar[int]
    IS_SAVE_FIELD_NUMBER: _ClassVar[int]
    CHOOSE_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    title: str
    initialFile: str
    accept_types: _containers.RepeatedScalarFieldContainer[str]
    is_save: bool
    choose_directory: bool
    filters: _containers.RepeatedCompositeFieldContainer[CMsgFileLoadDialog.Filter]
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., title: _Optional[str] = ..., initialFile: _Optional[str] = ..., accept_types: _Optional[_Iterable[str]] = ..., is_save: bool = ..., choose_directory: bool = ..., filters: _Optional[_Iterable[_Union[CMsgFileLoadDialog.Filter, _Mapping]]] = ...) -> None: ...

class CMsgFileLoadDialogResponse(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "bsuccess", "files")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BSUCCESS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    bsuccess: bool
    files: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., bsuccess: bool = ..., files: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgRequestProcessInfo(_message.Message):
    __slots__ = ("requestid",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestid: int
    def __init__(self, requestid: _Optional[int] = ...) -> None: ...

class CMsgProcessInfoNotification(_message.Message):
    __slots__ = ("requestid", "gpu_status", "canvas_2d", "canvas_oop_rasterization", "direct_rendering_display_compositor", "gpu_compositing", "multiple_raster_threads", "opengl", "rasterization", "raw_draw", "skia_graphite", "video_decode", "video_encode", "vulkan", "webgl", "webgl2", "webgpu", "webnn")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    GPU_STATUS_FIELD_NUMBER: _ClassVar[int]
    CANVAS_2D_FIELD_NUMBER: _ClassVar[int]
    CANVAS_OOP_RASTERIZATION_FIELD_NUMBER: _ClassVar[int]
    DIRECT_RENDERING_DISPLAY_COMPOSITOR_FIELD_NUMBER: _ClassVar[int]
    GPU_COMPOSITING_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_RASTER_THREADS_FIELD_NUMBER: _ClassVar[int]
    OPENGL_FIELD_NUMBER: _ClassVar[int]
    RASTERIZATION_FIELD_NUMBER: _ClassVar[int]
    RAW_DRAW_FIELD_NUMBER: _ClassVar[int]
    SKIA_GRAPHITE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DECODE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_ENCODE_FIELD_NUMBER: _ClassVar[int]
    VULKAN_FIELD_NUMBER: _ClassVar[int]
    WEBGL_FIELD_NUMBER: _ClassVar[int]
    WEBGL2_FIELD_NUMBER: _ClassVar[int]
    WEBGPU_FIELD_NUMBER: _ClassVar[int]
    WEBNN_FIELD_NUMBER: _ClassVar[int]
    requestid: int
    gpu_status: _enums_pb2.EBrowserGPUStatus
    canvas_2d: _enums_pb2.EBrowserFeatureStatus
    canvas_oop_rasterization: _enums_pb2.EBrowserFeatureStatus
    direct_rendering_display_compositor: _enums_pb2.EBrowserFeatureStatus
    gpu_compositing: _enums_pb2.EBrowserFeatureStatus
    multiple_raster_threads: _enums_pb2.EBrowserFeatureStatus
    opengl: _enums_pb2.EBrowserFeatureStatus
    rasterization: _enums_pb2.EBrowserFeatureStatus
    raw_draw: _enums_pb2.EBrowserFeatureStatus
    skia_graphite: _enums_pb2.EBrowserFeatureStatus
    video_decode: _enums_pb2.EBrowserFeatureStatus
    video_encode: _enums_pb2.EBrowserFeatureStatus
    vulkan: _enums_pb2.EBrowserFeatureStatus
    webgl: _enums_pb2.EBrowserFeatureStatus
    webgl2: _enums_pb2.EBrowserFeatureStatus
    webgpu: _enums_pb2.EBrowserFeatureStatus
    webnn: _enums_pb2.EBrowserFeatureStatus
    def __init__(self, requestid: _Optional[int] = ..., gpu_status: _Optional[_Union[_enums_pb2.EBrowserGPUStatus, str]] = ..., canvas_2d: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., canvas_oop_rasterization: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., direct_rendering_display_compositor: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., gpu_compositing: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., multiple_raster_threads: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., opengl: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., rasterization: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., raw_draw: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., skia_graphite: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., video_decode: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., video_encode: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., vulkan: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., webgl: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., webgl2: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., webgpu: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ..., webnn: _Optional[_Union[_enums_pb2.EBrowserFeatureStatus, str]] = ...) -> None: ...

class CMsgShowToolTip(_message.Message):
    __slots__ = ("browser_handle", "text")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    text: str
    def __init__(self, browser_handle: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgUpdateToolTip(_message.Message):
    __slots__ = ("browser_handle", "text")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    text: str
    def __init__(self, browser_handle: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgHideToolTip(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSearchResults(_message.Message):
    __slots__ = ("browser_handle", "activeMatch", "results")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ACTIVEMATCH_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    activeMatch: int
    results: int
    def __init__(self, browser_handle: _Optional[int] = ..., activeMatch: _Optional[int] = ..., results: _Optional[int] = ...) -> None: ...

class CMsgClose(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetSharedPaintBuffers(_message.Message):
    __slots__ = ("browser_handle", "wide", "tall", "source_pid", "source_handle", "handle")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    WIDE_FIELD_NUMBER: _ClassVar[int]
    TALL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    wide: int
    tall: int
    source_pid: int
    source_handle: int
    handle: int
    def __init__(self, browser_handle: _Optional[int] = ..., wide: _Optional[int] = ..., tall: _Optional[int] = ..., source_pid: _Optional[int] = ..., source_handle: _Optional[int] = ..., handle: _Optional[int] = ...) -> None: ...

class CMsgAckSharedPaintBuffers(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgNeedsPaint(_message.Message):
    __slots__ = ("browser_handle", "scrollx", "scrolly", "pagescale", "pageserial", "avg_frame_ms", "stddev_sum_frame_ms", "long_frame_ms")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCROLLX_FIELD_NUMBER: _ClassVar[int]
    SCROLLY_FIELD_NUMBER: _ClassVar[int]
    PAGESCALE_FIELD_NUMBER: _ClassVar[int]
    PAGESERIAL_FIELD_NUMBER: _ClassVar[int]
    AVG_FRAME_MS_FIELD_NUMBER: _ClassVar[int]
    STDDEV_SUM_FRAME_MS_FIELD_NUMBER: _ClassVar[int]
    LONG_FRAME_MS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scrollx: int
    scrolly: int
    pagescale: float
    pageserial: int
    avg_frame_ms: int
    stddev_sum_frame_ms: float
    long_frame_ms: int
    def __init__(self, browser_handle: _Optional[int] = ..., scrollx: _Optional[int] = ..., scrolly: _Optional[int] = ..., pagescale: _Optional[float] = ..., pageserial: _Optional[int] = ..., avg_frame_ms: _Optional[int] = ..., stddev_sum_frame_ms: _Optional[float] = ..., long_frame_ms: _Optional[int] = ...) -> None: ...

class CMsgComboNeedsPaint(_message.Message):
    __slots__ = ("browser_handle", "rgba", "combobox_wide", "combobox_tall", "shared_memory_handle", "shared_memory_size")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    RGBA_FIELD_NUMBER: _ClassVar[int]
    COMBOBOX_WIDE_FIELD_NUMBER: _ClassVar[int]
    COMBOBOX_TALL_FIELD_NUMBER: _ClassVar[int]
    SHARED_MEMORY_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SHARED_MEMORY_SIZE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    rgba: int
    combobox_wide: int
    combobox_tall: int
    shared_memory_handle: int
    shared_memory_size: int
    def __init__(self, browser_handle: _Optional[int] = ..., rgba: _Optional[int] = ..., combobox_wide: _Optional[int] = ..., combobox_tall: _Optional[int] = ..., shared_memory_handle: _Optional[int] = ..., shared_memory_size: _Optional[int] = ...) -> None: ...

class CMsgNeedsSharedTexturePaint(_message.Message):
    __slots__ = ("browser_handle", "share_handle", "width", "height", "scrollx", "scrolly", "pagescale", "pageserial")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SHARE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SCROLLX_FIELD_NUMBER: _ClassVar[int]
    SCROLLY_FIELD_NUMBER: _ClassVar[int]
    PAGESCALE_FIELD_NUMBER: _ClassVar[int]
    PAGESERIAL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    share_handle: int
    width: int
    height: int
    scrollx: int
    scrolly: int
    pagescale: float
    pageserial: int
    def __init__(self, browser_handle: _Optional[int] = ..., share_handle: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., scrollx: _Optional[int] = ..., scrolly: _Optional[int] = ..., pagescale: _Optional[float] = ..., pageserial: _Optional[int] = ...) -> None: ...

class CMsgGetZoom(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgGetZoomResponse(_message.Message):
    __slots__ = ("browser_handle", "zoom")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    zoom: float
    def __init__(self, browser_handle: _Optional[int] = ..., zoom: _Optional[float] = ...) -> None: ...

class CMsgLinkAtPosition(_message.Message):
    __slots__ = ("browser_handle", "x", "y")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class CMsgLinkAtPositionResponse(_message.Message):
    __slots__ = ("browser_handle", "x", "y", "url", "blivelink", "binput")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BLIVELINK_FIELD_NUMBER: _ClassVar[int]
    BINPUT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    url: str
    blivelink: bool
    binput: bool
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ..., url: _Optional[str] = ..., blivelink: bool = ..., binput: bool = ...) -> None: ...

class CMsgZoomToElementAtPosition(_message.Message):
    __slots__ = ("browser_handle", "x", "y")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class CMsgZoomToElementAtPositionResponse(_message.Message):
    __slots__ = ("browser_handle", "scale", "duration")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scale: float
    duration: float
    def __init__(self, browser_handle: _Optional[int] = ..., scale: _Optional[float] = ..., duration: _Optional[float] = ...) -> None: ...

class CMsgScalePageToValue(_message.Message):
    __slots__ = ("browser_handle", "scale", "x", "y")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    scale: float
    x: float
    y: float
    def __init__(self, browser_handle: _Optional[int] = ..., scale: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class CMsgForcePopupsToDirectHWND(_message.Message):
    __slots__ = ("browser_handle", "force_direct_hwnd_popups")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FORCE_DIRECT_HWND_POPUPS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    force_direct_hwnd_popups: bool
    def __init__(self, browser_handle: _Optional[int] = ..., force_direct_hwnd_popups: bool = ...) -> None: ...

class CMsgScalePageToValueResponse(_message.Message):
    __slots__ = ("browser_handle", "zoom")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    zoom: float
    def __init__(self, browser_handle: _Optional[int] = ..., zoom: _Optional[float] = ...) -> None: ...

class CMsgSavePageToJPEG(_message.Message):
    __slots__ = ("browser_handle", "url", "filename", "width", "height")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    filename: str
    width: int
    height: int
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., filename: _Optional[str] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class CMsgSavePageToJPEGResponse(_message.Message):
    __slots__ = ("browser_handle", "url", "filename")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    filename: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class CMsgJSAlert(_message.Message):
    __slots__ = ("browser_handle", "message")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    message: str
    def __init__(self, browser_handle: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CMsgJSConfirm(_message.Message):
    __slots__ = ("browser_handle", "message")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    message: str
    def __init__(self, browser_handle: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class CMsgJSDialogResponse(_message.Message):
    __slots__ = ("browser_handle", "result")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    result: bool
    def __init__(self, browser_handle: _Optional[int] = ..., result: bool = ...) -> None: ...

class CMsgCanGoBackAndForward(_message.Message):
    __slots__ = ("browser_handle", "bgoback", "bgoforward")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BGOBACK_FIELD_NUMBER: _ClassVar[int]
    BGOFORWARD_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    bgoback: bool
    bgoforward: bool
    def __init__(self, browser_handle: _Optional[int] = ..., bgoback: bool = ..., bgoforward: bool = ...) -> None: ...

class CMsgOpenSteamURL(_message.Message):
    __slots__ = ("browser_handle", "url", "referrer")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    referrer: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., referrer: _Optional[str] = ...) -> None: ...

class CMsgSetCookie(_message.Message):
    __slots__ = ("key", "value", "path", "host", "expires", "secure", "httponly", "samesite")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_FIELD_NUMBER: _ClassVar[int]
    SECURE_FIELD_NUMBER: _ClassVar[int]
    HTTPONLY_FIELD_NUMBER: _ClassVar[int]
    SAMESITE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    path: str
    host: str
    expires: int
    secure: bool
    httponly: bool
    samesite: int
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., path: _Optional[str] = ..., host: _Optional[str] = ..., expires: _Optional[int] = ..., secure: bool = ..., httponly: bool = ..., samesite: _Optional[int] = ...) -> None: ...

class CMsgSetTargetFrameRate(_message.Message):
    __slots__ = ("browser_handle", "nTargetFrameRate")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    NTARGETFRAMERATE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    nTargetFrameRate: int
    def __init__(self, browser_handle: _Optional[int] = ..., nTargetFrameRate: _Optional[int] = ...) -> None: ...

class CMsgPauseRepaint(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgFullRepaint(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgRequestFullScreen(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgExitFullScreen(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgToggleFindInPageDialog(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetPIDShuttingDown(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgDisableBackgroundThrottling(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgAckPIDShuttingDown(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgGetCookiesForURL(_message.Message):
    __slots__ = ("browser_handle", "url")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class CCookie(_message.Message):
    __slots__ = ("name", "value", "domain", "path")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    domain: str
    path: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., domain: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CMsgGetCookiesForURLResponse(_message.Message):
    __slots__ = ("browser_handle", "url", "cookies")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    COOKIES_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    cookies: _containers.RepeatedCompositeFieldContainer[CCookie]
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ..., cookies: _Optional[_Iterable[_Union[CCookie, _Mapping]]] = ...) -> None: ...

class CMsgNodeHasFocus(_message.Message):
    __slots__ = ("browser_handle", "bInput", "name", "elementtagname", "searchbuttontext", "bHasMultipleInputs", "input_type", "bIsMainFrame")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BINPUT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ELEMENTTAGNAME_FIELD_NUMBER: _ClassVar[int]
    SEARCHBUTTONTEXT_FIELD_NUMBER: _ClassVar[int]
    BHASMULTIPLEINPUTS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BISMAINFRAME_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    bInput: bool
    name: str
    elementtagname: str
    searchbuttontext: str
    bHasMultipleInputs: bool
    input_type: str
    bIsMainFrame: bool
    def __init__(self, browser_handle: _Optional[int] = ..., bInput: bool = ..., name: _Optional[str] = ..., elementtagname: _Optional[str] = ..., searchbuttontext: _Optional[str] = ..., bHasMultipleInputs: bool = ..., input_type: _Optional[str] = ..., bIsMainFrame: bool = ...) -> None: ...

class CMsgZoomToFocusedElement(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgFocusedNodeText(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgFocusedNodeTextResponse(_message.Message):
    __slots__ = ("browser_handle", "value")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    value: str
    def __init__(self, browser_handle: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class CMsgBuildID(_message.Message):
    __slots__ = ("build_id",)
    BUILD_ID_FIELD_NUMBER: _ClassVar[int]
    build_id: int
    def __init__(self, build_id: _Optional[int] = ...) -> None: ...

class CMsgOpenDevTools(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgCloseDevTools(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgUnlockH264(_message.Message):
    __slots__ = ("browser_handle", "unlock_code")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_CODE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    unlock_code: str
    def __init__(self, browser_handle: _Optional[int] = ..., unlock_code: _Optional[str] = ...) -> None: ...

class CMsgScreenInformationChanged(_message.Message):
    __slots__ = ("browser_handle", "override_width", "override_height", "monitor_left", "monitor_top", "monitor_right", "monitor_bottom", "usable_left", "usable_top", "usable_right", "usable_bottom")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MONITOR_LEFT_FIELD_NUMBER: _ClassVar[int]
    MONITOR_TOP_FIELD_NUMBER: _ClassVar[int]
    MONITOR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MONITOR_BOTTOM_FIELD_NUMBER: _ClassVar[int]
    USABLE_LEFT_FIELD_NUMBER: _ClassVar[int]
    USABLE_TOP_FIELD_NUMBER: _ClassVar[int]
    USABLE_RIGHT_FIELD_NUMBER: _ClassVar[int]
    USABLE_BOTTOM_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    override_width: int
    override_height: int
    monitor_left: int
    monitor_top: int
    monitor_right: int
    monitor_bottom: int
    usable_left: int
    usable_top: int
    usable_right: int
    usable_bottom: int
    def __init__(self, browser_handle: _Optional[int] = ..., override_width: _Optional[int] = ..., override_height: _Optional[int] = ..., monitor_left: _Optional[int] = ..., monitor_top: _Optional[int] = ..., monitor_right: _Optional[int] = ..., monitor_bottom: _Optional[int] = ..., usable_left: _Optional[int] = ..., usable_top: _Optional[int] = ..., usable_right: _Optional[int] = ..., usable_bottom: _Optional[int] = ...) -> None: ...

class CMsgClearAllCookies(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgScreenDPI(_message.Message):
    __slots__ = ("browser_handle", "dpi_scaling")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DPI_SCALING_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    dpi_scaling: float
    def __init__(self, browser_handle: _Optional[int] = ..., dpi_scaling: _Optional[float] = ...) -> None: ...

class CMsgAckScreenDPI(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgAuthedSteamDomains(_message.Message):
    __slots__ = ("domains",)
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    domains: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domains: _Optional[_Iterable[str]] = ...) -> None: ...

class CMsgSteamAuthNeeded(_message.Message):
    __slots__ = ("filler",)
    FILLER_FIELD_NUMBER: _ClassVar[int]
    filler: bool
    def __init__(self, filler: bool = ...) -> None: ...

class CMsgSteamAuthCookiesSet(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class CMsgJSRegisterMethod(_message.Message):
    __slots__ = ("browser_handle", "name", "method_type")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_TYPE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    name: str
    method_type: EJSRegisterMethodType
    def __init__(self, browser_handle: _Optional[int] = ..., name: _Optional[str] = ..., method_type: _Optional[_Union[EJSRegisterMethodType, str]] = ...) -> None: ...

class CMsgJSValue(_message.Message):
    __slots__ = ("bool_value", "int_value", "uint_value", "double_value", "string_value", "function_handle", "bytes_value", "is_array", "array_values", "is_object", "object_properties")
    class JSObjectProperty(_message.Message):
        __slots__ = ("name", "value")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        value: CMsgJSValue
        def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[CMsgJSValue, _Mapping]] = ...) -> None: ...
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_HANDLE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_ARRAY_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUES_FIELD_NUMBER: _ClassVar[int]
    IS_OBJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    int_value: int
    uint_value: int
    double_value: float
    string_value: str
    function_handle: int
    bytes_value: bytes
    is_array: bool
    array_values: _containers.RepeatedCompositeFieldContainer[CMsgJSValue]
    is_object: bool
    object_properties: _containers.RepeatedCompositeFieldContainer[CMsgJSValue.JSObjectProperty]
    def __init__(self, bool_value: bool = ..., int_value: _Optional[int] = ..., uint_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., function_handle: _Optional[int] = ..., bytes_value: _Optional[bytes] = ..., is_array: bool = ..., array_values: _Optional[_Iterable[_Union[CMsgJSValue, _Mapping]]] = ..., is_object: bool = ..., object_properties: _Optional[_Iterable[_Union[CMsgJSValue.JSObjectProperty, _Mapping]]] = ...) -> None: ...

class CMsgJSMethodCall(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "name", "arguments")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    name: str
    arguments: _containers.RepeatedCompositeFieldContainer[CMsgJSValue]
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., name: _Optional[str] = ..., arguments: _Optional[_Iterable[_Union[CMsgJSValue, _Mapping]]] = ...) -> None: ...

class CMsgJSExecuteCallback(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "function_handle", "arguments")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    function_handle: int
    arguments: _containers.RepeatedCompositeFieldContainer[CMsgJSValue]
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., function_handle: _Optional[int] = ..., arguments: _Optional[_Iterable[_Union[CMsgJSValue, _Mapping]]] = ...) -> None: ...

class CMsgJSExecutePromise(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "promise_handle", "reject_reason", "argument")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    PROMISE_HANDLE_FIELD_NUMBER: _ClassVar[int]
    REJECT_REASON_FIELD_NUMBER: _ClassVar[int]
    ARGUMENT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    promise_handle: int
    reject_reason: str
    argument: CMsgJSValue
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., promise_handle: _Optional[int] = ..., reject_reason: _Optional[str] = ..., argument: _Optional[_Union[CMsgJSValue, _Mapping]] = ...) -> None: ...

class CMsgJSReleaseCallback(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "function_handle")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    function_handle: int
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., function_handle: _Optional[int] = ...) -> None: ...

class CMsgJSRaiseException(_message.Message):
    __slots__ = ("browser_handle", "owning_browser_handle", "exception")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    OWNING_BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    owning_browser_handle: int
    exception: str
    def __init__(self, browser_handle: _Optional[int] = ..., owning_browser_handle: _Optional[int] = ..., exception: _Optional[str] = ...) -> None: ...

class CMsgLoadLocalization(_message.Message):
    __slots__ = ("browser_handle", "localization_path", "language")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_PATH_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    localization_path: str
    language: str
    def __init__(self, browser_handle: _Optional[int] = ..., localization_path: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...

class CMsgNotifyUserActivation(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetNetFakeLocalSystemState(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: int
    def __init__(self, state: _Optional[int] = ...) -> None: ...

class CMsgDraggableRegionsChanged(_message.Message):
    __slots__ = ("browser_handle", "rects")
    class DraggableRects(_message.Message):
        __slots__ = ("x", "y", "width", "height", "draggable", "transparent")
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        DRAGGABLE_FIELD_NUMBER: _ClassVar[int]
        TRANSPARENT_FIELD_NUMBER: _ClassVar[int]
        x: int
        y: int
        width: int
        height: int
        draggable: bool
        transparent: bool
        def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., draggable: bool = ..., transparent: bool = ...) -> None: ...
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    RECTS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    rects: _containers.RepeatedCompositeFieldContainer[CMsgDraggableRegionsChanged.DraggableRects]
    def __init__(self, browser_handle: _Optional[int] = ..., rects: _Optional[_Iterable[_Union[CMsgDraggableRegionsChanged.DraggableRects, _Mapping]]] = ...) -> None: ...

class CMsgResizeGripChanged(_message.Message):
    __slots__ = ("browser_handle", "width", "height")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    width: int
    height: int
    def __init__(self, browser_handle: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class CMsgSetWindowPosition(_message.Message):
    __slots__ = ("browser_handle", "x", "y", "width", "height", "min_width", "min_height", "max_width", "max_height")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MIN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MIN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAX_WIDTH_FIELD_NUMBER: _ClassVar[int]
    MAX_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: float
    y: float
    width: float
    height: float
    min_width: float
    min_height: float
    max_width: float
    max_height: float
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., min_width: _Optional[float] = ..., min_height: _Optional[float] = ..., max_width: _Optional[float] = ..., max_height: _Optional[float] = ...) -> None: ...

class CMsgShowWindow(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgHideWindow(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgBringWindowToFront(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetForegroundWindow(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgMaximizeRestoreWindow(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgMinimizeWindow(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgShowBrowserContextMenu(_message.Message):
    __slots__ = ("browser_handle", "custom_commands", "type_flags", "page_url", "coord_x", "coord_y", "link_url", "unfiltered_link_url", "selection_text", "misspelled_word", "edit_state_flags")
    class ContextCommand(_message.Message):
        __slots__ = ("id", "label")
        ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        id: int
        label: str
        def __init__(self, id: _Optional[int] = ..., label: _Optional[str] = ...) -> None: ...
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COMMANDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    COORD_X_FIELD_NUMBER: _ClassVar[int]
    COORD_Y_FIELD_NUMBER: _ClassVar[int]
    LINK_URL_FIELD_NUMBER: _ClassVar[int]
    UNFILTERED_LINK_URL_FIELD_NUMBER: _ClassVar[int]
    SELECTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    MISSPELLED_WORD_FIELD_NUMBER: _ClassVar[int]
    EDIT_STATE_FLAGS_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    custom_commands: _containers.RepeatedCompositeFieldContainer[CMsgShowBrowserContextMenu.ContextCommand]
    type_flags: int
    page_url: str
    coord_x: int
    coord_y: int
    link_url: str
    unfiltered_link_url: str
    selection_text: str
    misspelled_word: str
    edit_state_flags: int
    def __init__(self, browser_handle: _Optional[int] = ..., custom_commands: _Optional[_Iterable[_Union[CMsgShowBrowserContextMenu.ContextCommand, _Mapping]]] = ..., type_flags: _Optional[int] = ..., page_url: _Optional[str] = ..., coord_x: _Optional[int] = ..., coord_y: _Optional[int] = ..., link_url: _Optional[str] = ..., unfiltered_link_url: _Optional[str] = ..., selection_text: _Optional[str] = ..., misspelled_word: _Optional[str] = ..., edit_state_flags: _Optional[int] = ...) -> None: ...

class CMsgHandleContextMenuCommand(_message.Message):
    __slots__ = ("browser_handle", "command_id")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    COMMAND_ID_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    command_id: int
    def __init__(self, browser_handle: _Optional[int] = ..., command_id: _Optional[int] = ...) -> None: ...

class CMsgTouchGesture(_message.Message):
    __slots__ = ("browser_handle", "id", "gesture", "x", "y", "width", "height", "tap_count", "pinch_scale")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    GESTURE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TAP_COUNT_FIELD_NUMBER: _ClassVar[int]
    PINCH_SCALE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    id: int
    gesture: int
    x: float
    y: float
    width: float
    height: float
    tap_count: int
    pinch_scale: float
    def __init__(self, browser_handle: _Optional[int] = ..., id: _Optional[int] = ..., gesture: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., tap_count: _Optional[int] = ..., pinch_scale: _Optional[float] = ...) -> None: ...

class CMsgSetTouchGesturesToCancel(_message.Message):
    __slots__ = ("browser_handle", "gestures")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    GESTURES_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    gestures: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, browser_handle: _Optional[int] = ..., gestures: _Optional[_Iterable[int]] = ...) -> None: ...

class CMsgImeSetComposition(_message.Message):
    __slots__ = ("browser_handle", "text")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    text: str
    def __init__(self, browser_handle: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgImeCommitText(_message.Message):
    __slots__ = ("browser_handle", "text")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    text: str
    def __init__(self, browser_handle: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class CMsgImeCancelComposition(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgImeCompositionRangeChanged(_message.Message):
    __slots__ = ("browser_handle", "x", "y")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class CMsgInspectElement(_message.Message):
    __slots__ = ("browser_handle", "x", "y")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    x: int
    y: int
    def __init__(self, browser_handle: _Optional[int] = ..., x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class CMsgDisableF5(_message.Message):
    __slots__ = ("browser_handle", "disable")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    disable: bool
    def __init__(self, browser_handle: _Optional[int] = ..., disable: bool = ...) -> None: ...

class CMsgStartDownload(_message.Message):
    __slots__ = ("browser_handle", "url")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class CMsgSetWindowStackingOrder(_message.Message):
    __slots__ = ("browser_handle", "estackingorder")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    ESTACKINGORDER_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    estackingorder: int
    def __init__(self, browser_handle: _Optional[int] = ..., estackingorder: _Optional[int] = ...) -> None: ...

class CMsgBrowserViewPostMessageToParentRequest(_message.Message):
    __slots__ = ("browser_handle", "message", "args", "requesting_url")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    REQUESTING_URL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    message: str
    args: str
    requesting_url: str
    def __init__(self, browser_handle: _Optional[int] = ..., message: _Optional[str] = ..., args: _Optional[str] = ..., requesting_url: _Optional[str] = ...) -> None: ...

class CMsgBlockedRequest(_message.Message):
    __slots__ = ("browser_handle", "url")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    url: str
    def __init__(self, browser_handle: _Optional[int] = ..., url: _Optional[str] = ...) -> None: ...

class CMsgBrowserFocusChanged(_message.Message):
    __slots__ = ("browser_handle", "focused")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    FOCUSED_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    focused: bool
    def __init__(self, browser_handle: _Optional[int] = ..., focused: bool = ...) -> None: ...

class CMsgSetProtocolBlockList(_message.Message):
    __slots__ = ("browser_handle", "list")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    list: str
    def __init__(self, browser_handle: _Optional[int] = ..., list: _Optional[str] = ...) -> None: ...

class CMsgSetForceDeviceScaleFactors(_message.Message):
    __slots__ = ("dpi_scale", "browser_scale")
    DPI_SCALE_FIELD_NUMBER: _ClassVar[int]
    BROWSER_SCALE_FIELD_NUMBER: _ClassVar[int]
    dpi_scale: float
    browser_scale: float
    def __init__(self, dpi_scale: _Optional[float] = ..., browser_scale: _Optional[float] = ...) -> None: ...

class CMsgSetUIMode(_message.Message):
    __slots__ = ("ui_mode",)
    UI_MODE_FIELD_NUMBER: _ClassVar[int]
    ui_mode: int
    def __init__(self, ui_mode: _Optional[int] = ...) -> None: ...

class CMsgSetSteamBetaName(_message.Message):
    __slots__ = ("steam_beta_name",)
    STEAM_BETA_NAME_FIELD_NUMBER: _ClassVar[int]
    steam_beta_name: str
    def __init__(self, steam_beta_name: _Optional[str] = ...) -> None: ...

class CMsgPopupCreated(_message.Message):
    __slots__ = ("browser_handle",)
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    def __init__(self, browser_handle: _Optional[int] = ...) -> None: ...

class CMsgSetVRKeyboardVisibility(_message.Message):
    __slots__ = ("browser_handle", "visible")
    BROWSER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    browser_handle: int
    visible: bool
    def __init__(self, browser_handle: _Optional[int] = ..., visible: bool = ...) -> None: ...

class CMsgRestartJSContext(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
