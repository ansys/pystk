ITimeToolTimeArray
==================

.. py:class:: ansys.stk.core.vgt.ITimeToolTimeArray

   An ordered array of times, which may or may not be evenly spaced.

.. py:currentmodule:: ITimeToolTimeArray

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolTimeArray.find_times`
              - Return computed array of times.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolTimeArray.type`
              - Return the type of time array.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolTimeArray


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolTimeArray.type
    :type: EVENT_ARRAY_TYPE

    Return the type of time array.


Method detail
-------------


.. py:method:: find_times(self) -> TimeToolTimeArrayFindTimesResult
    :canonical: ansys.stk.core.vgt.ITimeToolTimeArray.find_times

    Return computed array of times.

    :Returns:

        :obj:`~TimeToolTimeArrayFindTimesResult`

