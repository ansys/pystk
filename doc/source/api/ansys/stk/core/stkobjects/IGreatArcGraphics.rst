IGreatArcGraphics
=================

.. py:class:: IGreatArcGraphics

   object
   
   2D Graphics common for all Great Arc Vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_attributes_type`
              - Set the 2D Graphics attributes type for the vehicle.
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
            * - :py:meth:`~waypoint_marker`
            * - :py:meth:`~resolution`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~lighting`
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~label_notes`
            * - :py:meth:`~use_inst_name_label`
            * - :py:meth:`~label_name`
            * - :py:meth:`~is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGreatArcGraphics


Property detail
---------------

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.attributes_type
    :type: "VEHICLE_GRAPHICS_2D_ATTRIBUTES"

    Get the 2D Graphics attributes type for the vehicle: basic, access intervals, custom intervals, or real time.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.attributes
    :type: "IAgVeGfxAttributes"

    Get the vehicle's 2D Graphics attributes.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.pass_data
    :type: "IAgVeGfxRoutePassData"

    Get the vehicle's 2D route graphics.

.. py:property:: waypoint_marker
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.waypoint_marker
    :type: "IAgVeGfxWaypointMarker"

    Get the vehicle's 2D waypoint marker graphics.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.resolution
    :type: "IAgVeGfxRouteResolution"

    Get the vehicle's 2D resolution graphics.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.range_contours
    :type: "IAgGfxRangeContours"

    Get the vehicle's 2D range contour graphics.

.. py:property:: lighting
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.lighting
    :type: "IAgVeGfxLighting"

    Get the vehicle's 2D lighting graphics.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.ground_ellipses
    :type: "IAgVeGfxGroundEllipsesCollection"

    Get the vehicle's 2D ground ellipses graphics.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.label_notes
    :type: "IAgLabelNoteCollection"

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.use_inst_name_label
    :type: bool

    Specify whether to use the name of the vehicle (as shown in the Object Browser) as its label.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.label_name
    :type: str

    The user-specified name to use as a label for the vehicle.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IGreatArcGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the vehicle are visible.


Method detail
-------------


.. py:method:: set_attributes_type(self, attributes:"VEHICLE_GRAPHICS_2D_ATTRIBUTES") -> None

    Set the 2D Graphics attributes type for the vehicle.

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
















