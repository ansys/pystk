IProcedureHoverTranslate
========================

.. py:class:: IProcedureHoverTranslate

   object
   
   Interface used to access the options for a hover translate procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_relative_course`
              - Set the relative heading change.
            * - :py:meth:`~set_absolute_course`
              - Set the absolute heading and reference.
            * - :py:meth:`~set_final_translation_course`
              - Set the option to have the final heading to match the translation bearing.
            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_options`
            * - :py:meth:`~heading_mode`
            * - :py:meth:`~final_heading_mode`
            * - :py:meth:`~absolute_course`
            * - :py:meth:`~relative_course`
            * - :py:meth:`~use_magnetic_heading`
            * - :py:meth:`~final_heading_rate`
            * - :py:meth:`~final_course_mode`
            * - :py:meth:`~smooth_translation_mode`
            * - :py:meth:`~radius_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureHoverTranslate


Property detail
---------------

.. py:property:: altitude_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.altitude_options
    :type: IAgAvtrHoverAltitudeOptions

    Get the altitude options.

.. py:property:: heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.heading_mode
    :type: VTOL_HEADING_MODE

    Gets or sets the heading mode for the aircraft.

.. py:property:: final_heading_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.final_heading_mode
    :type: VTOL_FINAL_HEADING_MODE

    Get the mode to define the heading at the end of the hover.

.. py:property:: absolute_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.absolute_course
    :type: typing.Any

    Get the absolute course for the heading.

.. py:property:: relative_course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.relative_course
    :type: typing.Any

    Get the relative heading change.

.. py:property:: use_magnetic_heading
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.use_magnetic_heading
    :type: bool

    Get the option to use a magnetic heading for the heading course.

.. py:property:: final_heading_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.final_heading_rate
    :type: VTOL_RATE_MODE

    Gets or sets the options to define the heading rate of the aircraft at the end of the procedure.

.. py:property:: final_course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.final_course_mode
    :type: VTOL_TRANSLATION_FINAL_COURSE_MODE

    Gets or sets the mode to specify the final course at the end of the hover.

.. py:property:: smooth_translation_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.smooth_translation_mode
    :type: VTOL_RATE_MODE

    Gets or sets the translation mode of the aircraft at the end of the procedure.

.. py:property:: radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.radius_factor
    :type: float

    Gets or sets the turn radius factor.


Method detail
-------------





.. py:method:: set_relative_course(self, headingChange: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.set_relative_course

    Set the relative heading change.

    :Parameters:

    **headingChange** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_absolute_course(self, course: typing.Any, isMagnetic: bool) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.set_absolute_course

    Set the absolute heading and reference.

    :Parameters:

    **course** : :obj:`~typing.Any`
    **isMagnetic** : :obj:`~bool`

    :Returns:

        :obj:`~None`

.. py:method:: set_final_translation_course(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.set_final_translation_course

    Set the option to have the final heading to match the translation bearing.

    :Returns:

        :obj:`~None`












.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureHoverTranslate.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

