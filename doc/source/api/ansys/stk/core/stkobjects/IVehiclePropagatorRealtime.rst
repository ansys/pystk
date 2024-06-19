IVehiclePropagatorRealtime
==========================

.. py:class:: IVehiclePropagatorRealtime

   IVehiclePropagator
   
   Realtime propagator interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~propagate`
              - Set the vehicle's propagator to Realtime.
            * - :py:meth:`~is_look_ahead_propagator_supported`
              - Return whether the specified look ahead propagator is supported.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~duration`
            * - :py:meth:`~interpolation_order`
            * - :py:meth:`~look_ahead_propagator`
            * - :py:meth:`~supported_look_ahead_propagators`
            * - :py:meth:`~time_step`
            * - :py:meth:`~timeout_gap`
            * - :py:meth:`~point_builder`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorRealtime


Property detail
---------------

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.duration
    :type: IAgVeDuration

    Get look ahead/look behind duration values.

.. py:property:: interpolation_order
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.interpolation_order
    :type: int

    The interpolation order. Dimensionless.

.. py:property:: look_ahead_propagator
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.look_ahead_propagator
    :type: LOOK_AHEAD_PROPAGATOR

    A name of the lookahead propagator.

.. py:property:: supported_look_ahead_propagators
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.supported_look_ahead_propagators
    :type: list

    Returns an array of supported lookahead propagators.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.time_step
    :type: float

    Specify the interval between computed ephemeris output points. Valid value is between 0.1 and 9999.0 seconds.

.. py:property:: timeout_gap
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.timeout_gap
    :type: float

    Specify the time after which look ahead values are considered to be \"stale\" (that is, the data has dropped out). Valid value is between 1.0 and 1000000.0 seconds.

.. py:property:: point_builder
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.point_builder
    :type: IAgVeRealtimePointBuilder

    Gets a object to create ephemeris data for a vehicle by sending it point by point.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.propagate

    Set the vehicle's propagator to Realtime.

    :Returns:

        :obj:`~None`







.. py:method:: is_look_ahead_propagator_supported(self, propagator: LOOK_AHEAD_PROPAGATOR) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorRealtime.is_look_ahead_propagator_supported

    Return whether the specified look ahead propagator is supported.

    :Parameters:

    **propagator** : :obj:`~LOOK_AHEAD_PROPAGATOR`

    :Returns:

        :obj:`~bool`






