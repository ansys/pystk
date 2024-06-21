IDataProviderResult
===================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResult

   object
   
   Provide methods to access the results returned by the data provider.

.. py:currentmodule:: IDataProviderResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResult.category`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResult.value`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResult.sections`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResult.intervals`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResult.data_sets`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResult.message`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResult


Property detail
---------------

.. py:property:: category
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.category
    :type: DATA_PROVIDER_RESULT_CATEGORIES

    Returns a value representing the category of the result.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.value
    :type: typing.Any

    Returns the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.

.. py:property:: sections
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.sections
    :type: IDataProviderResultSubSectionCollection

    Returns a collection of sections.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.intervals
    :type: IDataProviderResultIntervalCollection

    Returns a collection of intervals.

.. py:property:: data_sets
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.data_sets
    :type: IDataProviderResultDataSetCollection

    Returns a collection of Datasets.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.message
    :type: IDataProviderResultTextMessage

    Returns the message returned with the result.


