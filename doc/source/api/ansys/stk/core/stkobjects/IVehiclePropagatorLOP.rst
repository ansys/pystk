IVehiclePropagatorLOP
=====================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePropagatorLOP

   IVehiclePropagator
   
   LOP (Long-Range Orbit Predictor) propagator interface.

.. py:currentmodule:: IVehiclePropagatorLOP

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorLOP.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorLOP.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorLOP.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorLOP.force_model`
              - Get the force model parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorLOP.ephemeris_interval`
              - Get the propagator's ephemeris interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorLOP


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.initial_state
    :type: IVehicleInitialState

    Get the initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.force_model
    :type: IVehicleLOPForceModel

    Get the force model parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`






