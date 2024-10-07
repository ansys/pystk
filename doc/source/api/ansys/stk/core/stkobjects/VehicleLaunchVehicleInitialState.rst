VehicleLaunchVehicleInitialState
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState

   Class defining launch vehicle initial state.

.. py:currentmodule:: VehicleLaunchVehicleInitialState

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.launch`
              - Get the geocentric or geodetic launch position coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.burnout_vel`
              - Burnout velocity, i.e. the velocity of the vehicle at the stop time.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.burnout`
              - Get the geocentric or geodetic burnout position coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.trajectory_epoch`
              - Get the smart epoch component to access the trajectory epoch.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleLaunchVehicleInitialState


Property detail
---------------

.. py:property:: launch
    :canonical: ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.launch
    :type: ILLAPosition

    Get the geocentric or geodetic launch position coordinates.

.. py:property:: burnout_vel
    :canonical: ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.burnout_vel
    :type: float

    Burnout velocity, i.e. the velocity of the vehicle at the stop time.

.. py:property:: burnout
    :canonical: ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.burnout
    :type: ILLAPosition

    Get the geocentric or geodetic burnout position coordinates.

.. py:property:: trajectory_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleLaunchVehicleInitialState.trajectory_epoch
    :type: ITimeToolInstantSmartEpoch

    Get the smart epoch component to access the trajectory epoch.


