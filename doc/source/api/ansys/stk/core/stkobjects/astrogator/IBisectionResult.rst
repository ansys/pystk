IBisectionResult
================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IBisectionResult

   object
   
   Properties for result parameters of a Bisection profile.

.. py:currentmodule:: IBisectionResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.current_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.desired_value`
              - Gets or sets the value that you want to achieve.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.tolerance`
              - Gets or sets the profile will stop when it achieves a value within this range of the Desired Value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IBisectionResult.custom_display_unit`
              - Gets or sets the unit in which the value will be displayed in the GUI.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBisectionResult


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: desired_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.desired_value
    :type: typing.Any

    Gets or sets the value that you want to achieve.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.tolerance
    :type: typing.Any

    Gets or sets the profile will stop when it achieves a value within this range of the Desired Value.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResult.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


