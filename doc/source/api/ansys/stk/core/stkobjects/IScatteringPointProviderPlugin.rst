IScatteringPointProviderPlugin
==============================

.. py:class:: IScatteringPointProviderPlugin

   object
   
   Provide access to the properties and methods defining a plugin scattering point provider.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~plugin_configuration`
            * - :py:meth:`~raw_plugin_object`
            * - :py:meth:`~scattering_point_model`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointProviderPlugin


Property detail
---------------

.. py:property:: plugin_configuration
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderPlugin.plugin_configuration
    :type: "IAgCRPluginConfiguration"

    Gets the plugin configuration interface.

.. py:property:: raw_plugin_object
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderPlugin.raw_plugin_object
    :type: typing.Any

    Gets the raw plugin IUnknown interface.

.. py:property:: scattering_point_model
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderPlugin.scattering_point_model
    :type: "IAgComponentLinkEmbedControl"

    Gets the link/embed controller for managing the default scattering point model component.


