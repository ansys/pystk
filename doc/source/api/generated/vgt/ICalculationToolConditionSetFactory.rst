ICalculationToolConditionSetFactory
===================================

.. py:class:: ICalculationToolConditionSetFactory

   object
   
   The factory creates condition set components.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create`
              - Create and registers a condition set using specified name, description, and type.
            * - :py:meth:`~create_scalar_thresholds`
              - Create a scalar thresholds condition set.
            * - :py:meth:`~is_type_supported`
              - Return whether the specified type is supported.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionSetFactory



Method detail
-------------

.. py:method:: create(self, name:str, description:str, type:"CRDN_CONDITION_SET_TYPE") -> "ICalculationToolConditionSet"

    Create and registers a condition set using specified name, description, and type.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`
    **type** : :obj:`~"CRDN_CONDITION_SET_TYPE"`

    :Returns:

        :obj:`~"ICalculationToolConditionSet"`

.. py:method:: create_scalar_thresholds(self, name:str, description:str) -> "ICalculationToolConditionSet"

    Create a scalar thresholds condition set.

    :Parameters:

    **name** : :obj:`~str`
    **description** : :obj:`~str`

    :Returns:

        :obj:`~"ICalculationToolConditionSet"`

.. py:method:: is_type_supported(self, eType:"CRDN_CONDITION_SET_TYPE") -> bool

    Return whether the specified type is supported.

    :Parameters:

    **eType** : :obj:`~"CRDN_CONDITION_SET_TYPE"`

    :Returns:

        :obj:`~bool`

