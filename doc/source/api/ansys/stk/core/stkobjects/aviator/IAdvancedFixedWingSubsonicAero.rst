IAdvancedFixedWingSubsonicAero
==============================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero

   object
   
   Interface used to access the options for the subsonic aerodynamic strategy in the advanced fixed wing tool.

.. py:currentmodule:: IAdvancedFixedWingSubsonicAero

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.geometry_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.geometry_mode_as_basic`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.geometry_mode_as_variable`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.max_aoa`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.cd0`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.mach_divergence`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.transonic_mach_drag_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAdvancedFixedWingSubsonicAero


Property detail
---------------

.. py:property:: geometry_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.geometry_type
    :type: ADVANCED_FIXED_WING_GEOMETRY

    Gets or sets the type of wing geometry for the aircraft.

.. py:property:: geometry_mode_as_basic
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.geometry_mode_as_basic
    :type: IAdvancedFixedWingGeometryBasic

    Get the options for a basic geometry wing.

.. py:property:: geometry_mode_as_variable
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.geometry_mode_as_variable
    :type: IAdvancedFixedWingGeometryVariable

    Get the options for a variable geometry wing.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.max_aoa
    :type: typing.Any

    Gets or sets the maximum angle of attack possible.

.. py:property:: cd0
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.cd0
    :type: float

    Gets or sets the parasitic drag coefficient of the aircraft when flying at a speed less than the Mach Divergence.

.. py:property:: mach_divergence
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.mach_divergence
    :type: float

    Gets or sets the speed at which the aircraft begins to experience air compression.

.. py:property:: transonic_mach_drag_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IAdvancedFixedWingSubsonicAero.transonic_mach_drag_factor
    :type: float

    Gets or sets the factor applied to the aircraft's parasitic drag coefficient when it is flying faster than the Mach Divergence.


