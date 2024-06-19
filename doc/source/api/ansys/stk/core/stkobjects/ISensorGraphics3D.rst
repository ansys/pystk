ISensorGraphics3D
=================

.. py:class:: ISensorGraphics3D

   object
   
   IAgSnVO Interface for a sensor's 3D Graphics properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~boresight_marker_visible`
            * - :py:meth:`~radial_lines_visible`
            * - :py:meth:`~translucent_lines_visible`
            * - :py:meth:`~percent_translucency`
            * - :py:meth:`~projection_type`
            * - :py:meth:`~space_projection`
            * - :py:meth:`~targeting`
            * - :py:meth:`~enable_const_ext_length`
            * - :py:meth:`~enable_range_constraint`
            * - :py:meth:`~pulse`
            * - :py:meth:`~vertex_offset`
            * - :py:meth:`~data_displays`
            * - :py:meth:`~vector`
            * - :py:meth:`~fill_visible`
            * - :py:meth:`~fill_translucency`
            * - :py:meth:`~inherit_from_2d`
            * - :py:meth:`~is_targeted`
            * - :py:meth:`~space_projection_intervals`
            * - :py:meth:`~target_projection_intervals`
            * - :py:meth:`~fill_resolution`
            * - :py:meth:`~persist_projected_lines_in_space`
            * - :py:meth:`~persist_partial_central_body_intersection_lines`
            * - :py:meth:`~projection_time_dependency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorGraphics3D


Property detail
---------------

.. py:property:: boresight_marker_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.boresight_marker_visible
    :type: bool

    Opt whether to display the sensor's boresight marker.

.. py:property:: radial_lines_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.radial_lines_visible
    :type: bool

    Opt whether to display radial lines, i.e. a series of solid lines extending from the vertex to the base of the sensor.

.. py:property:: translucent_lines_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.translucent_lines_visible
    :type: bool

    Opt whether sensor lines are set to the translucency of the cone.Otherwise, the sensor and radial lines are solid.

.. py:property:: percent_translucency
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.percent_translucency
    :type: float

    Specify the percent translucency of the sensor projection. Translucency ranges from 0 to 100 percent, where 100 percent is invisible. Dimensionless.

.. py:property:: projection_type
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.projection_type
    :type: SENSOR_GRAPHICS_3D_PROJECTION_TYPE

    Select the projection type from the AgESnVOProjectionType enumeration.

.. py:property:: space_projection
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.space_projection
    :type: float

    Length of the sensor's projection when it is not intersecting the Earth. In this case, distance is computed so that the projection of the outermost point on the contour along the boresight is equal to the specified distance. Uses Distance Dimension.

.. py:property:: targeting
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.targeting
    :type: float

    For a targeted sensor, specify the targeting distance, or how far past the target a sensor is projected (typically zero). Uses Distance Dimension.

.. py:property:: enable_const_ext_length
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.enable_const_ext_length
    :type: bool

    Opt whether to use the extension distance as the maximum, i.e. to scale the maximum distance drawn along the sensor boundary to the targeting extension distance for a targeting sensor or the space projection extension distance for a non-targeting sensor.

.. py:property:: enable_range_constraint
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.enable_range_constraint
    :type: bool

    If a range constraint has been imposed on the sensor, opt whether the sensor graphics display a dome-shaped cap on the end of the sensor projection.

.. py:property:: pulse
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.pulse
    :type: IAgSnVOPulse

    Get the sensor's Pulse properties.

.. py:property:: vertex_offset
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.vertex_offset
    :type: IAgSnVOOffset

    Get the sensor's Vertex Offset properties.

.. py:property:: data_displays
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.data_displays
    :type: IAgVODataDisplayCollection

    Get the sensor's Data Display properties.

.. py:property:: vector
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.vector
    :type: IAgVOVector

    Get the sensor's Vector properties.

.. py:property:: fill_visible
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.fill_visible
    :type: bool

    Opt whether to display fill for the sensor projection, i.e. to display the sensor's footprint as a filled area on the surface of the central body.

.. py:property:: fill_translucency
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.fill_translucency
    :type: float

    Specify the fill translucency percentage for the sensor. Dimensionless.

.. py:property:: inherit_from_2d
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.inherit_from_2d
    :type: SENSOR_GRAPHICS_3D_INHERIT_FROM_2D

    Specify how projection distances that are computed based on 2D Graphics projection settings are displayed in the 3D Graphics window.

.. py:property:: is_targeted
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.is_targeted
    :type: bool

    Is the sensor targeted?

.. py:property:: space_projection_intervals
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.space_projection_intervals
    :type: IAgSnVOSpaceProjectionCollection

    Returns time dependent space projection list.

.. py:property:: target_projection_intervals
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.target_projection_intervals
    :type: IAgSnVOTargetProjectionCollection

    Returns time dependent target projection list.

.. py:property:: fill_resolution
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.fill_resolution
    :type: float

    Specify the fill resolution angle for the sensor. Dimensionless.

.. py:property:: persist_projected_lines_in_space
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.persist_projected_lines_in_space
    :type: bool

    Persist projected lines in space.

.. py:property:: persist_partial_central_body_intersection_lines
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.persist_partial_central_body_intersection_lines
    :type: bool

    Persist partial central body intersection lines.

.. py:property:: projection_time_dependency
    :canonical: ansys.stk.core.stkobjects.ISensorGraphics3D.projection_time_dependency
    :type: SENSOR_GRAPHICS_3D_PROJECTION_TIME_DEPENDENCY_TYPE

    Specify how projection distances are determined in the 3D Graphics window. Either using a constant distance at all times or set of user defined intervals and distance values.


