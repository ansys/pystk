IProcedureExtEphem
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem

   object
   
   Interface used to access the options for an ExtEphem procedure.

.. py:currentmodule:: IProcedureExtEphem

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.get_as_procedure`
              - Get the procedure interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.shift_rotate_set`
              - Shift rotate set values.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.ephemeris_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.ephemeris_file_duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.use_start_duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.start_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.duration`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.flight_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.use_shift_rotate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.shift_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.latitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.longitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.course`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.course_mode`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.altitude_mode`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureExtEphem


Property detail
---------------

.. py:property:: ephemeris_file
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.ephemeris_file
    :type: None

    Set the ephemeris filename.

.. py:property:: ephemeris_file_duration
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.ephemeris_file_duration
    :type: float

    Get the ephemeris file duration.

.. py:property:: use_start_duration
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.use_start_duration
    :type: None

    Set whether to use Start and Duration.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.start_time
    :type: None

    Set the start time.

.. py:property:: duration
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.duration
    :type: None

    Set the duration.

.. py:property:: flight_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.flight_mode
    :type: EXT_EPHEM_FLIGHT_MODE

    Get the flight mode.

.. py:property:: use_shift_rotate
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.use_shift_rotate
    :type: None

    Set whether to use Shift/Rotate.

.. py:property:: shift_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.shift_time
    :type: float

    Get the shift time.

.. py:property:: latitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.latitude
    :type: float

    Get the waypoint latitude.

.. py:property:: longitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.longitude
    :type: float

    Get the waypoint longitude.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.altitude
    :type: float

    Get the altitude.

.. py:property:: course
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.course
    :type: float

    Get the course.

.. py:property:: course_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.course_mode
    :type: EPHEM_SHIFT_ROTATE_COURSE_MODE

    Get the course mode.

.. py:property:: altitude_mode
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.altitude_mode
    :type: EPHEM_SHIFT_ROTATE_ALTITUDE_MODE

    Get the alt mode.


Method detail
-------------












.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

















.. py:method:: shift_rotate_set(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureExtEphem.shift_rotate_set

    Shift rotate set values.

    :Returns:

        :obj:`~None`

