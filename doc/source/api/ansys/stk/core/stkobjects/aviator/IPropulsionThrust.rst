IPropulsionThrust
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IPropulsionThrust

   object
   
   Interface used to access propulsion thrust for basic maneuver strategies.

.. py:currentmodule:: IPropulsionThrust

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.set_min_airspeed`
              - Set the min airspeed type and value for a thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.set_max_airspeed`
              - Set the max airspeed type and value for a thrust model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.use_constant_thrust`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.constant_thrust`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.boost_thrust`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.boost_thrust_time_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.sustain_thrust`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.sustain_thrust_time_limit`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.min_airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.min_airspeed`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.max_airspeed_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPropulsionThrust.max_airspeed`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPropulsionThrust


Property detail
---------------

.. py:property:: use_constant_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.use_constant_thrust
    :type: bool

    Gets or sets the option to use a constant thrust for a thrust model.

.. py:property:: constant_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.constant_thrust
    :type: float

    Gets or sets the constant thrust value for a thrust model set to Constant Thrust mode.

.. py:property:: boost_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.boost_thrust
    :type: float

    Gets or sets the boost thrust value for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: boost_thrust_time_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.boost_thrust_time_limit
    :type: float

    Gets or sets the boost thrust time limit for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: sustain_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.sustain_thrust
    :type: float

    Gets or sets the sustain thrust value for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: sustain_thrust_time_limit
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.sustain_thrust_time_limit
    :type: float

    Gets or sets the sustain thrust time limit for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: min_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.min_airspeed_type
    :type: AIRSPEED_TYPE

    Get the min airspeed type for a thrust model.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.min_airspeed
    :type: float

    Get the min airspeed for a thrust model.

.. py:property:: max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.max_airspeed_type
    :type: AIRSPEED_TYPE

    Get the max airspeed type for a thrust model.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.max_airspeed
    :type: float

    Get the max airspeed for a thrust model.


Method detail
-------------















.. py:method:: set_min_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.set_min_airspeed

    Set the min airspeed type and value for a thrust model.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_airspeed(self, airspeedType: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPropulsionThrust.set_max_airspeed

    Set the max airspeed type and value for a thrust model.

    :Parameters:

    **airspeedType** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`

