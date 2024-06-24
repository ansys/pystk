ICalculationToolConditionSetScalarThresholds
============================================

.. py:class:: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds

   object
   
   Condition set based on single scalar calculation compared to set of threshold values.

.. py:currentmodule:: ICalculationToolConditionSetScalarThresholds

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.set_thresholds_and_labels`
              - Set thresholds and threshold labels.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.scalar`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.thresholds`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.threshold_labels`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.include_above_highest_threshold`
            * - :py:attr:`~ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.include_below_lowest_threshold`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolConditionSetScalarThresholds


Property detail
---------------

.. py:property:: scalar
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.scalar
    :type: ICalculationToolScalar

    The input scalar calculation.

.. py:property:: thresholds
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.thresholds
    :type: list

    The input threshold values, flags indicating whether to include conditions above the highest and below the lowest threhsolds, and corresponding labels.

.. py:property:: threshold_labels
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.threshold_labels
    :type: list

    The input threshold values, flags indicating whether to include conditions above the highest and below the lowest threhsolds, and corresponding labels.

.. py:property:: include_above_highest_threshold
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.include_above_highest_threshold
    :type: bool

    The threshold indicates whether to include conditions above the highest threhsold.

.. py:property:: include_below_lowest_threshold
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.include_below_lowest_threshold
    :type: bool

    The threshold indicates whether to include conditions below the lowest threhsolds.


Method detail
-------------









.. py:method:: set_thresholds_and_labels(self, thresholds: list, thresholdLabels: list) -> None
    :canonical: ansys.stk.core.vgt.ICalculationToolConditionSetScalarThresholds.set_thresholds_and_labels

    Set thresholds and threshold labels.

    :Parameters:

    **thresholds** : :obj:`~list`
    **thresholdLabels** : :obj:`~list`

    :Returns:

        :obj:`~None`

