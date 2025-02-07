VectorGeometryToolVectorGroup
=============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorGroup

   Access or create VGT vectors associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolVectorGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.remove`
              - Remove a specified vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.item`
              - Return a vector by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.get_item_by_index`
              - Retrieve a vector from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.get_item_by_name`
              - Retrieve a vector from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup.factory`
              - Return a Factory object used to create custom vectors.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorGroup._new_enum`
              - Return a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.factory
    :type: VectorGeometryToolVectorFactory

    Return a Factory object used to create custom vectors.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, vector_name: str) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.remove

    Remove a specified vector.

    :Parameters:

    **vector_name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.item

    Return a vector by name or at a specified position.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolVector`


.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.get_item_by_index

    Retrieve a vector from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolVector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorGroup.get_item_by_name

    Retrieve a vector from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolVector`

