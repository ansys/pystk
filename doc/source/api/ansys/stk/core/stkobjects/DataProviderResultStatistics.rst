DataProviderResultStatistics
============================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultStatistics

   Bases: 

   Class used to compute statistics and time varying extremum on data provider result data sets.

.. py:currentmodule:: DataProviderResultStatistics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultStatistics.compute_statistic`
              - Compute the requested statistic for the data set.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultStatistics.compute_time_varying_extremum`
              - Compute the requested time varying extremum for the data set.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultStatistics.is_statistic_available`
              - Is the supplied statistic available for the data?
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultStatistics.is_time_varying_extremum_available`
              - Is the supplied time varying extremum available for the data?



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultStatistics



Method detail
-------------

.. py:method:: compute_statistic(self, statistic: STATISTICS) -> DataProviderResultStatisticResult
    :canonical: ansys.stk.core.stkobjects.DataProviderResultStatistics.compute_statistic

    Compute the requested statistic for the data set.

    :Parameters:

    **statistic** : :obj:`~STATISTICS`

    :Returns:

        :obj:`~DataProviderResultStatisticResult`

.. py:method:: compute_time_varying_extremum(self, timeVarExtremum: TIME_VARYING_EXTREMUM) -> DataProviderResultTimeVaryingExtremumResult
    :canonical: ansys.stk.core.stkobjects.DataProviderResultStatistics.compute_time_varying_extremum

    Compute the requested time varying extremum for the data set.

    :Parameters:

    **timeVarExtremum** : :obj:`~TIME_VARYING_EXTREMUM`

    :Returns:

        :obj:`~DataProviderResultTimeVaryingExtremumResult`

.. py:method:: is_statistic_available(self, statistic: STATISTICS) -> bool
    :canonical: ansys.stk.core.stkobjects.DataProviderResultStatistics.is_statistic_available

    Is the supplied statistic available for the data?

    :Parameters:

    **statistic** : :obj:`~STATISTICS`

    :Returns:

        :obj:`~bool`

.. py:method:: is_time_varying_extremum_available(self, timeVarExtremum: TIME_VARYING_EXTREMUM) -> bool
    :canonical: ansys.stk.core.stkobjects.DataProviderResultStatistics.is_time_varying_extremum_available

    Is the supplied time varying extremum available for the data?

    :Parameters:

    **timeVarExtremum** : :obj:`~TIME_VARYING_EXTREMUM`

    :Returns:

        :obj:`~bool`

