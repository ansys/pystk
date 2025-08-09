GoldenSectionControl
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl

   Control parameters for Golden Section profile.

.. py:currentmodule:: GoldenSectionControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.current_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.lower_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.tolerance`
              - How close the targeter should come to the desired. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.upper_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.use_custom_display_unit`
              - If true, allows display of values in another unit.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GoldenSectionControl


Property detail
---------------

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.tolerance
    :type: typing.Any

    How close the targeter should come to the desired. Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.


