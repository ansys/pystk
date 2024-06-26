VEHICLE_WAYPOINT_INTERP_METHOD
==============================

.. py:class:: ansys.stk.core.stkobjects.VEHICLE_WAYPOINT_INTERP_METHOD

   IntEnum


.. py:currentmodule:: VEHICLE_WAYPOINT_INTERP_METHOD

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~WAYPOINT_ELLIPSOID_HEIGHT`
              - Ellipsoid height: interpolate using the greatArc interpolator without considering terrain.

            * - :py:attr:`~WAYPOINT_TERRAIN_HEIGHT`
              - Terrain height: assigns a height above terrain by a linear interpolation between the heights above terrain at the waypoints.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_WAYPOINT_INTERP_METHOD


