ITimeToolTimeIntervalCollection
===============================

.. py:class:: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection

   A collection of related interval lists.

.. py:currentmodule:: ITimeToolTimeIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.find_interval_collection`
              - Return computed collection of interval lists.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.occurred`
              - Determine if specified time falls within any of the computed interval lists in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.labels`
              - Get the labels associated with the interval lists in the collection.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.type`
              - Return the type of collection of interval lists.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import ITimeToolTimeIntervalCollection


Property detail
---------------

.. py:property:: labels
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.labels
    :type: list

    Get the labels associated with the interval lists in the collection.

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.type
    :type: EventIntervalCollectionType

    Return the type of collection of interval lists.


Method detail
-------------

.. py:method:: find_interval_collection(self) -> TimeToolIntervalsVectorResult
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.find_interval_collection

    Return computed collection of interval lists.

    :Returns:

        :obj:`~TimeToolIntervalsVectorResult`


.. py:method:: occurred(self, epoch: typing.Any) -> TimeToolTimeIntervalCollectionOccurredResult
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalCollection.occurred

    Determine if specified time falls within any of the computed interval lists in the collection.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~TimeToolTimeIntervalCollectionOccurredResult`


