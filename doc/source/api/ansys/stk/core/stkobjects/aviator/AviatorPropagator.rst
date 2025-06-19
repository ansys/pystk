AviatorPropagator
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.AviatorPropagator

   Class defining the Aviator propagator.

.. py:currentmodule:: AviatorPropagator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.propagate`
              - Apply All Change.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_mission`
              - Get the Aviator mission.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.auto_recalculate`
              - Opt whether to have the propagator auto recalculate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_catalog`
              - Get the Aviator catalog.



Examples
--------

Configure the Aviator propagator

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    # Set to Propagator to Aviator
    aircraft.set_route_type(PropagatorType.AVIATOR)
    # Get the aircraft's route
    aircraftRoute = aircraft.route
    # Get the Aviator propagator
    propagator = aircraftRoute.aviator_propagator
    # Get the Aviator mission
    mission = propagator.aviator_mission
    # Get the list of phases from the mission
    phases = mission.phases
    # Get the list of procedures from the first phase
    procedures = phases[0].procedures
    # Propagate the route
    propagator.propagate()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AviatorPropagator


Property detail
---------------

.. py:property:: aviator_mission
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_mission
    :type: Mission

    Get the Aviator mission.

.. py:property:: auto_recalculate
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.auto_recalculate
    :type: bool

    Opt whether to have the propagator auto recalculate.

.. py:property:: aviator_catalog
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.aviator_catalog
    :type: Catalog

    Get the Aviator catalog.


Method detail
-------------


.. py:method:: propagate(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AviatorPropagator.propagate

    Apply All Change.

    :Returns:

        :obj:`~None`




