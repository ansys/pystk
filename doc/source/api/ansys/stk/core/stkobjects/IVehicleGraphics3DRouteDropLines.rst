IVehicleGraphics3DRouteDropLines
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines

   object
   
   Interface for droplines for great arc vehicles.

.. py:currentmodule:: IVehicleGraphics3DRouteDropLines

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines.position`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines.route`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DRouteDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines.position
    :type: IVehicleGraphics3DDropLinePositionItemCollection

    Get the list of droplines from the vehicle's current positions.

.. py:property:: route
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DRouteDropLines.route
    :type: IVehicleGraphics3DDropLinePathItemCollection

    Get the list of droplines at intervals along the vehicle's route.


