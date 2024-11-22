PriorityCollection
==================

.. py:class:: ansys.stk.core.stkobjects.PriorityCollection

   Class defining a priority data collection.

.. py:currentmodule:: PriorityCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PriorityCollection.item`
              - Given an index, returns the item in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PriorityCollection.count`
              - Returns the number of priorities in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PriorityCollection._new_enum`
              - Returns an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PriorityCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.PriorityCollection.count
    :type: int

    Returns the number of priorities in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.PriorityCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Priority
    :canonical: ansys.stk.core.stkobjects.PriorityCollection.item

    Given an index, returns the item in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Priority`


