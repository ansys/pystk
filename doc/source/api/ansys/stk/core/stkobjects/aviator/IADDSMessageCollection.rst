IADDSMessageCollection
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.IADDSMessageCollection

   object
   
   Interface used to access the collection of messages from the NOAA ADDS forecast.

.. py:currentmodule:: IADDSMessageCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.remove_message`
              - Remove this message from the forecast.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.clear_messages`
              - Clear all of the messages in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IADDSMessageCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IADDSMessageCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessageCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IADDSMessage
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IADDSMessage`


.. py:method:: remove_message(self, message: IADDSMessage) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.remove_message

    Remove this message from the forecast.

    :Parameters:

    **message** : :obj:`~IADDSMessage`

    :Returns:

        :obj:`~None`

.. py:method:: clear_messages(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IADDSMessageCollection.clear_messages

    Clear all of the messages in the collection.

    :Returns:

        :obj:`~None`

