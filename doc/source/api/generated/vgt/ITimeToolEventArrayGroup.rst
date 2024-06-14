ITimeToolEventArrayGroup
========================

.. py:class:: ITimeToolEventArrayGroup

   object
   
   Access or create VGT event arrays associated with an object.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove`
              - Remove a specified element.
            * - :py:meth:`~contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return an element by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve an event array from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve an event array from the collection by name.

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

    from ansys.stk.core.vgt import ITimeToolEventArrayGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayGroup.context
    :type: "IAgCrdnContext"

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayGroup.factory
    :type: "IAgCrdnEventArrayFactory"

    Returns a Factory object used to create event arrays.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolEventArrayGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventName:str) -> None

    Remove a specified element.

    :Parameters:

    **eventName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name:str) -> bool

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName:typing.Any) -> "ITimeToolEventArray"

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"ITimeToolEventArray"`


.. py:method:: get_item_by_index(self, index:int) -> "ITimeToolEventArray"

    Retrieve an event array from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ITimeToolEventArray"`

.. py:method:: get_item_by_name(self, name:str) -> "ITimeToolEventArray"

    Retrieve an event array from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"ITimeToolEventArray"`

