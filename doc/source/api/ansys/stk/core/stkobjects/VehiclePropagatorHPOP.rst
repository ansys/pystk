VehiclePropagatorHPOP
=====================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorHPOP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the High Precision Orbit Propagator (HPOP).

.. py:currentmodule:: VehiclePropagatorHPOP

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.initial_state`
              - Get the satellite's initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.force_model`
              - Get the force model parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.integrator`
              - Get the integrator parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.covariance`
              - Get the covariance parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorHPOP.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorHPOP


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.initial_state
    :type: IVehicleInitialState

    Get the satellite's initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.force_model
    :type: IVehicleHPOPForceModel

    Get the force model parameters.

.. py:property:: integrator
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.integrator
    :type: IVehicleIntegrator

    Get the integrator parameters.

.. py:property:: covariance
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.covariance
    :type: IVehicleCovariance

    Get the covariance parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorHPOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`








