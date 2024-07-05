IDataProviderResultStatistics
=============================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultStatistics

   object
   
   Compute statistics and time varying extremums on a data set when available.

.. py:currentmodule:: IDataProviderResultStatistics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultStatistics.compute_statistic`
              - Compute the requested statistic for the data set.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultStatistics.compute_time_varying_extremum`
              - Compute the requested time varying extremum for the data set.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultStatistics.is_statistic_available`
              - Is the supplied statistic available for the data?
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultStatistics.is_time_varying_extremum_available`
              - Is the supplied time varying extremum available for the data?


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultStatistics



Method detail
-------------

.. py:method:: compute_statistic(self, statistic: STATISTICS) -> IDataProviderResultStatisticResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultStatistics.compute_statistic

    Compute the requested statistic for the data set.

    :Parameters:

    **statistic** : :obj:`~STATISTICS`

    :Returns:

        :obj:`~IDataProviderResultStatisticResult`

.. py:method:: compute_time_varying_extremum(self, timeVarExtremum: TIME_VARYING_EXTREMUM) -> IDataProviderResultTimeVaryingExtremumResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultStatistics.compute_time_varying_extremum

    Compute the requested time varying extremum for the data set.

    :Parameters:

    **timeVarExtremum** : :obj:`~TIME_VARYING_EXTREMUM`

    :Returns:

        :obj:`~IDataProviderResultTimeVaryingExtremumResult`

.. py:method:: is_statistic_available(self, statistic: STATISTICS) -> bool
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultStatistics.is_statistic_available

    Is the supplied statistic available for the data?

    :Parameters:

    **statistic** : :obj:`~STATISTICS`

    :Returns:

        :obj:`~bool`

.. py:method:: is_time_varying_extremum_available(self, timeVarExtremum: TIME_VARYING_EXTREMUM) -> bool
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultStatistics.is_time_varying_extremum_available

    Is the supplied time varying extremum available for the data?

    :Parameters:

    **timeVarExtremum** : :obj:`~TIME_VARYING_EXTREMUM`

    :Returns:

        :obj:`~bool`

