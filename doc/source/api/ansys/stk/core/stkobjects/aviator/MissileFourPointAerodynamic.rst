MissileFourPointAerodynamic
===========================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic

   Class defining the FourPoint aerodynamic strategy in the Missile.

.. py:currentmodule:: MissileFourPointAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.validate_lift_design_points`
              - Validate the lift design points - ensure the choices do not result in a singular system of equations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.validate_drag_design_points`
              - Validate the drag design points - ensure the choices do not result in a singular system of equations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.set_aoa`
              - Get or set and validates the maximum, max range and max endurance AOA values for the aircraft.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_1`
              - Get or set the Mach for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_1`
              - Get or set the AOA for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_1`
              - Get or set the lift coefficient for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_1`
              - Get or set the drag coefficient for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_2`
              - Get or set the Mach for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_2`
              - Get or set the AOA for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_2`
              - Get or set the lift coefficient for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_2`
              - Get or set the drag coefficient for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_3`
              - Get or set the Mach for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_3`
              - Get or set the AOA for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_3`
              - Get or set the lift coefficient for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_3`
              - Get or set the drag coefficient for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_4`
              - Get or set the Mach for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_4`
              - Get or set the AOA for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_4`
              - Get or set the lift coefficient for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_4`
              - Get or set the drag coefficient for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.s_reference`
              - Get or set the aerodynamic reference area for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.max_aoa`
              - Get the maximum AOA for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.max_endurance_aoa`
              - Get the maximum endurance AOA for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.max_range_aoa`
              - Get the maximum range AOA for the aircraft.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileFourPointAerodynamic


Property detail
---------------

.. py:property:: mach_1
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_1
    :type: float

    Get or set the Mach for the first design point.

.. py:property:: aoa_1
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_1
    :type: typing.Any

    Get or set the AOA for the first design point.

.. py:property:: cl_1
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_1
    :type: float

    Get or set the lift coefficient for the first design point.

.. py:property:: cd_1
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_1
    :type: float

    Get or set the drag coefficient for the first design point.

.. py:property:: mach_2
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_2
    :type: float

    Get or set the Mach for the second design point.

.. py:property:: aoa_2
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_2
    :type: typing.Any

    Get or set the AOA for the second design point.

.. py:property:: cl_2
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_2
    :type: float

    Get or set the lift coefficient for the second design point.

.. py:property:: cd_2
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_2
    :type: float

    Get or set the drag coefficient for the second design point.

.. py:property:: mach_3
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_3
    :type: float

    Get or set the Mach for the third design point.

.. py:property:: aoa_3
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_3
    :type: typing.Any

    Get or set the AOA for the third design point.

.. py:property:: cl_3
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_3
    :type: float

    Get or set the lift coefficient for the third design point.

.. py:property:: cd_3
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_3
    :type: float

    Get or set the drag coefficient for the third design point.

.. py:property:: mach_4
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.mach_4
    :type: float

    Get or set the Mach for the fourth design point.

.. py:property:: aoa_4
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.aoa_4
    :type: typing.Any

    Get or set the AOA for the fourth design point.

.. py:property:: cl_4
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cl_4
    :type: float

    Get or set the lift coefficient for the fourth design point.

.. py:property:: cd_4
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.cd_4
    :type: float

    Get or set the drag coefficient for the fourth design point.

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.s_reference
    :type: typing.Any

    Get or set the aerodynamic reference area for the aircraft.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.max_aoa
    :type: typing.Any

    Get the maximum AOA for the aircraft.

.. py:property:: max_endurance_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.max_endurance_aoa
    :type: typing.Any

    Get the maximum endurance AOA for the aircraft.

.. py:property:: max_range_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.max_range_aoa
    :type: typing.Any

    Get the maximum range AOA for the aircraft.


Method detail
-------------

































.. py:method:: validate_lift_design_points(self, d_mach_1: float, d_aoa_1: typing.Any, d_mach_2: float, d_aoa_2: typing.Any, d_mach_3: float, d_aoa_3: typing.Any, d_mach_4: float, d_aoa_4: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.validate_lift_design_points

    Validate the lift design points - ensure the choices do not result in a singular system of equations.

    :Parameters:

    **d_mach_1** : :obj:`~float`
    **d_aoa_1** : :obj:`~typing.Any`
    **d_mach_2** : :obj:`~float`
    **d_aoa_2** : :obj:`~typing.Any`
    **d_mach_3** : :obj:`~float`
    **d_aoa_3** : :obj:`~typing.Any`
    **d_mach_4** : :obj:`~float`
    **d_aoa_4** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: validate_drag_design_points(self, d_mach_1: float, d_c_l_1: float, d_mach_2: float, d_c_l_2: float, d_mach_3: float, d_c_l_3: float, d_mach_4: float, d_c_l_4: float) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.validate_drag_design_points

    Validate the drag design points - ensure the choices do not result in a singular system of equations.

    :Parameters:

    **d_mach_1** : :obj:`~float`
    **d_c_l_1** : :obj:`~float`
    **d_mach_2** : :obj:`~float`
    **d_c_l_2** : :obj:`~float`
    **d_mach_3** : :obj:`~float`
    **d_c_l_3** : :obj:`~float`
    **d_mach_4** : :obj:`~float`
    **d_c_l_4** : :obj:`~float`

    :Returns:

        :obj:`~bool`



.. py:method:: set_aoa(self, d_max_aoa: typing.Any, d_max_endurance_aoa: typing.Any, d_max_range_aoa: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.MissileFourPointAerodynamic.set_aoa

    Get or set and validates the maximum, max range and max endurance AOA values for the aircraft.

    :Parameters:

    **d_max_aoa** : :obj:`~typing.Any`
    **d_max_endurance_aoa** : :obj:`~typing.Any`
    **d_max_range_aoa** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`




