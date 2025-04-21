AnalysisWorkbenchAngleFindAngleResult
=====================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleResult

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchMethodCallResult`

   Contains the results returned with IVectorGeometryToolAngle.FindAngle method.

.. py:currentmodule:: AnalysisWorkbenchAngleFindAngleResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleResult.angle`
              - The computed angle. The value of the angle is in ``AngleUnit`` dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchAngleFindAngleResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchAngleFindAngleResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in ``AngleUnit`` dimension.


