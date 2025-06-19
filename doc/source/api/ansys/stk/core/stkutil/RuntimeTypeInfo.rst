RuntimeTypeInfo
===============

.. py:class:: ansys.stk.core.stkutil.RuntimeTypeInfo

   Runtime Type info coclass.

.. py:currentmodule:: RuntimeTypeInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.RuntimeTypeInfo.get_item`
              - Return the property of the collection at the given index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.RuntimeTypeInfo.properties`
              - Get the collection of properties.
            * - :py:attr:`~ansys.stk.core.stkutil.RuntimeTypeInfo.is_collection`
              - Determine if the interface is a collection.
            * - :py:attr:`~ansys.stk.core.stkutil.RuntimeTypeInfo.count`
              - If the interface is a collection, returns the collection count.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import RuntimeTypeInfo


Property detail
---------------

.. py:property:: properties
    :canonical: ansys.stk.core.stkutil.RuntimeTypeInfo.properties
    :type: PropertyInfoCollection

    Get the collection of properties.

.. py:property:: is_collection
    :canonical: ansys.stk.core.stkutil.RuntimeTypeInfo.is_collection
    :type: bool

    Determine if the interface is a collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.RuntimeTypeInfo.count
    :type: int

    If the interface is a collection, returns the collection count.


Method detail
-------------




.. py:method:: get_item(self, index: int) -> PropertyInfo
    :canonical: ansys.stk.core.stkutil.RuntimeTypeInfo.get_item

    Return the property of the collection at the given index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~PropertyInfo`

