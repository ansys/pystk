VehiclePropagatorSPICE
======================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorSPICE

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the SPICE propagator.

.. py:currentmodule:: VehiclePropagatorSPICE

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.spice`
              - Name of SPICE file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.body_name`
              - Body name.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.segments`
              - Get the segment list.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.available_body_names`
              - Gets a list of available body names.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorSPICE.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorSPICE


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: spice
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.spice
    :type: str

    Name of SPICE file.

.. py:property:: body_name
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.body_name
    :type: str

    Body name.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.segments
    :type: IVehicleSegmentsCollection

    Get the segment list.

.. py:property:: available_body_names
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.available_body_names
    :type: list

    Gets a list of available body names.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.ephemeris_interval
    :type: ITimeToolEventIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorSPICE.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










