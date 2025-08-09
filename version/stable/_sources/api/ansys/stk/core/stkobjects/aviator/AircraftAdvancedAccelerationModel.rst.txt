AircraftAdvancedAccelerationModel
=================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the advanced acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftAdvancedAccelerationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.level_turns`
              - Get the level turns interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.attitude_transitions`
              - Get the attitude transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.climb_and_descent_transitions`
              - Get the climb and descent transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.acceleration_mode`
              - Get the acceleration mode interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAdvancedAccelerationModel


Property detail
---------------

.. py:property:: level_turns
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.level_turns
    :type: LevelTurns

    Get the level turns interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.attitude_transitions
    :type: AttitudeTransitions

    Get the attitude transitions interface.

.. py:property:: climb_and_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.climb_and_descent_transitions
    :type: ClimbAndDescentTransitions

    Get the climb and descent transitions interface.

.. py:property:: acceleration_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.acceleration_mode
    :type: AircraftAccelerationMode

    Get the acceleration mode interface.


Method detail
-------------





.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedAccelerationModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

