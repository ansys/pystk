IAircraftAero
=============

.. py:class:: IAircraftAero

   object
   
   Interface used to access the Aerodynamics options for the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aero_strategy`
            * - :py:meth:`~mode_as_simple`
            * - :py:meth:`~mode_as_basic_fixed_wing`
            * - :py:meth:`~mode_as_external`
            * - :py:meth:`~mode_as_advanced_missile`
            * - :py:meth:`~lift_factor`
            * - :py:meth:`~drag_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAero


Property detail
---------------

.. py:property:: aero_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.aero_strategy
    :type: "AIRCRAFT_AERO_STRATEGY"

    Gets or sets the aerodynamic strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.mode_as_simple
    :type: "IAgAvtrAircraftSimpleAero"

    Get the interface for a simple aerodynamics strategy.

.. py:property:: mode_as_basic_fixed_wing
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.mode_as_basic_fixed_wing
    :type: "IAgAvtrAircraftBasicFixedWingAero"

    Get the interface for a basic fixed wing aerodynamics strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.mode_as_external
    :type: "IAgAvtrAircraftExternalAero"

    Get the interface for an external file aerodynamics strategy.

.. py:property:: mode_as_advanced_missile
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.mode_as_advanced_missile
    :type: "IAgAvtrMissileAdvancedAero"

    Get the interface for an advanced missile aerodynamics strategy.

.. py:property:: lift_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.lift_factor
    :type: float

    Gets or sets the scalar value applied to the lift for parametric analysis.

.. py:property:: drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAero.drag_factor
    :type: float

    Gets or sets the scalar value applied to the drag for parametric analysis.


