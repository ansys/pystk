VehicleWaypointAltitudeReferenceTerrain
=======================================

.. py:class:: ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleWaypointAltitudeReference`

   Terrain altitude reference.

.. py:currentmodule:: VehicleWaypointAltitudeReferenceTerrain

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.granularity`
              - Defines the distance between sampling points along a vehicle route, used when waypoint altitudes are referenced to terrain. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.interpolation_method`
              - Gets or sets the terrain interpolation method to be used to define the height of the vehicle with respect to terrain data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleWaypointAltitudeReferenceTerrain


Property detail
---------------

.. py:property:: granularity
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.granularity
    :type: float

    Defines the distance between sampling points along a vehicle route, used when waypoint altitudes are referenced to terrain. Uses Distance Dimension.

.. py:property:: interpolation_method
    :canonical: ansys.stk.core.stkobjects.VehicleWaypointAltitudeReferenceTerrain.interpolation_method
    :type: VehicleWaypointInterpolationMethod

    Gets or sets the terrain interpolation method to be used to define the height of the vehicle with respect to terrain data.


