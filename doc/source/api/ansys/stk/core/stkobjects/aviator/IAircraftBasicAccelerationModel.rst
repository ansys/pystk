IAircraftBasicAccelerationModel
===============================

.. py:class:: IAircraftBasicAccelerationModel

   object
   
   Interface used to access the basic acceleration model options for an acceleration model of an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~level_turns`
            * - :py:meth:`~attitude_transitions`
            * - :py:meth:`~climb_and_descent_transitions`
            * - :py:meth:`~aerodynamics`
            * - :py:meth:`~propulsion`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftBasicAccelerationModel


Property detail
---------------

.. py:property:: level_turns
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicAccelerationModel.level_turns
    :type: "IAgAvtrLevelTurns"

    Get the level turns interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicAccelerationModel.attitude_transitions
    :type: "IAgAvtrAttitudeTransitions"

    Get the attitude transitions interface.

.. py:property:: climb_and_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicAccelerationModel.climb_and_descent_transitions
    :type: "IAgAvtrClimbAndDescentTransitions"

    Get the climb and descent transitions interface.

.. py:property:: aerodynamics
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicAccelerationModel.aerodynamics
    :type: "IAgAvtrAircraftAero"

    Get the aerodynamics interface.

.. py:property:: propulsion
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftBasicAccelerationModel.propulsion
    :type: "IAgAvtrAircraftProp"

    Get the propulsion interface.


Method detail
-------------






.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

