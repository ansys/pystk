PlanetGraphics
==============

.. py:class:: ansys.stk.core.stkobjects.PlanetGraphics

   Class defining 2D Graphics properties of a Planet.

.. py:currentmodule:: PlanetGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.inherit`
              - Specify whether inheritable 2D Graphics attributes are inherited from Scenario-level settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.color`
              - The color in which the planet's marker, label and orbit path (if any) are displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.show_sub_planet_label`
              - Specify whether a label displays for the point on the Earth directly below the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.show_position_label`
              - Specify whether a label displays for the inertial position of the planet. This option affects only the perspective and orthographic map projections.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.marker_style`
              - The style of the marker representing the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.show_inertial_position`
              - Specify whether the position of the planet displays in the 2D Graphics window in the Central-Body Inertial (CBI) coordinate frame. This option affects only the perspective and orthographic map projections.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.show_sub_planet_point`
              - Specify whether the point on the Earth directly below the planet displays in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.show_orbit`
              - Specify whether the planet's orbit path displays. This option affects only the perspective and orthographic map projections.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.orbit_display`
              - The factor used in determining how much of the orbit displays. A member of the PlanetOrbitDisplayType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.orbit_display_data`
              - If time is used to determine how much of the orbit displays, specify a time value.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.line_style`
              - The type of line to represent the object's pattern or tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.line_width`
              - The width of the line to represent the object's pattern or tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics.show_graphics`
              - Specify whether graphics attributes of the planet are visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PlanetGraphics


Property detail
---------------

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.inherit
    :type: bool

    Specify whether inheritable 2D Graphics attributes are inherited from Scenario-level settings.

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.color
    :type: agcolor.Color

    The color in which the planet's marker, label and orbit path (if any) are displayed.

.. py:property:: show_sub_planet_label
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.show_sub_planet_label
    :type: bool

    Specify whether a label displays for the point on the Earth directly below the planet.

.. py:property:: show_position_label
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.show_position_label
    :type: bool

    Specify whether a label displays for the inertial position of the planet. This option affects only the perspective and orthographic map projections.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.marker_style
    :type: str

    The style of the marker representing the planet.

.. py:property:: show_inertial_position
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.show_inertial_position
    :type: bool

    Specify whether the position of the planet displays in the 2D Graphics window in the Central-Body Inertial (CBI) coordinate frame. This option affects only the perspective and orthographic map projections.

.. py:property:: show_sub_planet_point
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.show_sub_planet_point
    :type: bool

    Specify whether the point on the Earth directly below the planet displays in the 2D Graphics window.

.. py:property:: show_orbit
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.show_orbit
    :type: bool

    Specify whether the planet's orbit path displays. This option affects only the perspective and orthographic map projections.

.. py:property:: orbit_display
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.orbit_display
    :type: PlanetOrbitDisplayType

    The factor used in determining how much of the orbit displays. A member of the PlanetOrbitDisplayType enumeration.

.. py:property:: orbit_display_data
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.orbit_display_data
    :type: IOrbitDisplayData

    If time is used to determine how much of the orbit displays, specify a time value.

.. py:property:: line_style
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.line_style
    :type: LineStyle

    The type of line to represent the object's pattern or tracks.

.. py:property:: line_width
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.line_width
    :type: LineWidth

    The width of the line to represent the object's pattern or tracks.

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics.show_graphics
    :type: bool

    Specify whether graphics attributes of the planet are visible.


