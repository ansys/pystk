CoverageDefinition
==================

.. py:class:: ansys.stk.core.stkobjects.CoverageDefinition

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   The AgCoverageDefinition class.

.. py:currentmodule:: CoverageDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.compute_accesses`
              - Compute accesses between the grid points and the assigned assets.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.clear_accesses`
              - Remove access information currently maintained in association with each grid point in the coverage area.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.reload_accesses`
              - Reload access data that was previously saved with a coverage definition object.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.export_accesses_as_text`
              - Export all computed accesses to an ASCII text file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.grid`
              - Definition of the coverage grid.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.point_definition`
              - Location of points on the coverage grid.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.asset_list`
              - List of assets to use in coverage computations.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.advanced`
              - Advanced properties of the coverage definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.interval`
              - Coverage interval.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.graphics`
              - 2D Graphics properties of the coverage definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.graphics_3d`
              - 3D Graphics properties of the coverage definition.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageDefinition.grid_inspector`
              - Get the grid inspector tool.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageDefinition


Property detail
---------------

.. py:property:: grid
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.grid
    :type: ICoverageGrid

    Definition of the coverage grid.

.. py:property:: point_definition
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.point_definition
    :type: ICoveragePointDefinition

    Location of points on the coverage grid.

.. py:property:: asset_list
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.asset_list
    :type: ICoverageAssetListCollection

    List of assets to use in coverage computations.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.advanced
    :type: ICoverageAdvanced

    Advanced properties of the coverage definition.

.. py:property:: interval
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.interval
    :type: ICoverageInterval

    Coverage interval.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.graphics
    :type: ICoverageGraphics

    2D Graphics properties of the coverage definition.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.graphics_3d
    :type: ICoverageGraphics3D

    3D Graphics properties of the coverage definition.

.. py:property:: grid_inspector
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.grid_inspector
    :type: ICoverageGridInspector

    Get the grid inspector tool.


Method detail
-------------








.. py:method:: compute_accesses(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.compute_accesses

    Compute accesses between the grid points and the assigned assets.

    :Returns:

        :obj:`~None`

.. py:method:: clear_accesses(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.clear_accesses

    Remove access information currently maintained in association with each grid point in the coverage area.

    :Returns:

        :obj:`~None`

.. py:method:: reload_accesses(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.reload_accesses

    Reload access data that was previously saved with a coverage definition object.

    :Returns:

        :obj:`~None`

.. py:method:: export_accesses_as_text(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.export_accesses_as_text

    Export all computed accesses to an ASCII text file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`


