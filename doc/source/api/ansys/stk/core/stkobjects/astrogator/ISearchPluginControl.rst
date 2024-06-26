ISearchPluginControl
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl

   object
   
   Properties of search plugin control parameters.

.. py:currentmodule:: ISearchPluginControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.control_name`
              - Get the name of the control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.current_value`
              - Get the current value of the control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.parent_segment_name`
              - Get the parent segment of the control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.initial_value`
              - Get the initial value of the control parameter. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.plugin_identifier`
              - Get the plugin identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.dimension`
              - Get the dimension of the values.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.custom_display_unit`
              - Gets or sets the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.values`
              - List of values of this independent variable at each iteration, including nominal run. Dimension depends on context.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISearchPluginControl


Property detail
---------------

.. py:property:: control_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.control_name
    :type: str

    Get the name of the control parameter.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.current_value
    :type: typing.Any

    Get the current value of the control parameter.

.. py:property:: parent_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.parent_segment_name
    :type: str

    Get the parent segment of the control parameter.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.initial_value
    :type: typing.Any

    Get the initial value of the control parameter. Dimension depends on context.

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.plugin_identifier
    :type: str

    Get the plugin identifier.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.plugin_config
    :type: IPluginProperties

    Get the properties of the selected plugin.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.dimension
    :type: str

    Get the dimension of the values.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.

.. py:property:: values
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginControl.values
    :type: list

    List of values of this independent variable at each iteration, including nominal run. Dimension depends on context.


