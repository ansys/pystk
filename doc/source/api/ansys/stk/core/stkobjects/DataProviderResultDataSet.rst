DataProviderResultDataSet
=========================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultDataSet

   Represents a dataset in the collection of datasets returned by the data providers.

.. py:currentmodule:: DataProviderResultDataSet

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.get_values`
              - Retrieve an array of values of the elements in the dataset.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.get_internal_units_values`
              - Get the Internal Unit Values of the Data.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.element_name`
              - Returns a name of the dataset.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.element_type`
              - Returns a type of elements of the dataset. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.dimension_name`
              - Returns the dimension of elements of the dataset.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.count`
              - Returns a number of elements in the dataset. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSet.statistics`
              - Returns an interface for computing statistics on the results.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultDataSet


Property detail
---------------

.. py:property:: element_name
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.element_name
    :type: str

    Returns a name of the dataset.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.element_type
    :type: int

    Returns a type of elements of the dataset. Dimensionless.

.. py:property:: dimension_name
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.dimension_name
    :type: str

    Returns the dimension of elements of the dataset.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.count
    :type: int

    Returns a number of elements in the dataset. Dimensionless.

.. py:property:: statistics
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.statistics
    :type: DataProviderResultStatistics

    Returns an interface for computing statistics on the results.


Method detail
-------------





.. py:method:: get_values(self) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.get_values

    Retrieve an array of values of the elements in the dataset.

    :Returns:

        :obj:`~list`

.. py:method:: get_internal_units_values(self) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSet.get_internal_units_values

    Get the Internal Unit Values of the Data.

    :Returns:

        :obj:`~list`


