ICruiseAirspeedAndProfileOptions
================================

.. py:class:: ICruiseAirspeedAndProfileOptions

   object
   
   Interface used to access the cruise airspeed options that also include a profile field.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_other_airspeed`
              - Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~cruise_speed_type`
            * - :py:meth:`~other_airspeed_type`
            * - :py:meth:`~other_airspeed`
            * - :py:meth:`~fly_cruise_airspeed_profile`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICruiseAirspeedAndProfileOptions


Property detail
---------------

.. py:property:: cruise_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.cruise_speed_type
    :type: CRUISE_SPEED

    Gets or sets the method for determining the aircraft's airspeed.

.. py:property:: other_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.other_airspeed_type
    :type: AIRSPEED_TYPE

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





.. py:method:: set_other_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedAndProfileOptions.set_other_airspeed

    Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



