CalculationToolConditionTrajectoryWithinVolume
==============================================

.. py:class:: ansys.stk.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ICalculationToolCondition`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Defined by determining if input trajectory poiny is within extents of specified volume grid coordinate.

.. py:currentmodule:: CalculationToolConditionTrajectoryWithinVolume

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.point`
              - Get the trajectory point from the condition.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.constraint`
              - Get the volume constraint on trajectory point.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import CalculationToolConditionTrajectoryWithinVolume


Property detail
---------------

.. py:property:: point
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.point
    :type: IVectorGeometryToolPoint

    Get the trajectory point from the condition.

.. py:property:: constraint
    :canonical: ansys.stk.core.analysis_workbench.CalculationToolConditionTrajectoryWithinVolume.constraint
    :type: ISpatialAnalysisToolVolume

    Get the volume constraint on trajectory point.


