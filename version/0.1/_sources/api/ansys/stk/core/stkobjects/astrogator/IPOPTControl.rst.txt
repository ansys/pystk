IPOPTControl
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPOPTControl

   Control parameters for IPOPT optimizer profile.

.. py:currentmodule:: IPOPTControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.initial_value`
              - Get the nominal value of the element selected as a parameter. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.current_value`
              - Get or set the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.lower_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.upper_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.scaling_value`
              - Apply to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTControl.custom_display_unit`
              - Get or set the unit in which the value will be displayed in the GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPOPTControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.initial_value
    :type: typing.Any

    Get the nominal value of the element selected as a parameter. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.current_value
    :type: typing.Any

    Get or set the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.scaling_value
    :type: typing.Any

    Apply to the Specified Value scaling method. Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTControl.custom_display_unit
    :type: str

    Get or set the unit in which the value will be displayed in the GUI.


