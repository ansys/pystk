Volumetric
==========

.. py:class:: ansys.stk.core.stkobjects.Volumetric

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   The Volumetric class.

.. py:currentmodule:: Volumetric

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.set_volume_grid_definition_type`
              - Set volume grid definition type, using the VolumetricDefinitionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.compute`
              - Compute computations for Volumetric.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.clear`
              - Clear computations for Volumetric.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.get_volumetric_export_tool`
              - Volumetric export tool.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.compute_in_parallel`
              - Compute computations in parallel for Volumetric.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.volume_grid_definition_type`
              - Get Volume Grid definition type. A member of the VolumetricDefinitionType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.volume_grid_definition`
              - Get Volume Grid definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.volume_analysis_interval`
              - Get Volume Analysis Interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.advanced`
              - Get Advanced options.
            * - :py:attr:`~ansys.stk.core.stkobjects.Volumetric.graphics_3d`
              - Get the 3D Graphics properties for the volumetric object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Volumetric


Property detail
---------------

.. py:property:: volume_grid_definition_type
    :canonical: ansys.stk.core.stkobjects.Volumetric.volume_grid_definition_type
    :type: VolumetricDefinitionType

    Get Volume Grid definition type. A member of the VolumetricDefinitionType enumeration.

.. py:property:: volume_grid_definition
    :canonical: ansys.stk.core.stkobjects.Volumetric.volume_grid_definition
    :type: IVolumetricGridDefinition

    Get Volume Grid definition.

.. py:property:: volume_analysis_interval
    :canonical: ansys.stk.core.stkobjects.Volumetric.volume_analysis_interval
    :type: VolumetricAnalysisInterval

    Get Volume Analysis Interval.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.Volumetric.advanced
    :type: VolumetricAdvancedSettings

    Get Advanced options.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Volumetric.graphics_3d
    :type: VolumetricGraphics3D

    Get the 3D Graphics properties for the volumetric object.


Method detail
-------------


.. py:method:: set_volume_grid_definition_type(self, vm_grid_calc_type: VolumetricDefinitionType) -> None
    :canonical: ansys.stk.core.stkobjects.Volumetric.set_volume_grid_definition_type

    Set volume grid definition type, using the VolumetricDefinitionType enumeration.

    :Parameters:

    **vm_grid_calc_type** : :obj:`~VolumetricDefinitionType`

    :Returns:

        :obj:`~None`





.. py:method:: compute(self) -> None
    :canonical: ansys.stk.core.stkobjects.Volumetric.compute

    Compute computations for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.Volumetric.clear

    Clear computations for Volumetric.

    :Returns:

        :obj:`~None`

.. py:method:: get_volumetric_export_tool(self) -> VolumetricExportTool
    :canonical: ansys.stk.core.stkobjects.Volumetric.get_volumetric_export_tool

    Volumetric export tool.

    :Returns:

        :obj:`~VolumetricExportTool`

.. py:method:: compute_in_parallel(self) -> None
    :canonical: ansys.stk.core.stkobjects.Volumetric.compute_in_parallel

    Compute computations in parallel for Volumetric.

    :Returns:

        :obj:`~None`

