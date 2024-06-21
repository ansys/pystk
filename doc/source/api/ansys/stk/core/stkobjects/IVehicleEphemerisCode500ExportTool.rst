IVehicleEphemerisCode500ExportTool
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool

   object
   
   The Code 500 Ephemeris type for the Export Ephemeris/Attitude Tool.

.. py:currentmodule:: IVehicleEphemerisCode500ExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.sat_id`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.step_size`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.time_period`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleEphemerisCode500ExportTool


Property detail
---------------

.. py:property:: sat_id
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.sat_id
    :type: int

    Gets or sets the identifying number for the satellite ephemeris being created. Dimensionless.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.step_size
    :type: IExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.time_period
    :type: IExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.


Method detail
-------------





.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleEphemerisCode500ExportTool.export

    Export the ephemeris file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

