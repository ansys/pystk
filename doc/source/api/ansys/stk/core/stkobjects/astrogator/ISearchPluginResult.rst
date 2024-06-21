ISearchPluginResult
===================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult

   object
   
   Properties of search plugin equality constraints.

.. py:currentmodule:: ISearchPluginResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.result_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.current_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.parent_segment_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.plugin_identifier`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.plugin_config`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.dimension`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.use_custom_display_unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.custom_display_unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.values`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISearchPluginResult


Property detail
---------------

.. py:property:: result_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.result_name
    :type: str

    Get the name of the equality constraint.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.current_value
    :type: typing.Any

    Get the current value of the result variable.

.. py:property:: parent_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.parent_segment_name
    :type: str

    Get the parent segment of the result variable.

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.plugin_identifier
    :type: str

    Get the plugin identifier.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.plugin_config
    :type: IPluginProperties

    Get the properties of the selected plugin.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.dimension
    :type: str

    Get the dimension of the values.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.

.. py:property:: values
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResult.values
    :type: list

    List of values of this dependent variable at each iteration, including nominal run. Dimension depends on context.


