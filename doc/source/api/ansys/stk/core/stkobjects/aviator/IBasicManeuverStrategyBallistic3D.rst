IBasicManeuverStrategyBallistic3D
=================================

.. py:class:: IBasicManeuverStrategyBallistic3D

   object
   
   Interface used to access options for a balistic 3D strategy of a basic maneuver procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~control_mode`
            * - :py:meth:`~airspeed_options`
            * - :py:meth:`~parachute_area`
            * - :py:meth:`~parachute_cd`
            * - :py:meth:`~wind_force_effective_area`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyBallistic3D


Property detail
---------------

.. py:property:: control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBallistic3D.control_mode
    :type: BALLISTIC_3D_CONTROL_MODE

    Gets or sets the control mode for the ballistic 3D strategy.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBallistic3D.airspeed_options
    :type: IAgAvtrBasicManeuverAirspeedOptions

    Get the airspeed options.

.. py:property:: parachute_area
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBallistic3D.parachute_area
    :type: float

    Gets or sets the parachute area used as part of the Parachute control mode for the ballistic 3D strategy.

.. py:property:: parachute_cd
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBallistic3D.parachute_cd
    :type: float

    Gets or sets the parachute coefficient of drag used as part of the Parachute control mode for the ballistic 3D strategy.

.. py:property:: wind_force_effective_area
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyBallistic3D.wind_force_effective_area
    :type: float

    Gets or sets the vehicle's wind force effective area.


