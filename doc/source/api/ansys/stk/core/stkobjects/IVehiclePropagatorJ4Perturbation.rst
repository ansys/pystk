IVehiclePropagatorJ4Perturbation
================================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation

   IVehiclePropagator
   
   J4 Perturbation propagator interface.

.. py:currentmodule:: IVehiclePropagatorJ4Perturbation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.step`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.initial_state`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.ephemeris_interval`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.propagation_frame`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.supported_propagation_frames`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorJ4Perturbation


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.initial_state
    :type: IVehicleJxInitialState

    Get the initial state.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.propagation_frame
    :type: VEHICLE_PROPAGATION_FRAME

    Gets or sets the propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.supported_propagation_frames
    :type: list

    Returns supported propagation frames.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorJ4Perturbation.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`








