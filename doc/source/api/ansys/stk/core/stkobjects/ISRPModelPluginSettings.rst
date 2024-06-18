ISRPModelPluginSettings
=======================

.. py:class:: ISRPModelPluginSettings

   object
   
   Plugin Light Reflection Model Settings.

.. py:currentmodule:: ansys.stk.core.stkobjects

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

    from ansys.stk.core.stkobjects import ISRPModelPluginSettings


Property detail
---------------

.. py:property:: available_properties
    :canonical: ansys.stk.core.stkobjects.ISRPModelPluginSettings.available_properties
    :type: list

    Available properties.


Method detail
-------------

.. py:method:: get_property(self, path:str) -> typing.Any

    Get a property.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path:str, val:typing.Any) -> None

    Set a property.

    :Parameters:

    **path** : :obj:`~str`
    **val** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`


