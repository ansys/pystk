AircraftAdvancedLandingModel
============================

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IPerformanceModel`, :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the advanced landing performance model for an Aviator aircraft.

.. py:currentmodule:: AircraftAdvancedLandingModel

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.set_stall_speed_ratio`
              - Set the landing speed mode to StallSpeedRatio and specify the stall speed ratio.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.set_angle_of_attack`
              - Set the landing speed mode to AngleOfAttack and specify the angle of attack.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.landing_speed_mode`
              - Gets or sets the mode to calculate the aircraft's speed at wheels down.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.stall_speed_ratio`
              - Get the ratio of the airspeed to the stall speed at wheels down.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.angle_of_attack`
              - Get the Angle of Attack at wheels down.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.flaps`
              - Gets or sets the extension of the flaps during the landing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.speedbrakes`
              - Gets or sets the extension of the speedbrakes during the landing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.braking_deceleration_g`
              - Gets or sets the deceleration rate, in G, when braking.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftAdvancedLandingModel


Property detail
---------------

.. py:property:: landing_speed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.landing_speed_mode
    :type: TAKEOFF_LANDING_SPEED_MODE

    Gets or sets the mode to calculate the aircraft's speed at wheels down.

.. py:property:: stall_speed_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.stall_speed_ratio
    :type: float

    Get the ratio of the airspeed to the stall speed at wheels down.

.. py:property:: angle_of_attack
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.angle_of_attack
    :type: typing.Any

    Get the Angle of Attack at wheels down.

.. py:property:: flaps
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.flaps
    :type: float

    Gets or sets the extension of the flaps during the landing.

.. py:property:: speedbrakes
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.speedbrakes
    :type: float

    Gets or sets the extension of the speedbrakes during the landing.

.. py:property:: braking_deceleration_g
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.braking_deceleration_g
    :type: float

    Gets or sets the deceleration rate, in G, when braking.


Method detail
-------------




.. py:method:: set_stall_speed_ratio(self, stall_speed_ratio: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.set_stall_speed_ratio

    Set the landing speed mode to StallSpeedRatio and specify the stall speed ratio.

    :Parameters:

    **stall_speed_ratio** : :obj:`~float`

    :Returns:

        :obj:`~None`


.. py:method:: set_angle_of_attack(self, angle_of_attack: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.set_angle_of_attack

    Set the landing speed mode to AngleOfAttack and specify the angle of attack.

    :Parameters:

    **angle_of_attack** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`







.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftAdvancedLandingModel.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

