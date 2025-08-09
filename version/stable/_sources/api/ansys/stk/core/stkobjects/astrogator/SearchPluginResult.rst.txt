SearchPluginResult
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SearchPluginResult

   Equality constraints for a plugin search profile.

.. py:currentmodule:: SearchPluginResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.result_name`
              - Get the name of the equality constraint.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.current_value`
              - Get the current value of the result variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.parent_segment_name`
              - Get the parent segment of the result variable.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.plugin_identifier`
              - Get the plugin identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.dimension`
              - Get the dimension of the values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResult.values`
              - List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SearchPluginResult


Property detail
---------------

.. py:property:: result_name
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.result_name
    :type: str

    Get the name of the equality constraint.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.current_value
    :type: typing.Any

    Get the current value of the result variable.

.. py:property:: parent_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.parent_segment_name
    :type: str

    Get the parent segment of the result variable.

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.plugin_identifier
    :type: str

    Get the plugin identifier.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.plugin_config
    :type: PluginProperties

    Get the properties of the selected plugin.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.dimension
    :type: str

    Get the dimension of the values.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.

.. py:property:: values
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResult.values
    :type: list

    List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.


