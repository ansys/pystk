FigureOfMeritGraphics3D
=======================

.. py:class:: ansys.stk.core.stkobjects.FigureOfMeritGraphics3D

   Figure of Merit 3D graphics.

.. py:currentmodule:: FigureOfMeritGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.static`
              - Get the static graphics.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.animation_graphics_3d_settings`
              - Get the animation graphics:.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.granularity`
              - Fill granularity: the sampling distance between points used when grid points are filled and smooth contours are not used.
            * - :py:attr:`~ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.pixels_per_degree`
              - Gets or sets the number of pixels used in one degree in the temporary file created when smooth contours are used.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import FigureOfMeritGraphics3D


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.static
    :type: FigureOfMeritGraphics3DAttributes

    Get the static graphics.

.. py:property:: animation_graphics_3d_settings
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.animation_graphics_3d_settings
    :type: FigureOfMeritGraphics3DAttributes

    Get the animation graphics:.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.granularity
    :type: float

    Fill granularity: the sampling distance between points used when grid points are filled and smooth contours are not used.

.. py:property:: pixels_per_degree
    :canonical: ansys.stk.core.stkobjects.FigureOfMeritGraphics3D.pixels_per_degree
    :type: float

    Gets or sets the number of pixels used in one degree in the temporary file created when smooth contours are used.


