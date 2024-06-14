IBasicManeuverStrategyLTAHover
==============================

.. py:class:: IBasicManeuverStrategyLTAHover

   object
   
   Interface used to access options for a Lighter than Air Hover Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~heading_mode`
            * - :py:meth:`~relative_heading`
            * - :py:meth:`~absolute_heading`
            * - :py:meth:`~use_magnetic_heading`
            * - :py:meth:`~heading_rate`
            * - :py:meth:`~altitude_mode`
            * - :py:meth:`~absolute_altitude`
            * - :py:meth:`~relative_altitude_change`
            * - :py:meth:`~control_altitude_rate`
            * - :py:meth:`~altitude_rate`
            * - :py:meth:`~parachute_area`
            * - :py:meth:`~parachute_cd`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyLTAHover


Property detail
---------------

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.heading_mode
    :type: "HOVER_HEADING_MODE"

    Gets or sets the heading mode for the lighter than air hover.

.. py:property:: relative_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.relative_heading
    :type: typing.Any

    Gets or sets the relative heading for the relative to start heading mode.

.. py:property:: absolute_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.absolute_heading
    :type: typing.Any

    Gets or sets the absolute heading for the absolute heading mode.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.use_magnetic_heading
    :type: bool

    Gets or sets the option to use a magentic heading for the absolute heading mode.

.. py:property:: heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.heading_rate
    :type: typing.Any

    Gets or sets the maximum heading rate.

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.altitude_mode
    :type: "HOVER_ALTITUDE_MODE"

    Gets or sets the altitude mode for the lighter than air hover.

.. py:property:: absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.absolute_altitude
    :type: float

    Gets or sets the absolute altitude for the Specify Altitude mode.

.. py:property:: relative_altitude_change
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.relative_altitude_change
    :type: float

    Gets or sets the relative altitude change for the Specify Altitude Change mode.

.. py:property:: control_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.control_altitude_rate
    :type: float

    Gets or sets the controlled altitude rate for the Specify Altitude or Specify Altitude Change mode.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.altitude_rate
    :type: float

    Gets or sets the altitude rate for the Specify Altitude Rate mode.

.. py:property:: parachute_area
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.parachute_area
    :type: float

    Gets or sets the parachute area for the Parachute mode.

.. py:property:: parachute_cd
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyLTAHover.parachute_cd
    :type: float

    Gets or sets the parachute drag coefficient for the Parachute mode.


