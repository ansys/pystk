ProcedureExtEphem
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining an ExtEphem procedure.

.. py:currentmodule:: ProcedureExtEphem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.shift_rotate_set`
              - Shift rotate set values.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.ephemeris_file`
              - Set the ephemeris filename.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.ephemeris_file_duration`
              - Get the ephemeris file duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.use_start_duration`
              - Set whether to use Start and Duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.start_time`
              - Set the start time.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.duration`
              - Set the duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.flight_mode`
              - Get the flight mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.use_shift_rotate`
              - Set whether to use Shift/Rotate.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.shift_time`
              - Get the shift time.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.latitude`
              - Get the waypoint latitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.longitude`
              - Get the waypoint longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.altitude`
              - Get the altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.course`
              - Get the course.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.course_mode`
              - Get the course mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.altitude_mode`
              - Get the alt mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureExtEphem


Property detail
---------------

.. py:property:: ephemeris_file
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.ephemeris_file
    :type: None

    Set the ephemeris filename.

.. py:property:: ephemeris_file_duration
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.ephemeris_file_duration
    :type: float

    Get the ephemeris file duration.

.. py:property:: use_start_duration
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.use_start_duration
    :type: None

    Set whether to use Start and Duration.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.start_time
    :type: None

    Set the start time.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.duration
    :type: None

    Set the duration.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.flight_mode
    :type: EXT_EPHEM_FLIGHT_MODE

    Get the flight mode.

.. py:property:: use_shift_rotate
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.use_shift_rotate
    :type: None

    Set whether to use Shift/Rotate.

.. py:property:: shift_time
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.shift_time
    :type: float

    Get the shift time.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.latitude
    :type: float

    Get the waypoint latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.longitude
    :type: float

    Get the waypoint longitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.altitude
    :type: float

    Get the altitude.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.course
    :type: float

    Get the course.

.. py:property:: course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.course_mode
    :type: EPHEM_SHIFT_ROTATE_COURSE_MODE

    Get the course mode.

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.altitude_mode
    :type: EPHEM_SHIFT_ROTATE_ALTITUDE_MODE

    Get the alt mode.


Method detail
-------------












.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

















.. py:method:: shift_rotate_set(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureExtEphem.shift_rotate_set

    Shift rotate set values.

    :Returns:

        :obj:`~None`

