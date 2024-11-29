from steam.enums.base import SteamIntEnum


class EACState(SteamIntEnum):
    Unknown = 0
    Disconnected = 1
    Connected = 2
    ConnectedSlow = 3


class EAgreementType(SteamIntEnum):
    Invalid = -1
    GlobalSSA = 0
    ChinaSSA = 1


class EAppCloudStatus(SteamIntEnum):
    EAppCloudStatusInvalid = 0
    EAppCloudStatusDisabled = 1
    EAppCloudStatusUnknown = 2
    EAppCloudStatusSynchronized = 3
    EAppCloudStatusChecking = 4
    EAppCloudStatusOutOfSync = 5
    EAppCloudStatusUploading = 6
    EAppCloudStatusDownloading = 7
    EAppCloudStatusSyncFailed = 8
    EAppCloudStatusConflict = 9
    EAppCloudStatusPendingElsewhere = 10


class EAppControllerSupportLevel(SteamIntEnum):
    EAppControllerSupportLevelNone = 0
    EAppControllerSupportLevelPartial = 1
    EAppControllerSupportLevelFull = 2


class EAppGamepadGyroTrackpadSupportLevel(SteamIntEnum):
    EAppGamepadGyroTrackpadSupportLevelUnknown = -1
    EAppGamepadGyroTrackpadSupportLevelNoGamepad = 0
    EAppGamepadGyroTrackpadSupportLevelGamepad = 1
    EAppGamepadGyroTrackpadSupportLevelSimultaneous = 2


class EAppHDRSupport(SteamIntEnum):
    EHDRSupport_Unknown = 0
    EHDRSupport_SDR = 1
    EHDRSupport_HDR = 2
    EHDRSupport_HDR_Broken = 3
    EHDRSupport_HDR_RequiresUserAction = 4


class EAppReportType(SteamIntEnum):
    Invalid = 0
    Scam = 1
    Malware = 2
    HateSpeech = 3
    Pornography = 4
    NonLabeledAdultContent = 5
    Libelous = 6
    Offensive = 7
    ExploitsChildren = 8
    MtxWithNonSteamWalletPaymentMethods = 9
    CopyrightViolation = 10
    ViolatesLaws = 11
    Other = 12
    Broken = 13
    AIContentReport = 14


class EAsyncGameSessionUserState(SteamIntEnum):
    EAsyncGameSessionUserStateUnknown = -1
    EAsyncGameSessionUserStateWaitingForOthers = 0
    EAsyncGameSessionUserStateReadyForAction = 1
    EAsyncGameSessionUserStateDone = 2


class EAsyncGameSessionUserVisibility(SteamIntEnum):
    EAsyncGameSessionUserVisibilityEnvelopeAndSessionList = 0
    EAsyncGameSessionUserVisibilitySessionListOnly = 1
    EAsyncGameSessionUserVisibilityDismissed = 2


class EAuthenticationType(SteamIntEnum):
    Unknown = 0
    Password = 1
    QR = 2
    AccountCreation = 3
    GuestAccount = 4


EAuthSessionGuardType = SteamIntEnum(
    'EAuthSessionGuardType',
    {
        'Unknown': 0,
        'None': 1,
        'EmailCode': 2,
        'DeviceCode': 3,
        'DeviceConfirmation': 4,
        'EmailConfirmation': 5,
        'MachineToken': 6,
        'LegacyMachineAuth': 7,
    },
)


class EAuthSessionSecurityHistory(SteamIntEnum):
    Invalid = 0
    UsedPreviously = 1
    NoPriorHistory = 2


class EAuthTokenPlatformType(SteamIntEnum):
    Unknown = 0
    SteamClient = 1
    WebBrowser = 2
    MobileApp = 3


class EAuthTokenRevokeAction(SteamIntEnum):
    EAuthTokenRevokeLogout = 0
    EAuthTokenRevokePermanent = 1
    EAuthTokenRevokeReplaced = 2
    EAuthTokenRevokeSupport = 3
    EAuthTokenRevokeConsume = 4
    EAuthTokenRevokeNonRememberedLogout = 5
    EAuthTokenRevokeNonRememberedPermanent = 6
    EAuthTokenRevokeAutomatic = 7


class EAuthTokenState(SteamIntEnum):
    Invalid = 0
    New = 1
    Confirmed = 2
    Issued = 3
    Denied = 4
    LoggedOut = 5
    Consumed = 6
    Revoked = 99


class EBatteryState(SteamIntEnum):
    Unknown = 0
    Discharging = 1
    Charging = 2
    Full = 3


class EBluetoothDeviceType(SteamIntEnum):
    BluetoothDeviceType_Invalid = 0
    BluetoothDeviceType_Unknown = 1
    BluetoothDeviceType_Phone = 2
    BluetoothDeviceType_Computer = 3
    BluetoothDeviceType_Headset = 4
    BluetoothDeviceType_Headphones = 5
    BluetoothDeviceType_Speakers = 6
    BluetoothDeviceType_OtherAudio = 7
    BluetoothDeviceType_Mouse = 8
    BluetoothDeviceType_Joystick = 9
    BluetoothDeviceType_Gamepad = 10
    BluetoothDeviceType_Keyboard = 11


