AtmosphereModel
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.AtmosphereModel

   Class defining the atmosphere model for a mission, scenario, or procedure.

.. py:currentmodule:: AtmosphereModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.copy`
              - Copy the atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.paste`
              - Paste the atmosphere model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_type_string`
              - Get or set the atmosphere model type as a string value.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_source`
              - Get or set the atmosphere model source.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModel.mode_as_basic`
              - Get the options for a Basic Atmosphere model.



Examples
--------

Configure the weather and atmosphere of the Mission

.. code-block:: python

    # Mission mission: Aviator Mission object
    # Get the wind model used for the mission
    windModel = mission.wind_model
    # Let's use the mission model
    windModel.wind_model_source = WindAtmosphereModelSource.MISSION_MODEL
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
    atmosphere.atmosphere_model_source = WindAtmosphereModelSource.MISSION_MODEL
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
    windModel.wind_model_source = WindAtmosphereModelSource.PROCEDURE_MODEL
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
    atmosphere.atmosphere_model_source = WindAtmosphereModelSource.PROCEDURE_MODEL
    # Get the basic atmosphere options
    basicAtmosphere = atmosphere.mode_as_basic
    # Use standard 1976 atmosphere
    basicAtmosphere.basic_model_type = AtmosphereModelType.STANDARD1976


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AtmosphereModel


Property detail
---------------

.. py:property:: atmosphere_model_type_string
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_type_string
    :type: str

    Get or set the atmosphere model type as a string value.

.. py:property:: atmosphere_model_source
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.atmosphere_model_source
    :type: WindAtmosphereModelSource

    Get or set the atmosphere model source.

.. py:property:: mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.mode_as_basic
    :type: AtmosphereModelBasic

    Get the options for a Basic Atmosphere model.


Method detail
-------------






.. py:method:: copy(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.copy

    Copy the atmosphere model.

    :Returns:

        :obj:`~None`

.. py:method:: paste(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModel.paste

    Paste the atmosphere model.

    :Returns:

        :obj:`~None`

