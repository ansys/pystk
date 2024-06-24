ITimeToolEventFindOccurrenceResult
==================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventFindOccurrenceResult

   object
   
   Contains the results returned with IAgCrdnEvent.FindOccurrence method.

.. py:currentmodule:: ITimeToolEventFindOccurrenceResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventFindOccurrenceResult.is_valid`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventFindOccurrenceResult.epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventFindOccurrenceResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.ITimeToolEventFindOccurrenceResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.ITimeToolEventFindOccurrenceResult.epoch
    :type: typing.Any

    The epoch at which the event occurs.


