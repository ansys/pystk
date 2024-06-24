ITimeToolEventArray
===================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventArray

   object
   
   An ordered array of times, which may or may not be evenly spaced.

.. py:currentmodule:: ITimeToolEventArray

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArray.find_times`
              - Return computed array of times.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventArray.type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventArray


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolEventArray.type
    :type: CRDN_EVENT_ARRAY_TYPE

    Return the type of time array.


Method detail
-------------


.. py:method:: find_times(self) -> ITimeToolFindTimesResult
    :canonical: ansys.stk.core.vgt.ITimeToolEventArray.find_times

    Return computed array of times.

    :Returns:

        :obj:`~ITimeToolFindTimesResult`

