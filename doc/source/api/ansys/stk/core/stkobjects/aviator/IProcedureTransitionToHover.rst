IProcedureTransitionToHover
===========================

.. py:class:: IProcedureTransitionToHover

   object
   
   Interface used to access the options for a transition to hover procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_transition_course`
              - Set the course and heading reference.
            * - :py:meth:`~set_transition_into_wind`
              - Set the option to transition into the wind to true.
            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_reference`
            * - :py:meth:`~altitude`
            * - :py:meth:`~use_magnetic_heading`
            * - :py:meth:`~course`
            * - :py:meth:`~transition_into_wind`
            * - :py:meth:`~enroute_options`
            * - :py:meth:`~enroute_turn_direction_options`
            * - :py:meth:`~vertical_plane_options`
            * - :py:meth:`~smooth_transition_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureTransitionToHover


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.altitude_reference
    :type: AGL_MSL

    Gets or sets the altitude reference.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.altitude
    :type: float

    Gets or sets the altitude for the procedure.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.use_magnetic_heading
    :type: bool

    Gets or sets the option to use a magnetic heading for the course.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.course
    :type: typing.Any

    Gets or sets the course for the procedure.

.. py:property:: transition_into_wind
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.transition_into_wind
    :type: bool

    Gets or sets the option to transition into the wind.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.enroute_options
    :type: IAgAvtrEnrouteOptions

    Get the enroute options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.enroute_turn_direction_options
    :type: IAgAvtrEnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.vertical_plane_options
    :type: IAgAvtrVerticalPlaneAndFlightPathOptions

    Get the vertical plane options.

.. py:property:: smooth_transition_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.smooth_transition_mode
    :type: TRANSITION_TO_HOVER_MODE

    Gets or sets the transition mode of the aircraft at the end of the procedure.


Method detail
-------------








.. py:method:: set_transition_course(self, course: typing.Any, useMagneticCourse: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.set_transition_course

    Set the course and heading reference.

    :Parameters:

    **course** : :obj:`~typing.Any`
    **useMagneticCourse** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: set_transition_into_wind(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.set_transition_into_wind

    Set the option to transition into the wind to true.

    :Returns:

        :obj:`~None`






.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToHover.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

