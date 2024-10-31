CoverageGraphics3D
==================

.. py:class:: ansys.stk.core.stkobjects.CoverageGraphics3D

   AgCvVOStatic Class.

.. py:currentmodule:: CoverageGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3D.static`
              - 3D static graphics options.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3D.animation_graphics_3d_settings`
              - 3D animation graphics options.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3D.granularity`
              - Fill Granularity: sampling distance between points used when grid points are filled. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3D.show_at_altitude`
              - Show Graphics at Altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3D.draw_at_altitude_mode`
              - Draw at Altitude Polygon Mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGraphics3D.automatic_computation_of_granularity`
              - Auto Compute Fill Granularity.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGraphics3D


Property detail
---------------

.. py:property:: static
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3D.static
    :type: CoverageGraphics3DAttributes

    3D static graphics options.

.. py:property:: animation_graphics_3d_settings
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3D.animation_graphics_3d_settings
    :type: CoverageGraphics3DAttributes

    3D animation graphics options.

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3D.granularity
    :type: float

    Fill Granularity: sampling distance between points used when grid points are filled. Uses Angle Dimension.

.. py:property:: show_at_altitude
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3D.show_at_altitude
    :type: bool

    Show Graphics at Altitude.

.. py:property:: draw_at_altitude_mode
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3D.draw_at_altitude_mode
    :type: COVERAGE_3D_DRAW_AT_ALTITUDE_MODE

    Draw at Altitude Polygon Mode.

.. py:property:: automatic_computation_of_granularity
    :canonical: ansys.stk.core.stkobjects.CoverageGraphics3D.automatic_computation_of_granularity
    :type: bool

    Auto Compute Fill Granularity.


