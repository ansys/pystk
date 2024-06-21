IEnginePlugin
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IEnginePlugin

   object
   
   Properties for a Plugin engine model.

.. py:currentmodule:: IEnginePlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEnginePlugin.g`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEnginePlugin.plugin_identifier`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEnginePlugin.plugin_config`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEnginePlugin


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEnginePlugin.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.IEnginePlugin.plugin_identifier
    :type: str

    Gets or sets the PluginIdentifier - the ProgID of the COM component you are using for this model.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.IEnginePlugin.plugin_config
    :type: IPluginProperties

    Get the properties of the plugin.


