PayloadStation
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.PayloadStation

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IStation`

   Class defining a payload station for an Aviator aircraft.

.. py:currentmodule:: PayloadStation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.set_position`
              - Set the payload station's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.remove_sub_item`
              - Remove any sub item that may be attached to the payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.add_external_fuel_tank`
              - Add an external fuel tank to the payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.get_external_fuel_tank`
              - Get the external fuel tank attached to the payload station.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.name`
              - Get or set the name of the payload station.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.position_x`
              - Get the X value of the payload station's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.position_y`
              - Get the Y value of the payload station's parent relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PayloadStation.position_z`
              - Get the Z value of the payload station's parent relative position.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import PayloadStation


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.name
    :type: str

    Get or set the name of the payload station.

.. py:property:: position_x
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.position_x
    :type: float

    Get the X value of the payload station's parent relative position.

.. py:property:: position_y
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.position_y
    :type: float

    Get the Y value of the payload station's parent relative position.

.. py:property:: position_z
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.position_z
    :type: float

    Get the Z value of the payload station's parent relative position.


Method detail
-------------






.. py:method:: set_position(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.set_position

    Set the payload station's parent relative position.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_sub_item(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.remove_sub_item

    Remove any sub item that may be attached to the payload station.

    :Returns:

        :obj:`~None`

.. py:method:: add_external_fuel_tank(self) -> FuelTankExternal
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.add_external_fuel_tank

    Add an external fuel tank to the payload station.

    :Returns:

        :obj:`~FuelTankExternal`

.. py:method:: get_external_fuel_tank(self) -> FuelTankExternal
    :canonical: ansys.stk.core.stkobjects.aviator.PayloadStation.get_external_fuel_tank

    Get the external fuel tank attached to the payload station.

    :Returns:

        :obj:`~FuelTankExternal`

