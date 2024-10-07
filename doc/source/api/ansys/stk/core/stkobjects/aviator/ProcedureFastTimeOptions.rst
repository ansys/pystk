ProcedureFastTimeOptions
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions

   Class defining fast operations (without error or constraint checks) for time options for the current procedure.

.. py:currentmodule:: ProcedureFastTimeOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.set_start_time`
              - Set the start time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.set_interrupt_time`
              - Set the interrupt time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.set_stop_time`
              - Set the stop time for the procedure.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.start_time`
              - Start time for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.stop_time`
              - Stop time for the procedure.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureFastTimeOptions


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.start_time
    :type: typing.Any

    Start time for the procedure.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.stop_time
    :type: typing.Any

    Stop time for the procedure.


Method detail
-------------


.. py:method:: set_start_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.set_start_time

    Set the start time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_interrupt_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.set_interrupt_time

    Set the interrupt time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


.. py:method:: set_stop_time(self, time: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureFastTimeOptions.set_stop_time

    Set the stop time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

