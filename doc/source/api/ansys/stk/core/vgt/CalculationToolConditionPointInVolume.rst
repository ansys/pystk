CalculationToolConditionPointInVolume
=====================================

.. py:class:: ansys.stk.core.vgt.CalculationToolConditionPointInVolume

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolCondition`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

.. py:currentmodule:: CalculationToolConditionPointInVolume

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionPointInVolume.point`
              - Get the trajectory point from the condition.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionPointInVolume.constraint`
              - Get the volume constraint on trajectory point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolConditionPointInVolume


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.CalculationToolConditionPointInVolume.point
    :type: IVectorGeometryToolPoint

    Get the trajectory point from the condition.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.CalculationToolConditionPointInVolume.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on trajectory point.


