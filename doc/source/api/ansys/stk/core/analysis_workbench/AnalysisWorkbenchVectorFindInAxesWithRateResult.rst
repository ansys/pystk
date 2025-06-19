AnalysisWorkbenchVectorFindInAxesWithRateResult
===============================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolVector.FindInAxesWithRate method.

.. py:currentmodule:: AnalysisWorkbenchVectorFindInAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult.vector`
              - The vector in a specified axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult.rate`
              - The vector rate in a specified axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        AnalysisWorkbenchVectorFindInAxesWithRateResult,
    )


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult.vector
    :type: ICartesian3Vector

    The vector in a specified axes.

.. py:property:: rate
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesWithRateResult.rate
    :type: ICartesian3Vector

    The vector rate in a specified axes.


