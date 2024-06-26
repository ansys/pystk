ITimeToolEventIntervalListGroup
===============================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup

   object
   
   Access or create VGT event interval lists associated with an object.

.. py:currentmodule:: ITimeToolEventIntervalListGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.get_item_by_index`
              - Retrieve an event interval list from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.get_item_by_name`
              - Retrieve an event interval list from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.factory`
              - Returns a factory object used to create custom event interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListGroup._NewEnum`
              - Returns a COM enumerator.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalListGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.factory
    :type: ITimeToolEventIntervalListFactory

    Returns a factory object used to create custom event interval lists.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventName: str) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.remove

    Remove a specified element.

    :Parameters:

    **eventName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`


.. py:method:: get_item_by_index(self, index: int) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.get_item_by_index

    Retrieve an event interval list from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

.. py:method:: get_item_by_name(self, name: str) -> ITimeToolEventIntervalList
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListGroup.get_item_by_name

    Retrieve an event interval list from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventIntervalList`

