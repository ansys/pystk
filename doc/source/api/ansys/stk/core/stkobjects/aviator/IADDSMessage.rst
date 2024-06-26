IADDSMessage
============

.. py:class:: ansys.stk.core.stkobjects.aviator.IADDSMessage

   object
   
   Interface used to access a message from the NOAA ADDS forecast.

.. py:currentmodule:: IADDSMessage

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessage.start_time`
              - Valid start time for the ADDS message.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessage.stop_time`
              - Valid stop time for the ADDS message.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessage.message_time`
              - Get the message time for the ADDS message.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessage.type`
              - Get the ADDS message type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessage.source`
              - Get the ADDS message source.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IADDSMessage


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessage.start_time
    :type: typing.Any

    Valid start time for the ADDS message.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessage.stop_time
    :type: typing.Any

    Valid stop time for the ADDS message.

.. py:property:: message_time
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessage.message_time
    :type: typing.Any

    Get the message time for the ADDS message.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessage.type
    :type: ADDS_FORECAST_TYPE

    Get the ADDS message type.

.. py:property:: source
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessage.source
    :type: str

    Get the ADDS message source.


