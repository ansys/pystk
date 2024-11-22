PropagatorTwoBody
=================

.. py:class:: ansys.stk.core.stkobjects.PropagatorTwoBody

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the two body propagator.

.. py:currentmodule:: PropagatorTwoBody

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.propagation_frame`
              - Gets or sets the propagation frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.supported_propagation_frames`
              - Returns supported propagation frames.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorTwoBody.display_coord_type`
              - The propagator's display coordinate type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorTwoBody


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.initial_state
    :type: VehicleInitialState

    Get the initial state.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.propagation_frame
    :type: VEHICLE_PROPAGATION_FRAME

    Gets or sets the propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.supported_propagation_frames
    :type: list

    Returns supported propagation frames.

.. py:property:: display_coord_type
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.display_coord_type
    :type: PROPAGATOR_DISPLAY_COORDINATE_TYPE

    The propagator's display coordinate type.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorTwoBody.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










