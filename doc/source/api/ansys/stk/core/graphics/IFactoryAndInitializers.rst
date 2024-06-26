IFactoryAndInitializers
=======================

.. py:class:: ansys.stk.core.graphics.IFactoryAndInitializers

   object
   
   Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

.. py:currentmodule:: IFactoryAndInitializers

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.box_triangulator`
              - Access global methods and properties of BoxTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.cylinder_triangulator`
              - Access global methods and properties of CylinderTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.ellipsoid_triangulator`
              - Access global methods and properties of EllipsoidTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.extruded_polyline_triangulator`
              - Access global methods and properties of ExtrudedPolylineTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.surface_extent_triangulator`
              - Access global methods and properties of SurfaceExtentTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.surface_polygon_triangulator`
              - Access global methods and properties of SurfacePolygonTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.surface_shapes`
              - Access global methods and properties of SurfaceShapes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.agi_processed_image_globe_overlay`
              - Access global methods and properties of AGIProcessedImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.agi_processed_terrain_overlay`
              - Access global methods and properties of AGIProcessedTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.agi_roam_image_globe_overlay`
              - Access global methods and properties of AGIRoamImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.custom_image_globe_overlay_plugin_activator`
              - Access global methods and properties of CustomImageGlobeOverlayPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.geospatial_image_globe_overlay`
              - Access global methods and properties of GeospatialImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.projected_raster_overlay`
              - Access global methods and properties of ProjectedRasterOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.projection`
              - Access global methods and properties of Projection (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.altitude_display_condition`
              - Access global methods and properties of AltitudeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.composite_display_condition`
              - Access global methods and properties of CompositeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.composite_primitive`
              - Access global methods and properties of CompositePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.constant_display_condition`
              - Access global methods and properties of ConstantDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.distance_display_condition`
              - Access global methods and properties of DistanceDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_globe_overlay_display_condition`
              - Access global methods and properties of DistanceToGlobeOverlayDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_position_display_condition`
              - Access global methods and properties of DistanceToPositionDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_primitive_display_condition`
              - Access global methods and properties of DistanceToPrimitiveDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.duration_path_primitive_update_policy`
              - Access global methods and properties of DurationPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.globe_image_overlay`
              - Access global methods and properties of GlobeImageOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.graphics_font`
              - Access global methods and properties of GraphicsFont (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.great_arc_interpolator`
              - Access global methods and properties of GreatArcInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_luminance_filter`
              - Access global methods and properties of AlphaFromLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_pixel_filter`
              - Access global methods and properties of AlphaFromPixelFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_raster_filter`
              - Access global methods and properties of AlphaFromRasterFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.band_extract_filter`
              - Access global methods and properties of BandExtractFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.band_order_filter`
              - Access global methods and properties of BandOrderFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.blur_filter`
              - Access global methods and properties of BlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.brightness_filter`
              - Access global methods and properties of BrightnessFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.color_to_luminance_filter`
              - Access global methods and properties of ColorToLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.contrast_filter`
              - Access global methods and properties of ContrastFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.convolution_filter`
              - Access global methods and properties of ConvolutionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.edge_detect_filter`
              - Access global methods and properties of EdgeDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.filtering_raster_stream`
              - Access global methods and properties of FilteringRasterStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.flip_filter`
              - Access global methods and properties of FlipFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.gamma_correction_filter`
              - Access global methods and properties of GammaCorrectionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.gaussian_blur_filter`
              - Access global methods and properties of GaussianBlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.gradient_detect_filter`
              - Access global methods and properties of GradientDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.jpeg2000_writer`
              - Access global methods and properties of Jpeg2000Writer (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.levels_filter`
              - Access global methods and properties of LevelsFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.projection_raster_stream_plugin_activator`
              - Access global methods and properties of ProjectionRasterStreamPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.raster`
              - Access global methods and properties of Raster (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.raster_attributes`
              - Access global methods and properties of RasterAttributes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.rotate_filter`
              - Access global methods and properties of RotateFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.sequence_filter`
              - Access global methods and properties of SequenceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.sharpen_filter`
              - Access global methods and properties of SharpenFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.video_stream`
              - Access global methods and properties of VideoStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.marker_batch_primitive`
              - Access global methods and properties of MarkerBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.marker_batch_primitive_optional_parameters`
              - Access global methods and properties of MarkerBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.maximum_count_path_primitive_update_policy`
              - Access global methods and properties of MaximumCountPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.model_primitive`
              - Access global methods and properties of ModelPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.path_primitive`
              - Access global methods and properties of PathPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.pixel_size_display_condition`
              - Access global methods and properties of PixelSizeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.point_batch_primitive`
              - Access global methods and properties of PointBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.polyline_primitive`
              - Access global methods and properties of PolylinePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.raster_image_globe_overlay`
              - Access global methods and properties of RasterImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.rhumb_line_interpolator`
              - Access global methods and properties of RhumbLineInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.scene_display_condition`
              - Access global methods and properties of SceneDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.scene_manager`
              - Access global methods and properties of SceneManager (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.screen_overlay`
              - Access global methods and properties of ScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.solid_primitive`
              - Access global methods and properties of SolidPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.surface_mesh_primitive`
              - Access global methods and properties of SurfaceMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.terrain_overlay`
              - Access global methods and properties of TerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.text_batch_primitive`
              - Access global methods and properties of TextBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.text_batch_primitive_optional_parameters`
              - Access global methods and properties of TextBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.texture_matrix`
              - Access global methods and properties of TextureMatrix (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.texture_screen_overlay`
              - Access global methods and properties of TextureScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.time_interval_display_condition`
              - Access global methods and properties of TimeIntervalDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.triangle_mesh_primitive`
              - Access global methods and properties of TriangleMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.triangle_mesh_primitive_optional_parameters`
              - Access global methods and properties of TriangleMeshPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.texture_filter_2d`
              - Factory creates texture filters.
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.bounding_sphere`
              - Factory creates bounding spheres.
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.path_point`
              - Factory creates path points.
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.text_overlay`
              - Access global methods and properties of TextOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.agi_custom_terrain_overlay`
              - Access global methods and properties of AGICustomTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.axes_primitive`
              - Access global methods and properties of AxesPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.vector_primitive`
              - Access global methods and properties of VectorPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.polyline_primitive_optional_parameters`
              - Access global methods and properties of PolylinePrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.IFactoryAndInitializers.point_batch_primitive_optional_parameters`
              - Access global methods and properties of PointBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IFactoryAndInitializers


Property detail
---------------

.. py:property:: box_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.box_triangulator
    :type: IBoxTriangulatorInitializer

    Access global methods and properties of BoxTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: cylinder_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.cylinder_triangulator
    :type: ICylinderTriangulatorInitializer

    Access global methods and properties of CylinderTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: ellipsoid_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.ellipsoid_triangulator
    :type: IEllipsoidTriangulatorInitializer

    Access global methods and properties of EllipsoidTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: extruded_polyline_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.extruded_polyline_triangulator
    :type: IExtrudedPolylineTriangulatorInitializer

    Access global methods and properties of ExtrudedPolylineTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_extent_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_extent_triangulator
    :type: ISurfaceExtentTriangulatorInitializer

    Access global methods and properties of SurfaceExtentTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_polygon_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_polygon_triangulator
    :type: ISurfacePolygonTriangulatorInitializer

    Access global methods and properties of SurfacePolygonTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_shapes
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_shapes
    :type: ISurfaceShapesInitializer

    Access global methods and properties of SurfaceShapes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_processed_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_processed_image_globe_overlay
    :type: IAGIProcessedImageGlobeOverlayFactory

    Access global methods and properties of AGIProcessedImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_processed_terrain_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_processed_terrain_overlay
    :type: IAGIProcessedTerrainOverlayFactory

    Access global methods and properties of AGIProcessedTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_roam_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_roam_image_globe_overlay
    :type: IAGIRoamImageGlobeOverlayFactory

    Access global methods and properties of AGIRoamImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: custom_image_globe_overlay_plugin_activator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.custom_image_globe_overlay_plugin_activator
    :type: ICustomImageGlobeOverlayPluginActivatorFactory

    Access global methods and properties of CustomImageGlobeOverlayPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: geospatial_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.geospatial_image_globe_overlay
    :type: IGeospatialImageGlobeOverlayFactory

    Access global methods and properties of GeospatialImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projected_raster_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.projected_raster_overlay
    :type: IProjectedRasterOverlayFactory

    Access global methods and properties of ProjectedRasterOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projection
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.projection
    :type: IProjectionFactory

    Access global methods and properties of Projection (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: altitude_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.altitude_display_condition
    :type: IAltitudeDisplayConditionFactory

    Access global methods and properties of AltitudeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: composite_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.composite_display_condition
    :type: ICompositeDisplayConditionFactory

    Access global methods and properties of CompositeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: composite_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.composite_primitive
    :type: ICompositePrimitiveFactory

    Access global methods and properties of CompositePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: constant_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.constant_display_condition
    :type: IConstantDisplayConditionFactory

    Access global methods and properties of ConstantDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_display_condition
    :type: IDistanceDisplayConditionFactory

    Access global methods and properties of DistanceDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_globe_overlay_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_globe_overlay_display_condition
    :type: IDistanceToGlobeOverlayDisplayConditionFactory

    Access global methods and properties of DistanceToGlobeOverlayDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_position_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_position_display_condition
    :type: IDistanceToPositionDisplayConditionFactory

    Access global methods and properties of DistanceToPositionDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_primitive_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_primitive_display_condition
    :type: IDistanceToPrimitiveDisplayConditionFactory

    Access global methods and properties of DistanceToPrimitiveDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: duration_path_primitive_update_policy
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.duration_path_primitive_update_policy
    :type: IDurationPathPrimitiveUpdatePolicyFactory

    Access global methods and properties of DurationPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: globe_image_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.globe_image_overlay
    :type: IGlobeImageOverlayInitializer

    Access global methods and properties of GlobeImageOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: graphics_font
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.graphics_font
    :type: IGraphicsFontFactory

    Access global methods and properties of GraphicsFont (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: great_arc_interpolator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.great_arc_interpolator
    :type: IGreatArcInterpolatorFactory

    Access global methods and properties of GreatArcInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_luminance_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_luminance_filter
    :type: IAlphaFromLuminanceFilterFactory

    Access global methods and properties of AlphaFromLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_pixel_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_pixel_filter
    :type: IAlphaFromPixelFilterFactory

    Access global methods and properties of AlphaFromPixelFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_raster_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_raster_filter
    :type: IAlphaFromRasterFilterFactory

    Access global methods and properties of AlphaFromRasterFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: band_extract_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.band_extract_filter
    :type: IBandExtractFilterFactory

    Access global methods and properties of BandExtractFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: band_order_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.band_order_filter
    :type: IBandOrderFilterFactory

    Access global methods and properties of BandOrderFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: blur_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.blur_filter
    :type: IBlurFilterFactory

    Access global methods and properties of BlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: brightness_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.brightness_filter
    :type: IBrightnessFilterFactory

    Access global methods and properties of BrightnessFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: color_to_luminance_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.color_to_luminance_filter
    :type: IColorToLuminanceFilterFactory

    Access global methods and properties of ColorToLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: contrast_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.contrast_filter
    :type: IContrastFilterFactory

    Access global methods and properties of ContrastFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: convolution_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.convolution_filter
    :type: IConvolutionFilterFactory

    Access global methods and properties of ConvolutionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: edge_detect_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.edge_detect_filter
    :type: IEdgeDetectFilterFactory

    Access global methods and properties of EdgeDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: filtering_raster_stream
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.filtering_raster_stream
    :type: IFilteringRasterStreamFactory

    Access global methods and properties of FilteringRasterStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: flip_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.flip_filter
    :type: IFlipFilterFactory

    Access global methods and properties of FlipFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gamma_correction_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.gamma_correction_filter
    :type: IGammaCorrectionFilterFactory

    Access global methods and properties of GammaCorrectionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gaussian_blur_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.gaussian_blur_filter
    :type: IGaussianBlurFilterFactory

    Access global methods and properties of GaussianBlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gradient_detect_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.gradient_detect_filter
    :type: IGradientDetectFilterFactory

    Access global methods and properties of GradientDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: jpeg2000_writer
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.jpeg2000_writer
    :type: IJpeg2000WriterInitializer

    Access global methods and properties of Jpeg2000Writer (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: levels_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.levels_filter
    :type: ILevelsFilterFactory

    Access global methods and properties of LevelsFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projection_raster_stream_plugin_activator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.projection_raster_stream_plugin_activator
    :type: IProjectionRasterStreamPluginActivatorFactory

    Access global methods and properties of ProjectionRasterStreamPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.raster
    :type: IRasterFactory

    Access global methods and properties of Raster (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster_attributes
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.raster_attributes
    :type: IRasterAttributesFactory

    Access global methods and properties of RasterAttributes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: rotate_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.rotate_filter
    :type: IRotateFilterFactory

    Access global methods and properties of RotateFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: sequence_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.sequence_filter
    :type: ISequenceFilterFactory

    Access global methods and properties of SequenceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: sharpen_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.sharpen_filter
    :type: ISharpenFilterFactory

    Access global methods and properties of SharpenFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: video_stream
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.video_stream
    :type: IVideoStreamFactory

    Access global methods and properties of VideoStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: marker_batch_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.marker_batch_primitive
    :type: IMarkerBatchPrimitiveFactory

    Access global methods and properties of MarkerBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: marker_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.marker_batch_primitive_optional_parameters
    :type: IMarkerBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of MarkerBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: maximum_count_path_primitive_update_policy
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.maximum_count_path_primitive_update_policy
    :type: IMaximumCountPathPrimitiveUpdatePolicyFactory

    Access global methods and properties of MaximumCountPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: model_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.model_primitive
    :type: IModelPrimitiveFactory

    Access global methods and properties of ModelPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: path_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.path_primitive
    :type: IPathPrimitiveFactory

    Access global methods and properties of PathPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: pixel_size_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.pixel_size_display_condition
    :type: IPixelSizeDisplayConditionFactory

    Access global methods and properties of PixelSizeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: point_batch_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.point_batch_primitive
    :type: IPointBatchPrimitiveFactory

    Access global methods and properties of PointBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: polyline_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.polyline_primitive
    :type: IPolylinePrimitiveFactory

    Access global methods and properties of PolylinePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.raster_image_globe_overlay
    :type: IRasterImageGlobeOverlayFactory

    Access global methods and properties of RasterImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: rhumb_line_interpolator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.rhumb_line_interpolator
    :type: IRhumbLineInterpolatorFactory

    Access global methods and properties of RhumbLineInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: scene_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.scene_display_condition
    :type: ISceneDisplayConditionFactory

    Access global methods and properties of SceneDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: scene_manager
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.scene_manager
    :type: ISceneManagerInitializer

    Access global methods and properties of SceneManager (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: screen_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.screen_overlay
    :type: IScreenOverlayFactory

    Access global methods and properties of ScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: solid_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.solid_primitive
    :type: ISolidPrimitiveFactory

    Access global methods and properties of SolidPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_mesh_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_mesh_primitive
    :type: ISurfaceMeshPrimitiveFactory

    Access global methods and properties of SurfaceMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: terrain_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.terrain_overlay
    :type: ITerrainOverlayInitializer

    Access global methods and properties of TerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_batch_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.text_batch_primitive
    :type: ITextBatchPrimitiveFactory

    Access global methods and properties of TextBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.text_batch_primitive_optional_parameters
    :type: ITextBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of TextBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_matrix
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.texture_matrix
    :type: ITextureMatrixFactory

    Access global methods and properties of TextureMatrix (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_screen_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.texture_screen_overlay
    :type: ITextureScreenOverlayFactory

    Access global methods and properties of TextureScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: time_interval_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.time_interval_display_condition
    :type: ITimeIntervalDisplayConditionFactory

    Access global methods and properties of TimeIntervalDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: triangle_mesh_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.triangle_mesh_primitive
    :type: ITriangleMeshPrimitiveFactory

    Access global methods and properties of TriangleMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: triangle_mesh_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.triangle_mesh_primitive_optional_parameters
    :type: ITriangleMeshPrimitiveOptionalParametersFactory

    Access global methods and properties of TriangleMeshPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_filter_2d
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.texture_filter_2d
    :type: ITextureFilter2DFactory

    Factory creates texture filters.

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.bounding_sphere
    :type: IBoundingSphereFactory

    Factory creates bounding spheres.

.. py:property:: path_point
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.path_point
    :type: IPathPointFactory

    Factory creates path points.

.. py:property:: text_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.text_overlay
    :type: ITextOverlayFactory

    Access global methods and properties of TextOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_custom_terrain_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_custom_terrain_overlay
    :type: IAGICustomTerrainOverlayFactory

    Access global methods and properties of AGICustomTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: axes_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.axes_primitive
    :type: IAxesPrimitiveFactory

    Access global methods and properties of AxesPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: vector_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.vector_primitive
    :type: IVectorPrimitiveFactory

    Access global methods and properties of VectorPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: polyline_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.polyline_primitive_optional_parameters
    :type: IPolylinePrimitiveOptionalParametersFactory

    Access global methods and properties of PolylinePrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: point_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.point_batch_primitive_optional_parameters
    :type: IPointBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of PointBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).


