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
              - Return a value representing the category of the result.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.value`
              - Return the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.sections`
              - Return a collection of sections.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.intervals`
              - Return a collection of intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.data_sets`
              - Return a collection of Datasets.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResult.message`
              - Return the message returned with the result.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResult


Property detail
---------------

.. py:property:: category
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.category
    :type: DataProviderResultCategory

    Return a value representing the category of the result.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.value
    :type: typing.Any

    Return the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.

.. py:property:: sections
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.sections
    :type: DataProviderResultSubSectionCollection

    Return a collection of sections.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.intervals
    :type: DataProviderResultIntervalCollection

    Return a collection of intervals.

.. py:property:: data_sets
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.data_sets
    :type: DataProviderResultDataSetCollection

    Return a collection of Datasets.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.DataProviderResult.message
    :type: DataProviderResultTextMessage

    Return the message returned with the result.


