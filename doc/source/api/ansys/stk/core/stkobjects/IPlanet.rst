IPlanet
=======

.. py:class:: IPlanet

   object
   
   Provide access to the properties and methods used in defining a planet object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~graphics`
            * - :py:meth:`~access_constraints`
            * - :py:meth:`~graphics_3d`
            * - :py:meth:`~position_source`
            * - :py:meth:`~position_source_data`
            * - :py:meth:`~common_tasks`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPlanet


Property detail
---------------

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IPlanet.graphics
    :type: IAgPlGraphics

    Get the planet's 2D Graphics properties.

.. py:property:: access_constraints
    :canonical: ansys.stk.core.stkobjects.IPlanet.access_constraints
    :type: IAgAccessConstraintCollection

    Get the constraints imposed on the planet.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IPlanet.graphics_3d
    :type: IAgPlVO

    Get the planet's 3D Graphics properties.

.. py:property:: position_source
    :canonical: ansys.stk.core.stkobjects.IPlanet.position_source
    :type: PLANET_POSITION_SOURCE_TYPE

    The criterion for defining the planet. A member of the AgEPlPositionSourceType enumeration.

.. py:property:: position_source_data
    :canonical: ansys.stk.core.stkobjects.IPlanet.position_source_data
    :type: IAgPositionSourceData

    Get definitional data for the planet.

.. py:property:: common_tasks
    :canonical: ansys.stk.core.stkobjects.IPlanet.common_tasks
    :type: IAgPlCommonTasks

    Common Tasks associated with the planet.


