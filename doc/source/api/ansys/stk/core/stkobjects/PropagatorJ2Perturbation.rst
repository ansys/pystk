PropagatorJ2Perturbation
========================

.. py:class:: ansys.stk.core.stkobjects.PropagatorJ2Perturbation

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the J2 perturbation propagator.

.. py:currentmodule:: PropagatorJ2Perturbation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.initial_state`
              - Get the initial state.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.ephemeris_interval`
              - Get the propagator's ephemeris interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.propagation_frame`
              - Get or set the propagation frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.supported_propagation_frames`
              - Return supported propagation frames.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorJ2Perturbation.display_coordinate_type`
              - The propagator's display coordinate type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorJ2Perturbation


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.initial_state
    :type: VehicleZonalPropagatorInitialState

    Get the initial state.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.propagation_frame
    :type: VehiclePropagationFrame

    Get or set the propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.supported_propagation_frames
    :type: list

    Return supported propagation frames.

.. py:property:: display_coordinate_type
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.display_coordinate_type
    :type: PropagatorDisplayCoordinateType

    The propagator's display coordinate type.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorJ2Perturbation.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










