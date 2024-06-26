IPropertyInfo
=============

.. py:class:: ansys.stk.core.stkutil.IPropertyInfo

   object
   
   Property information.

.. py:currentmodule:: IPropertyInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.get_value`
              - Get the value of the property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.set_value`
              - Set the value of the property. Use PropertyType to determine the type to cast to.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.name`
              - Get the name of the property.
            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.property_type`
              - Get the type of property.
            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.has_min`
              - Determine if the property has a minimum value.
            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.has_max`
              - Determine if the property has a maximum value.
            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.min`
              - Get the minimum value of this property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~ansys.stk.core.stkutil.IPropertyInfo.max`
              - Get the maximum value of this property. Use PropertyType to determine the type to cast to.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IPropertyInfo


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.name
    :type: str

    Get the name of the property.

.. py:property:: property_type
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.property_type
    :type: PROPERTY_INFO_VALUE_TYPE

    Get the type of property.

.. py:property:: has_min
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.has_min
    :type: bool

    Determine if the property has a minimum value.

.. py:property:: has_max
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.has_max
    :type: bool

    Determine if the property has a maximum value.

.. py:property:: min
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.min
    :type: typing.Any

    Get the minimum value of this property. Use PropertyType to determine the type to cast to.

.. py:property:: max
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.max
    :type: typing.Any

    Get the maximum value of this property. Use PropertyType to determine the type to cast to.


Method detail
-------------



.. py:method:: get_value(self) -> typing.Any
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.get_value

    Get the value of the property. Use PropertyType to determine the type to cast to.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_value(self, propertyInfo: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.IPropertyInfo.set_value

    Set the value of the property. Use PropertyType to determine the type to cast to.

    :Parameters:

    **propertyInfo** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`





