ADDSMessage
===========

.. py:class:: ansys.stk.core.stkobjects.aviator.ADDSMessage

   Class defining a message from the NOAA ADDS service.

.. py:currentmodule:: ADDSMessage

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ADDSMessage.start_time`
              - Valid start time for the ADDS message.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ADDSMessage.stop_time`
              - Valid stop time for the ADDS message.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ADDSMessage.message_time`
              - Get the message time for the ADDS message.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ADDSMessage.type`
              - Get the ADDS message type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ADDSMessage.source`
              - Get the ADDS message source.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ADDSMessage


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ADDSMessage.start_time
    :type: typing.Any

    Valid start time for the ADDS message.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.ADDSMessage.stop_time
    :type: typing.Any

    Valid stop time for the ADDS message.

.. py:property:: message_time
    :canonical: ansys.stk.core.stkobjects.aviator.ADDSMessage.message_time
    :type: typing.Any

    Get the message time for the ADDS message.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.aviator.ADDSMessage.type
    :type: ADDS_FORECAST_TYPE

    Get the ADDS message type.

.. py:property:: source
    :canonical: ansys.stk.core.stkobjects.aviator.ADDSMessage.source
    :type: str

    Get the ADDS message source.


