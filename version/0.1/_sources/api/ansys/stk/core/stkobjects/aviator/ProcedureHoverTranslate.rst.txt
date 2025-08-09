ProcedureHoverTranslate
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a hover translate procedure.

.. py:currentmodule:: ProcedureHoverTranslate

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.set_relative_course`
              - Set the relative heading change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.set_absolute_course`
              - Set the absolute heading and reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.set_final_translation_course`
              - Set the option to have the final heading to match the translation bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.altitude_options`
              - Get the altitude options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.heading_mode`
              - Get or set the heading mode for the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.final_heading_mode`
              - Get the mode to define the heading at the end of the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.absolute_course`
              - Get the absolute course for the heading.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.relative_course`
              - Get the relative heading change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.use_magnetic_heading`
              - Get the option to use a magnetic heading for the heading course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.final_heading_rate`
              - Get or set the options to define the heading rate of the aircraft at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.final_course_mode`
              - Get or set the mode to specify the final course at the end of the hover.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.smooth_translation_mode`
              - Get or set the translation mode of the aircraft at the end of the procedure.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.radius_factor`
              - Get or set the turn radius factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureHoverTranslate


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.altitude_options
    :type: HoverAltitudeOptions

    Get the altitude options.

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.heading_mode
    :type: VTOLHeadingMode

    Get or set the heading mode for the aircraft.

.. py:property:: final_heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.final_heading_mode
    :type: VTOLFinalHeadingMode

    Get the mode to define the heading at the end of the hover.

.. py:property:: absolute_course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.absolute_course
    :type: typing.Any

    Get the absolute course for the heading.

.. py:property:: relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.relative_course
    :type: typing.Any

    Get the relative heading change.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading for the heading course.

.. py:property:: final_heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.final_heading_rate
    :type: VTOLRateMode

    Get or set the options to define the heading rate of the aircraft at the end of the procedure.

.. py:property:: final_course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.final_course_mode
    :type: VTOLTranslationFinalCourseMode

    Get or set the mode to specify the final course at the end of the hover.

.. py:property:: smooth_translation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.smooth_translation_mode
    :type: VTOLRateMode

    Get or set the translation mode of the aircraft at the end of the procedure.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.radius_factor
    :type: float

    Get or set the turn radius factor.


Method detail
-------------





.. py:method:: set_relative_course(self, heading_change: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.set_relative_course

    Set the relative heading change.

    :Parameters:

        **heading_change** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: set_absolute_course(self, course: typing.Any, is_magnetic: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.set_absolute_course

    Set the absolute heading and reference.

    :Parameters:

        **course** : :obj:`~typing.Any`

        **is_magnetic** : :obj:`~bool`


    :Returns:

        :obj:`~None`

.. py:method:: set_final_translation_course(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.set_final_translation_course

    Set the option to have the final heading to match the translation bearing.

    :Returns:

        :obj:`~None`












.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureHoverTranslate.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

