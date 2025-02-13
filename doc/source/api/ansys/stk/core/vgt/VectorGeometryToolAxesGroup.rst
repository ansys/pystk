VectorGeometryToolAxesGroup
===========================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesGroup

   Access or create VGT axes associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolAxesGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.remove`
              - Remove a specified Axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.item`
              - Return an axes by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.get_item_by_index`
              - Retrieve an axes from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.get_item_by_name`
              - Retrieve an axes from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.factory`
              - Return a Factory object used to create custom axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesGroup.common_tasks`
              - Provide access to common tasks that allow users quickly carry out tasks such as creating known axes, etc.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.factory
    :type: VectorGeometryToolAxesFactory

    Return a Factory object used to create custom axes.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.common_tasks
    :type: VectorGeometryToolAxesCommonTasks

    Provide access to common tasks that allow users quickly carry out tasks such as creating known axes, etc.


Method detail
-------------

.. py:method:: remove(self, axes_name: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.remove

    Remove a specified Axes.

    :Parameters:

    **axes_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.item

    Return an axes by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolAxes`



.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.get_item_by_index

    Retrieve an axes from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesGroup.get_item_by_name

    Retrieve an axes from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolAxes`

