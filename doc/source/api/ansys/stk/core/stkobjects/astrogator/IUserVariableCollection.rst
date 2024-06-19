IUserVariableCollection
=======================

.. py:class:: IUserVariableCollection

   object
   
   The list of User Variables accessed through a segment that sets initial conditions.

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
            * - :py:meth:`~get_item_by_index`
              - Retrieve a user variable in the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a user variable in the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IUserVariableCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IUserVariable
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IUserVariable`



.. py:method:: get_item_by_index(self, index: int) -> IUserVariable
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableCollection.get_item_by_index

    Retrieve a user variable in the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IUserVariable`

.. py:method:: get_item_by_name(self, name: str) -> IUserVariable
    :canonical: ansys.stk.core.stkobjects.astrogator.IUserVariableCollection.get_item_by_name

    Retrieve a user variable in the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IUserVariable`

