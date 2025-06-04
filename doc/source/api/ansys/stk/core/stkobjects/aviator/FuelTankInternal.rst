FuelTankInternal
================

.. py:class:: ansys.stk.core.stkobjects.aviator.FuelTankInternal

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IStation`

   Class defining an internal fuel tank for an Aviator aircraft.

.. py:currentmodule:: FuelTankInternal

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.set_position`
              - Set the fuel tank's parent relative position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.name`
              - Get or set the name of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.capacity`
              - Get or set the capacity of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.consumption_order`
              - Get or set the consumption order of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.initial_fuel_state`
              - Get or set the initial fuel state of the fuel tank.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.position_x`
              - Get the X value of the fuel tank's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.position_y`
              - Get the Y value of the fuel tank's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.FuelTankInternal.position_z`
              - Get the Z value of the fuel tank's parent relative position.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import FuelTankInternal


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.name
    :type: str

    Get or set the name of the fuel tank.

.. py:property:: capacity
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.capacity
    :type: float

    Get or set the capacity of the fuel tank.

.. py:property:: consumption_order
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.consumption_order
    :type: int

    Get or set the consumption order of the fuel tank.

.. py:property:: initial_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.initial_fuel_state
    :type: float

    Get or set the initial fuel state of the fuel tank.

.. py:property:: position_x
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.position_x
    :type: float

    Get the X value of the fuel tank's parent relative position.

.. py:property:: position_y
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.position_y
    :type: float

    Get the Y value of the fuel tank's parent relative position.

.. py:property:: position_z
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.position_z
    :type: float

    Get the Z value of the fuel tank's parent relative position.


Method detail
-------------












.. py:method:: set_position(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.FuelTankInternal.set_position

    Set the fuel tank's parent relative position.

    :Parameters:

        **x** : :obj:`~float`

        **y** : :obj:`~float`

        **z** : :obj:`~float`


    :Returns:

        :obj:`~None`

