IProcedureTransitionToForwardFlight
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight

   object
   
   Interface used to access the options for a transition to forward flight procedure.

.. py:currentmodule:: IProcedureTransitionToForwardFlight

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.set_transition_into_wind`
              - Set the option to transition into the wind to true.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.set_absolute_course`
              - Set the mode to absolute and specify the course and heading reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.set_relative_course`
              - Set the mode to relative and specify the heading change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.transition_course_mode`
              - Get the mode to specify the course of the transition maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.use_magnetic_heading`
              - Get the option to use a magnetic heading for the course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.absolute_course`
              - Get the absolute course for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.relative_course`
              - Get the relative course for the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.flight_path_angle`
              - Gets or sets the pitch angle of the flight path at the end of the procedure.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureTransitionToForwardFlight


Property detail
---------------

.. py:property:: transition_course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.transition_course_mode
    :type: VTOL_TRANSITION_MODE

    Get the mode to specify the course of the transition maneuver.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading for the course.

.. py:property:: absolute_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.absolute_course
    :type: typing.Any

    Get the absolute course for the procedure.

.. py:property:: relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.relative_course
    :type: typing.Any

    Get the relative course for the procedure.

.. py:property:: flight_path_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.flight_path_angle
    :type: typing.Any

    Gets or sets the pitch angle of the flight path at the end of the procedure.


Method detail
-------------


.. py:method:: set_transition_into_wind(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.set_transition_into_wind

    Set the option to transition into the wind to true.

    :Returns:

        :obj:`~None`

.. py:method:: set_absolute_course(self, course: typing.Any, useMagneticCourse: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.set_absolute_course

    Set the mode to absolute and specify the course and heading reference.

    :Parameters:

    **course** : :obj:`~typing.Any`
    **useMagneticCourse** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: set_relative_course(self, headingChange: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.set_relative_course

    Set the mode to relative and specify the heading change.

    :Parameters:

    **headingChange** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`






.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTransitionToForwardFlight.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

