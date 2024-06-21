IVehiclePropagatorSGP4
======================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4

   IVehiclePropagator
   
   SGP4 propagator interface.

.. py:currentmodule:: IVehiclePropagatorSGP4

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.step`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.segments`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.auto_update_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.auto_update`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.common_tasks`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.settings`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.ephemeris_interval`


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
    :type: IVehicleSGP4SegmentCollection

    Get the element set list.

.. py:property:: auto_update_enabled
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.auto_update_enabled
    :type: bool

    Whether automatic update is enabled.

.. py:property:: auto_update
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.auto_update
    :type: IVehicleSGP4AutoUpdate

    Allows configuring the auto-update parameters and settings.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.common_tasks
    :type: IVehiclePropagatorSGP4CommonTasks

    Most commonly used tasks such as importing file data, etc.

.. py:property:: settings
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.settings
    :type: IVehicleSGP4PropagatorSettings

    Propagator settings.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSGP4.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










