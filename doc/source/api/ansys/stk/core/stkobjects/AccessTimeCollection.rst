AccessTimeCollection
====================

.. py:class:: ansys.stk.core.stkobjects.AccessTimeCollection

   Collection of access times.

.. py:currentmodule:: AccessTimeCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimeCollection.item`
              - Return target times scheme by name or at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimeCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTimeCollection._NewEnum`
              - Enumerates the elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessTimeCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AccessTimeCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.AccessTimeCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AccessTime
    :canonical: ansys.stk.core.stkobjects.AccessTimeCollection.item

    Return target times scheme by name or at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AccessTime`


