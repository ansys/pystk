RotorcraftAerodynamic
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic

   Class defining the aerodynamic options for a rotorcraft.

.. py:currentmodule:: RotorcraftAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.rotor_count`
              - Get or set the number of rotors.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.rotor_diameter`
              - Get or set the diameter of the rotor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blades_per_rotor`
              - Get or set the number of blades on each rotor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blade_chord`
              - Get or set the chord length of the blade.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.rotor_tip_mach`
              - Get or set the Mach number of the advancing blade tip.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.fuselage_flat_plate_area`
              - Get or set the flat plate area for the fuselage.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.tail_rotor_offset`
              - Get or set the offset of the tail rotor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.tail_rotor_diameter`
              - Get or set the diameter of the tail rotor.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blade_profile_drag_cd0`
              - Get or set the drag coefficient when the rotor disc does not generate any lift.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blade_profile_drag_k`
              - Get or set the induced drag coefficient, which accounts for how lift generation impacts drag.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.induced_power_correction_factor`
              - Get or set the slop factor that accounts for losses.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import RotorcraftAerodynamic


Property detail
---------------

.. py:property:: rotor_count
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.rotor_count
    :type: int

    Get or set the number of rotors.

.. py:property:: rotor_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.rotor_diameter
    :type: float

    Get or set the diameter of the rotor.

.. py:property:: blades_per_rotor
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blades_per_rotor
    :type: int

    Get or set the number of blades on each rotor.

.. py:property:: blade_chord
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blade_chord
    :type: float

    Get or set the chord length of the blade.

.. py:property:: rotor_tip_mach
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.rotor_tip_mach
    :type: float

    Get or set the Mach number of the advancing blade tip.

.. py:property:: fuselage_flat_plate_area
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.fuselage_flat_plate_area
    :type: float

    Get or set the flat plate area for the fuselage.

.. py:property:: tail_rotor_offset
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.tail_rotor_offset
    :type: float

    Get or set the offset of the tail rotor.

.. py:property:: tail_rotor_diameter
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.tail_rotor_diameter
    :type: float

    Get or set the diameter of the tail rotor.

.. py:property:: blade_profile_drag_cd0
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blade_profile_drag_cd0
    :type: float

    Get or set the drag coefficient when the rotor disc does not generate any lift.

.. py:property:: blade_profile_drag_k
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.blade_profile_drag_k
    :type: float

    Get or set the induced drag coefficient, which accounts for how lift generation impacts drag.

.. py:property:: induced_power_correction_factor
    :canonical: ansys.stk.core.stkobjects.aviator.RotorcraftAerodynamic.induced_power_correction_factor
    :type: float

    Get or set the slop factor that accounts for losses.


