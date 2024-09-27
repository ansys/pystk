LaunchVehicleGraphics
=====================

.. py:class:: ansys.stk.core.stkobjects.LaunchVehicleGraphics

   2D Graphics for a launch vehicle.

.. py:currentmodule:: LaunchVehicleGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.set_attributes_type`
              - Set the 2D Graphics attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.attributes_type`
              - Get the 2D Graphics attributes type: basic, access intervals, custom intervals, or real time.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.attributes_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.attributes`
              - Get the launch vehicle's 2D Graphics attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.pass_data`
              - Get the launch vehicle's 2D trajectory properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.resolution`
              - Get the launch vehicle's 2D resolution properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.elev_contours`
              - Get the launch vehicle's 2D elevation contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.range_contours`
              - Get the launch vehicle's 2D range contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.lighting`
              - Get the launch vehicle's 2D lighting properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.swath`
              - Get the launch vehicle's 2D swath properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.ground_ellipses`
              - Get the launch vehicle's 2D ground ellipses properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.use_inst_name`
              - Opt whether to use the instance name as the label.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.use_inst_name_label`
              - Specify whether to use the name of the launch vehicle (as shown in the Object Browser) as its label.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.label_name`
              - The user-specified name to use as a label for the launch vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.saa`
              - Get the vehicle's South Atlantic Anomaly Contour properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.is_object_graphics_visible`
              - Specify whether graphics attributes of the launch vehicle are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.LaunchVehicleGraphics.radar_cross_section`
              - Gets the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LaunchVehicleGraphics


Property detail
---------------

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.attributes_type
    :type: VEHICLE_GRAPHICS_2D_ATTRIBUTES

    Get the 2D Graphics attributes type: basic, access intervals, custom intervals, or real time.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.attributes
    :type: IVehicleGraphics2DAttributes

    Get the launch vehicle's 2D Graphics attributes.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.pass_data
    :type: VehicleGraphics2DTrajectoryPassData

    Get the launch vehicle's 2D trajectory properties.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.resolution
    :type: VehicleGraphics2DTrajectoryResolution

    Get the launch vehicle's 2D resolution properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.elev_contours
    :type: VehicleGraphics2DElevContours

    Get the launch vehicle's 2D elevation contour properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.range_contours
    :type: Graphics2DRangeContours

    Get the launch vehicle's 2D range contour properties.

.. py:property:: lighting
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.lighting
    :type: VehicleGraphics2DLighting

    Get the launch vehicle's 2D lighting properties.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.swath
    :type: VehicleGraphics2DSwath

    Get the launch vehicle's 2D swath properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.ground_ellipses
    :type: VehicleGraphics2DGroundEllipsesCollection

    Get the launch vehicle's 2D ground ellipses properties.

.. py:property:: use_inst_name
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.use_inst_name
    :type: bool

    Opt whether to use the instance name as the label.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.use_inst_name_label
    :type: bool

    Specify whether to use the name of the launch vehicle (as shown in the Object Browser) as its label.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.label_name
    :type: str

    The user-specified name to use as a label for the launch vehicle.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.saa
    :type: VehicleGraphics2DSAA

    Get the vehicle's South Atlantic Anomaly Contour properties.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the launch vehicle are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Gets the radar cross section graphics interface.


Method detail
-------------


.. py:method:: set_attributes_type(self, attributes: VEHICLE_GRAPHICS_2D_ATTRIBUTES) -> None
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.set_attributes_type

    Set the 2D Graphics attributes type.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_2D_ATTRIBUTES`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VEHICLE_GRAPHICS_2D_ATTRIBUTES) -> bool
    :canonical: ansys.stk.core.stkobjects.LaunchVehicleGraphics.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_2D_ATTRIBUTES`

    :Returns:

        :obj:`~bool`





















