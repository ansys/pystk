IDataProviderInterval
=====================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderInterval

   object
   
   Represents the Interval Data Provider (for instance facility lighting times).

.. py:currentmodule:: IDataProviderInterval

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInterval.exec`
              - Compute the data; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInterval.exec_elements`
              - Compute the data and return just the indicated data elements; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInterval.exec_event_array`
              - Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderInterval.exec_elements_event_array`
              - Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderInterval



Method detail
-------------

.. py:method:: exec(self, startTime: typing.Any, stopTime: typing.Any) -> IDataProviderResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderInterval.exec

    Compute the data; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDataProviderResult`

.. py:method:: exec_elements(self, startTime: typing.Any, stopTime: typing.Any, elementNames: list) -> IDataProviderResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderInterval.exec_elements

    Compute the data and return just the indicated data elements; interval data providers require an interval or list of intervals. StartTime/StopTime use DateFormat Dimension.

    :Parameters:

    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~IDataProviderResult`

.. py:method:: exec_event_array(self, pEventArray: ITimeToolEventArray, startTime: typing.Any, stopTime: typing.Any) -> IDataProviderResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderInterval.exec_event_array

    Compute the data given a Times Array component. Also requires object start and stop times, which use DateFormat Dimension.

    :Parameters:

    **pEventArray** : :obj:`~ITimeToolEventArray`
    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IDataProviderResult`

.. py:method:: exec_elements_event_array(self, pEventArray: ITimeToolEventArray, startTime: typing.Any, stopTime: typing.Any, elementNames: list) -> IDataProviderResult
    :canonical: ansys.stk.core.stkobjects.IDataProviderInterval.exec_elements_event_array

    Compute the data and returns just the indicated data elements; Input is a Times Array component, and object start and stop times. Start/Stop use DateFormat Dimension.

    :Parameters:

    **pEventArray** : :obj:`~ITimeToolEventArray`
    **startTime** : :obj:`~typing.Any`
    **stopTime** : :obj:`~typing.Any`
    **elementNames** : :obj:`~list`

    :Returns:

        :obj:`~IDataProviderResult`

