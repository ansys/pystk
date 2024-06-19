IVehicleGraphics3DTrajectoryDropLines
=====================================

.. py:class:: IVehicleGraphics3DTrajectoryDropLines

   object
   
   Interface for droplines for launch vehicles and missiles.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~trajectory`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DTrajectoryDropLines


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines.position
    :type: IAgVeVODropLinePosItemCollection

    Get the list of droplines from the vehicle's current positions.

.. py:property:: trajectory
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DTrajectoryDropLines.trajectory
    :type: IAgVeVODropLinePathItemCollection

    Get the list of droplines at intervals along the vehicle's trajectory.