class EBroadcastEncoderSetting(SteamIntEnum):
    EBroadcastEncoderBestQuality = 0
    EBroadcastEncoderBestPerformance = 1


class EBroadcastPermission(SteamIntEnum):
    EBroadcastPermissionDisabled = 0
    EBroadcastPermissionFriendsApprove = 1
    EBroadcastPermissionFriendsAllowed = 2
    EBroadcastPermissionPublic = 3
    EBroadcastPermissionSubscribers = 4


class EBrowserFeatureStatus(SteamIntEnum):
    Invalid = 0
    NotFound = 1
    Unknown = 2
    DisabledSoftware = 3
    DisabledOff = 4
    DisabledOffOk = 5
    UnavailableSoftware = 6
    UnavailableOff = 7
    UnavailableOffOk = 8
    EnabledReadback = 9
    EnabledForce = 10
    Enabled = 11
    EnabledOn = 12
    EnabledForceOn = 13


class EBrowserGPUStatus(SteamIntEnum):
    Invalid = 0
    Enabled = 1
    DisabledUnknown = 2
    DisabledCrashCount = 4
    DisabledBlocklist = 5
    DisabledJSRequest = 6
    DisabledCommandLine = 7
    DisabledRuntimeDetect = 8
    DisabledChildCommandLine = 9
    DisabledCompositingCommandLine = 10


class EClientExecutionSite(SteamIntEnum):
    EClientExecutionSiteInvalid = 0
    EClientExecutionSiteSteamUI = 1
    EClientExecutionSiteClientdll = 2
    EClientExecutionSiteAny = 3


class EClientSettingStore(SteamIntEnum):
    Invalid = 0
    ConfigStore_Install = 1
    ConfigStore_UserRoaming = 2
    ConfigStore_UserLocal = 3
    Registry = 4
    CustomFunc = 5


class EClipRangeMethod(SteamIntEnum):
    CreateClipButton = 1
    Highlight = 2
    BeginEndButtons = 3
    ContextMenu = 4
    Drag = 5
    EntireClip = 6
    PhaseRecording = 7


class EClipShareMethod(SteamIntEnum):
    Chat = 1
    Clipboard = 2
    File = 3
    SendClip = 4
    SaveToMedia = 5
    CreateLink = 6


class ECloudGamingPlatform(SteamIntEnum):
    ECloudGamingPlatformNone = 0
    ECloudGamingPlatformValve = 1
    ECloudGamingPlatformNVIDIA = 2


class ECloudPendingRemoteOperation(SteamIntEnum):
    ECloudPendingRemoteOperationNone = 0
    ECloudPendingRemoteOperationAppSessionActive = 1
    ECloudPendingRemoteOperationUploadInProgress = 2
    ECloudPendingRemoteOperationUploadPending = 3
    ECloudPendingRemoteOperationAppSessionSuspended = 4


class ECloudStoragePersistState(SteamIntEnum):
    ECloudStoragePersistStatePersisted = 0
    ECloudStoragePersistStateForgotten = 1
    ECloudStoragePersistStateDeleted = 2


class EColorGamutLabelSet(SteamIntEnum):
    ColorGamutLabelSet_Default = 0
    ColorGamutLabelSet_sRGB_Native = 1
    ColorGamutLabelSet_Native_sRGB_Boosted = 2


class ECommentThreadType(SteamIntEnum):
    ECommentThreadTypeInvalid = 0
    ECommentThreadTypeScreenshot_Deprecated = 1
    ECommentThreadTypeWorkshopAccount_Developer = 2
    ECommentThreadTypeWorkshopAccount_Public = 3
    ECommentThreadTypePublishedFile_Developer = 4
    ECommentThreadTypePublishedFile_Public = 5
    ECommentThreadTypeTest = 6
    ECommentThreadTypeForumTopic = 7
    ECommentThreadTypeRecommendation = 8
    ECommentThreadTypeVideo_Deprecated = 9
    ECommentThreadTypeProfile = 10
    ECommentThreadTypeNewsPost = 11
    ECommentThreadTypeClan = 12
    ECommentThreadTypeClanAnnouncement = 13
    ECommentThreadTypeClanEvent = 14
    ECommentThreadTypeUserStatusPublished = 15
    ECommentThreadTypeUserReceivedNewGame = 16
    ECommentThreadTypePublishedFile_Announcement = 17
    ECommentThreadTypeModeratorMessage = 18
    ECommentThreadTypeClanCuratedApp = 19
    ECommentThreadTypeQAndASession = 20
    ECommentThreadTypeMax = 21


