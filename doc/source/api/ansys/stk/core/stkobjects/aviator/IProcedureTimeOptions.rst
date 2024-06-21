IProcedureTimeOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions

   object
   
   Interface used to access the time options for the current procedure. Use this interface to set an Interrupt Time or Fixed Duration for a procedure.

.. py:currentmodule:: IProcedureTimeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.set_start_time`
              - Set the start time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.set_interrupt_time`
              - Set the interrupt time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.set_stop_time`
              - Set the stop time for the procedure.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.start_time_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.use_start_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.start_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.interrupt_time_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.use_interrupt_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.interrupt_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.stop_time_enabled`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.use_stop_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureTimeOptions


Property detail
---------------

.. py:property:: start_time_enabled
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.start_time_enabled
    :type: bool

    Check to see if the start time is enabled for this procedure.

.. py:property:: use_start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.use_start_time
    :type: bool

    Opt whether to set a start time for the procedure.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.start_time
    :type: typing.Any

    Start time for the procedure.

.. py:property:: interrupt_time_enabled
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.interrupt_time_enabled
    :type: bool

    Check to see if the interrupt time is enabled for this procedure.

.. py:property:: use_interrupt_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.use_interrupt_time
    :type: bool

    Opt whether to set an interrupt time for the procedure.

.. py:property:: interrupt_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.interrupt_time
    :type: typing.Any

    Interrupt time for the procedure.

.. py:property:: stop_time_enabled
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.stop_time_enabled
    :type: bool

    Check to see if the stop time is enabled for this procedure.

.. py:property:: use_stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.use_stop_time
    :type: bool

    Opt whether to set a stop  time for the procedure.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.stop_time
    :type: typing.Any

    Stop time for the procedure.


Method detail
-------------





.. py:method:: set_start_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.set_start_time

    Set the start time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`





.. py:method:: set_interrupt_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.set_interrupt_time

    Set the interrupt time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`





.. py:method:: set_stop_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTimeOptions.set_stop_time

    Set the stop time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

