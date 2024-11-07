CoverageGridInspector
=====================

.. py:class:: ansys.stk.core.stkobjects.CoverageGridInspector

   AgCvGridInspector class provides methods to use the grid inspector tool for coverage definition.

.. py:currentmodule:: CoverageGridInspector

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.select_point`
              - Lat param uses Latitude Dimension. Lon param uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.select_region`
              - Select a region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.clear_selection`
              - Clear the selected point or region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.get_grid_point_selection`
              - Return a collection of grid points that allows the user to select points into the grid inspector.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.point_coverage`
              - Accesses for the point selected in the graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.point_daily_coverage`
              - Access times for the point selected in the graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.point_probability_of_coverage`
              - Get the probability of coverage for the point selected in the graphics window being achieved as a function of the time past a request for coverage.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.region_coverage`
              - Summary of coverage for the region selected in the graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.region_full_coverage`
              - Summary of the coverage intervals for the selected region, including access start and end times, duration of each interval and the percentage of the region covered during each pass.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.region_pass_coverage`
              - Detailed information about the intervals of time when each asset can provide coverage to the selected region.
            * - :py:attr:`~ansys.stk.core.stkobjects.CoverageGridInspector.message`
              - Retrieves the message when a point or region is selected.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageGridInspector


Property detail
---------------

.. py:property:: point_coverage
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.point_coverage
    :type: IDataProviderInfo

    Accesses for the point selected in the graphics window.

.. py:property:: point_daily_coverage
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.point_daily_coverage
    :type: IDataProviderInfo

    Access times for the point selected in the graphics window.

.. py:property:: point_probability_of_coverage
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.point_probability_of_coverage
    :type: IDataProviderInfo

    Get the probability of coverage for the point selected in the graphics window being achieved as a function of the time past a request for coverage.

.. py:property:: region_coverage
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.region_coverage
    :type: IDataProviderInfo

    Summary of coverage for the region selected in the graphics window.

.. py:property:: region_full_coverage
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.region_full_coverage
    :type: IDataProviderInfo

    Summary of the coverage intervals for the selected region, including access start and end times, duration of each interval and the percentage of the region covered during each pass.

.. py:property:: region_pass_coverage
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.region_pass_coverage
    :type: IDataProviderInfo

    Detailed information about the intervals of time when each asset can provide coverage to the selected region.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.message
    :type: str

    Retrieves the message when a point or region is selected.


Method detail
-------------

.. py:method:: select_point(self, lat: typing.Any, lon: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.select_point

    Lat param uses Latitude Dimension. Lon param uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: select_region(self, region_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.select_region

    Select a region.

    :Parameters:

    **region_name** : :obj:`~str`

    :Returns:

        :obj:`~None`







.. py:method:: clear_selection(self) -> None
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.clear_selection

    Clear the selected point or region.

    :Returns:

        :obj:`~None`


.. py:method:: get_grid_point_selection(self) -> CoverageGridPointSelection
    :canonical: ansys.stk.core.stkobjects.CoverageGridInspector.get_grid_point_selection

    Return a collection of grid points that allows the user to select points into the grid inspector.

    :Returns:

        :obj:`~CoverageGridPointSelection`

