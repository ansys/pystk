IStkCentralBodyCollection
=========================

.. py:class:: IStkCentralBodyCollection

   object
   
   A collection of available central bodies.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~contains`
              - Search for a central body with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return a central body by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a central body from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~earth`
            * - :py:meth:`~sun`
            * - :py:meth:`~moon`
            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkCentralBodyCollection


Property detail
---------------

.. py:property:: earth
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.earth
    :type: IAgStkCentralBody

    Returns the Earth central body.

.. py:property:: sun
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.sun
    :type: IAgStkCentralBody

    Returns the Sun central body.

.. py:property:: moon
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.moon
    :type: IAgStkCentralBody

    Returns the Moon central body.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------

.. py:method:: contains(self, centralName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.contains

    Search for a central body with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **centralName** : :obj:`~str`

    :Returns:

        :obj:`~bool`





.. py:method:: item(self, indexOrName: typing.Any) -> IStkCentralBody
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.item

    Return a central body by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IStkCentralBody`


.. py:method:: get_item_by_index(self, index: int) -> IStkCentralBody
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IStkCentralBody`

.. py:method:: get_item_by_name(self, cbName: str) -> IStkCentralBody
    :canonical: ansys.stk.core.stkobjects.IStkCentralBodyCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~IStkCentralBody`

