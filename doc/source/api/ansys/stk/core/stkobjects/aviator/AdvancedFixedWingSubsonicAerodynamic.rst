AdvancedFixedWingSubsonicAerodynamic
====================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic

   Class defining the subsonic aerodynamic strategy in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingSubsonicAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.cd0`
              - Get or set the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_basic`
              - Get the options for a basic geometry wing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_variable`
              - Get the options for a variable geometry wing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_type`
              - Get or set the type of wing geometry for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.mach_divergence`
              - Get or set the speed at which the aircraft begins to experience air compression.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.max_aoa`
              - Get or set the maximum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.transonic_mach_drag_factor`
              - Get or set the factor applied to the aircraft's parasitic drag coefficient when it is flying faster than the Mach Divergence.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingSubsonicAerodynamic


Property detail
---------------

.. py:property:: cd0
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.cd0
    :type: float

    Get or set the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.

.. py:property:: geometry_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_basic
    :type: AdvancedFixedWingGeometryBasic

    Get the options for a basic geometry wing.

.. py:property:: geometry_mode_as_variable
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_variable
    :type: AdvancedFixedWingGeometryVariable

    Get the options for a variable geometry wing.

.. py:property:: geometry_type
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_type
    :type: AdvancedFixedWingGeometry

    Get or set the type of wing geometry for the aircraft.

.. py:property:: mach_divergence
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.mach_divergence
    :type: float

    Get or set the speed at which the aircraft begins to experience air compression.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.max_aoa
    :type: typing.Any

    Get or set the maximum angle of attack possible.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.transonic_mach_drag_factor
    :type: float

    Get or set the factor applied to the aircraft's parasitic drag coefficient when it is flying faster than the Mach Divergence.


