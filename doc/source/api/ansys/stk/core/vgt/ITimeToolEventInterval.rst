ITimeToolEventInterval
======================

.. py:class:: ITimeToolEventInterval

   object
   
   A single time interval.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~find_interval`
              - Return computed interval if it exists.
            * - :py:meth:`~occurred`
              - Determine if specified time falls within computed interval if it exists.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~label_start_description`
            * - :py:meth:`~label_stop_description`
            * - :py:meth:`~label_start`
            * - :py:meth:`~label_stop`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventInterval


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.type
    :type: CRDN_EVENT_INTERVAL_TYPE

    Return the type of interval.

.. py:property:: label_start_description
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.label_start_description
    :type: str

    The start description.

.. py:property:: label_stop_description
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.label_stop_description
    :type: str

    The stop description.

.. py:property:: label_start
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.label_start
    :type: str

    A label associated with the interval start.

.. py:property:: label_stop
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.label_stop
    :type: str

    A label associated with the interval stop.


Method detail
-------------






.. py:method:: find_interval(self) -> ITimeToolEventIntervalResult
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.find_interval

    Return computed interval if it exists.

    :Returns:

        :obj:`~ITimeToolEventIntervalResult`

.. py:method:: occurred(self, epoch: typing.Any) -> bool
    :canonical: ansys.stk.core.vgt.ITimeToolEventInterval.occurred

    Determine if specified time falls within computed interval if it exists.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

