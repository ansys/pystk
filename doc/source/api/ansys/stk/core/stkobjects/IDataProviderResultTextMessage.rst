IDataProviderResultTextMessage
==============================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultTextMessage

   object
   
   Represents notification/failure message returned by the data provider.

.. py:currentmodule:: IDataProviderResultTextMessage

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTextMessage.item`
              - Given an index, returns a string in the collection at the given position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTextMessage.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTextMessage._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTextMessage.messages`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTextMessage.is_failure`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultTextMessage


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTextMessage.count
    :type: int

    Returns a number of strings in the message.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTextMessage._NewEnum
    :type: EnumeratorProxy

    Returns a string enumeration.

.. py:property:: messages
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTextMessage.messages
    :type: list

    Returns an array of strings in the message.

.. py:property:: is_failure
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTextMessage.is_failure
    :type: bool

    Determines if the message represents a failure notification.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTextMessage.item

    Given an index, returns a string in the collection at the given position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`




