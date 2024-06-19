IFactoryAndInitializers
=======================

.. py:class:: IFactoryAndInitializers

   object
   
   Methods and properties are used to initialize new primitives, display conditions, screen overlays, textures and many other types; compute and retrieve triangulator results and access global properties (what's known as static properties, static methods a...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~box_triangulator`
            * - :py:meth:`~cylinder_triangulator`
            * - :py:meth:`~ellipsoid_triangulator`
            * - :py:meth:`~extruded_polyline_triangulator`
            * - :py:meth:`~surface_extent_triangulator`
            * - :py:meth:`~surface_polygon_triangulator`
            * - :py:meth:`~surface_shapes`
            * - :py:meth:`~agi_processed_image_globe_overlay`
            * - :py:meth:`~agi_processed_terrain_overlay`
            * - :py:meth:`~agi_roam_image_globe_overlay`
            * - :py:meth:`~custom_image_globe_overlay_plugin_activator`
            * - :py:meth:`~geospatial_image_globe_overlay`
            * - :py:meth:`~projected_raster_overlay`
            * - :py:meth:`~projection`
            * - :py:meth:`~altitude_display_condition`
            * - :py:meth:`~composite_display_condition`
            * - :py:meth:`~composite_primitive`
            * - :py:meth:`~constant_display_condition`
            * - :py:meth:`~distance_display_condition`
            * - :py:meth:`~distance_to_globe_overlay_display_condition`
            * - :py:meth:`~distance_to_position_display_condition`
            * - :py:meth:`~distance_to_primitive_display_condition`
            * - :py:meth:`~duration_path_primitive_update_policy`
            * - :py:meth:`~globe_image_overlay`
            * - :py:meth:`~graphics_font`
            * - :py:meth:`~great_arc_interpolator`
            * - :py:meth:`~alpha_from_luminance_filter`
            * - :py:meth:`~alpha_from_pixel_filter`
            * - :py:meth:`~alpha_from_raster_filter`
            * - :py:meth:`~band_extract_filter`
            * - :py:meth:`~band_order_filter`
            * - :py:meth:`~blur_filter`
            * - :py:meth:`~brightness_filter`
            * - :py:meth:`~color_to_luminance_filter`
            * - :py:meth:`~contrast_filter`
            * - :py:meth:`~convolution_filter`
            * - :py:meth:`~edge_detect_filter`
            * - :py:meth:`~filtering_raster_stream`
            * - :py:meth:`~flip_filter`
            * - :py:meth:`~gamma_correction_filter`
            * - :py:meth:`~gaussian_blur_filter`
            * - :py:meth:`~gradient_detect_filter`
            * - :py:meth:`~jpeg2000_writer`
            * - :py:meth:`~levels_filter`
            * - :py:meth:`~projection_raster_stream_plugin_activator`
            * - :py:meth:`~raster`
            * - :py:meth:`~raster_attributes`
            * - :py:meth:`~rotate_filter`
            * - :py:meth:`~sequence_filter`
            * - :py:meth:`~sharpen_filter`
            * - :py:meth:`~video_stream`
            * - :py:meth:`~marker_batch_primitive`
            * - :py:meth:`~marker_batch_primitive_optional_parameters`
            * - :py:meth:`~maximum_count_path_primitive_update_policy`
            * - :py:meth:`~model_primitive`
            * - :py:meth:`~path_primitive`
            * - :py:meth:`~pixel_size_display_condition`
            * - :py:meth:`~point_batch_primitive`
            * - :py:meth:`~polyline_primitive`
            * - :py:meth:`~raster_image_globe_overlay`
            * - :py:meth:`~rhumb_line_interpolator`
            * - :py:meth:`~scene_display_condition`
            * - :py:meth:`~scene_manager`
            * - :py:meth:`~screen_overlay`
            * - :py:meth:`~solid_primitive`
            * - :py:meth:`~surface_mesh_primitive`
            * - :py:meth:`~terrain_overlay`
            * - :py:meth:`~text_batch_primitive`
            * - :py:meth:`~text_batch_primitive_optional_parameters`
            * - :py:meth:`~texture_matrix`
            * - :py:meth:`~texture_screen_overlay`
            * - :py:meth:`~time_interval_display_condition`
            * - :py:meth:`~triangle_mesh_primitive`
            * - :py:meth:`~triangle_mesh_primitive_optional_parameters`
            * - :py:meth:`~texture_filter_2d`
            * - :py:meth:`~bounding_sphere`
            * - :py:meth:`~path_point`
            * - :py:meth:`~text_overlay`
            * - :py:meth:`~agi_custom_terrain_overlay`
            * - :py:meth:`~axes_primitive`
            * - :py:meth:`~vector_primitive`
            * - :py:meth:`~polyline_primitive_optional_parameters`
            * - :py:meth:`~point_batch_primitive_optional_parameters`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IFactoryAndInitializers


Property detail
---------------

.. py:property:: box_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.box_triangulator
    :type: IAgStkGraphicsBoxTriangulatorInitializer

    Access global methods and properties of BoxTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: cylinder_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.cylinder_triangulator
    :type: IAgStkGraphicsCylinderTriangulatorInitializer

    Access global methods and properties of CylinderTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: ellipsoid_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.ellipsoid_triangulator
    :type: IAgStkGraphicsEllipsoidTriangulatorInitializer

    Access global methods and properties of EllipsoidTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: extruded_polyline_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.extruded_polyline_triangulator
    :type: IAgStkGraphicsExtrudedPolylineTriangulatorInitializer

    Access global methods and properties of ExtrudedPolylineTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_extent_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_extent_triangulator
    :type: IAgStkGraphicsSurfaceExtentTriangulatorInitializer

    Access global methods and properties of SurfaceExtentTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_polygon_triangulator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_polygon_triangulator
    :type: IAgStkGraphicsSurfacePolygonTriangulatorInitializer

    Access global methods and properties of SurfacePolygonTriangulator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_shapes
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_shapes
    :type: IAgStkGraphicsSurfaceShapesInitializer

    Access global methods and properties of SurfaceShapes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_processed_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_processed_image_globe_overlay
    :type: IAgStkGraphicsAGIProcessedImageGlobeOverlayFactory

    Access global methods and properties of AGIProcessedImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_processed_terrain_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_processed_terrain_overlay
    :type: IAgStkGraphicsAGIProcessedTerrainOverlayFactory

    Access global methods and properties of AGIProcessedTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_roam_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_roam_image_globe_overlay
    :type: IAgStkGraphicsAGIRoamImageGlobeOverlayFactory

    Access global methods and properties of AGIRoamImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: custom_image_globe_overlay_plugin_activator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.custom_image_globe_overlay_plugin_activator
    :type: IAgStkGraphicsCustomImageGlobeOverlayPluginActivatorFactory

    Access global methods and properties of CustomImageGlobeOverlayPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: geospatial_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.geospatial_image_globe_overlay
    :type: IAgStkGraphicsGeospatialImageGlobeOverlayFactory

    Access global methods and properties of GeospatialImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projected_raster_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.projected_raster_overlay
    :type: IAgStkGraphicsProjectedRasterOverlayFactory

    Access global methods and properties of ProjectedRasterOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projection
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.projection
    :type: IAgStkGraphicsProjectionFactory

    Access global methods and properties of Projection (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: altitude_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.altitude_display_condition
    :type: IAgStkGraphicsAltitudeDisplayConditionFactory

    Access global methods and properties of AltitudeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: composite_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.composite_display_condition
    :type: IAgStkGraphicsCompositeDisplayConditionFactory

    Access global methods and properties of CompositeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: composite_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.composite_primitive
    :type: IAgStkGraphicsCompositePrimitiveFactory

    Access global methods and properties of CompositePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: constant_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.constant_display_condition
    :type: IAgStkGraphicsConstantDisplayConditionFactory

    Access global methods and properties of ConstantDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_display_condition
    :type: IAgStkGraphicsDistanceDisplayConditionFactory

    Access global methods and properties of DistanceDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_globe_overlay_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_globe_overlay_display_condition
    :type: IAgStkGraphicsDistanceToGlobeOverlayDisplayConditionFactory

    Access global methods and properties of DistanceToGlobeOverlayDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_position_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_position_display_condition
    :type: IAgStkGraphicsDistanceToPositionDisplayConditionFactory

    Access global methods and properties of DistanceToPositionDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: distance_to_primitive_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.distance_to_primitive_display_condition
    :type: IAgStkGraphicsDistanceToPrimitiveDisplayConditionFactory

    Access global methods and properties of DistanceToPrimitiveDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: duration_path_primitive_update_policy
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.duration_path_primitive_update_policy
    :type: IAgStkGraphicsDurationPathPrimitiveUpdatePolicyFactory

    Access global methods and properties of DurationPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: globe_image_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.globe_image_overlay
    :type: IAgStkGraphicsGlobeImageOverlayInitializer

    Access global methods and properties of GlobeImageOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: graphics_font
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.graphics_font
    :type: IAgStkGraphicsGraphicsFontFactory

    Access global methods and properties of GraphicsFont (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: great_arc_interpolator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.great_arc_interpolator
    :type: IAgStkGraphicsGreatArcInterpolatorFactory

    Access global methods and properties of GreatArcInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_luminance_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_luminance_filter
    :type: IAgStkGraphicsAlphaFromLuminanceFilterFactory

    Access global methods and properties of AlphaFromLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_pixel_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_pixel_filter
    :type: IAgStkGraphicsAlphaFromPixelFilterFactory

    Access global methods and properties of AlphaFromPixelFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: alpha_from_raster_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.alpha_from_raster_filter
    :type: IAgStkGraphicsAlphaFromRasterFilterFactory

    Access global methods and properties of AlphaFromRasterFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: band_extract_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.band_extract_filter
    :type: IAgStkGraphicsBandExtractFilterFactory

    Access global methods and properties of BandExtractFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: band_order_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.band_order_filter
    :type: IAgStkGraphicsBandOrderFilterFactory

    Access global methods and properties of BandOrderFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: blur_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.blur_filter
    :type: IAgStkGraphicsBlurFilterFactory

    Access global methods and properties of BlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: brightness_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.brightness_filter
    :type: IAgStkGraphicsBrightnessFilterFactory

    Access global methods and properties of BrightnessFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: color_to_luminance_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.color_to_luminance_filter
    :type: IAgStkGraphicsColorToLuminanceFilterFactory

    Access global methods and properties of ColorToLuminanceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: contrast_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.contrast_filter
    :type: IAgStkGraphicsContrastFilterFactory

    Access global methods and properties of ContrastFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: convolution_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.convolution_filter
    :type: IAgStkGraphicsConvolutionFilterFactory

    Access global methods and properties of ConvolutionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: edge_detect_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.edge_detect_filter
    :type: IAgStkGraphicsEdgeDetectFilterFactory

    Access global methods and properties of EdgeDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: filtering_raster_stream
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.filtering_raster_stream
    :type: IAgStkGraphicsFilteringRasterStreamFactory

    Access global methods and properties of FilteringRasterStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: flip_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.flip_filter
    :type: IAgStkGraphicsFlipFilterFactory

    Access global methods and properties of FlipFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gamma_correction_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.gamma_correction_filter
    :type: IAgStkGraphicsGammaCorrectionFilterFactory

    Access global methods and properties of GammaCorrectionFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gaussian_blur_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.gaussian_blur_filter
    :type: IAgStkGraphicsGaussianBlurFilterFactory

    Access global methods and properties of GaussianBlurFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: gradient_detect_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.gradient_detect_filter
    :type: IAgStkGraphicsGradientDetectFilterFactory

    Access global methods and properties of GradientDetectFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: jpeg2000_writer
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.jpeg2000_writer
    :type: IAgStkGraphicsJpeg2000WriterInitializer

    Access global methods and properties of Jpeg2000Writer (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: levels_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.levels_filter
    :type: IAgStkGraphicsLevelsFilterFactory

    Access global methods and properties of LevelsFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: projection_raster_stream_plugin_activator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.projection_raster_stream_plugin_activator
    :type: IAgStkGraphicsProjectionRasterStreamPluginActivatorFactory

    Access global methods and properties of ProjectionRasterStreamPluginActivator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.raster
    :type: IAgStkGraphicsRasterFactory

    Access global methods and properties of Raster (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster_attributes
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.raster_attributes
    :type: IAgStkGraphicsRasterAttributesFactory

    Access global methods and properties of RasterAttributes (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: rotate_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.rotate_filter
    :type: IAgStkGraphicsRotateFilterFactory

    Access global methods and properties of RotateFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: sequence_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.sequence_filter
    :type: IAgStkGraphicsSequenceFilterFactory

    Access global methods and properties of SequenceFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: sharpen_filter
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.sharpen_filter
    :type: IAgStkGraphicsSharpenFilterFactory

    Access global methods and properties of SharpenFilter (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: video_stream
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.video_stream
    :type: IAgStkGraphicsVideoStreamFactory

    Access global methods and properties of VideoStream (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: marker_batch_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.marker_batch_primitive
    :type: IAgStkGraphicsMarkerBatchPrimitiveFactory

    Access global methods and properties of MarkerBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: marker_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.marker_batch_primitive_optional_parameters
    :type: IAgStkGraphicsMarkerBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of MarkerBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: maximum_count_path_primitive_update_policy
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.maximum_count_path_primitive_update_policy
    :type: IAgStkGraphicsMaximumCountPathPrimitiveUpdatePolicyFactory

    Access global methods and properties of MaximumCountPathPrimitiveUpdatePolicy (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: model_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.model_primitive
    :type: IAgStkGraphicsModelPrimitiveFactory

    Access global methods and properties of ModelPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: path_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.path_primitive
    :type: IAgStkGraphicsPathPrimitiveFactory

    Access global methods and properties of PathPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: pixel_size_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.pixel_size_display_condition
    :type: IAgStkGraphicsPixelSizeDisplayConditionFactory

    Access global methods and properties of PixelSizeDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: point_batch_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.point_batch_primitive
    :type: IAgStkGraphicsPointBatchPrimitiveFactory

    Access global methods and properties of PointBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: polyline_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.polyline_primitive
    :type: IAgStkGraphicsPolylinePrimitiveFactory

    Access global methods and properties of PolylinePrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: raster_image_globe_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.raster_image_globe_overlay
    :type: IAgStkGraphicsRasterImageGlobeOverlayFactory

    Access global methods and properties of RasterImageGlobeOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: rhumb_line_interpolator
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.rhumb_line_interpolator
    :type: IAgStkGraphicsRhumbLineInterpolatorFactory

    Access global methods and properties of RhumbLineInterpolator (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: scene_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.scene_display_condition
    :type: IAgStkGraphicsSceneDisplayConditionFactory

    Access global methods and properties of SceneDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: scene_manager
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.scene_manager
    :type: IAgStkGraphicsSceneManagerInitializer

    Access global methods and properties of SceneManager (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: screen_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.screen_overlay
    :type: IAgStkGraphicsScreenOverlayFactory

    Access global methods and properties of ScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: solid_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.solid_primitive
    :type: IAgStkGraphicsSolidPrimitiveFactory

    Access global methods and properties of SolidPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: surface_mesh_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.surface_mesh_primitive
    :type: IAgStkGraphicsSurfaceMeshPrimitiveFactory

    Access global methods and properties of SurfaceMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: terrain_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.terrain_overlay
    :type: IAgStkGraphicsTerrainOverlayInitializer

    Access global methods and properties of TerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_batch_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.text_batch_primitive
    :type: IAgStkGraphicsTextBatchPrimitiveFactory

    Access global methods and properties of TextBatchPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: text_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.text_batch_primitive_optional_parameters
    :type: IAgStkGraphicsTextBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of TextBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_matrix
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.texture_matrix
    :type: IAgStkGraphicsTextureMatrixFactory

    Access global methods and properties of TextureMatrix (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_screen_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.texture_screen_overlay
    :type: IAgStkGraphicsTextureScreenOverlayFactory

    Access global methods and properties of TextureScreenOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: time_interval_display_condition
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.time_interval_display_condition
    :type: IAgStkGraphicsTimeIntervalDisplayConditionFactory

    Access global methods and properties of TimeIntervalDisplayCondition (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: triangle_mesh_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.triangle_mesh_primitive
    :type: IAgStkGraphicsTriangleMeshPrimitiveFactory

    Access global methods and properties of TriangleMeshPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: triangle_mesh_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.triangle_mesh_primitive_optional_parameters
    :type: IAgStkGraphicsTriangleMeshPrimitiveOptionalParametersFactory

    Access global methods and properties of TriangleMeshPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: texture_filter_2d
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.texture_filter_2d
    :type: IAgStkGraphicsTextureFilter2DFactory

    Factory creates texture filters.

.. py:property:: bounding_sphere
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.bounding_sphere
    :type: IAgStkGraphicsBoundingSphereFactory

    Factory creates bounding spheres.

.. py:property:: path_point
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.path_point
    :type: IAgStkGraphicsPathPointFactory

    Factory creates path points.

.. py:property:: text_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.text_overlay
    :type: IAgStkGraphicsTextOverlayFactory

    Access global methods and properties of TextOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: agi_custom_terrain_overlay
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.agi_custom_terrain_overlay
    :type: IAgStkGraphicsAGICustomTerrainOverlayFactory

    Access global methods and properties of AGICustomTerrainOverlay (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: axes_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.axes_primitive
    :type: IAgStkGraphicsAxesPrimitiveFactory

    Access global methods and properties of AxesPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: vector_primitive
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.vector_primitive
    :type: IAgStkGraphicsVectorPrimitiveFactory

    Access global methods and properties of VectorPrimitive (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: polyline_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.polyline_primitive_optional_parameters
    :type: IAgStkGraphicsPolylinePrimitiveOptionalParametersFactory

    Access global methods and properties of PolylinePrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).

.. py:property:: point_batch_primitive_optional_parameters
    :canonical: ansys.stk.core.graphics.IFactoryAndInitializers.point_batch_primitive_optional_parameters
    :type: IAgStkGraphicsPointBatchPrimitiveOptionalParametersFactory

    Access global methods and properties of PointBatchPrimitiveOptionalParameters (what's known as static properties, static methods and constructors in languages such as C++, C#, etc.).


