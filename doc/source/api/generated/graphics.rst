Module contents
---------------

Overview
########

Interfaces
~~~~~~~~~~

.. autosummary::

    IPathPoint
    IPathPointFactory
    IBoundingSphere
    IBoundingSphereFactory
    ITextureFilter2D
    ITextureFilter2DFactory
    IRendererTexture2D
    IRendererTextureTemplate2D
    IPathPointCollection
    IObjectCollection
    ISceneCollection
    IScreenOverlayContainer
    IScreenOverlayPickResultCollection
    IGlobeImageOverlayAddCompleteEventArgs
    ITerrainOverlayAddCompleteEventArgs
    IPickResultCollection
    IRenderingEventArgs
    IBatchPrimitiveIndex
    IKmlDocumentCollection
    IKmlFeatureCollection
    IKmlDocumentLoadedEventArgs
    IFactoryAndInitializers
    IExtrudedPolylineTriangulatorResult
    ISolidTriangulatorResult
    ISurfaceShapesResult
    ISurfaceTriangulatorResult
    ITriangulatorResult
    IAGICustomTerrainOverlay
    IAGIProcessedImageGlobeOverlay
    IAGIProcessedTerrainOverlay
    IAGIRoamImageGlobeOverlay
    ICameraSnapshot
    ICameraVideoRecording
    ICentralBodyGraphicsIndexer
    ICustomImageGlobeOverlay
    ICustomImageGlobeOverlayPluginActivator
    ICustomImageGlobeOverlayPluginProxy
    IGeospatialImageGlobeOverlay
    IGlobeOverlay
    IGlobeOverlaySettings
    ILighting
    IPathPrimitiveUpdatePolicy
    IProjectedRasterOverlay
    IProjection
    IProjectionStream
    ISceneGlobeOverlaySettings
    IScreenOverlayCollectionBase
    ITexture2DFactory
    IVisualEffects
    IAltitudeDisplayCondition
    IAxesPrimitive
    ICamera
    ICentralBodyGraphics
    IClouds
    ICompositeDisplayCondition
    ICompositePrimitive
    IConstantDisplayCondition
    IDisplayCondition
    IDistanceDisplayCondition
    IDistanceToGlobeOverlayDisplayCondition
    IDistanceToPositionDisplayCondition
    IDistanceToPrimitiveDisplayCondition
    IDurationPathPrimitiveUpdatePolicy
    IFrameRate
    IGlobeImageOverlay
    IGraphicsFont
    IGreatArcInterpolator
    IImageCollection
    IAlphaFromLuminanceFilter
    IAlphaFromPixelFilter
    IAlphaFromRasterFilter
    IBandExtractFilter
    IBandOrderFilter
    IBlurFilter
    IBrightnessFilter
    IColorToLuminanceFilter
    IContrastFilter
    IConvolutionFilter
    IEdgeDetectFilter
    IFilteringRasterStream
    IFlipFilter
    IGammaCorrectionFilter
    IGaussianBlurFilter
    IGradientDetectFilter
    ILevelsFilter
    IProjectionRasterStreamPluginActivator
    IProjectionRasterStreamPluginProxy
    IRaster
    IRasterAttributes
    IRasterFilter
    IRasterStream
    IRotateFilter
    ISequenceFilter
    ISharpenFilter
    IVideoStream
    IKmlContainer
    IKmlDocument
    IKmlFeature
    IKmlFolder
    IKmlGraphics
    IKmlNetworkLink
    IMarkerBatchPrimitive
    IMarkerBatchPrimitiveOptionalParameters
    IMaximumCountPathPrimitiveUpdatePolicy
    IModelArticulation
    IModelArticulationCollection
    IModelPrimitive
    IModelTransformation
    IOverlay
    IPathPrimitive
    IPickResult
    IPixelSizeDisplayCondition
    IPointBatchPrimitive
    IPointBatchPrimitiveOptionalParameters
    IPolylinePrimitive
    IPolylinePrimitiveOptionalParameters
    IPositionInterpolator
    IPrimitive
    IPrimitiveManager
    IRasterImageGlobeOverlay
    IRhumbLineInterpolator
    IScene
    ISceneDisplayCondition
    ISceneManager
    IScreenOverlay
    IScreenOverlayCollection
    IScreenOverlayManager
    IScreenOverlayPickResult
    ISolidPrimitive
    IStereoscopic
    ISurfaceMeshPrimitive
    ITerrainOverlayCollection
    ITerrainOverlay
    ITextBatchPrimitive
    ITextBatchPrimitiveOptionalParameters
    ITextOverlay
    ITextureMatrix
    ITextureScreenOverlay
    ITimeIntervalDisplayCondition
    ITriangleMeshPrimitive
    ITriangleMeshPrimitiveOptionalParameters
    IVectorPrimitive
    IBoxTriangulatorInitializer
    ICylinderTriangulatorInitializer
    IEllipsoidTriangulatorInitializer
    IExtrudedPolylineTriangulatorInitializer
    ISurfaceExtentTriangulatorInitializer
    ISurfacePolygonTriangulatorInitializer
    ISurfaceShapesInitializer
    IAGICustomTerrainOverlayFactory
    IAGIProcessedImageGlobeOverlayFactory
    IAGIProcessedTerrainOverlayFactory
    IAGIRoamImageGlobeOverlayFactory
    ICustomImageGlobeOverlayPluginActivatorFactory
    IGeospatialImageGlobeOverlayFactory
    IProjectedRasterOverlayFactory
    IProjectionFactory
    IAltitudeDisplayConditionFactory
    IAxesPrimitiveFactory
    ICompositeDisplayConditionFactory
    ICompositePrimitiveFactory
    IConstantDisplayConditionFactory
    IDistanceDisplayConditionFactory
    IDistanceToGlobeOverlayDisplayConditionFactory
    IDistanceToPositionDisplayConditionFactory
    IDistanceToPrimitiveDisplayConditionFactory
    IDurationPathPrimitiveUpdatePolicyFactory
    IGlobeImageOverlayInitializer
    IGraphicsFontFactory
    IGreatArcInterpolatorFactory
    IAlphaFromLuminanceFilterFactory
    IAlphaFromPixelFilterFactory
    IAlphaFromRasterFilterFactory
    IBandExtractFilterFactory
    IBandOrderFilterFactory
    IBlurFilterFactory
    IBrightnessFilterFactory
    IColorToLuminanceFilterFactory
    IContrastFilterFactory
    IConvolutionFilterFactory
    IEdgeDetectFilterFactory
    IFilteringRasterStreamFactory
    IFlipFilterFactory
    IGammaCorrectionFilterFactory
    IGaussianBlurFilterFactory
    IGradientDetectFilterFactory
    IJpeg2000WriterInitializer
    ILevelsFilterFactory
    IProjectionRasterStreamPluginActivatorFactory
    IRasterFactory
    IRasterAttributesFactory
    IRotateFilterFactory
    ISequenceFilterFactory
    ISharpenFilterFactory
    IVideoStreamFactory
    IMarkerBatchPrimitiveFactory
    IMarkerBatchPrimitiveOptionalParametersFactory
    IMaximumCountPathPrimitiveUpdatePolicyFactory
    IModelPrimitiveFactory
    IPathPrimitiveFactory
    IPixelSizeDisplayConditionFactory
    IPointBatchPrimitiveFactory
    IPointBatchPrimitiveOptionalParametersFactory
    IPolylinePrimitiveFactory
    IPolylinePrimitiveOptionalParametersFactory
    IRasterImageGlobeOverlayFactory
    IRhumbLineInterpolatorFactory
    ISceneDisplayConditionFactory
    ISceneManagerInitializer
    IScreenOverlayFactory
    ISolidPrimitiveFactory
    ISurfaceMeshPrimitiveFactory
    ITerrainOverlayInitializer
    ITextBatchPrimitiveFactory
    ITextBatchPrimitiveOptionalParametersFactory
    ITextOverlayFactory
    ITextureMatrixFactory
    ITextureScreenOverlayFactory
    ITimeIntervalDisplayConditionFactory
    ITriangleMeshPrimitiveFactory
    ITriangleMeshPrimitiveOptionalParametersFactory
    IVectorPrimitiveFactory


