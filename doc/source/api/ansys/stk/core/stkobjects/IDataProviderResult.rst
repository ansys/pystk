IDataProviderResult
===================

.. py:class:: IDataProviderResult

   object
   
   Provide methods to access the results returned by the data provider.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~category`
            * - :py:meth:`~value`
            * - :py:meth:`~sections`
            * - :py:meth:`~intervals`
            * - :py:meth:`~data_sets`
            * - :py:meth:`~message`


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
    :type: IAgDrSubSectionCollection

    Returns a collection of sections.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.intervals
    :type: IAgDrIntervalCollection

    Returns a collection of intervals.

.. py:property:: data_sets
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.data_sets
    :type: IAgDrDataSetCollection

    Returns a collection of Datasets.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.IDataProviderResult.message
    :type: IAgDrTextMessage

    Returns the message returned with the result.


