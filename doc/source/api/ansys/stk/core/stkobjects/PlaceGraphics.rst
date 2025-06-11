PlaceGraphics
=============

.. py:class:: ansys.stk.core.stkobjects.PlaceGraphics

   2D Graphics properties of a Place.

.. py:currentmodule:: PlaceGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.inherit_from_scenario`
              - Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility or place.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.color`
              - The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.marker_style`
              - The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.show_label`
              - Display the label for the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.az_el_mask`
              - The graphics az-el mask properties for the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.contours`
              - The range contours properties for the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.use_instance_name_label`
              - Use the name of the object as the label for the place.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.label_name`
              - Use a user-specified name as the label for the place. This does not have to correspond to the name of the object in the Object Browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.label_notes`
              - Notes attached to the object and displayed in the 2D and 3D Graphics windows.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.marker_color`
              - The color in which the marker for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.label_color`
              - The color in which the label for the object is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.show_graphics`
              - Specify whether graphics attributes of the place are visible.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlaceGraphics.radar_cross_section`
              - Get the radar cross section graphics interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PlaceGraphics


Property detail
---------------

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.inherit_from_scenario
    :type: bool

    Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility or place.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.color
    :type: agcolor.Color

    The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.marker_style
    :type: str

    The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.

.. py:property:: show_label
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.show_label
    :type: bool

    Display the label for the place.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.az_el_mask
    :type: BasicAzElMask

    The graphics az-el mask properties for the place.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.contours
    :type: Graphics2DRangeContours

    The range contours properties for the place.

.. py:property:: use_instance_name_label
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.use_instance_name_label
    :type: bool

    Use the name of the object as the label for the place.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.label_name
    :type: str

    Use a user-specified name as the label for the place. This does not have to correspond to the name of the object in the Object Browser.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.label_notes
    :type: LabelNoteCollection

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_color
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.marker_color
    :type: agcolor.Color

    The color in which the marker for the object is displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.label_color
    :type: agcolor.Color

    The color in which the label for the object is displayed.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the place are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.PlaceGraphics.radar_cross_section
    :type: RadarCrossSectionGraphics

    Get the radar cross section graphics interface.


