IMissileGraphics
================

.. py:class:: IMissileGraphics

   object
   
   2D Graphics for missiles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_attributes_type`
              - Set the type of display.
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
            * - :py:meth:`~ground_ellipses`
            * - :py:meth:`~range_contours`
            * - :py:meth:`~lighting`
            * - :py:meth:`~swath`
            * - :py:meth:`~label_notes`
            * - :py:meth:`~use_inst_name_label`
            * - :py:meth:`~label_name`
            * - :py:meth:`~saa`
            * - :py:meth:`~is_object_graphics_visible`
            * - :py:meth:`~radar_cross_section`


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
    :type: IAgVeGfxAttributes

    Get the 2D Graphics attributes.

.. py:property:: pass_data
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.pass_data
    :type: IAgVeGfxTrajectoryPassData

    Get the 2D trajectory graphics.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.resolution
    :type: IAgVeGfxTrajectoryResolution

    Get the resolution graphics.

.. py:property:: elev_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.elev_contours
    :type: IAgVeGfxElevContours

    Get the elevation contours graphics.

.. py:property:: ground_ellipses
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.ground_ellipses
    :type: IAgVeGfxGroundEllipsesCollection

    Get the ground ellipses graphics.

.. py:property:: range_contours
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.range_contours
    :type: IAgGfxRangeContours

    Get the range contour graphics.

.. py:property:: lighting
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.lighting
    :type: IAgVeGfxLighting

    Get the lighting graphics.

.. py:property:: swath
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.swath
    :type: IAgVeGfxSwath

    Get the swath graphics.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.label_notes
    :type: IAgLabelNoteCollection

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
    :type: IAgVeGfxSAA

    Get the missile's South Atlantic Anomaly Contour properties.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the missile are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IMissileGraphics.radar_cross_section
    :type: IAgRadarCrossSectionGraphics

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



















