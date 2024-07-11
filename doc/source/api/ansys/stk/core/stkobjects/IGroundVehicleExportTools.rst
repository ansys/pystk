IGroundVehicleExportTools
=========================

.. py:class:: ansys.stk.core.stkobjects.IGroundVehicleExportTools

   object
   
   Interface used to define the export to data file options.

.. py:currentmodule:: IGroundVehicleExportTools

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_ephemeris_stk_export_tool`
              - Return the ephemeris export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_prop_definition_export_tool`
              - Return the Prop Def export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_attitude_export_tool`
              - Return the attitude export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_ephemeris_stk_binary_export_tool`
              - Return an Ephemeris file of the STK Binary ephemeris type for export.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGroundVehicleExportTools



Method detail
-------------

.. py:method:: get_ephemeris_stk_export_tool(self) -> IVehicleEphemerisStkExportTool
    :canonical: ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_ephemeris_stk_export_tool

    Return the ephemeris export tool.

    :Returns:

        :obj:`~IVehicleEphemerisStkExportTool`

.. py:method:: get_prop_definition_export_tool(self) -> IVehiclePropDefinitionExportTool
    :canonical: ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_prop_definition_export_tool

    Return the Prop Def export tool.

    :Returns:

        :obj:`~IVehiclePropDefinitionExportTool`

.. py:method:: get_attitude_export_tool(self) -> IVehicleAttitudeExportTool
    :canonical: ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_attitude_export_tool

    Return the attitude export tool.

    :Returns:

        :obj:`~IVehicleAttitudeExportTool`

.. py:method:: get_ephemeris_stk_binary_export_tool(self) -> IVehicleEphemerisStkBinaryExportTool
    :canonical: ansys.stk.core.stkobjects.IGroundVehicleExportTools.get_ephemeris_stk_binary_export_tool

    Return an Ephemeris file of the STK Binary ephemeris type for export.

    :Returns:

        :obj:`~IVehicleEphemerisStkBinaryExportTool`

