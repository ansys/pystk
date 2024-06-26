IEngineThrottleTable
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable

   object
   
   Properties for engine parameters for a Throttle Table engine model.

.. py:currentmodule:: IEngineThrottleTable

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.throttle_table_filename`
              - A file containing the engine performance data in the tabular format.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.operation_mode_definition`
              - The engine operation mode definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.regression_polynomial_degree`
              - The degree of the regression polynomial. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.g`
              - The gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.input_power_source_name`
              - The object that computes the power input to the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.percent_degradation_per_year`
              - The degradation factor is ((1-x%/yr)^(timeSinceRefEpoch)).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.reference_epoch`
              - The date and Time used as reference epoch for degradation. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.control_parameters_available`
              - Returns whether or not the control parameters can be set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineThrottleTable


Property detail
---------------

.. py:property:: throttle_table_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.throttle_table_filename
    :type: str

    A file containing the engine performance data in the tabular format.

.. py:property:: operation_mode_definition
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.operation_mode_definition
    :type: THROTTLE_TABLE_OPERATION_MODE

    The engine operation mode definition.

.. py:property:: regression_polynomial_degree
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.regression_polynomial_degree
    :type: int

    The degree of the regression polynomial. Dimensionless.

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.g
    :type: float

    The gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.input_power_source_name
    :type: str

    The object that computes the power input to the engine.

.. py:property:: percent_degradation_per_year
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.percent_degradation_per_year
    :type: float

    The degradation factor is ((1-x%/yr)^(timeSinceRefEpoch)).

.. py:property:: reference_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.reference_epoch
    :type: typing.Any

    The date and Time used as reference epoch for degradation. Uses DateFormat Dimension.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------















.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_THROTTLE_TABLE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_THROTTLE_TABLE`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_THROTTLE_TABLE) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_THROTTLE_TABLE`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_THROTTLE_TABLE) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineThrottleTable.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_THROTTLE_TABLE`

    :Returns:

        :obj:`~bool`


