CruiseAirspeedOptions
=====================

.. py:class:: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions

   Class defining the cruise airspeed options in a procedure.

.. py:currentmodule:: CruiseAirspeedOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.set_other_airspeed`
              - Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.cruise_speed_type`
              - Gets or sets the method for determining the aircraft's airspeed.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed_type`
              - Get the airspeed type for the other airspeed option.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed`
              - Get the airspeed for the other airspeed option.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import CruiseAirspeedOptions


Property detail
---------------

.. py:property:: cruise_speed_type
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.cruise_speed_type
    :type: CRUISE_SPEED

    Gets or sets the method for determining the aircraft's airspeed.

.. py:property:: other_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed_type
    :type: AIRSPEED_TYPE

    Get the airspeed type for the other airspeed option.

.. py:property:: other_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.other_airspeed
    :type: float

    Get the airspeed for the other airspeed option.


Method detail
-------------





.. py:method:: set_other_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.CruiseAirspeedOptions.set_other_airspeed

    Set the cruise airspeed. This option is only enabled if the cruise speed type is set to other.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`

