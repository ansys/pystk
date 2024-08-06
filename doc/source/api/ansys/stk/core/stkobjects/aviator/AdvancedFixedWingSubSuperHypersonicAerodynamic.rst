AdvancedFixedWingSubSuperHypersonicAerodynamic
==============================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic

   Class defining the Sub/Super/Hypersonic aerodynamic strategy in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingSubSuperHypersonicAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.max_aoa`
              - Gets or sets the maximum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.transonic_min_mach`
              - Gets or sets the minimum speed at which the aircraft begins to experience air compression.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.transonic_max_mach`
              - Gets or sets the maximum speed, below supersonic, at which the aircraft begins to experience air compression.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.super_hyper_mach_transition`
              - Gets or sets the minimum speed at which the air flow will be treated as hypersonic.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.leading_edge_frontal_area_ratio`
              - Gets or sets the frontal face thickness of the aircraft's wings at their leading edge.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.subsonic_aspect_ratio`
              - Gets or sets the aircraft's wingspan squared divided by the wing area.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.transonic_mach_drag_factor`
              - Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying between the Transonic Min Mach and Transonic Mach Drag Factor speeds.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.wave_drag_factor`
              - Gets or sets the scalar value that models drag produced by shock waves at or near the aircraft's critical Mach number.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingSubSuperHypersonicAerodynamic


Property detail
---------------

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: transonic_min_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.transonic_min_mach
    :type: float

    Gets or sets the minimum speed at which the aircraft begins to experience air compression.

.. py:property:: transonic_max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.transonic_max_mach
    :type: float

    Gets or sets the maximum speed, below supersonic, at which the aircraft begins to experience air compression.

.. py:property:: super_hyper_mach_transition
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.super_hyper_mach_transition
    :type: float

    Gets or sets the minimum speed at which the air flow will be treated as hypersonic.

.. py:property:: leading_edge_frontal_area_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.leading_edge_frontal_area_ratio
    :type: float

    Gets or sets the frontal face thickness of the aircraft's wings at their leading edge.

.. py:property:: subsonic_aspect_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.subsonic_aspect_ratio
    :type: float

    Gets or sets the aircraft's wingspan squared divided by the wing area.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.transonic_mach_drag_factor
    :type: float

    Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying between the Transonic Min Mach and Transonic Mach Drag Factor speeds.

.. py:property:: wave_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubSuperHypersonicAerodynamic.wave_drag_factor
    :type: float

    Gets or sets the scalar value that models drag produced by shock waves at or near the aircraft's critical Mach number.


