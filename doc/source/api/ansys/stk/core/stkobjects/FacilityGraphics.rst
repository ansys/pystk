FacilityGraphics
================

.. py:class:: ansys.stk.core.stkobjects.FacilityGraphics

   2D Graphics properties of a Facility.

.. py:currentmodule:: FacilityGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.inherit_from_scenario`
              - Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.color`
              - The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.marker_style`
              - The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.show_label`
              - Display the label for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.az_el_mask`
              - The graphics az-el mask properties for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.contours`
              - The range contours properties for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.use_instance_name_label`
              - Use the name of the object as the label for the facility, place or target.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.label_name`
              - Use a user-specified name as the label for the facility, place or target. This does not have to correspond to the name of the object in the Object Browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.marker_color`
              - The color in which the marker for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.label_color`
              - The color in which the label for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.show_graphics`
              - Specify whether graphics attributes of the facility are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.FacilityGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FacilityGraphics


Property detail
---------------

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.inherit_from_scenario
    :type: bool

    Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility, place or target.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.color
    :type: agcolor.Color

    The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.marker_style
    :type: str

    The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.show_label
    :type: bool

    Display the label for the facility, place or target.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.az_el_mask
    :type: BasicAzElMask

    The graphics az-el mask properties for the facility, place or target.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.contours
    :type: Graphics2DRangeContours

    The range contours properties for the facility, place or target.

.. py:property:: use_instance_name_label
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.use_instance_name_label
    :type: bool

    Use the name of the object as the label for the facility, place or target.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.label_name
    :type: str

    Use a user-specified name as the label for the facility, place or target. This does not have to correspond to the name of the object in the Object Browser.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_color
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.marker_color
    :type: agcolor.Color

    The color in which the marker for the object is displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.label_color
    :type: agcolor.Color

    The color in which the label for the object is displayed.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the facility are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.FacilityGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.


