IMissileAdvancedAero
====================

.. py:class:: IMissileAdvancedAero

   object
   
   Interface used to access the Advanced aerodynamics options for a missile.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~body_width`
            * - :py:meth:`~body_height`
            * - :py:meth:`~body_length`
            * - :py:meth:`~nose_length`
            * - :py:meth:`~nose_tip_diameter`
            * - :py:meth:`~nozzle_diameter`
            * - :py:meth:`~max_aoa`
            * - :py:meth:`~min_mach`
            * - :py:meth:`~wing_count`
            * - :py:meth:`~wing_span`
            * - :py:meth:`~wing_surface_area`
            * - :py:meth:`~wing_leading_edge_sweep_angle`
            * - :py:meth:`~wing_leading_edge_section_angle`
            * - :py:meth:`~wing_mean_aero_chord_length`
            * - :py:meth:`~wing_max_thickness_along_mac`
            * - :py:meth:`~wing_lift_fraction`
            * - :py:meth:`~tail_count`
            * - :py:meth:`~tail_span`
            * - :py:meth:`~tail_surface_area`
            * - :py:meth:`~tail_leading_edge_sweep_angle`
            * - :py:meth:`~tail_leading_edge_section_angle`
            * - :py:meth:`~tail_mean_aero_chord_length`
            * - :py:meth:`~tail_max_thickness_along_mac`
            * - :py:meth:`~tail_lift_fraction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileAdvancedAero


Property detail
---------------

.. py:property:: body_width
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.body_width
    :type: float

    Gets or sets the missile body's width.

.. py:property:: body_height
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.body_height
    :type: float

    Gets or sets the missile body's height.

.. py:property:: body_length
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.body_length
    :type: float

    Gets or sets the missile body's length.

.. py:property:: nose_length
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.nose_length
    :type: float

    Gets or sets the missile nose's length.

.. py:property:: nose_tip_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.nose_tip_diameter
    :type: float

    Gets or sets the missile nose's diameter at the tip.

.. py:property:: nozzle_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.nozzle_diameter
    :type: float

    Gets or sets the diameter of the missile's nozzle.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.max_aoa
    :type: typing.Any

    Gets or sets the missile's maximum angle of attack.

.. py:property:: min_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.min_mach
    :type: float

    Gets or sets the minimum mach number of the missile.

.. py:property:: wing_count
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_count
    :type: int

    Gets or sets the number of wings on the missile.

.. py:property:: wing_span
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_span
    :type: float

    Gets or sets the span of one of the missile's wings.

.. py:property:: wing_surface_area
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_surface_area
    :type: float

    Gets or sets the area of one of the missile's wings.

.. py:property:: wing_leading_edge_sweep_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_leading_edge_sweep_angle
    :type: typing.Any

    Gets or sets the leading edge weep angle of the wings.

.. py:property:: wing_leading_edge_section_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_leading_edge_section_angle
    :type: typing.Any

    Gets or sets the leading edge section angle of the wings.

.. py:property:: wing_mean_aero_chord_length
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_mean_aero_chord_length
    :type: float

    Gets or sets the mean chord length of one of the missile's wings.

.. py:property:: wing_max_thickness_along_mac
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_max_thickness_along_mac
    :type: float

    Gets or sets the max thickness of the wing along the mean aerodynamic chord.

.. py:property:: wing_lift_fraction
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.wing_lift_fraction
    :type: float

    Gets or sets the lift fraction of the wing.

.. py:property:: tail_count
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_count
    :type: int

    Gets or sets the number of tails on the missile.

.. py:property:: tail_span
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_span
    :type: float

    Gets or sets the span of one of the missile's tails.

.. py:property:: tail_surface_area
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_surface_area
    :type: float

    Gets or sets the area of one of the missile's tails.

.. py:property:: tail_leading_edge_sweep_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_leading_edge_sweep_angle
    :type: typing.Any

    Gets or sets the leading edge weep angle of the tails.

.. py:property:: tail_leading_edge_section_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_leading_edge_section_angle
    :type: typing.Any

    Gets or sets the leading edge section angle of the tails.

.. py:property:: tail_mean_aero_chord_length
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_mean_aero_chord_length
    :type: float

    Gets or sets the mean chord length of one of the missile's tails.

.. py:property:: tail_max_thickness_along_mac
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_max_thickness_along_mac
    :type: float

    Gets or sets the max thickness of the tail along the mean aerodynamic chord.

.. py:property:: tail_lift_fraction
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAdvancedAero.tail_lift_fraction
    :type: float

    Gets or sets the lift fraction of the tail.


