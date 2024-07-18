CalculationToolConditionSetFactory
==================================

.. py:class:: ansys.stk.core.vgt.CalculationToolConditionSetFactory

   Bases: 

   The factory creates condition set components.

.. py:currentmodule:: CalculationToolConditionSetFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetFactory.create`
              - Create and registers a condition set using specified name, description, and type.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetFactory.create_scalar_thresholds`
              - Create a scalar thresholds condition set.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionSetFactory.is_type_supported`
              - Return whether the specified type is supported.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolConditionSetFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_CONDITION_SET_TYPE) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetFactory.create

    Create and registers a condition set using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_CONDITION_SET_TYPE`

    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: create_scalar_thresholds(self, name: str, description: str) -> ICalculationToolConditionSet
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetFactory.create_scalar_thresholds

    Create a scalar thresholds condition set.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolConditionSet`

.. py:method:: is_type_supported(self, eType: CRDN_CONDITION_SET_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.CalculationToolConditionSetFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_CONDITION_SET_TYPE`

    :Returns:

        :obj:`~bool`

