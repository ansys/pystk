VolumetricExportTool
====================

.. py:class:: ansys.stk.core.stkobjects.VolumetricExportTool

   The Volumetric Export Tool.

.. py:currentmodule:: VolumetricExportTool

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricExportTool.export`
              - Export the Volumetric data file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricExportTool.export_data_format_type`
              - Volumetric data export format type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricExportTool.include_grid_point_cartesian`
              - Include grid point cartesian coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricExportTool.include_grid_point_native`
              - Include grid point native coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricExportTool.include_grid_reference`
              - Include grid point native coordinates.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricExportTool.volume_grid_export_type`
              - Volumetric data export format type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VolumetricExportTool


Property detail
---------------

.. py:property:: export_data_format_type
    :canonical: ansys.stk.core.stkobjects.VolumetricExportTool.export_data_format_type
    :type: VolumetricDataExportFormatType

    Volumetric data export format type.

.. py:property:: include_grid_point_cartesian
    :canonical: ansys.stk.core.stkobjects.VolumetricExportTool.include_grid_point_cartesian
    :type: bool

    Include grid point cartesian coordinates.

.. py:property:: include_grid_point_native
    :canonical: ansys.stk.core.stkobjects.VolumetricExportTool.include_grid_point_native
    :type: bool

    Include grid point native coordinates.

.. py:property:: include_grid_reference
    :canonical: ansys.stk.core.stkobjects.VolumetricExportTool.include_grid_reference
    :type: bool

    Include grid point native coordinates.

.. py:property:: volume_grid_export_type
    :canonical: ansys.stk.core.stkobjects.VolumetricExportTool.volume_grid_export_type
    :type: VolumetricVolumeGridExportType

    Volumetric data export format type.


Method detail
-------------

.. py:method:: export(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.VolumetricExportTool.export

    Export the Volumetric data file.

    :Parameters:

        **file_name** : :obj:`~str`


    :Returns:

        :obj:`~None`











