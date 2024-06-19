ITimeIntervalDisplayConditionFactory
====================================

.. py:class:: ITimeIntervalDisplayConditionFactory

   object
   
   Define an inclusive time interval that determines when an object, such as a primitive, is rendered based on the current animation time .

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default time display condition. minimum time is set to JulianDate.MinValue and maximum time is set to JulianDate.MaxValue. With this interval, an object is always rendered regardless of the current animation time.
            * - :py:meth:`~initialize_with_times`
              - Initialize a time display condition with the inclusive time interval [minimumTime, maximumTime]...
            * - :py:meth:`~initialize_with_time_interval`
              - Initialize a time display condition with a time interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITimeIntervalDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> ITimeIntervalDisplayCondition
    :canonical: ansys.stk.core.graphics.ITimeIntervalDisplayConditionFactory.initialize

    Initialize a default time display condition. minimum time is set to JulianDate.MinValue and maximum time is set to JulianDate.MaxValue. With this interval, an object is always rendered regardless of the current animation time.

    :Returns:

        :obj:`~ITimeIntervalDisplayCondition`

.. py:method:: initialize_with_times(self, minimumTime: IDate, maximumTime: IDate) -> ITimeIntervalDisplayCondition
    :canonical: ansys.stk.core.graphics.ITimeIntervalDisplayConditionFactory.initialize_with_times

    Initialize a time display condition with the inclusive time interval [minimumTime, maximumTime]...

    :Parameters:

    **minimumTime** : :obj:`~IDate`
    **maximumTime** : :obj:`~IDate`

    :Returns:

        :obj:`~ITimeIntervalDisplayCondition`

.. py:method:: initialize_with_time_interval(self, timeInterval: list) -> ITimeIntervalDisplayCondition
    :canonical: ansys.stk.core.graphics.ITimeIntervalDisplayConditionFactory.initialize_with_time_interval

    Initialize a time display condition with a time interval.

    :Parameters:

    **timeInterval** : :obj:`~list`

    :Returns:

        :obj:`~ITimeIntervalDisplayCondition`

