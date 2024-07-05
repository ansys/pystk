IScatteringPointModelPlugin
===========================

.. py:class:: ansys.stk.core.stkobjects.IScatteringPointModelPlugin

   object
   
   Provide access to the properties and methods defining a plugin scattering point model.

.. py:currentmodule:: IScatteringPointModelPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointModelPlugin.plugin_configuration`
              - Gets the plugin configuration interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointModelPlugin.raw_plugin_object`
              - Gets the raw plugin IUnknown interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointModelPlugin


Property detail
---------------

.. py:property:: plugin_configuration
    :canonical: ansys.stk.core.stkobjects.IScatteringPointModelPlugin.plugin_configuration
    :type: ICRPluginConfiguration

    Gets the plugin configuration interface.

.. py:property:: raw_plugin_object
    :canonical: ansys.stk.core.stkobjects.IScatteringPointModelPlugin.raw_plugin_object
    :type: typing.Any

    Gets the raw plugin IUnknown interface.


