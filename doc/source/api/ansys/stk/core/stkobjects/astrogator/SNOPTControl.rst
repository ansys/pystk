SNOPTControl
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.SNOPTControl

   Bases: 

   Control parameters for SNOPT optimizer profile.

.. py:currentmodule:: SNOPTControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.initial_value`
              - Get the nominal value of the element selected as a parameter. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.current_value`
              - Gets or sets the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.lower_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.upper_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.scaling_value`
              - Applies to the Specified Value scaling method. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTControl.custom_display_unit`
              - Gets or sets the unit in which the value will be displayed in the GUI.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SNOPTControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.initial_value
    :type: typing.Any

    Get the nominal value of the element selected as a parameter. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.current_value
    :type: typing.Any

    Gets or sets the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.scaling_value
    :type: typing.Any

    Applies to the Specified Value scaling method. Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


