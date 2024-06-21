ISatelliteExportTools
=====================

.. py:class:: ansys.stk.core.stkobjects.ISatelliteExportTools

   object
   
   Interface used to define the export to data file options.

.. py:currentmodule:: ISatelliteExportTools

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_ccsds_export_tool`
              - Return an Ephemeris file of the CCSDS ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_stk_export_tool`
              - Return an Ephemeris file of the STK ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_spice_export_tool`
              - Return an Ephemeris file of the Spice ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_code500_export_tool`
              - Return an Ephemeris file of the Code500Ephem ephemeris type for export; AgAsCode500.dll must be copied to your install data's 'Modules' directory.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_prop_definition_export_tool`
              - Return a Propagator (Prop Def) file for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_attitude_export_tool`
              - Return an Attitude file for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_stk_binary_export_tool`
              - Return an Ephemeris file of the STK Binary ephemeris type for export.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_ccsd_sv2_export_tool`
              - Return an Ephemeris file of the CCSDS v2 ephemeris type for export.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISatelliteExportTools



Method detail
-------------

.. py:method:: get_ephemeris_ccsds_export_tool(self) -> IVehicleEphemerisCCSDSExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_ccsds_export_tool

    Return an Ephemeris file of the CCSDS ephemeris type for export.

    :Returns:

        :obj:`~IVehicleEphemerisCCSDSExportTool`

.. py:method:: get_ephemeris_stk_export_tool(self) -> IVehicleEphemerisStkExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_stk_export_tool

    Return an Ephemeris file of the STK ephemeris type for export.

    :Returns:

        :obj:`~IVehicleEphemerisStkExportTool`

.. py:method:: get_ephemeris_spice_export_tool(self) -> IVehicleEphemerisSpiceExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_spice_export_tool

    Return an Ephemeris file of the Spice ephemeris type for export.

    :Returns:

        :obj:`~IVehicleEphemerisSpiceExportTool`

.. py:method:: get_ephemeris_code500_export_tool(self) -> IVehicleEphemerisCode500ExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_code500_export_tool

    Return an Ephemeris file of the Code500Ephem ephemeris type for export; AgAsCode500.dll must be copied to your install data's 'Modules' directory.

    :Returns:

        :obj:`~IVehicleEphemerisCode500ExportTool`

.. py:method:: get_prop_definition_export_tool(self) -> IVehiclePropDefinitionExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_prop_definition_export_tool

    Return a Propagator (Prop Def) file for export.

    :Returns:

        :obj:`~IVehiclePropDefinitionExportTool`

.. py:method:: get_attitude_export_tool(self) -> IVehicleAttitudeExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_attitude_export_tool

    Return an Attitude file for export.

    :Returns:

        :obj:`~IVehicleAttitudeExportTool`

.. py:method:: get_ephemeris_stk_binary_export_tool(self) -> IVehicleEphemerisStkBinaryExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_stk_binary_export_tool

    Return an Ephemeris file of the STK Binary ephemeris type for export.

    :Returns:

        :obj:`~IVehicleEphemerisStkBinaryExportTool`

.. py:method:: get_ephemeris_ccsd_sv2_export_tool(self) -> IVehicleEphemerisCCSDSv2ExportTool
    :canonical: ansys.stk.core.stkobjects.ISatelliteExportTools.get_ephemeris_ccsd_sv2_export_tool

    Return an Ephemeris file of the CCSDS v2 ephemeris type for export.

    :Returns:

        :obj:`~IVehicleEphemerisCCSDSv2ExportTool`

