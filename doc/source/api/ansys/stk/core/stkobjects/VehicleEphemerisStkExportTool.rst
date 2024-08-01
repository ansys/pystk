VehicleEphemerisStkExportTool
=============================

.. py:class:: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool

   Bases: 

   AgVeEphemerisTypeSTK Class.

.. py:currentmodule:: VehicleEphemerisStkExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.coordinate_system`
              - Gets or sets the coordinate system in which to express the ephemeris.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.central_body_name`
              - Gets or sets the central body of the coordinate system in which to express the ephemeris.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.version_format`
              - Provides the option to generate files compatible with prior versions of STK.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.include_interpolation`
              - Include or ignore interpolation boundaries.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.time_period`
              - Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.covariance_type`
              - Choose to export position covariance (3x3), position/velocity covariance (6x6), or no covariance information. CovarianceType is valid only if the vehicle has ephemeris with covariance.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.use_vehicle_central_body`
              - Uses vehicle's central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEphemerisStkExportTool


Property detail
---------------

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.coordinate_system
    :type: STK_EPHEM_COORDINATE_SYSTEM

    Gets or sets the coordinate system in which to express the ephemeris.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.central_body_name
    :type: str

    Gets or sets the central body of the coordinate system in which to express the ephemeris.

.. py:property:: version_format
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.version_format
    :type: EXPORT_TOOL_VERSION_FORMAT

    Provides the option to generate files compatible with prior versions of STK.

.. py:property:: include_interpolation
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.include_interpolation
    :type: bool

    Include or ignore interpolation boundaries.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.time_period
    :type: IExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.step_size
    :type: IExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: covariance_type
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.covariance_type
    :type: STK_EPHEM_COVARIANCE_TYPE

    Choose to export position covariance (3x3), position/velocity covariance (6x6), or no covariance information. CovarianceType is valid only if the vehicle has ephemeris with covariance.

.. py:property:: use_vehicle_central_body
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.use_vehicle_central_body
    :type: bool

    Uses vehicle's central body.


Method detail
-------------













.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisStkExportTool.export

    Export the ephemeris file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`



