IVectorGeometryToolAxesGroup
============================

.. py:class:: IVectorGeometryToolAxesGroup

   object
   
   Access or create VGT axes associated with an object or a central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove`
              - Remove a specified Axes.
            * - :py:meth:`~contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return an axes by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve an axes from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve an axes from the collection by name.

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

    from ansys.stk.core.vgt import IVectorGeometryToolAxesGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesGroup.context
    :type: "IAgCrdnContext"

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesGroup.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesGroup.factory
    :type: "IAgCrdnAxesFactory"

    Returns a Factory object used to create custom axes.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesGroup.common_tasks
    :type: "IAgCrdnAxesCommonTasks"

    Provides access to common tasks that allow users quickly carry out tasks such as creating known axes, etc.


Method detail
-------------

.. py:method:: remove(self, axesName:str) -> None

    Remove a specified Axes.

    :Parameters:

    **axesName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name:str) -> bool

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName:typing.Any) -> "IVectorGeometryToolAxes"

    Return an axes by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IVectorGeometryToolAxes"`



.. py:method:: get_item_by_index(self, index:int) -> "IVectorGeometryToolAxes"

    Retrieve an axes from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVectorGeometryToolAxes"`

.. py:method:: get_item_by_name(self, name:str) -> "IVectorGeometryToolAxes"

    Retrieve an axes from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IVectorGeometryToolAxes"`

