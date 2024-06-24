ITimeToolEventIntervalGroup
===========================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalGroup

   object
   
   Access or create VGT event intervals associated with an object.

.. py:currentmodule:: ITimeToolEventIntervalGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.remove`
              - Remove an element by name.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.get_item_by_index`
              - Retrieve an event interval from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.get_item_by_name`
              - Retrieve an event interval from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.context`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.count`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup.factory`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalGroup._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.factory
    :type: ITimeToolEventIntervalFactory

    Returns a Factory object used to create custom event intervals.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventIntervalName: str) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.remove

    Remove an element by name.

    :Parameters:

    **eventIntervalName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITimeToolEventInterval`


.. py:method:: get_item_by_index(self, index: int) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.get_item_by_index

    Retrieve an event interval from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITimeToolEventInterval`

.. py:method:: get_item_by_name(self, name: str) -> ITimeToolEventInterval
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalGroup.get_item_by_name

    Retrieve an event interval from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ITimeToolEventInterval`