class ECommunityItemClass(SteamIntEnum):
    Invalid = 0
    Badge = 1
    GameCard = 2
    ProfileBackground = 3
    Emoticon = 4
    BoosterPack = 5
    Consumable = 6
    GameGoo = 7
    ProfileModifier = 8
    Scene = 9
    SalienItem = 10
    Sticker = 11
    ChatEffect = 12
    MiniProfileBackground = 13
    AvatarFrame = 14
    AnimatedAvatar = 15
    SteamDeckKeyboardSkin = 16
    SteamDeckStartupMovie = 17


ECompromiseDetectionType = SteamIntEnum(
    'ECompromiseDetectionType',
    {
        'None': 0,
        'TradeEvent': 1,
        'ApiCallRate': 2,
        'Manual': 3,
        'TicketAction': 4,
        'MaliciousRefund': 5,
    },
)


class EContentCheckProvider(SteamIntEnum):
    Invalid = 0
    Google_DEPRECATED = 1
    Amazon = 2
    Local = 3
    GoogleVertexAI = 4


class ECPUGovernor(SteamIntEnum):
    Invalid = 0
    Perf = 1
    Powersave = 2
    Manual = 3


class EDiskSpaceType(SteamIntEnum):
    eDiskSpaceType_Recording = 0
    eDiskSpaceType_Clip = 1


class EDisplayStatus(SteamIntEnum):
    EDisplayStatusInvalid = 0
    EDisplayStatusLaunching = 1
    EDisplayStatusUninstalling = 2
    EDisplayStatusInstalling = 3
    EDisplayStatusRunning = 4
    EDisplayStatusValidating = 5
    EDisplayStatusUpdating = 6
    EDisplayStatusDownloading = 7
    EDisplayStatusSynchronizing = 8
    EDisplayStatusReadyToInstall = 9
    EDisplayStatusReadyToPreload = 10
    EDisplayStatusReadyToLaunch = 11
    EDisplayStatusRegionRestricted = 12
    EDisplayStatusPresaleOnly = 13
    EDisplayStatusInvalidPlatform = 14
    EDisplayStatusPreloadComplete = 16
    EDisplayStatusBorrowerLocked = 17
    EDisplayStatusUpdatePaused = 18
    EDisplayStatusUpdateQueued = 19
    EDisplayStatusUpdateRequired = 20
    EDisplayStatusUpdateDisabled = 21
    EDisplayStatusDownloadPaused = 22
    EDisplayStatusDownloadQueued = 23
    EDisplayStatusDownloadRequired = 24
    EDisplayStatusDownloadDisabled = 25
    EDisplayStatusLicensePending = 26
    EDisplayStatusLicenseExpired = 27
    EDisplayStatusAvailForFree = 28
    EDisplayStatusAvailToBorrow = 29
    EDisplayStatusAvailGuestPass = 30
    EDisplayStatusPurchase = 31
    EDisplayStatusUnavailable = 32
    EDisplayStatusNotLaunchable = 33
    EDisplayStatusCloudError = 34
    EDisplayStatusCloudOutOfDate = 35
    EDisplayStatusTerminating = 36
    EDisplayStatusOwnerLocked = 37
    EDisplayStatusDownloadFailed = 38
    EDisplayStatusUpdateFailed = 39


class EExportCodec(SteamIntEnum):
    Default = 0
    H264 = 1
    H265 = 2


class EExternalSaleEventType(SteamIntEnum):
    Unknown = 0
    Publisher = 1
    Showcase = 2
    Region = 3
    Theme = 4
    Franchise = 5


class EFamilyGroupChangeLogType(SteamIntEnum):
    InvalidChangeType = 0
    FamilyGroupCreated = 1
    FamilyGroupModified = 2
    FamilyGroupDeleted = 3
    AccountInvited = 4
    InviteDeniedByGroupSize = 5
    JoinedFamilyGroup = 6
    JoinDeniedByRegionMismatch = 7
    JoinDeniedByMissingIpAddress = 8
    JoinDeniedByFamilyCooldown = 9
    JoinDeniedByUserCooldown = 10
    JoinDeniedByOtherGroup = 11
    AccountRemoved = 12
    InviteCanceled = 13
    PurchaseRequested = 14
    ParentalSettingsEnabled = 15
    ParentalSettingsDisabled = 16
    ParentalSettingsChanged = 17
    FamilyCooldownOverridesChanged = 18
    PurchaseRequestCanceled = 19
    PurchaseRequestApproved = 20
    PurchaseRequestDeclined = 21
    CooldownSkipConsumed = 22
    FamilyGroupRestored = 23
    JoinDenied = 24
    SupportForceAcceptedInvite = 25


EFamilyGroupRole = SteamIntEnum(
    'EFamilyGroupRole',
    {
        'None': 0,
        'Adult': 1,
        'Child': 2,
        'MAX': 3,
    },
)


class EFamilyGroupsTwoFactorMethod(SteamIntEnum):
    EFamilyGroupsTwoFactorMethodNone = 0
    EFamilyGroupsTwoFactorMethodMobile = 1
    EFamilyGroupsTwoFactorMethodEmail = 2


class EForumType(SteamIntEnum):
    Invalid = 0
    General = 1
    ReportedPosts = 2
    Workshop = 3
    PublishedFile = 4
    Trading = 5
    PlayTest = 6
    Event = 7
    Max = 8


