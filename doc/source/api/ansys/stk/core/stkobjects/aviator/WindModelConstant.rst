WindModelConstant
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.WindModelConstant

   Class defining a constant bearing/speed wind model for a mission.

.. py:currentmodule:: WindModelConstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelConstant.blend_time`
              - Get or set the blend time to transition from the previous wind model if one exists.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelConstant.name`
              - Get or set the name of the wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelConstant.wind_bearing`
              - Get or set the wind's true bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelConstant.wind_speed`
              - Get or set the constant wind speed.



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

    from ansys.stk.core.stkobjects.aviator import WindModelConstant


Property detail
---------------

.. py:property:: blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelConstant.blend_time
    :type: float

    Get or set the blend time to transition from the previous wind model if one exists.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelConstant.name
    :type: str

    Get or set the name of the wind model.

.. py:property:: wind_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelConstant.wind_bearing
    :type: typing.Any

    Get or set the wind's true bearing.

.. py:property:: wind_speed
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelConstant.wind_speed
    :type: float

    Get or set the constant wind speed.


