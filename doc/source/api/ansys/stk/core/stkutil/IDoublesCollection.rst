IDoublesCollection
==================

.. py:class:: IDoublesCollection

   object
   
   Represents a collection of doubles.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return a double at a specified position.
            * - :py:meth:`~add`
              - Add a value to the collection of doubles.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection at a specified position.
            * - :py:meth:`~remove_all`
              - Clear the collection.
            * - :py:meth:`~to_array`
              - Return an array of the elements in the collection.
            * - :py:meth:`~set_at`
              - Update an element in the collection at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IDoublesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IDoublesCollection.count
    :type: int

    Returns the number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.IDoublesCollection._NewEnum
    :type: EnumeratorProxy

    Returns a collection enumerator.


Method detail
-------------

.. py:method:: item(self, index:int) -> float

    Return a double at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~float`



.. py:method:: add(self, value:float) -> None

    Add a value to the collection of doubles.

    :Parameters:

    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index:int) -> None

    Remove an element from the collection at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Clear the collection.

    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list

    Return an array of the elements in the collection.

    :Returns:

        :obj:`~list`

.. py:method:: set_at(self, index:int, value:float) -> None

    Update an element in the collection at a specified position.

    :Parameters:

    **index** : :obj:`~int`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~None`

