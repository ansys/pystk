
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
        

            * - :py:class:`~ansys.stk.core.graphics.IPathPoint`
              - A path point used with the Path Primitive.

            * - :py:class:`~ansys.stk.core.graphics.IPathPointFactory`
              - Create Path Primitive's path points.

            * - :py:class:`~ansys.stk.core.graphics.IBoundingSphere`
              - A sphere that encapsulates an object.

            * - :py:class:`~ansys.stk.core.graphics.IBoundingSphereFactory`
              - Create instances of the bounding sphere type.

            * - :py:class:`~ansys.stk.core.graphics.ITextureFilter2D`
              - A texture filter.

            * - :py:class:`~ansys.stk.core.graphics.ITextureFilter2DFactory`
              - Create texture filters.

            * - :py:class:`~ansys.stk.core.graphics.IRendererTexture2D`
              - A 2D Texture. A texture represents an image that is ready for use by objects such as primitives and overlays. Textures typically reside in video memory.

            * - :py:class:`~ansys.stk.core.graphics.IRendererTextureTemplate2D`
              - Template object containing attributes required to create a 2D texture.

            * - :py:class:`~ansys.stk.core.graphics.IPathPointCollection`
              - A collection of path points.

            * - :py:class:`~ansys.stk.core.graphics.IObjectCollection`
              - A collection of objects.

            * - :py:class:`~ansys.stk.core.graphics.ISceneCollection`
              - A collection of scenes.

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayContainer`
              - The interface for screen overlays that contain a collection of other overlays. This interface is implemented by ScreenOverlayManager and ScreenOverlay.

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayPickResultCollection`
              - A collection of pick results.

            * - :py:class:`~ansys.stk.core.graphics.IGlobeImageOverlayAddCompleteEventArgs`
              - The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

            * - :py:class:`~ansys.stk.core.graphics.ITerrainOverlayAddCompleteEventArgs`
              - The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

            * - :py:class:`~ansys.stk.core.graphics.IPickResultCollection`
              - A collection of picked objects.

            * - :py:class:`~ansys.stk.core.graphics.IRenderingEventArgs`
              - The event is raised when the scene is rendered.

            * - :py:class:`~ansys.stk.core.graphics.IBatchPrimitiveIndex`
              - Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

            * - :py:class:`~ansys.stk.core.graphics.IKmlDocumentCollection`
              - A collection of KML documents.

            * - :py:class:`~ansys.stk.core.graphics.IKmlFeatureCollection`
              - A collection of KML features.

            * - :py:class:`~ansys.stk.core.graphics.IKmlDocumentLoadedEventArgs`
              - The event is raised when a KML document has been loaded.

            * - :py:class:`~ansys.stk.core.graphics.IFactoryAndInitializers`
              - Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

            * - :py:class:`~ansys.stk.core.graphics.IExtrudedPolylineTriangulatorResult`
              - The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.ISolidTriangulatorResult`
              - The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

            * - :py:class:`~ansys.stk.core.graphics.ISurfaceShapesResult`
              - Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

            * - :py:class:`~ansys.stk.core.graphics.ISurfaceTriangulatorResult`
              - The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

            * - :py:class:`~ansys.stk.core.graphics.ITriangulatorResult`
              - The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

            * - :py:class:`~ansys.stk.core.graphics.IAGICustomTerrainOverlay`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~ansys.stk.core.graphics.IAGIProcessedImageGlobeOverlay`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~ansys.stk.core.graphics.IAGIProcessedTerrainOverlay`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~ansys.stk.core.graphics.IAGIRoamImageGlobeOverlay`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~ansys.stk.core.graphics.ICameraSnapshot`
              - Takes snapshots of the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.ICameraVideoRecording`
              - Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

            * - :py:class:`~ansys.stk.core.graphics.ICentralBodyGraphicsIndexer`
              - An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

            * - :py:class:`~ansys.stk.core.graphics.ICustomImageGlobeOverlay`
              - A globe image overlay that allows for a user defined image to be specified.

            * - :py:class:`~ansys.stk.core.graphics.ICustomImageGlobeOverlayPluginActivator`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.ICustomImageGlobeOverlayPluginProxy`
              - A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

            * - :py:class:`~ansys.stk.core.graphics.IGeospatialImageGlobeOverlay`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~ansys.stk.core.graphics.IGlobeOverlay`
              - The base class of all terrain overlay and globe image overlay objects.

            * - :py:class:`~ansys.stk.core.graphics.IGlobeOverlaySettings`
              - Settings used by globe overlay objects. These setting affect all scenes.

            * - :py:class:`~ansys.stk.core.graphics.ILighting`
              - Lighting in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.IPathPrimitiveUpdatePolicy`
              - A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

            * - :py:class:`~ansys.stk.core.graphics.IProjectedRasterOverlay`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~ansys.stk.core.graphics.IProjection`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~ansys.stk.core.graphics.IProjectionStream`
              - A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

            * - :py:class:`~ansys.stk.core.graphics.ISceneGlobeOverlaySettings`
              - Settings used by globe overlay objects. These settings only affect the scene.

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayCollectionBase`
              - The common base class for collections of overlays held by screen overlay and by screen overlay manager.

            * - :py:class:`~ansys.stk.core.graphics.ITexture2DFactory`
              - A factory for creating texture 2d objects from various sources.

            * - :py:class:`~ansys.stk.core.graphics.IVisualEffects`
              - Control various post processing effects that can be applied to the scene.

            * - :py:class:`~ansys.stk.core.graphics.IAltitudeDisplayCondition`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~ansys.stk.core.graphics.IAxesPrimitive`
              - Render an axes in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.ICamera`
              - Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

            * - :py:class:`~ansys.stk.core.graphics.ICentralBodyGraphics`
              - The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

            * - :py:class:`~ansys.stk.core.graphics.IClouds`
              - Load, show and hide clouds in the scene.

            * - :py:class:`~ansys.stk.core.graphics.ICompositeDisplayCondition`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~ansys.stk.core.graphics.ICompositePrimitive`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~ansys.stk.core.graphics.IConstantDisplayCondition`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~ansys.stk.core.graphics.IDisplayCondition`
              - When assigned to objects, such as primitives or globe overlays, display conditions are evaluated to determine if the object should be rendered.

            * - :py:class:`~ansys.stk.core.graphics.IDistanceDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~ansys.stk.core.graphics.IDistanceToPrimitiveDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~ansys.stk.core.graphics.IDurationPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~ansys.stk.core.graphics.IFrameRate`
              - Keeps track of how many times the scenes are rendered per second.

            * - :py:class:`~ansys.stk.core.graphics.IGlobeImageOverlay`
              - A globe overlay that shows an image.

            * - :py:class:`~ansys.stk.core.graphics.IGraphicsFont`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~ansys.stk.core.graphics.IGreatArcInterpolator`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~ansys.stk.core.graphics.IImageCollection`
              - A collection of globe image overlay objects.

            * - :py:class:`~ansys.stk.core.graphics.IAlphaFromLuminanceFilter`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~ansys.stk.core.graphics.IAlphaFromPixelFilter`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~ansys.stk.core.graphics.IAlphaFromRasterFilter`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IBandExtractFilter`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~ansys.stk.core.graphics.IBandOrderFilter`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~ansys.stk.core.graphics.IBlurFilter`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~ansys.stk.core.graphics.IBrightnessFilter`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~ansys.stk.core.graphics.IColorToLuminanceFilter`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IContrastFilter`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~ansys.stk.core.graphics.IConvolutionFilter`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~ansys.stk.core.graphics.IEdgeDetectFilter`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IFilteringRasterStream`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~ansys.stk.core.graphics.IFlipFilter`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~ansys.stk.core.graphics.IGammaCorrectionFilter`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~ansys.stk.core.graphics.IGaussianBlurFilter`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~ansys.stk.core.graphics.IGradientDetectFilter`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.ILevelsFilter`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~ansys.stk.core.graphics.IProjectionRasterStreamPluginActivator`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.IProjectionRasterStreamPluginProxy`
              - A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

            * - :py:class:`~ansys.stk.core.graphics.IRaster`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~ansys.stk.core.graphics.IRasterAttributes`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~ansys.stk.core.graphics.IRasterFilter`
              - A filter for processing raster datasets. RasterFilter is the base class for all raster filters...

            * - :py:class:`~ansys.stk.core.graphics.IRasterStream`
              - A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

            * - :py:class:`~ansys.stk.core.graphics.IRotateFilter`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~ansys.stk.core.graphics.ISequenceFilter`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~ansys.stk.core.graphics.ISharpenFilter`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IVideoStream`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~ansys.stk.core.graphics.IKmlContainer`
              - A KmlContainer contains a collection of children kml features.

            * - :py:class:`~ansys.stk.core.graphics.IKmlDocument`
              - A KML document.

            * - :py:class:`~ansys.stk.core.graphics.IKmlFeature`
              - A KML feature.

            * - :py:class:`~ansys.stk.core.graphics.IKmlFolder`
              - A KML folder.

            * - :py:class:`~ansys.stk.core.graphics.IKmlGraphics`
              - Provide loading and unloading of kml documents for a particular central body.

            * - :py:class:`~ansys.stk.core.graphics.IKmlNetworkLink`
              - A KML network link.

            * - :py:class:`~ansys.stk.core.graphics.IMarkerBatchPrimitive`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~ansys.stk.core.graphics.IMarkerBatchPrimitiveOptionalParameters`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~ansys.stk.core.graphics.IModelArticulation`
              - A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~ansys.stk.core.graphics.IModelArticulationCollection`
              - A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~ansys.stk.core.graphics.IModelPrimitive`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~ansys.stk.core.graphics.IModelTransformation`
              - A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

            * - :py:class:`~ansys.stk.core.graphics.IOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.IPathPrimitive`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~ansys.stk.core.graphics.IPickResult`
              - A single result from Pick.

            * - :py:class:`~ansys.stk.core.graphics.IPixelSizeDisplayCondition`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~ansys.stk.core.graphics.IPointBatchPrimitive`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~ansys.stk.core.graphics.IPointBatchPrimitiveOptionalParameters`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.IPolylinePrimitive`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~ansys.stk.core.graphics.IPolylinePrimitiveOptionalParameters`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.IPositionInterpolator`
              - Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

            * - :py:class:`~ansys.stk.core.graphics.IPrimitive`
              - Primitives represent objects rendered in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.IPrimitiveManager`
              - The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

            * - :py:class:`~ansys.stk.core.graphics.IRasterImageGlobeOverlay`
              - A globe image overlay for handling rasters.

            * - :py:class:`~ansys.stk.core.graphics.IRhumbLineInterpolator`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~ansys.stk.core.graphics.IScene`
              - A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

            * - :py:class:`~ansys.stk.core.graphics.ISceneDisplayCondition`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~ansys.stk.core.graphics.ISceneManager`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayCollection`
              - A collection of screen overlays.

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayManager`
              - The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayPickResult`
              - Describes a picked screen overlay as a result of a call to pick screen overlays.

            * - :py:class:`~ansys.stk.core.graphics.ISolidPrimitive`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~ansys.stk.core.graphics.IStereoscopic`
              - Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :py:class:`~ansys.stk.core.graphics.ISurfaceMeshPrimitive`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~ansys.stk.core.graphics.ITerrainOverlayCollection`
              - A collection of terrain overlay objects.

            * - :py:class:`~ansys.stk.core.graphics.ITerrainOverlay`
              - A globe overlay which shows terrain.

            * - :py:class:`~ansys.stk.core.graphics.ITextBatchPrimitive`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~ansys.stk.core.graphics.ITextOverlay`
              - A rectangular overlay that contains text.

            * - :py:class:`~ansys.stk.core.graphics.ITextureMatrix`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~ansys.stk.core.graphics.ITextureScreenOverlay`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~ansys.stk.core.graphics.ITimeIntervalDisplayCondition`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~ansys.stk.core.graphics.ITriangleMeshPrimitive`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~ansys.stk.core.graphics.ITriangleMeshPrimitiveOptionalParameters`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.IVectorPrimitive`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

            * - :py:class:`~ansys.stk.core.graphics.IBoxTriangulatorInitializer`
              - Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ansys.stk.core.graphics.ICylinderTriangulatorInitializer`
              - Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ansys.stk.core.graphics.IEllipsoidTriangulatorInitializer`
              - Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ansys.stk.core.graphics.IExtrudedPolylineTriangulatorInitializer`
              - Triangulates a polyline into an extrusion with bottom and top boundaries.

            * - :py:class:`~ansys.stk.core.graphics.ISurfaceExtentTriangulatorInitializer`
              - Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

            * - :py:class:`~ansys.stk.core.graphics.ISurfacePolygonTriangulatorInitializer`
              - Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.ISurfaceShapesInitializer`
              - Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

            * - :py:class:`~ansys.stk.core.graphics.IAGICustomTerrainOverlayFactory`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~ansys.stk.core.graphics.IAGIProcessedImageGlobeOverlayFactory`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~ansys.stk.core.graphics.IAGIProcessedTerrainOverlayFactory`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~ansys.stk.core.graphics.IAGIRoamImageGlobeOverlayFactory`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~ansys.stk.core.graphics.ICustomImageGlobeOverlayPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.IGeospatialImageGlobeOverlayFactory`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~ansys.stk.core.graphics.IProjectedRasterOverlayFactory`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~ansys.stk.core.graphics.IProjectionFactory`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~ansys.stk.core.graphics.IAltitudeDisplayConditionFactory`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~ansys.stk.core.graphics.IAxesPrimitiveFactory`
              - Render an axes in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.ICompositeDisplayConditionFactory`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~ansys.stk.core.graphics.ICompositePrimitiveFactory`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~ansys.stk.core.graphics.IConstantDisplayConditionFactory`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~ansys.stk.core.graphics.IDistanceDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~ansys.stk.core.graphics.IDistanceToPositionDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~ansys.stk.core.graphics.IDistanceToPrimitiveDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~ansys.stk.core.graphics.IDurationPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~ansys.stk.core.graphics.IGlobeImageOverlayInitializer`
              - A globe overlay that shows an image.

            * - :py:class:`~ansys.stk.core.graphics.IGraphicsFontFactory`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~ansys.stk.core.graphics.IGreatArcInterpolatorFactory`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~ansys.stk.core.graphics.IAlphaFromLuminanceFilterFactory`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~ansys.stk.core.graphics.IAlphaFromPixelFilterFactory`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~ansys.stk.core.graphics.IAlphaFromRasterFilterFactory`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IBandExtractFilterFactory`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~ansys.stk.core.graphics.IBandOrderFilterFactory`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~ansys.stk.core.graphics.IBlurFilterFactory`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~ansys.stk.core.graphics.IBrightnessFilterFactory`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~ansys.stk.core.graphics.IColorToLuminanceFilterFactory`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IContrastFilterFactory`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~ansys.stk.core.graphics.IConvolutionFilterFactory`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~ansys.stk.core.graphics.IEdgeDetectFilterFactory`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IFilteringRasterStreamFactory`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~ansys.stk.core.graphics.IFlipFilterFactory`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~ansys.stk.core.graphics.IGammaCorrectionFilterFactory`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~ansys.stk.core.graphics.IGaussianBlurFilterFactory`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~ansys.stk.core.graphics.IGradientDetectFilterFactory`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IJpeg2000WriterInitializer`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

            * - :py:class:`~ansys.stk.core.graphics.ILevelsFilterFactory`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~ansys.stk.core.graphics.IProjectionRasterStreamPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.IRasterFactory`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~ansys.stk.core.graphics.IRasterAttributesFactory`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~ansys.stk.core.graphics.IRotateFilterFactory`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~ansys.stk.core.graphics.ISequenceFilterFactory`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~ansys.stk.core.graphics.ISharpenFilterFactory`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.IVideoStreamFactory`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~ansys.stk.core.graphics.IMarkerBatchPrimitiveFactory`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~ansys.stk.core.graphics.IMarkerBatchPrimitiveOptionalParametersFactory`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~ansys.stk.core.graphics.IMaximumCountPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~ansys.stk.core.graphics.IModelPrimitiveFactory`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~ansys.stk.core.graphics.IPathPrimitiveFactory`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~ansys.stk.core.graphics.IPixelSizeDisplayConditionFactory`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~ansys.stk.core.graphics.IPointBatchPrimitiveFactory`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~ansys.stk.core.graphics.IPointBatchPrimitiveOptionalParametersFactory`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.IPolylinePrimitiveFactory`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~ansys.stk.core.graphics.IPolylinePrimitiveOptionalParametersFactory`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.IRasterImageGlobeOverlayFactory`
              - A globe image overlay for handling rasters.

            * - :py:class:`~ansys.stk.core.graphics.IRhumbLineInterpolatorFactory`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~ansys.stk.core.graphics.ISceneDisplayConditionFactory`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~ansys.stk.core.graphics.ISceneManagerInitializer`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~ansys.stk.core.graphics.IScreenOverlayFactory`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.ISolidPrimitiveFactory`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~ansys.stk.core.graphics.ISurfaceMeshPrimitiveFactory`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~ansys.stk.core.graphics.ITerrainOverlayInitializer`
              - A globe overlay which shows terrain.

            * - :py:class:`~ansys.stk.core.graphics.ITextBatchPrimitiveFactory`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParametersFactory`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~ansys.stk.core.graphics.ITextOverlayFactory`
              - A rectangular overlay that contains text.

            * - :py:class:`~ansys.stk.core.graphics.ITextureMatrixFactory`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~ansys.stk.core.graphics.ITextureScreenOverlayFactory`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~ansys.stk.core.graphics.ITimeIntervalDisplayConditionFactory`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~ansys.stk.core.graphics.ITriangleMeshPrimitiveFactory`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~ansys.stk.core.graphics.ITriangleMeshPrimitiveOptionalParametersFactory`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.IVectorPrimitiveFactory`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

    
    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.graphics.PathPoint`
              - Represents a path point used in conjunction with the Path Primitive.

            * - :py:class:`~ansys.stk.core.graphics.PathPointFactory`
              - Factory creates path points.

            * - :py:class:`~ansys.stk.core.graphics.BoundingSphere`
              - A sphere that encapsulates an object.

            * - :py:class:`~ansys.stk.core.graphics.BoundingSphereFactory`
              - Create bounding spheres.

            * - :py:class:`~ansys.stk.core.graphics.TextureFilter2D`
              - A texture filter.

            * - :py:class:`~ansys.stk.core.graphics.TextureFilter2DFactory`
              - Create texture filters.

            * - :py:class:`~ansys.stk.core.graphics.RendererTexture2D`
              - A 2D Texture. A texture represents an image that is ready for use by objects such as primitives and overlays. Textures typically reside in video memory.

            * - :py:class:`~ansys.stk.core.graphics.RendererTextureTemplate2D`
              - Template object containing attributes required to create a 2D texture.

            * - :py:class:`~ansys.stk.core.graphics.PathPointCollection`
              - A collection of path points.

            * - :py:class:`~ansys.stk.core.graphics.ObjectCollection`
              - A collection of objects.

            * - :py:class:`~ansys.stk.core.graphics.SceneCollection`
              - A collection of scenes.

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlayPickResultCollection`
              - A collection of pick results.

            * - :py:class:`~ansys.stk.core.graphics.GlobeImageOverlayAddCompleteEventArgs`
              - The event is raised when the globe image overlay is displayed for the first time after being added using AddAsync.

            * - :py:class:`~ansys.stk.core.graphics.TerrainOverlayAddCompleteEventArgs`
              - The event is raised when the terrain overlay is displayed for the first time after having been added using AddAsync.

            * - :py:class:`~ansys.stk.core.graphics.PickResultCollection`
              - A collection of picked objects.

            * - :py:class:`~ansys.stk.core.graphics.RenderingEventArgs`
              - The event is raised when the scene is rendered.

            * - :py:class:`~ansys.stk.core.graphics.BatchPrimitiveIndex`
              - Represents an individual item index that is associated with a batch primitive. Provides the Index of the individual item and the Primitive that contains that index...

            * - :py:class:`~ansys.stk.core.graphics.KmlDocumentCollection`
              - A collection of KML documents.

            * - :py:class:`~ansys.stk.core.graphics.KmlFeatureCollection`
              - A collection of KML features.

            * - :py:class:`~ansys.stk.core.graphics.KmlDocumentLoadedEventArgs`
              - The event is raised when a KML document has been loaded.

            * - :py:class:`~ansys.stk.core.graphics.FactoryAndInitializers`
              - Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

            * - :py:class:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorResult`
              - The result from extruded polyline triangulation: a triangle mesh defined using an indexed triangle list with top and bottom boundary positions. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.SolidTriangulatorResult`
              - The result from a triangulation of a solid: a triangle mesh defined using an indexed triangle list and positions outlining the solid. It is recommended to visualize the solid using a solid primitive...

            * - :py:class:`~ansys.stk.core.graphics.SurfaceShapesResult`
              - Represents the boundary positions of a shape on the surface computed from by a surface shapes method.

            * - :py:class:`~ansys.stk.core.graphics.SurfaceTriangulatorResult`
              - The result from a triangulation on the surface of a central body: a triangle mesh defined using an indexed triangle list and boundary positions surrounding the mesh...

            * - :py:class:`~ansys.stk.core.graphics.TriangulatorResult`
              - The result from triangulation: a triangle mesh defined using an indexed triangle list. This is commonly visualized with the triangle mesh primitive or surface mesh primitive.

            * - :py:class:`~ansys.stk.core.graphics.AGICustomTerrainOverlay`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~ansys.stk.core.graphics.AGIProcessedImageGlobeOverlay`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~ansys.stk.core.graphics.AGIProcessedTerrainOverlay`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~ansys.stk.core.graphics.AGIRoamImageGlobeOverlay`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~ansys.stk.core.graphics.CameraSnapshot`
              - Takes snapshots of the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.CameraVideoRecording`
              - Records the 3D window to either a movie file or to consecutively ordered image files each time the scene is rendered.

            * - :py:class:`~ansys.stk.core.graphics.CentralBodyGraphicsIndexer`
              - An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

            * - :py:class:`~ansys.stk.core.graphics.CustomImageGlobeOverlay`
              - A globe image overlay that allows for a user defined image to be specified.

            * - :py:class:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivator`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy`
              - A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

            * - :py:class:`~ansys.stk.core.graphics.GeospatialImageGlobeOverlay`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~ansys.stk.core.graphics.GlobeOverlay`
              - The base class of all terrain overlay and globe image overlay objects.

            * - :py:class:`~ansys.stk.core.graphics.GlobeOverlaySettings`
              - Settings used by globe overlay objects. These setting affect all scenes.

            * - :py:class:`~ansys.stk.core.graphics.Lighting`
              - Lighting in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.PathPrimitiveUpdatePolicy`
              - A class that encapsulates the update logic for a path primitive. Derived classes must implement the Update method.

            * - :py:class:`~ansys.stk.core.graphics.ProjectedRasterOverlay`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~ansys.stk.core.graphics.Projection`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~ansys.stk.core.graphics.ProjectionStream`
              - A projection that is updated dynamically at the specified update delta. The class can be used to stream projection data to projection clients, like projected raster overlay...

            * - :py:class:`~ansys.stk.core.graphics.SceneGlobeOverlaySettings`
              - Settings used by globe overlay objects. These settings only affect the scene.

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlayCollectionBase`
              - The common base class for collections of overlays held by screen overlay and by screen overlay manager.

            * - :py:class:`~ansys.stk.core.graphics.Texture2DFactory`
              - A factory for creating texture 2d objects from various sources.

            * - :py:class:`~ansys.stk.core.graphics.VisualEffects`
              - Control various post processing effects that can be applied to the scene.

            * - :py:class:`~ansys.stk.core.graphics.AltitudeDisplayCondition`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~ansys.stk.core.graphics.AxesPrimitive`
              - Render an axes in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.Camera`
              - Implemented by the scene camera. Contains operations to manipulate the camera position, view direction and orientation in the scene.

            * - :py:class:`~ansys.stk.core.graphics.CentralBodyGraphics`
              - The graphical properties associated with a particular central body. Changing the central body graphics will affect how the associated central body is rendered in a scene. For instance, to show or hide the central body, use the show property...

            * - :py:class:`~ansys.stk.core.graphics.Clouds`
              - Load, show and hide clouds in the scene.

            * - :py:class:`~ansys.stk.core.graphics.CompositeDisplayCondition`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~ansys.stk.core.graphics.CompositePrimitive`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~ansys.stk.core.graphics.ConstantDisplayCondition`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~ansys.stk.core.graphics.DisplayCondition`
              - When assigned to objects, such as primitives or globe overlays, display conditions are evaluated to determine if the object should be rendered.

            * - :py:class:`~ansys.stk.core.graphics.DistanceDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~ansys.stk.core.graphics.FrameRate`
              - Keeps track of how many times the scenes are rendered per second.

            * - :py:class:`~ansys.stk.core.graphics.GlobeImageOverlay`
              - A globe overlay that shows an image.

            * - :py:class:`~ansys.stk.core.graphics.GraphicsFont`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~ansys.stk.core.graphics.GreatArcInterpolator`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~ansys.stk.core.graphics.ImageCollection`
              - A collection of globe image overlay objects.

            * - :py:class:`~ansys.stk.core.graphics.AlphaFromLuminanceFilter`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~ansys.stk.core.graphics.AlphaFromPixelFilter`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~ansys.stk.core.graphics.AlphaFromRasterFilter`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~ansys.stk.core.graphics.BandExtractFilter`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~ansys.stk.core.graphics.BandOrderFilter`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~ansys.stk.core.graphics.BlurFilter`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~ansys.stk.core.graphics.BrightnessFilter`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~ansys.stk.core.graphics.ColorToLuminanceFilter`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.ContrastFilter`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~ansys.stk.core.graphics.ConvolutionFilter`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~ansys.stk.core.graphics.EdgeDetectFilter`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.FilteringRasterStream`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~ansys.stk.core.graphics.FlipFilter`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~ansys.stk.core.graphics.GammaCorrectionFilter`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~ansys.stk.core.graphics.GaussianBlurFilter`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~ansys.stk.core.graphics.GradientDetectFilter`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.LevelsFilter`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginActivator`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginProxy`
              - A proxy class provides access to the raster and projection streams implemented by a plugin. Proxies are instantiated using projection raster stream plugin activator.

            * - :py:class:`~ansys.stk.core.graphics.Raster`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~ansys.stk.core.graphics.RasterAttributes`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~ansys.stk.core.graphics.RasterFilter`
              - A filter for processing raster datasets. RasterFilter is the base class for all raster filters...

            * - :py:class:`~ansys.stk.core.graphics.RasterStream`
              - A raster, the data of which, is updated dynamically at the specified update delta. The class can be used to stream video and other dynamic raster data to textures and other raster clients...

            * - :py:class:`~ansys.stk.core.graphics.RotateFilter`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~ansys.stk.core.graphics.SequenceFilter`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~ansys.stk.core.graphics.SharpenFilter`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.VideoStream`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~ansys.stk.core.graphics.KmlContainer`
              - A KmlContainer contains a collection of children kml features.

            * - :py:class:`~ansys.stk.core.graphics.KmlDocument`
              - A KML document.

            * - :py:class:`~ansys.stk.core.graphics.KmlFeature`
              - A KML feature.

            * - :py:class:`~ansys.stk.core.graphics.KmlFolder`
              - A KML folder.

            * - :py:class:`~ansys.stk.core.graphics.KmlGraphics`
              - Provide loading and unloading of kml documents for a particular central body.

            * - :py:class:`~ansys.stk.core.graphics.KmlNetworkLink`
              - A KML network link.

            * - :py:class:`~ansys.stk.core.graphics.MarkerBatchPrimitive`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~ansys.stk.core.graphics.MarkerBatchPrimitiveOptionalParameters`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicy`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~ansys.stk.core.graphics.ModelArticulation`
              - A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~ansys.stk.core.graphics.ModelArticulationCollection`
              - A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

            * - :py:class:`~ansys.stk.core.graphics.ModelPrimitive`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~ansys.stk.core.graphics.ModelTransformation`
              - A model transformation defines a transformation that is applied to geometry on a model primitive. That geometry is identified by the model articulation which contains the transformation...

            * - :py:class:`~ansys.stk.core.graphics.Overlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.PathPrimitive`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~ansys.stk.core.graphics.PickResult`
              - A single result from Pick.

            * - :py:class:`~ansys.stk.core.graphics.PixelSizeDisplayCondition`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~ansys.stk.core.graphics.PointBatchPrimitive`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~ansys.stk.core.graphics.PointBatchPrimitiveOptionalParameters`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.PolylinePrimitive`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~ansys.stk.core.graphics.PolylinePrimitiveOptionalParameters`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.PositionInterpolator`
              - Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

            * - :py:class:`~ansys.stk.core.graphics.Primitive`
              - Primitives represent objects rendered in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.PrimitiveManager`
              - The primitive manager contains spatial data structures used to efficiently render primitives. Once a primitive is constructed, it must be added to the primitive manager before it will be rendered.

            * - :py:class:`~ansys.stk.core.graphics.RasterImageGlobeOverlay`
              - A globe image overlay for handling rasters.

            * - :py:class:`~ansys.stk.core.graphics.RhumbLineInterpolator`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~ansys.stk.core.graphics.Scene`
              - A scene provides properties and functionality that are reflected in the rendering of the globe control that it is associated with. An globe control's scene is available from the scene property...

            * - :py:class:`~ansys.stk.core.graphics.SceneDisplayCondition`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~ansys.stk.core.graphics.SceneManager`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlay`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlayCollection`
              - A collection of screen overlays.

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlayManager`
              - The top-level container for screen overlays. All child screen overlays that are added to this container are specified relative to the overall globe control.

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlayPickResult`
              - Describes a picked screen overlay as a result of a call to pick screen overlays.

            * - :py:class:`~ansys.stk.core.graphics.SolidPrimitive`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~ansys.stk.core.graphics.Stereoscopic`
              - Get the stereoscopic options for all Scenes. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :py:class:`~ansys.stk.core.graphics.SurfaceMeshPrimitive`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~ansys.stk.core.graphics.TerrainOverlayCollection`
              - A collection of terrain overlay objects.

            * - :py:class:`~ansys.stk.core.graphics.TerrainOverlay`
              - A globe overlay which shows terrain.

            * - :py:class:`~ansys.stk.core.graphics.TextBatchPrimitive`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~ansys.stk.core.graphics.TextBatchPrimitiveOptionalParameters`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~ansys.stk.core.graphics.TextOverlay`
              - A rectangular overlay that contains text.

            * - :py:class:`~ansys.stk.core.graphics.TextureMatrix`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~ansys.stk.core.graphics.TextureScreenOverlay`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~ansys.stk.core.graphics.TimeIntervalDisplayCondition`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~ansys.stk.core.graphics.TriangleMeshPrimitive`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~ansys.stk.core.graphics.TriangleMeshPrimitiveOptionalParameters`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.VectorPrimitive`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.

            * - :py:class:`~ansys.stk.core.graphics.BoxTriangulatorInitializer`
              - Triangulates a box. It is recommended to visualize the box using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ansys.stk.core.graphics.CylinderTriangulatorInitializer`
              - Triangulates a cylinder. It is recommended to visualize the cylinder using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ansys.stk.core.graphics.EllipsoidTriangulatorInitializer`
              - Triangulates an ellipsoid. It is recommended to visualize the ellipsoid using a solid primitive. Although, if only the fill is desired for visualization, a triangle mesh primitive with render back then front faces set to true can be used...

            * - :py:class:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer`
              - Triangulates a polyline into an extrusion with bottom and top boundaries.

            * - :py:class:`~ansys.stk.core.graphics.SurfaceExtentTriangulatorInitializer`
              - Triangulates an extent on a central body into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive. The boundary is commonly visualized with the polyline primitive.

            * - :py:class:`~ansys.stk.core.graphics.SurfacePolygonTriangulatorInitializer`
              - Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.SurfaceShapesInitializer`
              - Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

            * - :py:class:`~ansys.stk.core.graphics.AGICustomTerrainOverlayFactory`
              - A terrain overlay for handling AGI Cesium Terrain.

            * - :py:class:`~ansys.stk.core.graphics.AGIProcessedImageGlobeOverlayFactory`
              - A globe image overlay for handling AGI Processed Image (PDTTX) files.

            * - :py:class:`~ansys.stk.core.graphics.AGIProcessedTerrainOverlayFactory`
              - A terrain overlay for handling AGI Processed Terrain (PDTT) files.

            * - :py:class:`~ansys.stk.core.graphics.AGIRoamImageGlobeOverlayFactory`
              - A globe image overlay for handling ROAM (TXM/TXB) files.

            * - :py:class:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.GeospatialImageGlobeOverlayFactory`
              - A globe image overlay for handling `JPEG 2000 <https://jpeg.org/jpeg2000/>`_ (.jp2), ECW (.ecw), ECWP, and MrSid (.sid) image formats in the WGS84 geographic projection.

            * - :py:class:`~ansys.stk.core.graphics.ProjectedRasterOverlayFactory`
              - A globe image overlay which projects a raster onto the terrain or surface of the central body. You can also enable projection onto models by setting projected raster model projection to true for a Scene...

            * - :py:class:`~ansys.stk.core.graphics.ProjectionFactory`
              - A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

            * - :py:class:`~ansys.stk.core.graphics.AltitudeDisplayConditionFactory`
              - Define an inclusive altitude interval that determines when an object is rendered based on the camera's altitude relative to a central body.

            * - :py:class:`~ansys.stk.core.graphics.AxesPrimitiveFactory`
              - Render an axes in the 3D scene.

            * - :py:class:`~ansys.stk.core.graphics.CompositeDisplayConditionFactory`
              - A composite of display conditions combined using a binary logic operation. For example, several time interval display condition objects can be added to a composite...

            * - :py:class:`~ansys.stk.core.graphics.CompositePrimitiveFactory`
              - A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

            * - :py:class:`~ansys.stk.core.graphics.ConstantDisplayConditionFactory`
              - A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

            * - :py:class:`~ansys.stk.core.graphics.DistanceDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

            * - :py:class:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

            * - :py:class:`~ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

            * - :py:class:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayConditionFactory`
              - Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

            * - :py:class:`~ansys.stk.core.graphics.DurationPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location after a given duration.

            * - :py:class:`~ansys.stk.core.graphics.GlobeImageOverlayInitializer`
              - A globe overlay that shows an image.

            * - :py:class:`~ansys.stk.core.graphics.GraphicsFontFactory`
              - A font that is suitable for use with the text batch primitive. For best performance, avoid creating duplicate font objects. Instead assign the same font object to several text batch primitives.

            * - :py:class:`~ansys.stk.core.graphics.GreatArcInterpolatorFactory`
              - The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

            * - :py:class:`~ansys.stk.core.graphics.AlphaFromLuminanceFilterFactory`
              - Add an alpha band to the source raster derived from the luminance of the raster's color bands.

            * - :py:class:`~ansys.stk.core.graphics.AlphaFromPixelFilterFactory`
              - Add an alpha band to the source raster based on the value of its first pixel. All pixels in the source raster that are the same color as the first pixel will be made transparent.

            * - :py:class:`~ansys.stk.core.graphics.AlphaFromRasterFilterFactory`
              - Add an alpha band to the source raster derived from the color bands or alpha of another raster. This filter can be used to apply an alpha mask to the source raster.

            * - :py:class:`~ansys.stk.core.graphics.BandExtractFilterFactory`
              - Extract a band or set of bands from the source raster. The extract format property specifies the bands and the order of the bands that will be extracted.

            * - :py:class:`~ansys.stk.core.graphics.BandOrderFilterFactory`
              - Reorders or swizzles the bands of the source raster to match the band order of the raster format specified by the band order property. When maintain raster format is true, the source raster's format is maintained after swizzling.

            * - :py:class:`~ansys.stk.core.graphics.BlurFilterFactory`
              - Apply a convolution filter to blur or smooth the source raster. Can be used to reduce noise in the raster.

            * - :py:class:`~ansys.stk.core.graphics.BrightnessFilterFactory`
              - Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

            * - :py:class:`~ansys.stk.core.graphics.ColorToLuminanceFilterFactory`
              - Extract a luminance band derived from the color bands of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.ContrastFilterFactory`
              - Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

            * - :py:class:`~ansys.stk.core.graphics.ConvolutionFilterFactory`
              - Apply convolution to the source raster. Convolution is the modification of a pixel's value based on the values of its surrounding pixels. The kernel is the numerical matrix that is applied to each pixel in this process...

            * - :py:class:`~ansys.stk.core.graphics.EdgeDetectFilterFactory`
              - Apply a convolution filter to detect edges in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.FilteringRasterStreamFactory`
              - A class decorator for applying a raster filter to each update of a raster stream. Can be used to apply filters to videos and other raster streams as they are updated.

            * - :py:class:`~ansys.stk.core.graphics.FlipFilterFactory`
              - Flips the source raster along the given flip axis.

            * - :py:class:`~ansys.stk.core.graphics.GammaCorrectionFilterFactory`
              - Apply gamma correction to the source raster. The gamma is a value between .2 and 5. The default gamma value is 2.2.

            * - :py:class:`~ansys.stk.core.graphics.GaussianBlurFilterFactory`
              - Apply a convolution filter to blur the source raster using the Gaussian function.

            * - :py:class:`~ansys.stk.core.graphics.GradientDetectFilterFactory`
              - Apply a convolution filter to detect gradients in the source raster.

            * - :py:class:`~ansys.stk.core.graphics.Jpeg2000WriterInitializer`
              - Convert an image, such as a BMP, to a GeoJP2 file that can be used as an image globe overlay.

            * - :py:class:`~ansys.stk.core.graphics.LevelsFilterFactory`
              - Adjusts the band levels of the source raster linearly.

            * - :py:class:`~ansys.stk.core.graphics.ProjectionRasterStreamPluginActivatorFactory`
              - The Activator class provides methods to load COM plugins that implement projection and raster streaming. For more information about the projection and raster plugins, see the STK Programming Interface.

            * - :py:class:`~ansys.stk.core.graphics.RasterFactory`
              - A raster dataset. A raster consists of one or more bands, or sets of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~ansys.stk.core.graphics.RasterAttributesFactory`
              - The attributes describing a raster dataset. raster attributes define the memory layout of a raster, and includes properties defining the order of each raster band that the raster contains, as specified by the raster format...

            * - :py:class:`~ansys.stk.core.graphics.RotateFilterFactory`
              - Rotate the source raster clockwise by the specified angle.

            * - :py:class:`~ansys.stk.core.graphics.SequenceFilterFactory`
              - Apply a sequence of filters to the source raster in the order in which they were added. When continue on failure is set to true, subsequent filters will still be applied to the source raster even if one or more filters in the sequence cannot be applied.

            * - :py:class:`~ansys.stk.core.graphics.SharpenFilterFactory`
              - Apply a convolution filter to increase the sharpness of the source raster.

            * - :py:class:`~ansys.stk.core.graphics.VideoStreamFactory`
              - A raster stream that streams from a video. The video can be read from a file, or streamed from an HTTP, RTP, UDP, or TCP source. See the Video Streams Overview for a list of supported video formats and Uri usage.

            * - :py:class:`~ansys.stk.core.graphics.MarkerBatchPrimitiveFactory`
              - Render one or more markers in the 3D scene. Markers are 2D images that always face the viewer which can be sized in pixels or meters. Markers are also referred to as sprites or billboards...

            * - :py:class:`~ansys.stk.core.graphics.MarkerBatchPrimitiveOptionalParametersFactory`
              - Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

            * - :py:class:`~ansys.stk.core.graphics.MaximumCountPathPrimitiveUpdatePolicyFactory`
              - path primitive update policy that removes points from remove location when the number of points in the path exceeds maximum count.

            * - :py:class:`~ansys.stk.core.graphics.ModelPrimitiveFactory`
              - The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

            * - :py:class:`~ansys.stk.core.graphics.PathPrimitiveFactory`
              - Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

            * - :py:class:`~ansys.stk.core.graphics.PixelSizeDisplayConditionFactory`
              - Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

            * - :py:class:`~ansys.stk.core.graphics.PointBatchPrimitiveFactory`
              - Render one or more points in the 3D scene. Each point in the batch has a unique position and an optional color. All points in the batch share the same pixel size. For best performance, avoid creating lots of batches with only a few points each...

            * - :py:class:`~ansys.stk.core.graphics.PointBatchPrimitiveOptionalParametersFactory`
              - Optional per-point parameters for point batch primitive that overrides the point batch primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.PolylinePrimitiveFactory`
              - Render a polyline in the 3D scene. Each line segment may have a different color. A polyline can be constructed with a position interpolator to render great arcs or rhumb lines.

            * - :py:class:`~ansys.stk.core.graphics.PolylinePrimitiveOptionalParametersFactory`
              - Optional per-point or per-segment parameters for polyline primitive that overrides the polyline primitive's global parameters...

            * - :py:class:`~ansys.stk.core.graphics.RasterImageGlobeOverlayFactory`
              - A globe image overlay for handling rasters.

            * - :py:class:`~ansys.stk.core.graphics.RhumbLineInterpolatorFactory`
              - The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

            * - :py:class:`~ansys.stk.core.graphics.SceneDisplayConditionFactory`
              - A display condition used to control what scene or scenes an object, such as a primitive, is rendered in. This is used to show an object in some scenes and hide it in others.

            * - :py:class:`~ansys.stk.core.graphics.SceneManagerInitializer`
              - The static scene manager class provides global properties and functionality that apply to all scenes and thus affect the rendering of every globe control...

            * - :py:class:`~ansys.stk.core.graphics.ScreenOverlayFactory`
              - A visible element drawn in screen space. Overlays are useful for floating logos, heads up displays, and integrating user interfaces into the 3D window.

            * - :py:class:`~ansys.stk.core.graphics.SolidPrimitiveFactory`
              - Render filled solid objects and their outlines. Example solids include boxes and ellipsoids. Various effects are supported, such as displaying the solid's silhouette, and hiding the outline of the backside of the solid...

            * - :py:class:`~ansys.stk.core.graphics.SurfaceMeshPrimitiveFactory`
              - A triangle mesh primitive for meshes on the surface that need to conform to terrain.

            * - :py:class:`~ansys.stk.core.graphics.TerrainOverlayInitializer`
              - A globe overlay which shows terrain.

            * - :py:class:`~ansys.stk.core.graphics.TextBatchPrimitiveFactory`
              - Render one or more strings in the 3D scene. For best performance, avoid creating lots of batches with only a few strings each. See the Batching Performance Overview.

            * - :py:class:`~ansys.stk.core.graphics.TextBatchPrimitiveOptionalParametersFactory`
              - Optional per-string and per-batch parameters for text batch primitive...

            * - :py:class:`~ansys.stk.core.graphics.TextOverlayFactory`
              - A rectangular overlay that contains text.

            * - :py:class:`~ansys.stk.core.graphics.TextureMatrixFactory`
              - A 4 by 4 matrix applied to a texture coordinate.

            * - :py:class:`~ansys.stk.core.graphics.TextureScreenOverlayFactory`
              - A rectangular overlay that can be assigned a texture.

            * - :py:class:`~ansys.stk.core.graphics.TimeIntervalDisplayConditionFactory`
              - Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

            * - :py:class:`~ansys.stk.core.graphics.TriangleMeshPrimitiveFactory`
              - Render a triangle mesh in the 3D scene. Examples of triangle meshes include polygons on the globe (e.g. states or countries), terrain and imagery extents, ellipses, and extrusions.

            * - :py:class:`~ansys.stk.core.graphics.TriangleMeshPrimitiveOptionalParametersFactory`
              - Optional parameters for triangle mesh primitive...

            * - :py:class:`~ansys.stk.core.graphics.VectorPrimitiveFactory`
              - Render a vector in the 3D scene. A vector is defined by a source (given by a reference frame) and a direction (given by a vector). Length is auto-calculated or can be set separately.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto
        

            * - :py:class:`~ansys.stk.core.graphics.CYLINDER_FILL`
              - Cylinder faces that can be filled.

            * - :py:class:`~ansys.stk.core.graphics.WINDING_ORDER`
              - Specify the order for positions or front facing triangles. Winding order is important for triangulation and backface culling.

            * - :py:class:`~ansys.stk.core.graphics.CAMERA_SNAPSHOT_FILE_FORMAT`
              - When using camera snapshot or camera video recording to save a snapshot to a file, this specifies the file format.

            * - :py:class:`~ansys.stk.core.graphics.CAMERA_VIDEO_FORMAT`
              - When using camera video recording to record a video, this specifies the file format.

            * - :py:class:`~ansys.stk.core.graphics.CONSTRAINED_UP_AXIS`
              - When setting the camera'saxes, this defines which axis of the axes is up in screen space, where up is from the bottom to the top of the screen.

            * - :py:class:`~ansys.stk.core.graphics.GLOBE_OVERLAY_ROLE`
              - The role of a globe overlay.

            * - :py:class:`~ansys.stk.core.graphics.INDICES_ORDER_HINT`
              - An optimization hint optionally provided to a primitive'sSetPartial method to enhance performance.

            * - :py:class:`~ansys.stk.core.graphics.MAINTAIN_ASPECT_RATIO`
              - Specify whether the aspect ratio of a texture will be maintained during sizing of a screen overlay.

            * - :py:class:`~ansys.stk.core.graphics.MAP_PROJECTION`
              - The projection of the pixel data returned from a custom image globe overlay.

            * - :py:class:`~ansys.stk.core.graphics.MARKER_BATCH_RENDERING_METHOD`
              - Rendering methods available for use by the marker batch primitive. Different methods may have different performance characteristics and require different video card support. When in doubt, use Automatic.

            * - :py:class:`~ansys.stk.core.graphics.MARKER_BATCH_RENDER_PASS`
              - The pass during which the marker batch is rendered.

            * - :py:class:`~ansys.stk.core.graphics.MARKER_BATCH_SIZE_SOURCE`
              - Determine which marker batch property is used to size each marker in a marker batch.

            * - :py:class:`~ansys.stk.core.graphics.MARKER_BATCH_SORT_ORDER`
              - The order in which markers in a marker batch are sorted before rendering.

            * - :py:class:`~ansys.stk.core.graphics.MARKER_BATCH_UNIT`
              - The unit for marker sizes in a marker batch.

            * - :py:class:`~ansys.stk.core.graphics.MODEL_TRANSFORMATION_TYPE`
              - Transformation types that define the way a model transformation changes the geometry of the model articulation it is associated with.

            * - :py:class:`~ansys.stk.core.graphics.ORIGIN`
              - Vertical and horizontal origin.

            * - :py:class:`~ansys.stk.core.graphics.PATH_PRIMITIVE_REMOVE_LOCATION`
              - Represents the location of a point to be removed.

            * - :py:class:`~ansys.stk.core.graphics.PRIMITIVES_SORT_ORDER`
              - The order in which primitives are sorted before rendering.

            * - :py:class:`~ansys.stk.core.graphics.REFRESH_RATE`
              - The rate at which animation frames will occur.

            * - :py:class:`~ansys.stk.core.graphics.RENDER_PASS`
              - Describes when a primitive will be rendered. Some primitives need to be rendered during or at a certain time. For example, translucent primitives need to be rendered after opaque primitives to allow proper blending...

            * - :py:class:`~ansys.stk.core.graphics.RENDER_PASS_HINT`
              - An optimization hint optionally provided to a primitive'sSet method to enhance performance when per-position colors are used.

            * - :py:class:`~ansys.stk.core.graphics.SCREEN_OVERLAY_ORIGIN`
              - Specify the origin of a screen overlay, as well as the direction of the horizontal and vertical axes. The origin specifies both the origin in the parent overlay's coordinate system and the origin within the overlay itself that is positioned.

            * - :py:class:`~ansys.stk.core.graphics.SCREEN_OVERLAY_PINNING_ORIGIN`
              - Specify the origin of the pinning position of the screen overlay, as well as the direction of the horizontal and vertical axes for that pinning position. The pinning origin specifies the origin of the pinning position in the overlay's coordinate system.

            * - :py:class:`~ansys.stk.core.graphics.SCREEN_OVERLAY_UNIT`
              - A unit specifying how a screen overlay is sized and positioned relative to its parent.

            * - :py:class:`~ansys.stk.core.graphics.SURFACE_MESH_RENDERING_METHOD`
              - Rendering methods available for use by the surface mesh primitive. Different methods may have different performance characteristics and require different video card support. When in doubt, use Automatic.

            * - :py:class:`~ansys.stk.core.graphics.VISIBILITY`
              - Result of a visibility test, such as testing if a sphere intersects a frustum.

            * - :py:class:`~ansys.stk.core.graphics.ANTI_ALIASING`
              - The multisample anti-aliasing (MSAA) options for Scenes. As the level of anti-aliasing increases, performance will generally decrease, but the quality of the anti-aliasing will improve.

            * - :py:class:`~ansys.stk.core.graphics.BINARY_LOGIC_OPERATION`
              - Binary logic operations that can be used by composite display condition.

            * - :py:class:`~ansys.stk.core.graphics.BLUR_METHOD`
              - The method used to blur or smooth a raster.

            * - :py:class:`~ansys.stk.core.graphics.EDGE_DETECT_METHOD`
              - The method used to detect edges in a raster.

            * - :py:class:`~ansys.stk.core.graphics.FLIP_AXIS`
              - The axis on which a raster will be flipped.

            * - :py:class:`~ansys.stk.core.graphics.GRADIENT_DETECT_METHOD`
              - The method used to detect gradients in a raster. Gradient detection is commonly referred to as embossing.

            * - :py:class:`~ansys.stk.core.graphics.JPEG2000_COMPRESSION_PROFILE`
              - Define the profile used when encoding a JPEG 2000 file.

            * - :py:class:`~ansys.stk.core.graphics.RASTER_BAND`
              - Common band types that may be contained within a raster dataset. Each band can be thought of as a set of values, which are most commonly associated with colors when the raster represents an image...

            * - :py:class:`~ansys.stk.core.graphics.RASTER_FORMAT`
              - Common raster band layouts that may be contained within a raster dataset. Each pixel of the raster will contain the bands defined by the layout in the specified order. A typical color raster image will have an rgbraster format.

            * - :py:class:`~ansys.stk.core.graphics.RASTER_ORIENTATION`
              - The vertical orientation of the raster.

            * - :py:class:`~ansys.stk.core.graphics.RASTER_TYPE`
              - The type of data contained within each band of a raster dataset.

            * - :py:class:`~ansys.stk.core.graphics.SHARPEN_METHOD`
              - The method used to sharpen a raster.

            * - :py:class:`~ansys.stk.core.graphics.VIDEO_PLAYBACK`
              - Specify how the video stream will playback. When the playback is set to real time, the video will playback in real time...

            * - :py:class:`~ansys.stk.core.graphics.KML_NETWORK_LINK_REFRESH_MODE`
              - Define the options available for a KmlNetworkLink's RefreshMode property.

            * - :py:class:`~ansys.stk.core.graphics.KML_NETWORK_LINK_VIEW_REFRESH_MODE`
              - Define the options available for a KmlNetworkLink's ViewRefreshMode property.

            * - :py:class:`~ansys.stk.core.graphics.MODEL_UP_AXIS`
              - When setting the camera'saxes, this defines which axis of the axes is up in screen space, where up is from the bottom to the top of the screen.

            * - :py:class:`~ansys.stk.core.graphics.OUTLINE_APPEARANCE`
              - Possible appearances of an outline. Front lines are lines on front facing geometry and back lines are lines on back facing geometry.

            * - :py:class:`~ansys.stk.core.graphics.POLYLINE_TYPE`
              - Describes how to interpret positions defining a polyline.

            * - :py:class:`~ansys.stk.core.graphics.CULL_FACE`
              - Identifies whether front- and/or back-facing triangles are culled.

            * - :py:class:`~ansys.stk.core.graphics.INTERNAL_TEXTURE_FORMAT`
              - The format of individual texels in a texture.

            * - :py:class:`~ansys.stk.core.graphics.MAGNIFICATION_FILTER`
              - The filter used when the pixel being textured maps to an area less than or equal to one texel.

            * - :py:class:`~ansys.stk.core.graphics.MINIFICATION_FILTER`
              - The filter used when the pixel being textured maps to an area greater than one texel.

            * - :py:class:`~ansys.stk.core.graphics.RENDERER_SHADE_MODEL`
              - Identifies which shade model to use. The primitive can be drawn with a single color or multiple colors.

            * - :py:class:`~ansys.stk.core.graphics.TEXTURE_WRAP`
              - Determine how to handle textures coordinates that fall outside of the range [0, 1].

            * - :py:class:`~ansys.stk.core.graphics.SET_HINT`
              - An optimization hint optionally provided to primitives to enhance performance for static or dynamic primitives. See the Set Hint Performance Overview for selecting an appropriate value.

            * - :py:class:`~ansys.stk.core.graphics.STEREO_PROJECTION_MODE`
              - The stereoscopic projection mode used for the left and right eye scenes.

            * - :py:class:`~ansys.stk.core.graphics.STEREOSCOPIC_DISPLAY_MODE`
              - The stereoscopic display mode. To use a particular stereoscopic display mode, ensure that your system supports the feature and that it is enabled.

            * - :py:class:`~ansys.stk.core.graphics.FONT_STYLE`
              - Font styles.



