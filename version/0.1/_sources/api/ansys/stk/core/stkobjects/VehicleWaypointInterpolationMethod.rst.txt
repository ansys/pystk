VehicleWaypointInterpolationMethod
==================================

.. py:class:: ansys.stk.core.stkobjects.VehicleWaypointInterpolationMethod

   IntEnum


.. py:currentmodule:: VehicleWaypointInterpolationMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ELLIPSOID_HEIGHT`
              - Ellipsoid height: interpolate using the greatArc interpolator without considering terrain.

            * - :py:attr:`~TERRAIN_HEIGHT`
              - Terrain height: assigns a height above terrain by a linear interpolation between the heights above terrain at the waypoints.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleWaypointInterpolationMethod


