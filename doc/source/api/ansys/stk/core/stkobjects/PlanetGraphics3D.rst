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
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.inertial_position_visible`
              - Display the position of the planet as a point.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.sub_planet_point_visible`
              - Display the location at which the planet is overhead on the globe.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.position_label_visible`
              - Display a label at the inertial position of the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.sub_planet_label_visible`
              - Display a label on the globe at the location at which the planet is overhead.
            * - :py:attr:`~ansys.stk.core.stkobjects.PlanetGraphics3D.orbit_visible`
              - Display the planet's orbit around its parent object in the 3D graphics window as defined in 2D Graphics for that planet. For instance, the Moon orbits around the Sun.



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

.. py:property:: inertial_position_visible
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.inertial_position_visible
    :type: bool

    Display the position of the planet as a point.

.. py:property:: sub_planet_point_visible
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.sub_planet_point_visible
    :type: bool

    Display the location at which the planet is overhead on the globe.

.. py:property:: position_label_visible
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.position_label_visible
    :type: bool

    Display a label at the inertial position of the planet.

.. py:property:: sub_planet_label_visible
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.sub_planet_label_visible
    :type: bool

    Display a label on the globe at the location at which the planet is overhead.

.. py:property:: orbit_visible
    :canonical: ansys.stk.core.stkobjects.PlanetGraphics3D.orbit_visible
    :type: bool

    Display the planet's orbit around its parent object in the 3D graphics window as defined in 2D Graphics for that planet. For instance, the Moon orbits around the Sun.


