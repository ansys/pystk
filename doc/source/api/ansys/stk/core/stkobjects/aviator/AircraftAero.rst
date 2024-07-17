AircraftAero
============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAero

   Bases: 

   Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftAero

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.aero_strategy`
              - Gets or sets the aerodynamic strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_simple`
              - Get the interface for a simple aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_basic_fixed_wing`
              - Get the interface for a basic fixed wing aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_external`
              - Get the interface for an external file aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_advanced_missile`
              - Get the interface for an advanced missile aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.lift_factor`
              - Gets or sets the scalar value applied to the lift for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAero.drag_factor`
              - Gets or sets the scalar value applied to the drag for parametric analysis.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAero


Property detail
---------------

.. py:property:: aero_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.aero_strategy
    :type: AIRCRAFT_AERO_STRATEGY

    Gets or sets the aerodynamic strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_simple
    :type: IAircraftSimpleAero

    Get the interface for a simple aerodynamics strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_basic_fixed_wing
    :type: IAircraftBasicFixedWingAero

    Get the interface for a basic fixed wing aerodynamics strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_external
    :type: IAircraftExternalAero

    Get the interface for an external file aerodynamics strategy.

.. py:property:: mode_as_advanced_missile
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.mode_as_advanced_missile
    :type: IMissileAdvancedAero

    Get the interface for an advanced missile aerodynamics strategy.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.lift_factor
    :type: float

    Gets or sets the scalar value applied to the lift for parametric analysis.

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAero.drag_factor
    :type: float

    Gets or sets the scalar value applied to the drag for parametric analysis.