Description
-----------

Access and manipulate visual elements in STK.

These include STK globe terrain
and imagery, camera control, 3D models, triangle meshes, surface polygons and
polylines, text batches, screen overlays, scene lighting, and raster and
projection streaming. STK Graphics is available in STK, using UI plugins, as
well as in STK Engine custom applications.


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

    ≔ CYLINDER_FILL<graphics/CYLINDER_FILL_enum>
    ≔ WINDING_ORDER<graphics/WINDING_ORDER_enum>
    ≔ CAMERA_SNAPSHOT_FILE_FORMAT<graphics/CAMERA_SNAPSHOT_FILE_FORMAT_enum>
    ≔ CAMERA_VIDEO_FORMAT<graphics/CAMERA_VIDEO_FORMAT_enum>
    ≔ CONSTRAINED_UP_AXIS<graphics/CONSTRAINED_UP_AXIS_enum>
    ≔ GLOBE_OVERLAY_ROLE<graphics/GLOBE_OVERLAY_ROLE_enum>
    ≔ INDICES_ORDER_HINT<graphics/INDICES_ORDER_HINT_enum>
    ≔ MAINTAIN_ASPECT_RATIO<graphics/MAINTAIN_ASPECT_RATIO_enum>
    ≔ MAP_PROJECTION<graphics/MAP_PROJECTION_enum>
    ≔ MARKER_BATCH_RENDERING_METHOD<graphics/MARKER_BATCH_RENDERING_METHOD_enum>
    ≔ MARKER_BATCH_RENDER_PASS<graphics/MARKER_BATCH_RENDER_PASS_enum>
    ≔ MARKER_BATCH_SIZE_SOURCE<graphics/MARKER_BATCH_SIZE_SOURCE_enum>
    ≔ MARKER_BATCH_SORT_ORDER<graphics/MARKER_BATCH_SORT_ORDER_enum>
    ≔ MARKER_BATCH_UNIT<graphics/MARKER_BATCH_UNIT_enum>
    ≔ MODEL_TRANSFORMATION_TYPE<graphics/MODEL_TRANSFORMATION_TYPE_enum>
    ≔ ORIGIN<graphics/ORIGIN_enum>
    ≔ PATH_PRIMITIVE_REMOVE_LOCATION<graphics/PATH_PRIMITIVE_REMOVE_LOCATION_enum>
    ≔ PRIMITIVES_SORT_ORDER<graphics/PRIMITIVES_SORT_ORDER_enum>
    ≔ REFRESH_RATE<graphics/REFRESH_RATE_enum>
    ≔ RENDER_PASS<graphics/RENDER_PASS_enum>
    ≔ RENDER_PASS_HINT<graphics/RENDER_PASS_HINT_enum>
    ≔ SCREEN_OVERLAY_ORIGIN<graphics/SCREEN_OVERLAY_ORIGIN_enum>
    ≔ SCREEN_OVERLAY_PINNING_ORIGIN<graphics/SCREEN_OVERLAY_PINNING_ORIGIN_enum>
    ≔ SCREEN_OVERLAY_UNIT<graphics/SCREEN_OVERLAY_UNIT_enum>
    ≔ SURFACE_MESH_RENDERING_METHOD<graphics/SURFACE_MESH_RENDERING_METHOD_enum>
    ≔ VISIBILITY<graphics/VISIBILITY_enum>
    ≔ ANTI_ALIASING<graphics/ANTI_ALIASING_enum>
    ≔ BINARY_LOGIC_OPERATION<graphics/BINARY_LOGIC_OPERATION_enum>
    ≔ BLUR_METHOD<graphics/BLUR_METHOD_enum>
    ≔ EDGE_DETECT_METHOD<graphics/EDGE_DETECT_METHOD_enum>
    ≔ FLIP_AXIS<graphics/FLIP_AXIS_enum>
    ≔ GRADIENT_DETECT_METHOD<graphics/GRADIENT_DETECT_METHOD_enum>
    ≔ JPEG2000_COMPRESSION_PROFILE<graphics/JPEG2000_COMPRESSION_PROFILE_enum>
    ≔ RASTER_BAND<graphics/RASTER_BAND_enum>
    ≔ RASTER_FORMAT<graphics/RASTER_FORMAT_enum>
    ≔ RASTER_ORIENTATION<graphics/RASTER_ORIENTATION_enum>
    ≔ RASTER_TYPE<graphics/RASTER_TYPE_enum>
    ≔ SHARPEN_METHOD<graphics/SHARPEN_METHOD_enum>
    ≔ VIDEO_PLAYBACK<graphics/VIDEO_PLAYBACK_enum>
    ≔ KML_NETWORK_LINK_REFRESH_MODE<graphics/KML_NETWORK_LINK_REFRESH_MODE_enum>
    ≔ KML_NETWORK_LINK_VIEW_REFRESH_MODE<graphics/KML_NETWORK_LINK_VIEW_REFRESH_MODE_enum>
    ≔ MODEL_UP_AXIS<graphics/MODEL_UP_AXIS_enum>
    ≔ OUTLINE_APPEARANCE<graphics/OUTLINE_APPEARANCE_enum>
    ≔ POLYLINE_TYPE<graphics/POLYLINE_TYPE_enum>
    ≔ CULL_FACE<graphics/CULL_FACE_enum>
    ≔ INTERNAL_TEXTURE_FORMAT<graphics/INTERNAL_TEXTURE_FORMAT_enum>
    ≔ MAGNIFICATION_FILTER<graphics/MAGNIFICATION_FILTER_enum>
    ≔ MINIFICATION_FILTER<graphics/MINIFICATION_FILTER_enum>
    ≔ RENDERER_SHADE_MODEL<graphics/RENDERER_SHADE_MODEL_enum>
    ≔ TEXTURE_WRAP<graphics/TEXTURE_WRAP_enum>
    ≔ SET_HINT<graphics/SET_HINT_enum>
    ≔ STEREO_PROJECTION_MODE<graphics/STEREO_PROJECTION_MODE_enum>
    ≔ STEREOSCOPIC_DISPLAY_MODE<graphics/STEREOSCOPIC_DISPLAY_MODE_enum>
    ≔ FONT_STYLE<graphics/FONT_STYLE_enum>

