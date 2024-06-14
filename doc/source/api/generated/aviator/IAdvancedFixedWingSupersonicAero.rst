IAdvancedFixedWingSupersonicAero
================================

.. py:class:: IAdvancedFixedWingSupersonicAero

   object
   
   Interface used to access the options for the supersonic aerodynamic strategy in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~geometry_type`
            * - :py:meth:`~geometry_mode_as_basic`
            * - :py:meth:`~geometry_mode_as_variable`
            * - :py:meth:`~max_aoa`
            * - :py:meth:`~subsonic_cd0`
            * - :py:meth:`~transonic_min_mach`
            * - :py:meth:`~transonic_max_mach`
            * - :py:meth:`~supersonic_max_mach`
            * - :py:meth:`~transonic_mach_drag_factor`
            * - :py:meth:`~supersonic_mach_drag_factor`
            * - :py:meth:`~leading_edge_suction_efficiency`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingSupersonicAero


Property detail
---------------

.. py:property:: geometry_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.geometry_type
    :type: "ADVANCED_FIXED_WING_GEOMETRY"

    Gets or sets the type of wing geometry for the aircraft.

.. py:property:: geometry_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.geometry_mode_as_basic
    :type: "IAgAvtrAdvFixedWingGeometryBasic"

    Get the options for a basic geometry wing.

.. py:property:: geometry_mode_as_variable
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.geometry_mode_as_variable
    :type: "IAgAvtrAdvFixedWingGeometryVariable"

    Get the options for a variable geometry wing.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: subsonic_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.subsonic_cd0
    :type: float

    Gets or sets the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.

.. py:property:: transonic_min_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.transonic_min_mach
    :type: float

    Gets or sets the minimum speed at which the aircraft begins to experience air compression.

.. py:property:: transonic_max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.transonic_max_mach
    :type: float

    Gets or sets the maximum speed, below supersonic, at which the aircraft begins to experience air compression.

.. py:property:: supersonic_max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.supersonic_max_mach
    :type: float

    Gets or sets the speed at which the Supersonic Mach Drag Factor is applied.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.transonic_mach_drag_factor
    :type: float

    Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying between the Transonic Min Mach and Transonic Mach Drag Factor speeds.

.. py:property:: supersonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.supersonic_mach_drag_factor
    :type: float

    Gets or sets the scalar value applied to the aircraft's parasitic drag coefficient when it is flying faster than the Supersonic Max Mach.

.. py:property:: leading_edge_suction_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSupersonicAero.leading_edge_suction_efficiency
    :type: float

    Gets or sets the ability of the wing's leading edge to ingest turbulent airflow and thereby reduce induced drag.


