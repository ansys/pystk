AircraftModels
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftModels

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogSource`

   Class defining the User Aircraft Models in the Aviator Catalog.

.. py:currentmodule:: AircraftModels

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModels.get_aircraft`
              - Get the aircraft with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModels.add_aircraft`
              - Create a new aircraft with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftModels.get_as_catalog_source`
              - Get the catalog source interface for this object.


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

    from ansys.stk.core.stkobjects.aviator import AircraftModels



Method detail
-------------

.. py:method:: get_aircraft(self, aircraft_name: str) -> AircraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModels.get_aircraft

    Get the aircraft with the given name.

    :Parameters:

        **aircraft_name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftModel`

.. py:method:: add_aircraft(self, aircraft_name: str) -> AircraftModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModels.add_aircraft

    Create a new aircraft with the given name.

    :Parameters:

        **aircraft_name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftModel`

.. py:method:: get_as_catalog_source(self) -> ICatalogSource
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftModels.get_as_catalog_source

    Get the catalog source interface for this object.

    :Returns:

        :obj:`~ICatalogSource`

