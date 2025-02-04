AircraftAerodynamic
===================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic

   Class defining the aerodynamic options for a basic acceleration performance model of an Aviator aircraft.

.. py:currentmodule:: AircraftAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.aerodynamic_strategy`
              - Gets or sets the aerodynamic strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_simple`
              - Get the interface for a simple aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_basic_fixed_wing`
              - Get the interface for a basic fixed wing aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_external`
              - Get the interface for an external file aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_advanced_missile`
              - Get the interface for an advanced missile aerodynamics strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.lift_factor`
              - Gets or sets the scalar value applied to the lift for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.drag_factor`
              - Gets or sets the scalar value applied to the drag for parametric analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_four_point`
              - Get the interface for a four point aerodynamics strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAerodynamic


Property detail
---------------

.. py:property:: aerodynamic_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.aerodynamic_strategy
    :type: AircraftAerodynamicStrategy

    Gets or sets the aerodynamic strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_simple
    :type: AircraftSimpleAerodynamic

    Get the interface for a simple aerodynamics strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_basic_fixed_wing
    :type: AircraftBasicFixedWingAerodynamic

    Get the interface for a basic fixed wing aerodynamics strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_external
    :type: AircraftExternalAerodynamic

    Get the interface for an external file aerodynamics strategy.

.. py:property:: mode_as_advanced_missile
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_advanced_missile
    :type: MissileAdvancedAerodynamic

    Get the interface for an advanced missile aerodynamics strategy.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.lift_factor
    :type: float

    Gets or sets the scalar value applied to the lift for parametric analysis.

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.drag_factor
    :type: float

    Gets or sets the scalar value applied to the drag for parametric analysis.

.. py:property:: mode_as_four_point
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAerodynamic.mode_as_four_point
    :type: FourPointAerodynamic

    Get the interface for a four point aerodynamics strategy.


