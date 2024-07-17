MissileSimpleAero
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissileSimpleAero

   Bases: 

   Class defining the simple aerodynamic options for a missile.

.. py:currentmodule:: MissileSimpleAero

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero.set_max_aoa`
              - Set whether to calculate the Angle of Attack and the corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero.s_reference`
              - Gets or sets the area of the lifting surface of the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero.cl_max`
              - Gets or sets the max coefficient of lift.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero.cd`
              - Gets or sets the coefficient of drag.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero.calculate_aoa`
              - Opt to allow Aviator to calculate the Angle of Attack. Otherwise, the value will be 0 by default.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissileSimpleAero.max_aoa`
              - Get the missile's maximum angle of attack.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissileSimpleAero


Property detail
---------------

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAero.s_reference
    :type: float

    Gets or sets the area of the lifting surface of the missile.

.. py:property:: cl_max
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAero.cl_max
    :type: float

    Gets or sets the max coefficient of lift.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAero.cd
    :type: float

    Gets or sets the coefficient of drag.

.. py:property:: calculate_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAero.calculate_aoa
    :type: bool

    Opt to allow Aviator to calculate the Angle of Attack. Otherwise, the value will be 0 by default.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAero.max_aoa
    :type: typing.Any

    Get the missile's maximum angle of attack.


Method detail
-------------









.. py:method:: set_max_aoa(self, calculateAoA: bool, maxAoA: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.MissileSimpleAero.set_max_aoa

    Set whether to calculate the Angle of Attack and the corresponding value.

    :Parameters:

    **calculateAoA** : :obj:`~bool`
    **maxAoA** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

