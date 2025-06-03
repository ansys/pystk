ICalculationToolParameterSet
============================

.. py:class:: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet

   Parameter set contains various sets of scalar computations.

.. py:currentmodule:: ICalculationToolParameterSet

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.calculate`
              - Return results of computing individual scalars within parameter set at the specified time.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.calculate_with_derivative`
              - Return results of computing individual scalars and their time derivatives within parameter set at the specified time.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.type`
              - Get the type of parameter set.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.labels`
              - Get the labels identifying hierarchy of representations within parameter set.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.dimensions`
              - Get the names identifying types of dimensions of individual scalars within parameter set.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.scalar_names`
              - Get the names identifying individual scalars within parameter set.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import ICalculationToolParameterSet


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.type
    :type: ParameterSetType

    Get the type of parameter set.

.. py:property:: labels
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.labels
    :type: list

    Get the labels identifying hierarchy of representations within parameter set.

.. py:property:: dimensions
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.dimensions
    :type: list

    Get the names identifying types of dimensions of individual scalars within parameter set.

.. py:property:: scalar_names
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.scalar_names
    :type: list

    Get the names identifying individual scalars within parameter set.


Method detail
-------------





.. py:method:: calculate(self, epoch: typing.Any) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.calculate

    Return results of computing individual scalars within parameter set at the specified time.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: calculate_with_derivative(self, epoch: typing.Any) -> list
    :canonical: ansys.stk.core.analysis_workbench.ICalculationToolParameterSet.calculate_with_derivative

    Return results of computing individual scalars and their time derivatives within parameter set at the specified time.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

