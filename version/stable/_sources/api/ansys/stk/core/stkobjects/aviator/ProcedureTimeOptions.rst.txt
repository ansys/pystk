ProcedureTimeOptions
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions

   Class defining the time options for the current procedure.

.. py:currentmodule:: ProcedureTimeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.set_start_time`
              - Set the start time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.set_interrupt_time`
              - Set the interrupt time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.set_stop_time`
              - Set the stop time for the procedure.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.start_time_enabled`
              - Check to see if the start time is enabled for this procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.use_start_time`
              - Opt whether to set a start time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.start_time`
              - Start time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.interrupt_time_enabled`
              - Check to see if the interrupt time is enabled for this procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.use_interrupt_time`
              - Opt whether to set an interrupt time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.interrupt_time`
              - Interrupt time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.stop_time_enabled`
              - Check to see if the stop time is enabled for this procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.use_stop_time`
              - Opt whether to set a stop  time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.stop_time`
              - Stop time for the procedure.



Examples
--------

Configure a procedure's time options

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Get the time in epoch seconds
    root.units_preferences.set_current_unit("DateFormat", "EpSec")
    # Get the time options
    timeOptions = procedure.time_options
    # Get the start time
    startTime = timeOptions.start_time
    # Set the procedure to interrupt after 15 seconds
    timeOptions.set_interrupt_time(15)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureTimeOptions


Property detail
---------------

.. py:property:: start_time_enabled
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.start_time_enabled
    :type: bool

    Check to see if the start time is enabled for this procedure.

.. py:property:: use_start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.use_start_time
    :type: bool

    Opt whether to set a start time for the procedure.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.start_time
    :type: typing.Any

    Start time for the procedure.

.. py:property:: interrupt_time_enabled
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.interrupt_time_enabled
    :type: bool

    Check to see if the interrupt time is enabled for this procedure.

.. py:property:: use_interrupt_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.use_interrupt_time
    :type: bool

    Opt whether to set an interrupt time for the procedure.

.. py:property:: interrupt_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.interrupt_time
    :type: typing.Any

    Interrupt time for the procedure.

.. py:property:: stop_time_enabled
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.stop_time_enabled
    :type: bool

    Check to see if the stop time is enabled for this procedure.

.. py:property:: use_stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.use_stop_time
    :type: bool

    Opt whether to set a stop  time for the procedure.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.stop_time
    :type: typing.Any

    Stop time for the procedure.


Method detail
-------------





.. py:method:: set_start_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.set_start_time

    Set the start time for the procedure.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`





.. py:method:: set_interrupt_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.set_interrupt_time

    Set the interrupt time for the procedure.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`





.. py:method:: set_stop_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTimeOptions.set_stop_time

    Set the stop time for the procedure.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

