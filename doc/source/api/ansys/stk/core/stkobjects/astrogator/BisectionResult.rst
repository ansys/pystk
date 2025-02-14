BisectionResult
===============

.. py:class:: ansys.stk.core.stkobjects.astrogator.BisectionResult

   Result parameters for Bisection profile.

.. py:currentmodule:: BisectionResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.current_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.desired_value`
              - Get or set the value that you want to achieve.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.tolerance`
              - Get or set the profile will stop when it achieves a value within this range of the Desired Value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResult.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BisectionResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.desired_value
    :type: typing.Any

    Get or set the value that you want to achieve.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.tolerance
    :type: typing.Any

    Get or set the profile will stop when it achieves a value within this range of the Desired Value.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResult.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.


