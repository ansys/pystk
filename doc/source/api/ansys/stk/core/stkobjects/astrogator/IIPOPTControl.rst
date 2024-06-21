IIPOPTControl
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IIPOPTControl

   object
   
   Properties for control parameters of a IPOPT profile.

.. py:currentmodule:: IIPOPTControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.enable`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.parent_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.initial_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.current_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.lower_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.upper_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.scaling_value`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.use_custom_display_unit`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IIPOPTControl.custom_display_unit`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IIPOPTControl


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.enable
    :type: bool

    If true, the variable is being used.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.name
    :type: str

    Get the name of the parameter.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.parent_name
    :type: str

    Get the name of the segment to which the parameter belongs.

.. py:property:: initial_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.initial_value
    :type: typing.Any

    Get the nominal value of the element selected as a parameter. Dimension depends on context.

.. py:property:: current_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.current_value
    :type: typing.Any

    Gets or sets the value of the independent variable after the last targeter run.

.. py:property:: lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.lower_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.upper_bound
    :type: typing.Any

    Dimension depends on context.

.. py:property:: scaling_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.scaling_value
    :type: typing.Any

    Applies to the Specified Value scaling method. Dimension depends on context.

.. py:property:: use_custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.use_custom_display_unit
    :type: bool

    If true, allows display of values in another unit.

.. py:property:: custom_display_unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IIPOPTControl.custom_display_unit
    :type: str

    Gets or sets the unit in which the value will be displayed in the GUI.


