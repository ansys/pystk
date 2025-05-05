AnalysisWorkbenchSystemTransformWithRateResult
==============================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolSystem.TransformFromWithRate and IVectorGeometryToolSystem.TransformToWithRate methods.

.. py:currentmodule:: AnalysisWorkbenchSystemTransformWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult.vector`
              - The transformed vector.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult.velocity`
              - The vector's velocity.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchSystemTransformWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult.vector
    :type: ICartesian3Vector

    The transformed vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformWithRateResult.velocity
    :type: ICartesian3Vector

    The vector's velocity.


