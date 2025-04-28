AnalysisWorkbenchSystemFindInSystemResult
=========================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolSystem.FindInSystem method.

.. py:currentmodule:: AnalysisWorkbenchSystemFindInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.position`
              - A position vector.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.velocity`
              - A velocity vector.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.rate`
              - Rate of change.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.orientation`
              - Orientation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchSystemFindInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.position
    :type: ICartesian3Vector

    A position vector.

.. py:property:: velocity
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.velocity
    :type: ICartesian3Vector

    A velocity vector.

.. py:property:: rate
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.rate
    :type: ICartesian3Vector

    Rate of change.

.. py:property:: orientation
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemFindInSystemResult.orientation
    :type: IOrientation

    Orientation.


