AdvancedFixedWingFourPointAerodynamic
=====================================

.. py:class:: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic

   Class defining the FourPoint aerodynamic strategy in the Advanced Fixed Wing Tool.

.. py:currentmodule:: AdvancedFixedWingFourPointAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.validate_lift_design_points`
              - Validate the lift design points - ensure the choices do not result in a singular system of equations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.validate_drag_design_points`
              - Validate the drag design points - ensure the choices do not result in a singular system of equations.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.max_aoa`
              - Get or set the maximum AOA for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_1`
              - Get or set the Mach for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_1`
              - Get or set the AOA for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_1`
              - Get or set the lift coefficient for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_1`
              - Get or set the drag coefficient for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_2`
              - Get or set the Mach for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_2`
              - Get or set the AOA for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_2`
              - Get or set the lift coefficient for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_2`
              - Get or set the drag coefficient for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_3`
              - Get or set the Mach for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_3`
              - Get or set the AOA for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_3`
              - Get or set the lift coefficient for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_3`
              - Get or set the drag coefficient for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_4`
              - Get or set the Mach for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_4`
              - Get or set the AOA for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_4`
              - Get or set the lift coefficient for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_4`
              - Get or set the drag coefficient for the fourth design point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AdvancedFixedWingFourPointAerodynamic


Property detail
---------------

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.max_aoa
    :type: typing.Any

    Get or set the maximum AOA for the aircraft.

.. py:property:: mach_1
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_1
    :type: float

    Get or set the Mach for the first design point.

.. py:property:: aoa_1
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_1
    :type: typing.Any

    Get or set the AOA for the first design point.

.. py:property:: cl_1
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_1
    :type: float

    Get or set the lift coefficient for the first design point.

.. py:property:: cd_1
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_1
    :type: float

    Get or set the drag coefficient for the first design point.

.. py:property:: mach_2
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_2
    :type: float

    Get or set the Mach for the second design point.

.. py:property:: aoa_2
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_2
    :type: typing.Any

    Get or set the AOA for the second design point.

.. py:property:: cl_2
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_2
    :type: float

    Get or set the lift coefficient for the second design point.

.. py:property:: cd_2
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_2
    :type: float

    Get or set the drag coefficient for the second design point.

.. py:property:: mach_3
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_3
    :type: float

    Get or set the Mach for the third design point.

.. py:property:: aoa_3
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_3
    :type: typing.Any

    Get or set the AOA for the third design point.

.. py:property:: cl_3
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_3
    :type: float

    Get or set the lift coefficient for the third design point.

.. py:property:: cd_3
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_3
    :type: float

    Get or set the drag coefficient for the third design point.

.. py:property:: mach_4
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.mach_4
    :type: float

    Get or set the Mach for the fourth design point.

.. py:property:: aoa_4
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.aoa_4
    :type: typing.Any

    Get or set the AOA for the fourth design point.

.. py:property:: cl_4
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cl_4
    :type: float

    Get or set the lift coefficient for the fourth design point.

.. py:property:: cd_4
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.cd_4
    :type: float

    Get or set the drag coefficient for the fourth design point.


Method detail
-------------



































.. py:method:: validate_lift_design_points(self, d_mach_1: float, d_aoa_1: typing.Any, d_mach_2: float, d_aoa_2: typing.Any, d_mach_3: float, d_aoa_3: typing.Any, d_mach_4: float, d_aoa_4: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.validate_lift_design_points

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
    :canonical: ansys.stk.core.stkobjects.aviator.AdvancedFixedWingFourPointAerodynamic.validate_drag_design_points

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

