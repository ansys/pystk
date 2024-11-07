PropulsionThrust
================

.. py:class:: ansys.stk.core.stkobjects.aviator.PropulsionThrust

   Class defining the the thrust propulsion used in basic maneuver procedures.

.. py:currentmodule:: PropulsionThrust

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.set_min_airspeed`
              - Set the min airspeed type and value for a thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.set_max_airspeed`
              - Set the max airspeed type and value for a thrust model.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.use_constant_thrust`
              - Gets or sets the option to use a constant thrust for a thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.constant_thrust`
              - Gets or sets the constant thrust value for a thrust model set to Constant Thrust mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.boost_thrust`
              - Gets or sets the boost thrust value for a thrust model set to Boost/Sustain Thrust mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.boost_thrust_time_limit`
              - Gets or sets the boost thrust time limit for a thrust model set to Boost/Sustain Thrust mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.sustain_thrust`
              - Gets or sets the sustain thrust value for a thrust model set to Boost/Sustain Thrust mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.sustain_thrust_time_limit`
              - Gets or sets the sustain thrust time limit for a thrust model set to Boost/Sustain Thrust mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.min_airspeed_type`
              - Get the min airspeed type for a thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.min_airspeed`
              - Get the min airspeed for a thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.max_airspeed_type`
              - Get the max airspeed type for a thrust model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PropulsionThrust.max_airspeed`
              - Get the max airspeed for a thrust model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import PropulsionThrust


Property detail
---------------

.. py:property:: use_constant_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.use_constant_thrust
    :type: bool

    Gets or sets the option to use a constant thrust for a thrust model.

.. py:property:: constant_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.constant_thrust
    :type: float

    Gets or sets the constant thrust value for a thrust model set to Constant Thrust mode.

.. py:property:: boost_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.boost_thrust
    :type: float

    Gets or sets the boost thrust value for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: boost_thrust_time_limit
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.boost_thrust_time_limit
    :type: float

    Gets or sets the boost thrust time limit for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: sustain_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.sustain_thrust
    :type: float

    Gets or sets the sustain thrust value for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: sustain_thrust_time_limit
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.sustain_thrust_time_limit
    :type: float

    Gets or sets the sustain thrust time limit for a thrust model set to Boost/Sustain Thrust mode.

.. py:property:: min_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.min_airspeed_type
    :type: AIRSPEED_TYPE

    Get the min airspeed type for a thrust model.

.. py:property:: min_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.min_airspeed
    :type: float

    Get the min airspeed for a thrust model.

.. py:property:: max_airspeed_type
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.max_airspeed_type
    :type: AIRSPEED_TYPE

    Get the max airspeed type for a thrust model.

.. py:property:: max_airspeed
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.max_airspeed
    :type: float

    Get the max airspeed for a thrust model.


Method detail
-------------















.. py:method:: set_min_airspeed(self, airspeed_type: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.set_min_airspeed

    Set the min airspeed type and value for a thrust model.

    :Parameters:

    **airspeed_type** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`



.. py:method:: set_max_airspeed(self, airspeed_type: AIRSPEED_TYPE, airspeed: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PropulsionThrust.set_max_airspeed

    Set the max airspeed type and value for a thrust model.

    :Parameters:

    **airspeed_type** : :obj:`~AIRSPEED_TYPE`
    **airspeed** : :obj:`~float`

    :Returns:

        :obj:`~None`

