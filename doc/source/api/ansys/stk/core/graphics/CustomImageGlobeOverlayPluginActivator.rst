CustomImageGlobeOverlayPluginActivator
======================================

.. py:class:: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivator

   Bases: 

   The Activator class provides methods to load COM plugins that implement custom image globe overlays. For more information about custom image globe overlays, see the STK Programming Interface.

.. py:currentmodule:: CustomImageGlobeOverlayPluginActivator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivator.create_from_display_name`
              - Load a custom image globe overlay COM plugin associated with the specified display name and returns a proxy object that allows accessing the custom image globe overlays implemented by the plugin.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivator.get_available_display_names`
              - Get a list of available custom image globe overlay Display Names (Programmatic Identifiers).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CustomImageGlobeOverlayPluginActivator



Method detail
-------------

.. py:method:: create_from_display_name(self, displayName: str) -> CustomImageGlobeOverlayPluginProxy
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivator.create_from_display_name

    Load a custom image globe overlay COM plugin associated with the specified display name and returns a proxy object that allows accessing the custom image globe overlays implemented by the plugin.

    :Parameters:

    **displayName** : :obj:`~str`

    :Returns:

        :obj:`~CustomImageGlobeOverlayPluginProxy`

.. py:method:: get_available_display_names(self) -> list
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginActivator.get_available_display_names

    Get a list of available custom image globe overlay Display Names (Programmatic Identifiers).

    :Returns:

        :obj:`~list`

