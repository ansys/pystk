IGridSearchControl
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IGridSearchControl

   object
   
   Properties for control parameters of a Grid Search profile.

.. py:currentmodule:: IGridSearchControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.enable`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.parent_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.current_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.lower_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.upper_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.use_custom_display_unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.custom_display_unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControl.step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGridSearchControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControl.step
    :type: typing.Any

    Specifies the step size to use when evaluating the grid search. Dimension depends on context.


