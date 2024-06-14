IPlaceGraphics
==============

.. py:class:: IPlaceGraphics

   object
   
   IAgPlaceGraphics used to access the 2-d graphics properties for a Place object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~inherit_from_scenario`
            * - :py:meth:`~color`
            * - :py:meth:`~marker_style`
            * - :py:meth:`~label_visible`
            * - :py:meth:`~az_el_mask`
            * - :py:meth:`~contours`
            * - :py:meth:`~use_inst_name_label`
            * - :py:meth:`~label_name`
            * - :py:meth:`~label_notes`
            * - :py:meth:`~marker_color`
            * - :py:meth:`~label_color`
            * - :py:meth:`~is_object_graphics_visible`
            * - :py:meth:`~radar_cross_section`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlaceGraphics


Property detail
---------------

.. py:property:: inherit_from_scenario
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.inherit_from_scenario
    :type: bool

    Inheritable graphics attributes are inherited from the Scenario object instead of being set locally for the facility or place.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.color
    :type: agcolor.Color

    The color in which the marker and label for the object is displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.marker_style
    :type: str

    The style of the marker representing the object in the 2D Graphics window. A member of the MarkerStyle enumeration.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.label_visible
    :type: bool

    Display the label for the place.

.. py:property:: az_el_mask
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.az_el_mask
    :type: "IAgBasicAzElMask"

    The graphics az-el mask properties for the place.

.. py:property:: contours
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.contours
    :type: "IAgGfxRangeContours"

    The range contours properties for the place.

.. py:property:: use_inst_name_label
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.use_inst_name_label
    :type: bool

    Use the name of the object as the label for the place.

.. py:property:: label_name
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.label_name
    :type: str

    Use a user-specified name as the label for the place. This does not have to correspond to the name of the object in the Object Browser.

.. py:property:: label_notes
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.label_notes
    :type: "IAgLabelNoteCollection"

    Notes attached to the object and displayed in the 2D and 3D Graphics windows.

.. py:property:: marker_color
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.marker_color
    :type: agcolor.Color

    The color in which the marker for the object is displayed.

.. py:property:: label_color
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.label_color
    :type: agcolor.Color

    The color in which the label for the object is displayed.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the place are visible.

.. py:property:: radar_cross_section
    :canonical: ansys.stk.core.stkobjects.IPlaceGraphics.radar_cross_section
    :type: "IAgRadarCrossSectionGraphics"

    Gets the radar cross section graphics interface.


