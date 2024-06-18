IAircraftAdvancedTakeoffModel
=============================

.. py:class:: IAircraftAdvancedTakeoffModel

   object
   
   Interface used to access the advanced takeoff model options for a takeoff model of an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_stall_speed_ratio`
              - Set the takeoff speed mode to StallSpeedRatio and specify the stall speed ratio.
            * - :py:meth:`~set_angle_of_attack`
              - Set the takeoff speed mode to AngleOfAttack and specify the angle of attack.
            * - :py:meth:`~set_departure_speed_limit`
              - Set the departure speed limit of the aircraft.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~takeoff_speed_mode`
            * - :py:meth:`~stall_speed_ratio`
            * - :py:meth:`~angle_of_attack`
            * - :py:meth:`~flaps`
            * - :py:meth:`~departure_speed_mode`
            * - :py:meth:`~departure_speed_limit`
            * - :py:meth:`~departure_speed_limit_type`
            * - :py:meth:`~use_afterburner`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedTakeoffModel


Property detail
---------------

.. py:property:: takeoff_speed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.takeoff_speed_mode
    :type: "TAKEOFF_LANDING_SPEED_MODE"

    Gets or sets the mode to calculate the aircraft's airspeed upon leaving the ground.

.. py:property:: stall_speed_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.stall_speed_ratio
    :type: float

    Get the ratio of the airspeed to the stall speed upon leaving the ground.

.. py:property:: angle_of_attack
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.angle_of_attack
    :type: typing.Any

    Get the Angle of Attack upon leaving the ground.

.. py:property:: flaps
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.flaps
    :type: float

    Gets or sets the extension of the flaps during takeoff.

.. py:property:: departure_speed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.departure_speed_mode
    :type: "DEPARTURE_SPEED_MODE"

    Gets or sets the mode to calculate the airspeed upon leaving the ground.

.. py:property:: departure_speed_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.departure_speed_limit
    :type: float

    Get the aircraft's maximum airspeed upon leaving the ground.

.. py:property:: departure_speed_limit_type
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.departure_speed_limit_type
    :type: "AIRSPEED_TYPE"

    Get the departure speed limim type.

.. py:property:: use_afterburner
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedTakeoffModel.use_afterburner
    :type: bool

    Opt whether to use the afterburner if it is possible.


Method detail
-------------




.. py:method:: set_stall_speed_ratio(self, stallSpeedRatio:float) -> None

    Set the takeoff speed mode to StallSpeedRatio and specify the stall speed ratio.

    :Parameters:

    **stallSpeedRatio** : :obj:`~float`

    :Returns:

        :obj:`~None`


.. py:method:: set_angle_of_attack(self, angleOfAttack:typing.Any) -> None

    Set the takeoff speed mode to AngleOfAttack and specify the angle of attack.

    :Parameters:

    **angleOfAttack** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`







.. py:method:: set_departure_speed_limit(self, airspeedType:"AIRSPEED_TYPE", aispeed:float) -> None

    Set the departure speed limit of the aircraft.

    :Parameters:

    **airspeedType** : :obj:`~"AIRSPEED_TYPE"`
    **aispeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

