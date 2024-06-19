IFigureOfMeritGraphics3D
========================

.. py:class:: IFigureOfMeritGraphics3D

   object
   
   Figure of Merit 3D graphics.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~static`
            * - :py:meth:`~animation`
            * - :py:meth:`~granularity`
            * - :py:meth:`~pixels_per_deg`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics3D


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.static
    :type: IAgFmVOAttributes

    Get the static graphics.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.animation
    :type: IAgFmVOAttributes

    Get the animation graphics:.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.granularity
    :type: float

    Fill granularity: the sampling distance between points used when grid points are filled and smooth contours are not used.

.. py:property:: pixels_per_deg
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.pixels_per_deg
    :type: float

    Gets or sets the number of pixels used in one degree in the temporary file created when smooth contours are used.


