IDataProviderResultDataSet
==========================

.. py:class:: ansys.stk.core.stkobjects.IDataProviderResultDataSet

   object
   
   Represents a dataset element.

.. py:currentmodule:: IDataProviderResultDataSet

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.get_values`
              - Retrieve an array of values of the elements in the dataset.
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.get_internal_unit_values`
              - Get the Internal Unit Values of the Data.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.element_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.element_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.dimension_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IDataProviderResultDataSet.statistics`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IDataProviderResultDataSet


Property detail
---------------

.. py:property:: element_name
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.element_name
    :type: str

    Returns a name of the dataset.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.element_type
    :type: int

    Returns a type of elements of the dataset. Dimensionless.

.. py:property:: dimension_name
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.dimension_name
    :type: str

    Returns the dimension of elements of the dataset.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.count
    :type: int

    Returns a number of elements in the dataset. Dimensionless.

.. py:property:: statistics
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.statistics
    :type: IDataProviderResultStatistics

    Returns an interface for computing statistics on the results.


Method detail
-------------





.. py:method:: get_values(self) -> list
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.get_values

    Retrieve an array of values of the elements in the dataset.

    :Returns:

        :obj:`~list`

.. py:method:: get_internal_unit_values(self) -> list
    :canonical: ansys.stk.core.stkobjects.IDataProviderResultDataSet.get_internal_unit_values

    Get the Internal Unit Values of the Data.

    :Returns:

        :obj:`~list`