Enumerations
~~~~~~~~~~~~

.. autosummary::

    CYLINDER_FILL
    WINDING_ORDER
    CAMERA_SNAPSHOT_FILE_FORMAT
    CAMERA_VIDEO_FORMAT
    CONSTRAINED_UP_AXIS
    GLOBE_OVERLAY_ROLE
    INDICES_ORDER_HINT
    MAINTAIN_ASPECT_RATIO
    MAP_PROJECTION
    MARKER_BATCH_RENDERING_METHOD
    MARKER_BATCH_RENDER_PASS
    MARKER_BATCH_SIZE_SOURCE
    MARKER_BATCH_SORT_ORDER
    MARKER_BATCH_UNIT
    MODEL_TRANSFORMATION_TYPE
    ORIGIN
    PATH_PRIMITIVE_REMOVE_LOCATION
    PRIMITIVES_SORT_ORDER
    REFRESH_RATE
    RENDER_PASS
    RENDER_PASS_HINT
    SCREEN_OVERLAY_ORIGIN
    SCREEN_OVERLAY_PINNING_ORIGIN
    SCREEN_OVERLAY_UNIT
    SURFACE_MESH_RENDERING_METHOD
    VISIBILITY
    ANTI_ALIASING
    BINARY_LOGIC_OPERATION
    BLUR_METHOD
    EDGE_DETECT_METHOD
    FLIP_AXIS
    GRADIENT_DETECT_METHOD
    JPEG2000_COMPRESSION_PROFILE
    RASTER_BAND
    RASTER_FORMAT
    RASTER_ORIENTATION
    RASTER_TYPE
    SHARPEN_METHOD
    VIDEO_PLAYBACK
    KML_NETWORK_LINK_REFRESH_MODE
    KML_NETWORK_LINK_VIEW_REFRESH_MODE
    MODEL_UP_AXIS
    OUTLINE_APPEARANCE
    POLYLINE_TYPE
    CULL_FACE
    INTERNAL_TEXTURE_FORMAT
    MAGNIFICATION_FILTER
    MINIFICATION_FILTER
    RENDERER_SHADE_MODEL
    TEXTURE_WRAP
    SET_HINT
    STEREO_PROJECTION_MODE
    STEREOSCOPIC_DISPLAY_MODE
    FONT_STYLE


