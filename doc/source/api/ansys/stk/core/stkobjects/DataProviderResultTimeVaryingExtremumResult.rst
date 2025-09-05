DataProviderResultTimeVaryingExtremumResult
===========================================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult

   Results returned by time varying extremum computation.

.. py:currentmodule:: DataProviderResultTimeVaryingExtremumResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult.time`
              - Get the time when the value occurred. Use this time with the Exec methods to retrieve other element values when the statistics occurred. Uses DateFormat Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult.value`
              - Value of the time varying extremum computed. Uses the dimension of the data set used to compute the time varying extremum.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultTimeVaryingExtremumResult


Property detail
---------------

.. py:property:: time
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult.time
    :type: typing.Any

    Get the time when the value occurred. Use this time with the Exec methods to retrieve other element values when the statistics occurred. Uses DateFormat Dimension.

.. py:property:: value
    :canonical: ansys.stk.core.stkobjects.DataProviderResultTimeVaryingExtremumResult.value
    :type: float

    Value of the time varying extremum computed. Uses the dimension of the data set used to compute the time varying extremum.


