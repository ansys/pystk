IVehicleWaypointAltitudeReferenceTerrain
========================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReferenceTerrain

   IVehicleWaypointAltitudeReference
   
   Interface for terrain altitude reference.

.. py:currentmodule:: IVehicleWaypointAltitudeReferenceTerrain

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReferenceTerrain.granularity`
              - Defines the distance between sampling points along a vehicle route, used when waypoint altitudes are referenced to terrain. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReferenceTerrain.interp_method`
              - Gets or sets the terrain interpolation method to be used to define the height of the vehicle with respect to terrain data.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleWaypointAltitudeReferenceTerrain


Property detail
---------------

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReferenceTerrain.granularity
    :type: float

    Defines the distance between sampling points along a vehicle route, used when waypoint altitudes are referenced to terrain. Uses Distance Dimension.

.. py:property:: interp_method
    :canonical: ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReferenceTerrain.interp_method
    :type: VEHICLE_WAYPOINT_INTERP_METHOD

    Gets or sets the terrain interpolation method to be used to define the height of the vehicle with respect to terrain data.