Classes
~~~~~~~

.. autosummary::

    PathPoint
    PathPointFactory
    BoundingSphere
    BoundingSphereFactory
    TextureFilter2D
    TextureFilter2DFactory
    RendererTexture2D
    RendererTextureTemplate2D
    PathPointCollection
    ObjectCollection
    SceneCollection
    ScreenOverlayPickResultCollection
    GlobeImageOverlayAddCompleteEventArgs
    TerrainOverlayAddCompleteEventArgs
    PickResultCollection
    RenderingEventArgs
    BatchPrimitiveIndex
    KmlDocumentCollection
    KmlFeatureCollection
    KmlDocumentLoadedEventArgs
    FactoryAndInitializers
    ExtrudedPolylineTriangulatorResult
    SolidTriangulatorResult
    SurfaceShapesResult
    SurfaceTriangulatorResult
    TriangulatorResult
    AGICustomTerrainOverlay
    AGIProcessedImageGlobeOverlay
    AGIProcessedTerrainOverlay
    AGIRoamImageGlobeOverlay
    CameraSnapshot
    CameraVideoRecording
    CentralBodyGraphicsIndexer
    CustomImageGlobeOverlay
    CustomImageGlobeOverlayPluginActivator
    CustomImageGlobeOverlayPluginProxy
    GeospatialImageGlobeOverlay
    GlobeOverlay
    GlobeOverlaySettings
    Lighting
    PathPrimitiveUpdatePolicy
    ProjectedRasterOverlay
    Projection
    ProjectionStream
    SceneGlobeOverlaySettings
    ScreenOverlayCollectionBase
    Texture2DFactory
    VisualEffects
    AltitudeDisplayCondition
    AxesPrimitive
    Camera
    CentralBodyGraphics
    Clouds
    CompositeDisplayCondition
    CompositePrimitive
    ConstantDisplayCondition
    DisplayCondition
    DistanceDisplayCondition
    DistanceToGlobeOverlayDisplayCondition
    DistanceToPositionDisplayCondition
    DistanceToPrimitiveDisplayCondition
    DurationPathPrimitiveUpdatePolicy
    FrameRate
    GlobeImageOverlay
    GraphicsFont
    GreatArcInterpolator
    ImageCollection
    AlphaFromLuminanceFilter
    AlphaFromPixelFilter
    AlphaFromRasterFilter
    BandExtractFilter
    BandOrderFilter
    BlurFilter
    BrightnessFilter
    ColorToLuminanceFilter
    ContrastFilter
    ConvolutionFilter
    EdgeDetectFilter
    FilteringRasterStream
    FlipFilter
    GammaCorrectionFilter
    GaussianBlurFilter
    GradientDetectFilter
    LevelsFilter
    ProjectionRasterStreamPluginActivator
    ProjectionRasterStreamPluginProxy
    Raster
    RasterAttributes
    RasterFilter
    RasterStream
    RotateFilter
    SequenceFilter
    SharpenFilter
    VideoStream
    KmlContainer
    KmlDocument
    KmlFeature
    KmlFolder
    KmlGraphics
    KmlNetworkLink
    MarkerBatchPrimitive
    MarkerBatchPrimitiveOptionalParameters
    MaximumCountPathPrimitiveUpdatePolicy
    ModelArticulation
    ModelArticulationCollection
    ModelPrimitive
    ModelTransformation
    Overlay
    PathPrimitive
    PickResult
    PixelSizeDisplayCondition
    PointBatchPrimitive
    PointBatchPrimitiveOptionalParameters
    PolylinePrimitive
    PolylinePrimitiveOptionalParameters
    PositionInterpolator
    Primitive
    PrimitiveManager
    RasterImageGlobeOverlay
    RhumbLineInterpolator
    Scene
    SceneDisplayCondition
    SceneManager
    ScreenOverlay
    ScreenOverlayCollection
    ScreenOverlayManager
    ScreenOverlayPickResult
    SolidPrimitive
    Stereoscopic
    SurfaceMeshPrimitive
    TerrainOverlayCollection
    TerrainOverlay
    TextBatchPrimitive
    TextBatchPrimitiveOptionalParameters
    TextOverlay
    TextureMatrix
    TextureScreenOverlay
    TimeIntervalDisplayCondition
    TriangleMeshPrimitive
    TriangleMeshPrimitiveOptionalParameters
    VectorPrimitive
    BoxTriangulatorInitializer
    CylinderTriangulatorInitializer
    EllipsoidTriangulatorInitializer
    ExtrudedPolylineTriangulatorInitializer
    SurfaceExtentTriangulatorInitializer
    SurfacePolygonTriangulatorInitializer
    SurfaceShapesInitializer
    AGICustomTerrainOverlayFactory
    AGIProcessedImageGlobeOverlayFactory
    AGIProcessedTerrainOverlayFactory
    AGIRoamImageGlobeOverlayFactory
    CustomImageGlobeOverlayPluginActivatorFactory
    GeospatialImageGlobeOverlayFactory
    ProjectedRasterOverlayFactory
    ProjectionFactory
    AltitudeDisplayConditionFactory
    AxesPrimitiveFactory
    CompositeDisplayConditionFactory
    CompositePrimitiveFactory
    ConstantDisplayConditionFactory
    DistanceDisplayConditionFactory
    DistanceToGlobeOverlayDisplayConditionFactory
    DistanceToPositionDisplayConditionFactory
    DistanceToPrimitiveDisplayConditionFactory
    DurationPathPrimitiveUpdatePolicyFactory
    GlobeImageOverlayInitializer
    GraphicsFontFactory
    GreatArcInterpolatorFactory
    AlphaFromLuminanceFilterFactory
    AlphaFromPixelFilterFactory
    AlphaFromRasterFilterFactory
    BandExtractFilterFactory
    BandOrderFilterFactory
    BlurFilterFactory
    BrightnessFilterFactory
    ColorToLuminanceFilterFactory
    ContrastFilterFactory
    ConvolutionFilterFactory
    EdgeDetectFilterFactory
    FilteringRasterStreamFactory
    FlipFilterFactory
    GammaCorrectionFilterFactory
    GaussianBlurFilterFactory
    GradientDetectFilterFactory
    Jpeg2000WriterInitializer
    LevelsFilterFactory
    ProjectionRasterStreamPluginActivatorFactory
    RasterFactory
    RasterAttributesFactory
    RotateFilterFactory
    SequenceFilterFactory
    SharpenFilterFactory
    VideoStreamFactory
    MarkerBatchPrimitiveFactory
    MarkerBatchPrimitiveOptionalParametersFactory
    MaximumCountPathPrimitiveUpdatePolicyFactory
    ModelPrimitiveFactory
    PathPrimitiveFactory
    PixelSizeDisplayConditionFactory
    PointBatchPrimitiveFactory
    PointBatchPrimitiveOptionalParametersFactory
    PolylinePrimitiveFactory
    PolylinePrimitiveOptionalParametersFactory
    RasterImageGlobeOverlayFactory
    RhumbLineInterpolatorFactory
    SceneDisplayConditionFactory
    SceneManagerInitializer
    ScreenOverlayFactory
    SolidPrimitiveFactory
    SurfaceMeshPrimitiveFactory
    TerrainOverlayInitializer
    TextBatchPrimitiveFactory
    TextBatchPrimitiveOptionalParametersFactory
    TextOverlayFactory
    TextureMatrixFactory
    TextureScreenOverlayFactory
    TimeIntervalDisplayConditionFactory
    TriangleMeshPrimitiveFactory
    TriangleMeshPrimitiveOptionalParametersFactory
    VectorPrimitiveFactory


