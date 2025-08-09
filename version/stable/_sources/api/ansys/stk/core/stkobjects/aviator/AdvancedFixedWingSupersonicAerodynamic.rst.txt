AdvancedFixedWingSupersonicAerodynamic
======================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic

   Class defining the supersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingSupersonicAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.geometry_type`
              - Get or set the type of wing geometry for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.geometry_mode_as_basic`
              - Get the options for a basic geometry wing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.geometry_mode_as_variable`
              - Get the options for a variable geometry wing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.max_aoa`
              - Get or set the maximum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.subsonic_cd0`
              - Get or set the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.transonic_min_mach`
              - Get or set the minimum speed at which the aircraft begins to experience air compression.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.transonic_max_mach`
              - Get or set the maximum speed, below supersonic, at which the aircraft begins to experience air compression.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.supersonic_max_mach`
              - Get or set the speed at which the Supersonic Mach Drag Factor is applied.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.transonic_mach_drag_factor`
              - Get or set the factor applied to the aircraft's parasitic drag coefficient when it is flying between the Transonic Min Mach and Transonic Mach Drag Factor speeds.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.supersonic_mach_drag_factor`
              - Get or set the scalar value applied to the aircraft's parasitic drag coefficient when it is flying faster than the Supersonic Max Mach.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.leading_edge_suction_efficiency`
              - Get or set the ability of the wing's leading edge to ingest turbulent airflow and thereby reduce induced drag.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingSupersonicAerodynamic


Property detail
---------------

.. py:property:: geometry_type
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.geometry_type
    :type: AdvancedFixedWingGeometry

    Get or set the type of wing geometry for the aircraft.

.. py:property:: geometry_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.geometry_mode_as_basic
    :type: AdvancedFixedWingGeometryBasic

    Get the options for a basic geometry wing.

.. py:property:: geometry_mode_as_variable
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.geometry_mode_as_variable
    :type: AdvancedFixedWingGeometryVariable

    Get the options for a variable geometry wing.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.max_aoa
    :type: typing.Any

    Get or set the maximum angle of attack possible.

.. py:property:: subsonic_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.subsonic_cd0
    :type: float

    Get or set the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.

.. py:property:: transonic_min_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.transonic_min_mach
    :type: float

    Get or set the minimum speed at which the aircraft begins to experience air compression.

.. py:property:: transonic_max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.transonic_max_mach
    :type: float

    Get or set the maximum speed, below supersonic, at which the aircraft begins to experience air compression.

.. py:property:: supersonic_max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.supersonic_max_mach
    :type: float

    Get or set the speed at which the Supersonic Mach Drag Factor is applied.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.transonic_mach_drag_factor
    :type: float

    Get or set the factor applied to the aircraft's parasitic drag coefficient when it is flying between the Transonic Min Mach and Transonic Mach Drag Factor speeds.

.. py:property:: supersonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.supersonic_mach_drag_factor
    :type: float

    Get or set the scalar value applied to the aircraft's parasitic drag coefficient when it is flying faster than the Supersonic Max Mach.

.. py:property:: leading_edge_suction_efficiency
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSupersonicAerodynamic.leading_edge_suction_efficiency
    :type: float

    Get or set the ability of the wing's leading edge to ingest turbulent airflow and thereby reduce induced drag.


