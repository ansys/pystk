DataProviderResultTextMessage
=============================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultTextMessage

   Notification or failure messages returned by the data provider.

.. py:currentmodule:: DataProviderResultTextMessage

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage.item`
              - Given an index, returns a string in the collection at the given position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage.count`
              - Return a number of strings in the message.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage._new_enum`
              - Return a string enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage.messages`
              - Return an array of strings in the message.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTextMessage.is_failure`
              - Determine if the message represents a failure notification.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultTextMessage


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTextMessage.count
    :type: int

    Return a number of strings in the message.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTextMessage._new_enum
    :type: EnumeratorProxy

    Return a string enumeration.

.. py:property:: messages
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTextMessage.messages
    :type: list

    Return an array of strings in the message.

.. py:property:: is_failure
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTextMessage.is_failure
    :type: bool

    Determine if the message represents a failure notification.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTextMessage.item

    Given an index, returns a string in the collection at the given position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`




