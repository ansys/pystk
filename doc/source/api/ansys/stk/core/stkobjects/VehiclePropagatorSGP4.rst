VehiclePropagatorSGP4
=====================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorSGP4

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the SGP4 propagator.

.. py:currentmodule:: VehiclePropagatorSGP4

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.segments`
              - Get the element set list.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.auto_update_enabled`
              - Whether automatic update is enabled.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.auto_update`
              - Allows configuring the auto-update parameters and settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.common_tasks`
              - Most commonly used tasks such as importing file data, etc.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.settings`
              - Propagator settings.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSGP4.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorSGP4


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.segments
    :type: VehicleSGP4SegmentCollection

    Get the element set list.

.. py:property:: auto_update_enabled
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.auto_update_enabled
    :type: bool

    Whether automatic update is enabled.

.. py:property:: auto_update
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.auto_update
    :type: VehicleSGP4AutoUpdate

    Allows configuring the auto-update parameters and settings.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.common_tasks
    :type: VehiclePropagatorSGP4CommonTasks

    Most commonly used tasks such as importing file data, etc.

.. py:property:: settings
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.settings
    :type: VehicleSGP4PropagatorSettings

    Propagator settings.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSGP4.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










