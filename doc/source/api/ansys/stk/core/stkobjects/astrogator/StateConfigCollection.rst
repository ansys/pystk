StateConfigCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateConfigCollection

   State config. properties Collection.

.. py:currentmodule:: StateConfigCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateConfigCollection.get_item_by_index`
              - Retrieve a state config property in the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateConfigCollection.get_item_by_name`
              - Retrieve a state config property in the collection by name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateConfigCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateConfigCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateConfigCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateConfigCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.StateConfigCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.StateConfigCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------


.. py:method:: get_item_by_index(self, index: int) -> StateConfig
    :canonical: ansys.stk.core.stkobjects.astrogator.StateConfigCollection.get_item_by_index

    Retrieve a state config property in the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~StateConfig`

.. py:method:: get_item_by_name(self, name: str) -> StateConfig
    :canonical: ansys.stk.core.stkobjects.astrogator.StateConfigCollection.get_item_by_name

    Retrieve a state config property in the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~StateConfig`

.. py:method:: item(self, index_or_name: typing.Any) -> StateConfig
    :canonical: ansys.stk.core.stkobjects.astrogator.StateConfigCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~StateConfig`


