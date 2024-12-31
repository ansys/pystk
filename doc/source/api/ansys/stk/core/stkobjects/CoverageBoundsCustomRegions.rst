CoverageBoundsCustomRegions
===========================

.. py:class:: ansys.stk.core.stkobjects.CoverageBoundsCustomRegions

   Bases: :py:class:`~ansys.stk.core.stkobjects.ICoverageBounds`

   Custom Regions.

.. py:currentmodule:: CoverageBoundsCustomRegions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.region_files`
              - File containing user-defined points defining a specific grid region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.area_targets`
              - Area target to be used as part of the coverage area.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.check_for_holes`
              - Check for holes in custom region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.small_region_algorithm`
              - Disables or enables one of the two special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageBoundsCustomRegions


Property detail
---------------

.. py:property:: region_files
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.region_files
    :type: CoverageRegionFilesCollection

    File containing user-defined points defining a specific grid region.

.. py:property:: area_targets
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.area_targets
    :type: CoverageAreaTargetsCollection

    Area target to be used as part of the coverage area.

.. py:property:: check_for_holes
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.check_for_holes
    :type: bool

    Check for holes in custom region.

.. py:property:: small_region_algorithm
    :canonical: ansys.stk.core.stkobjects.CoverageBoundsCustomRegions.small_region_algorithm
    :type: CoverageCustomRegionAlgorithm

    Disables or enables one of the two special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).