Reference
#########

Interfaces
~~~~~~~~~~

.. autoclass:: IPathPoint
    :members:
    :exclude-members: __init__
.. autoclass:: IPathPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IBoundingSphere
    :members:
    :exclude-members: __init__
.. autoclass:: IBoundingSphereFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITextureFilter2D
    :members:
    :exclude-members: __init__
.. autoclass:: ITextureFilter2DFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRendererTexture2D
    :members:
    :exclude-members: __init__
.. autoclass:: IRendererTextureTemplate2D
    :members:
    :exclude-members: __init__
.. autoclass:: IPathPointCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ISceneCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayContainer
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayPickResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IGlobeImageOverlayAddCompleteEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: ITerrainOverlayAddCompleteEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: IPickResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IRenderingEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: IBatchPrimitiveIndex
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlDocumentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlFeatureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlDocumentLoadedEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: IFactoryAndInitializers
    :members:
    :exclude-members: __init__
.. autoclass:: IExtrudedPolylineTriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISolidTriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfaceShapesResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfaceTriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: ITriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: IAGICustomTerrainOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IAGIProcessedImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IAGIProcessedTerrainOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IAGIRoamImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: ICameraSnapshot
    :members:
    :exclude-members: __init__
.. autoclass:: ICameraVideoRecording
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyGraphicsIndexer
    :members:
    :exclude-members: __init__
.. autoclass:: ICustomImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: ICustomImageGlobeOverlayPluginActivator
    :members:
    :exclude-members: __init__
.. autoclass:: ICustomImageGlobeOverlayPluginProxy
    :members:
    :exclude-members: __init__
.. autoclass:: IGeospatialImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IGlobeOverlaySettings
    :members:
    :exclude-members: __init__
.. autoclass:: ILighting
    :members:
    :exclude-members: __init__
