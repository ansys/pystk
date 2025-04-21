AnalysisWorkbenchPointLocateInSystemResult
==========================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolPlane.FindInSystemWithRate method.

.. py:currentmodule:: AnalysisWorkbenchPointLocateInSystemResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemResult.position`
              - The point position in the specified coordinate system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchPointLocateInSystemResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchPointLocateInSystemResult.position
    :type: ICartesian3Vector

    The point position in the specified coordinate system.


