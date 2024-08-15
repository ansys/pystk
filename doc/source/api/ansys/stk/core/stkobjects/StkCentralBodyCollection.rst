StkCentralBodyCollection
========================

.. py:class:: ansys.stk.core.stkobjects.StkCentralBodyCollection

   Central body collection coclass.

.. py:currentmodule:: StkCentralBodyCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.contains`
              - Search for a central body with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.item`
              - Return a central body by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.get_item_by_name`
              - Retrieve a central body from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.earth`
              - Returns the Earth central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.sun`
              - Returns the Sun central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.moon`
              - Returns the Moon central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkCentralBodyCollection._NewEnum`
              - Enumerates the elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkCentralBodyCollection


Property detail
---------------

.. py:property:: earth
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.earth
    :type: StkCentralBody

    Returns the Earth central body.

.. py:property:: sun
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.sun
    :type: StkCentralBody

    Returns the Sun central body.

.. py:property:: moon
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.moon
    :type: StkCentralBody

    Returns the Moon central body.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------

.. py:method:: contains(self, centralName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.contains

    Search for a central body with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **centralName** : :obj:`~str`

    :Returns:

        :obj:`~bool`





.. py:method:: item(self, indexOrName: typing.Any) -> StkCentralBody
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.item

    Return a central body by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~StkCentralBody`


.. py:method:: get_item_by_index(self, index: int) -> StkCentralBody
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~StkCentralBody`

.. py:method:: get_item_by_name(self, cbName: str) -> StkCentralBody
    :canonical: ansys.stk.core.stkobjects.StkCentralBodyCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~StkCentralBody`

