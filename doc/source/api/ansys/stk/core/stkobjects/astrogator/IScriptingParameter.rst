IScriptingParameter
===================

.. py:class:: IScriptingParameter

   object
   
   Parameter properties for scripting options.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~param_value`
            * - :py:meth:`~unit`
            * - :py:meth:`~type`
            * - :py:meth:`~inherit_value`
            * - :py:meth:`~user_comment`
            * - :py:meth:`~dimension`
            * - :py:meth:`~enumeration_choices`
            * - :py:meth:`~use_min_value`
            * - :py:meth:`~min_value`
            * - :py:meth:`~use_max_value`
            * - :py:meth:`~max_value`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IScriptingParameter


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.name
    :type: str

    Gets or sets the parameter name.

.. py:property:: param_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.param_value
    :type: typing.Any

    Gets or sets the parameter value.  Set in Object Model unit preference for selected dimension.

.. py:property:: unit
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.unit
    :type: str

    Gets or sets the parameter's unit that is used to represent ParamValue during the scripting tool script execution. ParamValue is set in Object Model unit preference for selected dimension and not this unit. As with other units configurable in the desktop environment for STK, this unit is separate (and may differ) from the Object Model unit preference.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.type
    :type: "SCRIPTING_PARAMETER_TYPE"

    Gets or sets the parameter's type.

.. py:property:: inherit_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.inherit_value
    :type: bool

    If true, parameter value will be inherited from previous profile's value.

.. py:property:: user_comment
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.user_comment
    :type: str

    Gets or sets the parameter's comment.

.. py:property:: dimension
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.dimension
    :type: str

    Gets or sets the parameter's dimension.

.. py:property:: enumeration_choices
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.enumeration_choices
    :type: "IAgVAScriptingParameterEnumerationChoiceCollection"

    Get the collection of enumerations to use when parameter type is eVAScriptingParameterTypeEnumeration.

.. py:property:: use_min_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.use_min_value
    :type: bool

    If true, a minimum value will be enforced for the parameter value.

.. py:property:: min_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.min_value
    :type: typing.Any

    Gets or sets the minimum value permitted for the parameter value.

.. py:property:: use_max_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.use_max_value
    :type: bool

    If true, a maximum value will be enforced for the parameter value.

.. py:property:: max_value
    :canonical: ansys.stk.core.stkobjects.astrogator.IScriptingParameter.max_value
    :type: typing.Any

    Gets or sets the maximum value permitted for the parameter value.


