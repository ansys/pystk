VectorGeometryToolPlaneGroup
============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup

   Represents a VGT Plane component.

.. py:currentmodule:: VectorGeometryToolPlaneGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.remove`
              - Remove a specified Plane.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.item`
              - Return an Plane by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.get_item_by_index`
              - Retrieve a plane from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.get_item_by_name`
              - Retrieve a plane from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.factory`
              - Return a Factory object used to create custom planes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPlaneGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPlaneGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.factory
    :type: VectorGeometryToolPlaneFactory

    Return a Factory object used to create custom planes.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, plane_name: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.remove

    Remove a specified Plane.

    :Parameters:

    **plane_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.item

    Return an Plane by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`


.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.get_item_by_index

    Retrieve a plane from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPlaneGroup.get_item_by_name

    Retrieve a plane from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

