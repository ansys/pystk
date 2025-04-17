AnalysisWorkbenchAxesFindInAxesWithRateResult
=============================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.FindInAxesWithRate method.

.. py:currentmodule:: AnalysisWorkbenchAxesFindInAxesWithRateResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult.angular_velocity`
              - Axes' angular velocity.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult.orientation`
              - The axes' orientation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchAxesFindInAxesWithRateResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: angular_velocity
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult.angular_velocity
    :type: ICartesian3Vector

    Axes' angular velocity.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesWithRateResult.orientation
    :type: IOrientation

    The axes' orientation.


