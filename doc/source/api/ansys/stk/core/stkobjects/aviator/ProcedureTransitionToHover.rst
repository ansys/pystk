ProcedureTransitionToHover
==========================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a transition to hover procedure.

.. py:currentmodule:: ProcedureTransitionToHover

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.set_transition_course`
              - Set the course and heading reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.set_transition_into_wind`
              - Set the option to transition into the wind to true.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.altitude_reference`
              - Get or set the altitude reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.altitude`
              - Get or set the altitude for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.use_magnetic_heading`
              - Get or set the option to use a magnetic heading for the course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.course`
              - Get or set the course for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.transition_into_wind`
              - Get or set the option to transition into the wind.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.enroute_options`
              - Get the enroute options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.enroute_turn_direction_options`
              - Get the enroute turn direction options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.vertical_plane_options`
              - Get the vertical plane options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.smooth_transition_mode`
              - Get or set the transition mode of the aircraft at the end of the procedure.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureTransitionToHover


Property detail
---------------

.. py:property:: altitude_reference
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.altitude_reference
    :type: AGLMSL

    Get or set the altitude reference.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.altitude
    :type: float

    Get or set the altitude for the procedure.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.use_magnetic_heading
    :type: bool

    Get or set the option to use a magnetic heading for the course.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.course
    :type: typing.Any

    Get or set the course for the procedure.

.. py:property:: transition_into_wind
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.transition_into_wind
    :type: bool

    Get or set the option to transition into the wind.

.. py:property:: enroute_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.enroute_options
    :type: EnrouteOptions

    Get the enroute options.

.. py:property:: enroute_turn_direction_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.enroute_turn_direction_options
    :type: EnrouteTurnDirectionOptions

    Get the enroute turn direction options.

.. py:property:: vertical_plane_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.vertical_plane_options
    :type: VerticalPlaneAndFlightPathOptions

    Get the vertical plane options.

.. py:property:: smooth_transition_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.smooth_transition_mode
    :type: TransitionToHoverMode

    Get or set the transition mode of the aircraft at the end of the procedure.


Method detail
-------------








.. py:method:: set_transition_course(self, course: typing.Any, use_magnetic_course: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.set_transition_course

    Set the course and heading reference.

    :Parameters:

    **course** : :obj:`~typing.Any`
    **use_magnetic_course** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: set_transition_into_wind(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.set_transition_into_wind

    Set the option to transition into the wind to true.

    :Returns:

        :obj:`~None`






.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTransitionToHover.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

