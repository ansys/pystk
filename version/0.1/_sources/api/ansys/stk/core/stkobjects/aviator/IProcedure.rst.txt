IProcedure
==========

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedure

   Interface used to access the options for a procedure. Use this interface to get the Site and Get the time options for the current procedure.

.. py:currentmodule:: IProcedure

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.name`
              - Get or set the name of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.site`
              - Get the site of the current procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.time_options`
              - Get the time options for the current procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.wind_model`
              - Get the wind model for the current procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.atmosphere_model`
              - Get the mission atmosphere model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.calculation_options`
              - Get the calculation options for the current procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_is_supported`
              - Refuel/dump is supported for the current procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_properties`
              - Get the refuel/dump properties for the current procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedure.fast_time_options`
              - Get the fast time options (without validation or constraints) for the current procedure.


Examples
--------

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


Configure a procedure's time options

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Get the time in epoch seconds
    root.units_preferences.set_current_unit("DateFormat", "EpSec")
    # Get the time options
    timeOptions = procedure.time_options
    # Get the start time
    startTime = timeOptions.start_time
    # Set the procedure to interrupt after 15 seconds
    timeOptions.set_interrupt_time(15)


Rename a procedure and its site

.. code-block:: python

    # IProcedure procedure: Procedure object
    # Rename the procedure
    procedure.name = "New Procedure"
    # Get the site corresponding to the procedure
    site = procedure.site
    # Rename the site
    site.name = "New Site"


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedure


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.name
    :type: str

    Get or set the name of the procedure.

.. py:property:: site
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.site
    :type: ISite

    Get the site of the current procedure.

.. py:property:: time_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.time_options
    :type: ProcedureTimeOptions

    Get the time options for the current procedure.

.. py:property:: wind_model
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.wind_model
    :type: WindModel

    Get the wind model for the current procedure.

.. py:property:: atmosphere_model
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.atmosphere_model
    :type: AtmosphereModel

    Get the mission atmosphere model.

.. py:property:: calculation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.calculation_options
    :type: CalculationOptions

    Get the calculation options for the current procedure.

.. py:property:: refuel_dump_is_supported
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_is_supported
    :type: bool

    Refuel/dump is supported for the current procedure.

.. py:property:: refuel_dump_properties
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.refuel_dump_properties
    :type: RefuelDumpProperties

    Get the refuel/dump properties for the current procedure.

.. py:property:: fast_time_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedure.fast_time_options
    :type: ProcedureFastTimeOptions

    Get the fast time options (without validation or constraints) for the current procedure.