class EGameRecordingType(SteamIntEnum):
    Unknown = 0
    NotRecording = 1
    ManualRecording = 2
    BackgroundRecording = 3
    Clip = 4


class EGamescopeBlurMode(SteamIntEnum):
    Disabled = 0
    IfOccluded = 1
    Always = 2


class EGpuDriverId(SteamIntEnum):
    Invalid = 0
    Unknown = 1
    AmdProprietary = 2
    AmdOpenSource = 3
    MesaRadv = 4
    NvidiaProprietary = 5
    IntelPropietary = 6
    MesaIntel = 7
    QualcommProprietary = 8
    ArmProprietary = 9
    GoogleSwiftshader = 10
    BroadcomProprietary = 11
    MesaLLVMPipe = 12
    MoltenVK = 13
    MesaTurnip = 14
    MesaPanVK = 15
    MesaVenus = 16
    MesaDozen = 17
    MesaNVK = 18
    MesaHoneyKrisp = 19


class EGPUPerformanceLevel(SteamIntEnum):
    Invalid = 0
    Auto = 1
    Manual = 2
    Low = 3
    High = 4
    Profiling = 5


class EGraphicsPerfOverlayLevel(SteamIntEnum):
    Hidden = 0
    Basic = 1
    Medium = 2
    Full = 3
    Minimal = 4


class EGRAudio(SteamIntEnum):
    Game = 0
    System = 1
    Select = 2


class EGRExportLimitType(SteamIntEnum):
    Native = 0
    FileSize = 1
    Advanced = 2


class EGRMode(SteamIntEnum):
    Never = 0
    Always = 1
    Manual = 2


class EHDRToneMapOperator(SteamIntEnum):
    Invalid = 0
    Uncharted = 1
    Reinhard = 2


EHDRVisualization = SteamIntEnum(
    'EHDRVisualization',
    {
        'None': 0,
        'Heatmap': 1,
        'Analysis': 2,
        'HeatmapExtended': 3,
        'HeatmapClassic': 4,
    },
)


class EJSRegisterMethodType(SteamIntEnum):
    Invalid = 0
    Function = 1
    Callback = 2
    Promise = 3


class ENewSteamAnnouncementState(SteamIntEnum):
    Invalid = 0
    AllRead = 1
    NewAnnouncement = 2
    FeaturedAnnouncement = 3


class ENotificationSetting(SteamIntEnum):
    ENotificationSettingNotifyUseDefault = 0
    ENotificationSettingAlways = 1
    ENotificationSettingNever = 2


class EOSBranch(SteamIntEnum):
    Unknown = 0
    Release = 1
    ReleaseCandidate = 2
    Beta = 3
    BetaCandidate = 4
    Preview = 5
    PreviewCandidate = 6
    Main = 7
    Staging = 8


class EOverlayToggleBarLocation(SteamIntEnum):
    Bottom = 0
    Left = 1
    Right = 2
    Top = 3


class EPartnerEventDisplayLocation(SteamIntEnum):
    Invalid = 0
    AppDetailsSpotlight = 1
    LibraryOverview = 2
    StoreAppPage = 3
    EventScroller = 4
    AppDetailsActivity = 5
    CommunityHub = 6
    StoreFrontPage = 7
    NewsHub = 8
    GamepadHome = 9
    StoreHub = 10


EPartnerLinkTrackingBackfillSource = SteamIntEnum(
    'EPartnerLinkTrackingBackfillSource',
    {
        'None': 0,
        'Web': 1,
        'Mobile': 2,
        'Desktop': 3,
    },
)


class EPhaseResultType(SteamIntEnum):
    Automatic = 1
    Blank = 2
    API = 3


class EPlaytestStatus(SteamIntEnum):
    ETesterStatusNone = 0
    ETesterStatusPending = 1
    ETesterStatusInvited = 2
    ETesterStatusGranted = 3


class EProfileCustomizationStyle(SteamIntEnum):
    EProfileCustomizationStyleDefault = 0
    EProfileCustomizationStyleSelected = 1
    EProfileCustomizationStyleRarest = 2
    EProfileCustomizationStyleMostRecent = 3
    EProfileCustomizationStyleRandom = 4
    EProfileCustomizationStyleHighestRated = 5


