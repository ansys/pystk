IAircraftAdvancedLandingModel
=============================

.. py:class:: IAircraftAdvancedLandingModel

   object
   
   Interface used to access the advanced landing model options for a landing model of an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_stall_speed_ratio`
              - Set the landing speed mode to StallSpeedRatio and specify the stall speed ratio.
            * - :py:meth:`~set_angle_of_attack`
              - Set the landing speed mode to AngleOfAttack and specify the angle of attack.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~landing_speed_mode`
            * - :py:meth:`~stall_speed_ratio`
            * - :py:meth:`~angle_of_attack`
            * - :py:meth:`~flaps`
            * - :py:meth:`~speedbrakes`
            * - :py:meth:`~braking_decel_g`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftAdvancedLandingModel


Property detail
---------------

.. py:property:: landing_speed_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedLandingModel.landing_speed_mode
    :type: "TAKEOFF_LANDING_SPEED_MODE"

    Gets or sets the mode to calculate the aircraft's speed at wheels down.

.. py:property:: stall_speed_ratio
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedLandingModel.stall_speed_ratio
    :type: float

    Get the ratio of the airspeed to the stall speed at wheels down.

.. py:property:: angle_of_attack
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedLandingModel.angle_of_attack
    :type: typing.Any

    Get the Angle of Attack at wheels down.

.. py:property:: flaps
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedLandingModel.flaps
    :type: float

    Gets or sets the extension of the flaps during the landing.

.. py:property:: speedbrakes
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedLandingModel.speedbrakes
    :type: float

    Gets or sets the extension of the speedbrakes during the landing.

.. py:property:: braking_decel_g
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftAdvancedLandingModel.braking_decel_g
    :type: float

    Gets or sets the deceleration rate, in G, when braking.


Method detail
-------------




.. py:method:: set_stall_speed_ratio(self, stallSpeedRatio:float) -> None

    Set the landing speed mode to StallSpeedRatio and specify the stall speed ratio.

    :Parameters:

    **stallSpeedRatio** : :obj:`~float`

    :Returns:

        :obj:`~None`


.. py:method:: set_angle_of_attack(self, angleOfAttack:typing.Any) -> None

    Set the landing speed mode to AngleOfAttack and specify the angle of attack.

    :Parameters:

    **angleOfAttack** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`







.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

