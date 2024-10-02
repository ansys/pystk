VectorGeometryToolSystemGroup
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolSystemGroup

   Access or create VGT systems associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolSystemGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.remove`
              - Remove a specified System.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.item`
              - Return a System by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.get_item_by_index`
              - Retrieve a system from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.get_item_by_name`
              - Retrieve a system from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.factory`
              - Returns a Factory object used to create custom VGT systems.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup._NewEnum`
              - Returns a COM enumerator.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemGroup.common_tasks`
              - Provides access to common tasks that allow users quickly carry out tasks such as creating known systems, etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolSystemGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.context
    :type: IComponentContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.factory
    :type: VectorGeometryToolSystemFactory

    Returns a Factory object used to create custom VGT systems.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.common_tasks
    :type: VectorGeometryToolSystemCommonTasks

    Provides access to common tasks that allow users quickly carry out tasks such as creating known systems, etc.


Method detail
-------------

.. py:method:: remove(self, systemName: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.remove

    Remove a specified System.

    :Parameters:

    **systemName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> IVectorGeometryToolSystem
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.item

    Return a System by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolSystem`



.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolSystem
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.get_item_by_index

    Retrieve a system from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolSystem`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolSystem
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemGroup.get_item_by_name

    Retrieve a system from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolSystem`

