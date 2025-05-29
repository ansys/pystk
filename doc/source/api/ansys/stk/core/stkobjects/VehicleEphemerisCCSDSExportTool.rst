VehicleEphemerisCCSDSExportTool
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool

   VehicleEphemerisCCSDSExportTool Class.

.. py:currentmodule:: VehicleEphemerisCCSDSExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.originator`
              - A string that specifies an identifier of the organization producing the data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.object_identifier`
              - A string defining the Object ID - to be specified as the international spacecraft designator, also known as an NSSDC identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.object_name`
              - A name for the Object. By recommendation of the CCSDS standard, the name from the SPACEWARN Bulletin should be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.central_body_name`
              - Get or set the central body of the coordinate system in which to express the ephemeris.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.reference_frame`
              - Get or set the reference frame in which to express the ephemeris. Some frames are allowed for use only when the CentralBodyName is Earth or Moon.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.date_format`
              - Get or set the desired date format.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.ephemeris_format`
              - Get or set the desired format to be used for representing the position and velocity information as either scientific notation or floating point notation. Scientific notation is recommended when possible.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.time_precision`
              - If selected, STK uses the Step Size specified in the vehicle's Basic properties. If not selected, specify a Step Size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.time_period`
              - Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.reference_frames_supported`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.use_satellite_center_and_frame`
              - Use the satellite center and frame. Setting the property to 'True' will cause CentralBody and ReferenceFrame properties become read-only.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.time_system`
              - Get or set the time system of the ephemeris.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEphemerisCCSDSExportTool


Property detail
---------------

.. py:property:: originator
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.originator
    :type: str

    A string that specifies an identifier of the organization producing the data file.

.. py:property:: object_identifier
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.object_identifier
    :type: str

    A string defining the Object ID - to be specified as the international spacecraft designator, also known as an NSSDC identifier.

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.object_name
    :type: str

    A name for the Object. By recommendation of the CCSDS standard, the name from the SPACEWARN Bulletin should be used.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.central_body_name
    :type: str

    Get or set the central body of the coordinate system in which to express the ephemeris.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.reference_frame
    :type: CCSDSReferenceFrame

    Get or set the reference frame in which to express the ephemeris. Some frames are allowed for use only when the CentralBodyName is Earth or Moon.

.. py:property:: date_format
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.date_format
    :type: CCSDSDateFormat

    Get or set the desired date format.

.. py:property:: ephemeris_format
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.ephemeris_format
    :type: CCSDSEphemerisFormatType

    Get or set the desired format to be used for representing the position and velocity information as either scientific notation or floating point notation. Scientific notation is recommended when possible.

.. py:property:: time_precision
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.time_precision
    :type: int

    If selected, STK uses the Step Size specified in the vehicle's Basic properties. If not selected, specify a Step Size. Dimensionless.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.step_size
    :type: ExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.time_period
    :type: ExportToolTimePeriod

    Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: reference_frames_supported
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.reference_frames_supported
    :type: list

    Return an array of valid choices.

.. py:property:: use_satellite_center_and_frame
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.use_satellite_center_and_frame
    :type: bool

    Use the satellite center and frame. Setting the property to 'True' will cause CentralBody and ReferenceFrame properties become read-only.

.. py:property:: time_system
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.time_system
    :type: CCSDSTimeSystem

    Get or set the time system of the ephemeris.


Method detail
-------------






















.. py:method:: export(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCCSDSExportTool.export

    Export the ephemeris file.

    :Parameters:

        **file_name** : :obj:`~str`


    :Returns:

        :obj:`~None`



