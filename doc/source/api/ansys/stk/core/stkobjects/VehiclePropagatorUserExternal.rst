VehiclePropagatorUserExternal
=============================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the user-external propagator.

.. py:currentmodule:: VehiclePropagatorUserExternal

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.propagate`
              - Propagates the vehicle's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.start_time`
              - Gets or sets the start time of ephemeris interval. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.stop_time`
              - Gets or sets the stop time of ephemeris interval. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.propagator`
              - Propagator.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.file`
              - Name of user-external file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.vehicle_id`
              - Vehicle ID.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.description`
              - Description.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.available_vehicle_ids`
              - Get available IDs.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.available_propagators`
              - Get available propagators.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorUserExternal


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.start_time
    :type: typing.Any

    Gets or sets the start time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.stop_time
    :type: typing.Any

    Gets or sets the stop time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: propagator
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.propagator
    :type: str

    Propagator.

.. py:property:: file
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.file
    :type: str

    Name of user-external file.

.. py:property:: vehicle_id
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.vehicle_id
    :type: str

    Vehicle ID.

.. py:property:: description
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.description
    :type: str

    Description.

.. py:property:: available_vehicle_ids
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.available_vehicle_ids
    :type: list

    Get available IDs.

.. py:property:: available_propagators
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.available_propagators
    :type: list

    Get available propagators.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorUserExternal.propagate

    Propagates the vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`

















