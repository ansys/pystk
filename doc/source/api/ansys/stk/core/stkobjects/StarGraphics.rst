StarGraphics
============

.. py:class:: ansys.stk.core.stkobjects.StarGraphics

   Class defining 2D Graphics properties of a Star.

.. py:currentmodule:: StarGraphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics.color`
              - Color in which the star's marker and label are displayed in the 2D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics.inherit`
              - Specify whether display of label is inherited from the Scenario-level setting.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics.marker_style`
              - The style of the star's marker.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics.label_visible`
              - Specify whether the star's label is displayed.
            * - :py:attr:`~ansys.stk.core.stkobjects.StarGraphics.is_object_graphics_visible`
              - Specify whether graphics attributes of the star are visible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StarGraphics


Property detail
---------------

.. py:property:: color
    :canonical: ansys.stk.core.stkobjects.StarGraphics.color
    :type: agcolor.Color

    Color in which the star's marker and label are displayed in the 2D Graphics window.

.. py:property:: inherit
    :canonical: ansys.stk.core.stkobjects.StarGraphics.inherit
    :type: bool

    Specify whether display of label is inherited from the Scenario-level setting.

.. py:property:: marker_style
    :canonical: ansys.stk.core.stkobjects.StarGraphics.marker_style
    :type: str

    The style of the star's marker.

.. py:property:: label_visible
    :canonical: ansys.stk.core.stkobjects.StarGraphics.label_visible
    :type: bool

    Specify whether the star's label is displayed.

.. py:property:: is_object_graphics_visible
    :canonical: ansys.stk.core.stkobjects.StarGraphics.is_object_graphics_visible
    :type: bool

    Specify whether graphics attributes of the star are visible.


