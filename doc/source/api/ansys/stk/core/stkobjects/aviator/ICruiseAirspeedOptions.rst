ICruiseAirspeedOptions
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions

   object
   
   Interface used to access the Cruise Airspeed options for an Aviator procedure.

.. py:currentmodule:: ICruiseAirspeedOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.set_other_airspeed`
              - Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.cruise_speed_type`
              - Gets or sets the method for determining the aircraft's airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.other_airspeed_type`
              - Get the airspeed type for the other airspeed option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.other_airspeed`
              - Get the airspeed for the other airspeed option.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ICruiseAirspeedOptions


Property detail
---------------

.. py:property:: cruise_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.cruise_speed_type
    :type: CRUISE_SPEED

    Gets or sets the method for determining the aircraft's airspeed.

.. py:property:: other_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.other_airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type for the other airspeed option.

.. py:property:: other_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.other_airspeed
    :type: float

    Get the airspeed for the other airspeed option.


Method detail
-------------





.. py:method:: set_other_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ICruiseAirspeedOptions.set_other_airspeed

    Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`

