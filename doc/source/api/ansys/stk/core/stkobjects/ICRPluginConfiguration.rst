ICRPluginConfiguration
======================

.. py:class:: ansys.stk.core.stkobjects.ICRPluginConfiguration

   object
   
   Provide access to plugin properties.

.. py:currentmodule:: ICRPluginConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICRPluginConfiguration.get_property`
              - Get a property.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICRPluginConfiguration.set_property`
              - Set a property.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICRPluginConfiguration.available_properties`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICRPluginConfiguration


Property detail
---------------

.. py:property:: available_properties
    :canonical: ansys.stk.core.stkobjects.ICRPluginConfiguration.available_properties
    :type: list

    Available properties.


Method detail
-------------

.. py:method:: get_property(self, path: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.ICRPluginConfiguration.get_property

    Get a property.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path: str, val: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.ICRPluginConfiguration.set_property

    Set a property.

    :Parameters:

    **path** : :obj:`~str`
    **val** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


