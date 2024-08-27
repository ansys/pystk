GridSearchControl
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GridSearchControl

   Control parameters for Grid Search profile.

.. py:currentmodule:: GridSearchControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.current_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.lower_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.upper_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.custom_display_unit`
              - Gets or sets the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GridSearchControl.step`
              - Specifies the step size to use when evaluating the grid search. Dimension depends on context.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GridSearchControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.

.. py:property:: step
    :canonical: ansys.stk.core.stkobjects.astrogator.GridSearchControl.step
    :type: typing.Any

    Specifies the step size to use when evaluating the grid search. Dimension depends on context.


