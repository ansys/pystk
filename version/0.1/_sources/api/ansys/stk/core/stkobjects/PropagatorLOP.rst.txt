PropagatorLOP
=============

.. py:class:: ansys.stk.core.stkobjects.PropagatorLOP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the Long-term Orbit Predictor (LOP).

.. py:currentmodule:: PropagatorLOP

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorLOP.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorLOP.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorLOP.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorLOP.force_model`
              - Get the force model parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorLOP.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorLOP.display_coordinate_type`
              - The propagator's display coordinate type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorLOP


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorLOP.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.PropagatorLOP.initial_state
    :type: VehicleInitialState

    Get the initial state.

.. py:property:: force_model
    :canonical: ansys.stk.core.stkobjects.PropagatorLOP.force_model
    :type: VehicleLOPForceModel

    Get the force model parameters.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorLOP.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: display_coordinate_type
    :canonical: ansys.stk.core.stkobjects.PropagatorLOP.display_coordinate_type
    :type: PropagatorDisplayCoordinateType

    The propagator's display coordinate type.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorLOP.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`








