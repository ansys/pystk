IVehiclePropagatorSPICE
=======================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE

   IVehiclePropagator
   
   SPICE propagator interface.

.. py:currentmodule:: IVehiclePropagatorSPICE

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.step`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.spice`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.body_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.segments`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.available_body_names`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.ephemeris_interval`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorSPICE


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: spice
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.spice
    :type: str

    Name of SPICE file.

.. py:property:: body_name
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.body_name
    :type: str

    Body name.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.segments
    :type: IVehicleSegmentsCollection

    Get the segment list.

.. py:property:: available_body_names
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.available_body_names
    :type: list

    Gets a list of available body names.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










