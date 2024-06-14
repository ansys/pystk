IBasicManeuverStrategyPitch3D
=============================

.. py:class:: IBasicManeuverStrategyPitch3D

   object
   
   Interface used to access options for a pitch 3D strategy of a basic maneuver procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~control_mode`
            * - :py:meth:`~command_fpa`
            * - :py:meth:`~control_fpa_dot`
            * - :py:meth:`~stop_when_fpa_achieved`
            * - :py:meth:`~airspeed_options`
            * - :py:meth:`~wind_force_effective_area`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyPitch3D


Property detail
---------------

.. py:property:: control_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPitch3D.control_mode
    :type: "PITCH_3D_CONTROL_MODE"

    Gets or sets the control mode for the pitch 3D strategy.

.. py:property:: command_fpa
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPitch3D.command_fpa
    :type: typing.Any

    Gets or sets the commanded flight path angle.

.. py:property:: control_fpa_dot
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPitch3D.control_fpa_dot
    :type: typing.Any

    Gets or sets the flight path angle rate.

.. py:property:: stop_when_fpa_achieved
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPitch3D.stop_when_fpa_achieved
    :type: bool

    Stop when the commanded flight path angle is achieved.

.. py:property:: airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPitch3D.airspeed_options
    :type: "IAgAvtrBasicManeuverAirspeedOptions"

    Get the airspeed options.

.. py:property:: wind_force_effective_area
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyPitch3D.wind_force_effective_area
    :type: float

    Gets or sets the vehicle's wind force effective area.


