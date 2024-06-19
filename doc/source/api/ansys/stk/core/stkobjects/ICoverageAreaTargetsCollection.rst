ICoverageAreaTargetsCollection
==============================

.. py:class:: ICoverageAreaTargetsCollection

   object
   
   Area Targets.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~remove`
              - Remove an element from the collection given a Target name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~available_area_targets`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageAreaTargetsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_area_targets
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.available_area_targets
    :type: list

    Gets the available area targets.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, targetName: str) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.add

    Add a new element to the collection.

    :Parameters:

    **targetName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, targetName: str) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageAreaTargetsCollection.remove

    Remove an element from the collection given a Target name.

    :Parameters:

    **targetName** : :obj:`~str`

    :Returns:

        :obj:`~None`


