IMissileGraphics
================

.. py:class:: ansys.stk.core.stkobjects.IMissileGraphics

   object
   
   2D Graphics for missiles.

.. py:currentmodule:: IMissileGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.set_attributes_type`
              - Set the type of display.
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.attributes_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.attributes_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.attributes`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.pass_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.elev_contours`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.ground_ellipses`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.range_contours`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.lighting`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.swath`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.label_notes`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.use_inst_name_label`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.label_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.saa`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.is_object_graphics_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IMissileGraphics.radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IMissileGraphics


Property detail
---------------

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.attributes_type
    :type: VEHICLE_GRAPHICS_2D_ATTRIBUTES

    Type of display: basic, during access intervals, during custom intervals, or real time.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.attributes
    :type: IVehicleGraphics2DAttributes

    Get the 2D Graphics attributes.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.pass_data
    :type: IVehicleGraphics2DTrajectoryPassData

    Get the 2D trajectory graphics.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.resolution
    :type: IVehicleGraphics2DTrajectoryResolution

    Get the resolution graphics.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.elev_contours
    :type: IVehicleGraphics2DElevContours

    Get the elevation contours graphics.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.ground_ellipses
    :type: IVehicleGraphics2DGroundEllipsesCollection

    Get the ground ellipses graphics.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.range_contours
    :type: IGraphics2DRangeContours

    Get the range contour graphics.

.. py:property:: lighting
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.lighting
    :type: IVehicleGraphics2DLighting

    Get the lighting graphics.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.swath
    :type: IVehicleGraphics2DSwath

    Get the swath graphics.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.label_notes
    :type: ILabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.use_inst_name_label
    :type: bool

    Specify whether to use the name of the missile (as shown in the Object Browser) as its label.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.label_name
    :type: str

    The user-specified name to use as a label for the missile.

.. py:property:: saa
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.saa
    :type: IVehicleGraphics2DSAA

    Get the missile's South Atlantic Anomaly Contour properties.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the missile are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.radar_cross_section
    :type: IRadarCrossSectionGraphics

    Gets the radar cross section graphics interface.


Method detail
-------------


.. py:method:: set_attributes_type(self, attributes: VEHICLE_GRAPHICS_2D_ATTRIBUTES) -> None
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.set_attributes_type

    Set the type of display.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_2D_ATTRIBUTES`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VEHICLE_GRAPHICS_2D_ATTRIBUTES) -> bool
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_2D_ATTRIBUTES`

    :Returns:

        :obj:`~bool`



















