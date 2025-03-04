AircraftCategory
================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftCategory

   Class defining the aircraft category in the Aviator catalog.

.. py:currentmodule:: AircraftCategory

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCategory.aircraft_models`
              - Get the user aircraft models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCategory.missile_models`
              - Get the user missile models.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftCategory.rotorcraft_models`
              - Get the user rotorcraft models.



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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftCategory


Property detail
---------------

.. py:property:: aircraft_models
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCategory.aircraft_models
    :type: AircraftModels

    Get the user aircraft models.

.. py:property:: missile_models
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCategory.missile_models
    :type: MissileModels

    Get the user missile models.

.. py:property:: rotorcraft_models
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftCategory.rotorcraft_models
    :type: RotorcraftModels

    Get the user rotorcraft models.


