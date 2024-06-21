IProcedureHover
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureHover

   object
   
   Interface used to access the options for a hover procedure.

.. py:currentmodule:: IProcedureHover

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.set_relative_course`
              - Set the relative heading change.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.set_absolute_course`
              - Set the absolute heading and reference.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.set_final_translation_course`
              - Set the option to have the final heading to match the translation bearing.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.altitude_options`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.hover_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.fixed_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.heading_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.final_heading_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.absolute_course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.relative_course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.use_magnetic_heading`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.final_heading_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.translation_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.use_magnetic_bearing`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.final_course_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.smooth_translation_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureHover.radius_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureHover


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.altitude_options
    :type: IHoverAltitudeOptions

    Get the altitude options.

.. py:property:: hover_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.hover_mode
    :type: HOVER_MODE

    Gets or sets the option to have the aircraft hover in place for a fixed time or to perform a hovering maneuver.

.. py:property:: fixed_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.fixed_time
    :type: typing.Any

    Gets or sets the time to hover in place.

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.heading_mode
    :type: VTOL_HEADING_MODE

    Gets or sets the heading mode for the aircraft.

.. py:property:: final_heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.final_heading_mode
    :type: VTOL_FINAL_HEADING_MODE

    Get the mode to define the heading at the end of the hover.

.. py:property:: absolute_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.absolute_course
    :type: typing.Any

    Get the absolute course for the heading.

.. py:property:: relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.relative_course
    :type: typing.Any

    Get the relative heading change.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading for the heading course.

.. py:property:: final_heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.final_heading_rate
    :type: VTOL_RATE_MODE

    Gets or sets the options to define the heading rate of the aircraft at the end of the procedure.

.. py:property:: translation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.translation_mode
    :type: VTOL_TRANSLATION_MODE

    Define how the aircraft will translate during the hover.

.. py:property:: bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.bearing
    :type: typing.Any

    Gets or sets the bearing of the translation during the hover.

.. py:property:: use_magnetic_bearing
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.use_magnetic_bearing
    :type: bool

    Gets or sets the option to use a magnetic heading for the translation bearing.

.. py:property:: range
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.range
    :type: float

    Gets or sets the range to translate during the hover.

.. py:property:: final_course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.final_course_mode
    :type: VTOL_TRANSLATION_FINAL_COURSE_MODE

    Gets or sets the mode to specify the final course at the end of the hover.

.. py:property:: smooth_translation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.smooth_translation_mode
    :type: VTOL_RATE_MODE

    Gets or sets the translation mode of the aircraft at the end of the procedure.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.radius_factor
    :type: float

    Gets or sets the turn radius factor.


Method detail
-------------









.. py:method:: set_relative_course(self, headingChange: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.set_relative_course

    Set the relative heading change.

    :Parameters:

    **headingChange** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_absolute_course(self, course: typing.Any, isMagnetic: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.set_absolute_course

    Set the absolute heading and reference.

    :Parameters:

    **course** : :obj:`~typing.Any`
    **isMagnetic** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: set_final_translation_course(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.set_final_translation_course

    Set the option to have the final heading to match the translation bearing.

    :Returns:

        :obj:`~None`




















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHover.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

