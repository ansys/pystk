ICoverageGraphics3D
===================

.. py:class:: ICoverageGraphics3D

   object
   
   3D graphics options for the coverage grid.

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
            * - :py:meth:`~show_at_altitude`
            * - :py:meth:`~draw_at_altitude_mode`
            * - :py:meth:`~auto_granularity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGraphics3D


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3D.static
    :type: IAgCvVOAttributes

    3D static graphics options.

.. py:property:: animation
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3D.animation
    :type: IAgCvVOAttributes

    3D animation graphics options.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3D.granularity
    :type: float

    Fill Granularity: sampling distance between points used when grid points are filled. Uses Angle Dimension.

.. py:property:: show_at_altitude
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3D.show_at_altitude
    :type: bool

    Show Graphics at Altitude.

.. py:property:: draw_at_altitude_mode
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3D.draw_at_altitude_mode
    :type: COVERAGE_3D_DRAW_AT_ALTITUDE_MODE

    Draw at Altitude Polygon Mode.

.. py:property:: auto_granularity
    :canonical: ansys.stk.core.stkobjects.ICoverageGraphics3D.auto_granularity
    :type: bool

    Auto Compute Fill Granularity.


