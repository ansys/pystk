IProcedureFastTimeOptions
=========================

.. py:class:: IProcedureFastTimeOptions

   object
   
   Interface used to access the fast time options (without error or constraint checks) for the current procedure. Use this interface to set an Interrupt Time or Fixed Duration for a procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_start_time`
              - Set the start time for the procedure.
            * - :py:meth:`~set_interrupt_time`
              - Set the interrupt time for the procedure.
            * - :py:meth:`~set_stop_time`
              - Set the stop time for the procedure.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureFastTimeOptions


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFastTimeOptions.start_time
    :type: typing.Any

    Start time for the procedure.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFastTimeOptions.stop_time
    :type: typing.Any

    Stop time for the procedure.


Method detail
-------------


.. py:method:: set_start_time(self, time:typing.Any) -> None

    Set the start time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_interrupt_time(self, time:typing.Any) -> None

    Set the interrupt time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


.. py:method:: set_stop_time(self, time:typing.Any) -> None

    Set the stop time for the procedure.

    :Parameters:

    **time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

