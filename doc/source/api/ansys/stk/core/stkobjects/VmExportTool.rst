VmExportTool
============

.. py:class:: ansys.stk.core.stkobjects.VmExportTool

   Bases: 

   The Volumetric Export Tool.

.. py:currentmodule:: VmExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmExportTool.export`
              - Export the Volumetric data file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmExportTool.export_data_format_type`
              - Volumetric data export format type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmExportTool.volume_grid_export_type`
              - Volumetric data export format type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmExportTool.include_grid_point_cartesian`
              - Include grid point cartesian coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmExportTool.include_grid_point_native`
              - Include grid point native coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmExportTool.include_grid_reference`
              - Include grid point native coordinates.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VmExportTool


Property detail
---------------

.. py:property:: export_data_format_type
    :canonical: ansys.stk.core.stkobjects.VmExportTool.export_data_format_type
    :type: VM_DATA_EXPORT_FORMAT_TYPE

    Volumetric data export format type.

.. py:property:: volume_grid_export_type
    :canonical: ansys.stk.core.stkobjects.VmExportTool.volume_grid_export_type
    :type: VM_VOLUME_GRID_EXPORT_TYPE

    Volumetric data export format type.

.. py:property:: include_grid_point_cartesian
    :canonical: ansys.stk.core.stkobjects.VmExportTool.include_grid_point_cartesian
    :type: bool

    Include grid point cartesian coordinates.

.. py:property:: include_grid_point_native
    :canonical: ansys.stk.core.stkobjects.VmExportTool.include_grid_point_native
    :type: bool

    Include grid point native coordinates.

.. py:property:: include_grid_reference
    :canonical: ansys.stk.core.stkobjects.VmExportTool.include_grid_reference
    :type: bool

    Include grid point native coordinates.


Method detail
-------------











.. py:method:: export(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.VmExportTool.export

    Export the Volumetric data file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

