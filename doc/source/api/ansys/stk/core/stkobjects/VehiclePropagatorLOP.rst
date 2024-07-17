VehiclePropagatorLOP
====================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorLOP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the Long-term Orbit Predictor (LOP).

.. py:currentmodule:: VehiclePropagatorLOP

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorLOP.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorLOP.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorLOP.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorLOP.force_model`
              - Get the force model parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorLOP.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorLOP


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorLOP.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorLOP.initial_state
    :type: IVehicleInitialState

    Get the initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorLOP.force_model
    :type: IVehicleLOPForceModel

    Get the force model parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorLOP.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorLOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`






