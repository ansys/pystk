GroundVehicleExportTools
========================

.. py:class:: ansys.stk.core.stkobjects.GroundVehicleExportTools

   The GroundVehicle Export Tools.

.. py:currentmodule:: GroundVehicleExportTools

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicleExportTools.get_ephemeris_stk_export_tool`
              - Return the ephemeris export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicleExportTools.get_propagator_definition_export_tool`
              - Return the Prop Def export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicleExportTools.get_attitude_export_tool`
              - Return the attitude export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.GroundVehicleExportTools.get_ephemeris_stk_binary_export_tool`
              - Return an Ephemeris file of the STK Binary ephemeris type for export.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import GroundVehicleExportTools



Method detail
-------------

.. py:method:: get_ephemeris_stk_export_tool(self) -> VehicleEphemerisStkExportTool
    :canonical: ansys.stk.core.stkobjects.GroundVehicleExportTools.get_ephemeris_stk_export_tool

    Return the ephemeris export tool.

    :Returns:

        :obj:`~VehicleEphemerisStkExportTool`

.. py:method:: get_propagator_definition_export_tool(self) -> VehiclePropagationDefinitionExportTool
    :canonical: ansys.stk.core.stkobjects.GroundVehicleExportTools.get_propagator_definition_export_tool

    Return the Prop Def export tool.

    :Returns:

        :obj:`~VehiclePropagationDefinitionExportTool`

.. py:method:: get_attitude_export_tool(self) -> VehicleAttitudeExportTool
    :canonical: ansys.stk.core.stkobjects.GroundVehicleExportTools.get_attitude_export_tool

    Return the attitude export tool.

    :Returns:

        :obj:`~VehicleAttitudeExportTool`

.. py:method:: get_ephemeris_stk_binary_export_tool(self) -> VehicleEphemerisStkBinaryExportTool
    :canonical: ansys.stk.core.stkobjects.GroundVehicleExportTools.get_ephemeris_stk_binary_export_tool

    Return an Ephemeris file of the STK Binary ephemeris type for export.

    :Returns:

        :obj:`~VehicleEphemerisStkBinaryExportTool`

