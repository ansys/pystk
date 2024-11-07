ObjectPathCollection
====================

.. py:class:: ansys.stk.core.stkx.ObjectPathCollection

   Collection of object paths.

.. py:currentmodule:: ObjectPathCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.ObjectPathCollection.item`
              - Get the element at the specified index (0-based).
            * - :py:attr:`~ansys.stk.core.stkx.ObjectPathCollection.range`
              - Return the elements within the specified range.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.ObjectPathCollection.count`
              - Number of elements contained in the collection.
            * - :py:attr:`~ansys.stk.core.stkx.ObjectPathCollection._NewEnum`
              - Returns an object that can be used to iterate through all the object paths in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import ObjectPathCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkx.ObjectPathCollection.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkx.ObjectPathCollection._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the object paths in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkx.ObjectPathCollection.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: range(self, start_index: int, stop_index: int) -> list
    :canonical: ansys.stk.core.stkx.ObjectPathCollection.range

    Return the elements within the specified range.

    :Parameters:

    **start_index** : :obj:`~int`
    **stop_index** : :obj:`~int`

    :Returns:

        :obj:`~list`

