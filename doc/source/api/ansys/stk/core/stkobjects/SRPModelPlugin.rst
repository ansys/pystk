SRPModelPlugin
==============

.. py:class:: ansys.stk.core.stkobjects.SRPModelPlugin

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISRPModelBase`

   Plugin Light Reflection Model.

.. py:currentmodule:: SRPModelPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SRPModelPlugin.plugin_name`
              - Gets or sets the complete name of the plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.SRPModelPlugin.plugin_settings`
              - Get the parameters of the selected plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.SRPModelPlugin.available_plugins`
              - Get the list of all the available plugins.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SRPModelPlugin


Property detail
---------------

.. py:property:: plugin_name
    :canonical: ansys.stk.core.stkobjects.SRPModelPlugin.plugin_name
    :type: str

    Gets or sets the complete name of the plugin.

.. py:property:: plugin_settings
    :canonical: ansys.stk.core.stkobjects.SRPModelPlugin.plugin_settings
    :type: ISRPModelPluginSettings

    Get the parameters of the selected plugin.

.. py:property:: available_plugins
    :canonical: ansys.stk.core.stkobjects.SRPModelPlugin.available_plugins
    :type: list

    Get the list of all the available plugins.


