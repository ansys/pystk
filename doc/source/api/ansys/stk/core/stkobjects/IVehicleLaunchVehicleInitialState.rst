IVehicleLaunchVehicleInitialState
=================================

.. py:class:: IVehicleLaunchVehicleInitialState

   object
   
   Simple Ascent propagator initial state interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~launch`
            * - :py:meth:`~burnout_vel`
            * - :py:meth:`~burnout`
            * - :py:meth:`~trajectory_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleLaunchVehicleInitialState


Property detail
---------------

.. py:property:: launch
    :canonical: ansys.stk.core.stkobjects.IVehicleLaunchVehicleInitialState.launch
    :type: IAgLLAPosition

    Get the geocentric or geodetic launch position coordinates.

.. py:property:: burnout_vel
    :canonical: ansys.stk.core.stkobjects.IVehicleLaunchVehicleInitialState.burnout_vel
    :type: float

    Burnout velocity, i.e. the velocity of the vehicle at the stop time.

.. py:property:: burnout
    :canonical: ansys.stk.core.stkobjects.IVehicleLaunchVehicleInitialState.burnout
    :type: IAgLLAPosition

    Get the geocentric or geodetic burnout position coordinates.

.. py:property:: trajectory_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleLaunchVehicleInitialState.trajectory_epoch
    :type: IAgCrdnEventSmartEpoch

    Get the smart epoch component to access the trajectory epoch.


