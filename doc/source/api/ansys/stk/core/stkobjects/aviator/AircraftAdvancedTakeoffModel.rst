AircraftAdvancedTakeoffModel
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the advanced takeoff performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftAdvancedTakeoffModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.set_stall_speed_ratio`
              - Set the takeoff speed mode to StallSpeedRatio and specify the stall speed ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.set_angle_of_attack`
              - Set the takeoff speed mode to AngleOfAttack and specify the angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.set_departure_speed_limit`
              - Set the departure speed limit of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.takeoff_speed_mode`
              - Gets or sets the mode to calculate the aircraft's airspeed upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.stall_speed_ratio`
              - Get the ratio of the airspeed to the stall speed upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.angle_of_attack`
              - Get the Angle of Attack upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.flaps`
              - Gets or sets the extension of the flaps during takeoff.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.departure_speed_mode`
              - Gets or sets the mode to calculate the airspeed upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.departure_speed_limit`
              - Get the aircraft's maximum airspeed upon leaving the ground.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.departure_speed_limit_type`
              - Get the departure speed limim type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.use_afterburner`
              - Opt whether to use the afterburner if it is possible.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAdvancedTakeoffModel


Property detail
---------------

.. py:property:: takeoff_speed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.takeoff_speed_mode
    :type: TAKEOFF_LANDING_SPEED_MODE

    Gets or sets the mode to calculate the aircraft's airspeed upon leaving the ground.

.. py:property:: stall_speed_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.stall_speed_ratio
    :type: float

    Get the ratio of the airspeed to the stall speed upon leaving the ground.

.. py:property:: angle_of_attack
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.angle_of_attack
    :type: typing.Any

    Get the Angle of Attack upon leaving the ground.

.. py:property:: flaps
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.flaps
    :type: float

    Gets or sets the extension of the flaps during takeoff.

.. py:property:: departure_speed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.departure_speed_mode
    :type: DEPARTURE_SPEED_MODE

    Gets or sets the mode to calculate the airspeed upon leaving the ground.

.. py:property:: departure_speed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.departure_speed_limit
    :type: float

    Get the aircraft's maximum airspeed upon leaving the ground.

.. py:property:: departure_speed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.departure_speed_limit_type
    :type: AIRSPEED_TYPE

    Get the departure speed limim type.

.. py:property:: use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.use_afterburner
    :type: bool

    Opt whether to use the afterburner if it is possible.


Method detail
-------------




.. py:method:: set_stall_speed_ratio(self, stall_speed_ratio: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.set_stall_speed_ratio

    Set the takeoff speed mode to StallSpeedRatio and specify the stall speed ratio.

    :Parameters:

    **stall_speed_ratio** : :obj:`~float`

    :Returns:

        :obj:`~None`


.. py:method:: set_angle_of_attack(self, angle_of_attack: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.set_angle_of_attack

    Set the takeoff speed mode to AngleOfAttack and specify the angle of attack.

    :Parameters:

    **angle_of_attack** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`







.. py:method:: set_departure_speed_limit(self, airspeed_type: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.set_departure_speed_limit

    Set the departure speed limit of the aircraft.

    :Parameters:

    **airspeed_type** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedTakeoffModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

