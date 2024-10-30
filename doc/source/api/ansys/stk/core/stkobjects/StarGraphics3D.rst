StarGraphics3D
==============

.. py:class:: ansys.stk.core.stkobjects.StarGraphics3D

   Class defining 3D Graphics properties of a Star.

.. py:currentmodule:: StarGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.show_inertial_position`
              - Display the inertial position of the star, i.e. its position on the celestial sphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.show_sub_star_point`
              - Display the location at which the star is overhead on the globe.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.inherit_from_2d_graphics_2d`
              - Specify whether star properties set for 2D Graphics are used in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.show_position_label`
              - Display a label on the globe at the inertial position of the star.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics3D.show_sub_star_label`
              - Display a label at the location at which the star is overhead.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StarGraphics3D


Property detail
---------------

.. py:property:: show_inertial_position
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.show_inertial_position
    :type: bool

    Display the inertial position of the star, i.e. its position on the celestial sphere.

.. py:property:: show_sub_star_point
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.show_sub_star_point
    :type: bool

    Display the location at which the star is overhead on the globe.

.. py:property:: inherit_from_2d_graphics_2d
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.inherit_from_2d_graphics_2d
    :type: bool

    Specify whether star properties set for 2D Graphics are used in the 3D Graphics window.

.. py:property:: show_position_label
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.show_position_label
    :type: bool

    Display a label on the globe at the inertial position of the star.

.. py:property:: show_sub_star_label
    :canonical: ansys.stk.core.stkobjects.StarGraphics3D.show_sub_star_label
    :type: bool

    Display a label at the location at which the star is overhead.


