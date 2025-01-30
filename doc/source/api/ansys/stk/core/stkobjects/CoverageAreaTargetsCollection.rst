CoverageAreaTargetsCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection

   Collection of Area Targets.

.. py:currentmodule:: CoverageAreaTargetsCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.remove`
              - Remove an element from the collection given a Target name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.available_area_targets`
              - Gets the available area targets.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageAreaTargetsCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_area_targets
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.available_area_targets
    :type: list

    Gets the available area targets.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, target_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.add

    Add a new element to the collection.

    :Parameters:

    **target_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, target_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageAreaTargetsCollection.remove

    Remove an element from the collection given a Target name.

    :Parameters:

    **target_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


