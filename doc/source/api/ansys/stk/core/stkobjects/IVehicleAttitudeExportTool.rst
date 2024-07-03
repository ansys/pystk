IVehicleAttitudeExportTool
==========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool

   object
   
   Attitude file for the Export Ephemeris/Attitude File Tool.

.. py:currentmodule:: IVehicleAttitudeExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.set_coordinate_axes_type`
              - Select the coordinate axes to be used in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.export`
              - Export the Attitude file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.coordinate_axes_type`
              - Get the coordinate axes to be used in the file.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.coordinate_axes`
              - Selects a custom coordinate axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.time_period`
              - Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.include`
              - Gets or sets the details to include in the data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.version_format`
              - Provides the option to generate files compatible with prior versions of STK.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.step_size`
              - If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.supported_coordinate_axes`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.central_body_name`
              - Get the central body of the satellite.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeExportTool


Property detail
---------------

.. py:property:: coordinate_axes_type
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.coordinate_axes_type
    :type: ATTITUDE_COORDINATE_AXES

    Get the coordinate axes to be used in the file.

.. py:property:: coordinate_axes
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.coordinate_axes
    :type: IVehicleCoordinateAxes

    Selects a custom coordinate axes.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.time_period
    :type: IExportToolTimePeriod

    Sets the time period. Options are Use Entire Ephemeris - STK creates a data file using the Start and Stop Time specified in the vehicle's Orbit tab or Specify Time Period - STK creates a data file using the Start and Stop Time specified here.

.. py:property:: include
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.include
    :type: ATTITUDE_INCLUDE

    Gets or sets the details to include in the data file.

.. py:property:: version_format
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.version_format
    :type: EXPORT_TOOL_VERSION_FORMAT

    Provides the option to generate files compatible with prior versions of STK.

.. py:property:: step_size
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.step_size
    :type: IExportToolStepSize

    If the Use Ephemeris Steps option is not selected, enter a Step Size to be used for the vehicle.

.. py:property:: supported_coordinate_axes
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.supported_coordinate_axes
    :type: list

    Returns an array of valid choices.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.central_body_name
    :type: str

    Get the central body of the satellite.


Method detail
-------------


.. py:method:: set_coordinate_axes_type(self, coordinateAxes: ATTITUDE_COORDINATE_AXES) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.set_coordinate_axes_type

    Select the coordinate axes to be used in the file.

    :Parameters:

    **coordinateAxes** : :obj:`~ATTITUDE_COORDINATE_AXES`

    :Returns:

        :obj:`~None`










.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeExportTool.export

    Export the Attitude file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

