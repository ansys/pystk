IPluginProperties
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPluginProperties

   object
   
   Properties of a plugin attitude control.

.. py:currentmodule:: IPluginProperties

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPluginProperties.get_property`
              - Get a property.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPluginProperties.set_property`
              - Set a property.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPluginProperties.available_properties`
              - Returns an array of all available properties.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPluginProperties


Property detail
---------------

.. py:property:: available_properties
    :canonical: ansys.stk.core.stkobjects.astrogator.IPluginProperties.available_properties
    :type: list

    Returns an array of all available properties.


Method detail
-------------

.. py:method:: get_property(self, path: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.astrogator.IPluginProperties.get_property

    Get a property.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path: str, propertyValue: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IPluginProperties.set_property

    Set a property.

    :Parameters:

    **path** : :obj:`~str`
    **propertyValue** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


