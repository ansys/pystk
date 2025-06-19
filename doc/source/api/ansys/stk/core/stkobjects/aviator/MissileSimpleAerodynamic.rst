MissileSimpleAerodynamic
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic

   Class defining the simple aerodynamic options for a missile.

.. py:currentmodule:: MissileSimpleAerodynamic

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.set_max_aoa`
              - Set whether to calculate the Angle of Attack and the corresponding value.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.s_reference`
              - Get or set the area of the lifting surface of the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.cl_max`
              - Get or set the max coefficient of lift.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.cd`
              - Get or set the coefficient of drag.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.calculate_aoa`
              - Opt to allow Aviator to calculate the Angle of Attack. Otherwise, the value will be 0 by default.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.max_aoa`
              - Get the missile's maximum angle of attack.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileSimpleAerodynamic


Property detail
---------------

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.s_reference
    :type: float

    Get or set the area of the lifting surface of the missile.

.. py:property:: cl_max
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.cl_max
    :type: float

    Get or set the max coefficient of lift.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.cd
    :type: float

    Get or set the coefficient of drag.

.. py:property:: calculate_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.calculate_aoa
    :type: bool

    Opt to allow Aviator to calculate the Angle of Attack. Otherwise, the value will be 0 by default.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.max_aoa
    :type: typing.Any

    Get the missile's maximum angle of attack.


Method detail
-------------









.. py:method:: set_max_aoa(self, calculate_aoa: bool, max_aoa: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAerodynamic.set_max_aoa

    Set whether to calculate the Angle of Attack and the corresponding value.

    :Parameters:

        **calculate_aoa** : :obj:`~bool`

        **max_aoa** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

