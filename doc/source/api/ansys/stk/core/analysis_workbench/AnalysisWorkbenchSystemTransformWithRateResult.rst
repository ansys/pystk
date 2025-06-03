AnalysisWorkbenchSystemTransformWithRateResult
==============================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolSystem.TransformFromWithRate and IVectorGeometryToolSystem.TransformToWithRate methods.

.. py:currentmodule:: AnalysisWorkbenchSystemTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.vector`
              - The transformed vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.velocity`
              - The vector's velocity.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchSystemTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.vector
    :type: ICartesian3Vector

    The transformed vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchSystemTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector's velocity.


