IUserVariableUpdateCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection

   object
   
   The list of User Variables accessed through an Update segment.

.. py:currentmodule:: IUserVariableUpdateCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.get_item_by_index`
              - Retrieve a user variable update in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.get_item_by_name`
              - Retrieve a user variable update in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IUserVariableUpdateCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IUserVariableUpdate
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IUserVariableUpdate`



.. py:method:: get_item_by_index(self, index: int) -> IUserVariableUpdate
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.get_item_by_index

    Retrieve a user variable update in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IUserVariableUpdate`

.. py:method:: get_item_by_name(self, name: str) -> IUserVariableUpdate
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableUpdateCollection.get_item_by_name

    Retrieve a user variable update in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserVariableUpdate`

