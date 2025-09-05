FactoryAndInitializers
======================

.. py:class:: ansys.stk.core.graphics.FactoryAndInitializers

   Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

.. py:currentmodule:: FactoryAndInitializers

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.agi_custom_terrain_overlay`
              - Access global methods and properties of AGICustomTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.agi_processed_image_globe_overlay`
              - Access global methods and properties of AGIProcessedImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.agi_processed_terrain_overlay`
              - Access global methods and properties of AGIProcessedTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.agi_roam_image_globe_overlay`
              - Access global methods and properties of AGIRoamImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.alpha_from_luminance_filter`
              - Access global methods and properties of AlphaFromLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.alpha_from_pixel_filter`
              - Access global methods and properties of AlphaFromPixelFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.alpha_from_raster_filter`
              - Access global methods and properties of AlphaFromRasterFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.altitude_display_condition`
              - Access global methods and properties of AltitudeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.axes_primitive`
              - Access global methods and properties of AxesPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.band_extract_filter`
              - Access global methods and properties of BandExtractFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.band_order_filter`
              - Access global methods and properties of BandOrderFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.blur_filter`
              - Access global methods and properties of BlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.bounding_sphere`
              - Factory creates bounding spheres.
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.box_triangulator`
              - Access global methods and properties of BoxTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.brightness_filter`
              - Access global methods and properties of BrightnessFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.color_to_luminance_filter`
              - Access global methods and properties of ColorToLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.composite_display_condition`
              - Access global methods and properties of CompositeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.composite_primitive`
              - Access global methods and properties of CompositePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.constant_display_condition`
              - Access global methods and properties of ConstantDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.contrast_filter`
              - Access global methods and properties of ContrastFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.convolution_filter`
              - Access global methods and properties of ConvolutionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.custom_image_globe_overlay_plugin_activator`
              - Access global methods and properties of CustomImageGlobeOverlayPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.cylinder_triangulator`
              - Access global methods and properties of CylinderTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.distance_display_condition`
              - Access global methods and properties of DistanceDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.distance_to_globe_overlay_display_condition`
              - Access global methods and properties of DistanceToGlobeOverlayDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.distance_to_position_display_condition`
              - Access global methods and properties of DistanceToPositionDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.distance_to_primitive_display_condition`
              - Access global methods and properties of DistanceToPrimitiveDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.duration_path_primitive_update_policy`
              - Access global methods and properties of DurationPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.edge_detect_filter`
              - Access global methods and properties of EdgeDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.ellipsoid_triangulator`
              - Access global methods and properties of EllipsoidTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.extruded_polyline_triangulator`
              - Access global methods and properties of ExtrudedPolylineTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.filtering_raster_stream`
              - Access global methods and properties of FilteringRasterStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.flip_filter`
              - Access global methods and properties of FlipFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.gamma_correction_filter`
              - Access global methods and properties of GammaCorrectionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.gaussian_blur_filter`
              - Access global methods and properties of GaussianBlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.geospatial_image_globe_overlay`
              - Access global methods and properties of GeospatialImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.globe_image_overlay`
              - Access global methods and properties of GlobeImageOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.gradient_detect_filter`
              - Access global methods and properties of GradientDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.graphics_font`
              - Access global methods and properties of GraphicsFont (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.great_arc_interpolator`
              - Access global methods and properties of GreatArcInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.jpeg2000_writer`
              - Access global methods and properties of Jpeg2000Writer (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.levels_filter`
              - Access global methods and properties of LevelsFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.marker_batch_primitive`
              - Access global methods and properties of MarkerBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.marker_batch_primitive_optional_parameters`
              - Access global methods and properties of MarkerBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.maximum_count_path_primitive_update_policy`
              - Access global methods and properties of MaximumCountPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.model_primitive`
              - Access global methods and properties of ModelPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.path_point`
              - Factory creates path points.
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.path_primitive`
              - Access global methods and properties of PathPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.pixel_size_display_condition`
              - Access global methods and properties of PixelSizeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.point_batch_primitive`
              - Access global methods and properties of PointBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.point_batch_primitive_optional_parameters`
              - Access global methods and properties of PointBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.polyline_primitive`
              - Access global methods and properties of PolylinePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.polyline_primitive_optional_parameters`
              - Access global methods and properties of PolylinePrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.projected_raster_overlay`
              - Access global methods and properties of ProjectedRasterOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.projection`
              - Access global methods and properties of Projection (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.projection_raster_stream_plugin_activator`
              - Access global methods and properties of ProjectionRasterStreamPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.raster`
              - Access global methods and properties of Raster (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.raster_attributes`
              - Access global methods and properties of RasterAttributes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.raster_image_globe_overlay`
              - Access global methods and properties of RasterImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.rhumb_line_interpolator`
              - Access global methods and properties of RhumbLineInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.rotate_filter`
              - Access global methods and properties of RotateFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.scene_display_condition`
              - Access global methods and properties of SceneDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.scene_manager`
              - Access global methods and properties of SceneManager (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.screen_overlay`
              - Access global methods and properties of ScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.sequence_filter`
              - Access global methods and properties of SequenceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.sharpen_filter`
              - Access global methods and properties of SharpenFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.solid_primitive`
              - Access global methods and properties of SolidPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.surface_extent_triangulator`
              - Access global methods and properties of SurfaceExtentTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.surface_mesh_primitive`
              - Access global methods and properties of SurfaceMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.surface_polygon_triangulator`
              - Access global methods and properties of SurfacePolygonTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.surface_shapes`
              - Access global methods and properties of SurfaceShapes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.terrain_overlay`
              - Access global methods and properties of TerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.text_batch_primitive`
              - Access global methods and properties of TextBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.text_batch_primitive_optional_parameters`
              - Access global methods and properties of TextBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.text_overlay`
              - Access global methods and properties of TextOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.texture_filter_2d`
              - Factory creates texture filters.
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.texture_matrix`
              - Access global methods and properties of TextureMatrix (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.texture_screen_overlay`
              - Access global methods and properties of TextureScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.time_interval_display_condition`
              - Access global methods and properties of TimeIntervalDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.triangle_mesh_primitive`
              - Access global methods and properties of TriangleMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.triangle_mesh_primitive_optional_parameters`
              - Access global methods and properties of TriangleMeshPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.vector_primitive`
              - Access global methods and properties of VectorPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).
            * - :py:attr:`~ansys.stk.core.graphics.FactoryAndInitializers.video_stream`
              - Access global methods and properties of VideoStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import FactoryAndInitializers


