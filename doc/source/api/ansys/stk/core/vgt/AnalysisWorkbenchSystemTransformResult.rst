AnalysisWorkbenchSystemTransformResult
======================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IAgCrdnSystem.TransformFrom and IAgCrdnSystem.TransformTo methods.

.. py:currentmodule:: AnalysisWorkbenchSystemTransformResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformResult.is_valid`
              - True indicates the method call was successful.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformResult.vector`
              - The transformed vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchSystemTransformResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformResult.is_valid
    :type: bool

    True indicates the method call was successful.

.. py:property:: vector
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchSystemTransformResult.vector
    :type: ICartesian3Vector

    The transformed vector.


