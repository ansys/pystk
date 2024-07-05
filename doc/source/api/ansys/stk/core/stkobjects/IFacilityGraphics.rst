IFacilityGraphics
=================

.. py:class:: ansys.stk.core.stkobjects.IFacilityGraphics

   object
   
   AgFaGraphics used to access the 2D graphics for a Facility object interface.

.. py:currentmodule:: IFacilityGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.inherit_from_scenario`
              - Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.color`
              - The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.marker_style`
              - The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.label_visible`
              - Display the label for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.az_el_mask`
              - The graphics az-el mask properties for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.contours`
              - The range contours properties for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.use_inst_name_label`
              - Use the name of the object as the label for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.label_name`
              - Use a user-specified name as the label for the facility, place or target. This does not have to correspond to the name of the object in the Object Browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.marker_color`
              - The color in which the marker for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.label_color`
              - The color in which the label for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.is_object_graphics_visible`
              - Specify whether graphics attributes of the facility are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFacilityGraphics.radar_cross_section`
              - Gets the radar cross section graphics interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFacilityGraphics


Property detail
---------------

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.inherit_from_scenario
    :type: bool

    Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility, place or target.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.color
    :type: agcolor.Color

    The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.marker_style
    :type: str

    The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.label_visible
    :type: bool

    Display the label for the facility, place or target.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.az_el_mask
    :type: IBasicAzElMask

    The graphics az-el mask properties for the facility, place or target.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.contours
    :type: IGraphics2DRangeContours

    The range contours properties for the facility, place or target.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.use_inst_name_label
    :type: bool

    Use the name of the object as the label for the facility, place or target.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.label_name
    :type: str

    Use a user-specified name as the label for the facility, place or target. This does not have to correspond to the name of the object in the Object Browser.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.label_notes
    :type: ILabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_color
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.marker_color
    :type: agcolor.Color

    The color in which the marker for the object is displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.label_color
    :type: agcolor.Color

    The color in which the label for the object is displayed.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the facility are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IFacilityGraphics.radar_cross_section
    :type: IRadarCrossSectionGraphics

    Gets the radar cross section graphics interface.


