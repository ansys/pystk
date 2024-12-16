ProcedureHover
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureHover

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a hover procedure.

.. py:currentmodule:: ProcedureHover

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.set_relative_course`
              - Set the relative heading change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.set_absolute_course`
              - Set the absolute heading and reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.set_final_translation_course`
              - Set the option to have the final heading to match the translation bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.hover_mode`
              - Gets or sets the option to have the aircraft hover in place for a fixed time or to perform a hovering maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.fixed_time`
              - Gets or sets the time to hover in place.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.heading_mode`
              - Gets or sets the heading mode for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.final_heading_mode`
              - Get the mode to define the heading at the end of the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.absolute_course`
              - Get the absolute course for the heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.relative_course`
              - Get the relative heading change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.use_magnetic_heading`
              - Get the option to use a magnetic heading for the heading course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.final_heading_rate`
              - Gets or sets the options to define the heading rate of the aircraft at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.translation_mode`
              - Define how the aircraft will translate during the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.bearing`
              - Gets or sets the bearing of the translation during the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.use_magnetic_bearing`
              - Gets or sets the option to use a magnetic heading for the translation bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.range`
              - Gets or sets the range to translate during the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.final_course_mode`
              - Gets or sets the mode to specify the final course at the end of the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.smooth_translation_mode`
              - Gets or sets the translation mode of the aircraft at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHover.radius_factor`
              - Gets or sets the turn radius factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureHover


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.altitude_options
    :type: HoverAltitudeOptions

    Get the altitude options.

.. py:property:: hover_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.hover_mode
    :type: HoverMode

    Gets or sets the option to have the aircraft hover in place for a fixed time or to perform a hovering maneuver.

.. py:property:: fixed_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.fixed_time
    :type: typing.Any

    Gets or sets the time to hover in place.

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.heading_mode
    :type: VTOLHeadingMode

    Gets or sets the heading mode for the aircraft.

.. py:property:: final_heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.final_heading_mode
    :type: VTOLFinalHeadingMode

    Get the mode to define the heading at the end of the hover.

.. py:property:: absolute_course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.absolute_course
    :type: typing.Any

    Get the absolute course for the heading.

.. py:property:: relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.relative_course
    :type: typing.Any

    Get the relative heading change.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading for the heading course.

.. py:property:: final_heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.final_heading_rate
    :type: VTOLRateMode

    Gets or sets the options to define the heading rate of the aircraft at the end of the procedure.

.. py:property:: translation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.translation_mode
    :type: VTOLTranslationMode

    Define how the aircraft will translate during the hover.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.bearing
    :type: typing.Any

    Gets or sets the bearing of the translation during the hover.

.. py:property:: use_magnetic_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.use_magnetic_bearing
    :type: bool

    Gets or sets the option to use a magnetic heading for the translation bearing.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.range
    :type: float

    Gets or sets the range to translate during the hover.

.. py:property:: final_course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.final_course_mode
    :type: VTOLTranslationFinalCourseMode

    Gets or sets the mode to specify the final course at the end of the hover.

.. py:property:: smooth_translation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.smooth_translation_mode
    :type: VTOLRateMode

    Gets or sets the translation mode of the aircraft at the end of the procedure.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.radius_factor
    :type: float

    Gets or sets the turn radius factor.


Method detail
-------------









.. py:method:: set_relative_course(self, heading_change: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.set_relative_course

    Set the relative heading change.

    :Parameters:

    **heading_change** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_absolute_course(self, course: typing.Any, is_magnetic: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.set_absolute_course

    Set the absolute heading and reference.

    :Parameters:

    **course** : :obj:`~typing.Any`
    **is_magnetic** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: set_final_translation_course(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.set_final_translation_course

    Set the option to have the final heading to match the translation bearing.

    :Returns:

        :obj:`~None`




















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHover.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

