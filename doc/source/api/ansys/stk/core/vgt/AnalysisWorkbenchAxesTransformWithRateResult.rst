AnalysisWorkbenchAxesTransformWithRateResult
============================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IAgCrdnAxes.TransformFromWithRate method.

.. py:currentmodule:: AnalysisWorkbenchAxesTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult.is_valid`
              - Indicates whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult.vector`
              - The output vector in the current axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult.velocity`
              - The vector velocity.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchAxesTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult.is_valid
    :type: bool

    Indicates whether the result object is valid.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult.vector
    :type: ICartesian3Vector

    The output vector in the current axes.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector velocity.


