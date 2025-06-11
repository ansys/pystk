PropertyInfo
============

.. py:class:: ansys.stk.core.stkutil.PropertyInfo

   Property Information coclass.

.. py:currentmodule:: PropertyInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.get_value`
              - Get the value of the property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.set_value`
              - Set the value of the property. Use PropertyType to determine the type to cast to.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.name`
              - Get the name of the property.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.property_type`
              - Get the type of property.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.has_min`
              - Determine if the property has a minimum value.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.has_max`
              - Determine if the property has a maximum value.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.min`
              - Get the minimum value of this property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~ansys.stk.core.stkutil.PropertyInfo.max`
              - Get the maximum value of this property. Use PropertyType to determine the type to cast to.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import PropertyInfo


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkutil.PropertyInfo.name
    :type: str

    Get the name of the property.

.. py:property:: property_type
    :canonical: ansys.stk.core.stkutil.PropertyInfo.property_type
    :type: PropertyInfoValueType

    Get the type of property.

.. py:property:: has_min
    :canonical: ansys.stk.core.stkutil.PropertyInfo.has_min
    :type: bool

    Determine if the property has a minimum value.

.. py:property:: has_max
    :canonical: ansys.stk.core.stkutil.PropertyInfo.has_max
    :type: bool

    Determine if the property has a maximum value.

.. py:property:: min
    :canonical: ansys.stk.core.stkutil.PropertyInfo.min
    :type: typing.Any

    Get the minimum value of this property. Use PropertyType to determine the type to cast to.

.. py:property:: max
    :canonical: ansys.stk.core.stkutil.PropertyInfo.max
    :type: typing.Any

    Get the maximum value of this property. Use PropertyType to determine the type to cast to.


Method detail
-------------



.. py:method:: get_value(self) -> typing.Any
    :canonical: ansys.stk.core.stkutil.PropertyInfo.get_value

    Get the value of the property. Use PropertyType to determine the type to cast to.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_value(self, property_info: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.PropertyInfo.set_value

    Set the value of the property. Use PropertyType to determine the type to cast to.

    :Parameters:

        **property_info** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`





