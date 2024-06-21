IVehicleEphemerisCCSDSExportTool
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool

   object
   
   The CCSDS Ephemeris type for the Export Ephemeris/Attitude Tool.

.. py:currentmodule:: IVehicleEphemerisCCSDSExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.originator`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.object_id`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.object_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.central_body_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.reference_frame`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.date_format`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.ephemeris_format`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.time_precision`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.step_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.time_period`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.reference_frames_supported`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.use_satellite_center_and_frame`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.time_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEphemerisCCSDSExportTool


Property detail
---------------

.. py:property:: originator
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.originator
    :type: str

    A string that specifies an identifier of the organization producing the data file.

.. py:property:: object_id
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.object_id
    :type: str

    A string defining the Object ID - to be specified as the international spacecraft designator, also known as an NSSDC identifier.

.. py:property:: object_name
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.object_name
    :type: str

    A name for the Object. By recommendation of the CCSDS standard, the name from the SPACEWARN Bulletin should be used.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.central_body_name
    :type: str

    Gets or sets the central body of the coordinate system in which to express the ephemeris.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.reference_frame
    :type: CCSDS_REFERENCE_FRAME

    Gets or sets the reference frame in which to express the ephemeris. Some frames are allowed for use only when the CentralBodyName is Earth or Moon.

.. py:property:: date_format
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.date_format
    :type: CCSDS_DATE_FORMAT

    Gets or sets the desired date format.

.. py:property:: ephemeris_format
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.ephemeris_format
    :type: CCSDS_EPHEM_FORMAT

    Gets or sets the desired format to be used for representing the position and velocity information as either scientific notation or floating point notation. Scientific notation is recommended when possible.

.. py:property:: time_precision
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.time_precision
    :type: int

    If selected, STK uses the Step Size specified in the vehicle's Basic properties. If not selected, specify a Step Size. Dimensionless.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.step_size
    :type: IExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.time_period
    :type: IExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: reference_frames_supported
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.reference_frames_supported
    :type: list

    Returns an array of valid choices.

.. py:property:: use_satellite_center_and_frame
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.use_satellite_center_and_frame
    :type: bool

    Use the satellite center and frame. Setting the property to 'True' will cause CentralBody and ReferenceFrame properties become read-only.

.. py:property:: time_system
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.time_system
    :type: CCSDS_TIME_SYSTEM

    Gets or sets the time system of the ephemeris.


Method detail
-------------






















.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCCSDSExportTool.export

    Export the ephemeris file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`



