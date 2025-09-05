PropagatorSimpleAscent
======================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSimpleAscent

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the simple ascent propagator for a launch vehicle.

.. py:currentmodule:: PropagatorSimpleAscent

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSimpleAscent.propagate`
              - Propagates the launch vehicle's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSimpleAscent.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSimpleAscent.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSimpleAscent.step`
              - Step size. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSimpleAscent


Property detail
---------------

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorSimpleAscent.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.PropagatorSimpleAscent.initial_state
    :type: LaunchVehicleInitialState

    Get the initial state.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorSimpleAscent.step
    :type: float

    Step size. Uses Time Dimension.


Method detail
-------------



.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSimpleAscent.propagate

    Propagates the launch vehicle's path using the specified time interval.

    :Returns:

        :obj:`~None`



