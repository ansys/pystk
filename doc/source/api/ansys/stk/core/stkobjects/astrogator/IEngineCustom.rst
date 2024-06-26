IEngineCustom
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.IEngineCustom

   object
   
   Properties for a Custom engine model.

.. py:currentmodule:: IEngineCustom

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.g`
              - Gets or sets the earth surface gravity acceleration for Isp conversions. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.eval_function_name`
              - Gets or sets the EvalFunction - custom function to call at every thrust evaluation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.post_function_name`
              - Gets or sets the PostFunction - custom function to call after all propagation ends.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.pre_function_name`
              - Gets or sets the PreFunction - custom function to call before any propagation begins.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.seg_start_function_name`
              - Gets or sets the SegStartFunction - custom function to call at the beginning of each segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.update_function_name`
              - Gets or sets the UpdateFunction - custom function to call at the beginning of each integration step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineCustom.control_parameters_available`
              - Returns whether or not the control parameters can be set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineCustom


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.g
    :type: float

    Gets or sets the earth surface gravity acceleration for Isp conversions. Uses Acceleration Dimension.

.. py:property:: eval_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.eval_function_name
    :type: str

    Gets or sets the EvalFunction - custom function to call at every thrust evaluation.

.. py:property:: post_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.post_function_name
    :type: str

    Gets or sets the PostFunction - custom function to call after all propagation ends.

.. py:property:: pre_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.pre_function_name
    :type: str

    Gets or sets the PreFunction - custom function to call before any propagation begins.

.. py:property:: seg_start_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.seg_start_function_name
    :type: str

    Gets or sets the SegStartFunction - custom function to call at the beginning of each segment.

.. py:property:: update_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.update_function_name
    :type: str

    Gets or sets the UpdateFunction - custom function to call at the beginning of each integration step.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------













.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_CUSTOM) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CUSTOM`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_CUSTOM) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CUSTOM`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_CUSTOM) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineCustom.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_CUSTOM`

    :Returns:

        :obj:`~bool`