.. autoclass:: IPathPrimitiveUpdatePolicy
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectedRasterOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IProjection
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectionStream
    :members:
    :exclude-members: __init__
.. autoclass:: ISceneGlobeOverlaySettings
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayCollectionBase
    :members:
    :exclude-members: __init__
.. autoclass:: ITexture2DFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IVisualEffects
    :members:
    :exclude-members: __init__
.. autoclass:: IAltitudeDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: ICamera
    :members:
    :exclude-members: __init__
.. autoclass:: ICentralBodyGraphics
    :members:
    :exclude-members: __init__
.. autoclass:: IClouds
    :members:
    :exclude-members: __init__
.. autoclass:: ICompositeDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ICompositePrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IConstantDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceToGlobeOverlayDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceToPositionDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceToPrimitiveDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IDurationPathPrimitiveUpdatePolicy
    :members:
    :exclude-members: __init__
.. autoclass:: IFrameRate
    :members:
    :exclude-members: __init__
.. autoclass:: IGlobeImageOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IGraphicsFont
    :members:
    :exclude-members: __init__
.. autoclass:: IGreatArcInterpolator
    :members:
    :exclude-members: __init__
.. autoclass:: IImageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IAlphaFromLuminanceFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAlphaFromPixelFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IAlphaFromRasterFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IBandExtractFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IBandOrderFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IBlurFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IBrightnessFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IColorToLuminanceFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IContrastFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IConvolutionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IEdgeDetectFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IFilteringRasterStream
    :members:
    :exclude-members: __init__
.. autoclass:: IFlipFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IGammaCorrectionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IGaussianBlurFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IGradientDetectFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ILevelsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectionRasterStreamPluginActivator
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectionRasterStreamPluginProxy
    :members:
    :exclude-members: __init__
.. autoclass:: IRaster
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterAttributes
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterStream
    :members:
    :exclude-members: __init__
.. autoclass:: IRotateFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ISequenceFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ISharpenFilter
    :members:
    :exclude-members: __init__
.. autoclass:: IVideoStream
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlContainer
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlDocument
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlFeature
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlFolder
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlGraphics
    :members:
    :exclude-members: __init__
.. autoclass:: IKmlNetworkLink
    :members:
    :exclude-members: __init__
.. autoclass:: IMarkerBatchPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IMarkerBatchPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: IMaximumCountPathPrimitiveUpdatePolicy
    :members:
    :exclude-members: __init__
.. autoclass:: IModelArticulation
    :members:
    :exclude-members: __init__
.. autoclass:: IModelArticulationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IModelPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IModelTransformation
    :members:
    :exclude-members: __init__
.. autoclass:: IOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IPathPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IPickResult
    :members:
    :exclude-members: __init__
.. autoclass:: IPixelSizeDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: IPointBatchPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IPointBatchPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: IPolylinePrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IPolylinePrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: IPositionInterpolator
    :members:
    :exclude-members: __init__
.. autoclass:: IPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IPrimitiveManager
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IRhumbLineInterpolator
    :members:
    :exclude-members: __init__
.. autoclass:: IScene
    :members:
    :exclude-members: __init__
.. autoclass:: ISceneDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ISceneManager
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayCollection
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayManager
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayPickResult
    :members:
    :exclude-members: __init__
.. autoclass:: ISolidPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IStereoscopic
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfaceMeshPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: ITerrainOverlayCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ITerrainOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: ITextBatchPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: ITextBatchPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: ITextOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: ITextureMatrix
    :members:
    :exclude-members: __init__
.. autoclass:: ITextureScreenOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: ITimeIntervalDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: ITriangleMeshPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: ITriangleMeshPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: IBoxTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ICylinderTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: IEllipsoidTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: IExtrudedPolylineTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfaceExtentTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfacePolygonTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfaceShapesInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: IAGICustomTerrainOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAGIProcessedImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAGIProcessedTerrainOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAGIRoamImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICustomImageGlobeOverlayPluginActivatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGeospatialImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectedRasterOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAltitudeDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAxesPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICompositeDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ICompositePrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IConstantDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceToGlobeOverlayDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceToPositionDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IDistanceToPrimitiveDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IDurationPathPrimitiveUpdatePolicyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGlobeImageOverlayInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: IGraphicsFontFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGreatArcInterpolatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAlphaFromLuminanceFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAlphaFromPixelFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IAlphaFromRasterFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IBandExtractFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IBandOrderFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IBlurFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IBrightnessFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IColorToLuminanceFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IContrastFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IConvolutionFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IEdgeDetectFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IFilteringRasterStreamFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IFlipFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGammaCorrectionFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGaussianBlurFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IGradientDetectFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IJpeg2000WriterInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ILevelsFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IProjectionRasterStreamPluginActivatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterAttributesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRotateFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISequenceFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISharpenFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IVideoStreamFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IMarkerBatchPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IMarkerBatchPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IMaximumCountPathPrimitiveUpdatePolicyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IModelPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPathPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPixelSizeDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPointBatchPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPointBatchPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPolylinePrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IPolylinePrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRasterImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IRhumbLineInterpolatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISceneDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISceneManagerInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: IScreenOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISolidPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ISurfaceMeshPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITerrainOverlayInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ITextBatchPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITextBatchPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITextOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITextureMatrixFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITextureScreenOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITimeIntervalDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITriangleMeshPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ITriangleMeshPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: IVectorPrimitiveFactory
    :members:
    :exclude-members: __init__