class EProfileCustomizationType(SteamIntEnum):
    EProfileCustomizationTypeInvalid = 0
    EProfileCustomizationTypeRareAchievementShowcase = 1
    EProfileCustomizationTypeGameCollector = 2
    EProfileCustomizationTypeItemShowcase = 3
    EProfileCustomizationTypeTradeShowcase = 4
    EProfileCustomizationTypeBadges = 5
    EProfileCustomizationTypeFavoriteGame = 6
    EProfileCustomizationTypeScreenshotShowcase = 7
    EProfileCustomizationTypeCustomText = 8
    EProfileCustomizationTypeFavoriteGroup = 9
    EProfileCustomizationTypeRecommendation = 10
    EProfileCustomizationTypeWorkshopItem = 11
    EProfileCustomizationTypeMyWorkshop = 12
    EProfileCustomizationTypeArtworkShowcase = 13
    EProfileCustomizationTypeVideoShowcase = 14
    EProfileCustomizationTypeGuides = 15
    EProfileCustomizationTypeMyGuides = 16
    EProfileCustomizationTypeAchievements = 17
    EProfileCustomizationTypeGreenlight = 18
    EProfileCustomizationTypeMyGreenlight = 19
    EProfileCustomizationTypeSalien = 20
    EProfileCustomizationTypeLoyaltyRewardReactions = 21
    EProfileCustomizationTypeSingleArtworkShowcase = 22
    EProfileCustomizationTypeAchievementsCompletionist = 23
    EProfileCustomizationTypeReplay = 24


class EProvideDeckFeedbackPreference(SteamIntEnum):
    Unset = 0
    Yes = 1
    No = 2


class EPublishedFileStorageSystem(SteamIntEnum):
    EPublishedFileStorageSystemInvalid = 0
    EPublishedFileStorageSystemLegacyCloud = 1
    EPublishedFileStorageSystemDepot = 2
    EPublishedFileStorageSystemUGCCloud = 3


EPurchaseRequestAction = SteamIntEnum(
    'EPurchaseRequestAction',
    {
        'None': 0,
        'Decline': 1,
        'Purchased': 2,
        'Abandoned': 3,
        'Cancel': 4,
        'MAX': 5,
    },
)


class ERecordingSessionChangeNotificationType(SteamIntEnum):
    Started = 1
    Stopped = 2
    Deleted = 3
    Updated = 4


class EScalingFilter(SteamIntEnum):
    Invalid = 0
    FSR = 1
    Nearest = 2
    Integer = 3
    Linear = 4
    NIS = 5


class ESDCardFormatStage(SteamIntEnum):
    Invalid = 0
    Starting = 1
    Testing = 2
    Rescuing = 3
    Formatting = 4
    Finalizing = 5


class ESessionPersistence(SteamIntEnum):
    Invalid = -1
    Ephemeral = 0
    Persistent = 1


ESettingProfileMode = SteamIntEnum(
    'ESettingProfileMode',
    {
        'None': 0,
        'PerGame': 1,
        'PerGamePerDisplay': 2,
        'PerDisplay': 3,
    },
)


class ESharedLibraryExcludeReason(SteamIntEnum):
    ESharedLibrary_Included = 0
    ESharedLibrary_AppExcluded_ByPartner = 1
    ESharedLibrary_LicenseExcluded = 2
    ESharedLibrary_FreeGame = 3
    ESharedLibrary_LicensePrivate = 4
    ESharedLibrary_AppExcluded_WrongAppType = 6
    ESharedLibrary_AppExcluded_NonrefundableDLC = 7
    ESharedLibrary_AppExcluded_UnreleasedApp = 8
    ESharedLibrary_AppExcluded_ParentAppExcluded = 9
    ESharedLibrary_PackageExcluded_ByPartner = 10
    ESharedLibrary_PackageExcluded_Special = 11
    ESharedLibrary_PackageExcluded_Dev = 12
    ESharedLibrary_PackageExcluded_FreeWeekend = 13
    ESharedLibrary_PackageExcluded_Invalid = 15
    ESharedLibrary_PackageExcluded_RecurringLicense = 16
    ESharedLibrary_PackageExcluded_WrongLicenseType = 17
    ESharedLibrary_PackageExcluded_MasterSub = 18
    ESharedLibrary_PackageExcluded_NoShareableApps = 19
    ESharedLibrary_LicenseExcluded_PaymentMasterSub = 20
    ESharedLibrary_LicenseExcluded_PaymentFamilyGroup = 21
    ESharedLibrary_LicenseExcluded_PaymentAuthorizedDevice = 22
    ESharedLibrary_LicenseExcluded_PaymentAutoGrant = 23
    ESharedLibrary_LicenseExcluded_FlagPending = 24
    ESharedLibrary_LicenseExcluded_FlagPendingRefund = 25
    ESharedLibrary_LicenseExcluded_FlagBorrowed = 26
    ESharedLibrary_LicenseExcluded_FlagAutoGrant = 27
    ESharedLibrary_LicenseExcluded_FlagTimedTrial = 28
    ESharedLibrary_LicenseExcluded_FreeSub = 29
    ESharedLibrary_LicenseExcluded_Inactive = 30


class ESLSHelper(SteamIntEnum):
    Invalid = 0
    Minidump = 1
    Kdump = 2
    Journal = 3
    Gpu = 4
    SystemInfo = 5


class ESplitScalingFilter(SteamIntEnum):
    Invalid = 0
    Linear = 1
    Nearest = 2
    FSR = 3
    NIS = 4


class ESplitScalingScaler(SteamIntEnum):
    Invalid = 0
    Auto = 1
    Integer = 2
    Fit = 3
    Fill = 4
    Stretch = 5


