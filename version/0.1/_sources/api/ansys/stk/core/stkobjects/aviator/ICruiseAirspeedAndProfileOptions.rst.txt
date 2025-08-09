ICruiseAirspeedAndProfileOptions
================================

.. py:class:: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions

   Interface used to access the cruise airspeed options that also include a profile field.

.. py:currentmodule:: ICruiseAirspeedAndProfileOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.set_other_airspeed`
              - Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.cruise_speed_type`
              - Get or set the method for determining the aircraft's airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.other_airspeed_type`
              - Get the airspeed type for the other airspeed option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.other_airspeed`
              - Get the airspeed for the other airspeed option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.fly_cruise_airspeed_profile`
              - Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICruiseAirspeedAndProfileOptions


Property detail
---------------

.. py:property:: cruise_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.cruise_speed_type
    :type: CruiseSpeed

    Get or set the method for determining the aircraft's airspeed.

.. py:property:: other_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.other_airspeed_type
    :type: AirspeedType

    Get the airspeed type for the other airspeed option.

.. py:property:: other_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.other_airspeed
    :type: float

    Get the airspeed for the other airspeed option.

.. py:property:: fly_cruise_airspeed_profile
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.fly_cruise_airspeed_profile
    :type: bool

    Opt whether the aircraft immediately adopts the selected cruise airspeed or gradually begins accelerating/decelerating in the previous procedure.


Method detail
-------------





.. py:method:: set_other_airspeed(self, airspeed_type: AirspeedType, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.set_other_airspeed

    Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    :Parameters:

        **airspeed_type** : :obj:`~AirspeedType`

        **airspeed** : :obj:`~float`


    :Returns:

        :obj:`~None`



