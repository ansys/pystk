
The ``AgSTKGraphicsLib`` module
===============================


.. py::module:: ansys.stk.core.graphics


Summary
-------

.. tab-set::
    .. tab-items:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~IPathPoint`
              - A path point used with the Path Primitive.

            * - :pyclass:`~IPathPointFactory`
              - Create Path Primitive's path points.

            * - :pyclass:`~IBoundingSphere`
              - A sphere that encapsulates an object.

            * - :pyclass:`~IBoundingSphereFactory`
              - Create instances of the bounding sphere type.

            * - :pyclass:`~ITextureFilter2D`
              - A texture filter.

            * - :pyclass:`~ITextureFilter2DFactory`
              - Create texture filters.

            * - :pyclass:`~IRendererTexture2D`
              - A 2D Texture. A texture represents an image that is ready for use by objects such as primitives and overlays. Textures typically reside in video memory.

            * - :pyclass:`~IRendererTextureTemplate2D`
              - Template object containing attributes required to create a 2D texture.

            * - :pyclass:`~IPathPointCollection`
              - A collection of path points.

            * - :pyclass:`~IObjectCollection`
              - A collection of objects.

            * - :pyclass:`~ISceneCollection`
              - A collection of scenes.

            * - :pyclass:`~IScreenOverlayContainer`
              - The interface for screen overlays that contain a collection of other overlays. This interface is implemented by ScreenOverlayManager and ScreenOverlay.

            * - :pyclass:`~IScreenOverlayPickResultCollection`
              - A collection of pick results.

            * - :pyclass:`~IGlobeImageOverlayAddCompleteEventArgs`
              - The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

            * - :pyclass:`~ITerrainOverlayAddCompleteEventArgs`
              - The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

            * - :pyclass:`~IPickResultCollection`
              - A collection of picked objects.

            * - :pyclass:`~IRenderingEventArgs`
              - The event is raised when the scene is rendered.

            * - :pyclass:`~IBatchPrimitiveIndex`
              - Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

            * - :pyclass:`~IKmlDocumentCollection`
              - A collection of KML documents.

            * - :pyclass:`~IKmlFeatureCollection`
              - A collection of KML features.

            * - :pyclass:`~IKmlDocumentLoadedEventArgs`
              - The event is raised when a KML document has been loaded.

            * - :pyclass:`~IFactoryAndInitializers`
              - Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

            * - :pyclass:`~IExtrudedPolylineTriangulatorResult`
              - The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :pyclass:`~ISolidTriangulatorResult`
              - The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

            * - :pyclass:`~ISurfaceShapesResult`
              - Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

            * - :pyclass:`~ISurfaceTriangulatorResult`
              - The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

            * - :pyclass:`~ITriangulatorResult`
              - The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

            * - :pyclass:`~IAGICustomTerrainOverlay`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :pyclass:`~IAGIProcessedImageGlobeOverlay`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :pyclass:`~IAGIProcessedTerrainOverlay`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :pyclass:`~IAGIRoamImageGlobeOverlay`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :pyclass:`~ICameraSnapshot`
              - Takes snapshots of the 3D window.

            * - :pyclass:`~ICameraVideoRecording`
              - Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

            * - :pyclass:`~ICentralBodyGraphicsIndexer`
              - An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

            * - :pyclass:`~ICustomImageGlobeOverlay`
              - A globe image overlay that allows for a user defined image to be specified.

            * - :pyclass:`~ICustomImageGlobeOverlayPluginActivator`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :pyclass:`~ICustomImageGlobeOverlayPluginProxy`
              - A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

            * - :pyclass:`~IGeospatialImageGlobeOverlay`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :pyclass:`~IGlobeOverlay`
              - The base class of all terrain overlay and globe image overlay objects.

            * - :pyclass:`~IGlobeOverlaySettings`
              - Settings used by globe overlay objects. These setting affect all scenes.

            * - :pyclass:`~ILighting`
              - Lighting in the 3D scene.

            * - :pyclass:`~IPathPrimitiveUpdatePolicy`
              - A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

            * - :pyclass:`~IProjectedRasterOverlay`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :pyclass:`~IProjection`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :pyclass:`~IProjectionStream`
              - A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

            * - :pyclass:`~ISceneGlobeOverlaySettings`
              - Settings used by globe overlay objects. These settings only affect the scene.

            * - :pyclass:`~IScreenOverlayCollectionBase`
              - The common base class for collections of overlays held by screen overlay and by screen overlay manager.

            * - :pyclass:`~ITexture2DFactory`
              - A factory for creating texture 2d objects from various sources.

            * - :pyclass:`~IVisualEffects`
              - Control various post processing effects that can be applied to the scene.

            * - :pyclass:`~IAltitudeDisplayCondition`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :pyclass:`~IAxesPrimitive`
              - Render an axes in the 3D scene.

            * - :pyclass:`~ICamera`
              - Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

            * - :pyclass:`~ICentralBodyGraphics`
              - The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

            * - :pyclass:`~IClouds`
              - Load, show and hide clouds in the scene.

            * - :pyclass:`~ICompositeDisplayCondition`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :pyclass:`~ICompositePrimitive`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :pyclass:`~IConstantDisplayCondition`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :pyclass:`~IDisplayCondition`
              - When assigned to objects, such as primitives or globe overlays, display conditions are evaluated to determine if the object should be rendered.

            * - :pyclass:`~IDistanceDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :pyclass:`~IDistanceToGlobeOverlayDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :pyclass:`~IDistanceToPositionDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :pyclass:`~IDistanceToPrimitiveDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :pyclass:`~IDurationPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :pyclass:`~IFrameRate`
              - Keeps track of how many times the scenes are rendered per second.

            * - :pyclass:`~IGlobeImageOverlay`
              - A globe overlay that shows an image.

            * - :pyclass:`~IGraphicsFont`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :pyclass:`~IGreatArcInterpolator`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :pyclass:`~IImageCollection`
              - A collection of globe image overlay objects.

            * - :pyclass:`~IAlphaFromLuminanceFilter`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :pyclass:`~IAlphaFromPixelFilter`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :pyclass:`~IAlphaFromRasterFilter`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :pyclass:`~IBandExtractFilter`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :pyclass:`~IBandOrderFilter`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :pyclass:`~IBlurFilter`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :pyclass:`~IBrightnessFilter`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :pyclass:`~IColorToLuminanceFilter`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :pyclass:`~IContrastFilter`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :pyclass:`~IConvolutionFilter`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :pyclass:`~IEdgeDetectFilter`
              - Apply a convolution filter to detect edges in the source raster.

            * - :pyclass:`~IFilteringRasterStream`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :pyclass:`~IFlipFilter`
              - Flips the source raster along the given flip axis.

            * - :pyclass:`~IGammaCorrectionFilter`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :pyclass:`~IGaussianBlurFilter`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :pyclass:`~IGradientDetectFilter`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :pyclass:`~ILevelsFilter`
              - Adjusts the band levels of the source raster linearly.

            * - :pyclass:`~IProjectionRasterStreamPluginActivator`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :pyclass:`~IProjectionRasterStreamPluginProxy`
              - A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

            * - :pyclass:`~IRaster`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :pyclass:`~IRasterAttributes`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :pyclass:`~IRasterFilter`
              - A filter for processing raster datasets. RasterFilter is the base class for all raster filters...

            * - :pyclass:`~IRasterStream`
              - A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

            * - :pyclass:`~IRotateFilter`
              - Rotate the source raster clockwise by the specified angle.

            * - :pyclass:`~ISequenceFilter`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :pyclass:`~ISharpenFilter`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :pyclass:`~IVideoStream`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :pyclass:`~IKmlContainer`
              - A KmlContainer contains a collection of children kml features.

            * - :pyclass:`~IKmlDocument`
              - A KML document.

            * - :pyclass:`~IKmlFeature`
              - A KML feature.

            * - :pyclass:`~IKmlFolder`
              - A KML folder.

            * - :pyclass:`~IKmlGraphics`
              - Provide loading and unloading of kml documents for a particular central body.

            * - :pyclass:`~IKmlNetworkLink`
              - A KML network link.

            * - :pyclass:`~IMarkerBatchPrimitive`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :pyclass:`~IMarkerBatchPrimitiveOptionalParameters`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :pyclass:`~IMaximumCountPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :pyclass:`~IModelArticulation`
              - A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :pyclass:`~IModelArticulationCollection`
              - A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :pyclass:`~IModelPrimitive`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :pyclass:`~IModelTransformation`
              - A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

            * - :pyclass:`~IOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :pyclass:`~IPathPrimitive`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :pyclass:`~IPickResult`
              - A single result from Pick.

            * - :pyclass:`~IPixelSizeDisplayCondition`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :pyclass:`~IPointBatchPrimitive`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :pyclass:`~IPointBatchPrimitiveOptionalParameters`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :pyclass:`~IPolylinePrimitive`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :pyclass:`~IPolylinePrimitiveOptionalParameters`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :pyclass:`~IPositionInterpolator`
              - Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

            * - :pyclass:`~IPrimitive`
              - Primitives represent objects rendered in the 3D scene.

            * - :pyclass:`~IPrimitiveManager`
              - The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

            * - :pyclass:`~IRasterImageGlobeOverlay`
              - A globe image overlay for handling rasters.

            * - :pyclass:`~IRhumbLineInterpolator`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :pyclass:`~IScene`
              - A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

            * - :pyclass:`~ISceneDisplayCondition`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :pyclass:`~ISceneManager`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :pyclass:`~IScreenOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :pyclass:`~IScreenOverlayCollection`
              - A collection of screen overlays.

            * - :pyclass:`~IScreenOverlayManager`
              - The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

            * - :pyclass:`~IScreenOverlayPickResult`
              - Describes a picked screen overlay as a result of a call to pick screen overlays.

            * - :pyclass:`~ISolidPrimitive`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :pyclass:`~IStereoscopic`
              - Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :pyclass:`~ISurfaceMeshPrimitive`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :pyclass:`~ITerrainOverlayCollection`
              - A collection of terrain overlay objects.

            * - :pyclass:`~ITerrainOverlay`
              - A globe overlay which shows terrain.

            * - :pyclass:`~ITextBatchPrimitive`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :pyclass:`~ITextBatchPrimitiveOptionalParameters`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :pyclass:`~ITextOverlay`
              - A rectangular overlay that contains text.

            * - :pyclass:`~ITextureMatrix`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :pyclass:`~ITextureScreenOverlay`
              - A rectangular overlay that can be assigned a texture.

            * - :pyclass:`~ITimeIntervalDisplayCondition`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :pyclass:`~ITriangleMeshPrimitive`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :pyclass:`~ITriangleMeshPrimitiveOptionalParameters`
              - Optional parameters for triangle mesh primitive...

            * - :pyclass:`~IVectorPrimitive`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

            * - :pyclass:`~IBoxTriangulatorInitializer`
              - Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :pyclass:`~ICylinderTriangulatorInitializer`
              - Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :pyclass:`~IEllipsoidTriangulatorInitializer`
              - Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :pyclass:`~IExtrudedPolylineTriangulatorInitializer`
              - Triangulates a polyline into an extrusion with bottom and top boundaries.

            * - :pyclass:`~ISurfaceExtentTriangulatorInitializer`
              - Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

            * - :pyclass:`~ISurfacePolygonTriangulatorInitializer`
              - Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :pyclass:`~ISurfaceShapesInitializer`
              - Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

            * - :pyclass:`~IAGICustomTerrainOverlayFactory`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :pyclass:`~IAGIProcessedImageGlobeOverlayFactory`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :pyclass:`~IAGIProcessedTerrainOverlayFactory`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :pyclass:`~IAGIRoamImageGlobeOverlayFactory`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :pyclass:`~ICustomImageGlobeOverlayPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :pyclass:`~IGeospatialImageGlobeOverlayFactory`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :pyclass:`~IProjectedRasterOverlayFactory`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :pyclass:`~IProjectionFactory`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :pyclass:`~IAltitudeDisplayConditionFactory`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :pyclass:`~IAxesPrimitiveFactory`
              - Render an axes in the 3D scene.

            * - :pyclass:`~ICompositeDisplayConditionFactory`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :pyclass:`~ICompositePrimitiveFactory`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :pyclass:`~IConstantDisplayConditionFactory`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :pyclass:`~IDistanceDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :pyclass:`~IDistanceToGlobeOverlayDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :pyclass:`~IDistanceToPositionDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :pyclass:`~IDistanceToPrimitiveDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :pyclass:`~IDurationPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :pyclass:`~IGlobeImageOverlayInitializer`
              - A globe overlay that shows an image.

            * - :pyclass:`~IGraphicsFontFactory`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :pyclass:`~IGreatArcInterpolatorFactory`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :pyclass:`~IAlphaFromLuminanceFilterFactory`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :pyclass:`~IAlphaFromPixelFilterFactory`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :pyclass:`~IAlphaFromRasterFilterFactory`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :pyclass:`~IBandExtractFilterFactory`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :pyclass:`~IBandOrderFilterFactory`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :pyclass:`~IBlurFilterFactory`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :pyclass:`~IBrightnessFilterFactory`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :pyclass:`~IColorToLuminanceFilterFactory`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :pyclass:`~IContrastFilterFactory`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :pyclass:`~IConvolutionFilterFactory`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :pyclass:`~IEdgeDetectFilterFactory`
              - Apply a convolution filter to detect edges in the source raster.

            * - :pyclass:`~IFilteringRasterStreamFactory`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :pyclass:`~IFlipFilterFactory`
              - Flips the source raster along the given flip axis.

            * - :pyclass:`~IGammaCorrectionFilterFactory`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :pyclass:`~IGaussianBlurFilterFactory`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :pyclass:`~IGradientDetectFilterFactory`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :pyclass:`~IJpeg2000WriterInitializer`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

            * - :pyclass:`~ILevelsFilterFactory`
              - Adjusts the band levels of the source raster linearly.

            * - :pyclass:`~IProjectionRasterStreamPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :pyclass:`~IRasterFactory`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :pyclass:`~IRasterAttributesFactory`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :pyclass:`~IRotateFilterFactory`
              - Rotate the source raster clockwise by the specified angle.

            * - :pyclass:`~ISequenceFilterFactory`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :pyclass:`~ISharpenFilterFactory`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :pyclass:`~IVideoStreamFactory`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :pyclass:`~IMarkerBatchPrimitiveFactory`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :pyclass:`~IMarkerBatchPrimitiveOptionalParametersFactory`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :pyclass:`~IMaximumCountPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :pyclass:`~IModelPrimitiveFactory`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :pyclass:`~IPathPrimitiveFactory`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :pyclass:`~IPixelSizeDisplayConditionFactory`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :pyclass:`~IPointBatchPrimitiveFactory`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :pyclass:`~IPointBatchPrimitiveOptionalParametersFactory`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :pyclass:`~IPolylinePrimitiveFactory`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :pyclass:`~IPolylinePrimitiveOptionalParametersFactory`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :pyclass:`~IRasterImageGlobeOverlayFactory`
              - A globe image overlay for handling rasters.

            * - :pyclass:`~IRhumbLineInterpolatorFactory`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :pyclass:`~ISceneDisplayConditionFactory`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :pyclass:`~ISceneManagerInitializer`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :pyclass:`~IScreenOverlayFactory`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :pyclass:`~ISolidPrimitiveFactory`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :pyclass:`~ISurfaceMeshPrimitiveFactory`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :pyclass:`~ITerrainOverlayInitializer`
              - A globe overlay which shows terrain.

            * - :pyclass:`~ITextBatchPrimitiveFactory`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :pyclass:`~ITextBatchPrimitiveOptionalParametersFactory`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :pyclass:`~ITextOverlayFactory`
              - A rectangular overlay that contains text.

            * - :pyclass:`~ITextureMatrixFactory`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :pyclass:`~ITextureScreenOverlayFactory`
              - A rectangular overlay that can be assigned a texture.

            * - :pyclass:`~ITimeIntervalDisplayConditionFactory`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :pyclass:`~ITriangleMeshPrimitiveFactory`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :pyclass:`~ITriangleMeshPrimitiveOptionalParametersFactory`
              - Optional parameters for triangle mesh primitive...

            * - :pyclass:`~IVectorPrimitiveFactory`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

    
    .. tab-items:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~PathPoint`
              - Represents a path point used in conjunction with the Path Primitive.

            * - :pyclass:`~PathPointFactory`
              - Factory creates path points.

            * - :pyclass:`~BoundingSphere`
              - A sphere that encapsulates an object.

            * - :pyclass:`~BoundingSphereFactory`
              - Create bounding spheres.

            * - :pyclass:`~TextureFilter2D`
              - A texture filter.

            * - :pyclass:`~TextureFilter2DFactory`
              - Create texture filters.

            * - :pyclass:`~RendererTexture2D`
              - A 2D Texture. A texture represents an image that is ready for use by objects such as primitives and overlays. Textures typically reside in video memory.

            * - :pyclass:`~RendererTextureTemplate2D`
              - Template object containing attributes required to create a 2D texture.

            * - :pyclass:`~PathPointCollection`
              - A collection of path points.

            * - :pyclass:`~ObjectCollection`
              - A collection of objects.

            * - :pyclass:`~SceneCollection`
              - A collection of scenes.

            * - :pyclass:`~ScreenOverlayPickResultCollection`
              - A collection of pick results.

            * - :pyclass:`~GlobeImageOverlayAddCompleteEventArgs`
              - The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

            * - :pyclass:`~TerrainOverlayAddCompleteEventArgs`
              - The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

            * - :pyclass:`~PickResultCollection`
              - A collection of picked objects.

            * - :pyclass:`~RenderingEventArgs`
              - The event is raised when the scene is rendered.

            * - :pyclass:`~BatchPrimitiveIndex`
              - Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

            * - :pyclass:`~KmlDocumentCollection`
              - A collection of KML documents.

            * - :pyclass:`~KmlFeatureCollection`
              - A collection of KML features.

            * - :pyclass:`~KmlDocumentLoadedEventArgs`
              - The event is raised when a KML document has been loaded.

            * - :pyclass:`~FactoryAndInitializers`
              - Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

            * - :pyclass:`~ExtrudedPolylineTriangulatorResult`
              - The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :pyclass:`~SolidTriangulatorResult`
              - The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

            * - :pyclass:`~SurfaceShapesResult`
              - Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

            * - :pyclass:`~SurfaceTriangulatorResult`
              - The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

            * - :pyclass:`~TriangulatorResult`
              - The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

            * - :pyclass:`~AGICustomTerrainOverlay`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :pyclass:`~AGIProcessedImageGlobeOverlay`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :pyclass:`~AGIProcessedTerrainOverlay`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :pyclass:`~AGIRoamImageGlobeOverlay`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :pyclass:`~CameraSnapshot`
              - Takes snapshots of the 3D window.

            * - :pyclass:`~CameraVideoRecording`
              - Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

            * - :pyclass:`~CentralBodyGraphicsIndexer`
              - An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

            * - :pyclass:`~CustomImageGlobeOverlay`
              - A globe image overlay that allows for a user defined image to be specified.

            * - :pyclass:`~CustomImageGlobeOverlayPluginActivator`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :pyclass:`~CustomImageGlobeOverlayPluginProxy`
              - A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

            * - :pyclass:`~GeospatialImageGlobeOverlay`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :pyclass:`~GlobeOverlay`
              - The base class of all terrain overlay and globe image overlay objects.

            * - :pyclass:`~GlobeOverlaySettings`
              - Settings used by globe overlay objects. These setting affect all scenes.

            * - :pyclass:`~Lighting`
              - Lighting in the 3D scene.

            * - :pyclass:`~PathPrimitiveUpdatePolicy`
              - A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

            * - :pyclass:`~ProjectedRasterOverlay`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :pyclass:`~Projection`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :pyclass:`~ProjectionStream`
              - A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

            * - :pyclass:`~SceneGlobeOverlaySettings`
              - Settings used by globe overlay objects. These settings only affect the scene.

            * - :pyclass:`~ScreenOverlayCollectionBase`
              - The common base class for collections of overlays held by screen overlay and by screen overlay manager.

            * - :pyclass:`~Texture2DFactory`
              - A factory for creating texture 2d objects from various sources.

            * - :pyclass:`~VisualEffects`
              - Control various post processing effects that can be applied to the scene.

            * - :pyclass:`~AltitudeDisplayCondition`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :pyclass:`~AxesPrimitive`
              - Render an axes in the 3D scene.

            * - :pyclass:`~Camera`
              - Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

            * - :pyclass:`~CentralBodyGraphics`
              - The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

            * - :pyclass:`~Clouds`
              - Load, show and hide clouds in the scene.

            * - :pyclass:`~CompositeDisplayCondition`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :pyclass:`~CompositePrimitive`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :pyclass:`~ConstantDisplayCondition`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :pyclass:`~DisplayCondition`
              - When assigned to objects, such as primitives or globe overlays, display conditions are evaluated to determine if the object should be rendered.

            * - :pyclass:`~DistanceDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :pyclass:`~DistanceToGlobeOverlayDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :pyclass:`~DistanceToPositionDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :pyclass:`~DistanceToPrimitiveDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :pyclass:`~DurationPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :pyclass:`~FrameRate`
              - Keeps track of how many times the scenes are rendered per second.

            * - :pyclass:`~GlobeImageOverlay`
              - A globe overlay that shows an image.

            * - :pyclass:`~GraphicsFont`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :pyclass:`~GreatArcInterpolator`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :pyclass:`~ImageCollection`
              - A collection of globe image overlay objects.

            * - :pyclass:`~AlphaFromLuminanceFilter`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :pyclass:`~AlphaFromPixelFilter`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :pyclass:`~AlphaFromRasterFilter`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :pyclass:`~BandExtractFilter`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :pyclass:`~BandOrderFilter`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :pyclass:`~BlurFilter`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :pyclass:`~BrightnessFilter`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :pyclass:`~ColorToLuminanceFilter`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :pyclass:`~ContrastFilter`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :pyclass:`~ConvolutionFilter`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :pyclass:`~EdgeDetectFilter`
              - Apply a convolution filter to detect edges in the source raster.

            * - :pyclass:`~FilteringRasterStream`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :pyclass:`~FlipFilter`
              - Flips the source raster along the given flip axis.

            * - :pyclass:`~GammaCorrectionFilter`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :pyclass:`~GaussianBlurFilter`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :pyclass:`~GradientDetectFilter`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :pyclass:`~LevelsFilter`
              - Adjusts the band levels of the source raster linearly.

            * - :pyclass:`~ProjectionRasterStreamPluginActivator`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :pyclass:`~ProjectionRasterStreamPluginProxy`
              - A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

            * - :pyclass:`~Raster`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :pyclass:`~RasterAttributes`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :pyclass:`~RasterFilter`
              - A filter for processing raster datasets. RasterFilter is the base class for all raster filters...

            * - :pyclass:`~RasterStream`
              - A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

            * - :pyclass:`~RotateFilter`
              - Rotate the source raster clockwise by the specified angle.

            * - :pyclass:`~SequenceFilter`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :pyclass:`~SharpenFilter`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :pyclass:`~VideoStream`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :pyclass:`~KmlContainer`
              - A KmlContainer contains a collection of children kml features.

            * - :pyclass:`~KmlDocument`
              - A KML document.

            * - :pyclass:`~KmlFeature`
              - A KML feature.

            * - :pyclass:`~KmlFolder`
              - A KML folder.

            * - :pyclass:`~KmlGraphics`
              - Provide loading and unloading of kml documents for a particular central body.

            * - :pyclass:`~KmlNetworkLink`
              - A KML network link.

            * - :pyclass:`~MarkerBatchPrimitive`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :pyclass:`~MarkerBatchPrimitiveOptionalParameters`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :pyclass:`~MaximumCountPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :pyclass:`~ModelArticulation`
              - A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :pyclass:`~ModelArticulationCollection`
              - A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :pyclass:`~ModelPrimitive`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :pyclass:`~ModelTransformation`
              - A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

            * - :pyclass:`~Overlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :pyclass:`~PathPrimitive`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :pyclass:`~PickResult`
              - A single result from Pick.

            * - :pyclass:`~PixelSizeDisplayCondition`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :pyclass:`~PointBatchPrimitive`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :pyclass:`~PointBatchPrimitiveOptionalParameters`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :pyclass:`~PolylinePrimitive`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :pyclass:`~PolylinePrimitiveOptionalParameters`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :pyclass:`~PositionInterpolator`
              - Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

            * - :pyclass:`~Primitive`
              - Primitives represent objects rendered in the 3D scene.

            * - :pyclass:`~PrimitiveManager`
              - The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

            * - :pyclass:`~RasterImageGlobeOverlay`
              - A globe image overlay for handling rasters.

            * - :pyclass:`~RhumbLineInterpolator`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :pyclass:`~Scene`
              - A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

            * - :pyclass:`~SceneDisplayCondition`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :pyclass:`~SceneManager`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :pyclass:`~ScreenOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :pyclass:`~ScreenOverlayCollection`
              - A collection of screen overlays.

            * - :pyclass:`~ScreenOverlayManager`
              - The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

            * - :pyclass:`~ScreenOverlayPickResult`
              - Describes a picked screen overlay as a result of a call to pick screen overlays.

            * - :pyclass:`~SolidPrimitive`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :pyclass:`~Stereoscopic`
              - Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :pyclass:`~SurfaceMeshPrimitive`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :pyclass:`~TerrainOverlayCollection`
              - A collection of terrain overlay objects.

            * - :pyclass:`~TerrainOverlay`
              - A globe overlay which shows terrain.

            * - :pyclass:`~TextBatchPrimitive`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :pyclass:`~TextBatchPrimitiveOptionalParameters`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :pyclass:`~TextOverlay`
              - A rectangular overlay that contains text.

            * - :pyclass:`~TextureMatrix`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :pyclass:`~TextureScreenOverlay`
              - A rectangular overlay that can be assigned a texture.

            * - :pyclass:`~TimeIntervalDisplayCondition`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :pyclass:`~TriangleMeshPrimitive`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :pyclass:`~TriangleMeshPrimitiveOptionalParameters`
              - Optional parameters for triangle mesh primitive...

            * - :pyclass:`~VectorPrimitive`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

            * - :pyclass:`~BoxTriangulatorInitializer`
              - Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :pyclass:`~CylinderTriangulatorInitializer`
              - Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :pyclass:`~EllipsoidTriangulatorInitializer`
              - Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :pyclass:`~ExtrudedPolylineTriangulatorInitializer`
              - Triangulates a polyline into an extrusion with bottom and top boundaries.

            * - :pyclass:`~SurfaceExtentTriangulatorInitializer`
              - Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

            * - :pyclass:`~SurfacePolygonTriangulatorInitializer`
              - Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :pyclass:`~SurfaceShapesInitializer`
              - Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

            * - :pyclass:`~AGICustomTerrainOverlayFactory`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :pyclass:`~AGIProcessedImageGlobeOverlayFactory`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :pyclass:`~AGIProcessedTerrainOverlayFactory`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :pyclass:`~AGIRoamImageGlobeOverlayFactory`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :pyclass:`~CustomImageGlobeOverlayPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :pyclass:`~GeospatialImageGlobeOverlayFactory`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :pyclass:`~ProjectedRasterOverlayFactory`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :pyclass:`~ProjectionFactory`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :pyclass:`~AltitudeDisplayConditionFactory`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :pyclass:`~AxesPrimitiveFactory`
              - Render an axes in the 3D scene.

            * - :pyclass:`~CompositeDisplayConditionFactory`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :pyclass:`~CompositePrimitiveFactory`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :pyclass:`~ConstantDisplayConditionFactory`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :pyclass:`~DistanceDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :pyclass:`~DistanceToGlobeOverlayDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :pyclass:`~DistanceToPositionDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :pyclass:`~DistanceToPrimitiveDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :pyclass:`~DurationPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :pyclass:`~GlobeImageOverlayInitializer`
              - A globe overlay that shows an image.

            * - :pyclass:`~GraphicsFontFactory`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :pyclass:`~GreatArcInterpolatorFactory`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :pyclass:`~AlphaFromLuminanceFilterFactory`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :pyclass:`~AlphaFromPixelFilterFactory`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :pyclass:`~AlphaFromRasterFilterFactory`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :pyclass:`~BandExtractFilterFactory`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :pyclass:`~BandOrderFilterFactory`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :pyclass:`~BlurFilterFactory`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :pyclass:`~BrightnessFilterFactory`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :pyclass:`~ColorToLuminanceFilterFactory`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :pyclass:`~ContrastFilterFactory`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :pyclass:`~ConvolutionFilterFactory`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :pyclass:`~EdgeDetectFilterFactory`
              - Apply a convolution filter to detect edges in the source raster.

            * - :pyclass:`~FilteringRasterStreamFactory`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :pyclass:`~FlipFilterFactory`
              - Flips the source raster along the given flip axis.

            * - :pyclass:`~GammaCorrectionFilterFactory`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :pyclass:`~GaussianBlurFilterFactory`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :pyclass:`~GradientDetectFilterFactory`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :pyclass:`~Jpeg2000WriterInitializer`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

            * - :pyclass:`~LevelsFilterFactory`
              - Adjusts the band levels of the source raster linearly.

            * - :pyclass:`~ProjectionRasterStreamPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :pyclass:`~RasterFactory`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :pyclass:`~RasterAttributesFactory`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :pyclass:`~RotateFilterFactory`
              - Rotate the source raster clockwise by the specified angle.

            * - :pyclass:`~SequenceFilterFactory`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :pyclass:`~SharpenFilterFactory`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :pyclass:`~VideoStreamFactory`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :pyclass:`~MarkerBatchPrimitiveFactory`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :pyclass:`~MarkerBatchPrimitiveOptionalParametersFactory`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :pyclass:`~MaximumCountPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :pyclass:`~ModelPrimitiveFactory`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :pyclass:`~PathPrimitiveFactory`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :pyclass:`~PixelSizeDisplayConditionFactory`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :pyclass:`~PointBatchPrimitiveFactory`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :pyclass:`~PointBatchPrimitiveOptionalParametersFactory`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :pyclass:`~PolylinePrimitiveFactory`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :pyclass:`~PolylinePrimitiveOptionalParametersFactory`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :pyclass:`~RasterImageGlobeOverlayFactory`
              - A globe image overlay for handling rasters.

            * - :pyclass:`~RhumbLineInterpolatorFactory`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :pyclass:`~SceneDisplayConditionFactory`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :pyclass:`~SceneManagerInitializer`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :pyclass:`~ScreenOverlayFactory`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :pyclass:`~SolidPrimitiveFactory`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :pyclass:`~SurfaceMeshPrimitiveFactory`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :pyclass:`~TerrainOverlayInitializer`
              - A globe overlay which shows terrain.

            * - :pyclass:`~TextBatchPrimitiveFactory`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :pyclass:`~TextBatchPrimitiveOptionalParametersFactory`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :pyclass:`~TextOverlayFactory`
              - A rectangular overlay that contains text.

            * - :pyclass:`~TextureMatrixFactory`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :pyclass:`~TextureScreenOverlayFactory`
              - A rectangular overlay that can be assigned a texture.

            * - :pyclass:`~TimeIntervalDisplayConditionFactory`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :pyclass:`~TriangleMeshPrimitiveFactory`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :pyclass:`~TriangleMeshPrimitiveOptionalParametersFactory`
              - Optional parameters for triangle mesh primitive...

            * - :pyclass:`~VectorPrimitiveFactory`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.


    .. tab-items:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :pyclass:`~CYLINDER_FILL`
              - Cylinder faces that can be filled.

            * - :pyclass:`~WINDING_ORDER`
              - Specify the order for positions or front facing triangles. Winding order is important for triangulation and backface culling.

            * - :pyclass:`~CAMERA_SNAPSHOT_FILE_FORMAT`
              - When using camera snapshot or camera video recording to save a snapshot to a file, this specifies the file format.

            * - :pyclass:`~CAMERA_VIDEO_FORMAT`
              - When using camera video recording to record a video, this specifies the file format.

            * - :pyclass:`~CONSTRAINED_UP_AXIS`
              - When setting the camera'saxes, this defines which axis of the axes is up in screen space, where up is from the bottom to the top of the screen.

            * - :pyclass:`~GLOBE_OVERLAY_ROLE`
              - The role of a globe overlay.

            * - :pyclass:`~INDICES_ORDER_HINT`
              - An optimization hint optionally provided to a primitive'sSetPartial method to enhance performance.

            * - :pyclass:`~MAINTAIN_ASPECT_RATIO`
              - Specify whether the aspect ratio of a texture will be maintained during sizing of a screen overlay.

            * - :pyclass:`~MAP_PROJECTION`
              - The projection of the pixel data returned from a custom image globe overlay.

            * - :pyclass:`~MARKER_BATCH_RENDERING_METHOD`
              - Rendering methods available for use by the marker batch primitive. Different methods may have different performance characteristics and require different video card support. When in doubt, use Automatic.

            * - :pyclass:`~MARKER_BATCH_RENDER_PASS`
              - The pass during which the marker batch is rendered.

            * - :pyclass:`~MARKER_BATCH_SIZE_SOURCE`
              - Determine which marker batch property is used to size each marker in a marker batch.

            * - :pyclass:`~MARKER_BATCH_SORT_ORDER`
              - The order in which markers in a marker batch are sorted before rendering.

            * - :pyclass:`~MARKER_BATCH_UNIT`
              - The unit for marker sizes in a marker batch.

            * - :pyclass:`~MODEL_TRANSFORMATION_TYPE`
              - Transformation types that define the way a model transformation changes the geometry of the model articulation it is associated with.

            * - :pyclass:`~ORIGIN`
              - Vertical and horizontal origin.

            * - :pyclass:`~PATH_PRIMITIVE_REMOVE_LOCATION`
              - Represents the location of a point to be removed.

            * - :pyclass:`~PRIMITIVES_SORT_ORDER`
              - The order in which primitives are sorted before rendering.

            * - :pyclass:`~REFRESH_RATE`
              - The rate at which animation frames will occur.

            * - :pyclass:`~RENDER_PASS`
              - Describes when a primitive will be rendered. Some primitives need to be rendered during or at a certain time. For example, translucent primitives need to be rendered after opaque primitives to allow proper blending...

            * - :pyclass:`~RENDER_PASS_HINT`
              - An optimization hint optionally provided to a primitive'sSet method to enhance performance when per-position colors are used.

            * - :pyclass:`~SCREEN_OVERLAY_ORIGIN`
              - Specify the origin of a screen overlay, as well as the direction of the horizontal and vertical axes. The origin specifies both the origin in the parent overlay's coordinate system and the origin within the overlay itself that is positioned.

            * - :pyclass:`~SCREEN_OVERLAY_PINNING_ORIGIN`
              - Specify the origin of the pinning position of the screen overlay, as well as the direction of the horizontal and vertical axes for that pinning position. The pinning origin specifies the origin of the pinning position in the overlay's coordinate system.

            * - :pyclass:`~SCREEN_OVERLAY_UNIT`
              - A unit specifying how a screen overlay is sized and positioned relative to its parent.

            * - :pyclass:`~SURFACE_MESH_RENDERING_METHOD`
              - Rendering methods available for use by the surface mesh primitive. Different methods may have different performance characteristics and require different video card support. When in doubt, use Automatic.

            * - :pyclass:`~VISIBILITY`
              - Result of a visibility test, such as testing if a sphere intersects a frustum.

            * - :pyclass:`~ANTI_ALIASING`
              - The multisample anti-aliasing (MSAA) options for Scenes. As the level of anti-aliasing increases, performance will generally decrease, but the quality of the anti-aliasing will improve.

            * - :pyclass:`~BINARY_LOGIC_OPERATION`
              - Binary logic operations that can be used by composite display condition.

            * - :pyclass:`~BLUR_METHOD`
              - The method used to blur or smooth a raster.

            * - :pyclass:`~EDGE_DETECT_METHOD`
              - The method used to detect edges in a raster.

            * - :pyclass:`~FLIP_AXIS`
              - The axis on which a raster will be flipped.

            * - :pyclass:`~GRADIENT_DETECT_METHOD`
              - The method used to detect gradients in a raster. Gradient detection is commonly referred to as embossing.

            * - :pyclass:`~JPEG2000_COMPRESSION_PROFILE`
              - Define the profile used when encoding a JPEG 2000 file.

            * - :pyclass:`~RASTER_BAND`
              - Common band types that may be contained within a raster dataset. Each band can be thought of as a set of values, which are most commonly associated with colors when the raster represents an image...

            * - :pyclass:`~RASTER_FORMAT`
              - Common raster band layouts that may be contained within a raster dataset. Each pixel of the raster will contain the bands defined by the layout in the specified order. A typical color raster image will have an rgbraster format.

            * - :pyclass:`~RASTER_ORIENTATION`
              - The vertical orientation of the raster.

            * - :pyclass:`~RASTER_TYPE`
              - The type of data contained within each band of a raster dataset.

            * - :pyclass:`~SHARPEN_METHOD`
              - The method used to sharpen a raster.

            * - :pyclass:`~VIDEO_PLAYBACK`
              - Specify how the video stream will playback. When the playback is set to real time, the video will playback in real time...

            * - :pyclass:`~KML_NETWORK_LINK_REFRESH_MODE`
              - Define the options available for a KmlNetworkLink's RefreshMode property.

            * - :pyclass:`~KML_NETWORK_LINK_VIEW_REFRESH_MODE`
              - Define the options available for a KmlNetworkLink's ViewRefreshMode property.

            * - :pyclass:`~MODEL_UP_AXIS`
              - When setting the camera'saxes, this defines which axis of the axes is up in screen space, where up is from the bottom to the top of the screen.

            * - :pyclass:`~OUTLINE_APPEARANCE`
              - Possible appearances of an outline. Front lines are lines on front facing geometry and back lines are lines on back facing geometry.

            * - :pyclass:`~POLYLINE_TYPE`
              - Describes how to interpret positions defining a polyline.

            * - :pyclass:`~CULL_FACE`
              - Identifies whether front- and/or back-facing triangles are culled.

            * - :pyclass:`~INTERNAL_TEXTURE_FORMAT`
              - The format of individual texels in a texture.

            * - :pyclass:`~MAGNIFICATION_FILTER`
              - The filter used when the pixel being textured maps to an area less than or equal to one texel.

            * - :pyclass:`~MINIFICATION_FILTER`
              - The filter used when the pixel being textured maps to an area greater than one texel.

            * - :pyclass:`~RENDERER_SHADE_MODEL`
              - Identifies which shade model to use. The primitive can be drawn with a single color or multiple colors.

            * - :pyclass:`~TEXTURE_WRAP`
              - Determine how to handle textures coordinates that fall outside of the range [0, 1].

            * - :pyclass:`~SET_HINT`
              - An optimization hint optionally provided to primitives to enhance performance for static or dynamic primitives. See the Set Hint Performance Overview for selecting an appropriate value.

            * - :pyclass:`~STEREO_PROJECTION_MODE`
              - The stereoscopic projection mode used for the left and right eye scenes.

            * - :pyclass:`~STEREOSCOPIC_DISPLAY_MODE`
              - The stereoscopic display mode. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :pyclass:`~FONT_STYLE`
              - Font styles.



