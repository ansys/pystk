ILaunchVehicleGraphics
======================

.. py:class:: ILaunchVehicleGraphics

   object
   
   2D Graphics for a launch vehicle.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_attributes_type`
              - Set the 2D Graphics attributes type.
            * - :py:meth:`~is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~attributes_type`
            * - :py:meth:`~attributes_supported_types`
            * - :py:meth:`~attributes`
            * - :py:meth:`~pass_data`
            * - :py:meth:`~resolution`
            * - :py:meth:`~elev_contours`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~lighting`
            * - :py:meth:`~swath`
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~use_inst_name`
            * - :py:meth:`~label_notes`
            * - :py:meth:`~use_inst_name_label`
            * - :py:meth:`~label_name`
            * - :py:meth:`~saa`
            * - :py:meth:`~is_object_graphics_visible`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILaunchVehicleGraphics


Property detail
---------------

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.attributes_type
    :type: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"

    Get the 2D Graphics attributes type: basic, access intervals, custom intervals, or real time.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.attributes
    :type: "IAgVeGfxAttributes"

    Get the launch vehicle's 2D Graphics attributes.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.pass_data
    :type: "IAgVeGfxTrajectoryPassData"

    Get the launch vehicle's 2D trajectory properties.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.resolution
    :type: "IAgVeGfxTrajectoryResolution"

    Get the launch vehicle's 2D resolution properties.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.elev_contours
    :type: "IAgVeGfxElevContours"

    Get the launch vehicle's 2D elevation contour properties.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.range_contours
    :type: "IAgGfxRangeContours"

    Get the launch vehicle's 2D range contour properties.

.. py:property:: lighting
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.lighting
    :type: "IAgVeGfxLighting"

    Get the launch vehicle's 2D lighting properties.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.swath
    :type: "IAgVeGfxSwath"

    Get the launch vehicle's 2D swath properties.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.ground_ellipses
    :type: "IAgVeGfxGroundEllipsesCollection"

    Get the launch vehicle's 2D ground ellipses properties.

.. py:property:: use_inst_name
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.use_inst_name
    :type: bool

    Opt whether to use the instance name as the label.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.label_notes
    :type: "IAgLabelNoteCollection"

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.use_inst_name_label
    :type: bool

    Specify whether to use the name of the launch vehicle (as shown in the Object Browser) as its label.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.label_name
    :type: str

    The user-specified name to use as a label for the launch vehicle.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.saa
    :type: "IAgVeGfxSAA"

    Get the vehicle's South Atlantic Anomaly Contour properties.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the launch vehicle are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.ILaunchVehicleGraphics.radar_cross_section
    :type: "IAgRadarCrossSectionGraphics"

    Gets the radar cross section graphics interface.


Method detail
-------------


.. py:method:: set_attributes_type(self, attributes:"VEHICLE_GRAPHICS_2D_ATTRIBUTES") -> None

    Set the 2D Graphics attributes type.

    :Parameters:

    **attributes** : :obj:`~"VEHICLE_GRAPHICS_2D_ATTRIBUTES"`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes:"VEHICLE_GRAPHICS_2D_ATTRIBUTES") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~"VEHICLE_GRAPHICS_2D_ATTRIBUTES"`

    :Returns:

        :obj:`~bool`





















