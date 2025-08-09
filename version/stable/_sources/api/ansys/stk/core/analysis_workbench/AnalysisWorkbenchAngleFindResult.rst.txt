AnalysisWorkbenchAngleFindResult
================================

.. py:class:: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchMethodCallResult`

   Represents result returned with IVectorGeometryToolAngle.FindCoordinates method.

.. py:currentmodule:: AnalysisWorkbenchAngleFindResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.is_valid`
              - Indicate whether the result object is valid.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.angle`
              - The computed angle. The value of the angle is in ``AngleUnit`` dimension.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.vector_from`
              - The first of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.vector_to`
              - The second of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.vector_about`
              - The vector the angle is rotated about.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import AnalysisWorkbenchAngleFindResult


Property detail
---------------

.. py:property:: is_valid
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.is_valid
    :type: bool

    Indicate whether the result object is valid.

.. py:property:: angle
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.angle
    :type: typing.Any

    The computed angle. The value of the angle is in ``AngleUnit`` dimension.

.. py:property:: vector_from
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.vector_from
    :type: ICartesian3Vector

    The first of the two vectors the angle is measured.

.. py:property:: vector_to
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.vector_to
    :type: ICartesian3Vector

    The second of the two vectors the angle is measured.

.. py:property:: vector_about
    :canonical: ansys.stk.core.analysis_workbench.AnalysisWorkbenchAngleFindResult.vector_about
    :type: ICartesian3Vector

    The vector the angle is rotated about.


