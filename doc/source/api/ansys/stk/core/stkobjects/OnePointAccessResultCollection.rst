OnePointAccessResultCollection
==============================

.. py:class:: ansys.stk.core.stkobjects.OnePointAccessResultCollection

   Represents the data sets for one point access.

.. py:currentmodule:: OnePointAccessResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessResultCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessResultCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.OnePointAccessResultCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import OnePointAccessResultCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.OnePointAccessResultCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.OnePointAccessResultCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> OnePointAccessResult
    :canonical: ansys.stk.core.stkobjects.OnePointAccessResultCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~OnePointAccessResult`


