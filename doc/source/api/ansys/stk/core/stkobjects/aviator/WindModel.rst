WindModel
=========

.. py:class:: ansys.stk.core.stkobjects.aviator.WindModel

   Class defining the wind model for a mission, scenario, or procedure.

.. py:currentmodule:: WindModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.copy`
              - Copy the wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.paste`
              - Paste the wind model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type`
              - Get or set the wind model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type_string`
              - Get or set the wind model type as a string value. Use this for custom models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.wind_model_source`
              - Get or set the wind model source.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.mode_as_constant`
              - Get the options for a Constant Bearing/Speed wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModel.mode_as_adds`
              - Get the options for a NOAA ADDS Service wind model.



Examples
--------

Configure the weather and atmosphere of the Mission

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the wind model used for the mission
    windModel = mission.wind_model
    # Let's use the mission model
    windModel.wind_model_source = WindAtmosModelSource.MISSION_MODEL
    # Let's use constant wind
    windModel.wind_model_type = WindModelType.CONSTANT_WIND
    # Get the constant wind model options
    constantWind = windModel.mode_as_constant
    # Set the wind bearing
    constantWind.wind_bearing = 30
    # Set the wind speed
    constantWind.wind_speed = 5

    # Get the atmosphere model used for the mission
    atmosphere = mission.atmosphere_model
    # Let's use the mission model
    atmosphere.atmosphere_model_source = WindAtmosModelSource.MISSION_MODEL
    # Get the basic atmosphere options
    basicAtmosphere = atmosphere.mode_as_basic
    # Use standard 1976 atmosphere
    basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976
    # Opt to override the values
    basicAtmosphere.use_non_standard_atmosphere = True
    # Override the temperature
    basicAtmosphere.temperature = 290


Configure the wind and atmosphere for a procedure

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Get the wind model for the procedure
    windModel = procedure.wind_model
    # Use the procedure model
    windModel.wind_model_source = WindAtmosModelSource.PROCEDURE_MODEL
    # Let's use constant wind
    windModel.wind_model_type = WindModelType.CONSTANT_WIND
    # Get the constant wind model options
    constantWind = windModel.mode_as_constant
    # Set the wind bearing
    constantWind.wind_bearing = 30
    # Set the wind speed
    constantWind.wind_speed = 5

    # Get the atmosphere model used for the procedure
    atmosphere = procedure.atmosphere_model
    # Let's use the procedure model
    atmosphere.atmosphere_model_source = WindAtmosModelSource.PROCEDURE_MODEL
    # Get the basic atmosphere options
    basicAtmosphere = atmosphere.mode_as_basic
    # Use standard 1976 atmosphere
    basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import WindModel


Property detail
---------------

.. py:property:: wind_model_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type
    :type: WindModelType

    Get or set the wind model type.

.. py:property:: wind_model_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.wind_model_type_string
    :type: str

    Get or set the wind model type as a string value. Use this for custom models.

.. py:property:: wind_model_source
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.wind_model_source
    :type: WindAtmosModelSource

    Get or set the wind model source.

.. py:property:: mode_as_constant
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.mode_as_constant
    :type: WindModelConstant

    Get the options for a Constant Bearing/Speed wind model.

.. py:property:: mode_as_adds
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.mode_as_adds
    :type: WindModelADDS

    Get the options for a NOAA ADDS Service wind model.


Method detail
-------------









.. py:method:: copy(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.copy

    Copy the wind model.

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.WindModel.paste

    Paste the wind model.

    :Returns:

        :obj:`~None`

