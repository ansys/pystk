AnalysisWorkbenchVectorFindInAxesResult
=======================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolVector.FindInAxes method.

.. py:currentmodule:: AnalysisWorkbenchVectorFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesResult.vector`
              - The vector in a specified axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchVectorFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchVectorFindInAxesResult.vector
    :type: ICartesian3Vector

    The vector in a specified axes.