Description
-----------

Access and manipulate visual elements in STK.

These include STK globe terrain
and imagery, camera control, 3D models, triangle meshes, surface polygons and
polylines, text batches, screen overlays, scene lighting, and raster and
projection streaming. STK Graphics is available in STK, using UI plugins, as
well as in STK Engine custom applications.

Detail
------

.. py:currentmodule:: ansys.stk.core.graphics


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> IPathPoint<IPathPoint>
    --> IPathPointFactory<IPathPointFactory>
    --> IBoundingSphere<IBoundingSphere>
    --> IBoundingSphereFactory<IBoundingSphereFactory>
    --> ITextureFilter2D<ITextureFilter2D>
    --> ITextureFilter2DFactory<ITextureFilter2DFactory>
    --> IRendererTexture2D<IRendererTexture2D>
    --> IRendererTextureTemplate2D<IRendererTextureTemplate2D>
    --> IPathPointCollection<IPathPointCollection>
    --> IObjectCollection<IObjectCollection>
    --> ISceneCollection<ISceneCollection>
    --> IScreenOverlayContainer<IScreenOverlayContainer>
    --> IScreenOverlayPickResultCollection<IScreenOverlayPickResultCollection>
    --> IGlobeImageOverlayAddCompleteEventArgs<IGlobeImageOverlayAddCompleteEventArgs>
    --> ITerrainOverlayAddCompleteEventArgs<ITerrainOverlayAddCompleteEventArgs>
    --> IPickResultCollection<IPickResultCollection>
    --> IRenderingEventArgs<IRenderingEventArgs>
    --> IBatchPrimitiveIndex<IBatchPrimitiveIndex>
    --> IKmlDocumentCollection<IKmlDocumentCollection>
    --> IKmlFeatureCollection<IKmlFeatureCollection>
    --> IKmlDocumentLoadedEventArgs<IKmlDocumentLoadedEventArgs>
    --> IFactoryAndInitializers<IFactoryAndInitializers>
    --> IExtrudedPolylineTriangulatorResult<IExtrudedPolylineTriangulatorResult>
    --> ISolidTriangulatorResult<ISolidTriangulatorResult>
    --> ISurfaceShapesResult<ISurfaceShapesResult>
    --> ISurfaceTriangulatorResult<ISurfaceTriangulatorResult>
    --> ITriangulatorResult<ITriangulatorResult>
    --> IAGICustomTerrainOverlay<IAGICustomTerrainOverlay>
    --> IAGIProcessedImageGlobeOverlay<IAGIProcessedImageGlobeOverlay>
    --> IAGIProcessedTerrainOverlay<IAGIProcessedTerrainOverlay>
    --> IAGIRoamImageGlobeOverlay<IAGIRoamImageGlobeOverlay>
    --> ICameraSnapshot<ICameraSnapshot>
    --> ICameraVideoRecording<ICameraVideoRecording>
    --> ICentralBodyGraphicsIndexer<ICentralBodyGraphicsIndexer>
    --> ICustomImageGlobeOverlay<ICustomImageGlobeOverlay>
    --> ICustomImageGlobeOverlayPluginActivator<ICustomImageGlobeOverlayPluginActivator>
    --> ICustomImageGlobeOverlayPluginProxy<ICustomImageGlobeOverlayPluginProxy>
    --> IGeospatialImageGlobeOverlay<IGeospatialImageGlobeOverlay>
    --> IGlobeOverlay<IGlobeOverlay>
    --> IGlobeOverlaySettings<IGlobeOverlaySettings>
    --> ILighting<ILighting>
    --> IPathPrimitiveUpdatePolicy<IPathPrimitiveUpdatePolicy>
    --> IProjectedRasterOverlay<IProjectedRasterOverlay>
    --> IProjection<IProjection>
    --> IProjectionStream<IProjectionStream>
    --> ISceneGlobeOverlaySettings<ISceneGlobeOverlaySettings>
    --> IScreenOverlayCollectionBase<IScreenOverlayCollectionBase>
    --> ITexture2DFactory<ITexture2DFactory>
    --> IVisualEffects<IVisualEffects>
    --> IAltitudeDisplayCondition<IAltitudeDisplayCondition>
    --> IAxesPrimitive<IAxesPrimitive>
    --> ICamera<ICamera>
    --> ICentralBodyGraphics<ICentralBodyGraphics>
    --> IClouds<IClouds>
    --> ICompositeDisplayCondition<ICompositeDisplayCondition>
    --> ICompositePrimitive<ICompositePrimitive>
    --> IConstantDisplayCondition<IConstantDisplayCondition>
    --> IDisplayCondition<IDisplayCondition>
    --> IDistanceDisplayCondition<IDistanceDisplayCondition>
    --> IDistanceToGlobeOverlayDisplayCondition<IDistanceToGlobeOverlayDisplayCondition>
    --> IDistanceToPositionDisplayCondition<IDistanceToPositionDisplayCondition>
    --> IDistanceToPrimitiveDisplayCondition<IDistanceToPrimitiveDisplayCondition>
    --> IDurationPathPrimitiveUpdatePolicy<IDurationPathPrimitiveUpdatePolicy>
    --> IFrameRate<IFrameRate>
    --> IGlobeImageOverlay<IGlobeImageOverlay>
    --> IGraphicsFont<IGraphicsFont>
    --> IGreatArcInterpolator<IGreatArcInterpolator>
    --> IImageCollection<IImageCollection>
    --> IAlphaFromLuminanceFilter<IAlphaFromLuminanceFilter>
    --> IAlphaFromPixelFilter<IAlphaFromPixelFilter>
    --> IAlphaFromRasterFilter<IAlphaFromRasterFilter>
    --> IBandExtractFilter<IBandExtractFilter>
    --> IBandOrderFilter<IBandOrderFilter>
    --> IBlurFilter<IBlurFilter>
    --> IBrightnessFilter<IBrightnessFilter>
    --> IColorToLuminanceFilter<IColorToLuminanceFilter>
    --> IContrastFilter<IContrastFilter>
    --> IConvolutionFilter<IConvolutionFilter>
    --> IEdgeDetectFilter<IEdgeDetectFilter>
    --> IFilteringRasterStream<IFilteringRasterStream>
    --> IFlipFilter<IFlipFilter>
    --> IGammaCorrectionFilter<IGammaCorrectionFilter>
    --> IGaussianBlurFilter<IGaussianBlurFilter>
    --> IGradientDetectFilter<IGradientDetectFilter>
    --> ILevelsFilter<ILevelsFilter>
    --> IProjectionRasterStreamPluginActivator<IProjectionRasterStreamPluginActivator>
    --> IProjectionRasterStreamPluginProxy<IProjectionRasterStreamPluginProxy>
    --> IRaster<IRaster>
    --> IRasterAttributes<IRasterAttributes>
    --> IRasterFilter<IRasterFilter>
    --> IRasterStream<IRasterStream>
    --> IRotateFilter<IRotateFilter>
    --> ISequenceFilter<ISequenceFilter>
    --> ISharpenFilter<ISharpenFilter>
    --> IVideoStream<IVideoStream>
    --> IKmlContainer<IKmlContainer>
    --> IKmlDocument<IKmlDocument>
    --> IKmlFeature<IKmlFeature>
    --> IKmlFolder<IKmlFolder>
    --> IKmlGraphics<IKmlGraphics>
    --> IKmlNetworkLink<IKmlNetworkLink>
    --> IMarkerBatchPrimitive<IMarkerBatchPrimitive>
    --> IMarkerBatchPrimitiveOptionalParameters<IMarkerBatchPrimitiveOptionalParameters>
    --> IMaximumCountPathPrimitiveUpdatePolicy<IMaximumCountPathPrimitiveUpdatePolicy>
    --> IModelArticulation<IModelArticulation>
    --> IModelArticulationCollection<IModelArticulationCollection>
    --> IModelPrimitive<IModelPrimitive>
    --> IModelTransformation<IModelTransformation>
    --> IOverlay<IOverlay>
    --> IPathPrimitive<IPathPrimitive>
    --> IPickResult<IPickResult>
    --> IPixelSizeDisplayCondition<IPixelSizeDisplayCondition>
    --> IPointBatchPrimitive<IPointBatchPrimitive>
    --> IPointBatchPrimitiveOptionalParameters<IPointBatchPrimitiveOptionalParameters>
    --> IPolylinePrimitive<IPolylinePrimitive>
    --> IPolylinePrimitiveOptionalParameters<IPolylinePrimitiveOptionalParameters>
    --> IPositionInterpolator<IPositionInterpolator>
    --> IPrimitive<IPrimitive>
    --> IPrimitiveManager<IPrimitiveManager>
    --> IRasterImageGlobeOverlay<IRasterImageGlobeOverlay>
    --> IRhumbLineInterpolator<IRhumbLineInterpolator>
    --> IScene<IScene>
    --> ISceneDisplayCondition<ISceneDisplayCondition>
    --> ISceneManager<ISceneManager>
    --> IScreenOverlay<IScreenOverlay>
    --> IScreenOverlayCollection<IScreenOverlayCollection>
    --> IScreenOverlayManager<IScreenOverlayManager>
    --> IScreenOverlayPickResult<IScreenOverlayPickResult>
    --> ISolidPrimitive<ISolidPrimitive>
    --> IStereoscopic<IStereoscopic>
    --> ISurfaceMeshPrimitive<ISurfaceMeshPrimitive>
    --> ITerrainOverlayCollection<ITerrainOverlayCollection>
    --> ITerrainOverlay<ITerrainOverlay>
    --> ITextBatchPrimitive<ITextBatchPrimitive>
    --> ITextBatchPrimitiveOptionalParameters<ITextBatchPrimitiveOptionalParameters>
    --> ITextOverlay<ITextOverlay>
    --> ITextureMatrix<ITextureMatrix>
    --> ITextureScreenOverlay<ITextureScreenOverlay>
    --> ITimeIntervalDisplayCondition<ITimeIntervalDisplayCondition>
    --> ITriangleMeshPrimitive<ITriangleMeshPrimitive>
    --> ITriangleMeshPrimitiveOptionalParameters<ITriangleMeshPrimitiveOptionalParameters>
    --> IVectorPrimitive<IVectorPrimitive>
    --> IBoxTriangulatorInitializer<IBoxTriangulatorInitializer>
    --> ICylinderTriangulatorInitializer<ICylinderTriangulatorInitializer>
    --> IEllipsoidTriangulatorInitializer<IEllipsoidTriangulatorInitializer>
    --> IExtrudedPolylineTriangulatorInitializer<IExtrudedPolylineTriangulatorInitializer>
    --> ISurfaceExtentTriangulatorInitializer<ISurfaceExtentTriangulatorInitializer>
    --> ISurfacePolygonTriangulatorInitializer<ISurfacePolygonTriangulatorInitializer>
    --> ISurfaceShapesInitializer<ISurfaceShapesInitializer>
    --> IAGICustomTerrainOverlayFactory<IAGICustomTerrainOverlayFactory>
    --> IAGIProcessedImageGlobeOverlayFactory<IAGIProcessedImageGlobeOverlayFactory>
    --> IAGIProcessedTerrainOverlayFactory<IAGIProcessedTerrainOverlayFactory>
    --> IAGIRoamImageGlobeOverlayFactory<IAGIRoamImageGlobeOverlayFactory>
    --> ICustomImageGlobeOverlayPluginActivatorFactory<ICustomImageGlobeOverlayPluginActivatorFactory>
    --> IGeospatialImageGlobeOverlayFactory<IGeospatialImageGlobeOverlayFactory>
    --> IProjectedRasterOverlayFactory<IProjectedRasterOverlayFactory>
    --> IProjectionFactory<IProjectionFactory>
    --> IAltitudeDisplayConditionFactory<IAltitudeDisplayConditionFactory>
    --> IAxesPrimitiveFactory<IAxesPrimitiveFactory>
    --> ICompositeDisplayConditionFactory<ICompositeDisplayConditionFactory>
    --> ICompositePrimitiveFactory<ICompositePrimitiveFactory>
    --> IConstantDisplayConditionFactory<IConstantDisplayConditionFactory>
    --> IDistanceDisplayConditionFactory<IDistanceDisplayConditionFactory>
    --> IDistanceToGlobeOverlayDisplayConditionFactory<IDistanceToGlobeOverlayDisplayConditionFactory>
    --> IDistanceToPositionDisplayConditionFactory<IDistanceToPositionDisplayConditionFactory>
    --> IDistanceToPrimitiveDisplayConditionFactory<IDistanceToPrimitiveDisplayConditionFactory>
    --> IDurationPathPrimitiveUpdatePolicyFactory<IDurationPathPrimitiveUpdatePolicyFactory>
    --> IGlobeImageOverlayInitializer<IGlobeImageOverlayInitializer>
    --> IGraphicsFontFactory<IGraphicsFontFactory>
    --> IGreatArcInterpolatorFactory<IGreatArcInterpolatorFactory>
    --> IAlphaFromLuminanceFilterFactory<IAlphaFromLuminanceFilterFactory>
    --> IAlphaFromPixelFilterFactory<IAlphaFromPixelFilterFactory>
    --> IAlphaFromRasterFilterFactory<IAlphaFromRasterFilterFactory>
    --> IBandExtractFilterFactory<IBandExtractFilterFactory>
    --> IBandOrderFilterFactory<IBandOrderFilterFactory>
    --> IBlurFilterFactory<IBlurFilterFactory>
    --> IBrightnessFilterFactory<IBrightnessFilterFactory>
    --> IColorToLuminanceFilterFactory<IColorToLuminanceFilterFactory>
    --> IContrastFilterFactory<IContrastFilterFactory>
    --> IConvolutionFilterFactory<IConvolutionFilterFactory>
    --> IEdgeDetectFilterFactory<IEdgeDetectFilterFactory>
    --> IFilteringRasterStreamFactory<IFilteringRasterStreamFactory>
    --> IFlipFilterFactory<IFlipFilterFactory>
    --> IGammaCorrectionFilterFactory<IGammaCorrectionFilterFactory>
    --> IGaussianBlurFilterFactory<IGaussianBlurFilterFactory>
    --> IGradientDetectFilterFactory<IGradientDetectFilterFactory>
    --> IJpeg2000WriterInitializer<IJpeg2000WriterInitializer>
    --> ILevelsFilterFactory<ILevelsFilterFactory>
    --> IProjectionRasterStreamPluginActivatorFactory<IProjectionRasterStreamPluginActivatorFactory>
    --> IRasterFactory<IRasterFactory>
    --> IRasterAttributesFactory<IRasterAttributesFactory>
    --> IRotateFilterFactory<IRotateFilterFactory>
    --> ISequenceFilterFactory<ISequenceFilterFactory>
    --> ISharpenFilterFactory<ISharpenFilterFactory>
    --> IVideoStreamFactory<IVideoStreamFactory>
    --> IMarkerBatchPrimitiveFactory<IMarkerBatchPrimitiveFactory>
    --> IMarkerBatchPrimitiveOptionalParametersFactory<IMarkerBatchPrimitiveOptionalParametersFactory>
    --> IMaximumCountPathPrimitiveUpdatePolicyFactory<IMaximumCountPathPrimitiveUpdatePolicyFactory>
    --> IModelPrimitiveFactory<IModelPrimitiveFactory>
    --> IPathPrimitiveFactory<IPathPrimitiveFactory>
    --> IPixelSizeDisplayConditionFactory<IPixelSizeDisplayConditionFactory>
    --> IPointBatchPrimitiveFactory<IPointBatchPrimitiveFactory>
    --> IPointBatchPrimitiveOptionalParametersFactory<IPointBatchPrimitiveOptionalParametersFactory>
    --> IPolylinePrimitiveFactory<IPolylinePrimitiveFactory>
    --> IPolylinePrimitiveOptionalParametersFactory<IPolylinePrimitiveOptionalParametersFactory>
    --> IRasterImageGlobeOverlayFactory<IRasterImageGlobeOverlayFactory>
    --> IRhumbLineInterpolatorFactory<IRhumbLineInterpolatorFactory>
    --> ISceneDisplayConditionFactory<ISceneDisplayConditionFactory>
    --> ISceneManagerInitializer<ISceneManagerInitializer>
    --> IScreenOverlayFactory<IScreenOverlayFactory>
    --> ISolidPrimitiveFactory<ISolidPrimitiveFactory>
    --> ISurfaceMeshPrimitiveFactory<ISurfaceMeshPrimitiveFactory>
    --> ITerrainOverlayInitializer<ITerrainOverlayInitializer>
    --> ITextBatchPrimitiveFactory<ITextBatchPrimitiveFactory>
    --> ITextBatchPrimitiveOptionalParametersFactory<ITextBatchPrimitiveOptionalParametersFactory>
    --> ITextOverlayFactory<ITextOverlayFactory>
    --> ITextureMatrixFactory<ITextureMatrixFactory>
    --> ITextureScreenOverlayFactory<ITextureScreenOverlayFactory>
    --> ITimeIntervalDisplayConditionFactory<ITimeIntervalDisplayConditionFactory>
    --> ITriangleMeshPrimitiveFactory<ITriangleMeshPrimitiveFactory>
    --> ITriangleMeshPrimitiveOptionalParametersFactory<ITriangleMeshPrimitiveOptionalParametersFactory>
    --> IVectorPrimitiveFactory<IVectorPrimitiveFactory>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    --> PathPoint<>
    --> PathPointFactory<>
    --> BoundingSphere<>
    --> BoundingSphereFactory<>
    --> TextureFilter2D<>
    --> TextureFilter2DFactory<>
    --> RendererTexture2D<>
    --> RendererTextureTemplate2D<>
    --> PathPointCollection<>
    --> ObjectCollection<>
    --> SceneCollection<>
    --> ScreenOverlayPickResultCollection<>
    --> GlobeImageOverlayAddCompleteEventArgs<>
    --> TerrainOverlayAddCompleteEventArgs<>
    --> PickResultCollection<>
    --> RenderingEventArgs<>
    --> BatchPrimitiveIndex<>
    --> KmlDocumentCollection<>
    --> KmlFeatureCollection<>
    --> KmlDocumentLoadedEventArgs<>
    --> FactoryAndInitializers<>
    --> ExtrudedPolylineTriangulatorResult<>
    --> SolidTriangulatorResult<>
    --> SurfaceShapesResult<>
    --> SurfaceTriangulatorResult<>
    --> TriangulatorResult<>
    --> AGICustomTerrainOverlay<>
    --> AGIProcessedImageGlobeOverlay<>
    --> AGIProcessedTerrainOverlay<>
    --> AGIRoamImageGlobeOverlay<>
    --> CameraSnapshot<>
    --> CameraVideoRecording<>
    --> CentralBodyGraphicsIndexer<>
    --> CustomImageGlobeOverlay<>
    --> CustomImageGlobeOverlayPluginActivator<>
    --> CustomImageGlobeOverlayPluginProxy<>
    --> GeospatialImageGlobeOverlay<>
    --> GlobeOverlay<>
    --> GlobeOverlaySettings<>
    --> Lighting<>
    --> PathPrimitiveUpdatePolicy<>
    --> ProjectedRasterOverlay<>
    --> Projection<>
    --> ProjectionStream<>
    --> SceneGlobeOverlaySettings<>
    --> ScreenOverlayCollectionBase<>
    --> Texture2DFactory<>
    --> VisualEffects<>
    --> AltitudeDisplayCondition<>
    --> AxesPrimitive<>
    --> Camera<>
    --> CentralBodyGraphics<>
    --> Clouds<>
    --> CompositeDisplayCondition<>
    --> CompositePrimitive<>
    --> ConstantDisplayCondition<>
    --> DisplayCondition<>
    --> DistanceDisplayCondition<>
    --> DistanceToGlobeOverlayDisplayCondition<>
    --> DistanceToPositionDisplayCondition<>
    --> DistanceToPrimitiveDisplayCondition<>
    --> DurationPathPrimitiveUpdatePolicy<>
    --> FrameRate<>
    --> GlobeImageOverlay<>
    --> GraphicsFont<>
    --> GreatArcInterpolator<>
    --> ImageCollection<>
    --> AlphaFromLuminanceFilter<>
    --> AlphaFromPixelFilter<>
    --> AlphaFromRasterFilter<>
    --> BandExtractFilter<>
    --> BandOrderFilter<>
    --> BlurFilter<>
    --> BrightnessFilter<>
    --> ColorToLuminanceFilter<>
    --> ContrastFilter<>
    --> ConvolutionFilter<>
    --> EdgeDetectFilter<>
    --> FilteringRasterStream<>
    --> FlipFilter<>
    --> GammaCorrectionFilter<>
    --> GaussianBlurFilter<>
    --> GradientDetectFilter<>
    --> LevelsFilter<>
    --> ProjectionRasterStreamPluginActivator<>
    --> ProjectionRasterStreamPluginProxy<>
    --> Raster<>
    --> RasterAttributes<>
    --> RasterFilter<>
    --> RasterStream<>
    --> RotateFilter<>
    --> SequenceFilter<>
    --> SharpenFilter<>
    --> VideoStream<>
    --> KmlContainer<>
    --> KmlDocument<>
    --> KmlFeature<>
    --> KmlFolder<>
    --> KmlGraphics<>
    --> KmlNetworkLink<>
    --> MarkerBatchPrimitive<>
    --> MarkerBatchPrimitiveOptionalParameters<>
    --> MaximumCountPathPrimitiveUpdatePolicy<>
    --> ModelArticulation<>
    --> ModelArticulationCollection<>
    --> ModelPrimitive<>
    --> ModelTransformation<>
    --> Overlay<>
    --> PathPrimitive<>
    --> PickResult<>
    --> PixelSizeDisplayCondition<>
    --> PointBatchPrimitive<>
    --> PointBatchPrimitiveOptionalParameters<>
    --> PolylinePrimitive<>
    --> PolylinePrimitiveOptionalParameters<>
    --> PositionInterpolator<>
    --> Primitive<>
    --> PrimitiveManager<>
    --> RasterImageGlobeOverlay<>
    --> RhumbLineInterpolator<>
    --> Scene<>
    --> SceneDisplayCondition<>
    --> SceneManager<>
    --> ScreenOverlay<>
    --> ScreenOverlayCollection<>
    --> ScreenOverlayManager<>
    --> ScreenOverlayPickResult<>
    --> SolidPrimitive<>
    --> Stereoscopic<>
    --> SurfaceMeshPrimitive<>
    --> TerrainOverlayCollection<>
    --> TerrainOverlay<>
    --> TextBatchPrimitive<>
    --> TextBatchPrimitiveOptionalParameters<>
    --> TextOverlay<>
    --> TextureMatrix<>
    --> TextureScreenOverlay<>
    --> TimeIntervalDisplayCondition<>
    --> TriangleMeshPrimitive<>
    --> TriangleMeshPrimitiveOptionalParameters<>
    --> VectorPrimitive<>
    --> BoxTriangulatorInitializer<>
    --> CylinderTriangulatorInitializer<>
    --> EllipsoidTriangulatorInitializer<>
    --> ExtrudedPolylineTriangulatorInitializer<>
    --> SurfaceExtentTriangulatorInitializer<>
    --> SurfacePolygonTriangulatorInitializer<>
    --> SurfaceShapesInitializer<>
    --> AGICustomTerrainOverlayFactory<>
    --> AGIProcessedImageGlobeOverlayFactory<>
    --> AGIProcessedTerrainOverlayFactory<>
    --> AGIRoamImageGlobeOverlayFactory<>
    --> CustomImageGlobeOverlayPluginActivatorFactory<>
    --> GeospatialImageGlobeOverlayFactory<>
    --> ProjectedRasterOverlayFactory<>
    --> ProjectionFactory<>
    --> AltitudeDisplayConditionFactory<>
    --> AxesPrimitiveFactory<>
    --> CompositeDisplayConditionFactory<>
    --> CompositePrimitiveFactory<>
    --> ConstantDisplayConditionFactory<>
    --> DistanceDisplayConditionFactory<>
    --> DistanceToGlobeOverlayDisplayConditionFactory<>
    --> DistanceToPositionDisplayConditionFactory<>
    --> DistanceToPrimitiveDisplayConditionFactory<>
    --> DurationPathPrimitiveUpdatePolicyFactory<>
    --> GlobeImageOverlayInitializer<>
    --> GraphicsFontFactory<>
    --> GreatArcInterpolatorFactory<>
    --> AlphaFromLuminanceFilterFactory<>
    --> AlphaFromPixelFilterFactory<>
    --> AlphaFromRasterFilterFactory<>
    --> BandExtractFilterFactory<>
    --> BandOrderFilterFactory<>
    --> BlurFilterFactory<>
    --> BrightnessFilterFactory<>
    --> ColorToLuminanceFilterFactory<>
    --> ContrastFilterFactory<>
    --> ConvolutionFilterFactory<>
    --> EdgeDetectFilterFactory<>
    --> FilteringRasterStreamFactory<>
    --> FlipFilterFactory<>
    --> GammaCorrectionFilterFactory<>
    --> GaussianBlurFilterFactory<>
    --> GradientDetectFilterFactory<>
    --> Jpeg2000WriterInitializer<>
    --> LevelsFilterFactory<>
    --> ProjectionRasterStreamPluginActivatorFactory<>
    --> RasterFactory<>
    --> RasterAttributesFactory<>
    --> RotateFilterFactory<>
    --> SequenceFilterFactory<>
    --> SharpenFilterFactory<>
    --> VideoStreamFactory<>
    --> MarkerBatchPrimitiveFactory<>
    --> MarkerBatchPrimitiveOptionalParametersFactory<>
    --> MaximumCountPathPrimitiveUpdatePolicyFactory<>
    --> ModelPrimitiveFactory<>
    --> PathPrimitiveFactory<>
    --> PixelSizeDisplayConditionFactory<>
    --> PointBatchPrimitiveFactory<>
    --> PointBatchPrimitiveOptionalParametersFactory<>
    --> PolylinePrimitiveFactory<>
    --> PolylinePrimitiveOptionalParametersFactory<>
    --> RasterImageGlobeOverlayFactory<>
    --> RhumbLineInterpolatorFactory<>
    --> SceneDisplayConditionFactory<>
    --> SceneManagerInitializer<>
    --> ScreenOverlayFactory<>
    --> SolidPrimitiveFactory<>
    --> SurfaceMeshPrimitiveFactory<>
    --> TerrainOverlayInitializer<>
    --> TextBatchPrimitiveFactory<>
    --> TextBatchPrimitiveOptionalParametersFactory<>
    --> TextOverlayFactory<>
    --> TextureMatrixFactory<>
    --> TextureScreenOverlayFactory<>
    --> TimeIntervalDisplayConditionFactory<>
    --> TriangleMeshPrimitiveFactory<>
    --> TriangleMeshPrimitiveOptionalParametersFactory<>
    --> VectorPrimitiveFactory<>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CYLINDER_FILL<CYLINDER_FILL>
    ≔ WINDING_ORDER<WINDING_ORDER>
    ≔ CAMERA_SNAPSHOT_FILE_FORMAT<CAMERA_SNAPSHOT_FILE_FORMAT>
    ≔ CAMERA_VIDEO_FORMAT<CAMERA_VIDEO_FORMAT>
    ≔ CONSTRAINED_UP_AXIS<CONSTRAINED_UP_AXIS>
    ≔ GLOBE_OVERLAY_ROLE<GLOBE_OVERLAY_ROLE>
    ≔ INDICES_ORDER_HINT<INDICES_ORDER_HINT>
    ≔ MAINTAIN_ASPECT_RATIO<MAINTAIN_ASPECT_RATIO>
    ≔ MAP_PROJECTION<MAP_PROJECTION>
    ≔ MARKER_BATCH_RENDERING_METHOD<MARKER_BATCH_RENDERING_METHOD>
    ≔ MARKER_BATCH_RENDER_PASS<MARKER_BATCH_RENDER_PASS>
    ≔ MARKER_BATCH_SIZE_SOURCE<MARKER_BATCH_SIZE_SOURCE>
    ≔ MARKER_BATCH_SORT_ORDER<MARKER_BATCH_SORT_ORDER>
    ≔ MARKER_BATCH_UNIT<MARKER_BATCH_UNIT>
    ≔ MODEL_TRANSFORMATION_TYPE<MODEL_TRANSFORMATION_TYPE>
    ≔ ORIGIN<ORIGIN>
    ≔ PATH_PRIMITIVE_REMOVE_LOCATION<PATH_PRIMITIVE_REMOVE_LOCATION>
    ≔ PRIMITIVES_SORT_ORDER<PRIMITIVES_SORT_ORDER>
    ≔ REFRESH_RATE<REFRESH_RATE>
    ≔ RENDER_PASS<RENDER_PASS>
    ≔ RENDER_PASS_HINT<RENDER_PASS_HINT>
    ≔ SCREEN_OVERLAY_ORIGIN<SCREEN_OVERLAY_ORIGIN>
    ≔ SCREEN_OVERLAY_PINNING_ORIGIN<SCREEN_OVERLAY_PINNING_ORIGIN>
    ≔ SCREEN_OVERLAY_UNIT<SCREEN_OVERLAY_UNIT>
    ≔ SURFACE_MESH_RENDERING_METHOD<SURFACE_MESH_RENDERING_METHOD>
    ≔ VISIBILITY<VISIBILITY>
    ≔ ANTI_ALIASING<ANTI_ALIASING>
    ≔ BINARY_LOGIC_OPERATION<BINARY_LOGIC_OPERATION>
    ≔ BLUR_METHOD<BLUR_METHOD>
    ≔ EDGE_DETECT_METHOD<EDGE_DETECT_METHOD>
    ≔ FLIP_AXIS<FLIP_AXIS>
    ≔ GRADIENT_DETECT_METHOD<GRADIENT_DETECT_METHOD>
    ≔ JPEG2000_COMPRESSION_PROFILE<JPEG2000_COMPRESSION_PROFILE>
    ≔ RASTER_BAND<RASTER_BAND>
    ≔ RASTER_FORMAT<RASTER_FORMAT>
    ≔ RASTER_ORIENTATION<RASTER_ORIENTATION>
    ≔ RASTER_TYPE<RASTER_TYPE>
    ≔ SHARPEN_METHOD<SHARPEN_METHOD>
    ≔ VIDEO_PLAYBACK<VIDEO_PLAYBACK>
    ≔ KML_NETWORK_LINK_REFRESH_MODE<KML_NETWORK_LINK_REFRESH_MODE>
    ≔ KML_NETWORK_LINK_VIEW_REFRESH_MODE<KML_NETWORK_LINK_VIEW_REFRESH_MODE>
    ≔ MODEL_UP_AXIS<MODEL_UP_AXIS>
    ≔ OUTLINE_APPEARANCE<OUTLINE_APPEARANCE>
    ≔ POLYLINE_TYPE<POLYLINE_TYPE>
    ≔ CULL_FACE<CULL_FACE>
    ≔ INTERNAL_TEXTURE_FORMAT<INTERNAL_TEXTURE_FORMAT>
    ≔ MAGNIFICATION_FILTER<MAGNIFICATION_FILTER>
    ≔ MINIFICATION_FILTER<MINIFICATION_FILTER>
    ≔ RENDERER_SHADE_MODEL<RENDERER_SHADE_MODEL>
    ≔ TEXTURE_WRAP<TEXTURE_WRAP>
    ≔ SET_HINT<SET_HINT>
    ≔ STEREO_PROJECTION_MODE<STEREO_PROJECTION_MODE>
    ≔ STEREOSCOPIC_DISPLAY_MODE<STEREOSCOPIC_DISPLAY_MODE>
    ≔ FONT_STYLE<FONT_STYLE>

