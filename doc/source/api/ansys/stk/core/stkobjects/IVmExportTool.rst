IVmExportTool
=============

.. py:class:: IVmExportTool

   object
   
   The Volumetric Export Tool.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~export`
              - Export the Volumetric data file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~export_data_format_type`
            * - :py:meth:`~volume_grid_export_type`
            * - :py:meth:`~include_grid_point_cartesian`
            * - :py:meth:`~include_grid_point_native`
            * - :py:meth:`~include_grid_reference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVmExportTool


Property detail
---------------

.. py:property:: export_data_format_type
    :canonical: ansys.stk.core.stkobjects.IVmExportTool.export_data_format_type
    :type: "VM_DATA_EXPORT_FORMAT_TYPE"

    Volumetric data export format type.

.. py:property:: volume_grid_export_type
    :canonical: ansys.stk.core.stkobjects.IVmExportTool.volume_grid_export_type
    :type: "VM_VOLUME_GRID_EXPORT_TYPE"

    Volumetric data export format type.

.. py:property:: include_grid_point_cartesian
    :canonical: ansys.stk.core.stkobjects.IVmExportTool.include_grid_point_cartesian
    :type: bool

    Include grid point cartesian coordinates.

.. py:property:: include_grid_point_native
    :canonical: ansys.stk.core.stkobjects.IVmExportTool.include_grid_point_native
    :type: bool

    Include grid point native coordinates.

.. py:property:: include_grid_reference
    :canonical: ansys.stk.core.stkobjects.IVmExportTool.include_grid_reference
    :type: bool

    Include grid point native coordinates.


Method detail
-------------











.. py:method:: export(self, fileName:str) -> None

    Export the Volumetric data file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

