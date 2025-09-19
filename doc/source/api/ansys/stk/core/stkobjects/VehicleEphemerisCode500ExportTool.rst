VehicleEphemerisCode500ExportTool
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool

   VehicleEphemerisCode500ExportTool Class.

.. py:currentmodule:: VehicleEphemerisCode500ExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.export`
              - Export the ephemeris file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.satellite_identifer`
              - Get or set the identifying number for the satellite ephemeris being created. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.time_period`
              - Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleEphemerisCode500ExportTool


Property detail
---------------

.. py:property:: satellite_identifer
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.satellite_identifer
    :type: int

    Get or set the identifying number for the satellite ephemeris being created. Dimensionless.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.step_size
    :type: ExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.time_period
    :type: ExportToolTimePeriod

    Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.


Method detail
-------------

.. py:method:: export(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleEphemerisCode500ExportTool.export

    Export the ephemeris file.

    :Parameters:

        **file_name** : :obj:`~str`


    :Returns:

        :obj:`~None`





