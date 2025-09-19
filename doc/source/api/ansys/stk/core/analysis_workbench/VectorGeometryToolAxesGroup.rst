VectorGeometryToolAxesGroup
===========================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup

   Access or create VGT axes associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolAxesGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.get_item_by_index`
              - Retrieve an axes from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.get_item_by_name`
              - Retrieve an axes from the collection by name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.item`
              - Return an axes by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.remove`
              - Remove a specified Axes.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.common_tasks`
              - Provide access to common tasks that allow users quickly carry out tasks such as creating known axes, etc.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.factory`
              - Return a Factory object used to create custom axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesGroup


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.common_tasks
    :type: VectorGeometryToolAxesCommonTasks

    Provide access to common tasks that allow users quickly carry out tasks such as creating known axes, etc.

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.factory
    :type: VectorGeometryToolAxesFactory

    Return a Factory object used to create custom axes.


Method detail
-------------


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`




.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.get_item_by_index

    Retrieve an axes from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.get_item_by_name

    Retrieve an axes from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolAxes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.item

    Return an axes by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IVectorGeometryToolAxes`

.. py:method:: remove(self, axes_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesGroup.remove

    Remove a specified Axes.

    :Parameters:

        **axes_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


