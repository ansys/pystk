IDataProviderResultInterval
===========================

.. py:class:: IDataProviderResultInterval

   object
   
   Represents a data interval element.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~threshold_crossings`
              - Return a two-dimensional array containing time and direction data (negative for decreasing). The DataSets property must contain the Time dataset for this method to work correctly.
            * - :py:meth:`~multiple_threshold_crossings`
              - Return an array of two-dimensional arrays.  Each two-dimensional array contains start and stop times based on the boundaries passed in. The DataSets property must contain the Time dataset for this method to work correctly.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~data_sets`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultInterval


Property detail
---------------

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultInterval.start_time
    :type: typing.Any

    Returns the start time of the interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultInterval.stop_time
    :type: typing.Any

    Returns the stop time of the interval. Uses DateFormat Dimension.

.. py:property:: data_sets
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultInterval.data_sets
    :type: "IAgDrDataSetCollection"

    Returns a collection of data sets within the interval.


Method detail
-------------




.. py:method:: threshold_crossings(self, elemName:str, threshold:typing.Any) -> list

    Return a two-dimensional array containing time and direction data (negative for decreasing). The DataSets property must contain the Time dataset for this method to work correctly.

    :Parameters:

    **elemName** : :obj:`~str`
    **threshold** : :obj:`~typing.Any`

    :Returns:

        :obj:`~list`

.. py:method:: multiple_threshold_crossings(self, elemName:str, thresholds:list) -> list

    Return an array of two-dimensional arrays.  Each two-dimensional array contains start and stop times based on the boundaries passed in. The DataSets property must contain the Time dataset for this method to work correctly.

    :Parameters:

    **elemName** : :obj:`~str`
    **thresholds** : :obj:`~list`

    :Returns:

        :obj:`~list`

