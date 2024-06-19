ICentralBodyCollection
======================

.. py:class:: ICentralBodyCollection

   object
   
   The list of central bodies.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~add`
              - Add a central body to the collection.
            * - :py:meth:`~remove`
              - Remove a central body from the collection.
            * - :py:meth:`~remove_all`
              - Remove all central bodies from the collection.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a central body from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a central body from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ICentralBodyCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection._NewEnum
    :type: EnumeratorProxy

    Iterates through the collection.


Method detail
-------------

.. py:method:: item(self, indexOrCbName: typing.Any) -> IAstrogatorCentralBody
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrCbName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IAstrogatorCentralBody`



.. py:method:: add(self, cbName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.add

    Add a central body to the collection.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.remove

    Remove a central body from the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.remove_all

    Remove all central bodies from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: get_item_by_index(self, index: int) -> IAstrogatorCentralBody
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.get_item_by_index

    Retrieve a central body from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAstrogatorCentralBody`

.. py:method:: get_item_by_name(self, cbName: str) -> IAstrogatorCentralBody
    :canonical: ansys.stk.core.stkobjects.astrogator.ICentralBodyCollection.get_item_by_name

    Retrieve a central body from the collection by name.

    :Parameters:

    **cbName** : :obj:`~str`

    :Returns:

        :obj:`~IAstrogatorCentralBody`

