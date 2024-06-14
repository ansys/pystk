IDataProviderTimeVarying
========================

.. py:class:: IDataProviderTimeVarying

   object
   
   Represents the Time-dependent Data Provider (for instance satellite position).

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~exec`
              - Compute the data; time-dependent data providers require an interval and a time step. Start/Stop use DateFormat Dimension. StepTime uses Time Dimension.
            * - :py:meth:`~exec_elements`
              - Compute the data and return just the indicated data elements; time-dependent data providers require an interval and a time step.
            * - :py:meth:`~exec_single`
              - Compute the data given a single Time. SingleTime uses DateFormat Dimension.
            * - :py:meth:`~exec_single_elements`
              - Compute the data given a single Time and return just the indicated data elements. SingleTime uses DateFormat Dimension.
            * - :py:meth:`~exec_single_elements_array`
              - Compute the data given a single Time array and return just the indicated data elements. If time values without data are requested, null entries will be returned in the data array. SingleTime uses DateFormat Dimension.
            * - :py:meth:`~exec_native_times`
              - Compute the data for default; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~exec_elements_native_times`
              - Compute the data for default; return just the indicated data elements; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~exec_event_array`
              - Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.
            * - :py:meth:`~exec_elements_event_array`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.
            * - :py:meth:`~exec_elements_event_array_only`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderTimeVarying



Method detail
-------------

.. py:method:: exec(self, startTime:typing.Any, stopTime:typing.Any, stepTime:float) -> "IDataProviderResult"

    Compute the data; time-dependent data providers require an interval and a time step. Start/Stop use DateFormat Dimension. StepTime uses Time Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **stepTime** : :obj:`~float`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_elements(self, startTime:typing.Any, stopTime:typing.Any, stepTime:float, elementNames:list) -> "IDataProviderResult"

    Compute the data and return just the indicated data elements; time-dependent data providers require an interval and a time step.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **stepTime** : :obj:`~float`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_single(self, singleTime:typing.Any) -> "IDataProviderResult"

    Compute the data given a single Time. SingleTime uses DateFormat Dimension.

    :Parameters:

    **singleTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_single_elements(self, singleTime:typing.Any, elementNames:list) -> "IDataProviderResult"

    Compute the data given a single Time and return just the indicated data elements. SingleTime uses DateFormat Dimension.

    :Parameters:

    **singleTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_single_elements_array(self, timeArray:list, elementNames:list) -> "IDataProviderResultTimeArrayElements"

    Compute the data given a single Time array and return just the indicated data elements. If time values without data are requested, null entries will be returned in the data array. SingleTime uses DateFormat Dimension.

    :Parameters:

    **timeArray** : :obj:`~list`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~"IDataProviderResultTimeArrayElements"`

.. py:method:: exec_native_times(self, startTime:typing.Any, stopTime:typing.Any) -> "IDataProviderResult"

    Compute the data for default; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_elements_native_times(self, startTime:typing.Any, stopTime:typing.Any, elementNames:list) -> "IDataProviderResult"

    Compute the data for default; return just the indicated data elements; default time-dependent data providers require an interval. Start/Stop use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_event_array(self, pEventArray:"ITimeToolEventArray", startTime:typing.Any, stopTime:typing.Any) -> "IDataProviderResult"

    Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.

    :Parameters:

    **pEventArray** : :obj:`~"ITimeToolEventArray"`
    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_elements_event_array(self, pEventArray:"ITimeToolEventArray", startTime:typing.Any, stopTime:typing.Any, elementNames:list) -> "IDataProviderResult"

    Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.

    :Parameters:

    **pEventArray** : :obj:`~"ITimeToolEventArray"`
    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~"IDataProviderResult"`

.. py:method:: exec_elements_event_array_only(self, pEventArray:"ITimeToolEventArray", elementNames:list) -> "IDataProviderResult"

    Compute the data and returns just the indicated data elements; Input is a Times Array component.

    :Parameters:

    **pEventArray** : :obj:`~"ITimeToolEventArray"`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~"IDataProviderResult"`

