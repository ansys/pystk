Planet
======

.. py:class:: ansys.stk.core.stkobjects.Planet

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Class defining the Planet object.

.. py:currentmodule:: Planet

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Planet.graphics`
              - Get the planet's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Planet.access_constraints`
              - Get the constraints imposed on the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.Planet.graphics_3d`
              - Get the planet's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.Planet.position_source`
              - The criterion for defining the planet. A member of the AgEPlPositionSourceType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Planet.position_source_data`
              - Get definitional data for the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.Planet.common_tasks`
              - Common Tasks associated with the planet.



Examples
--------

Modify a Planet's 2D Properties

.. code-block:: python

    # Planet planet: Planet object
    planet2D = planet.graphics
    planet2D.color = Colors.Red
    planet2D.inherit = False
    planet2D.show_orbit = True
    planet2D.show_sub_planet_point = False
    planet2D.show_sub_planet_label = False


Create a New Planet

.. code-block:: python

    # Scenario scenario: Scenario object
    planet = scenario.children.new(STKObjectType.PLANET, "Mars")
    planet.common_tasks.set_position_source_central_body("Mars", EphemSourceType.JPL_DEVELOPMENTAL_EPHEMERIS)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Planet


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Planet.graphics
    :type: PlanetGraphics

    Get the planet's 2D Graphics properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.Planet.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the planet.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Planet.graphics_3d
    :type: PlanetGraphics3D

    Get the planet's 3D Graphics properties.

.. py:property:: position_source
    :canonical: ansys.stk.core.stkobjects.Planet.position_source
    :type: PlanetPositionSourceType

    The criterion for defining the planet. A member of the AgEPlPositionSourceType enumeration.

.. py:property:: position_source_data
    :canonical: ansys.stk.core.stkobjects.Planet.position_source_data
    :type: IPositionSourceData

    Get definitional data for the planet.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.Planet.common_tasks
    :type: PlanetCommonTasks

    Common Tasks associated with the planet.


