IDataProviderElements
=====================

.. py:class:: IDataProviderElements

   object
   
   Represents a collection of elements in the data provider (for instance ``x``, ``y``, ``z``).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return the specific item provided an Index.
            * - :py:meth:`~get_item_by_index`
              - Return the specific item provided an Index.
            * - :py:meth:`~get_item_by_name`
              - Return the specific item provided a Name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderElements


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderElements.count
    :type: int

    Returns number of elements for this data provider.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IDataProviderElements._NewEnum
    :type: EnumeratorProxy

    Returns enum of AgDataPrvElement object.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IDataProviderElement
    :canonical: ansys.stk.core.stkobjects.IDataProviderElements.item

    Return the specific item provided an Index.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDataProviderElement`



.. py:method:: get_item_by_index(self, index: int) -> IDataProviderElement
    :canonical: ansys.stk.core.stkobjects.IDataProviderElements.get_item_by_index

    Return the specific item provided an Index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IDataProviderElement`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderElement
    :canonical: ansys.stk.core.stkobjects.IDataProviderElements.get_item_by_name

    Return the specific item provided a Name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IDataProviderElement`

