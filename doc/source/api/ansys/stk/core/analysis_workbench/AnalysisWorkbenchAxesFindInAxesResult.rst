AnalysisWorkbenchAxesFindInAxesResult
=====================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.FindInAxes method.

.. py:currentmodule:: AnalysisWorkbenchAxesFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesResult.orientation`
              - The axes' orientation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchAxesFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: orientation
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAxesFindInAxesResult.orientation
    :type: IOrientation

    The axes' orientation.


