VehicleAttitudeExportTool
=========================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudeExportTool

   AgVeExternalFileAttitude Class.

.. py:currentmodule:: VehicleAttitudeExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.set_coordinate_axes_type`
              - Select the coordinate axes to be used in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.export`
              - Export the Attitude file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.coordinate_axes_type`
              - Get the coordinate axes to be used in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.coordinate_axes`
              - Select a custom coordinate axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.time_period`
              - Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.include`
              - Get or set the details to include in the data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.version_format`
              - Provide the option to generate files compatible with prior versions of STK.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.supported_coordinate_axes`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeExportTool.central_body_name`
              - Get the central body of the satellite.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitudeExportTool


Property detail
---------------

.. py:property:: coordinate_axes_type
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.coordinate_axes_type
    :type: AttitudeCoordinateAxes

    Get the coordinate axes to be used in the file.

.. py:property:: coordinate_axes
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.coordinate_axes
    :type: IVehicleCoordinateAxes

    Select a custom coordinate axes.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.time_period
    :type: ExportToolTimePeriod

    Set the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: include
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.include
    :type: AttitudeInclude

    Get or set the details to include in the data file.

.. py:property:: version_format
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.version_format
    :type: ExportToolVersionFormat

    Provide the option to generate files compatible with prior versions of STK.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.step_size
    :type: ExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: supported_coordinate_axes
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.supported_coordinate_axes
    :type: list

    Return an array of valid choices.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.central_body_name
    :type: str

    Get the central body of the satellite.


Method detail
-------------


.. py:method:: set_coordinate_axes_type(self, coordinate_axes: AttitudeCoordinateAxes) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.set_coordinate_axes_type

    Select the coordinate axes to be used in the file.

    :Parameters:

    **coordinate_axes** : :obj:`~AttitudeCoordinateAxes`

    :Returns:

        :obj:`~None`










.. py:method:: export(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeExportTool.export

    Export the Attitude file.

    :Parameters:

    **file_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

