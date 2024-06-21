IGraphics3DRangeContours
========================

.. py:class:: ansys.stk.core.stkobjects.IGraphics3DRangeContours

   object
   
   AgVORangeContour used to access the 3D RangeContour attributes.

.. py:currentmodule:: IGraphics3DRangeContours

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DRangeContours.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DRangeContours.translucent_lines`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DRangeContours.percent_translucency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DRangeContours.border_wall`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGraphics3DRangeContours.label_swap_distance`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DRangeContours


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IGraphics3DRangeContours.is_visible
    :type: bool

    Display the contour cone's projection on the surface of the central body.

.. py:property:: translucent_lines
    :canonical: ansys.stk.core.stkobjects.IGraphics3DRangeContours.translucent_lines
    :type: bool

    Make the contour cone translucent at the specified percentage.

.. py:property:: percent_translucency
    :canonical: ansys.stk.core.stkobjects.IGraphics3DRangeContours.percent_translucency
    :type: float

    Gets or sets the translucency of the contour cone's projection on the surface of the central body, where 100% = invisible. Dimensionless.

.. py:property:: border_wall
    :canonical: ansys.stk.core.stkobjects.IGraphics3DRangeContours.border_wall
    :type: IGraphics3DBorderWall

    Retrieve the border wall properties of the range contours.

.. py:property:: label_swap_distance
    :canonical: ansys.stk.core.stkobjects.IGraphics3DRangeContours.label_swap_distance
    :type: IGraphics3DLabelSwapDistance

    Interface to control the level of detail in labels and other screen objects at specified distances.


