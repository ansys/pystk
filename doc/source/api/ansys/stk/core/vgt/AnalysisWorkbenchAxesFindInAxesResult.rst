AnalysisWorkbenchAxesFindInAxesResult
=====================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAxes.FindInAxes method.

.. py:currentmodule:: AnalysisWorkbenchAxesFindInAxesResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesResult.orientation`
              - The axes' orientation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchAxesFindInAxesResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAxesFindInAxesResult.orientation
    :type: IOrientation

    The axes' orientation.


