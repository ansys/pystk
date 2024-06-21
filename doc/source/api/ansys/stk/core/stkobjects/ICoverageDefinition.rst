ICoverageDefinition
===================

.. py:class:: ansys.stk.core.stkobjects.ICoverageDefinition

   object
   
   Coverage definition properties.

.. py:currentmodule:: ICoverageDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.compute_accesses`
              - Compute accesses between the grid points and the assigned assets.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.clear_accesses`
              - Remove access information currently maintained in association with each grid point in the coverage area.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.reload_accesses`
              - Reload access data that was previously saved with a coverage definition object.
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.export_accesses_as_text`
              - Export all computed accesses to an ASCII text file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.grid`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.point_definition`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.asset_list`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.advanced`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.interval`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.graphics`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.graphics_3d`
            * - :py:attr:`~ansys.stk.core.stkobjects.ICoverageDefinition.grid_inspector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageDefinition


Property detail
---------------

.. py:property:: grid
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.grid
    :type: ICoverageGrid

    Definition of the coverage grid.

.. py:property:: point_definition
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.point_definition
    :type: ICoveragePointDefinition

    Location of points on the coverage grid.

.. py:property:: asset_list
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.asset_list
    :type: ICoverageAssetListCollection

    List of assets to use in coverage computations.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.advanced
    :type: ICoverageAdvanced

    Advanced properties of the coverage definition.

.. py:property:: interval
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.interval
    :type: ICoverageInterval

    Coverage interval.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.graphics
    :type: ICoverageGraphics

    2D Graphics properties of the coverage definition.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.graphics_3d
    :type: ICoverageGraphics3D

    3D Graphics properties of the coverage definition.

.. py:property:: grid_inspector
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.grid_inspector
    :type: ICoverageGridInspector

    Get the grid inspector tool.


Method detail
-------------








.. py:method:: compute_accesses(self) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.compute_accesses

    Compute accesses between the grid points and the assigned assets.

    :Returns:

        :obj:`~None`

.. py:method:: clear_accesses(self) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.clear_accesses

    Remove access information currently maintained in association with each grid point in the coverage area.

    :Returns:

        :obj:`~None`

.. py:method:: reload_accesses(self) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.reload_accesses

    Reload access data that was previously saved with a coverage definition object.

    :Returns:

        :obj:`~None`

.. py:method:: export_accesses_as_text(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.ICoverageDefinition.export_accesses_as_text

    Export all computed accesses to an ASCII text file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`


