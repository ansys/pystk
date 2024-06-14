IRotorcraftAero
===============

.. py:class:: IRotorcraftAero

   object
   
   Interface used to access the aerodynamics options for a rotorcraft.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~rotor_count`
            * - :py:meth:`~rotor_diameter`
            * - :py:meth:`~blades_per_rotor`
            * - :py:meth:`~blade_chord`
            * - :py:meth:`~rotor_tip_mach`
            * - :py:meth:`~fuselage_flat_plate_area`
            * - :py:meth:`~tail_rotor_offset`
            * - :py:meth:`~tail_rotor_diameter`
            * - :py:meth:`~blade_profile_drag_cd0`
            * - :py:meth:`~blade_profile_drag_k`
            * - :py:meth:`~induced_power_correction_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IRotorcraftAero


Property detail
---------------

.. py:property:: rotor_count
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.rotor_count
    :type: int

    Gets or sets the number of rotors.

.. py:property:: rotor_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.rotor_diameter
    :type: float

    Gets or sets the diameter of the rotor.

.. py:property:: blades_per_rotor
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.blades_per_rotor
    :type: int

    Gets or sets the number of blades on each rotor.

.. py:property:: blade_chord
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.blade_chord
    :type: float

    Gets or sets the chord length of the blade.

.. py:property:: rotor_tip_mach
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.rotor_tip_mach
    :type: float

    Gets or sets the Mach number of the advancing blade tip.

.. py:property:: fuselage_flat_plate_area
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.fuselage_flat_plate_area
    :type: float

    Gets or sets the flat plate area for the fuselage.

.. py:property:: tail_rotor_offset
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.tail_rotor_offset
    :type: float

    Gets or sets the offset of the tail rotor.

.. py:property:: tail_rotor_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.tail_rotor_diameter
    :type: float

    Gets or sets the diameter of the tail rotor.

.. py:property:: blade_profile_drag_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.blade_profile_drag_cd0
    :type: float

    Gets or sets the drag coefficient when the rotor disc does not generate any lift.

.. py:property:: blade_profile_drag_k
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.blade_profile_drag_k
    :type: float

    Gets or sets the induced drag coefficient, which accounts for how lift generation impacts drag.

.. py:property:: induced_power_correction_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IRotorcraftAero.induced_power_correction_factor
    :type: float

    Gets or sets the slop factor that accounts for losses.