class EStartupMovieVariant(SteamIntEnum):
    Invalid = 0
    Default = 1
    Orange = 2


class ESteamDeckCompatibilityCategory(SteamIntEnum):
    Unknown = 0
    Unsupported = 1
    Playable = 2
    Verified = 3


class ESteamDeckCompatibilityFeedback(SteamIntEnum):
    Unset = 0
    Agree = 1
    Disagree = 2
    Ignore = 3


class ESteamDeckCompatibilityResultDisplayType(SteamIntEnum):
    Invisible = 0
    Informational = 1
    Unsupported = 2
    Playable = 3
    Verified = 4


class ESteamDeckCompatibilityTestResult(SteamIntEnum):
    Invalid = 0
    NotApplicable = 1
    Pass = 2
    Fail = 3
    FailMinor = 4


class ESteamDeckKeyboardLayout(SteamIntEnum):
    QWERTY = 0
    Bulgarian = 1
    Chinese_Simplified = 2
    Chinese_Traditional = 3
    Czech = 4
    Danish = 5
    Finnish = 6
    French = 7
    German = 8
    Greek = 9
    Hungarian = 10
    Italian = 11
    Japanese = 12
    Korean = 13
    Norwegian = 14
    Polish = 15
    Portuguese = 16
    Romanian = 17
    Russian = 18
    Spanish = 19
    Swedish = 20
    Thai = 21
    Turkish_F = 22
    Turkish_Q = 23
    Ukrainian = 24
    Vietnamese = 25
    QWERTY_International = 26
    Dvorak = 27
    Colemak = 28
    Bulgarian_Phonetic_Traditional = 29
    Bulgarian_Phonetic = 30
    Chinese_Traditional_Bopomofo = 31
    Chinese_Traditional_Cangjie = 32
    Japanese_Kana = 33
    Chinese_Traditional_Quick = 34
    Indonesian = 35


class ESteamPipeOperationType(SteamIntEnum):
    Invalid = 0
    DecryptCPU = 1
    DiskRead = 2
    DiskWrite = 3


class ESteamPipeWorkType(SteamIntEnum):
    ESteamPipeClientWorkType_Invalid = 0
    ESteamPipeClientWorkType_StageFromChunkStores = 1


class EStorageBlockContentType(SteamIntEnum):
    Invalid = 0
    Unknown = 1
    FileSystem = 2
    Crypto = 3
    Raid = 4


class EStorageBlockFileSystemType(SteamIntEnum):
    Invalid = 0
    Unknown = 1
    VFat = 2
    Ext4 = 3


class EStorageDriveMediaType(SteamIntEnum):
    Invalid = 0
    Unknown = 1
    HDD = 2
    SSD = 3
    Removable = 4


class EStorageFormatStage(SteamIntEnum):
    Invalid = 0
    NotRunning = 1
    Starting = 2
    Testing = 3
    Rescuing = 4
    Formatting = 5
    Finalizing = 6


class EStoreAppType(SteamIntEnum):
    Game = 0
    Demo = 1
    Mod = 2
    Movie = 3
    DLC = 4
    Guide = 5
    Software = 6
    Video = 7
    Series = 8
    Episode = 9
    Hardware = 10
    Music = 11
    Beta = 12
    Tool = 13
    Advertising = 14


EStoreBrowseFilterFailure = SteamIntEnum(
    'EStoreBrowseFilterFailure',
    {
        'None': 0,
        'Redundant': 10,
        'NotPreferred': 20,
        'NotInterested': 30,
        'UnwantedContent': 40,
        'Unavailable': 50,
    },
)


class EStoreCategoryType(SteamIntEnum):
    Category = 0
    SupportedPlayers = 1
    Feature = 2
    ControllerSupport = 3
    CloudGaming = 4
    MAX = 5


class EStoreDiscoveryQueueType(SteamIntEnum):
    EStoreDiscoveryQueueTypeNew = 0
    EStoreDiscoveryQueueTypeComingSoon = 1
    EStoreDiscoveryQueueTypeRecommended = 2
    EStoreDiscoveryQueueTypeEveryNewRelease = 3
    EStoreDiscoveryQueueTypeMLRecommender = 5
    EStoreDiscoveryQueueTypeWishlistOnSale = 6
    EStoreDiscoveryQueueTypeDLC = 7
    EStoreDiscoveryQueueTypeDLCOnSale = 8
    EStoreDiscoveryQueueTypeRecommendedComingSoon = 9
    EStoreDiscoveryQueueTypeRecommendedFree = 10
    EStoreDiscoveryQueueTypeRecommendedOnSale = 11
    EStoreDiscoveryQueueTypeRecommendedDemos = 12
    EStoreDiscoveryQueueTypeDLCNewReleases = 13
    EStoreDiscoveryQueueTypeDLCTopSellers = 14
    EStoreDiscoveryQueueTypeMAX = 15


class EStoreItemType(SteamIntEnum):
    Invalid = -1
    App = 0
    Package = 1
    Bundle = 2
    Mtx = 3
    Tag = 4
    Creator = 5
    HubCategory = 6


