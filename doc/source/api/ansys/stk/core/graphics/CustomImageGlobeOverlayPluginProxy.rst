CustomImageGlobeOverlayPluginProxy
==================================

.. py:class:: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy

   A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

.. py:currentmodule:: CustomImageGlobeOverlayPluginProxy

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy.custom_image_globe_overlay`
              - Returns a custom image globe overlay.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy.is_custom_image_globe_overlay_supported`
              - Returns true if custom image globe overlays are supported.
            * - :py:attr:`~ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy.real_plugin_object`
              - Returns a pointer to plugin object's IUnknown interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CustomImageGlobeOverlayPluginProxy


Property detail
---------------

.. py:property:: custom_image_globe_overlay
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy.custom_image_globe_overlay
    :type: CustomImageGlobeOverlay

    Returns a custom image globe overlay.

.. py:property:: is_custom_image_globe_overlay_supported
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy.is_custom_image_globe_overlay_supported
    :type: bool

    Returns true if custom image globe overlays are supported.

.. py:property:: real_plugin_object
    :canonical: ansys.stk.core.graphics.CustomImageGlobeOverlayPluginProxy.real_plugin_object
    :type: typing.Any

    Returns a pointer to plugin object's IUnknown interface.


