AnalysisWorkbenchAxesTransformResult
====================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.TransformFrom method.

.. py:currentmodule:: AnalysisWorkbenchAxesTransformResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformResult.vector`
              - The output vector in the current axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchAxesTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesTransformResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.


