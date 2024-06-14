IADDSMessage
============

.. py:class:: IADDSMessage

   object
   
   Interface used to access a message from the NOAA ADDS forecast.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~message_time`
            * - :py:meth:`~type`
            * - :py:meth:`~source`


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
    :type: "ADDS_FORECAST_TYPE"

    Get the ADDS message type.

.. py:property:: source
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessage.source
    :type: str

    Get the ADDS message source.


