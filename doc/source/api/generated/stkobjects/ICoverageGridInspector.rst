ICoverageGridInspector
======================

.. py:class:: ICoverageGridInspector

   object
   
   Provide access to the Coverage Definition grid inspector properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~select_point`
              - Lat param uses Latitude Dimension. Lon param uses Longitude Dimension.
            * - :py:meth:`~select_region`
              - Select a region.
            * - :py:meth:`~clear_selection`
              - Clear the selected point or region.
            * - :py:meth:`~get_grid_point_selection`
              - Return a collection of grid points that allows the user to select points into the grid inspector.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~point_coverage`
            * - :py:meth:`~point_daily_coverage`
            * - :py:meth:`~point_prob_of_coverage`
            * - :py:meth:`~region_coverage`
            * - :py:meth:`~region_full_coverage`
            * - :py:meth:`~region_pass_coverage`
            * - :py:meth:`~message`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ICoverageGridInspector


Property detail
---------------

.. py:property:: point_coverage
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.point_coverage
    :type: "IAgDataProviderInfo"

    Accesses for the point selected in the graphics window.

.. py:property:: point_daily_coverage
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.point_daily_coverage
    :type: "IAgDataProviderInfo"

    Access times for the point selected in the graphics window.

.. py:property:: point_prob_of_coverage
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.point_prob_of_coverage
    :type: "IAgDataProviderInfo"

    Get the probability of coverage for the point selected in the graphics window being achieved as a function of the time past a request for coverage.

.. py:property:: region_coverage
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.region_coverage
    :type: "IAgDataProviderInfo"

    Summary of coverage for the region selected in the graphics window.

.. py:property:: region_full_coverage
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.region_full_coverage
    :type: "IAgDataProviderInfo"

    Summary of the coverage intervals for the selected region, including access start and end times, duration of each interval and the percentage of the region covered during each pass.

.. py:property:: region_pass_coverage
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.region_pass_coverage
    :type: "IAgDataProviderInfo"

    Detailed information about the intervals of time when each asset can provide coverage to the selected region.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.ICoverageGridInspector.message
    :type: str

    Retrieves the message when a point or region is selected.


Method detail
-------------

.. py:method:: select_point(self, lat:typing.Any, lon:typing.Any) -> None

    Lat param uses Latitude Dimension. Lon param uses Longitude Dimension.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: select_region(self, regionName:str) -> None

    Select a region.

    :Parameters:

    **regionName** : :obj:`~str`

    :Returns:

        :obj:`~None`







.. py:method:: clear_selection(self) -> None

    Clear the selected point or region.

    :Returns:

        :obj:`~None`


.. py:method:: get_grid_point_selection(self) -> "ICoverageGridPointSelection"

    Return a collection of grid points that allows the user to select points into the grid inspector.

    :Returns:

        :obj:`~"ICoverageGridPointSelection"`

