PySTK Code Snippets
###################

Introduction
============

The following code snippets demonstrate tasks that are commonly encountered when working with the PySTK API.

How do I...
===========

STK Objects
  Access
      - :ref:`Add an Exclusion Zone access constraint <AddExclusionZoneConstraint>`
  Coverage Definition
      - :ref:`Set the Coverage Interval to an object's availability Analysis interval <CoverageInterval>`
      - :ref:`Set Advanced Settings for Coverage <CoverageAdvanced>`
      - :ref:`Compute Coverage <CoverageCompute>`


.. _AddExclusionZoneConstraint:

Add an Exclusion Zone access constraint
=======================================

.. code-block:: python

    # IAgAccessConstraintCollection accessConstraints: Access Constraint collection
    excludeZone: "AccessConstraintLatitudeLongitudeZone" = accessConstraints.add_named_constraint('ExclusionZone')
    excludeZone.maximum_latitude = 45
    excludeZone.minimum_latitude = 15
    excludeZone.minimum_longitude = -75
    excludeZone.maximum_longitude = -35

.. _CoverageInterval:

Set the Coverage Interval to an object's availability Analysis interval
=======================================================================

.. code-block:: python

    # IAgSatellite satellite: Satellite object
    # IAgCoverageDefinition coverage: Coverage object
    satVGT: "AnalysisWorkbenchComponentProvider" = IStkObject(satellite).analysis_workbench_components
    intervals: "TimeToolTimeIntervalGroup" = satVGT.time_intervals
    AvailTimeSpan: "ITimeToolTimeInterval" = intervals.item("AvailabilityTimeSpan")
    IntResult: "TimeToolTimeIntervalResult" = AvailTimeSpan.find_interval()
    coverage.interval.analysis_interval.set_start_and_stop_times(IntResult.interval.start, IntResult.interval.stop)

.. _CoverageAdvanced:

Set Advanced Settings for Coverage
==================================

.. code-block:: python

    # IAgCoverageDefinition coverage: Coverage object
    advanced: "CoverageAdvancedSettings" = coverage.advanced
    advanced.recompute_automatically = False
    advanced.data_retention = CoverageDataRetention.ALL_DATA
    advanced.save_mode = DataSaveMode.SAVE_ACCESSES

.. _CoverageCompute:

Compute Coverage
================

.. code-block:: python

    # IAgCoverageDefinition coverage: Coverage object
    coverage.compute_accesses()
