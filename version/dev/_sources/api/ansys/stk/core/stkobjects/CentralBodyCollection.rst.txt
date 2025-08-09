CentralBodyCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.CentralBodyCollection

   Central body collection coclass.

.. py:currentmodule:: CentralBodyCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.contains`
              - Search for a central body with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.get_item_by_name`
              - Retrieve a central body from the collection by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.item`
              - Return a central body by name or at a specified position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection._new_enum`
              - Enumerates the elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.earth`
              - Return the Earth central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.moon`
              - Return the Moon central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.CentralBodyCollection.sun`
              - Return the Sun central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CentralBodyCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection._new_enum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: earth
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.earth
    :type: CentralBody

    Return the Earth central body.

.. py:property:: moon
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.moon
    :type: CentralBody

    Return the Moon central body.

.. py:property:: sun
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.sun
    :type: CentralBody

    Return the Sun central body.


Method detail
-------------

.. py:method:: contains(self, central_name: str) -> bool
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.contains

    Search for a central body with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **central_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`



.. py:method:: get_item_by_index(self, index: int) -> CentralBody
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~CentralBody`

.. py:method:: get_item_by_name(self, cb_name: str) -> CentralBody
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

        **cb_name** : :obj:`~str`


    :Returns:

        :obj:`~CentralBody`

.. py:method:: item(self, index_or_name: typing.Any) -> CentralBody
    :canonical: ansys.stk.core.stkobjects.CentralBodyCollection.item

    Return a central body by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~CentralBody`