Property detail
---------------

.. py:property:: agi_custom_terrain_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.agi_custom_terrain_overlay
    :type: AGICustomTerrainOverlayFactory

    Access global methods and properties of AGICustomTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_processed_image_globe_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.agi_processed_image_globe_overlay
    :type: AGIProcessedImageGlobeOverlayFactory

    Access global methods and properties of AGIProcessedImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_processed_terrain_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.agi_processed_terrain_overlay
    :type: AGIProcessedTerrainOverlayFactory

    Access global methods and properties of AGIProcessedTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_roam_image_globe_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.agi_roam_image_globe_overlay
    :type: AGIRoamImageGlobeOverlayFactory

    Access global methods and properties of AGIRoamImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_luminance_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.alpha_from_luminance_filter
    :type: AlphaFromLuminanceFilterFactory

    Access global methods and properties of AlphaFromLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_pixel_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.alpha_from_pixel_filter
    :type: AlphaFromPixelFilterFactory

    Access global methods and properties of AlphaFromPixelFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_raster_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.alpha_from_raster_filter
    :type: AlphaFromRasterFilterFactory

    Access global methods and properties of AlphaFromRasterFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: altitude_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.altitude_display_condition
    :type: AltitudeDisplayConditionFactory

    Access global methods and properties of AltitudeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: axes_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.axes_primitive
    :type: AxesPrimitiveFactory

    Access global methods and properties of AxesPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: band_extract_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.band_extract_filter
    :type: BandExtractFilterFactory

    Access global methods and properties of BandExtractFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: band_order_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.band_order_filter
    :type: BandOrderFilterFactory

    Access global methods and properties of BandOrderFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: blur_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.blur_filter
    :type: BlurFilterFactory

    Access global methods and properties of BlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.bounding_sphere
    :type: BoundingSphereFactory

    Factory creates bounding spheres.

