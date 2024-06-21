IPlanetGraphics
===============

.. py:class:: ansys.stk.core.stkobjects.IPlanetGraphics

   object
   
   AgPlGraphics used to access the 2D graphics of the planet.

.. py:currentmodule:: IPlanetGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.inherit`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.color`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.sub_planet_label_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.position_label_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.marker_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.inertial_position_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.sub_planet_point_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.orbit_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.orbit_display`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.orbit_display_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.line_style`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.line_width`
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanetGraphics.is_object_graphics_visible`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlanetGraphics


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.inherit
    :type: bool

    Specify whether inheritable 2D Graphics attributes are inherited from Scenario-level settings.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.color
    :type: agcolor.Color

    The color in which the planet's marker, label and orbit path (if any) are displayed.

.. py:property:: sub_planet_label_visible
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.sub_planet_label_visible
    :type: bool

    Specify whether a label displays for the point on the Earth directly below the planet.

.. py:property:: position_label_visible
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.position_label_visible
    :type: bool

    Specify whether a label displays for the inertial position of the planet. This option affects only the perspective and orthographic map projections.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.marker_style
    :type: str

    The style of the marker representing the planet.

.. py:property:: inertial_position_visible
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.inertial_position_visible
    :type: bool

    Specify whether the position of the planet displays in the 2D Graphics window in the Central-Body Inertial (CBI) coordinate frame. This option affects only the perspective and orthographic map projections.

.. py:property:: sub_planet_point_visible
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.sub_planet_point_visible
    :type: bool

    Specify whether the point on the Earth directly below the planet displays in the 2D Graphics window.

.. py:property:: orbit_visible
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.orbit_visible
    :type: bool

    Specify whether the planet's orbit path displays. This option affects only the perspective and orthographic map projections.

.. py:property:: orbit_display
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.orbit_display
    :type: PLANET_ORBIT_DISPLAY_TYPE

    The factor used in determining how much of the orbit displays. A member of the AgEPlOrbitDisplayType enumeration.

.. py:property:: orbit_display_data
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.orbit_display_data
    :type: IOrbitDisplayData

    If time is used to determine how much of the orbit displays, specify a time value.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.line_style
    :type: LINE_STYLE

    The type of line to represent the object's pattern or tracks.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.line_width
    :type: LINE_WIDTH

    The width of the line to represent the object's pattern or tracks.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.IPlanetGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the planet are visible.


