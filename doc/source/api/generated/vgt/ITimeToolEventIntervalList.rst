ITimeToolEventIntervalList
==========================

.. py:class:: ITimeToolEventIntervalList

   object
   
   An ordered list of time intervals.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_intervals`
              - Return computed interval list that can be empty.
            * - :py:meth:`~occurred`
              - Determine if specified time falls within computed interval list.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~labels`
            * - :py:meth:`~descriptions`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalList


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalList.type
    :type: "CRDN_EVENT_INTERVAL_LIST_TYPE"

    Return the type of interval list.

.. py:property:: labels
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalList.labels
    :type: list

    Get the label descriptions associated with the interval list.

.. py:property:: descriptions
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalList.descriptions
    :type: list

    Get the labels associated with the interval list.


Method detail
-------------




.. py:method:: find_intervals(self) -> "ITimeToolIntervalListResult"

    Return computed interval list that can be empty.

    :Returns:

        :obj:`~"ITimeToolIntervalListResult"`

.. py:method:: occurred(self, epoch:typing.Any) -> bool

    Determine if specified time falls within computed interval list.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

