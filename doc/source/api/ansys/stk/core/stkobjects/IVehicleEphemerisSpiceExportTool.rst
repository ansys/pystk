IVehicleEphemerisSpiceExportTool
================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool

   object
   
   The SPICE Ephemeris type for the Export Ephemeris/Attitude Tool.

.. py:currentmodule:: IVehicleEphemerisSpiceExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.central_body_name`
              - Gets or sets the central body of the satellite.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.sat_id`
              - Gets or sets the identifying number for the satellite ephemeris being created. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.interpolation_type`
              - Gets or sets the interpolation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.interpolation`
              - Gets or sets the interpolation order value between 1 and 15. If the interpolation type is Type 13 (Hermitian), and then you are required to enter an odd interpolation order value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.time_period`
              - Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.use_vehicle_central_body`
              - Uses vehicle's central body.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEphemerisSpiceExportTool


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.central_body_name
    :type: str

    Gets or sets the central body of the satellite.

.. py:property:: sat_id
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.sat_id
    :type: int

    Gets or sets the identifying number for the satellite ephemeris being created. Dimensionless.

.. py:property:: interpolation_type
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.interpolation_type
    :type: SPICE_INTERPOLATION

    Gets or sets the interpolation type.

.. py:property:: interpolation
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.interpolation
    :type: int

    Gets or sets the interpolation order value between 1 and 15. If the interpolation type is Type 13 (Hermitian), and then you are required to enter an odd interpolation order value.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.step_size
    :type: IExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.time_period
    :type: IExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: use_vehicle_central_body
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.use_vehicle_central_body
    :type: bool

    Uses vehicle's central body.


Method detail
-------------











.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisSpiceExportTool.export

    Export the ephemeris file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`



