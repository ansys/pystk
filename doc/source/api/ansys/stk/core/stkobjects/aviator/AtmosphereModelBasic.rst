AtmosphereModelBasic
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic

   Class defining the basic atmosphere model.

.. py:currentmodule:: AtmosphereModelBasic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.name`
              - Get or set the name of the atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.basic_model_type`
              - Get or set the type of basic atmosphere.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.use_non_standard_atmosphere`
              - Opt whether to use non standard atmosphere conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.temperature`
              - Get or set the sea-level temperature.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.pressure`
              - Get or set the sea-level pressure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.density_altitude`
              - Get the sea-level density altitude.



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

    from ansys.stk.core.stkobjects.aviator import AtmosphereModelBasic


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.name
    :type: str

    Get or set the name of the atmosphere model.

.. py:property:: basic_model_type
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.basic_model_type
    :type: AtmosphereModelType

    Get or set the type of basic atmosphere.

.. py:property:: use_non_standard_atmosphere
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.use_non_standard_atmosphere
    :type: bool

    Opt whether to use non standard atmosphere conditions.

.. py:property:: temperature
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.temperature
    :type: float

    Get or set the sea-level temperature.

.. py:property:: pressure
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.pressure
    :type: float

    Get or set the sea-level pressure.

.. py:property:: density_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.AtmosphereModelBasic.density_altitude
    :type: float

    Get the sea-level density altitude.


