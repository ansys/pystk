IGoldenSectionControl
=====================

.. py:class:: IGoldenSectionControl

   object
   
   Properties for control parameters of a Golden Section profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable`
            * - :py:meth:`~name`
            * - :py:meth:`~parent_name`
            * - :py:meth:`~current_value`
            * - :py:meth:`~lower_bound`
            * - :py:meth:`~upper_bound`
            * - :py:meth:`~use_custom_display_unit`
            * - :py:meth:`~custom_display_unit`
            * - :py:meth:`~tolerance`


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


