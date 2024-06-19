IVehiclePropagatorStkExternal
=============================

.. py:class:: IVehiclePropagatorStkExternal

   IVehiclePropagator
   
   StkExternal propagator interface.

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

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~step`
            * - :py:meth:`~filename`
            * - :py:meth:`~override`
            * - :py:meth:`~file_format`
            * - :py:meth:`~ephemeris_start_epoch`
            * - :py:meth:`~limit_ephemeris_to_scenario_interval`
            * - :py:meth:`~message_level`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorStkExternal


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.start_time
    :type: typing.Any

    Get the start time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.stop_time
    :type: typing.Any

    Get the stop time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.filename
    :type: str

    Name of external file.

.. py:property:: override
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.override
    :type: bool

    Opt whether to override times contained in the external file.

.. py:property:: file_format
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.file_format
    :type: STK_EXTERNAL_EPHEMERIS_FORMAT

    Ephemeris file format.

.. py:property:: ephemeris_start_epoch
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.ephemeris_start_epoch
    :type: IAgCrdnEventSmartEpoch

    If overriding the times contained in the external file, specify the time of the first ephemeris point.

.. py:property:: limit_ephemeris_to_scenario_interval
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.limit_ephemeris_to_scenario_interval
    :type: bool

    Limit ephemeris for analysis to the Scenario Interval.

.. py:property:: message_level
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.message_level
    :type: STK_EXTERNAL_FILE_MESSAGE_LEVEL

    Message level used to report messages during file loading.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorStkExternal.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`















