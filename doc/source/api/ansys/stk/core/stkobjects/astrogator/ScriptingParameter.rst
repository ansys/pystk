ScriptingParameter
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ScriptingParameter

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Scripting Parameter.

.. py:currentmodule:: ScriptingParameter

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.name`
              - Gets or sets the parameter name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.parameter_value`
              - Gets or sets the parameter value.  Set in Object Model unit preference for selected dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.unit`
              - Gets or sets the parameter's unit that is used to represent ParamValue during the scripting tool script execution. ParamValue is set in Object Model unit preference for selected dimension and not this unit. As with other units configurable in the desktop environment for STK, this unit is separate (and may differ) from the Object Model unit preference.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.type`
              - Gets or sets the parameter's type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.inherit_value`
              - If true, parameter value will be inherited from previous profile's value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.user_comment`
              - Gets or sets the parameter's comment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.dimension`
              - Gets or sets the parameter's dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.enumeration_choices`
              - Get the collection of enumerations to use when parameter type is eVAScriptingParameterTypeEnumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.use_min_value`
              - If true, a minimum value will be enforced for the parameter value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.min_value`
              - Gets or sets the minimum value permitted for the parameter value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.use_max_value`
              - If true, a maximum value will be enforced for the parameter value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ScriptingParameter.max_value`
              - Gets or sets the maximum value permitted for the parameter value.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ScriptingParameter


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.name
    :type: str

    Gets or sets the parameter name.

.. py:property:: parameter_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.parameter_value
    :type: typing.Any

    Gets or sets the parameter value.  Set in Object Model unit preference for selected dimension.

.. py:property:: unit
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.unit
    :type: str

    Gets or sets the parameter's unit that is used to represent ParamValue during the scripting tool script execution. ParamValue is set in Object Model unit preference for selected dimension and not this unit. As with other units configurable in the desktop environment for STK, this unit is separate (and may differ) from the Object Model unit preference.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.type
    :type: SCRIPTING_PARAMETER_TYPE

    Gets or sets the parameter's type.

.. py:property:: inherit_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.inherit_value
    :type: bool

    If true, parameter value will be inherited from previous profile's value.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.user_comment
    :type: str

    Gets or sets the parameter's comment.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.dimension
    :type: str

    Gets or sets the parameter's dimension.

.. py:property:: enumeration_choices
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.enumeration_choices
    :type: ScriptingParameterEnumerationChoiceCollection

    Get the collection of enumerations to use when parameter type is eVAScriptingParameterTypeEnumeration.

.. py:property:: use_min_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.use_min_value
    :type: bool

    If true, a minimum value will be enforced for the parameter value.

.. py:property:: min_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.min_value
    :type: typing.Any

    Gets or sets the minimum value permitted for the parameter value.

.. py:property:: use_max_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.use_max_value
    :type: bool

    If true, a maximum value will be enforced for the parameter value.

.. py:property:: max_value
    :canonical: ansys.stk.core.stkobjects.astrogator.ScriptingParameter.max_value
    :type: typing.Any

    Gets or sets the maximum value permitted for the parameter value.


