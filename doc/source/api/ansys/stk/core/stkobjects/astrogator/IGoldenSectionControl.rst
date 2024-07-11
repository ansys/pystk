IGoldenSectionControl
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl

   object
   
   Properties for control parameters of a Golden Section profile.

.. py:currentmodule:: IGoldenSectionControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.enable`
              - If true, the variable is being used.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.name`
              - Get the name of the parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.parent_name`
              - Get the name of the segment to which the parameter belongs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.current_value`
              - Get the value of the independent variable after the last targeter run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.lower_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.upper_bound`
              - Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.use_custom_display_unit`
              - If true, allows display of values in another unit.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.custom_display_unit`
              - Gets or sets the unit in which the value will be displayed in the GUI.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.tolerance`
              - How close the targeter should come to the desired. Dimension depends on context.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGoldenSectionControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.current_value
    :type: typing.Any

    Get the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.

.. py:property:: tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IGoldenSectionControl.tolerance
    :type: typing.Any

    How close the targeter should come to the desired. Dimension depends on context.


