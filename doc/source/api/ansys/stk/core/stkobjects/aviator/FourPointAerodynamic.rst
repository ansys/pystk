FourPointAerodynamic
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic

   Class defining the FourPoint aerodynamic strategy.

.. py:currentmodule:: FourPointAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.validate_lift_design_points`
              - Validate the lift design points - ensure the choices do not result in a singular system of equations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.validate_drag_design_points`
              - Validate the drag design points - ensure the choices do not result in a singular system of equations.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_1`
              - Gets or sets the Mach for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_1`
              - Gets or sets the AOA for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_1`
              - Gets or sets the lift coefficient for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_1`
              - Gets or sets the drag coefficient for the first design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_2`
              - Gets or sets the Mach for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_2`
              - Gets or sets the AOA for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_2`
              - Gets or sets the lift coefficient for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_2`
              - Gets or sets the drag coefficient for the second design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_3`
              - Gets or sets the Mach for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_3`
              - Gets or sets the AOA for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_3`
              - Gets or sets the lift coefficient for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_3`
              - Gets or sets the drag coefficient for the third design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_4`
              - Gets or sets the Mach for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_4`
              - Gets or sets the AOA for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_4`
              - Gets or sets the lift coefficient for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_4`
              - Gets or sets the drag coefficient for the fourth design point.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.s_reference`
              - Gets or sets the aerodynamic reference area for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.max_aoa`
              - Gets or sets the maximum AOA for the aircraft.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import FourPointAerodynamic


Property detail
---------------

.. py:property:: mach_1
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_1
    :type: float

    Gets or sets the Mach for the first design point.

.. py:property:: a_o_a_1
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_1
    :type: typing.Any

    Gets or sets the AOA for the first design point.

.. py:property:: c_l_1
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_1
    :type: float

    Gets or sets the lift coefficient for the first design point.

.. py:property:: c_d_1
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_1
    :type: float

    Gets or sets the drag coefficient for the first design point.

.. py:property:: mach_2
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_2
    :type: float

    Gets or sets the Mach for the second design point.

.. py:property:: a_o_a_2
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_2
    :type: typing.Any

    Gets or sets the AOA for the second design point.

.. py:property:: c_l_2
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_2
    :type: float

    Gets or sets the lift coefficient for the second design point.

.. py:property:: c_d_2
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_2
    :type: float

    Gets or sets the drag coefficient for the second design point.

.. py:property:: mach_3
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_3
    :type: float

    Gets or sets the Mach for the third design point.

.. py:property:: a_o_a_3
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_3
    :type: typing.Any

    Gets or sets the AOA for the third design point.

.. py:property:: c_l_3
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_3
    :type: float

    Gets or sets the lift coefficient for the third design point.

.. py:property:: c_d_3
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_3
    :type: float

    Gets or sets the drag coefficient for the third design point.

.. py:property:: mach_4
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.mach_4
    :type: float

    Gets or sets the Mach for the fourth design point.

.. py:property:: a_o_a_4
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.a_o_a_4
    :type: typing.Any

    Gets or sets the AOA for the fourth design point.

.. py:property:: c_l_4
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_l_4
    :type: float

    Gets or sets the lift coefficient for the fourth design point.

.. py:property:: c_d_4
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.c_d_4
    :type: float

    Gets or sets the drag coefficient for the fourth design point.

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.s_reference
    :type: typing.Any

    Gets or sets the aerodynamic reference area for the aircraft.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.max_aoa
    :type: typing.Any

    Gets or sets the maximum AOA for the aircraft.


Method detail
-------------

































.. py:method:: validate_lift_design_points(self, d_mach_1: float, d_a_o_a_1: typing.Any, d_mach_2: float, d_a_o_a_2: typing.Any, d_mach_3: float, d_a_o_a_3: typing.Any, d_mach_4: float, d_a_o_a_4: typing.Any) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.validate_lift_design_points

    Validate the lift design points - ensure the choices do not result in a singular system of equations.

    :Parameters:

    **d_mach_1** : :obj:`~float`
    **d_a_o_a_1** : :obj:`~typing.Any`
    **d_mach_2** : :obj:`~float`
    **d_a_o_a_2** : :obj:`~typing.Any`
    **d_mach_3** : :obj:`~float`
    **d_a_o_a_3** : :obj:`~typing.Any`
    **d_mach_4** : :obj:`~float`
    **d_a_o_a_4** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

.. py:method:: validate_drag_design_points(self, d_mach_1: float, d_c_l_1: float, d_mach_2: float, d_c_l_2: float, d_mach_3: float, d_c_l_3: float, d_mach_4: float, d_c_l_4: float) -> bool
    :canonical: ansys.stk.core.stkobjects.aviator.FourPointAerodynamic.validate_drag_design_points

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





