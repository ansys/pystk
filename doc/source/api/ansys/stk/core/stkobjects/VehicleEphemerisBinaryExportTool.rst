VehicleEphemerisBinaryExportTool
================================

.. py:class:: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool

   AgVeEphemerisTypeSTKBinary Class.

.. py:currentmodule:: VehicleEphemerisBinaryExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.coordinate_system`
              - Whether the resulting data file should be in the Fixed, J2000, or Inertial coordinate system. If Earth or the Sun is the central body, the Inertial coordinate system is not an available option.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.central_body_name`
              - Get or set the central body of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.version_format`
              - Provide the option to generate files compatible with prior versions of STK.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.include_interpolation_boundaries`
              - Include or ignore interpolation boundaries.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.time_period`
              - Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.covariance_type`
              - Choose to export position covariance (3x3), position/velocity covariance (6x6), or no covariance information. CovarianceType is valid only if the vehicle has ephemeris with covariance.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.use_vehicle_central_body`
              - Uses vehicle's central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEphemerisBinaryExportTool


Property detail
---------------

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.coordinate_system
    :type: EphemerisCoordinateSystemType

    Whether the resulting data file should be in the Fixed, J2000, or Inertial coordinate system. If Earth or the Sun is the central body, the Inertial coordinate system is not an available option.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.central_body_name
    :type: str

    Get or set the central body of the satellite.

.. py:property:: version_format
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.version_format
    :type: ExportToolVersionFormat

    Provide the option to generate files compatible with prior versions of STK.

.. py:property:: include_interpolation_boundaries
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.include_interpolation_boundaries
    :type: bool

    Include or ignore interpolation boundaries.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.time_period
    :type: ExportToolTimePeriod

    Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.step_size
    :type: ExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: covariance_type
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.covariance_type
    :type: EphemerisCovarianceType

    Choose to export position covariance (3x3), position/velocity covariance (6x6), or no covariance information. CovarianceType is valid only if the vehicle has ephemeris with covariance.

.. py:property:: use_vehicle_central_body
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.use_vehicle_central_body
    :type: bool

    Uses vehicle's central body.


Method detail
-------------













.. py:method:: export(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisBinaryExportTool.export

    Export the ephemeris file.

    :Parameters:

    **file_name** : :obj:`~str`

    :Returns:

        :obj:`~None`