EStoreLinkType = SteamIntEnum(
    'EStoreLinkType',
    {
        'None': 0,
        'YouTube': 1,
        'Facebook': 2,
        'Twitter': 3,
        'Twitch': 4,
        'Discord': 5,
        'QQ': 6,
        'VK': 7,
        'Bilibili': 8,
        'Weibo': 9,
        'Reddit': 10,
        'Instagram': 11,
        'Tumblr': 12,
        'Tieba': 13,
        'Tiktok': 14,
        'Telegram': 15,
        'LinkedIn': 16,
        'WeChat': 17,
        'QQLink': 18,
        'MAX': 19,
    },
)


class ESystemAudioChannel(SteamIntEnum):
    SystemAudioChannel_Invalid = 0
    SystemAudioChannel_Aggregated = 1
    SystemAudioChannel_FrontLeft = 2
    SystemAudioChannel_FrontRight = 3
    SystemAudioChannel_LFE = 4
    SystemAudioChannel_BackLeft = 5
    SystemAudioChannel_BackRight = 6
    SystemAudioChannel_FrontCenter = 7
    SystemAudioChannel_Unknown = 8
    SystemAudioChannel_Mono = 9


class ESystemAudioDirection(SteamIntEnum):
    SystemAudioDirection_Invalid = 0
    SystemAudioDirection_Input = 1
    SystemAudioDirection_Output = 2


class ESystemAudioPortDirection(SteamIntEnum):
    SystemAudioPortDirection_Invalid = 0
    SystemAudioPortDirection_Input = 1
    SystemAudioPortDirection_Output = 2


class ESystemAudioPortType(SteamIntEnum):
    SystemAudioPortType_Invalid = 0
    SystemAudioPortType_Unknown = 1
    SystemAudioPortType_Audio32f = 2
    SystemAudioPortType_Midi8b = 3
    SystemAudioPortType_Video32RGBA = 4


ESystemDisplayCompatibilityMode = SteamIntEnum(
    'ESystemDisplayCompatibilityMode',
    {
        'Invalid': 0,
        'None': 1,
        'MinimalBandwith': 2,
    },
)


class ESystemFanControlMode(SteamIntEnum):
    SystemFanControlMode_Invalid = 0
    SystemFanControlMode_Disabled = 1
    SystemFanControlMode_Default = 2


class ESystemServiceState(SteamIntEnum):
    Unavailable = 0
    Disabled = 1
    Enabled = 2


class ETextFilterSetting(SteamIntEnum):
    ETextFilterSettingSteamLabOptedOut = 0
    ETextFilterSettingEnabled = 1
    ETextFilterSettingEnabledAllowProfanity = 2
    ETextFilterSettingDisabled = 3


class EThumbnailFormat(SteamIntEnum):
    eJPEG = 1
    eRGB = 2


class EThumbnailTimePrecision(SteamIntEnum):
    ePrecise = 0
    eLoose = 1


class ETimelineChangeNotificationType(SteamIntEnum):
    Started = 1
    Stopped = 2
    Deleted = 3
    RecordingStarted = 4
    RecordingStopped = 5
    RecordingUpdated = 6


class ETimelineEntryType(SteamIntEnum):
    Invalid = 0
    GameMode = 1
    Event = 2
    StateDescription = 3
    Achievement = 4
    UserMarker = 5
    Screenshot = 6
    Error = 7
    Tag = 8
    GamePhase = 9


ETokenRenewalType = SteamIntEnum(
    'ETokenRenewalType',
    {
        'None': 0,
        'Allow': 1,
    },
)


class ETouchGesture(SteamIntEnum):
    ETouchGestureNone = 0
    ETouchGestureTouch = 1
    ETouchGestureTap = 2
    ETouchGestureDoubleTap = 3
    ETouchGestureShortPress = 4
    ETouchGestureLongPress = 5
    ETouchGestureLongTap = 6
    ETouchGestureTwoFingerTap = 7
    ETouchGestureTapCancelled = 8
    ETouchGesturePinchBegin = 9
    ETouchGesturePinchUpdate = 10
    ETouchGesturePinchEnd = 11
    ETouchGestureFlingStart = 12
    ETouchGestureFlingCancelled = 13


class EUpdaterState(SteamIntEnum):
    Invalid = 0
    UpToDate = 2
    Checking = 3
    Available = 4
    Applying = 5
    ClientRestartPending = 6
    SystemRestartPending = 7
    RollBack = 8


class EUpdaterType(SteamIntEnum):
    Invalid = 0
    Client = 1
    OS = 2
    BIOS = 3
    Aggregated = 4
    Test1 = 5
    Test2 = 6
    Dummy = 7


EUserReviewScore = SteamIntEnum(
    'EUserReviewScore',
    {
        'None': 0,
        'OverwhelminglyNegative': 1,
        'VeryNegative': 2,
        'Negative': 3,
        'MostlyNegative': 4,
        'Mixed': 5,
        'MostlyPositive': 6,
        'Positive': 7,
        'VeryPositive': 8,
        'OverwhelminglyPositive': 9,
    },
)


