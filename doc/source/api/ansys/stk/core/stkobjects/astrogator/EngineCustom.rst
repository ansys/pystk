EngineCustom
============

.. py:class:: ansys.stk.core.stkobjects.astrogator.EngineCustom

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Custom engine model.

.. py:currentmodule:: EngineCustom

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.g`
              - Get or set the earth surface gravity acceleration for Isp conversions. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.eval_function_name`
              - Get or set the EvalFunction - custom function to call at every thrust evaluation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.post_function_name`
              - Get or set the PostFunction - custom function to call after all propagation ends.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.pre_function_name`
              - Get or set the PreFunction - custom function to call before any propagation begins.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.seg_start_function_name`
              - Get or set the SegStartFunction - custom function to call at the beginning of each segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.update_function_name`
              - Get or set the UpdateFunction - custom function to call at the beginning of each integration step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineCustom.control_parameters_available`
              - Return whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EngineCustom


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.g
    :type: float

    Get or set the earth surface gravity acceleration for Isp conversions. Uses Acceleration Dimension.

.. py:property:: eval_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.eval_function_name
    :type: str

    Get or set the EvalFunction - custom function to call at every thrust evaluation.

.. py:property:: post_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.post_function_name
    :type: str

    Get or set the PostFunction - custom function to call after all propagation ends.

.. py:property:: pre_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.pre_function_name
    :type: str

    Get or set the PreFunction - custom function to call before any propagation begins.

.. py:property:: seg_start_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.seg_start_function_name
    :type: str

    Get or set the SegStartFunction - custom function to call at the beginning of each segment.

.. py:property:: update_function_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.update_function_name
    :type: str

    Get or set the UpdateFunction - custom function to call at the beginning of each integration step.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.


Method detail
-------------













.. py:method:: enable_control_parameter(self, param: ControlEngineCustom) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlEngineCustom`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlEngineCustom) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~ControlEngineCustom`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlEngineCustom) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineCustom.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~ControlEngineCustom`

    :Returns:

        :obj:`~bool`


