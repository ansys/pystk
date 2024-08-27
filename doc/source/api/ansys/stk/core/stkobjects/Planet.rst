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
    :type: PLANET_POSITION_SOURCE_TYPE

    The criterion for defining the planet. A member of the AgEPlPositionSourceType enumeration.

.. py:property:: position_source_data
    :canonical: ansys.stk.core.stkobjects.Planet.position_source_data
    :type: IPositionSourceData

    Get definitional data for the planet.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.Planet.common_tasks
    :type: PlanetCommonTasks

    Common Tasks associated with the planet.


