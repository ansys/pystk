CRDN_EVENT_TYPE
===============

.. py:class:: ansys.stk.core.vgt.CRDN_EVENT_TYPE

   IntEnum


.. py:currentmodule:: CRDN_EVENT_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported time instant types.

            * - :py:attr:`~EPOCH`
              - Time instant set at specified date/time.

            * - :py:attr:`~EXTREMUM`
              - Determine time of global minimum or maximum of specified scalar calculation.

            * - :py:attr:`~FROM_INTERVAL`
              - Start or stop time of selected reference interval.

            * - :py:attr:`~SIGNALED`
              - Determine what time is recorded at target clock location by performing signal transmission of original time instant between base and target clock locations.

            * - :py:attr:`~TIME_OFFSET`
              - Time instant at fixed offset from specified reference time instant.

            * - :py:attr:`~SMART_EPOCH`
              - A smart epoch.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CRDN_EVENT_TYPE