Enumerations
~~~~~~~~~~~~

.. autoenum:: CYLINDER_FILL
    :members:
.. autoenum:: WINDING_ORDER
    :members:
.. autoenum:: CAMERA_SNAPSHOT_FILE_FORMAT
    :members:
.. autoenum:: CAMERA_VIDEO_FORMAT
    :members:
.. autoenum:: CONSTRAINED_UP_AXIS
    :members:
.. autoenum:: GLOBE_OVERLAY_ROLE
    :members:
.. autoenum:: INDICES_ORDER_HINT
    :members:
.. autoenum:: MAINTAIN_ASPECT_RATIO
    :members:
.. autoenum:: MAP_PROJECTION
    :members:
.. autoenum:: MARKER_BATCH_RENDERING_METHOD
    :members:
.. autoenum:: MARKER_BATCH_RENDER_PASS
    :members:
.. autoenum:: MARKER_BATCH_SIZE_SOURCE
    :members:
.. autoenum:: MARKER_BATCH_SORT_ORDER
    :members:
.. autoenum:: MARKER_BATCH_UNIT
    :members:
.. autoenum:: MODEL_TRANSFORMATION_TYPE
    :members:
.. autoenum:: ORIGIN
    :members:
.. autoenum:: PATH_PRIMITIVE_REMOVE_LOCATION
    :members:
.. autoenum:: PRIMITIVES_SORT_ORDER
    :members:
.. autoenum:: REFRESH_RATE
    :members:
.. autoenum:: RENDER_PASS
    :members:
.. autoenum:: RENDER_PASS_HINT
    :members:
.. autoenum:: SCREEN_OVERLAY_ORIGIN
    :members:
.. autoenum:: SCREEN_OVERLAY_PINNING_ORIGIN
    :members:
.. autoenum:: SCREEN_OVERLAY_UNIT
    :members:
.. autoenum:: SURFACE_MESH_RENDERING_METHOD
    :members:
.. autoenum:: VISIBILITY
    :members:
.. autoenum:: ANTI_ALIASING
    :members:
.. autoenum:: BINARY_LOGIC_OPERATION
    :members:
.. autoenum:: BLUR_METHOD
    :members:
.. autoenum:: EDGE_DETECT_METHOD
    :members:
.. autoenum:: FLIP_AXIS
    :members:
.. autoenum:: GRADIENT_DETECT_METHOD
    :members:
.. autoenum:: JPEG2000_COMPRESSION_PROFILE
    :members:
.. autoenum:: RASTER_BAND
    :members:
.. autoenum:: RASTER_FORMAT
    :members:
.. autoenum:: RASTER_ORIENTATION
    :members:
.. autoenum:: RASTER_TYPE
    :members:
.. autoenum:: SHARPEN_METHOD
    :members:
.. autoenum:: VIDEO_PLAYBACK
    :members:
.. autoenum:: KML_NETWORK_LINK_REFRESH_MODE
    :members:
.. autoenum:: KML_NETWORK_LINK_VIEW_REFRESH_MODE
    :members:
.. autoenum:: MODEL_UP_AXIS
    :members:
.. autoenum:: OUTLINE_APPEARANCE
    :members:
.. autoenum:: POLYLINE_TYPE
    :members:
.. autoenum:: CULL_FACE
    :members:
.. autoenum:: INTERNAL_TEXTURE_FORMAT
    :members:
.. autoenum:: MAGNIFICATION_FILTER
    :members:
.. autoenum:: MINIFICATION_FILTER
    :members:
.. autoenum:: RENDERER_SHADE_MODEL
    :members:
.. autoenum:: TEXTURE_WRAP
    :members:
.. autoenum:: SET_HINT
    :members:
.. autoenum:: STEREO_PROJECTION_MODE
    :members:
.. autoenum:: STEREOSCOPIC_DISPLAY_MODE
    :members:
.. autoenum:: FONT_STYLE
    :members:


Classes
~~~~~~~

.. autoclass:: PathPoint
    :members:
    :exclude-members: __init__
.. autoclass:: PathPointFactory
    :members:
    :exclude-members: __init__
.. autoclass:: BoundingSphere
    :members:
    :exclude-members: __init__
.. autoclass:: BoundingSphereFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TextureFilter2D
    :members:
    :exclude-members: __init__
.. autoclass:: TextureFilter2DFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RendererTexture2D
    :members:
    :exclude-members: __init__
.. autoclass:: RendererTextureTemplate2D
    :members:
    :exclude-members: __init__
