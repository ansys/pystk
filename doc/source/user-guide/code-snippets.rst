PySTK code snippets
###################

The following code snippets demonstrate tasks that are commonly encountered when working with the PySTK API.

How do I...
===========

STK Objects
  Access
      - :ref:`Add an exclusion zone access constraint <AddExclusionZoneConstraint>`
  Coverage Definition
      - :ref:`Set the coverage interval to an object's availability analysis interval <CoverageInterval>`
      - :ref:`Set advanced settings for coverage <CoverageAdvanced>`
      - :ref:`Compute coverage <CoverageCompute>`


.. _AddExclusionZoneConstraint:

Add an exclusion zone access constraint
=======================================

.. code-block:: python

    # AccessConstraintCollection accessConstraints: Access Constraint collection
    excludeZone: "AccessConstraintLatitudeLongitudeZone" = accessConstraints.add_named_constraint('ExclusionZone')
    excludeZone.maximum_latitude = 45
    excludeZone.minimum_latitude = 15
    excludeZone.minimum_longitude = -75
    excludeZone.maximum_longitude = -35

.. _CoverageInterval:

Set the coverage interval to an object's availability analysis interval
=======================================================================

.. code-block:: python

    # Satellite satellite: Satellite object
    # CoverageDefinition coverage: Coverage object
    satVGT: "AnalysisWorkbenchComponentProvider" = IStkObject(satellite).analysis_workbench_components
    intervals: "TimeToolTimeIntervalGroup" = satVGT.time_intervals
    AvailTimeSpan: "ITimeToolTimeInterval" = intervals.item("AvailabilityTimeSpan")
    IntResult: "TimeToolTimeIntervalResult" = AvailTimeSpan.find_interval()
    coverage.interval.analysis_interval.set_start_and_stop_times(IntResult.interval.start, IntResult.interval.stop)

.. _CoverageAdvanced:

Set advanced settings for coverage
==================================

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    advanced: "CoverageAdvancedSettings" = coverage.advanced
    advanced.recompute_automatically = False
    advanced.data_retention = CoverageDataRetention.ALL_DATA
    advanced.save_mode = DataSaveMode.SAVE_ACCESSES

.. _CoverageCompute:

Compute coverage
================

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    coverage.compute_accesses()
