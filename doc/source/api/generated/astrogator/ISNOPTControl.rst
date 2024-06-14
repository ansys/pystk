ISNOPTControl
=============

.. py:class:: ISNOPTControl

   object
   
   Properties for control parameters of a SNOPT profile.

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
            * - :py:meth:`~lower_bound`
            * - :py:meth:`~upper_bound`
            * - :py:meth:`~scaling_value`
            * - :py:meth:`~use_custom_display_unit`
            * - :py:meth:`~custom_display_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISNOPTControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.initial_value
    :type: typing.Any

    Get the nominal value of the element selected as a parameter. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.current_value
    :type: typing.Any

    Gets or sets the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.scaling_value
    :type: typing.Any

    Applies to the Specified Value scaling method. Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ISNOPTControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


