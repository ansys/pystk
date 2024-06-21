IFigureOfMeritGraphics3DAttributes
==================================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes

   object
   
   3D static graphics properties for a Figure of Merit.

.. py:currentmodule:: IFigureOfMeritGraphics3DAttributes

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes.is_visible`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes.translucency`
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes.point_size`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics3DAttributes


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes.is_visible
    :type: bool

    Opt whether to display coverage data for all points based on evaluation over the entire coverage interval.

.. py:property:: translucency
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes.translucency
    :type: float

    Percentage translucency of the static graphics when grid points are filled.

.. py:property:: point_size
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3DAttributes.point_size
    :type: float

    Gets or sets the size of a grid point for static graphics when grid points are not filled and smooth contours are not used.


