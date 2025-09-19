Catalog
=======

.. py:class:: ansys.stk.core.stkobjects.aviator.Catalog

   Class defining the Aviator Catalog.

.. py:currentmodule:: Catalog

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Catalog.aircraft_category`
              - Get the aircraft category.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Catalog.airport_category`
              - Get the airport category.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Catalog.navaid_category`
              - Get the navaid category.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Catalog.runway_category`
              - Get the runway category.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Catalog.vtol_point_category`
              - Get the vtol point category.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Catalog.waypoint_category`
              - Get the waypoint category.



Examples
--------

Set the aircraft used for the mission to an aircraft found in the Aviator catalog

.. code-block:: python

    # AviatorPropagator propagator: Aviator Propagator object
    # Get the Aviator catalog
    catalog = propagator.aviator_catalog
    # Get the aircraft category
    category = catalog.aircraft_category
    # Get the user aircraft models
    aircraftModels = category.aircraft_models
    # Get the basic fighter
    fighter = aircraftModels.get_aircraft("Basic Fighter")
    # Get the mission
    mission = propagator.aviator_mission
    # Set the vehicle used for the mission
    mission.vehicle = fighter


Configure a runway site from a runway in the Aviator catalog

.. code-block:: python

    # SiteRunway runway: Runway object
    # Catalog catalog: Aviator catalog object
    # Get the source of user runways
    userRunways = catalog.runway_category.user_runways
    # Check that the runway exists in the catalog
    if userRunways.contains("New User Runway") is True:
        # If so, get the user runway with the given name
        runwayFromCatalog = userRunways.get_user_runway("New User Runway")
        # Copy the parameters of that runway
        runway.copy_from_catalog(runwayFromCatalog)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import Catalog


Property detail
---------------

.. py:property:: aircraft_category
    :canonical: ansys.stk.core.stkobjects.aviator.Catalog.aircraft_category
    :type: AircraftCategory

    Get the aircraft category.

.. py:property:: airport_category
    :canonical: ansys.stk.core.stkobjects.aviator.Catalog.airport_category
    :type: AirportCategory

    Get the airport category.

.. py:property:: navaid_category
    :canonical: ansys.stk.core.stkobjects.aviator.Catalog.navaid_category
    :type: NavaidCategory

    Get the navaid category.

.. py:property:: runway_category
    :canonical: ansys.stk.core.stkobjects.aviator.Catalog.runway_category
    :type: RunwayCategory

    Get the runway category.

.. py:property:: vtol_point_category
    :canonical: ansys.stk.core.stkobjects.aviator.Catalog.vtol_point_category
    :type: VTOLPointCategory

    Get the vtol point category.

.. py:property:: waypoint_category
    :canonical: ansys.stk.core.stkobjects.aviator.Catalog.waypoint_category
    :type: WaypointCategory

    Get the waypoint category.


