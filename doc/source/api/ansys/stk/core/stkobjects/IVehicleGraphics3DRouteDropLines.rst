IVehicleGraphics3DRouteDropLines
================================

.. py:class:: IVehicleGraphics3DRouteDropLines

   object
   
   Interface for droplines for great arc vehicles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~route`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DRouteDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines.position
    :type: IAgVeVODropLinePosItemCollection

    Get the list of droplines from the vehicle's current positions.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines.route
    :type: IAgVeVODropLinePathItemCollection

    Get the list of droplines at intervals along the vehicle's route.


