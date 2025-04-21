AnalysisWorkbenchAxesTransformResult
====================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.TransformFrom method.

.. py:currentmodule:: AnalysisWorkbenchAxesTransformResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformResult.vector`
              - The output vector in the current axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchAxesTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.


