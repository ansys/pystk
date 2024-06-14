IBisectionControl
=================

.. py:class:: IBisectionControl

   object
   
   Properties for control parameters of a Bisection Search profile.

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
            * - :py:meth:`~initial_value`
            * - :py:meth:`~current_value`
            * - :py:meth:`~bound_search_step`
            * - :py:meth:`~use_custom_display_unit`
            * - :py:meth:`~custom_display_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBisectionControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.initial_value
    :type: typing.Any

    Get the nominal value of the element selected as a parameter. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.current_value
    :type: typing.Any

    Gets or sets the value of the independent variable after the last targeter run.

.. py:property:: bound_search_step
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.bound_search_step
    :type: typing.Any

    Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


