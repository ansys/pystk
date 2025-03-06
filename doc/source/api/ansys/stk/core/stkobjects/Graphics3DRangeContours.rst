Graphics3DRangeContours
=======================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DRangeContours

   Class defining 3D Graphics range contours: circles comprised of points at a given distance from an object and at the same altitude as that object.

.. py:currentmodule:: Graphics3DRangeContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DRangeContours.show_graphics`
              - Display the contour cone's projection on the surface of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DRangeContours.translucent_lines`
              - Make the contour cone translucent at the specified percentage.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DRangeContours.percent_translucency`
              - Get or set the translucency of the contour cone's projection on the surface of the central body, where 100% = invisible. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DRangeContours.border_wall`
              - Retrieve the border wall properties of the range contours.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DRangeContours.label_swap_distance`
              - Interface to control the level of detail in labels and other screen objects at specified distances.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DRangeContours


Property detail
---------------

.. py:property:: show_graphics
    :canonical: ansys.stk.core.stkobjects.Graphics3DRangeContours.show_graphics
    :type: bool

    Display the contour cone's projection on the surface of the central body.

.. py:property:: translucent_lines
    :canonical: ansys.stk.core.stkobjects.Graphics3DRangeContours.translucent_lines
    :type: bool

    Make the contour cone translucent at the specified percentage.

.. py:property:: percent_translucency
    :canonical: ansys.stk.core.stkobjects.Graphics3DRangeContours.percent_translucency
    :type: float

    Get or set the translucency of the contour cone's projection on the surface of the central body, where 100% = invisible. Dimensionless.

.. py:property:: border_wall
    :canonical: ansys.stk.core.stkobjects.Graphics3DRangeContours.border_wall
    :type: Graphics3DBorderWall

    Retrieve the border wall properties of the range contours.

.. py:property:: label_swap_distance
    :canonical: ansys.stk.core.stkobjects.Graphics3DRangeContours.label_swap_distance
    :type: Graphics3DLabelSwapDistance

    Interface to control the level of detail in labels and other screen objects at specified distances.


