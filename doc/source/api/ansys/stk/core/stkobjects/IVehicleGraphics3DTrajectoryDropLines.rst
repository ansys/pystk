IVehicleGraphics3DTrajectoryDropLines
=====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines

   object
   
   Interface for droplines for launch vehicles and missiles.

.. py:currentmodule:: IVehicleGraphics3DTrajectoryDropLines

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines.position`
              - Get the list of droplines from the vehicle's current positions.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines.trajectory`
              - Get the list of droplines at intervals along the vehicle's trajectory.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectoryDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines.position
    :type: IVehicleGraphics3DDropLinePositionItemCollection

    Get the list of droplines from the vehicle's current positions.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines.trajectory
    :type: IVehicleGraphics3DDropLinePathItemCollection

    Get the list of droplines at intervals along the vehicle's trajectory.


