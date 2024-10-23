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

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec`
              - Compute the data; time-dependent data providers require an interval and a time step. Start/Stop use DateFormat Dimension. StepTime uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements`
              - Compute the data and return just the indicated data elements; time-dependent data providers require an interval and a time step.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_single`
              - Compute the data given a single Time. SingleTime uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_single_elements`
              - Compute the data given a single Time and return just the indicated data elements. SingleTime uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_single_elements_array`
              - Compute the data given a single Time array and return just the indicated data elements. If time values without data are requested, null entries will be returned in the data array. SingleTime uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_native_times`
              - Compute the data for default; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements_native_times`
              - Compute the data for default; return just the indicated data elements; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_event_array`
              - Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements_event_array`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements_event_array_only`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderTimeVarying



Method detail
-------------

.. py:method:: exec(self, startTime: typing.Any, stopTime: typing.Any, stepTime: float) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec

    Compute the data; time-dependent data providers require an interval and a time step. Start/Stop use DateFormat Dimension. StepTime uses Time Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **stepTime** : :obj:`~float`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_elements(self, startTime: typing.Any, stopTime: typing.Any, stepTime: float, elementNames: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements

    Compute the data and return just the indicated data elements; time-dependent data providers require an interval and a time step.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **stepTime** : :obj:`~float`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_single(self, singleTime: typing.Any) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_single

    Compute the data given a single Time. SingleTime uses DateFormat Dimension.

    :Parameters:

    **singleTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_single_elements(self, singleTime: typing.Any, elementNames: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_single_elements

    Compute the data given a single Time and return just the indicated data elements. SingleTime uses DateFormat Dimension.

    :Parameters:

    **singleTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_single_elements_array(self, timeArray: list, elementNames: list) -> DataProviderResultTimeArrayElements
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_single_elements_array

    Compute the data given a single Time array and return just the indicated data elements. If time values without data are requested, null entries will be returned in the data array. SingleTime uses DateFormat Dimension.

    :Parameters:

    **timeArray** : :obj:`~list`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResultTimeArrayElements`

.. py:method:: exec_native_times(self, startTime: typing.Any, stopTime: typing.Any) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_native_times

    Compute the data for default; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_elements_native_times(self, startTime: typing.Any, stopTime: typing.Any, elementNames: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements_native_times

    Compute the data for default; return just the indicated data elements; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_event_array(self, pEventArray: ITimeToolTimeArray, startTime: typing.Any, stopTime: typing.Any) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_event_array

    Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.

    :Parameters:

    **pEventArray** : :obj:`~ITimeToolTimeArray`
    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_elements_event_array(self, pEventArray: ITimeToolTimeArray, startTime: typing.Any, stopTime: typing.Any, elementNames: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements_event_array

    Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.

    :Parameters:

    **pEventArray** : :obj:`~ITimeToolTimeArray`
    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

.. py:method:: exec_elements_event_array_only(self, pEventArray: ITimeToolTimeArray, elementNames: list) -> DataProviderResult
    :canonical: ansys.stk.core.stkobjects.DataProviderTimeVarying.exec_elements_event_array_only

    Compute the data and returns just the indicated data elements; Input is a Times Array component.

    :Parameters:

    **pEventArray** : :obj:`~ITimeToolTimeArray`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~DataProviderResult`

