DataProviderResultInterval
==========================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultInterval

   Represents a interval in the collection of intervals returned by the data providers.

.. py:currentmodule:: DataProviderResultInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultInterval.threshold_crossings`
              - Return a two-dimensional array containing time and direction data (negative for decreasing). The DataSets property must contain the Time dataset for this method to work correctly.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultInterval.multiple_threshold_crossings`
              - Return an array of two-dimensional arrays.  Each two-dimensional array contains start and stop times based on the boundaries passed in. The DataSets property must contain the Time dataset for this method to work correctly.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultInterval.start_time`
              - Return the start time of the interval. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultInterval.stop_time`
              - Return the stop time of the interval. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultInterval.data_sets`
              - Return a collection of data sets within the interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultInterval


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.DataProviderResultInterval.start_time
    :type: typing.Any

    Return the start time of the interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.DataProviderResultInterval.stop_time
    :type: typing.Any

    Return the stop time of the interval. Uses DateFormat Dimension.

.. py:property:: data_sets
    :canonical: ansys.stk.core.stkobjects.DataProviderResultInterval.data_sets
    :type: DataProviderResultDataSetCollection

    Return a collection of data sets within the interval.


Method detail
-------------




.. py:method:: threshold_crossings(self, elem_name: str, threshold: typing.Any) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultInterval.threshold_crossings

    Return a two-dimensional array containing time and direction data (negative for decreasing). The DataSets property must contain the Time dataset for this method to work correctly.

    :Parameters:

        **elem_name** : :obj:`~str`

        **threshold** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: multiple_threshold_crossings(self, elem_name: str, thresholds: list) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultInterval.multiple_threshold_crossings

    Return an array of two-dimensional arrays.  Each two-dimensional array contains start and stop times based on the boundaries passed in. The DataSets property must contain the Time dataset for this method to work correctly.

    :Parameters:

        **elem_name** : :obj:`~str`

        **thresholds** : :obj:`~list`


    :Returns:

        :obj:`~list`

