IVectorGeometryToolVectorGroup
==============================

.. py:class:: IVectorGeometryToolVectorGroup

   object
   
   Access or create VGT vectors associated with an object or a central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove`
              - Remove a specified vector.
            * - :py:meth:`~contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return a vector by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a vector from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a vector from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~context`
            * - :py:meth:`~count`
            * - :py:meth:`~factory`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorGroup.context
    :type: "IAgCrdnContext"

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorGroup.factory
    :type: "IAgCrdnVectorFactory"

    Returns a Factory object used to create custom vectors.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, vectorName:str) -> None

    Remove a specified vector.

    :Parameters:

    **vectorName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name:str) -> bool

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName:typing.Any) -> "IVectorGeometryToolVector"

    Return a vector by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IVectorGeometryToolVector"`


.. py:method:: get_item_by_index(self, index:int) -> "IVectorGeometryToolVector"

    Retrieve a vector from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVectorGeometryToolVector"`

.. py:method:: get_item_by_name(self, name:str) -> "IVectorGeometryToolVector"

    Retrieve a vector from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IVectorGeometryToolVector"`

