BasicManeuverStrategyLTAHover
=============================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the lighter than air hover strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyLTAHover

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.heading_mode`
              - Get or set the heading mode for the lighter than air hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.relative_heading`
              - Get or set the relative heading for the relative to start heading mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.absolute_heading`
              - Get or set the absolute heading for the absolute heading mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.use_magnetic_heading`
              - Get or set the option to use a magentic heading for the absolute heading mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.heading_rate`
              - Get or set the maximum heading rate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.altitude_mode`
              - Get or set the altitude mode for the lighter than air hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.absolute_altitude`
              - Get or set the absolute altitude for the Specify Altitude mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.relative_altitude_change`
              - Get or set the relative altitude change for the Specify Altitude Change mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.control_altitude_rate`
              - Get or set the controlled altitude rate for the Specify Altitude or Specify Altitude Change mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.altitude_rate`
              - Get or set the altitude rate for the Specify Altitude Rate mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.parachute_area`
              - Get or set the parachute area for the Parachute mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.parachute_cd`
              - Get or set the parachute drag coefficient for the Parachute mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyLTAHover


Property detail
---------------

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.heading_mode
    :type: HoverHeadingMode

    Get or set the heading mode for the lighter than air hover.

.. py:property:: relative_heading
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.relative_heading
    :type: typing.Any

    Get or set the relative heading for the relative to start heading mode.

.. py:property:: absolute_heading
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.absolute_heading
    :type: typing.Any

    Get or set the absolute heading for the absolute heading mode.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.use_magnetic_heading
    :type: bool

    Get or set the option to use a magentic heading for the absolute heading mode.

.. py:property:: heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.heading_rate
    :type: typing.Any

    Get or set the maximum heading rate.

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.altitude_mode
    :type: HoverAltitudeMode

    Get or set the altitude mode for the lighter than air hover.

.. py:property:: absolute_altitude
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.absolute_altitude
    :type: float

    Get or set the absolute altitude for the Specify Altitude mode.

.. py:property:: relative_altitude_change
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.relative_altitude_change
    :type: float

    Get or set the relative altitude change for the Specify Altitude Change mode.

.. py:property:: control_altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.control_altitude_rate
    :type: float

    Get or set the controlled altitude rate for the Specify Altitude or Specify Altitude Change mode.

.. py:property:: altitude_rate
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.altitude_rate
    :type: float

    Get or set the altitude rate for the Specify Altitude Rate mode.

.. py:property:: parachute_area
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.parachute_area
    :type: float

    Get or set the parachute area for the Parachute mode.

.. py:property:: parachute_cd
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyLTAHover.parachute_cd
    :type: float

    Get or set the parachute drag coefficient for the Parachute mode.


