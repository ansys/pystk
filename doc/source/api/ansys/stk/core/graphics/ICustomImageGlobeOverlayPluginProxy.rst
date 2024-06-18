ICustomImageGlobeOverlayPluginProxy
===================================

.. py:class:: ICustomImageGlobeOverlayPluginProxy

   object
   
   A proxy class provides access to a custom image globe overlay implemented by a plugin. Proxies are instantiated using custom image globe overlay plugin activator.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~custom_image_globe_overlay`
            * - :py:meth:`~is_custom_image_globe_overlay_supported`
            * - :py:meth:`~real_plugin_object`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICustomImageGlobeOverlayPluginProxy


Property detail
---------------

.. py:property:: custom_image_globe_overlay
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlayPluginProxy.custom_image_globe_overlay
    :type: "IAgStkGraphicsCustomImageGlobeOverlay"

    Returns a custom image globe overlay.

.. py:property:: is_custom_image_globe_overlay_supported
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlayPluginProxy.is_custom_image_globe_overlay_supported
    :type: bool

    Returns true if custom image globe overlays are supported.

.. py:property:: real_plugin_object
    :canonical: ansys.stk.core.graphics.ICustomImageGlobeOverlayPluginProxy.real_plugin_object
    :type: typing.Any

    Returns a pointer to plugin object's IUnknown interface.


