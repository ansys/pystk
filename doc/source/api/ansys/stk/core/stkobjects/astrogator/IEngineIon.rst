IEngineIon
==========

.. py:class:: IEngineIon

   object
   
   Properties for engine parameters for an Ion engine model.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~enable_control_parameter`
              - Enable the specified control parameter.
            * - :py:meth:`~disable_control_parameter`
              - Disables the specified control parameter.
            * - :py:meth:`~is_control_parameter_enabled`
              - Sees if the specified control is enabled.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~g`
            * - :py:meth:`~input_power_source_name`
            * - :py:meth:`~min_required_power`
            * - :py:meth:`~max_input_power`
            * - :py:meth:`~percent_degradation_per_year`
            * - :py:meth:`~reference_epoch`
            * - :py:meth:`~percent_throttle`
            * - :py:meth:`~engine_definition`
            * - :py:meth:`~control_parameters_available`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IEngineIon


Property detail
---------------

.. py:property:: g
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.g
    :type: float

    Gets or sets the gravitational acceleration constant at sea level on the Earth. Uses Acceleration Dimension.

.. py:property:: input_power_source_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.input_power_source_name
    :type: str

    Gets or sets the object that computes the power input to the engine.

.. py:property:: min_required_power
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.min_required_power
    :type: float

    Gets or sets the minimum power required for engine to produce thrust. Uses Power Dimension.

.. py:property:: max_input_power
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.max_input_power
    :type: float

    Gets or sets the maximum power that can be used by engine to produce thrust. Uses Power Dimension.

.. py:property:: percent_degradation_per_year
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.percent_degradation_per_year
    :type: float

    Gets or sets the degradation factor is ((1-x%/yr)^(timeSinceRefEpoch)).

.. py:property:: reference_epoch
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.reference_epoch
    :type: typing.Any

    Gets or sets the date and Time used as reference epoch for degradation. Uses DateFormat Dimension.

.. py:property:: percent_throttle
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.percent_throttle
    :type: float

    Gets or sets the percentage of available thrust to use (100 is full on, 0 is off). Dimensionless.

.. py:property:: engine_definition
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.engine_definition
    :type: IAgVAEngineDefinition

    Get the engine definition.

.. py:property:: control_parameters_available
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.control_parameters_available
    :type: bool

    Returns whether or not the control parameters can be set.


Method detail
-------------
















.. py:method:: enable_control_parameter(self, param: CONTROL_ENGINE_ION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.enable_control_parameter

    Enable the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_ION`

    :Returns:

        :obj:`~None`

.. py:method:: disable_control_parameter(self, param: CONTROL_ENGINE_ION) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.disable_control_parameter

    Disables the specified control parameter.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_ION`

    :Returns:

        :obj:`~None`

.. py:method:: is_control_parameter_enabled(self, param: CONTROL_ENGINE_ION) -> bool
    :canonical: ansys.stk.core.stkobjects.astrogator.IEngineIon.is_control_parameter_enabled

    Sees if the specified control is enabled.

    :Parameters:

    **param** : :obj:`~CONTROL_ENGINE_ION`

    :Returns:

        :obj:`~bool`


