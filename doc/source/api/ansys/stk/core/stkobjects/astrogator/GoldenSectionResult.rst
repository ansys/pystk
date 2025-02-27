GoldenSectionResult
===================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult

   Result parameters for Golden Section profile.

.. py:currentmodule:: GoldenSectionResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.current_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.desired_operation`
              - Get or set the Desired Operation/Objective of golden section.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GoldenSectionResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: desired_operation
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.desired_operation
    :type: GoldenSectionDesiredOperation

    Get or set the Desired Operation/Objective of golden section.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResult.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.