.. py:property:: box_triangulator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.box_triangulator
    :type: BoxTriangulatorInitializer

    Access global methods and properties of BoxTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: brightness_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.brightness_filter
    :type: BrightnessFilterFactory

    Access global methods and properties of BrightnessFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: color_to_luminance_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.color_to_luminance_filter
    :type: ColorToLuminanceFilterFactory

    Access global methods and properties of ColorToLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: composite_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.composite_display_condition
    :type: CompositeDisplayConditionFactory

    Access global methods and properties of CompositeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: composite_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.composite_primitive
    :type: CompositePrimitiveFactory

    Access global methods and properties of CompositePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: constant_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.constant_display_condition
    :type: ConstantDisplayConditionFactory

    Access global methods and properties of ConstantDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: contrast_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.contrast_filter
    :type: ContrastFilterFactory

    Access global methods and properties of ContrastFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: convolution_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.convolution_filter
    :type: ConvolutionFilterFactory

    Access global methods and properties of ConvolutionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: custom_image_globe_overlay_plugin_activator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.custom_image_globe_overlay_plugin_activator
    :type: CustomImageGlobeOverlayPluginActivatorFactory

    Access global methods and properties of CustomImageGlobeOverlayPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: cylinder_triangulator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.cylinder_triangulator
    :type: CylinderTriangulatorInitializer

    Access global methods and properties of CylinderTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.distance_display_condition
    :type: DistanceDisplayConditionFactory

    Access global methods and properties of DistanceDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_globe_overlay_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.distance_to_globe_overlay_display_condition
    :type: DistanceToGlobeOverlayDisplayConditionFactory

    Access global methods and properties of DistanceToGlobeOverlayDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_position_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.distance_to_position_display_condition
    :type: DistanceToPositionDisplayConditionFactory

    Access global methods and properties of DistanceToPositionDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_primitive_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.distance_to_primitive_display_condition
    :type: DistanceToPrimitiveDisplayConditionFactory

    Access global methods and properties of DistanceToPrimitiveDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: duration_path_primitive_update_policy
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.duration_path_primitive_update_policy
    :type: DurationPathPrimitiveUpdatePolicyFactory

    Access global methods and properties of DurationPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: edge_detect_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.edge_detect_filter
    :type: EdgeDetectFilterFactory

    Access global methods and properties of EdgeDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: ellipsoid_triangulator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.ellipsoid_triangulator
    :type: EllipsoidTriangulatorInitializer

    Access global methods and properties of EllipsoidTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: extruded_polyline_triangulator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.extruded_polyline_triangulator
    :type: ExtrudedPolylineTriangulatorInitializer

    Access global methods and properties of ExtrudedPolylineTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: filtering_raster_stream
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.filtering_raster_stream
    :type: FilteringRasterStreamFactory

    Access global methods and properties of FilteringRasterStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: flip_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.flip_filter
    :type: FlipFilterFactory

    Access global methods and properties of FlipFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gamma_correction_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.gamma_correction_filter
    :type: GammaCorrectionFilterFactory

    Access global methods and properties of GammaCorrectionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gaussian_blur_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.gaussian_blur_filter
    :type: GaussianBlurFilterFactory

    Access global methods and properties of GaussianBlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: geospatial_image_globe_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.geospatial_image_globe_overlay
    :type: GeospatialImageGlobeOverlayFactory

    Access global methods and properties of GeospatialImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: globe_image_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.globe_image_overlay
    :type: GlobeImageOverlayInitializer

    Access global methods and properties of GlobeImageOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gradient_detect_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.gradient_detect_filter
    :type: GradientDetectFilterFactory

    Access global methods and properties of GradientDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: graphics_font
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.graphics_font
    :type: GraphicsFontFactory

    Access global methods and properties of GraphicsFont (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: great_arc_interpolator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.great_arc_interpolator
    :type: GreatArcInterpolatorFactory

    Access global methods and properties of GreatArcInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: jpeg2000_writer
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.jpeg2000_writer
    :type: Jpeg2000WriterInitializer

    Access global methods and properties of Jpeg2000Writer (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: levels_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.levels_filter
    :type: LevelsFilterFactory

    Access global methods and properties of LevelsFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: marker_batch_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.marker_batch_primitive
    :type: MarkerBatchPrimitiveFactory

    Access global methods and properties of MarkerBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: marker_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.marker_batch_primitive_optional_parameters
    :type: MarkerBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of MarkerBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: maximum_count_path_primitive_update_policy
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.maximum_count_path_primitive_update_policy
    :type: MaximumCountPathPrimitiveUpdatePolicyFactory

    Access global methods and properties of MaximumCountPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: model_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.model_primitive
    :type: ModelPrimitiveFactory

    Access global methods and properties of ModelPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: path_point
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.path_point
    :type: PathPointFactory

    Factory creates path points.

.. py:property:: path_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.path_primitive
    :type: PathPrimitiveFactory

    Access global methods and properties of PathPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: pixel_size_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.pixel_size_display_condition
    :type: PixelSizeDisplayConditionFactory

    Access global methods and properties of PixelSizeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: point_batch_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.point_batch_primitive
    :type: PointBatchPrimitiveFactory

    Access global methods and properties of PointBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: point_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.point_batch_primitive_optional_parameters
    :type: PointBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of PointBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: polyline_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.polyline_primitive
    :type: PolylinePrimitiveFactory

    Access global methods and properties of PolylinePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: polyline_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.polyline_primitive_optional_parameters
    :type: PolylinePrimitiveOptionalParametersFactory

    Access global methods and properties of PolylinePrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projected_raster_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.projected_raster_overlay
    :type: ProjectedRasterOverlayFactory

    Access global methods and properties of ProjectedRasterOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projection
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.projection
    :type: ProjectionFactory

    Access global methods and properties of Projection (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projection_raster_stream_plugin_activator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.projection_raster_stream_plugin_activator
    :type: ProjectionRasterStreamPluginActivatorFactory

    Access global methods and properties of ProjectionRasterStreamPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.raster
    :type: RasterFactory

    Access global methods and properties of Raster (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster_attributes
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.raster_attributes
    :type: RasterAttributesFactory

    Access global methods and properties of RasterAttributes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster_image_globe_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.raster_image_globe_overlay
    :type: RasterImageGlobeOverlayFactory

    Access global methods and properties of RasterImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: rhumb_line_interpolator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.rhumb_line_interpolator
    :type: RhumbLineInterpolatorFactory

    Access global methods and properties of RhumbLineInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: rotate_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.rotate_filter
    :type: RotateFilterFactory

    Access global methods and properties of RotateFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: scene_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.scene_display_condition
    :type: SceneDisplayConditionFactory

    Access global methods and properties of SceneDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: scene_manager
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.scene_manager
    :type: SceneManagerInitializer

    Access global methods and properties of SceneManager (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: screen_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.screen_overlay
    :type: ScreenOverlayFactory

    Access global methods and properties of ScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: sequence_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.sequence_filter
    :type: SequenceFilterFactory

    Access global methods and properties of SequenceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: sharpen_filter
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.sharpen_filter
    :type: SharpenFilterFactory

    Access global methods and properties of SharpenFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: solid_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.solid_primitive
    :type: SolidPrimitiveFactory

    Access global methods and properties of SolidPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_extent_triangulator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.surface_extent_triangulator
    :type: SurfaceExtentTriangulatorInitializer

    Access global methods and properties of SurfaceExtentTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_mesh_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.surface_mesh_primitive
    :type: SurfaceMeshPrimitiveFactory

    Access global methods and properties of SurfaceMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_polygon_triangulator
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.surface_polygon_triangulator
    :type: SurfacePolygonTriangulatorInitializer

    Access global methods and properties of SurfacePolygonTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_shapes
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.surface_shapes
    :type: SurfaceShapesInitializer

    Access global methods and properties of SurfaceShapes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: terrain_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.terrain_overlay
    :type: TerrainOverlayInitializer

    Access global methods and properties of TerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_batch_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.text_batch_primitive
    :type: TextBatchPrimitiveFactory

    Access global methods and properties of TextBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.text_batch_primitive_optional_parameters
    :type: TextBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of TextBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.text_overlay
    :type: TextOverlayFactory

    Access global methods and properties of TextOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_filter_2d
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.texture_filter_2d
    :type: TextureFilter2DFactory

    Factory creates texture filters.

.. py:property:: texture_matrix
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.texture_matrix
    :type: TextureMatrixFactory

    Access global methods and properties of TextureMatrix (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_screen_overlay
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.texture_screen_overlay
    :type: TextureScreenOverlayFactory

    Access global methods and properties of TextureScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: time_interval_display_condition
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.time_interval_display_condition
    :type: TimeIntervalDisplayConditionFactory

    Access global methods and properties of TimeIntervalDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: triangle_mesh_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.triangle_mesh_primitive
    :type: TriangleMeshPrimitiveFactory

    Access global methods and properties of TriangleMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: triangle_mesh_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.triangle_mesh_primitive_optional_parameters
    :type: TriangleMeshPrimitiveOptionalParametersFactory

    Access global methods and properties of TriangleMeshPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: vector_primitive
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.vector_primitive
    :type: VectorPrimitiveFactory

    Access global methods and properties of VectorPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: video_stream
    :canonical: ansys.stk.core.graphics.FactoryAndInitializers.video_stream
    :type: VideoStreamFactory

    Access global methods and properties of VideoStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).


