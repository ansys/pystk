ITimeToolEventIntervalCollection
================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalCollection

   object
   
   A collection of related interval lists.

.. py:currentmodule:: ITimeToolEventIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollection.find_interval_collection`
              - Return computed collection of interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollection.occurred`
              - Determine if specified time falls within any of the computed interval lists in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollection.type`
              - Return the type of collection of interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalCollection.labels`
              - Get the labels associated with the interval lists in the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalCollection


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollection.type
    :type: CRDN_EVENT_INTERVAL_COLLECTION_TYPE

    Return the type of collection of interval lists.

.. py:property:: labels
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollection.labels
    :type: list

    Get the labels associated with the interval lists in the collection.


Method detail
-------------



.. py:method:: find_interval_collection(self) -> ITimeToolIntervalsVectorResult
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollection.find_interval_collection

    Return computed collection of interval lists.

    :Returns:

        :obj:`~ITimeToolIntervalsVectorResult`

.. py:method:: occurred(self, epoch: typing.Any) -> ITimeToolEventIntervalCollectionOccurredResult
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalCollection.occurred

    Determine if specified time falls within any of the computed interval lists in the collection.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITimeToolEventIntervalCollectionOccurredResult`

