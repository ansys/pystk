IPluginProperties
=================

.. py:class:: IPluginProperties

   object
   
   Properties of a plugin attitude control.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_property`
              - Get a property.
            * - :py:meth:`~set_property`
              - Set a property.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~available_properties`


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

.. py:method:: get_property(self, path:str) -> typing.Any

    Get a property.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path:str, propertyValue:typing.Any) -> None

    Set a property.

    :Parameters:

    **path** : :obj:`~str`
    **propertyValue** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


