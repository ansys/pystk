IFigureOfMeritGraphics3D
========================

.. py:class:: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D

   object
   
   Figure of Merit 3D graphics.

.. py:currentmodule:: IFigureOfMeritGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.static`
              - Get the static graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.animation`
              - Get the animation graphics:.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.granularity`
              - Fill granularity: the sampling distance between points used when grid points are filled and smooth contours are not used.
            * - :py:attr:`~ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.pixels_per_deg`
              - Gets or sets the number of pixels used in one degree in the temporary file created when smooth contours are used.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IFigureOfMeritGraphics3D


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.static
    :type: IFigureOfMeritGraphics3DAttributes

    Get the static graphics.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.animation
    :type: IFigureOfMeritGraphics3DAttributes

    Get the animation graphics:.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.granularity
    :type: float

    Fill granularity: the sampling distance between points used when grid points are filled and smooth contours are not used.

.. py:property:: pixels_per_deg
    :canonical: ansys.stk.core.stkobjects.IFigureOfMeritGraphics3D.pixels_per_deg
    :type: float

    Gets or sets the number of pixels used in one degree in the temporary file created when smooth contours are used.


