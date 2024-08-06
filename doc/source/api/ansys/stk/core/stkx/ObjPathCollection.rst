ObjPathCollection
=================

.. py:class:: ansys.stk.core.stkx.ObjPathCollection

   Collection of object paths.

.. py:currentmodule:: ObjPathCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.ObjPathCollection.item`
              - Get the element at the specified index (0-based).
            * - :py:attr:`~ansys.stk.core.stkx.ObjPathCollection.range`
              - Return the elements within the specified range.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.ObjPathCollection.count`
              - Number of elements contained in the collection.
            * - :py:attr:`~ansys.stk.core.stkx.ObjPathCollection._NewEnum`
              - Returns an object that can be used to iterate through all the object paths in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import ObjPathCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkx.ObjPathCollection.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkx.ObjPathCollection._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the object paths in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkx.ObjPathCollection.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: range(self, startIndex: int, stopIndex: int) -> list
    :canonical: ansys.stk.core.stkx.ObjPathCollection.range

    Return the elements within the specified range.

    :Parameters:

    **startIndex** : :obj:`~int`
    **stopIndex** : :obj:`~int`

    :Returns:

        :obj:`~list`

