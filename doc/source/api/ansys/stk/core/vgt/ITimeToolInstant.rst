ITimeToolInstant
================

.. py:class:: ansys.stk.core.vgt.ITimeToolInstant

   Define an event (time instant).

.. py:currentmodule:: ITimeToolInstant

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.find_occurrence`
              - Return computed time instance if it occurs.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.occurs_before`
              - Return true if computed time instance occurs before or at specified time, return false otherwise.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.type`
              - Return the type of time instant.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.today`
              - Return time instant that corresponds to today's GMT midnight.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.tomorrow`
              - Return time instant that corresponds to tomorrow's GMT midnight.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.noon_today`
              - Return time instant that corresponds to today's GMT noon.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolInstant.noon_tomorrow`
              - Return time instant that corresponds to tomorrow's GMT noon.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolInstant


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.type
    :type: TimeEventType

    Return the type of time instant.

.. py:property:: today
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.today
    :type: ITimeToolInstant

    Return time instant that corresponds to today's GMT midnight.

.. py:property:: tomorrow
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.tomorrow
    :type: ITimeToolInstant

    Return time instant that corresponds to tomorrow's GMT midnight.

.. py:property:: noon_today
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.noon_today
    :type: ITimeToolInstant

    Return time instant that corresponds to today's GMT noon.

.. py:property:: noon_tomorrow
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.noon_tomorrow
    :type: ITimeToolInstant

    Return time instant that corresponds to tomorrow's GMT noon.


Method detail
-------------






.. py:method:: find_occurrence(self) -> TimeToolInstantOccurrenceResult
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.find_occurrence

    Return computed time instance if it occurs.

    :Returns:

        :obj:`~TimeToolInstantOccurrenceResult`

.. py:method:: occurs_before(self, epoch: typing.Any) -> bool
    :canonical: ansys.stk.core.vgt.ITimeToolInstant.occurs_before

    Return true if computed time instance occurs before or at specified time, return false otherwise.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

