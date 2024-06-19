IVehiclePropagatorSimpleAscent
==============================

.. py:class:: IVehiclePropagatorSimpleAscent

   IVehiclePropagator
   
   SimpleAscent Propagator.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagate`
              - Propagates the launch vehicle's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~step`
            * - :py:meth:`~initial_state`
            * - :py:meth:`~ephemeris_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorSimpleAscent


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSimpleAscent.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSimpleAscent.initial_state
    :type: IAgVeLvInitialState

    Get the initial state.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSimpleAscent.ephemeris_interval
    :type: IAgCrdnEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSimpleAscent.propagate

    Propagates the launch vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`





