ICoverageBoundsCustomRegions
============================

.. py:class:: ICoverageBoundsCustomRegions

   ICoverageBounds
   
   Custom Regions.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~region_files`
            * - :py:meth:`~area_targets`
            * - :py:meth:`~check_for_holes`
            * - :py:meth:`~small_region_algorithm`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageBoundsCustomRegions


Property detail
---------------

.. py:property:: region_files
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsCustomRegions.region_files
    :type: IAgCvRegionFilesCollection

    File containing user-defined points defining a specific grid region.

.. py:property:: area_targets
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsCustomRegions.area_targets
    :type: IAgCvAreaTargetsCollection

    Area target to be used as part of the coverage area.

.. py:property:: check_for_holes
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsCustomRegions.check_for_holes
    :type: bool

    Check for holes in custom region.

.. py:property:: small_region_algorithm
    :canonical: ansys.stk.core.stkobjects.ICoverageBoundsCustomRegions.small_region_algorithm
    :type: COVERAGE_CUSTOM_REGION_ALGORITHM

    Disables or enables one of the two special gridding algorithms triggered when Custom Region grid includes a single small region (longitude span less than 1 deg).


