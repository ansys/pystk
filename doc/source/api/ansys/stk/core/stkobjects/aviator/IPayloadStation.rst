IPayloadStation
===============

.. py:class:: IPayloadStation

   object
   
   Interface used to set an aircraft's payload station.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_position`
              - Set the payload station's parent relative position.
            * - :py:meth:`~remove_sub_item`
              - Remove any sub item that may be attached to the payload station.
            * - :py:meth:`~add_external_fuel_tank`
              - Add an external fuel tank to the payload station.
            * - :py:meth:`~get_external_fuel_tank`
              - Get the external fuel tank attached to the payload station.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~position_x`
            * - :py:meth:`~position_y`
            * - :py:meth:`~position_z`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPayloadStation


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.name
    :type: str

    Gets or sets the name of the payload station.

.. py:property:: position_x
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.position_x
    :type: float

    Get the X value of the payload station's parent relative position.

.. py:property:: position_y
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.position_y
    :type: float

    Get the Y value of the payload station's parent relative position.

.. py:property:: position_z
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.position_z
    :type: float

    Get the Z value of the payload station's parent relative position.


Method detail
-------------






.. py:method:: set_position(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.set_position

    Set the payload station's parent relative position.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: remove_sub_item(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.remove_sub_item

    Remove any sub item that may be attached to the payload station.

    :Returns:

        :obj:`~None`

.. py:method:: add_external_fuel_tank(self) -> IFuelTankExternal
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.add_external_fuel_tank

    Add an external fuel tank to the payload station.

    :Returns:

        :obj:`~IFuelTankExternal`

.. py:method:: get_external_fuel_tank(self) -> IFuelTankExternal
    :canonical: ansys.stk.core.stkobjects.aviator.IPayloadStation.get_external_fuel_tank

    Get the external fuel tank attached to the payload station.

    :Returns:

        :obj:`~IFuelTankExternal`

