AnalysisWorkbenchSystemFindInSystemResult
=========================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolSystem.FindInSystem method.

.. py:currentmodule:: AnalysisWorkbenchSystemFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.position`
              - A position vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.velocity`
              - A velocity vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.rate`
              - Rate of change.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.orientation`
              - Orientation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchSystemFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.position
    :type: ICartesian3Vector

    A position vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.velocity
    :type: ICartesian3Vector

    A velocity vector.

.. py:property:: rate
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.rate
    :type: ICartesian3Vector

    Rate of change.

.. py:property:: orientation
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemFindInSystemResult.orientation
    :type: IOrientation

    Orientation.


