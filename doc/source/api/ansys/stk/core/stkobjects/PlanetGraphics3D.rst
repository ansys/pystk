PlanetGraphics3D
================

.. py:class:: ansys.stk.core.stkobjects.PlanetGraphics3D

   Class defining 3D Graphics properties of a Planet.

.. py:currentmodule:: PlanetGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.inherit_from_2d_graphics_2d`
              - Specify whether planet properties set for 2D Graphics are used in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.show_inertial_position`
              - Display the position of the planet as a point.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.show_orbit`
              - Display the planet's orbit around its parent object in the 3D graphics window as defined in 2D Graphics for that planet. For instance, the Moon orbits around the Sun.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.show_position_label`
              - Display a label at the inertial position of the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.show_sub_planet_label`
              - Display a label on the globe at the location at which the planet is overhead.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.show_sub_planet_point`
              - Display the location at which the planet is overhead on the globe.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PlanetGraphics3D


Property detail
---------------

.. py:property:: inherit_from_2d_graphics_2d
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.inherit_from_2d_graphics_2d
    :type: bool

    Specify whether planet properties set for 2D Graphics are used in the 3D Graphics window.

.. py:property:: show_inertial_position
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.show_inertial_position
    :type: bool

    Display the position of the planet as a point.

.. py:property:: show_orbit
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.show_orbit
    :type: bool

    Display the planet's orbit around its parent object in the 3D graphics window as defined in 2D Graphics for that planet. For instance, the Moon orbits around the Sun.

.. py:property:: show_position_label
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.show_position_label
    :type: bool

    Display a label at the inertial position of the planet.

.. py:property:: show_sub_planet_label
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.show_sub_planet_label
    :type: bool

    Display a label on the globe at the location at which the planet is overhead.

.. py:property:: show_sub_planet_point
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.show_sub_planet_point
    :type: bool

    Display the location at which the planet is overhead on the globe.


