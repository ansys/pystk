AnalysisWorkbenchPointLocateInSystemWithRateResult
==================================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPoint.LocateInSystemWithRate method.

.. py:currentmodule:: AnalysisWorkbenchPointLocateInSystemWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult.position`
              - The point position in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult.velocity`
              - The point velocity in the specified coordinate system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchPointLocateInSystemWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult.position
    :type: ICartesian3Vector

    The point position in the specified coordinate system.

.. py:property:: velocity
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchPointLocateInSystemWithRateResult.velocity
    :type: ICartesian3Vector

    The point velocity in the specified coordinate system.


