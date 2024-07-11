IFuelTankInternal
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IFuelTankInternal

   object
   
   Interface used to set an aircraft's internal fuel tank.

.. py:currentmodule:: IFuelTankInternal

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.set_position`
              - Set the fuel tank's parent relative position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.name`
              - Gets or sets the name of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.capacity`
              - Gets or sets the capacity of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.consumption_order`
              - Gets or sets the consumption order of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.initial_fuel_state`
              - Gets or sets the initial fuel state of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.position_x`
              - Get the X value of the fuel tank's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.position_y`
              - Get the Y value of the fuel tank's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IFuelTankInternal.position_z`
              - Get the Z value of the fuel tank's parent relative position.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IFuelTankInternal


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.name
    :type: str

    Gets or sets the name of the fuel tank.

.. py:property:: capacity
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.capacity
    :type: float

    Gets or sets the capacity of the fuel tank.

.. py:property:: consumption_order
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.consumption_order
    :type: int

    Gets or sets the consumption order of the fuel tank.

.. py:property:: initial_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.initial_fuel_state
    :type: float

    Gets or sets the initial fuel state of the fuel tank.

.. py:property:: position_x
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.position_x
    :type: float

    Get the X value of the fuel tank's parent relative position.

.. py:property:: position_y
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.position_y
    :type: float

    Get the Y value of the fuel tank's parent relative position.

.. py:property:: position_z
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.position_z
    :type: float

    Get the Z value of the fuel tank's parent relative position.


Method detail
-------------












.. py:method:: set_position(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IFuelTankInternal.set_position

    Set the fuel tank's parent relative position.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

