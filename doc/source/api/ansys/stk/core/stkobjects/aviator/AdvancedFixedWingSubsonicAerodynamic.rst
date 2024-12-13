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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_type`
              - Gets or sets the type of wing geometry for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_basic`
              - Get the options for a basic geometry wing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_variable`
              - Get the options for a variable geometry wing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.max_aoa`
              - Gets or sets the maximum angle of attack possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.cd0`
              - Gets or sets the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.mach_divergence`
              - Gets or sets the speed at which the aircraft begins to experience air compression.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.transonic_mach_drag_factor`
              - Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying faster than the Mach Divergence.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingSubsonicAerodynamic


Property detail
---------------

.. py:property:: geometry_type
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_type
    :type: AdvancedFixedWingGeometry

    Gets or sets the type of wing geometry for the aircraft.

.. py:property:: geometry_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_basic
    :type: AdvancedFixedWingGeometryBasic

    Get the options for a basic geometry wing.

.. py:property:: geometry_mode_as_variable
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.geometry_mode_as_variable
    :type: AdvancedFixedWingGeometryVariable

    Get the options for a variable geometry wing.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: cd0
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.cd0
    :type: float

    Gets or sets the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.

.. py:property:: mach_divergence
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.mach_divergence
    :type: float

    Gets or sets the speed at which the aircraft begins to experience air compression.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingSubsonicAerodynamic.transonic_mach_drag_factor
    :type: float

    Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying faster than the Mach Divergence.


