IMissileSimpleAero
==================

.. py:class:: IMissileSimpleAero

   object
   
   Interface used to access the Simple aerodynamics options for a missile.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_max_aoa`
              - Set whether to calculate the Angle of Attack and the corresponding value.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~s_reference`
            * - :py:meth:`~cl_max`
            * - :py:meth:`~cd`
            * - :py:meth:`~calculate_aoa`
            * - :py:meth:`~max_aoa`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileSimpleAero


Property detail
---------------

.. py:property:: s_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleAero.s_reference
    :type: float

    Gets or sets the area of the lifting surface of the missile.

.. py:property:: cl_max
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleAero.cl_max
    :type: float

    Gets or sets the max coefficient of lift.

.. py:property:: cd
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleAero.cd
    :type: float

    Gets or sets the coefficient of drag.

.. py:property:: calculate_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleAero.calculate_aoa
    :type: bool

    Opt to allow Aviator to calculate the Angle of Attack. Otherwise, the value will be 0 by default.

.. py:property:: max_aoa
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleAero.max_aoa
    :type: typing.Any

    Get the missile's maximum angle of attack.


Method detail
-------------









.. py:method:: set_max_aoa(self, calculateAoA:bool, maxAoA:typing.Any) -> None

    Set whether to calculate the Angle of Attack and the corresponding value.

    :Parameters:

    **calculateAoA** : :obj:`~bool`
    **maxAoA** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

