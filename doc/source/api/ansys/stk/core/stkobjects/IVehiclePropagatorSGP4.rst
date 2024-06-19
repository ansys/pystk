IVehiclePropagatorSGP4
======================

.. py:class:: IVehiclePropagatorSGP4

   IVehiclePropagator
   
   SGP4 propagator interface.

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
            * - :py:meth:`~segments`
            * - :py:meth:`~auto_update_enabled`
            * - :py:meth:`~auto_update`
            * - :py:meth:`~common_tasks`
            * - :py:meth:`~settings`
            * - :py:meth:`~ephemeris_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorSGP4


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.segments
    :type: IAgVeSGP4SegmentCollection

    Get the element set list.

.. py:property:: auto_update_enabled
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.auto_update_enabled
    :type: bool

    Whether automatic update is enabled.

.. py:property:: auto_update
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.auto_update
    :type: IAgVeSGP4AutoUpdate

    Allows configuring the auto-update parameters and settings.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.common_tasks
    :type: IAgVePropagatorSGP4CommonTasks

    Most commonly used tasks such as importing file data, etc.

.. py:property:: settings
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.settings
    :type: IAgVeSGP4PropagatorSettings

    Propagator settings.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.ephemeris_interval
    :type: IAgCrdnEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