class EUserReviewScorePreference(SteamIntEnum):
    Unset = 0
    IncludeAll = 1
    ExcludeBombs = 2


class EWindowStackingOrder(SteamIntEnum):
    Invalid = 0
    Top = 1
    Bottom = 2


class EWindowsUpdateInstallationImpact(SteamIntEnum):
    Unknown = -1
    Normal = 0
    Minor = 1
    ExclusiveHandling = 2


class EWindowsUpdateRebootBehavior(SteamIntEnum):
    Unknown = -1
    NeverNeedsReboot = 0
    AlwaysNeedsReboot = 1
    MightNeedReboot = 2


__all__ = [
    'EACState',
    'EAgreementType',
    'EAppCloudStatus',
    'EAppControllerSupportLevel',
    'EAppGamepadGyroTrackpadSupportLevel',
    'EAppHDRSupport',
    'EAppReportType',
    'EAsyncGameSessionUserState',
    'EAsyncGameSessionUserVisibility',
    'EAuthenticationType',
    'EAuthSessionGuardType',
    'EAuthSessionSecurityHistory',
    'EAuthTokenPlatformType',
    'EAuthTokenRevokeAction',
    'EAuthTokenState',
    'EBatteryState',
    'EBluetoothDeviceType',
    'EBroadcastEncoderSetting',
    'EBroadcastPermission',
    'EBrowserFeatureStatus',
    'EBrowserGPUStatus',
    'EClientExecutionSite',
    'EClientSettingStore',
    'EClipRangeMethod',
    'EClipShareMethod',
    'ECloudGamingPlatform',
    'ECloudPendingRemoteOperation',
    'ECloudStoragePersistState',
    'EColorGamutLabelSet',
    'ECommentThreadType',
    'ECommunityItemClass',
    'ECompromiseDetectionType',
    'EContentCheckProvider',
    'ECPUGovernor',
    'EDiskSpaceType',
    'EDisplayStatus',
    'EExportCodec',
    'EExternalSaleEventType',
    'EFamilyGroupChangeLogType',
    'EFamilyGroupRole',
    'EFamilyGroupsTwoFactorMethod',
    'EForumType',
    'EGameRecordingType',
    'EGamescopeBlurMode',
    'EGpuDriverId',
    'EGPUPerformanceLevel',
    'EGraphicsPerfOverlayLevel',
    'EGRAudio',
    'EGRExportLimitType',
    'EGRMode',
    'EHDRToneMapOperator',
    'EHDRVisualization',
    'EJSRegisterMethodType',
    'ENewSteamAnnouncementState',
    'ENotificationSetting',
    'EOSBranch',
    'EOverlayToggleBarLocation',
    'EPartnerEventDisplayLocation',
    'EPartnerLinkTrackingBackfillSource',
    'EPhaseResultType',
    'EPlaytestStatus',
    'EProfileCustomizationStyle',
    'EProfileCustomizationType',
    'EProvideDeckFeedbackPreference',
    'EPublishedFileStorageSystem',
    'EPurchaseRequestAction',
    'ERecordingSessionChangeNotificationType',
    'EScalingFilter',
    'ESDCardFormatStage',
    'ESessionPersistence',
    'ESettingProfileMode',
    'ESharedLibraryExcludeReason',
    'ESLSHelper',
    'ESplitScalingFilter',
    'ESplitScalingScaler',
    'EStartupMovieVariant',
    'ESteamDeckCompatibilityCategory',
    'ESteamDeckCompatibilityFeedback',
    'ESteamDeckCompatibilityResultDisplayType',
    'ESteamDeckCompatibilityTestResult',
    'ESteamDeckKeyboardLayout',
    'ESteamPipeOperationType',
    'ESteamPipeWorkType',
    'EStorageBlockContentType',
    'EStorageBlockFileSystemType',
    'EStorageDriveMediaType',
    'EStorageFormatStage',
    'EStoreAppType',
    'EStoreBrowseFilterFailure',
    'EStoreCategoryType',
    'EStoreDiscoveryQueueType',
    'EStoreItemType',
    'EStoreLinkType',
    'ESystemAudioChannel',
    'ESystemAudioDirection',
    'ESystemAudioPortDirection',
    'ESystemAudioPortType',
    'ESystemDisplayCompatibilityMode',
    'ESystemFanControlMode',
    'ESystemServiceState',
    'ETextFilterSetting',
    'EThumbnailFormat',
    'EThumbnailTimePrecision',
    'ETimelineChangeNotificationType',
    'ETimelineEntryType',
    'ETokenRenewalType',
    'ETouchGesture',
    'EUpdaterState',
    'EUpdaterType',
    'EUserReviewScore',
    'EUserReviewScorePreference',
    'EWindowStackingOrder',
    'EWindowsUpdateInstallationImpact',
    'EWindowsUpdateRebootBehavior',
]
