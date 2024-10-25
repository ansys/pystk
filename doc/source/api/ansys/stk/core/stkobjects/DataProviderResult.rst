DataProviderResult
==================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResult

   Results returned by the data provider.

.. py:currentmodule:: DataProviderResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.category`
              - Returns a value representing the category of the result.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.value`
              - Returns the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.sections`
              - Returns a collection of sections.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.intervals`
              - Returns a collection of intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.data_sets`
              - Returns a collection of Datasets.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.message`
              - Returns the message returned with the result.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResult


Property detail
---------------

.. py:property:: category
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.category
    :type: DATA_PROVIDER_RESULT_CATEGORY

    Returns a value representing the category of the result.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.value
    :type: typing.Any

    Returns the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.

.. py:property:: sections
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.sections
    :type: DataProviderResultSubSectionCollection

    Returns a collection of sections.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.intervals
    :type: DataProviderResultIntervalCollection

    Returns a collection of intervals.

.. py:property:: data_sets
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.data_sets
    :type: DataProviderResultDataSetCollection

    Returns a collection of Datasets.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.message
    :type: DataProviderResultTextMessage

    Returns the message returned with the result.


