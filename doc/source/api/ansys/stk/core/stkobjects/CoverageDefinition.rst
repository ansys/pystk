CoverageDefinition
==================

.. py:class:: ansys.stk.core.stkobjects.CoverageDefinition

   Bases: :py:class:`~ansys.stk.core.stkobjects.ISTKObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   The CoverageDefinition class.

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



Examples
--------

Compute Coverage

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    coverage.compute_accesses()


Set Advanced Settings for Coverage

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    advanced = coverage.advanced
    advanced.recompute_automatically = False
    advanced.data_retention = CoverageDataRetention.ALL_DATA
    advanced.save_mode = DataSaveMode.SAVE_ACCESSES


Set the Coverage Interval to an object's availability Analysis interval

.. code-block:: python

    # Satellite satellite: Satellite object
    # CoverageDefinition coverage: Coverage object
    satVGT = satellite.analysis_workbench_components
    AvailTimeSpan = satVGT.time_intervals.item("AvailabilityTimeSpan")
    IntResult = AvailTimeSpan.find_interval()
    coverage.interval.analysis_interval.set_start_and_stop_times(
        IntResult.interval.start, IntResult.interval.stop
    )


Create a New Coverage Definition (on the current scenario central body)

.. code-block:: python

    # Scenario scenario: Scenario object
    # Create new Coverage Definition and set the Bounds to an area target
    coverage = scenario.children.new(STKObjectType.COVERAGE_DEFINITION, "MyCoverage")
    coverage.grid.bounds_type = CoverageBounds.CUSTOM_REGIONS
    covGrid = coverage.grid
    bounds = covGrid.bounds
    bounds.area_targets.add("AreaTarget/MyAreaTarget")
    # Define the Grid Resolution
    Res = covGrid.resolution
    Res.latitude_longitude = 0.5  # deg
    # Set the satellite as the Asset
    coverage.asset_list.add("Satellite/MySatellite")

    # Turn off Show Grid Points
    coverage.graphics.static.show_points = False


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageDefinition


Property detail
---------------

.. py:property:: grid
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.grid
    :type: CoverageGrid

    Definition of the coverage grid.

.. py:property:: point_definition
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.point_definition
    :type: CoveragePointDefinition

    Location of points on the coverage grid.

.. py:property:: asset_list
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.asset_list
    :type: CoverageAssetListCollection

    List of assets to use in coverage computations.

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.advanced
    :type: CoverageAdvancedSettings

    Advanced properties of the coverage definition.

.. py:property:: interval
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.interval
    :type: CoverageInterval

    Coverage interval.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.graphics
    :type: CoverageGraphics

    2D Graphics properties of the coverage definition.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.graphics_3d
    :type: CoverageGraphics3D

    3D Graphics properties of the coverage definition.

.. py:property:: grid_inspector
    :canonical: ansys.stk.core.stkobjects.CoverageDefinition.grid_inspector
    :type: CoverageGridInspector

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


