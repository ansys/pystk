IAdvancedFixedWingSubSuperHypersonicAero
========================================

.. py:class:: IAdvancedFixedWingSubSuperHypersonicAero

   object
   
   Interface used to access the options for the Sub/Super/Hypersonic aerodynamic strategy in the advanced fixed wing tool.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~max_aoa`
            * - :py:meth:`~transonic_min_mach`
            * - :py:meth:`~transonic_max_mach`
            * - :py:meth:`~super_hyper_mach_transition`
            * - :py:meth:`~leading_edge_frontal_area_ratio`
            * - :py:meth:`~subsonic_aspect_ratio`
            * - :py:meth:`~transonic_mach_drag_factor`
            * - :py:meth:`~wave_drag_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingSubSuperHypersonicAero


Property detail
---------------

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: transonic_min_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.transonic_min_mach
    :type: float

    Gets or sets the minimum speed at which the aircraft begins to experience air compression.

.. py:property:: transonic_max_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.transonic_max_mach
    :type: float

    Gets or sets the maximum speed, below supersonic, at which the aircraft begins to experience air compression.

.. py:property:: super_hyper_mach_transition
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.super_hyper_mach_transition
    :type: float

    Gets or sets the minimum speed at which the air flow will be treated as hypersonic.

.. py:property:: leading_edge_frontal_area_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.leading_edge_frontal_area_ratio
    :type: float

    Gets or sets the frontal face thickness of the aircraft's wings at their leading edge.

.. py:property:: subsonic_aspect_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.subsonic_aspect_ratio
    :type: float

    Gets or sets the aircraft's wingspan squared divided by the wing area.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.transonic_mach_drag_factor
    :type: float

    Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying between the Transonic Min Mach and Transonic Mach Drag Factor speeds.

.. py:property:: wave_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubSuperHypersonicAero.wave_drag_factor
    :type: float

    Gets or sets the scalar value that models drag produced by shock waves at or near the aircraft's critical Mach number.


