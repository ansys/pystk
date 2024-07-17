StarGraphics3D
==============

.. py:class:: ansys.stk.core.stkobjects.StarGraphics3D

   Bases: 

   Class defining 3D Graphics properties of a Star.

.. py:currentmodule:: StarGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.inertial_position_visible`
              - Display the inertial position of the star, i.e. its position on the celestial sphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.sub_star_point_visible`
              - Display the location at which the star is overhead on the globe.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.inherit_from_2d_graphics_2d`
              - Specify whether star properties set for 2D Graphics are used in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.position_label_visible`
              - Display a label on the globe at the inertial position of the star.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.sub_star_label_visible`
              - Display a label at the location at which the star is overhead.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StarGraphics3D


Property detail
---------------

.. py:property:: inertial_position_visible
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.inertial_position_visible
    :type: bool

    Display the inertial position of the star, i.e. its position on the celestial sphere.

.. py:property:: sub_star_point_visible
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.sub_star_point_visible
    :type: bool

    Display the location at which the star is overhead on the globe.

.. py:property:: inherit_from_2d_graphics_2d
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.inherit_from_2d_graphics_2d
    :type: bool

    Specify whether star properties set for 2D Graphics are used in the 3D Graphics window.

.. py:property:: position_label_visible
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.position_label_visible
    :type: bool

    Display a label on the globe at the inertial position of the star.

.. py:property:: sub_star_label_visible
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.sub_star_label_visible
    :type: bool

    Display a label at the location at which the star is overhead.


