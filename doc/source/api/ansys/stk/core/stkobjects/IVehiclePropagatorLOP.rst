IVehiclePropagatorLOP
=====================

.. py:class:: IVehiclePropagatorLOP

   IVehiclePropagator
   
   LOP (Long-Range Orbit Predictor) propagator interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~step`
            * - :py:meth:`~initial_state`
            * - :py:meth:`~force_model`
            * - :py:meth:`~ephemeris_interval`


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
    :type: IAgVeInitialState

    Get the initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.force_model
    :type: IAgVeLOPForceModel

    Get the force model parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.ephemeris_interval
    :type: IAgCrdnEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorLOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`






