EngineIon
=========

.. py:class:: ansys.stk.core.stkobjects.astrogator.EngineIon

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Ion Engine engine model.

.. py:currentmodule:: EngineIon

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.g`
              - Get or set the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.input_power_source_name`
              - Get or set the object that computes the power input to the engine.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.min_required_power`
              - Get or set the minimum power required for engine to produce thrust. Uses Power Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.max_input_power`
              - Get or set the maximum power that can be used by engine to produce thrust. Uses Power Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.percent_degradation_per_year`
              - Get or set the degradation factor is ((1-x%/yr)^(timeSinceRefEpoch)).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.reference_epoch`
              - Get or set the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.percent_throttle`
              - Get or set the percentage of available thrust to use (100 is full on, 0 is off). Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.engine_definition`
              - Get the engine definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.EngineIon.control_parameters_available`
              - Return whether or not the control parameters can be set.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import EngineIon


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.g
    :type: float

    Get or set the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.input_power_source_name
    :type: str

    Get or set the object that computes the power input to the engine.

.. py:property:: min_required_power
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.min_required_power
    :type: float

    Get or set the minimum power required for engine to produce thrust. Uses Power Dimension.

.. py:property:: max_input_power
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.max_input_power
    :type: float

    Get or set the maximum power that can be used by engine to produce thrust. Uses Power Dimension.

.. py:property:: percent_degradation_per_year
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.percent_degradation_per_year
    :type: float

    Get or set the degradation factor is ((1-x%/yr)^(timeSinceRefEpoch)).

.. py:property:: reference_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.reference_epoch
    :type: typing.Any

    Get or set the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.

.. py:property:: percent_throttle
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.percent_throttle
    :type: float

    Get or set the percentage of available thrust to use (100 is full on, 0 is off). Dimensionless.

.. py:property:: engine_definition
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.engine_definition
    :type: EngineDefinition

    Get the engine definition.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.control_parameters_available
    :type: bool

    Return whether or not the control parameters can be set.


Method detail
-------------
















.. py:method:: enable_control_parameter(self, param: ControlEngineIon) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlEngineIon`


    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: ControlEngineIon) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

        **param** : :obj:`~ControlEngineIon`


    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: ControlEngineIon) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.EngineIon.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

        **param** : :obj:`~ControlEngineIon`


    :Returns:

        :obj:`~bool`


