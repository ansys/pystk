IPlanet
=======

.. py:class:: ansys.stk.core.stkobjects.IPlanet

   object
   
   Provide access to the properties and methods used in defining a planet object.

.. py:currentmodule:: IPlanet

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanet.graphics`
              - Get the planet's 2D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanet.access_constraints`
              - Get the constraints imposed on the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanet.graphics_3d`
              - Get the planet's 3D Graphics properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanet.position_source`
              - The criterion for defining the planet. A member of the AgEPlPositionSourceType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanet.position_source_data`
              - Get definitional data for the planet.
            * - :py:attr:`~ansys.stk.core.stkobjects.IPlanet.common_tasks`
              - Common Tasks associated with the planet.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlanet


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IPlanet.graphics
    :type: IPlanetGraphics

    Get the planet's 2D Graphics properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IPlanet.access_constraints
    :type: IAccessConstraintCollection

    Get the constraints imposed on the planet.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IPlanet.graphics_3d
    :type: IPlanetGraphics3D

    Get the planet's 3D Graphics properties.

.. py:property:: position_source
    :canonical: ansys.stk.core.stkobjects.IPlanet.position_source
    :type: PLANET_POSITION_SOURCE_TYPE

    The criterion for defining the planet. A member of the AgEPlPositionSourceType enumeration.

.. py:property:: position_source_data
    :canonical: ansys.stk.core.stkobjects.IPlanet.position_source_data
    :type: IPositionSourceData

    Get definitional data for the planet.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.IPlanet.common_tasks
    :type: IPlanetCommonTasks

    Common Tasks associated with the planet.


