DataProviderTimeVarying
=======================

.. py:class:: ansys.stk.core.stkobjects.DataProviderTimeVarying

   Bases: :py:class:`~ansys.stk.core.stkobjects.IDataProvider`, :py:class:`~ansys.stk.core.stkobjects.IDataProviderInfo`

   Support for time-dependent data providers (e.g. Satellite position).

.. py:currentmodule:: DataProviderTimeVarying

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute`
              - Compute the data; time-dependent data providers require an interval and a time step. Start/Stop use DateFormat Dimension. StepTime uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements`
              - Compute the data and return just the indicated data elements; time-dependent data providers require an interval and a time step.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_single`
              - Compute the data given a single Time. SingleTime uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_single_elements`
              - Compute the data given a single Time and return just the indicated data elements. SingleTime uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_single_elements_array`
              - Compute the data given a single Time array and return just the indicated data elements. If time values without data are requested, null entries will be returned in the data array. SingleTime uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_native_times`
              - Compute the data for default; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements_native_times`
              - Compute the data for default; return just the indicated data elements; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_event_array`
              - Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements_event_array`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements_event_array_only`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderTimeVarying



Method detail
-------------

.. py:method:: execute(self, start_time: typing.Any, stop_time: typing.Any, step_time: float) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute

    Compute the data; time-dependent data providers require an interval and a time step. Start/Stop use DateFormat Dimension. StepTime uses Time Dimension.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`
    **step_time** : :obj:`~float`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements(self, start_time: typing.Any, stop_time: typing.Any, step_time: float, element_names: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements

    Compute the data and return just the indicated data elements; time-dependent data providers require an interval and a time step.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`
    **step_time** : :obj:`~float`
    **element_names** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_single(self, single_time: typing.Any) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_single

    Compute the data given a single Time. SingleTime uses DateFormat Dimension.

    :Parameters:

    **single_time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_single_elements(self, single_time: typing.Any, element_names: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_single_elements

    Compute the data given a single Time and return just the indicated data elements. SingleTime uses DateFormat Dimension.

    :Parameters:

    **single_time** : :obj:`~typing.Any`
    **element_names** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_single_elements_array(self, time_array: list, element_names: list) -> DataProviderResultTimeArrayElements
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_single_elements_array

    Compute the data given a single Time array and return just the indicated data elements. If time values without data are requested, null entries will be returned in the data array. SingleTime uses DateFormat Dimension.

    :Parameters:

    **time_array** : :obj:`~list`
    **element_names** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResultTimeArrayElements`

.. py:method:: execute_native_times(self, start_time: typing.Any, stop_time: typing.Any) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_native_times

    Compute the data for default; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements_native_times(self, start_time: typing.Any, stop_time: typing.Any, element_names: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements_native_times

    Compute the data for default; return just the indicated data elements; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.

    :Parameters:

    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`
    **element_names** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_event_array(self, event_array: ITimeToolTimeArray, start_time: typing.Any, stop_time: typing.Any) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_event_array

    Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.

    :Parameters:

    **event_array** : :obj:`~ITimeToolTimeArray`
    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements_event_array(self, event_array: ITimeToolTimeArray, start_time: typing.Any, stop_time: typing.Any, element_names: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements_event_array

    Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.

    :Parameters:

    **event_array** : :obj:`~ITimeToolTimeArray`
    **start_time** : :obj:`~typing.Any`
    **stop_time** : :obj:`~typing.Any`
    **element_names** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: execute_elements_event_array_only(self, event_array: ITimeToolTimeArray, element_names: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.execute_elements_event_array_only

    Compute the data and returns just the indicated data elements; Input is a Times Array component.

    :Parameters:

    **event_array** : :obj:`~ITimeToolTimeArray`
    **element_names** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

