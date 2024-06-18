IAircraftAdvancedAccelerationModel
==================================

.. py:class:: IAircraftAdvancedAccelerationModel

   object
   
   Interface used to access the Advanced Acceleration Model options of an aircraft.

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
            * - :py:meth:`~acceleration_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedAccelerationModel


Property detail
---------------

.. py:property:: level_turns
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.level_turns
    :type: "IAgAvtrLevelTurns"

    Get the level turns interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.attitude_transitions
    :type: "IAgAvtrAttitudeTransitions"

    Get the attitude transitions interface.

.. py:property:: climb_and_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.climb_and_descent_transitions
    :type: "IAgAvtrClimbAndDescentTransitions"

    Get the climb and descent transitions interface.

.. py:property:: acceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.acceleration_mode
    :type: "IAgAvtrAircraftAccelerationMode"

    Get the acceleration mode interface.


Method detail
-------------





.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

