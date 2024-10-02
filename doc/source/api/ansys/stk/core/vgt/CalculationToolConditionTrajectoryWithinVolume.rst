CalculationToolConditionTrajectoryWithinVolume
==============================================

.. py:class:: ansys.stk.core.vgt.CalculationToolConditionTrajectoryWithinVolume

   Bases: :py:class:`~ansys.stk.core.vgt.ICalculationToolCondition`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

.. py:currentmodule:: CalculationToolConditionTrajectoryWithinVolume

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionTrajectoryWithinVolume.point`
              - Get the trajectory point from the condition.
            * - :py:attr:`~ansys.stk.core.vgt.CalculationToolConditionTrajectoryWithinVolume.constraint`
              - Get the volume constraint on trajectory point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationToolConditionTrajectoryWithinVolume


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.vgt.CalculationToolConditionTrajectoryWithinVolume.point
    :type: IVectorGeometryToolPoint

    Get the trajectory point from the condition.

.. py:property:: constraint
    :canonical: ansys.stk.core.vgt.CalculationToolConditionTrajectoryWithinVolume.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on trajectory point.


