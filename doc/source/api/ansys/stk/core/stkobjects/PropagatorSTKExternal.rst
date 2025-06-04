PropagatorSTKExternal
=====================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSTKExternal

   Bases: :py:class:`~ansys.stk.core.stkobjects.IPropagator`

   Class defining the STK External propagator.

.. py:currentmodule:: PropagatorSTKExternal

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.propagate`
              - Propagates the satellite's path using the specified time interval.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.start_time`
              - Get the start time of ephemeris interval. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.stop_time`
              - Get the stop time of ephemeris interval. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.step`
              - Step size. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.filename`
              - Name of external file.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.override`
              - Opt whether to override times contained in the external file.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.file_format`
              - Ephemeris file format.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.ephemeris_start_epoch`
              - If overriding the times contained in the external file, specify the time of the first ephemeris point.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.limit_ephemeris_to_scenario_interval`
              - Limit ephemeris for analysis to the Scenario Interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSTKExternal.message_level`
              - Message level used to report messages during file loading.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSTKExternal


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.start_time
    :type: typing.Any

    Get the start time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.stop_time
    :type: typing.Any

    Get the stop time of ephemeris interval. Uses DateFormat Dimension.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.step
    :type: float

    Step size. Uses Time Dimension.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.filename
    :type: str

    Name of external file.

.. py:property:: override
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.override
    :type: bool

    Opt whether to override times contained in the external file.

.. py:property:: file_format
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.file_format
    :type: ExternalEphemerisFormatType

    Ephemeris file format.

.. py:property:: ephemeris_start_epoch
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.ephemeris_start_epoch
    :type: ITimeToolInstantSmartEpoch

    If overriding the times contained in the external file, specify the time of the first ephemeris point.

.. py:property:: limit_ephemeris_to_scenario_interval
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.limit_ephemeris_to_scenario_interval
    :type: bool

    Limit ephemeris for analysis to the Scenario Interval.

.. py:property:: message_level
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.message_level
    :type: ExternalFileMessageLevelType

    Message level used to report messages during file loading.


Method detail
-------------

.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSTKExternal.propagate

    Propagates the satellite's path using the specified time interval.

    :Returns:

        :obj:`~None`















