IPropertyInfoCollection
=======================

.. py:class:: IPropertyInfoCollection

   object
   
   The collection of properties.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow the user to iterate through the properties.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a property from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a property from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IPropertyInfoCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.IPropertyInfoCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the properties.

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IPropertyInfoCollection.count
    :type: int

    Get the number of properties available.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> IPropertyInfo
    :canonical: ansys.stk.core.stkutil.IPropertyInfoCollection.item

    Allow the user to iterate through the properties.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IPropertyInfo`



.. py:method:: get_item_by_index(self, index: int) -> IPropertyInfo
    :canonical: ansys.stk.core.stkutil.IPropertyInfoCollection.get_item_by_index

    Retrieve a property from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IPropertyInfo`

.. py:method:: get_item_by_name(self, name: str) -> IPropertyInfo
    :canonical: ansys.stk.core.stkutil.IPropertyInfoCollection.get_item_by_name

    Retrieve a property from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IPropertyInfo`

