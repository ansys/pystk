IVehicleEphemerisStkBinaryExportTool
====================================

.. py:class:: IVehicleEphemerisStkBinaryExportTool

   object
   
   The STK Binary Ephemeris type for the Export Ephemeris/Attitude Tool.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~coordinate_system`
            * - :py:meth:`~central_body_name`
            * - :py:meth:`~version_format`
            * - :py:meth:`~include_interp`
            * - :py:meth:`~time_period`
            * - :py:meth:`~step_size`
            * - :py:meth:`~covariance_type`
            * - :py:meth:`~use_vehicle_central_body`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEphemerisStkBinaryExportTool


Property detail
---------------

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.coordinate_system
    :type: STK_EPHEM_COORDINATE_SYSTEM

    Whether the resulting data file should be in the Fixed, J2000, or Inertial coordinate system. If Earth or the Sun is the central body, the Inertial coordinate system is not an available option.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.central_body_name
    :type: str

    Gets or sets the central body of the satellite.

.. py:property:: version_format
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.version_format
    :type: EXPORT_TOOL_VERSION_FORMAT

    Provides the option to generate files compatible with prior versions of STK.

.. py:property:: include_interp
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.include_interp
    :type: bool

    Include or ignore interpolation boundaries.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.time_period
    :type: IAgExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.step_size
    :type: IAgExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: covariance_type
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.covariance_type
    :type: STK_EPHEM_COVARIANCE_TYPE

    Choose to export position covariance (3x3), position/velocity covariance (6x6), or no covariance information. CovarianceType is valid only if the vehicle has ephemeris with covariance.

.. py:property:: use_vehicle_central_body
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.use_vehicle_central_body
    :type: bool

    Uses vehicle's central body.


Method detail
-------------













.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisStkBinaryExportTool.export

    Export the ephemeris file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`



