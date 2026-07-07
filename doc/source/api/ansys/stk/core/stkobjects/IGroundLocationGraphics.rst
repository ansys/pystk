IGroundLocationGraphics
=======================

.. py:class:: ansys.stk.core.stkobjects.IGroundLocationGraphics

   IGroundLocationGraphics used to access the 2-d graphics properties for a ground location.

.. py:currentmodule:: IGroundLocationGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.az_el_mask`
              - The graphics az-el mask properties for the ground location.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.color`
              - The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.contours`
              - The range contours properties for the ground location.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.inherit_from_scenario`
              - Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the ground location.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.label_color`
              - The color in which the label for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.label_name`
              - Use a user-specified name as the label for the ground location. This does not have to correspond to the name of the object in the Object Browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.marker_color`
              - The color in which the marker for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.marker_style`
              - The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.show_graphics`
              - Specify whether graphics attributes of the ground location are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.show_label`
              - Display the label for the ground location.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundLocationGraphics.use_instance_name_label`
              - Use the name of the object as the label for the ground location.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGroundLocationGraphics


Property detail
---------------

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.az_el_mask
    :type: BasicAzElMask

    The graphics az-el mask properties for the ground location.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.color
    :type: Color

    The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.contours
    :type: Graphics2DRangeContours

    The range contours properties for the ground location.

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.inherit_from_scenario
    :type: bool

    Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the ground location.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.label_color
    :type: Color

    The color in which the label for the object is displayed.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.label_name
    :type: str

    Use a user-specified name as the label for the ground location. This does not have to correspond to the name of the object in the Object Browser.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_color
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.marker_color
    :type: Color

    The color in which the marker for the object is displayed.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.marker_style
    :type: str

    The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the ground location are visible.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.show_label
    :type: bool

    Display the label for the ground location.

.. py:property:: use_instance_name_label
    :canonical: ansys.stk.core.stkobjects.IGroundLocationGraphics.use_instance_name_label
    :type: bool

    Use the name of the object as the label for the ground location.