.. autoclass:: PathPointCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ObjectCollection
    :members:
    :exclude-members: __init__
.. autoclass:: SceneCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlayPickResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: GlobeImageOverlayAddCompleteEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: TerrainOverlayAddCompleteEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: PickResultCollection
    :members:
    :exclude-members: __init__
.. autoclass:: RenderingEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: BatchPrimitiveIndex
    :members:
    :exclude-members: __init__
.. autoclass:: KmlDocumentCollection
    :members:
    :exclude-members: __init__
.. autoclass:: KmlFeatureCollection
    :members:
    :exclude-members: __init__
.. autoclass:: KmlDocumentLoadedEventArgs
    :members:
    :exclude-members: __init__
.. autoclass:: FactoryAndInitializers
    :members:
    :exclude-members: __init__
.. autoclass:: ExtrudedPolylineTriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: SolidTriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: SurfaceShapesResult
    :members:
    :exclude-members: __init__
.. autoclass:: SurfaceTriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: TriangulatorResult
    :members:
    :exclude-members: __init__
.. autoclass:: AGICustomTerrainOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: AGIProcessedImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: AGIProcessedTerrainOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: AGIRoamImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: CameraSnapshot
    :members:
    :exclude-members: __init__
.. autoclass:: CameraVideoRecording
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyGraphicsIndexer
    :members:
    :exclude-members: __init__
.. autoclass:: CustomImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: CustomImageGlobeOverlayPluginActivator
    :members:
    :exclude-members: __init__
.. autoclass:: CustomImageGlobeOverlayPluginProxy
    :members:
    :exclude-members: __init__
.. autoclass:: GeospatialImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: GlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: GlobeOverlaySettings
    :members:
    :exclude-members: __init__
.. autoclass:: Lighting
    :members:
    :exclude-members: __init__
.. autoclass:: PathPrimitiveUpdatePolicy
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectedRasterOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: Projection
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectionStream
    :members:
    :exclude-members: __init__
.. autoclass:: SceneGlobeOverlaySettings
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlayCollectionBase
    :members:
    :exclude-members: __init__
.. autoclass:: Texture2DFactory
    :members:
    :exclude-members: __init__
.. autoclass:: VisualEffects
    :members:
    :exclude-members: __init__
.. autoclass:: AltitudeDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: AxesPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: Camera
    :members:
    :exclude-members: __init__
.. autoclass:: CentralBodyGraphics
    :members:
    :exclude-members: __init__
.. autoclass:: Clouds
    :members:
    :exclude-members: __init__
.. autoclass:: CompositeDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: CompositePrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: ConstantDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: DisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceToGlobeOverlayDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceToPositionDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceToPrimitiveDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: DurationPathPrimitiveUpdatePolicy
    :members:
    :exclude-members: __init__
.. autoclass:: FrameRate
    :members:
    :exclude-members: __init__
.. autoclass:: GlobeImageOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: GraphicsFont
    :members:
    :exclude-members: __init__
.. autoclass:: GreatArcInterpolator
    :members:
    :exclude-members: __init__
.. autoclass:: ImageCollection
    :members:
    :exclude-members: __init__
.. autoclass:: AlphaFromLuminanceFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AlphaFromPixelFilter
    :members:
    :exclude-members: __init__
.. autoclass:: AlphaFromRasterFilter
    :members:
    :exclude-members: __init__
.. autoclass:: BandExtractFilter
    :members:
    :exclude-members: __init__
.. autoclass:: BandOrderFilter
    :members:
    :exclude-members: __init__
.. autoclass:: BlurFilter
    :members:
    :exclude-members: __init__
.. autoclass:: BrightnessFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ColorToLuminanceFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ContrastFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ConvolutionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: EdgeDetectFilter
    :members:
    :exclude-members: __init__
.. autoclass:: FilteringRasterStream
    :members:
    :exclude-members: __init__
.. autoclass:: FlipFilter
    :members:
    :exclude-members: __init__
.. autoclass:: GammaCorrectionFilter
    :members:
    :exclude-members: __init__
.. autoclass:: GaussianBlurFilter
    :members:
    :exclude-members: __init__
.. autoclass:: GradientDetectFilter
    :members:
    :exclude-members: __init__
.. autoclass:: LevelsFilter
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectionRasterStreamPluginActivator
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectionRasterStreamPluginProxy
    :members:
    :exclude-members: __init__
.. autoclass:: Raster
    :members:
    :exclude-members: __init__
.. autoclass:: RasterAttributes
    :members:
    :exclude-members: __init__
.. autoclass:: RasterFilter
    :members:
    :exclude-members: __init__
.. autoclass:: RasterStream
    :members:
    :exclude-members: __init__
.. autoclass:: RotateFilter
    :members:
    :exclude-members: __init__
.. autoclass:: SequenceFilter
    :members:
    :exclude-members: __init__
.. autoclass:: SharpenFilter
    :members:
    :exclude-members: __init__
.. autoclass:: VideoStream
    :members:
    :exclude-members: __init__
