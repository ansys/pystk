IVectorGeometryToolPlaneGroup
=============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup

   object
   
   Represents a single entry point to manipulate VGT Planes associated with an object.

.. py:currentmodule:: IVectorGeometryToolPlaneGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.remove`
              - Remove a specified Plane.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.item`
              - Return an Plane by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.get_item_by_index`
              - Retrieve a plane from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.get_item_by_name`
              - Retrieve a plane from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.factory`
              - Returns a Factory object used to create custom planes.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup._NewEnum`
              - Returns a COM enumerator.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPlaneGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.factory
    :type: IVectorGeometryToolPlaneFactory

    Returns a Factory object used to create custom planes.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, planeName: str) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.remove

    Remove a specified Plane.

    :Parameters:

    **planeName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.item

    Return an Plane by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`


.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.get_item_by_index

    Retrieve a plane from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolPlane
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPlaneGroup.get_item_by_name

    Retrieve a plane from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolPlane`

