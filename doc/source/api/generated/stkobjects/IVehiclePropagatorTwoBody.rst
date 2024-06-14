IVehiclePropagatorTwoBody
=========================

.. py:class:: IVehiclePropagatorTwoBody

   IVehiclePropagator
   
   Two-body propagator interface.

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
            * - :py:meth:`~ephemeris_interval`
            * - :py:meth:`~propagation_frame`
            * - :py:meth:`~supported_propagation_frames`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorTwoBody


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorTwoBody.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorTwoBody.initial_state
    :type: "IAgVeInitialState"

    Get the initial state.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorTwoBody.ephemeris_interval
    :type: "IAgCrdnEventIntervalSmartInterval"

    Get the propagator's ephemeris interval.

.. py:property:: propagation_frame
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorTwoBody.propagation_frame
    :type: "VEHICLE_PROPAGATION_FRAME"

    Gets or sets the propagation frame.

.. py:property:: supported_propagation_frames
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorTwoBody.supported_propagation_frames
    :type: list

    Returns supported propagation frames.


Method detail
-------------

.. py:method:: propagate(self) -> None

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`








