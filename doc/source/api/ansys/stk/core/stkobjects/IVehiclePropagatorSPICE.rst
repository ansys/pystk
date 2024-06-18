IVehiclePropagatorSPICE
=======================

.. py:class:: IVehiclePropagatorSPICE

   IVehiclePropagator
   
   SPICE propagator interface.

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
            * - :py:meth:`~spice`
            * - :py:meth:`~body_name`
            * - :py:meth:`~segments`
            * - :py:meth:`~available_body_names`
            * - :py:meth:`~ephemeris_interval`


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
    :type: "IAgVeSegmentsCollection"

    Get the segment list.

.. py:property:: available_body_names
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.available_body_names
    :type: list

    Gets a list of available body names.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorSPICE.ephemeris_interval
    :type: "IAgCrdnEventIntervalSmartInterval"

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










