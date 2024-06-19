ICalculationToolConditionFactory
================================

.. py:class:: ICalculationToolConditionFactory

   object
   
   The factory creates condition components.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and registers a condition using specified name, description and type.
            * - :py:meth:`~create_condition_scalar_bounds`
              - Create a condition placing bounds on specified scalar.
            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.
            * - :py:meth:`~create_condition_combined`
              - Create a condition which combines multiple conditions.
            * - :py:meth:`~create_condition_point_in_volume`
              - Create a condition for point in volume.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionFactory



Method detail
-------------

.. py:method:: create(self, name: str, description: str, type: CRDN_CONDITION_TYPE) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionFactory.create

    Create and registers a condition using specified name, description and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~CRDN_CONDITION_TYPE`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: create_condition_scalar_bounds(self, name: str, description: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionFactory.create_condition_scalar_bounds

    Create a condition placing bounds on specified scalar.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: is_type_supported(self, eType: CRDN_CONDITION_TYPE) -> bool
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionFactory.is_type_supported

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~CRDN_CONDITION_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: create_condition_combined(self, name: str, description: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionFactory.create_condition_combined

    Create a condition which combines multiple conditions.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

.. py:method:: create_condition_point_in_volume(self, name: str, description: str) -> ICalculationToolCondition
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionFactory.create_condition_point_in_volume

    Create a condition for point in volume.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~ICalculationToolCondition`

