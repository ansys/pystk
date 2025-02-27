SatelliteExportTools
====================

.. py:class:: ansys.stk.core.stkobjects.SatelliteExportTools

   The Satellite Export Tools.

.. py:currentmodule:: SatelliteExportTools

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_ccsds_export_tool`
              - Return an Ephemeris file of the CCSDS ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_stk_export_tool`
              - Return an Ephemeris file of the STK ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_spice_export_tool`
              - Return an Ephemeris file of the Spice ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_code500_export_tool`
              - Return an Ephemeris file of the Code500Ephem ephemeris type for export; AgAsCode500.dll must be copied to your install data's 'Modules' directory.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_propagator_definition_export_tool`
              - Return a Propagator (Prop Def) file for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_attitude_export_tool`
              - Return an Attitude file for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_stk_binary_export_tool`
              - Return an Ephemeris file of the STK Binary ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_ccsds_v2_export_tool`
              - Return an Ephemeris file of the CCSDS v2 ephemeris type for export.


Examples
--------

Export an ephemeris file to scenario folder

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # Satellitesatellite: Satellite object
    scenPath = root.execute_command("GetDirectory / Scenario").item(0)
    satelliteFilePath = "%s\\%s.e" % (scenPath, satellite.instance_name)
    satelliteFilePath = satelliteFilePath.replace("\\", "\\\\")
    satellite.export_tools.get_ephemeris_stk_export_tool().export(satelliteFilePath)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SatelliteExportTools



Method detail
-------------

.. py:method:: get_ephemeris_ccsds_export_tool(self) -> VehicleEphemerisCCSDSExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_ccsds_export_tool

    Return an Ephemeris file of the CCSDS ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisCCSDSExportTool`

.. py:method:: get_ephemeris_stk_export_tool(self) -> VehicleEphemerisExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_stk_export_tool

    Return an Ephemeris file of the STK ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisExportTool`

.. py:method:: get_ephemeris_spice_export_tool(self) -> VehicleEphemerisSPICEExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_spice_export_tool

    Return an Ephemeris file of the Spice ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisSPICEExportTool`

.. py:method:: get_ephemeris_code500_export_tool(self) -> VehicleEphemerisCode500ExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_code500_export_tool

    Return an Ephemeris file of the Code500Ephem ephemeris type for export; AgAsCode500.dll must be copied to your install data's 'Modules' directory.

    :Returns:

        :obj:`~VehicleEphemerisCode500ExportTool`

.. py:method:: get_propagator_definition_export_tool(self) -> PropagatorDefinitionExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_propagator_definition_export_tool

    Return a Propagator (Prop Def) file for export.

    :Returns:

        :obj:`~PropagatorDefinitionExportTool`

.. py:method:: get_attitude_export_tool(self) -> VehicleAttitudeExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_attitude_export_tool

    Return an Attitude file for export.

    :Returns:

        :obj:`~VehicleAttitudeExportTool`

.. py:method:: get_ephemeris_stk_binary_export_tool(self) -> VehicleEphemerisBinaryExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_stk_binary_export_tool

    Return an Ephemeris file of the STK Binary ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisBinaryExportTool`

.. py:method:: get_ephemeris_ccsds_v2_export_tool(self) -> VehicleEphemerisCCSDSv2ExportTool
    :canonical: ansys.stk.core.stkobjects.SatelliteExportTools.get_ephemeris_ccsds_v2_export_tool

    Return an Ephemeris file of the CCSDS v2 ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisCCSDSv2ExportTool`

