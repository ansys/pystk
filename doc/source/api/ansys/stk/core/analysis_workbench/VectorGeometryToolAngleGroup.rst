VectorGeometryToolAngleGroup
============================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup

   Access or create VGT angles associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolAngleGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.get_item_by_index`
              - Retrieve an angle from the collection by index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.get_item_by_name`
              - Retrieve an angle from the collection by name.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.item`
              - Return an angle by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.remove`
              - Remove a specified Angle.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.factory`
              - Return a Factory object used to create custom angles.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAngleGroup


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: context
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.factory
    :type: VectorGeometryToolAngleFactory

    Return a Factory object used to create custom angles.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`




.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.get_item_by_index

    Retrieve an angle from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.get_item_by_name

    Retrieve an angle from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.item

    Return an angle by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: remove(self, angle_name: str) -> None
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAngleGroup.remove

    Remove a specified Angle.

    :Parameters:

        **angle_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


