VectorGeometryToolPointGroup
============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup

   Access or create VGT points associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolPointGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.remove`
              - Remove a specified point by name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.item`
              - Return a point by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.get_item_by_index`
              - Retrieve a point from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.get_item_by_name`
              - Retrieve a point from the collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.factory`
              - Return a Factory object used to create custom points.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.common_tasks`
              - Provide access to common tasks that allow users quickly carry out tasks such as creating known point types, etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.factory
    :type: VectorGeometryToolPointFactory

    Return a Factory object used to create custom points.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.common_tasks
    :type: VectorGeometryToolPointCommonTasks

    Provide access to common tasks that allow users quickly carry out tasks such as creating known point types, etc.


Method detail
-------------

.. py:method:: remove(self, point_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.remove

    Remove a specified point by name.

    :Parameters:

        **point_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.item

    Return a point by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IVectorGeometryToolPoint`



.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.get_item_by_index

    Retrieve a point from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IVectorGeometryToolPoint`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolPoint
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointGroup.get_item_by_name

    Retrieve a point from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IVectorGeometryToolPoint`

