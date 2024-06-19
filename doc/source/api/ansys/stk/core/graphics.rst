
The ``graphics`` module
=======================


.. py:module:: ansys.stk.core.graphics


Summary
-------

.. tab-set::

 
    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~IPathPoint`
              - A path point used with the Path Primitive.

            * - :py:class:`~IPathPointFactory`
              - Create Path Primitive's path points.

            * - :py:class:`~IBoundingSphere`
              - A sphere that encapsulates an object.

            * - :py:class:`~IBoundingSphereFactory`
              - Create instances of the bounding sphere type.

            * - :py:class:`~ITextureFilter2D`
              - A texture filter.

            * - :py:class:`~ITextureFilter2DFactory`
              - Create texture filters.

            * - :py:class:`~IRendererTexture2D`
              - A 2D Texture. A texture represents an image that is ready for use by objects such as primitives and overlays. Textures typically reside in video memory.

            * - :py:class:`~IRendererTextureTemplate2D`
              - Template object containing attributes required to create a 2D texture.

            * - :py:class:`~IPathPointCollection`
              - A collection of path points.

            * - :py:class:`~IObjectCollection`
              - A collection of objects.

            * - :py:class:`~ISceneCollection`
              - A collection of scenes.

            * - :py:class:`~IScreenOverlayContainer`
              - The interface for screen overlays that contain a collection of other overlays. This interface is implemented by ScreenOverlayManager and ScreenOverlay.

            * - :py:class:`~IScreenOverlayPickResultCollection`
              - A collection of pick results.

            * - :py:class:`~IGlobeImageOverlayAddCompleteEventArgs`
              - The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

            * - :py:class:`~ITerrainOverlayAddCompleteEventArgs`
              - The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

            * - :py:class:`~IPickResultCollection`
              - A collection of picked objects.

            * - :py:class:`~IRenderingEventArgs`
              - The event is raised when the scene is rendered.

            * - :py:class:`~IBatchPrimitiveIndex`
              - Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

            * - :py:class:`~IKmlDocumentCollection`
              - A collection of KML documents.

            * - :py:class:`~IKmlFeatureCollection`
              - A collection of KML features.

            * - :py:class:`~IKmlDocumentLoadedEventArgs`
              - The event is raised when a KML document has been loaded.

            * - :py:class:`~IFactoryAndInitializers`
              - Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

            * - :py:class:`~IExtrudedPolylineTriangulatorResult`
              - The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~ISolidTriangulatorResult`
              - The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

            * - :py:class:`~ISurfaceShapesResult`
              - Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

            * - :py:class:`~ISurfaceTriangulatorResult`
              - The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

            * - :py:class:`~ITriangulatorResult`
              - The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

            * - :py:class:`~IAGICustomTerrainOverlay`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~IAGIProcessedImageGlobeOverlay`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~IAGIProcessedTerrainOverlay`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~IAGIRoamImageGlobeOverlay`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~ICameraSnapshot`
              - Takes snapshots of the 3D window.

            * - :py:class:`~ICameraVideoRecording`
              - Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

            * - :py:class:`~ICentralBodyGraphicsIndexer`
              - An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

            * - :py:class:`~ICustomImageGlobeOverlay`
              - A globe image overlay that allows for a user defined image to be specified.

            * - :py:class:`~ICustomImageGlobeOverlayPluginActivator`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~ICustomImageGlobeOverlayPluginProxy`
              - A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

            * - :py:class:`~IGeospatialImageGlobeOverlay`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~IGlobeOverlay`
              - The base class of all terrain overlay and globe image overlay objects.

            * - :py:class:`~IGlobeOverlaySettings`
              - Settings used by globe overlay objects. These setting affect all scenes.

            * - :py:class:`~ILighting`
              - Lighting in the 3D scene.

            * - :py:class:`~IPathPrimitiveUpdatePolicy`
              - A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

            * - :py:class:`~IProjectedRasterOverlay`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~IProjection`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~IProjectionStream`
              - A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

            * - :py:class:`~ISceneGlobeOverlaySettings`
              - Settings used by globe overlay objects. These settings only affect the scene.

            * - :py:class:`~IScreenOverlayCollectionBase`
              - The common base class for collections of overlays held by screen overlay and by screen overlay manager.

            * - :py:class:`~ITexture2DFactory`
              - A factory for creating texture 2d objects from various sources.

            * - :py:class:`~IVisualEffects`
              - Control various post processing effects that can be applied to the scene.

            * - :py:class:`~IAltitudeDisplayCondition`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~IAxesPrimitive`
              - Render an axes in the 3D scene.

            * - :py:class:`~ICamera`
              - Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

            * - :py:class:`~ICentralBodyGraphics`
              - The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

            * - :py:class:`~IClouds`
              - Load, show and hide clouds in the scene.

            * - :py:class:`~ICompositeDisplayCondition`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~ICompositePrimitive`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~IConstantDisplayCondition`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~IDisplayCondition`
              - When assigned to objects, such as primitives or globe overlays, display conditions are evaluated to determine if the object should be rendered.

            * - :py:class:`~IDistanceDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~IDistanceToGlobeOverlayDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~IDistanceToPositionDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~IDistanceToPrimitiveDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~IDurationPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~IFrameRate`
              - Keeps track of how many times the scenes are rendered per second.

            * - :py:class:`~IGlobeImageOverlay`
              - A globe overlay that shows an image.

            * - :py:class:`~IGraphicsFont`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~IGreatArcInterpolator`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~IImageCollection`
              - A collection of globe image overlay objects.

            * - :py:class:`~IAlphaFromLuminanceFilter`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~IAlphaFromPixelFilter`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~IAlphaFromRasterFilter`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~IBandExtractFilter`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~IBandOrderFilter`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~IBlurFilter`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~IBrightnessFilter`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~IColorToLuminanceFilter`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~IContrastFilter`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~IConvolutionFilter`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~IEdgeDetectFilter`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~IFilteringRasterStream`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~IFlipFilter`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~IGammaCorrectionFilter`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~IGaussianBlurFilter`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~IGradientDetectFilter`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~ILevelsFilter`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~IProjectionRasterStreamPluginActivator`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~IProjectionRasterStreamPluginProxy`
              - A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

            * - :py:class:`~IRaster`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~IRasterAttributes`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~IRasterFilter`
              - A filter for processing raster datasets. RasterFilter is the base class for all raster filters...

            * - :py:class:`~IRasterStream`
              - A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

            * - :py:class:`~IRotateFilter`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~ISequenceFilter`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~ISharpenFilter`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~IVideoStream`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~IKmlContainer`
              - A KmlContainer contains a collection of children kml features.

            * - :py:class:`~IKmlDocument`
              - A KML document.

            * - :py:class:`~IKmlFeature`
              - A KML feature.

            * - :py:class:`~IKmlFolder`
              - A KML folder.

            * - :py:class:`~IKmlGraphics`
              - Provide loading and unloading of kml documents for a particular central body.

            * - :py:class:`~IKmlNetworkLink`
              - A KML network link.

            * - :py:class:`~IMarkerBatchPrimitive`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~IMarkerBatchPrimitiveOptionalParameters`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~IMaximumCountPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~IModelArticulation`
              - A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~IModelArticulationCollection`
              - A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~IModelPrimitive`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~IModelTransformation`
              - A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

            * - :py:class:`~IOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~IPathPrimitive`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~IPickResult`
              - A single result from Pick.

            * - :py:class:`~IPixelSizeDisplayCondition`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~IPointBatchPrimitive`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~IPointBatchPrimitiveOptionalParameters`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~IPolylinePrimitive`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~IPolylinePrimitiveOptionalParameters`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~IPositionInterpolator`
              - Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

            * - :py:class:`~IPrimitive`
              - Primitives represent objects rendered in the 3D scene.

            * - :py:class:`~IPrimitiveManager`
              - The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

            * - :py:class:`~IRasterImageGlobeOverlay`
              - A globe image overlay for handling rasters.

            * - :py:class:`~IRhumbLineInterpolator`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~IScene`
              - A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

            * - :py:class:`~ISceneDisplayCondition`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~ISceneManager`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~IScreenOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~IScreenOverlayCollection`
              - A collection of screen overlays.

            * - :py:class:`~IScreenOverlayManager`
              - The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

            * - :py:class:`~IScreenOverlayPickResult`
              - Describes a picked screen overlay as a result of a call to pick screen overlays.

            * - :py:class:`~ISolidPrimitive`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~IStereoscopic`
              - Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :py:class:`~ISurfaceMeshPrimitive`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~ITerrainOverlayCollection`
              - A collection of terrain overlay objects.

            * - :py:class:`~ITerrainOverlay`
              - A globe overlay which shows terrain.

            * - :py:class:`~ITextBatchPrimitive`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~ITextBatchPrimitiveOptionalParameters`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~ITextOverlay`
              - A rectangular overlay that contains text.

            * - :py:class:`~ITextureMatrix`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~ITextureScreenOverlay`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~ITimeIntervalDisplayCondition`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~ITriangleMeshPrimitive`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~ITriangleMeshPrimitiveOptionalParameters`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~IVectorPrimitive`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

            * - :py:class:`~IBoxTriangulatorInitializer`
              - Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ICylinderTriangulatorInitializer`
              - Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~IEllipsoidTriangulatorInitializer`
              - Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~IExtrudedPolylineTriangulatorInitializer`
              - Triangulates a polyline into an extrusion with bottom and top boundaries.

            * - :py:class:`~ISurfaceExtentTriangulatorInitializer`
              - Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

            * - :py:class:`~ISurfacePolygonTriangulatorInitializer`
              - Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~ISurfaceShapesInitializer`
              - Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

            * - :py:class:`~IAGICustomTerrainOverlayFactory`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~IAGIProcessedImageGlobeOverlayFactory`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~IAGIProcessedTerrainOverlayFactory`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~IAGIRoamImageGlobeOverlayFactory`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~ICustomImageGlobeOverlayPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~IGeospatialImageGlobeOverlayFactory`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~IProjectedRasterOverlayFactory`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~IProjectionFactory`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~IAltitudeDisplayConditionFactory`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~IAxesPrimitiveFactory`
              - Render an axes in the 3D scene.

            * - :py:class:`~ICompositeDisplayConditionFactory`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~ICompositePrimitiveFactory`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~IConstantDisplayConditionFactory`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~IDistanceDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~IDistanceToGlobeOverlayDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~IDistanceToPositionDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~IDistanceToPrimitiveDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~IDurationPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~IGlobeImageOverlayInitializer`
              - A globe overlay that shows an image.

            * - :py:class:`~IGraphicsFontFactory`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~IGreatArcInterpolatorFactory`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~IAlphaFromLuminanceFilterFactory`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~IAlphaFromPixelFilterFactory`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~IAlphaFromRasterFilterFactory`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~IBandExtractFilterFactory`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~IBandOrderFilterFactory`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~IBlurFilterFactory`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~IBrightnessFilterFactory`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~IColorToLuminanceFilterFactory`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~IContrastFilterFactory`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~IConvolutionFilterFactory`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~IEdgeDetectFilterFactory`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~IFilteringRasterStreamFactory`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~IFlipFilterFactory`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~IGammaCorrectionFilterFactory`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~IGaussianBlurFilterFactory`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~IGradientDetectFilterFactory`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~IJpeg2000WriterInitializer`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

            * - :py:class:`~ILevelsFilterFactory`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~IProjectionRasterStreamPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~IRasterFactory`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~IRasterAttributesFactory`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~IRotateFilterFactory`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~ISequenceFilterFactory`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~ISharpenFilterFactory`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~IVideoStreamFactory`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~IMarkerBatchPrimitiveFactory`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~IMarkerBatchPrimitiveOptionalParametersFactory`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~IMaximumCountPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~IModelPrimitiveFactory`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~IPathPrimitiveFactory`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~IPixelSizeDisplayConditionFactory`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~IPointBatchPrimitiveFactory`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~IPointBatchPrimitiveOptionalParametersFactory`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~IPolylinePrimitiveFactory`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~IPolylinePrimitiveOptionalParametersFactory`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~IRasterImageGlobeOverlayFactory`
              - A globe image overlay for handling rasters.

            * - :py:class:`~IRhumbLineInterpolatorFactory`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~ISceneDisplayConditionFactory`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~ISceneManagerInitializer`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~IScreenOverlayFactory`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ISolidPrimitiveFactory`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~ISurfaceMeshPrimitiveFactory`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~ITerrainOverlayInitializer`
              - A globe overlay which shows terrain.

            * - :py:class:`~ITextBatchPrimitiveFactory`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~ITextBatchPrimitiveOptionalParametersFactory`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~ITextOverlayFactory`
              - A rectangular overlay that contains text.

            * - :py:class:`~ITextureMatrixFactory`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~ITextureScreenOverlayFactory`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~ITimeIntervalDisplayConditionFactory`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~ITriangleMeshPrimitiveFactory`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~ITriangleMeshPrimitiveOptionalParametersFactory`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~IVectorPrimitiveFactory`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~PathPoint`
              - Represents a path point used in conjunction with the Path Primitive.

            * - :py:class:`~PathPointFactory`
              - Factory creates path points.

            * - :py:class:`~BoundingSphere`
              - A sphere that encapsulates an object.

            * - :py:class:`~BoundingSphereFactory`
              - Create bounding spheres.

            * - :py:class:`~TextureFilter2D`
              - A texture filter.

            * - :py:class:`~TextureFilter2DFactory`
              - Create texture filters.

            * - :py:class:`~RendererTexture2D`
              - A 2D Texture. A texture represents an image that is ready for use by objects such as primitives and overlays. Textures typically reside in video memory.

            * - :py:class:`~RendererTextureTemplate2D`
              - Template object containing attributes required to create a 2D texture.

            * - :py:class:`~PathPointCollection`
              - A collection of path points.

            * - :py:class:`~ObjectCollection`
              - A collection of objects.

            * - :py:class:`~SceneCollection`
              - A collection of scenes.

            * - :py:class:`~ScreenOverlayPickResultCollection`
              - A collection of pick results.

            * - :py:class:`~GlobeImageOverlayAddCompleteEventArgs`
              - The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

            * - :py:class:`~TerrainOverlayAddCompleteEventArgs`
              - The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

            * - :py:class:`~PickResultCollection`
              - A collection of picked objects.

            * - :py:class:`~RenderingEventArgs`
              - The event is raised when the scene is rendered.

            * - :py:class:`~BatchPrimitiveIndex`
              - Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

            * - :py:class:`~KmlDocumentCollection`
              - A collection of KML documents.

            * - :py:class:`~KmlFeatureCollection`
              - A collection of KML features.

            * - :py:class:`~KmlDocumentLoadedEventArgs`
              - The event is raised when a KML document has been loaded.

            * - :py:class:`~FactoryAndInitializers`
              - Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

            * - :py:class:`~ExtrudedPolylineTriangulatorResult`
              - The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~SolidTriangulatorResult`
              - The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

            * - :py:class:`~SurfaceShapesResult`
              - Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

            * - :py:class:`~SurfaceTriangulatorResult`
              - The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

            * - :py:class:`~TriangulatorResult`
              - The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

            * - :py:class:`~AGICustomTerrainOverlay`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~AGIProcessedImageGlobeOverlay`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~AGIProcessedTerrainOverlay`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~AGIRoamImageGlobeOverlay`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~CameraSnapshot`
              - Takes snapshots of the 3D window.

            * - :py:class:`~CameraVideoRecording`
              - Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

            * - :py:class:`~CentralBodyGraphicsIndexer`
              - An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

            * - :py:class:`~CustomImageGlobeOverlay`
              - A globe image overlay that allows for a user defined image to be specified.

            * - :py:class:`~CustomImageGlobeOverlayPluginActivator`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~CustomImageGlobeOverlayPluginProxy`
              - A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

            * - :py:class:`~GeospatialImageGlobeOverlay`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~GlobeOverlay`
              - The base class of all terrain overlay and globe image overlay objects.

            * - :py:class:`~GlobeOverlaySettings`
              - Settings used by globe overlay objects. These setting affect all scenes.

            * - :py:class:`~Lighting`
              - Lighting in the 3D scene.

            * - :py:class:`~PathPrimitiveUpdatePolicy`
              - A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

            * - :py:class:`~ProjectedRasterOverlay`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~Projection`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~ProjectionStream`
              - A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

            * - :py:class:`~SceneGlobeOverlaySettings`
              - Settings used by globe overlay objects. These settings only affect the scene.

            * - :py:class:`~ScreenOverlayCollectionBase`
              - The common base class for collections of overlays held by screen overlay and by screen overlay manager.

            * - :py:class:`~Texture2DFactory`
              - A factory for creating texture 2d objects from various sources.

            * - :py:class:`~VisualEffects`
              - Control various post processing effects that can be applied to the scene.

            * - :py:class:`~AltitudeDisplayCondition`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~AxesPrimitive`
              - Render an axes in the 3D scene.

            * - :py:class:`~Camera`
              - Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

            * - :py:class:`~CentralBodyGraphics`
              - The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

            * - :py:class:`~Clouds`
              - Load, show and hide clouds in the scene.

            * - :py:class:`~CompositeDisplayCondition`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~CompositePrimitive`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~ConstantDisplayCondition`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~DisplayCondition`
              - When assigned to objects, such as primitives or globe overlays, display conditions are evaluated to determine if the object should be rendered.

            * - :py:class:`~DistanceDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~DistanceToGlobeOverlayDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~DistanceToPositionDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~DistanceToPrimitiveDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~DurationPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~FrameRate`
              - Keeps track of how many times the scenes are rendered per second.

            * - :py:class:`~GlobeImageOverlay`
              - A globe overlay that shows an image.

            * - :py:class:`~GraphicsFont`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~GreatArcInterpolator`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~ImageCollection`
              - A collection of globe image overlay objects.

            * - :py:class:`~AlphaFromLuminanceFilter`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~AlphaFromPixelFilter`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~AlphaFromRasterFilter`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~BandExtractFilter`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~BandOrderFilter`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~BlurFilter`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~BrightnessFilter`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~ColorToLuminanceFilter`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~ContrastFilter`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~ConvolutionFilter`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~EdgeDetectFilter`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~FilteringRasterStream`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~FlipFilter`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~GammaCorrectionFilter`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~GaussianBlurFilter`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~GradientDetectFilter`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~LevelsFilter`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~ProjectionRasterStreamPluginActivator`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~ProjectionRasterStreamPluginProxy`
              - A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

            * - :py:class:`~Raster`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~RasterAttributes`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~RasterFilter`
              - A filter for processing raster datasets. RasterFilter is the base class for all raster filters...

            * - :py:class:`~RasterStream`
              - A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

            * - :py:class:`~RotateFilter`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~SequenceFilter`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~SharpenFilter`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~VideoStream`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~KmlContainer`
              - A KmlContainer contains a collection of children kml features.

            * - :py:class:`~KmlDocument`
              - A KML document.

            * - :py:class:`~KmlFeature`
              - A KML feature.

            * - :py:class:`~KmlFolder`
              - A KML folder.

            * - :py:class:`~KmlGraphics`
              - Provide loading and unloading of kml documents for a particular central body.

            * - :py:class:`~KmlNetworkLink`
              - A KML network link.

            * - :py:class:`~MarkerBatchPrimitive`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~MarkerBatchPrimitiveOptionalParameters`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~MaximumCountPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~ModelArticulation`
              - A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~ModelArticulationCollection`
              - A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~ModelPrimitive`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~ModelTransformation`
              - A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

            * - :py:class:`~Overlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~PathPrimitive`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~PickResult`
              - A single result from Pick.

            * - :py:class:`~PixelSizeDisplayCondition`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~PointBatchPrimitive`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~PointBatchPrimitiveOptionalParameters`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~PolylinePrimitive`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~PolylinePrimitiveOptionalParameters`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~PositionInterpolator`
              - Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

            * - :py:class:`~Primitive`
              - Primitives represent objects rendered in the 3D scene.

            * - :py:class:`~PrimitiveManager`
              - The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

            * - :py:class:`~RasterImageGlobeOverlay`
              - A globe image overlay for handling rasters.

            * - :py:class:`~RhumbLineInterpolator`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~Scene`
              - A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

            * - :py:class:`~SceneDisplayCondition`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~SceneManager`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~ScreenOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ScreenOverlayCollection`
              - A collection of screen overlays.

            * - :py:class:`~ScreenOverlayManager`
              - The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

            * - :py:class:`~ScreenOverlayPickResult`
              - Describes a picked screen overlay as a result of a call to pick screen overlays.

            * - :py:class:`~SolidPrimitive`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~Stereoscopic`
              - Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :py:class:`~SurfaceMeshPrimitive`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~TerrainOverlayCollection`
              - A collection of terrain overlay objects.

            * - :py:class:`~TerrainOverlay`
              - A globe overlay which shows terrain.

            * - :py:class:`~TextBatchPrimitive`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~TextBatchPrimitiveOptionalParameters`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~TextOverlay`
              - A rectangular overlay that contains text.

            * - :py:class:`~TextureMatrix`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~TextureScreenOverlay`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~TimeIntervalDisplayCondition`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~TriangleMeshPrimitive`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~TriangleMeshPrimitiveOptionalParameters`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~VectorPrimitive`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

            * - :py:class:`~BoxTriangulatorInitializer`
              - Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~CylinderTriangulatorInitializer`
              - Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~EllipsoidTriangulatorInitializer`
              - Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ExtrudedPolylineTriangulatorInitializer`
              - Triangulates a polyline into an extrusion with bottom and top boundaries.

            * - :py:class:`~SurfaceExtentTriangulatorInitializer`
              - Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

            * - :py:class:`~SurfacePolygonTriangulatorInitializer`
              - Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~SurfaceShapesInitializer`
              - Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

            * - :py:class:`~AGICustomTerrainOverlayFactory`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~AGIProcessedImageGlobeOverlayFactory`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~AGIProcessedTerrainOverlayFactory`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~AGIRoamImageGlobeOverlayFactory`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~CustomImageGlobeOverlayPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~GeospatialImageGlobeOverlayFactory`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~ProjectedRasterOverlayFactory`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~ProjectionFactory`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~AltitudeDisplayConditionFactory`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~AxesPrimitiveFactory`
              - Render an axes in the 3D scene.

            * - :py:class:`~CompositeDisplayConditionFactory`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~CompositePrimitiveFactory`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~ConstantDisplayConditionFactory`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~DistanceDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~DistanceToGlobeOverlayDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~DistanceToPositionDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~DistanceToPrimitiveDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~DurationPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~GlobeImageOverlayInitializer`
              - A globe overlay that shows an image.

            * - :py:class:`~GraphicsFontFactory`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~GreatArcInterpolatorFactory`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~AlphaFromLuminanceFilterFactory`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~AlphaFromPixelFilterFactory`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~AlphaFromRasterFilterFactory`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~BandExtractFilterFactory`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~BandOrderFilterFactory`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~BlurFilterFactory`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~BrightnessFilterFactory`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~ColorToLuminanceFilterFactory`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~ContrastFilterFactory`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~ConvolutionFilterFactory`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~EdgeDetectFilterFactory`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~FilteringRasterStreamFactory`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~FlipFilterFactory`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~GammaCorrectionFilterFactory`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~GaussianBlurFilterFactory`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~GradientDetectFilterFactory`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~Jpeg2000WriterInitializer`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

            * - :py:class:`~LevelsFilterFactory`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~ProjectionRasterStreamPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~RasterFactory`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~RasterAttributesFactory`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~RotateFilterFactory`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~SequenceFilterFactory`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~SharpenFilterFactory`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~VideoStreamFactory`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~MarkerBatchPrimitiveFactory`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~MarkerBatchPrimitiveOptionalParametersFactory`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~MaximumCountPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~ModelPrimitiveFactory`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~PathPrimitiveFactory`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~PixelSizeDisplayConditionFactory`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~PointBatchPrimitiveFactory`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~PointBatchPrimitiveOptionalParametersFactory`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~PolylinePrimitiveFactory`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~PolylinePrimitiveOptionalParametersFactory`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~RasterImageGlobeOverlayFactory`
              - A globe image overlay for handling rasters.

            * - :py:class:`~RhumbLineInterpolatorFactory`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~SceneDisplayConditionFactory`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~SceneManagerInitializer`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~ScreenOverlayFactory`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~SolidPrimitiveFactory`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~SurfaceMeshPrimitiveFactory`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~TerrainOverlayInitializer`
              - A globe overlay which shows terrain.

            * - :py:class:`~TextBatchPrimitiveFactory`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~TextBatchPrimitiveOptionalParametersFactory`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~TextOverlayFactory`
              - A rectangular overlay that contains text.

            * - :py:class:`~TextureMatrixFactory`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~TextureScreenOverlayFactory`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~TimeIntervalDisplayConditionFactory`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~TriangleMeshPrimitiveFactory`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~TriangleMeshPrimitiveOptionalParametersFactory`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~VectorPrimitiveFactory`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~CYLINDER_FILL`
              - Cylinder faces that can be filled.

            * - :py:class:`~WINDING_ORDER`
              - Specify the order for positions or front facing triangles. Winding order is important for triangulation and backface culling.

            * - :py:class:`~CAMERA_SNAPSHOT_FILE_FORMAT`
              - When using camera snapshot or camera video recording to save a snapshot to a file, this specifies the file format.

            * - :py:class:`~CAMERA_VIDEO_FORMAT`
              - When using camera video recording to record a video, this specifies the file format.

            * - :py:class:`~CONSTRAINED_UP_AXIS`
              - When setting the camera'saxes, this defines which axis of the axes is up in screen space, where up is from the bottom to the top of the screen.

            * - :py:class:`~GLOBE_OVERLAY_ROLE`
              - The role of a globe overlay.

            * - :py:class:`~INDICES_ORDER_HINT`
              - An optimization hint optionally provided to a primitive'sSetPartial method to enhance performance.

            * - :py:class:`~MAINTAIN_ASPECT_RATIO`
              - Specify whether the aspect ratio of a texture will be maintained during sizing of a screen overlay.

            * - :py:class:`~MAP_PROJECTION`
              - The projection of the pixel data returned from a custom image globe overlay.

            * - :py:class:`~MARKER_BATCH_RENDERING_METHOD`
              - Rendering methods available for use by the marker batch primitive. Different methods may have different performance characteristics and require different video card support. When in doubt, use Automatic.

            * - :py:class:`~MARKER_BATCH_RENDER_PASS`
              - The pass during which the marker batch is rendered.

            * - :py:class:`~MARKER_BATCH_SIZE_SOURCE`
              - Determine which marker batch property is used to size each marker in a marker batch.

            * - :py:class:`~MARKER_BATCH_SORT_ORDER`
              - The order in which markers in a marker batch are sorted before rendering.

            * - :py:class:`~MARKER_BATCH_UNIT`
              - The unit for marker sizes in a marker batch.

            * - :py:class:`~MODEL_TRANSFORMATION_TYPE`
              - Transformation types that define the way a model transformation changes the geometry of the model articulation it is associated with.

            * - :py:class:`~ORIGIN`
              - Vertical and horizontal origin.

            * - :py:class:`~PATH_PRIMITIVE_REMOVE_LOCATION`
              - Represents the location of a point to be removed.

            * - :py:class:`~PRIMITIVES_SORT_ORDER`
              - The order in which primitives are sorted before rendering.

            * - :py:class:`~REFRESH_RATE`
              - The rate at which animation frames will occur.

            * - :py:class:`~RENDER_PASS`
              - Describes when a primitive will be rendered. Some primitives need to be rendered during or at a certain time. For example, translucent primitives need to be rendered after opaque primitives to allow proper blending...

            * - :py:class:`~RENDER_PASS_HINT`
              - An optimization hint optionally provided to a primitive'sSet method to enhance performance when per-position colors are used.

            * - :py:class:`~SCREEN_OVERLAY_ORIGIN`
              - Specify the origin of a screen overlay, as well as the direction of the horizontal and vertical axes. The origin specifies both the origin in the parent overlay's coordinate system and the origin within the overlay itself that is positioned.

            * - :py:class:`~SCREEN_OVERLAY_PINNING_ORIGIN`
              - Specify the origin of the pinning position of the screen overlay, as well as the direction of the horizontal and vertical axes for that pinning position. The pinning origin specifies the origin of the pinning position in the overlay's coordinate system.

            * - :py:class:`~SCREEN_OVERLAY_UNIT`
              - A unit specifying how a screen overlay is sized and positioned relative to its parent.

            * - :py:class:`~SURFACE_MESH_RENDERING_METHOD`
              - Rendering methods available for use by the surface mesh primitive. Different methods may have different performance characteristics and require different video card support. When in doubt, use Automatic.

            * - :py:class:`~VISIBILITY`
              - Result of a visibility test, such as testing if a sphere intersects a frustum.

            * - :py:class:`~ANTI_ALIASING`
              - The multisample anti-aliasing (MSAA) options for Scenes. As the level of anti-aliasing increases, performance will generally decrease, but the quality of the anti-aliasing will improve.

            * - :py:class:`~BINARY_LOGIC_OPERATION`
              - Binary logic operations that can be used by composite display condition.

            * - :py:class:`~BLUR_METHOD`
              - The method used to blur or smooth a raster.

            * - :py:class:`~EDGE_DETECT_METHOD`
              - The method used to detect edges in a raster.

            * - :py:class:`~FLIP_AXIS`
              - The axis on which a raster will be flipped.

            * - :py:class:`~GRADIENT_DETECT_METHOD`
              - The method used to detect gradients in a raster. Gradient detection is commonly referred to as embossing.

            * - :py:class:`~JPEG2000_COMPRESSION_PROFILE`
              - Define the profile used when encoding a JPEG 2000 file.

            * - :py:class:`~RASTER_BAND`
              - Common band types that may be contained within a raster dataset. Each band can be thought of as a set of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~RASTER_FORMAT`
              - Common raster band layouts that may be contained within a raster dataset. Each pixel of the raster will contain the bands defined by the layout in the specified order. A typical color raster image will have an rgbraster format.

            * - :py:class:`~RASTER_ORIENTATION`
              - The vertical orientation of the raster.

            * - :py:class:`~RASTER_TYPE`
              - The type of data contained within each band of a raster dataset.

            * - :py:class:`~SHARPEN_METHOD`
              - The method used to sharpen a raster.

            * - :py:class:`~VIDEO_PLAYBACK`
              - Specify how the video stream will playback. When the playback is set to real time, the video will playback in real time...

            * - :py:class:`~KML_NETWORK_LINK_REFRESH_MODE`
              - Define the options available for a KmlNetworkLink's RefreshMode property.

            * - :py:class:`~KML_NETWORK_LINK_VIEW_REFRESH_MODE`
              - Define the options available for a KmlNetworkLink's ViewRefreshMode property.

            * - :py:class:`~MODEL_UP_AXIS`
              - When setting the camera'saxes, this defines which axis of the axes is up in screen space, where up is from the bottom to the top of the screen.

            * - :py:class:`~OUTLINE_APPEARANCE`
              - Possible appearances of an outline. Front lines are lines on front facing geometry and back lines are lines on back facing geometry.

            * - :py:class:`~POLYLINE_TYPE`
              - Describes how to interpret positions defining a polyline.

            * - :py:class:`~CULL_FACE`
              - Identifies whether front- and/or back-facing triangles are culled.

            * - :py:class:`~INTERNAL_TEXTURE_FORMAT`
              - The format of individual texels in a texture.

            * - :py:class:`~MAGNIFICATION_FILTER`
              - The filter used when the pixel being textured maps to an area less than or equal to one texel.

            * - :py:class:`~MINIFICATION_FILTER`
              - The filter used when the pixel being textured maps to an area greater than one texel.

            * - :py:class:`~RENDERER_SHADE_MODEL`
              - Identifies which shade model to use. The primitive can be drawn with a single color or multiple colors.

            * - :py:class:`~TEXTURE_WRAP`
              - Determine how to handle textures coordinates that fall outside of the range [0, 1].

            * - :py:class:`~SET_HINT`
              - An optimization hint optionally provided to primitives to enhance performance for static or dynamic primitives. See the Set Hint Performance Overview for selecting an appropriate value.

            * - :py:class:`~STEREO_PROJECTION_MODE`
              - The stereoscopic projection mode used for the left and right eye scenes.

            * - :py:class:`~STEREOSCOPIC_DISPLAY_MODE`
              - The stereoscopic display mode. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :py:class:`~FONT_STYLE`
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

     IPathPoint<graphics/IPathPoint>
     IPathPointFactory<graphics/IPathPointFactory>
     IBoundingSphere<graphics/IBoundingSphere>
     IBoundingSphereFactory<graphics/IBoundingSphereFactory>
     ITextureFilter2D<graphics/ITextureFilter2D>
     ITextureFilter2DFactory<graphics/ITextureFilter2DFactory>
     IRendererTexture2D<graphics/IRendererTexture2D>
     IRendererTextureTemplate2D<graphics/IRendererTextureTemplate2D>
     IPathPointCollection<graphics/IPathPointCollection>
     IObjectCollection<graphics/IObjectCollection>
     ISceneCollection<graphics/ISceneCollection>
     IScreenOverlayContainer<graphics/IScreenOverlayContainer>
     IScreenOverlayPickResultCollection<graphics/IScreenOverlayPickResultCollection>
     IGlobeImageOverlayAddCompleteEventArgs<graphics/IGlobeImageOverlayAddCompleteEventArgs>
     ITerrainOverlayAddCompleteEventArgs<graphics/ITerrainOverlayAddCompleteEventArgs>
     IPickResultCollection<graphics/IPickResultCollection>
     IRenderingEventArgs<graphics/IRenderingEventArgs>
     IBatchPrimitiveIndex<graphics/IBatchPrimitiveIndex>
     IKmlDocumentCollection<graphics/IKmlDocumentCollection>
     IKmlFeatureCollection<graphics/IKmlFeatureCollection>
     IKmlDocumentLoadedEventArgs<graphics/IKmlDocumentLoadedEventArgs>
     IFactoryAndInitializers<graphics/IFactoryAndInitializers>
     IExtrudedPolylineTriangulatorResult<graphics/IExtrudedPolylineTriangulatorResult>
     ISolidTriangulatorResult<graphics/ISolidTriangulatorResult>
     ISurfaceShapesResult<graphics/ISurfaceShapesResult>
     ISurfaceTriangulatorResult<graphics/ISurfaceTriangulatorResult>
     ITriangulatorResult<graphics/ITriangulatorResult>
     IAGICustomTerrainOverlay<graphics/IAGICustomTerrainOverlay>
     IAGIProcessedImageGlobeOverlay<graphics/IAGIProcessedImageGlobeOverlay>
     IAGIProcessedTerrainOverlay<graphics/IAGIProcessedTerrainOverlay>
     IAGIRoamImageGlobeOverlay<graphics/IAGIRoamImageGlobeOverlay>
     ICameraSnapshot<graphics/ICameraSnapshot>
     ICameraVideoRecording<graphics/ICameraVideoRecording>
     ICentralBodyGraphicsIndexer<graphics/ICentralBodyGraphicsIndexer>
     ICustomImageGlobeOverlay<graphics/ICustomImageGlobeOverlay>
     ICustomImageGlobeOverlayPluginActivator<graphics/ICustomImageGlobeOverlayPluginActivator>
     ICustomImageGlobeOverlayPluginProxy<graphics/ICustomImageGlobeOverlayPluginProxy>
     IGeospatialImageGlobeOverlay<graphics/IGeospatialImageGlobeOverlay>
     IGlobeOverlay<graphics/IGlobeOverlay>
     IGlobeOverlaySettings<graphics/IGlobeOverlaySettings>
     ILighting<graphics/ILighting>
     IPathPrimitiveUpdatePolicy<graphics/IPathPrimitiveUpdatePolicy>
     IProjectedRasterOverlay<graphics/IProjectedRasterOverlay>
     IProjection<graphics/IProjection>
     IProjectionStream<graphics/IProjectionStream>
     ISceneGlobeOverlaySettings<graphics/ISceneGlobeOverlaySettings>
     IScreenOverlayCollectionBase<graphics/IScreenOverlayCollectionBase>
     ITexture2DFactory<graphics/ITexture2DFactory>
     IVisualEffects<graphics/IVisualEffects>
     IAltitudeDisplayCondition<graphics/IAltitudeDisplayCondition>
     IAxesPrimitive<graphics/IAxesPrimitive>
     ICamera<graphics/ICamera>
     ICentralBodyGraphics<graphics/ICentralBodyGraphics>
     IClouds<graphics/IClouds>
     ICompositeDisplayCondition<graphics/ICompositeDisplayCondition>
     ICompositePrimitive<graphics/ICompositePrimitive>
     IConstantDisplayCondition<graphics/IConstantDisplayCondition>
     IDisplayCondition<graphics/IDisplayCondition>
     IDistanceDisplayCondition<graphics/IDistanceDisplayCondition>
     IDistanceToGlobeOverlayDisplayCondition<graphics/IDistanceToGlobeOverlayDisplayCondition>
     IDistanceToPositionDisplayCondition<graphics/IDistanceToPositionDisplayCondition>
     IDistanceToPrimitiveDisplayCondition<graphics/IDistanceToPrimitiveDisplayCondition>
     IDurationPathPrimitiveUpdatePolicy<graphics/IDurationPathPrimitiveUpdatePolicy>
     IFrameRate<graphics/IFrameRate>
     IGlobeImageOverlay<graphics/IGlobeImageOverlay>
     IGraphicsFont<graphics/IGraphicsFont>
     IGreatArcInterpolator<graphics/IGreatArcInterpolator>
     IImageCollection<graphics/IImageCollection>
     IAlphaFromLuminanceFilter<graphics/IAlphaFromLuminanceFilter>
     IAlphaFromPixelFilter<graphics/IAlphaFromPixelFilter>
     IAlphaFromRasterFilter<graphics/IAlphaFromRasterFilter>
     IBandExtractFilter<graphics/IBandExtractFilter>
     IBandOrderFilter<graphics/IBandOrderFilter>
     IBlurFilter<graphics/IBlurFilter>
     IBrightnessFilter<graphics/IBrightnessFilter>
     IColorToLuminanceFilter<graphics/IColorToLuminanceFilter>
     IContrastFilter<graphics/IContrastFilter>
     IConvolutionFilter<graphics/IConvolutionFilter>
     IEdgeDetectFilter<graphics/IEdgeDetectFilter>
     IFilteringRasterStream<graphics/IFilteringRasterStream>
     IFlipFilter<graphics/IFlipFilter>
     IGammaCorrectionFilter<graphics/IGammaCorrectionFilter>
     IGaussianBlurFilter<graphics/IGaussianBlurFilter>
     IGradientDetectFilter<graphics/IGradientDetectFilter>
     ILevelsFilter<graphics/ILevelsFilter>
     IProjectionRasterStreamPluginActivator<graphics/IProjectionRasterStreamPluginActivator>
     IProjectionRasterStreamPluginProxy<graphics/IProjectionRasterStreamPluginProxy>
     IRaster<graphics/IRaster>
     IRasterAttributes<graphics/IRasterAttributes>
     IRasterFilter<graphics/IRasterFilter>
     IRasterStream<graphics/IRasterStream>
     IRotateFilter<graphics/IRotateFilter>
     ISequenceFilter<graphics/ISequenceFilter>
     ISharpenFilter<graphics/ISharpenFilter>
     IVideoStream<graphics/IVideoStream>
     IKmlContainer<graphics/IKmlContainer>
     IKmlDocument<graphics/IKmlDocument>
     IKmlFeature<graphics/IKmlFeature>
     IKmlFolder<graphics/IKmlFolder>
     IKmlGraphics<graphics/IKmlGraphics>
     IKmlNetworkLink<graphics/IKmlNetworkLink>
     IMarkerBatchPrimitive<graphics/IMarkerBatchPrimitive>
     IMarkerBatchPrimitiveOptionalParameters<graphics/IMarkerBatchPrimitiveOptionalParameters>
     IMaximumCountPathPrimitiveUpdatePolicy<graphics/IMaximumCountPathPrimitiveUpdatePolicy>
     IModelArticulation<graphics/IModelArticulation>
     IModelArticulationCollection<graphics/IModelArticulationCollection>
     IModelPrimitive<graphics/IModelPrimitive>
     IModelTransformation<graphics/IModelTransformation>
     IOverlay<graphics/IOverlay>
     IPathPrimitive<graphics/IPathPrimitive>
     IPickResult<graphics/IPickResult>
     IPixelSizeDisplayCondition<graphics/IPixelSizeDisplayCondition>
     IPointBatchPrimitive<graphics/IPointBatchPrimitive>
     IPointBatchPrimitiveOptionalParameters<graphics/IPointBatchPrimitiveOptionalParameters>
     IPolylinePrimitive<graphics/IPolylinePrimitive>
     IPolylinePrimitiveOptionalParameters<graphics/IPolylinePrimitiveOptionalParameters>
     IPositionInterpolator<graphics/IPositionInterpolator>
     IPrimitive<graphics/IPrimitive>
     IPrimitiveManager<graphics/IPrimitiveManager>
     IRasterImageGlobeOverlay<graphics/IRasterImageGlobeOverlay>
     IRhumbLineInterpolator<graphics/IRhumbLineInterpolator>
     IScene<graphics/IScene>
     ISceneDisplayCondition<graphics/ISceneDisplayCondition>
     ISceneManager<graphics/ISceneManager>
     IScreenOverlay<graphics/IScreenOverlay>
     IScreenOverlayCollection<graphics/IScreenOverlayCollection>
     IScreenOverlayManager<graphics/IScreenOverlayManager>
     IScreenOverlayPickResult<graphics/IScreenOverlayPickResult>
     ISolidPrimitive<graphics/ISolidPrimitive>
     IStereoscopic<graphics/IStereoscopic>
     ISurfaceMeshPrimitive<graphics/ISurfaceMeshPrimitive>
     ITerrainOverlayCollection<graphics/ITerrainOverlayCollection>
     ITerrainOverlay<graphics/ITerrainOverlay>
     ITextBatchPrimitive<graphics/ITextBatchPrimitive>
     ITextBatchPrimitiveOptionalParameters<graphics/ITextBatchPrimitiveOptionalParameters>
     ITextOverlay<graphics/ITextOverlay>
     ITextureMatrix<graphics/ITextureMatrix>
     ITextureScreenOverlay<graphics/ITextureScreenOverlay>
     ITimeIntervalDisplayCondition<graphics/ITimeIntervalDisplayCondition>
     ITriangleMeshPrimitive<graphics/ITriangleMeshPrimitive>
     ITriangleMeshPrimitiveOptionalParameters<graphics/ITriangleMeshPrimitiveOptionalParameters>
     IVectorPrimitive<graphics/IVectorPrimitive>
     IBoxTriangulatorInitializer<graphics/IBoxTriangulatorInitializer>
     ICylinderTriangulatorInitializer<graphics/ICylinderTriangulatorInitializer>
     IEllipsoidTriangulatorInitializer<graphics/IEllipsoidTriangulatorInitializer>
     IExtrudedPolylineTriangulatorInitializer<graphics/IExtrudedPolylineTriangulatorInitializer>
     ISurfaceExtentTriangulatorInitializer<graphics/ISurfaceExtentTriangulatorInitializer>
     ISurfacePolygonTriangulatorInitializer<graphics/ISurfacePolygonTriangulatorInitializer>
     ISurfaceShapesInitializer<graphics/ISurfaceShapesInitializer>
     IAGICustomTerrainOverlayFactory<graphics/IAGICustomTerrainOverlayFactory>
     IAGIProcessedImageGlobeOverlayFactory<graphics/IAGIProcessedImageGlobeOverlayFactory>
     IAGIProcessedTerrainOverlayFactory<graphics/IAGIProcessedTerrainOverlayFactory>
     IAGIRoamImageGlobeOverlayFactory<graphics/IAGIRoamImageGlobeOverlayFactory>
     ICustomImageGlobeOverlayPluginActivatorFactory<graphics/ICustomImageGlobeOverlayPluginActivatorFactory>
     IGeospatialImageGlobeOverlayFactory<graphics/IGeospatialImageGlobeOverlayFactory>
     IProjectedRasterOverlayFactory<graphics/IProjectedRasterOverlayFactory>
     IProjectionFactory<graphics/IProjectionFactory>
     IAltitudeDisplayConditionFactory<graphics/IAltitudeDisplayConditionFactory>
     IAxesPrimitiveFactory<graphics/IAxesPrimitiveFactory>
     ICompositeDisplayConditionFactory<graphics/ICompositeDisplayConditionFactory>
     ICompositePrimitiveFactory<graphics/ICompositePrimitiveFactory>
     IConstantDisplayConditionFactory<graphics/IConstantDisplayConditionFactory>
     IDistanceDisplayConditionFactory<graphics/IDistanceDisplayConditionFactory>
     IDistanceToGlobeOverlayDisplayConditionFactory<graphics/IDistanceToGlobeOverlayDisplayConditionFactory>
     IDistanceToPositionDisplayConditionFactory<graphics/IDistanceToPositionDisplayConditionFactory>
     IDistanceToPrimitiveDisplayConditionFactory<graphics/IDistanceToPrimitiveDisplayConditionFactory>
     IDurationPathPrimitiveUpdatePolicyFactory<graphics/IDurationPathPrimitiveUpdatePolicyFactory>
     IGlobeImageOverlayInitializer<graphics/IGlobeImageOverlayInitializer>
     IGraphicsFontFactory<graphics/IGraphicsFontFactory>
     IGreatArcInterpolatorFactory<graphics/IGreatArcInterpolatorFactory>
     IAlphaFromLuminanceFilterFactory<graphics/IAlphaFromLuminanceFilterFactory>
     IAlphaFromPixelFilterFactory<graphics/IAlphaFromPixelFilterFactory>
     IAlphaFromRasterFilterFactory<graphics/IAlphaFromRasterFilterFactory>
     IBandExtractFilterFactory<graphics/IBandExtractFilterFactory>
     IBandOrderFilterFactory<graphics/IBandOrderFilterFactory>
     IBlurFilterFactory<graphics/IBlurFilterFactory>
     IBrightnessFilterFactory<graphics/IBrightnessFilterFactory>
     IColorToLuminanceFilterFactory<graphics/IColorToLuminanceFilterFactory>
     IContrastFilterFactory<graphics/IContrastFilterFactory>
     IConvolutionFilterFactory<graphics/IConvolutionFilterFactory>
     IEdgeDetectFilterFactory<graphics/IEdgeDetectFilterFactory>
     IFilteringRasterStreamFactory<graphics/IFilteringRasterStreamFactory>
     IFlipFilterFactory<graphics/IFlipFilterFactory>
     IGammaCorrectionFilterFactory<graphics/IGammaCorrectionFilterFactory>
     IGaussianBlurFilterFactory<graphics/IGaussianBlurFilterFactory>
     IGradientDetectFilterFactory<graphics/IGradientDetectFilterFactory>
     IJpeg2000WriterInitializer<graphics/IJpeg2000WriterInitializer>
     ILevelsFilterFactory<graphics/ILevelsFilterFactory>
     IProjectionRasterStreamPluginActivatorFactory<graphics/IProjectionRasterStreamPluginActivatorFactory>
     IRasterFactory<graphics/IRasterFactory>
     IRasterAttributesFactory<graphics/IRasterAttributesFactory>
     IRotateFilterFactory<graphics/IRotateFilterFactory>
     ISequenceFilterFactory<graphics/ISequenceFilterFactory>
     ISharpenFilterFactory<graphics/ISharpenFilterFactory>
     IVideoStreamFactory<graphics/IVideoStreamFactory>
     IMarkerBatchPrimitiveFactory<graphics/IMarkerBatchPrimitiveFactory>
     IMarkerBatchPrimitiveOptionalParametersFactory<graphics/IMarkerBatchPrimitiveOptionalParametersFactory>
     IMaximumCountPathPrimitiveUpdatePolicyFactory<graphics/IMaximumCountPathPrimitiveUpdatePolicyFactory>
     IModelPrimitiveFactory<graphics/IModelPrimitiveFactory>
     IPathPrimitiveFactory<graphics/IPathPrimitiveFactory>
     IPixelSizeDisplayConditionFactory<graphics/IPixelSizeDisplayConditionFactory>
     IPointBatchPrimitiveFactory<graphics/IPointBatchPrimitiveFactory>
     IPointBatchPrimitiveOptionalParametersFactory<graphics/IPointBatchPrimitiveOptionalParametersFactory>
     IPolylinePrimitiveFactory<graphics/IPolylinePrimitiveFactory>
     IPolylinePrimitiveOptionalParametersFactory<graphics/IPolylinePrimitiveOptionalParametersFactory>
     IRasterImageGlobeOverlayFactory<graphics/IRasterImageGlobeOverlayFactory>
     IRhumbLineInterpolatorFactory<graphics/IRhumbLineInterpolatorFactory>
     ISceneDisplayConditionFactory<graphics/ISceneDisplayConditionFactory>
     ISceneManagerInitializer<graphics/ISceneManagerInitializer>
     IScreenOverlayFactory<graphics/IScreenOverlayFactory>
     ISolidPrimitiveFactory<graphics/ISolidPrimitiveFactory>
     ISurfaceMeshPrimitiveFactory<graphics/ISurfaceMeshPrimitiveFactory>
     ITerrainOverlayInitializer<graphics/ITerrainOverlayInitializer>
     ITextBatchPrimitiveFactory<graphics/ITextBatchPrimitiveFactory>
     ITextBatchPrimitiveOptionalParametersFactory<graphics/ITextBatchPrimitiveOptionalParametersFactory>
     ITextOverlayFactory<graphics/ITextOverlayFactory>
     ITextureMatrixFactory<graphics/ITextureMatrixFactory>
     ITextureScreenOverlayFactory<graphics/ITextureScreenOverlayFactory>
     ITimeIntervalDisplayConditionFactory<graphics/ITimeIntervalDisplayConditionFactory>
     ITriangleMeshPrimitiveFactory<graphics/ITriangleMeshPrimitiveFactory>
     ITriangleMeshPrimitiveOptionalParametersFactory<graphics/ITriangleMeshPrimitiveOptionalParametersFactory>
     IVectorPrimitiveFactory<graphics/IVectorPrimitiveFactory>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     PathPoint<graphics/PathPoint>
     PathPointFactory<graphics/PathPointFactory>
     BoundingSphere<graphics/BoundingSphere>
     BoundingSphereFactory<graphics/BoundingSphereFactory>
     TextureFilter2D<graphics/TextureFilter2D>
     TextureFilter2DFactory<graphics/TextureFilter2DFactory>
     RendererTexture2D<graphics/RendererTexture2D>
     RendererTextureTemplate2D<graphics/RendererTextureTemplate2D>
     PathPointCollection<graphics/PathPointCollection>
     ObjectCollection<graphics/ObjectCollection>
     SceneCollection<graphics/SceneCollection>
     ScreenOverlayPickResultCollection<graphics/ScreenOverlayPickResultCollection>
     GlobeImageOverlayAddCompleteEventArgs<graphics/GlobeImageOverlayAddCompleteEventArgs>
     TerrainOverlayAddCompleteEventArgs<graphics/TerrainOverlayAddCompleteEventArgs>
     PickResultCollection<graphics/PickResultCollection>
     RenderingEventArgs<graphics/RenderingEventArgs>
     BatchPrimitiveIndex<graphics/BatchPrimitiveIndex>
     KmlDocumentCollection<graphics/KmlDocumentCollection>
     KmlFeatureCollection<graphics/KmlFeatureCollection>
     KmlDocumentLoadedEventArgs<graphics/KmlDocumentLoadedEventArgs>
     FactoryAndInitializers<graphics/FactoryAndInitializers>
     ExtrudedPolylineTriangulatorResult<graphics/ExtrudedPolylineTriangulatorResult>
     SolidTriangulatorResult<graphics/SolidTriangulatorResult>
     SurfaceShapesResult<graphics/SurfaceShapesResult>
     SurfaceTriangulatorResult<graphics/SurfaceTriangulatorResult>
     TriangulatorResult<graphics/TriangulatorResult>
     AGICustomTerrainOverlay<graphics/AGICustomTerrainOverlay>
     AGIProcessedImageGlobeOverlay<graphics/AGIProcessedImageGlobeOverlay>
     AGIProcessedTerrainOverlay<graphics/AGIProcessedTerrainOverlay>
     AGIRoamImageGlobeOverlay<graphics/AGIRoamImageGlobeOverlay>
     CameraSnapshot<graphics/CameraSnapshot>
     CameraVideoRecording<graphics/CameraVideoRecording>
     CentralBodyGraphicsIndexer<graphics/CentralBodyGraphicsIndexer>
     CustomImageGlobeOverlay<graphics/CustomImageGlobeOverlay>
     CustomImageGlobeOverlayPluginActivator<graphics/CustomImageGlobeOverlayPluginActivator>
     CustomImageGlobeOverlayPluginProxy<graphics/CustomImageGlobeOverlayPluginProxy>
     GeospatialImageGlobeOverlay<graphics/GeospatialImageGlobeOverlay>
     GlobeOverlay<graphics/GlobeOverlay>
     GlobeOverlaySettings<graphics/GlobeOverlaySettings>
     Lighting<graphics/Lighting>
     PathPrimitiveUpdatePolicy<graphics/PathPrimitiveUpdatePolicy>
     ProjectedRasterOverlay<graphics/ProjectedRasterOverlay>
     Projection<graphics/Projection>
     ProjectionStream<graphics/ProjectionStream>
     SceneGlobeOverlaySettings<graphics/SceneGlobeOverlaySettings>
     ScreenOverlayCollectionBase<graphics/ScreenOverlayCollectionBase>
     Texture2DFactory<graphics/Texture2DFactory>
     VisualEffects<graphics/VisualEffects>
     AltitudeDisplayCondition<graphics/AltitudeDisplayCondition>
     AxesPrimitive<graphics/AxesPrimitive>
     Camera<graphics/Camera>
     CentralBodyGraphics<graphics/CentralBodyGraphics>
     Clouds<graphics/Clouds>
     CompositeDisplayCondition<graphics/CompositeDisplayCondition>
     CompositePrimitive<graphics/CompositePrimitive>
     ConstantDisplayCondition<graphics/ConstantDisplayCondition>
     DisplayCondition<graphics/DisplayCondition>
     DistanceDisplayCondition<graphics/DistanceDisplayCondition>
     DistanceToGlobeOverlayDisplayCondition<graphics/DistanceToGlobeOverlayDisplayCondition>
     DistanceToPositionDisplayCondition<graphics/DistanceToPositionDisplayCondition>
     DistanceToPrimitiveDisplayCondition<graphics/DistanceToPrimitiveDisplayCondition>
     DurationPathPrimitiveUpdatePolicy<graphics/DurationPathPrimitiveUpdatePolicy>
     FrameRate<graphics/FrameRate>
     GlobeImageOverlay<graphics/GlobeImageOverlay>
     GraphicsFont<graphics/GraphicsFont>
     GreatArcInterpolator<graphics/GreatArcInterpolator>
     ImageCollection<graphics/ImageCollection>
     AlphaFromLuminanceFilter<graphics/AlphaFromLuminanceFilter>
     AlphaFromPixelFilter<graphics/AlphaFromPixelFilter>
     AlphaFromRasterFilter<graphics/AlphaFromRasterFilter>
     BandExtractFilter<graphics/BandExtractFilter>
     BandOrderFilter<graphics/BandOrderFilter>
     BlurFilter<graphics/BlurFilter>
     BrightnessFilter<graphics/BrightnessFilter>
     ColorToLuminanceFilter<graphics/ColorToLuminanceFilter>
     ContrastFilter<graphics/ContrastFilter>
     ConvolutionFilter<graphics/ConvolutionFilter>
     EdgeDetectFilter<graphics/EdgeDetectFilter>
     FilteringRasterStream<graphics/FilteringRasterStream>
     FlipFilter<graphics/FlipFilter>
     GammaCorrectionFilter<graphics/GammaCorrectionFilter>
     GaussianBlurFilter<graphics/GaussianBlurFilter>
     GradientDetectFilter<graphics/GradientDetectFilter>
     LevelsFilter<graphics/LevelsFilter>
     ProjectionRasterStreamPluginActivator<graphics/ProjectionRasterStreamPluginActivator>
     ProjectionRasterStreamPluginProxy<graphics/ProjectionRasterStreamPluginProxy>
     Raster<graphics/Raster>
     RasterAttributes<graphics/RasterAttributes>
     RasterFilter<graphics/RasterFilter>
     RasterStream<graphics/RasterStream>
     RotateFilter<graphics/RotateFilter>
     SequenceFilter<graphics/SequenceFilter>
     SharpenFilter<graphics/SharpenFilter>
     VideoStream<graphics/VideoStream>
     KmlContainer<graphics/KmlContainer>
     KmlDocument<graphics/KmlDocument>
     KmlFeature<graphics/KmlFeature>
     KmlFolder<graphics/KmlFolder>
     KmlGraphics<graphics/KmlGraphics>
     KmlNetworkLink<graphics/KmlNetworkLink>
     MarkerBatchPrimitive<graphics/MarkerBatchPrimitive>
     MarkerBatchPrimitiveOptionalParameters<graphics/MarkerBatchPrimitiveOptionalParameters>
     MaximumCountPathPrimitiveUpdatePolicy<graphics/MaximumCountPathPrimitiveUpdatePolicy>
     ModelArticulation<graphics/ModelArticulation>
     ModelArticulationCollection<graphics/ModelArticulationCollection>
     ModelPrimitive<graphics/ModelPrimitive>
     ModelTransformation<graphics/ModelTransformation>
     Overlay<graphics/Overlay>
     PathPrimitive<graphics/PathPrimitive>
     PickResult<graphics/PickResult>
     PixelSizeDisplayCondition<graphics/PixelSizeDisplayCondition>
     PointBatchPrimitive<graphics/PointBatchPrimitive>
     PointBatchPrimitiveOptionalParameters<graphics/PointBatchPrimitiveOptionalParameters>
     PolylinePrimitive<graphics/PolylinePrimitive>
     PolylinePrimitiveOptionalParameters<graphics/PolylinePrimitiveOptionalParameters>
     PositionInterpolator<graphics/PositionInterpolator>
     Primitive<graphics/Primitive>
     PrimitiveManager<graphics/PrimitiveManager>
     RasterImageGlobeOverlay<graphics/RasterImageGlobeOverlay>
     RhumbLineInterpolator<graphics/RhumbLineInterpolator>
     Scene<graphics/Scene>
     SceneDisplayCondition<graphics/SceneDisplayCondition>
     SceneManager<graphics/SceneManager>
     ScreenOverlay<graphics/ScreenOverlay>
     ScreenOverlayCollection<graphics/ScreenOverlayCollection>
     ScreenOverlayManager<graphics/ScreenOverlayManager>
     ScreenOverlayPickResult<graphics/ScreenOverlayPickResult>
     SolidPrimitive<graphics/SolidPrimitive>
     Stereoscopic<graphics/Stereoscopic>
     SurfaceMeshPrimitive<graphics/SurfaceMeshPrimitive>
     TerrainOverlayCollection<graphics/TerrainOverlayCollection>
     TerrainOverlay<graphics/TerrainOverlay>
     TextBatchPrimitive<graphics/TextBatchPrimitive>
     TextBatchPrimitiveOptionalParameters<graphics/TextBatchPrimitiveOptionalParameters>
     TextOverlay<graphics/TextOverlay>
     TextureMatrix<graphics/TextureMatrix>
     TextureScreenOverlay<graphics/TextureScreenOverlay>
     TimeIntervalDisplayCondition<graphics/TimeIntervalDisplayCondition>
     TriangleMeshPrimitive<graphics/TriangleMeshPrimitive>
     TriangleMeshPrimitiveOptionalParameters<graphics/TriangleMeshPrimitiveOptionalParameters>
     VectorPrimitive<graphics/VectorPrimitive>
     BoxTriangulatorInitializer<graphics/BoxTriangulatorInitializer>
     CylinderTriangulatorInitializer<graphics/CylinderTriangulatorInitializer>
     EllipsoidTriangulatorInitializer<graphics/EllipsoidTriangulatorInitializer>
     ExtrudedPolylineTriangulatorInitializer<graphics/ExtrudedPolylineTriangulatorInitializer>
     SurfaceExtentTriangulatorInitializer<graphics/SurfaceExtentTriangulatorInitializer>
     SurfacePolygonTriangulatorInitializer<graphics/SurfacePolygonTriangulatorInitializer>
     SurfaceShapesInitializer<graphics/SurfaceShapesInitializer>
     AGICustomTerrainOverlayFactory<graphics/AGICustomTerrainOverlayFactory>
     AGIProcessedImageGlobeOverlayFactory<graphics/AGIProcessedImageGlobeOverlayFactory>
     AGIProcessedTerrainOverlayFactory<graphics/AGIProcessedTerrainOverlayFactory>
     AGIRoamImageGlobeOverlayFactory<graphics/AGIRoamImageGlobeOverlayFactory>
     CustomImageGlobeOverlayPluginActivatorFactory<graphics/CustomImageGlobeOverlayPluginActivatorFactory>
     GeospatialImageGlobeOverlayFactory<graphics/GeospatialImageGlobeOverlayFactory>
     ProjectedRasterOverlayFactory<graphics/ProjectedRasterOverlayFactory>
     ProjectionFactory<graphics/ProjectionFactory>
     AltitudeDisplayConditionFactory<graphics/AltitudeDisplayConditionFactory>
     AxesPrimitiveFactory<graphics/AxesPrimitiveFactory>
     CompositeDisplayConditionFactory<graphics/CompositeDisplayConditionFactory>
     CompositePrimitiveFactory<graphics/CompositePrimitiveFactory>
     ConstantDisplayConditionFactory<graphics/ConstantDisplayConditionFactory>
     DistanceDisplayConditionFactory<graphics/DistanceDisplayConditionFactory>
     DistanceToGlobeOverlayDisplayConditionFactory<graphics/DistanceToGlobeOverlayDisplayConditionFactory>
     DistanceToPositionDisplayConditionFactory<graphics/DistanceToPositionDisplayConditionFactory>
     DistanceToPrimitiveDisplayConditionFactory<graphics/DistanceToPrimitiveDisplayConditionFactory>
     DurationPathPrimitiveUpdatePolicyFactory<graphics/DurationPathPrimitiveUpdatePolicyFactory>
     GlobeImageOverlayInitializer<graphics/GlobeImageOverlayInitializer>
     GraphicsFontFactory<graphics/GraphicsFontFactory>
     GreatArcInterpolatorFactory<graphics/GreatArcInterpolatorFactory>
     AlphaFromLuminanceFilterFactory<graphics/AlphaFromLuminanceFilterFactory>
     AlphaFromPixelFilterFactory<graphics/AlphaFromPixelFilterFactory>
     AlphaFromRasterFilterFactory<graphics/AlphaFromRasterFilterFactory>
     BandExtractFilterFactory<graphics/BandExtractFilterFactory>
     BandOrderFilterFactory<graphics/BandOrderFilterFactory>
     BlurFilterFactory<graphics/BlurFilterFactory>
     BrightnessFilterFactory<graphics/BrightnessFilterFactory>
     ColorToLuminanceFilterFactory<graphics/ColorToLuminanceFilterFactory>
     ContrastFilterFactory<graphics/ContrastFilterFactory>
     ConvolutionFilterFactory<graphics/ConvolutionFilterFactory>
     EdgeDetectFilterFactory<graphics/EdgeDetectFilterFactory>
     FilteringRasterStreamFactory<graphics/FilteringRasterStreamFactory>
     FlipFilterFactory<graphics/FlipFilterFactory>
     GammaCorrectionFilterFactory<graphics/GammaCorrectionFilterFactory>
     GaussianBlurFilterFactory<graphics/GaussianBlurFilterFactory>
     GradientDetectFilterFactory<graphics/GradientDetectFilterFactory>
     Jpeg2000WriterInitializer<graphics/Jpeg2000WriterInitializer>
     LevelsFilterFactory<graphics/LevelsFilterFactory>
     ProjectionRasterStreamPluginActivatorFactory<graphics/ProjectionRasterStreamPluginActivatorFactory>
     RasterFactory<graphics/RasterFactory>
     RasterAttributesFactory<graphics/RasterAttributesFactory>
     RotateFilterFactory<graphics/RotateFilterFactory>
     SequenceFilterFactory<graphics/SequenceFilterFactory>
     SharpenFilterFactory<graphics/SharpenFilterFactory>
     VideoStreamFactory<graphics/VideoStreamFactory>
     MarkerBatchPrimitiveFactory<graphics/MarkerBatchPrimitiveFactory>
     MarkerBatchPrimitiveOptionalParametersFactory<graphics/MarkerBatchPrimitiveOptionalParametersFactory>
     MaximumCountPathPrimitiveUpdatePolicyFactory<graphics/MaximumCountPathPrimitiveUpdatePolicyFactory>
     ModelPrimitiveFactory<graphics/ModelPrimitiveFactory>
     PathPrimitiveFactory<graphics/PathPrimitiveFactory>
     PixelSizeDisplayConditionFactory<graphics/PixelSizeDisplayConditionFactory>
     PointBatchPrimitiveFactory<graphics/PointBatchPrimitiveFactory>
     PointBatchPrimitiveOptionalParametersFactory<graphics/PointBatchPrimitiveOptionalParametersFactory>
     PolylinePrimitiveFactory<graphics/PolylinePrimitiveFactory>
     PolylinePrimitiveOptionalParametersFactory<graphics/PolylinePrimitiveOptionalParametersFactory>
     RasterImageGlobeOverlayFactory<graphics/RasterImageGlobeOverlayFactory>
     RhumbLineInterpolatorFactory<graphics/RhumbLineInterpolatorFactory>
     SceneDisplayConditionFactory<graphics/SceneDisplayConditionFactory>
     SceneManagerInitializer<graphics/SceneManagerInitializer>
     ScreenOverlayFactory<graphics/ScreenOverlayFactory>
     SolidPrimitiveFactory<graphics/SolidPrimitiveFactory>
     SurfaceMeshPrimitiveFactory<graphics/SurfaceMeshPrimitiveFactory>
     TerrainOverlayInitializer<graphics/TerrainOverlayInitializer>
     TextBatchPrimitiveFactory<graphics/TextBatchPrimitiveFactory>
     TextBatchPrimitiveOptionalParametersFactory<graphics/TextBatchPrimitiveOptionalParametersFactory>
     TextOverlayFactory<graphics/TextOverlayFactory>
     TextureMatrixFactory<graphics/TextureMatrixFactory>
     TextureScreenOverlayFactory<graphics/TextureScreenOverlayFactory>
     TimeIntervalDisplayConditionFactory<graphics/TimeIntervalDisplayConditionFactory>
     TriangleMeshPrimitiveFactory<graphics/TriangleMeshPrimitiveFactory>
     TriangleMeshPrimitiveOptionalParametersFactory<graphics/TriangleMeshPrimitiveOptionalParametersFactory>
     VectorPrimitiveFactory<graphics/VectorPrimitiveFactory>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ CYLINDER_FILL<graphics/CYLINDER_FILL>
    ≔ WINDING_ORDER<graphics/WINDING_ORDER>
    ≔ CAMERA_SNAPSHOT_FILE_FORMAT<graphics/CAMERA_SNAPSHOT_FILE_FORMAT>
    ≔ CAMERA_VIDEO_FORMAT<graphics/CAMERA_VIDEO_FORMAT>
    ≔ CONSTRAINED_UP_AXIS<graphics/CONSTRAINED_UP_AXIS>
    ≔ GLOBE_OVERLAY_ROLE<graphics/GLOBE_OVERLAY_ROLE>
    ≔ INDICES_ORDER_HINT<graphics/INDICES_ORDER_HINT>
    ≔ MAINTAIN_ASPECT_RATIO<graphics/MAINTAIN_ASPECT_RATIO>
    ≔ MAP_PROJECTION<graphics/MAP_PROJECTION>
    ≔ MARKER_BATCH_RENDERING_METHOD<graphics/MARKER_BATCH_RENDERING_METHOD>
    ≔ MARKER_BATCH_RENDER_PASS<graphics/MARKER_BATCH_RENDER_PASS>
    ≔ MARKER_BATCH_SIZE_SOURCE<graphics/MARKER_BATCH_SIZE_SOURCE>
    ≔ MARKER_BATCH_SORT_ORDER<graphics/MARKER_BATCH_SORT_ORDER>
    ≔ MARKER_BATCH_UNIT<graphics/MARKER_BATCH_UNIT>
    ≔ MODEL_TRANSFORMATION_TYPE<graphics/MODEL_TRANSFORMATION_TYPE>
    ≔ ORIGIN<graphics/ORIGIN>
    ≔ PATH_PRIMITIVE_REMOVE_LOCATION<graphics/PATH_PRIMITIVE_REMOVE_LOCATION>
    ≔ PRIMITIVES_SORT_ORDER<graphics/PRIMITIVES_SORT_ORDER>
    ≔ REFRESH_RATE<graphics/REFRESH_RATE>
    ≔ RENDER_PASS<graphics/RENDER_PASS>
    ≔ RENDER_PASS_HINT<graphics/RENDER_PASS_HINT>
    ≔ SCREEN_OVERLAY_ORIGIN<graphics/SCREEN_OVERLAY_ORIGIN>
    ≔ SCREEN_OVERLAY_PINNING_ORIGIN<graphics/SCREEN_OVERLAY_PINNING_ORIGIN>
    ≔ SCREEN_OVERLAY_UNIT<graphics/SCREEN_OVERLAY_UNIT>
    ≔ SURFACE_MESH_RENDERING_METHOD<graphics/SURFACE_MESH_RENDERING_METHOD>
    ≔ VISIBILITY<graphics/VISIBILITY>
    ≔ ANTI_ALIASING<graphics/ANTI_ALIASING>
    ≔ BINARY_LOGIC_OPERATION<graphics/BINARY_LOGIC_OPERATION>
    ≔ BLUR_METHOD<graphics/BLUR_METHOD>
    ≔ EDGE_DETECT_METHOD<graphics/EDGE_DETECT_METHOD>
    ≔ FLIP_AXIS<graphics/FLIP_AXIS>
    ≔ GRADIENT_DETECT_METHOD<graphics/GRADIENT_DETECT_METHOD>
    ≔ JPEG2000_COMPRESSION_PROFILE<graphics/JPEG2000_COMPRESSION_PROFILE>
    ≔ RASTER_BAND<graphics/RASTER_BAND>
    ≔ RASTER_FORMAT<graphics/RASTER_FORMAT>
    ≔ RASTER_ORIENTATION<graphics/RASTER_ORIENTATION>
    ≔ RASTER_TYPE<graphics/RASTER_TYPE>
    ≔ SHARPEN_METHOD<graphics/SHARPEN_METHOD>
    ≔ VIDEO_PLAYBACK<graphics/VIDEO_PLAYBACK>
    ≔ KML_NETWORK_LINK_REFRESH_MODE<graphics/KML_NETWORK_LINK_REFRESH_MODE>
    ≔ KML_NETWORK_LINK_VIEW_REFRESH_MODE<graphics/KML_NETWORK_LINK_VIEW_REFRESH_MODE>
    ≔ MODEL_UP_AXIS<graphics/MODEL_UP_AXIS>
    ≔ OUTLINE_APPEARANCE<graphics/OUTLINE_APPEARANCE>
    ≔ POLYLINE_TYPE<graphics/POLYLINE_TYPE>
    ≔ CULL_FACE<graphics/CULL_FACE>
    ≔ INTERNAL_TEXTURE_FORMAT<graphics/INTERNAL_TEXTURE_FORMAT>
    ≔ MAGNIFICATION_FILTER<graphics/MAGNIFICATION_FILTER>
    ≔ MINIFICATION_FILTER<graphics/MINIFICATION_FILTER>
    ≔ RENDERER_SHADE_MODEL<graphics/RENDERER_SHADE_MODEL>
    ≔ TEXTURE_WRAP<graphics/TEXTURE_WRAP>
    ≔ SET_HINT<graphics/SET_HINT>
    ≔ STEREO_PROJECTION_MODE<graphics/STEREO_PROJECTION_MODE>
    ≔ STEREOSCOPIC_DISPLAY_MODE<graphics/STEREOSCOPIC_DISPLAY_MODE>
    ≔ FONT_STYLE<graphics/FONT_STYLE>

