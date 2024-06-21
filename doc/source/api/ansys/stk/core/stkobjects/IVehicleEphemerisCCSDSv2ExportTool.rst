IVehicleEphemerisCCSDSv2ExportTool
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool

   object
   
   The CCSDSv2 Ephemeris type for the Export Ephemeris/Attitude Tool.

.. py:currentmodule:: IVehicleEphemerisCCSDSv2ExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.originator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.object_id`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.object_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.central_body_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.reference_frame`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.date_format`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.ephemeris_format`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.time_precision`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.step_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.time_period`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.reference_frames_supported`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.use_satellite_center_and_frame`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.time_system`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.include_acceleration`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.include_covariance`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.has_covariance_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.file_format`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEphemerisCCSDSv2ExportTool


Property detail
---------------

.. py:property:: originator
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.originator
    :type: str

    A string that specifies an identifier of the organization producing the data file.

.. py:property:: object_id
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.object_id
    :type: str

    A string defining the Object ID - to be specified as the international spacecraft designator, also known as an NSSDC identifier.

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.object_name
    :type: str

    A name for the Object. By recommendation of the CCSDS standard, the name from the SPACEWARN Bulletin should be used.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.central_body_name
    :type: str

    Gets or sets the central body of the satellite.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.reference_frame
    :type: CCSDS_REFERENCE_FRAME

    Gets or sets the reference frame of the ephemeris.

.. py:property:: date_format
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.date_format
    :type: CCSDS_DATE_FORMAT

    Gets or sets the desired date format.

.. py:property:: ephemeris_format
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.ephemeris_format
    :type: CCSDS_EPHEM_FORMAT

    Gets or sets the desired format to be used for representing the position and velocity information as either scientific notation or floating point notation. Scientific notation is recommended when possible.

.. py:property:: time_precision
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.time_precision
    :type: int

    If selected, STK uses the Step Size specified in the vehicle's Basic properties. If not selected, specify a Step Size. Dimensionless.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.step_size
    :type: IExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.time_period
    :type: IExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: reference_frames_supported
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.reference_frames_supported
    :type: list

    Returns an array of valid choices.

.. py:property:: use_satellite_center_and_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.use_satellite_center_and_frame
    :type: bool

    Use the satellite center and frame. Setting the property to 'True' will cause CentralBody and ReferenceFrame properties become read-only.

.. py:property:: time_system
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.time_system
    :type: CCSDS_TIME_SYSTEM

    Gets or sets the time system of the ephemeris.

.. py:property:: include_acceleration
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.include_acceleration
    :type: bool

    Include acceleration data in the exported file.

.. py:property:: include_covariance
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.include_covariance
    :type: bool

    Include covariance data in the exported file. If covariance data is not available, this property becomes read-only.

.. py:property:: has_covariance_data
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.has_covariance_data
    :type: bool

    Returns true if the object has covariance data.

.. py:property:: file_format
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.file_format
    :type: EPHEM_EXPORT_TOOL_FILE_FORMAT

    Gets or sets the file format that will be generated by the export tool.


Method detail
-------------






















.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSv2ExportTool.export

    Export the ephemeris file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`










