VehiclePropagatorSimpleAscent
=============================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the simple ascent propagator for a launch vehicle.

.. py:currentmodule:: VehiclePropagatorSimpleAscent

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.propagate`
              - Propagates the launch vehicle's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorSimpleAscent


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.initial_state
    :type: VehicleLaunchVehicleInitialState

    Get the initial state.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSimpleAscent.propagate

    Propagates the launch vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`





