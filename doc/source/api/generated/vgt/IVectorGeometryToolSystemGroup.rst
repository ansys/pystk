IVectorGeometryToolSystemGroup
==============================

.. py:class:: IVectorGeometryToolSystemGroup

   object
   
   Access or create VGT systems associated with an object or a central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove`
              - Remove a specified System.
            * - :py:meth:`~contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return a System by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a system from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a system from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~context`
            * - :py:meth:`~count`
            * - :py:meth:`~factory`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~common_tasks`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemGroup.context
    :type: "IAgCrdnContext"

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemGroup.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemGroup.factory
    :type: "IAgCrdnSystemFactory"

    Returns a Factory object used to create custom VGT systems.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemGroup.common_tasks
    :type: "IAgCrdnSystemCommonTasks"

    Provides access to common tasks that allow users quickly carry out tasks such as creating known systems, etc.


Method detail
-------------

.. py:method:: remove(self, systemName:str) -> None

    Remove a specified System.

    :Parameters:

    **systemName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name:str) -> bool

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName:typing.Any) -> "IVectorGeometryToolSystem"

    Return a System by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IVectorGeometryToolSystem"`



.. py:method:: get_item_by_index(self, index:int) -> "IVectorGeometryToolSystem"

    Retrieve a system from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVectorGeometryToolSystem"`

.. py:method:: get_item_by_name(self, name:str) -> "IVectorGeometryToolSystem"

    Retrieve a system from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IVectorGeometryToolSystem"`

