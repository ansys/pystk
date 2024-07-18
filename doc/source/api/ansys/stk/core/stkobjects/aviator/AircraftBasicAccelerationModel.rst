AircraftBasicAccelerationModel
==============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the basic acceleration performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftBasicAccelerationModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.level_turns`
              - Get the level turns interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.attitude_transitions`
              - Get the attitude transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.climb_and_descent_transitions`
              - Get the climb and descent transitions interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.aerodynamics`
              - Get the aerodynamics interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.propulsion`
              - Get the propulsion interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftBasicAccelerationModel


Property detail
---------------

.. py:property:: level_turns
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.level_turns
    :type: ILevelTurns

    Get the level turns interface.

.. py:property:: attitude_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.attitude_transitions
    :type: IAttitudeTransitions

    Get the attitude transitions interface.

.. py:property:: climb_and_descent_transitions
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.climb_and_descent_transitions
    :type: IClimbAndDescentTransitions

    Get the climb and descent transitions interface.

.. py:property:: aerodynamics
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.aerodynamics
    :type: IAircraftAero

    Get the aerodynamics interface.

.. py:property:: propulsion
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.propulsion
    :type: IAircraftProp

    Get the propulsion interface.


Method detail
-------------






.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftBasicAccelerationModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

