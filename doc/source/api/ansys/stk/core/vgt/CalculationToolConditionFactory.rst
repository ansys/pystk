CalculationToolConditionFactory
===============================

.. py:class:: ansys.stk.core.vgt.CalculationToolConditionFactory

   The factory creates condition components.

.. py:currentmodule:: CalculationToolConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionFactory.create`
              - Create and registers a condition using specified name, description and type.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionFactory.create_scalar_bounds`
              - Create a condition placing bounds on specified scalar.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionFactory.is_type_supported`
              - Return whether the specified type is supported.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionFactory.create_combined`
              - Create a condition which combines multiple conditions.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionFactory.create_trajectory_within_volume`
              - Create a condition for point in volume.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolConditionFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CONDITION_TYPE) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.CalculationToolConditionFactory.create

    Create and registers a condition using specified name, description and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CONDITION_TYPE`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: create_scalar_bounds(self, name: str, description: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.CalculationToolConditionFactory.create_scalar_bounds

    Create a condition placing bounds on specified scalar.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: is_type_supported(self, type: CONDITION_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.CalculationToolConditionFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **type** : :obj:`~CONDITION_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_combined(self, name: str, description: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.CalculationToolConditionFactory.create_combined

    Create a condition which combines multiple conditions.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: create_trajectory_within_volume(self, name: str, description: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.CalculationToolConditionFactory.create_trajectory_within_volume

    Create a condition for point in volume.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

