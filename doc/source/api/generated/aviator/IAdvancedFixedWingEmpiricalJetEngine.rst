IAdvancedFixedWingEmpiricalJetEngine
====================================

.. py:class:: IAdvancedFixedWingEmpiricalJetEngine

   object
   
   Interface used to access the options for the Sub/Super/Hypersonic powerplant strategy in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_sea_level_static_thrust`
            * - :py:meth:`~design_point_altitude`
            * - :py:meth:`~design_point_mach_number`
            * - :py:meth:`~fuel_flow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingEmpiricalJetEngine


Property detail
---------------

.. py:property:: max_sea_level_static_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingEmpiricalJetEngine.max_sea_level_static_thrust
    :type: float

    Gets or sets the maximum static thrust of the engine at sea level.

.. py:property:: design_point_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingEmpiricalJetEngine.design_point_altitude
    :type: float

    Gets or sets the altitude design point of the engine.

.. py:property:: design_point_mach_number
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingEmpiricalJetEngine.design_point_mach_number
    :type: float

    Gets or sets the mach number design point of the engine.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingEmpiricalJetEngine.fuel_flow
    :type: float

    Gets or sets the engine's fuel flow at max power.


