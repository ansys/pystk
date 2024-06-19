IVolumetric
===========

.. py:class:: IVolumetric

   object
   
   Volumetric properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_volume_grid_definition_type`
              - Set volume grid definition type, using the AgEVmDefinitionType enumeration.
            * - :py:meth:`~compute`
              - Compute computations for Volumetric.
            * - :py:meth:`~clear`
              - Clear computations for Volumetric.
            * - :py:meth:`~get_volumetric_export_tool`
              - Volumetric export tool.
            * - :py:meth:`~compute_in_parallel`
              - Compute computations in parallel for Volumetric.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~volume_grid_definition_type`
            * - :py:meth:`~volume_grid_definition`
            * - :py:meth:`~volume_analysis_interval`
            * - :py:meth:`~advanced`
            * - :py:meth:`~graphics_3d`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVolumetric


Property detail
---------------

.. py:property:: volume_grid_definition_type
    :canonical: ansys.stk.core.stkobjects.IVolumetric.volume_grid_definition_type
    :type: VM_DEFINITION_TYPE

    Get Volume Grid definition type. A member of the AgEVmDefinitionType enumeration.

.. py:property:: volume_grid_definition
    :canonical: ansys.stk.core.stkobjects.IVolumetric.volume_grid_definition
    :type: IAgVmGridDefinition

    Get Volume Grid definition.

.. py:property:: volume_analysis_interval
    :canonical: ansys.stk.core.stkobjects.IVolumetric.volume_analysis_interval
    :type: IAgVmAnalysisInterval

    Get Volume Analysis Interval.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.IVolumetric.advanced
    :type: IAgVmAdvanced

    Get Advanced options.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IVolumetric.graphics_3d
    :type: IAgVmVO

    Get the 3D Graphics properties for the volumetric object.


Method detail
-------------


.. py:method:: set_volume_grid_definition_type(self, vmGridCalcType: VM_DEFINITION_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IVolumetric.set_volume_grid_definition_type

    Set volume grid definition type, using the AgEVmDefinitionType enumeration.

    :Parameters:

    **vmGridCalcType** : :obj:`~VM_DEFINITION_TYPE`

    :Returns:

        :obj:`~None`





.. py:method:: compute(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVolumetric.compute

    Compute computations for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVolumetric.clear

    Clear computations for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: get_volumetric_export_tool(self) -> IVmExportTool
    :canonical: ansys.stk.core.stkobjects.IVolumetric.get_volumetric_export_tool

    Volumetric export tool.

    :Returns:

        :obj:`~IVmExportTool`

.. py:method:: compute_in_parallel(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVolumetric.compute_in_parallel

    Compute computations in parallel for Volumetric.

    :Returns:

        :obj:`~None`

