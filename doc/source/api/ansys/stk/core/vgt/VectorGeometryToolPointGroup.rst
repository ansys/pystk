VectorGeometryToolPointGroup
============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointGroup

   Bases: 

   Access or create VGT points associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolPointGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.remove`
              - Remove a specified point by name.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.item`
              - Return a point by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.get_item_by_index`
              - Retrieve a point from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.get_item_by_name`
              - Retrieve a point from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.factory`
              - Returns a Factory object used to create custom points.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup._NewEnum`
              - Returns a COM enumerator.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointGroup.common_tasks`
              - Provides access to common tasks that allow users quickly carry out tasks such as creating known point types, etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.factory
    :type: IVectorGeometryToolPointFactory

    Returns a Factory object used to create custom points.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.common_tasks
    :type: IVectorGeometryToolPointCommonTasks

    Provides access to common tasks that allow users quickly carry out tasks such as creating known point types, etc.


Method detail
-------------

.. py:method:: remove(self, pointName: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.remove

    Remove a specified point by name.

    :Parameters:

    **pointName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.item

    Return a point by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolPoint`



.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.get_item_by_index

    Retrieve a point from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolPoint`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointGroup.get_item_by_name

    Retrieve a point from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolPoint`

