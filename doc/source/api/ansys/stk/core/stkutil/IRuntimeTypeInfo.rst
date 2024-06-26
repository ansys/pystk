IRuntimeTypeInfo
================

.. py:class:: ansys.stk.core.stkutil.IRuntimeTypeInfo

   object
   
   Interface used to retrieve the properties at runtime.

.. py:currentmodule:: IRuntimeTypeInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IRuntimeTypeInfo.get_item`
              - Return the property of the collection at the given index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IRuntimeTypeInfo.properties`
              - Get the collection of properties.
            * - :py:attr:`~ansys.stk.core.stkutil.IRuntimeTypeInfo.is_collection`
              - Determines if the interface is a collection.
            * - :py:attr:`~ansys.stk.core.stkutil.IRuntimeTypeInfo.count`
              - If the interface is a collection, returns the collection count.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IRuntimeTypeInfo


Property detail
---------------

.. py:property:: properties
    :canonical: ansys.stk.core.stkutil.IRuntimeTypeInfo.properties
    :type: IPropertyInfoCollection

    Get the collection of properties.

.. py:property:: is_collection
    :canonical: ansys.stk.core.stkutil.IRuntimeTypeInfo.is_collection
    :type: bool

    Determines if the interface is a collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IRuntimeTypeInfo.count
    :type: int

    If the interface is a collection, returns the collection count.


Method detail
-------------




.. py:method:: get_item(self, index: int) -> IPropertyInfo
    :canonical: ansys.stk.core.stkutil.IRuntimeTypeInfo.get_item

    Return the property of the collection at the given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IPropertyInfo`