.. autoclass:: KmlContainer
    :members:
    :exclude-members: __init__
.. autoclass:: KmlDocument
    :members:
    :exclude-members: __init__
.. autoclass:: KmlFeature
    :members:
    :exclude-members: __init__
.. autoclass:: KmlFolder
    :members:
    :exclude-members: __init__
.. autoclass:: KmlGraphics
    :members:
    :exclude-members: __init__
.. autoclass:: KmlNetworkLink
    :members:
    :exclude-members: __init__
.. autoclass:: MarkerBatchPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: MarkerBatchPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: MaximumCountPathPrimitiveUpdatePolicy
    :members:
    :exclude-members: __init__
.. autoclass:: ModelArticulation
    :members:
    :exclude-members: __init__
.. autoclass:: ModelArticulationCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ModelPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: ModelTransformation
    :members:
    :exclude-members: __init__
.. autoclass:: Overlay
    :members:
    :exclude-members: __init__
.. autoclass:: PathPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: PickResult
    :members:
    :exclude-members: __init__
.. autoclass:: PixelSizeDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: PointBatchPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: PointBatchPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: PolylinePrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: PolylinePrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: PositionInterpolator
    :members:
    :exclude-members: __init__
.. autoclass:: Primitive
    :members:
    :exclude-members: __init__
.. autoclass:: PrimitiveManager
    :members:
    :exclude-members: __init__
.. autoclass:: RasterImageGlobeOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: RhumbLineInterpolator
    :members:
    :exclude-members: __init__
.. autoclass:: Scene
    :members:
    :exclude-members: __init__
.. autoclass:: SceneDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: SceneManager
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlayCollection
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlayManager
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlayPickResult
    :members:
    :exclude-members: __init__
.. autoclass:: SolidPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: Stereoscopic
    :members:
    :exclude-members: __init__
.. autoclass:: SurfaceMeshPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: TerrainOverlayCollection
    :members:
    :exclude-members: __init__
.. autoclass:: TerrainOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: TextBatchPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: TextBatchPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: TextOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: TextureMatrix
    :members:
    :exclude-members: __init__
.. autoclass:: TextureScreenOverlay
    :members:
    :exclude-members: __init__
.. autoclass:: TimeIntervalDisplayCondition
    :members:
    :exclude-members: __init__
.. autoclass:: TriangleMeshPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: TriangleMeshPrimitiveOptionalParameters
    :members:
    :exclude-members: __init__
.. autoclass:: VectorPrimitive
    :members:
    :exclude-members: __init__
.. autoclass:: BoxTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: CylinderTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: EllipsoidTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ExtrudedPolylineTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: SurfaceExtentTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: SurfacePolygonTriangulatorInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: SurfaceShapesInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: AGICustomTerrainOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AGIProcessedImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AGIProcessedTerrainOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AGIRoamImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CustomImageGlobeOverlayPluginActivatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GeospatialImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectedRasterOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AltitudeDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AxesPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CompositeDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: CompositePrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ConstantDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceToGlobeOverlayDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceToPositionDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: DistanceToPrimitiveDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: DurationPathPrimitiveUpdatePolicyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GlobeImageOverlayInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: GraphicsFontFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GreatArcInterpolatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AlphaFromLuminanceFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AlphaFromPixelFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: AlphaFromRasterFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: BandExtractFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: BandOrderFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: BlurFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: BrightnessFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ColorToLuminanceFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ContrastFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ConvolutionFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: EdgeDetectFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: FilteringRasterStreamFactory
    :members:
    :exclude-members: __init__
.. autoclass:: FlipFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GammaCorrectionFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GaussianBlurFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: GradientDetectFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: Jpeg2000WriterInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: LevelsFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ProjectionRasterStreamPluginActivatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RasterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RasterAttributesFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RotateFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SequenceFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SharpenFilterFactory
    :members:
    :exclude-members: __init__
.. autoclass:: VideoStreamFactory
    :members:
    :exclude-members: __init__
.. autoclass:: MarkerBatchPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: MarkerBatchPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: MaximumCountPathPrimitiveUpdatePolicyFactory
    :members:
    :exclude-members: __init__
.. autoclass:: ModelPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PathPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PixelSizeDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PointBatchPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PointBatchPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PolylinePrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: PolylinePrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RasterImageGlobeOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: RhumbLineInterpolatorFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SceneDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SceneManagerInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: ScreenOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SolidPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: SurfaceMeshPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TerrainOverlayInitializer
    :members:
    :exclude-members: __init__
.. autoclass:: TextBatchPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TextBatchPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TextOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TextureMatrixFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TextureScreenOverlayFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TimeIntervalDisplayConditionFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TriangleMeshPrimitiveFactory
    :members:
    :exclude-members: __init__
.. autoclass:: TriangleMeshPrimitiveOptionalParametersFactory
    :members:
    :exclude-members: __init__
.. autoclass:: VectorPrimitiveFactory
    :members:
    :exclude-members: __init__

