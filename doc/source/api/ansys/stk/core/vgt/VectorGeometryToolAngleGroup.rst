VectorGeometryToolAngleGroup
============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleGroup

   Access or create VGT angles associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolAngleGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.remove`
              - Remove a specified Angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.item`
              - Return an angle by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.get_item_by_index`
              - Retrieve an angle from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.get_item_by_name`
              - Retrieve an angle from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup.factory`
              - Returns a Factory object used to create custom angles.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleGroup._new_enum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.factory
    :type: VectorGeometryToolAngleFactory

    Returns a Factory object used to create custom angles.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup._new_enum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, angle_name: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.remove

    Remove a specified Angle.

    :Parameters:

    **angle_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.item

    Return an angle by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`


.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.get_item_by_index

    Retrieve an angle from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleGroup.get_item_by_name

    Retrieve an angle from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

