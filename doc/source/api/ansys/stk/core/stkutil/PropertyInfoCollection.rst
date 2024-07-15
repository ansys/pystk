PropertyInfoCollection
======================

.. py:class:: ansys.stk.core.stkutil.PropertyInfoCollection

   Bases: 

   Property Information Collection coclass.

.. py:currentmodule:: PropertyInfoCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfoCollection.item`
              - Allow the user to iterate through the properties.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfoCollection.get_item_by_index`
              - Retrieve a property from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfoCollection.get_item_by_name`
              - Retrieve a property from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfoCollection._NewEnum`
              - Enumerates through the properties.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfoCollection.count`
              - Get the number of properties available.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import PropertyInfoCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.PropertyInfoCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the properties.

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.PropertyInfoCollection.count
    :type: int

    Get the number of properties available.


Method detail
-------------

.. py:method:: item(self, indexOrName: typing.Any) -> PropertyInfo
    :canonical: ansys.stk.core.stkutil.PropertyInfoCollection.item

    Allow the user to iterate through the properties.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~PropertyInfo`



.. py:method:: get_item_by_index(self, index: int) -> PropertyInfo
    :canonical: ansys.stk.core.stkutil.PropertyInfoCollection.get_item_by_index

    Retrieve a property from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~PropertyInfo`

.. py:method:: get_item_by_name(self, name: str) -> PropertyInfo
    :canonical: ansys.stk.core.stkutil.PropertyInfoCollection.get_item_by_name

    Retrieve a property from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~PropertyInfo`

