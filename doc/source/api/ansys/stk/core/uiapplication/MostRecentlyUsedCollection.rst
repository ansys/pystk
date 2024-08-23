MostRecentlyUsedCollection
==========================

.. py:class:: ansys.stk.core.uiapplication.MostRecentlyUsedCollection

   Provide information about most recently used (MRU) list.

.. py:currentmodule:: MostRecentlyUsedCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.MostRecentlyUsedCollection.item`
              - Get the MRU at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.MostRecentlyUsedCollection.count`
              - Gets the total count of MRUs in the collection.
            * - :py:attr:`~ansys.stk.core.uiapplication.MostRecentlyUsedCollection._NewEnum`
              - Enumerates through the MRU collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import MostRecentlyUsedCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uiapplication.MostRecentlyUsedCollection.count
    :type: int

    Gets the total count of MRUs in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.uiapplication.MostRecentlyUsedCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the MRU collection.


Method detail
-------------

.. py:method:: item(self, index: typing.Any) -> str
    :canonical: ansys.stk.core.uiapplication.MostRecentlyUsedCollection.item

    Get the MRU at the specified index.

    :Parameters:

    **index** : :obj:`~typing.Any`

    :Returns:

        :obj:`~str`



