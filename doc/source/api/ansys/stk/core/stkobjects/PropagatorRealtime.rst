PropagatorRealtime
==================

.. py:class:: ansys.stk.core.stkobjects.PropagatorRealtime

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Realtime propagator.

.. py:currentmodule:: PropagatorRealtime

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.propagate`
              - Set the vehicle's propagator to Realtime.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.is_look_ahead_propagator_supported`
              - Return whether the specified look ahead propagator is supported.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.duration`
              - Get look ahead/look behind duration values.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.interpolation_order`
              - The interpolation order. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.look_ahead_propagator`
              - A name of the lookahead propagator.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.supported_look_ahead_propagators`
              - Return an array of supported lookahead propagators.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.time_step`
              - Specify the interval between computed ephemeris output points. Valid value is between 0.1 and 9999.0 seconds.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.timeout_gap`
              - Specify the time after which look ahead values are considered to be ``stale`` (that is, the data has dropped out). Valid value is between 1.0 and 1000000.0 seconds.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorRealtime.point_builder`
              - Get a object to create ephemeris data for a vehicle by sending it point by point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorRealtime


Property detail
---------------

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.duration
    :type: VehicleDuration

    Get look ahead/look behind duration values.

.. py:property:: interpolation_order
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.interpolation_order
    :type: int

    The interpolation order. Dimensionless.

.. py:property:: look_ahead_propagator
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.look_ahead_propagator
    :type: LookAheadPropagator

    A name of the lookahead propagator.

.. py:property:: supported_look_ahead_propagators
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.supported_look_ahead_propagators
    :type: list

    Return an array of supported lookahead propagators.

.. py:property:: time_step
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.time_step
    :type: float

    Specify the interval between computed ephemeris output points. Valid value is between 0.1 and 9999.0 seconds.

.. py:property:: timeout_gap
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.timeout_gap
    :type: float

    Specify the time after which look ahead values are considered to be ``stale`` (that is, the data has dropped out). Valid value is between 1.0 and 1000000.0 seconds.

.. py:property:: point_builder
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.point_builder
    :type: PropagatorRealtimePointBuilder

    Get a object to create ephemeris data for a vehicle by sending it point by point.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.propagate

    Set the vehicle's propagator to Realtime.

    :Returns:

        :obj:`~None`







.. py:method:: is_look_ahead_propagator_supported(self, propagator: LookAheadPropagator) -> bool
    :canonical: ansys.stk.core.stkobjects.PropagatorRealtime.is_look_ahead_propagator_supported

    Return whether the specified look ahead propagator is supported.

    :Parameters:

        **propagator** : :obj:`~LookAheadPropagator`


    :Returns:

        :obj:`~bool`






