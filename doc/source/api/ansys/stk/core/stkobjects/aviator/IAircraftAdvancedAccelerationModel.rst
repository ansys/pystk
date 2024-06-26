IAircraftAdvancedAccelerationModel
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel

   object
   
   Interface used to access the Advanced Acceleration Model options of an aircraft.

.. py:currentmodule:: IAircraftAdvancedAccelerationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.level_turns`
              - Get the level turns interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.attitude_transitions`
              - Get the attitude transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.climb_and_descent_transitions`
              - Get the climb and descent transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.acceleration_mode`
              - Get the acceleration mode interface.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedAccelerationModel


Property detail
---------------

.. py:property:: level_turns
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.level_turns
    :type: ILevelTurns

    Get the level turns interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.attitude_transitions
    :type: IAttitudeTransitions

    Get the attitude transitions interface.

.. py:property:: climb_and_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.climb_and_descent_transitions
    :type: IClimbAndDescentTransitions

    Get the climb and descent transitions interface.

.. py:property:: acceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.acceleration_mode
    :type: IAircraftAccelerationMode

    Get the acceleration mode interface.


Method detail
-------------





.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedAccelerationModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

