PropagatorSPICE
===============

.. py:class:: ansys.stk.core.stkobjects.PropagatorSPICE

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the SPICE propagator.

.. py:currentmodule:: PropagatorSPICE

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.spice`
              - Name of SPICE file.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.body_name`
              - Body name.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.segments`
              - Get the segment list.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.available_body_names`
              - Get a list of available body names.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSPICE.ephemeris_interval`
              - Get the propagator's ephemeris interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSPICE


Property detail
---------------

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: spice
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.spice
    :type: str

    Name of SPICE file.

.. py:property:: body_name
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.body_name
    :type: str

    Body name.

.. py:property:: segments
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.segments
    :type: PropagatorSPICESegmentsCollection

    Get the segment list.

.. py:property:: available_body_names
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.available_body_names
    :type: list

    Get a list of available body names.

.. py:property:: ephemeris_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.ephemeris_interval
    :type: ITimeToolTimeIntervalSmartInterval

    Get the propagator's ephemeris interval.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSPICE.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`










