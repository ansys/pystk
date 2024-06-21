IProcedureLanding
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureLanding

   object
   
   Interface used to access the options for a landing procedure.

.. py:currentmodule:: IProcedureLanding

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.mode_as_standard_instrument_approach`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.mode_as_intercept_glideslope`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.mode_as_enter_downwind_pattern`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.runway_heading_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.enroute_cruise_airspeed_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.enroute_turn_direction_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.enroute_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.vertical_plane_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureLanding.approach_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureLanding


Property detail
---------------

.. py:property:: mode_as_standard_instrument_approach
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.mode_as_standard_instrument_approach
    :type: ILandingStandardInstrumentApproach

    Get the interface for a standard instrument approach landing.

.. py:property:: mode_as_intercept_glideslope
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.mode_as_intercept_glideslope
    :type: ILandingInterceptGlideslope

    Get the interface for an intercept glideslope landing.

.. py:property:: mode_as_enter_downwind_pattern
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.mode_as_enter_downwind_pattern
    :type: ILandingEnterDownwindPattern

    Get the interface for a downwind pattern landing.

.. py:property:: runway_heading_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.runway_heading_options
    :type: IRunwayHeadingOptions

    Get the runway heading options.

.. py:property:: enroute_cruise_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.enroute_cruise_airspeed_options
    :type: ICruiseAirspeedAndProfileOptions

    Get the enroute cruise airspeed options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.enroute_turn_direction_options
    :type: IEnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.enroute_options
    :type: IEnrouteAndDelayOptions

    Get the enroute options.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.vertical_plane_options
    :type: IVerticalPlaneOptions

    Get the vertical plane options.

.. py:property:: approach_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.approach_mode
    :type: APPROACH_MODE

    Gets or sets the type of landing the aircraft will perform.


Method detail
-------------











.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureLanding.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

