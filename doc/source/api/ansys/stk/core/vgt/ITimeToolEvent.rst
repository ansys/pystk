ITimeToolEvent
==============

.. py:class:: ITimeToolEvent

   object
   
   Define an event (time instant).

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_occurrence`
              - Return computed time instance if it occurs.
            * - :py:meth:`~occurs_before`
              - Return true if computed time instance occurs before or at specified time, return false otherwise.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~today`
            * - :py:meth:`~tomorrow`
            * - :py:meth:`~noon_today`
            * - :py:meth:`~noon_tomorrow`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEvent


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolEvent.type
    :type: "CRDN_EVENT_TYPE"

    Return the type of time instant.

.. py:property:: today
    :canonical: ansys.stk.core.vgt.ITimeToolEvent.today
    :type: "IAgCrdnEvent"

    Return time instant that corresponds to today's GMT midnight.

.. py:property:: tomorrow
    :canonical: ansys.stk.core.vgt.ITimeToolEvent.tomorrow
    :type: "IAgCrdnEvent"

    Return time instant that corresponds to tomorrow's GMT midnight.

.. py:property:: noon_today
    :canonical: ansys.stk.core.vgt.ITimeToolEvent.noon_today
    :type: "IAgCrdnEvent"

    Return time instant that corresponds to today's GMT noon.

.. py:property:: noon_tomorrow
    :canonical: ansys.stk.core.vgt.ITimeToolEvent.noon_tomorrow
    :type: "IAgCrdnEvent"

    Return time instant that corresponds to tomorrow's GMT noon.


Method detail
-------------






.. py:method:: find_occurrence(self) -> "ITimeToolEventFindOccurrenceResult"

    Return computed time instance if it occurs.

    :Returns:

        :obj:`~"ITimeToolEventFindOccurrenceResult"`

.. py:method:: occurs_before(self, epoch:typing.Any) -> bool

    Return true if computed time instance occurs before or at specified time, return false otherwise.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

