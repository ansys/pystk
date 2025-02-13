DataProviderElements
====================

.. py:class:: ansys.stk.core.stkobjects.DataProviderElements

   Elements returned by the data provider (e.g. ``x``, ``y``, ``z``).

.. py:currentmodule:: DataProviderElements

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderElements.item`
              - Return the specific item provided an Index.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderElements.get_item_by_index`
              - Return the specific item provided an Index.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderElements.get_item_by_name`
              - Return the specific item provided a Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderElements.count`
              - Return number of elements for this data provider.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderElements._new_enum`
              - Return enum of AgDataPrvElement object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderElements


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderElements.count
    :type: int

    Return number of elements for this data provider.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderElements._new_enum
    :type: EnumeratorProxy

    Return enum of AgDataPrvElement object.


Method detail
-------------

.. py:method:: item(self, index_or_name: typing.Any) -> DataProviderElement
    :canonical: ansys.stk.core.stkobjects.DataProviderElements.item

    Return the specific item provided an Index.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderElement`



.. py:method:: get_item_by_index(self, index: int) -> DataProviderElement
    :canonical: ansys.stk.core.stkobjects.DataProviderElements.get_item_by_index

    Return the specific item provided an Index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DataProviderElement`

.. py:method:: get_item_by_name(self, name: str) -> DataProviderElement
    :canonical: ansys.stk.core.stkobjects.DataProviderElements.get_item_by_name

    Return the specific item provided a Name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~DataProviderElement`

