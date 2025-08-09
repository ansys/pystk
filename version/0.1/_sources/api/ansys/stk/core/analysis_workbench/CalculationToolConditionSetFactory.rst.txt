CalculationToolConditionSetFactory
==================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory

   The factory creates condition set components.

.. py:currentmodule:: CalculationToolConditionSetFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory.create`
              - Create and registers a condition set using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory.create_scalar_thresholds`
              - Create a scalar thresholds condition set.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory.is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolConditionSetFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: ConditionSetType) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory.create

    Create and registers a condition set using specified name, description, and type.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`

        **type** : :obj:`~ConditionSetType`


    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: create_scalar_thresholds(self, name: str, description: str) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory.create_scalar_thresholds

    Create a scalar thresholds condition set.

    :Parameters:

        **name** : :obj:`~str`

        **description** : :obj:`~str`


    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: is_type_supported(self, type: ConditionSetType) -> bool
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionSetFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

        **type** : :obj:`~ConditionSetType`


    :Returns:

        :obj:`~bool`

