IDataProviderResultTimeVaryingExtremumResult
============================================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultTimeVaryingExtremumResult

   object
   
   Represents the results of computing a data set time varying extremum using IAgDrStatistics.ComputeTimeVarExtremum method.

.. py:currentmodule:: IDataProviderResultTimeVaryingExtremumResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTimeVaryingExtremumResult.value`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultTimeVaryingExtremumResult.time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultTimeVaryingExtremumResult


Property detail
---------------

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTimeVaryingExtremumResult.value
    :type: float

    Value of the time varying extremum computed. Uses the dimension of the data set used to compute the time varying extremum.

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultTimeVaryingExtremumResult.time
    :type: typing.Any

    Get the time when the value occurred. Use this time with the Exec methods to retrieve other element values when the statistics occurred. Uses DateFormat Dimension.


