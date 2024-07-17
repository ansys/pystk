EOMFuncPluginFunction
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   EOM Function Plugin propagator function.

.. py:currentmodule:: EOMFuncPluginFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction.plugin_identifier`
              - Gets or sets the plugin name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction.plugin_config`
              - Get the properties of the selected plugin.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EOMFuncPluginFunction


Property detail
---------------

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction.plugin_identifier
    :type: str

    Gets or sets the plugin name.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.EOMFuncPluginFunction.plugin_config
    :type: IPluginProperties

    Get the properties of the selected plugin.


