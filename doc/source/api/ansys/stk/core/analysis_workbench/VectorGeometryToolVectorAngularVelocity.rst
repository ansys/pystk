VectorGeometryToolVectorAngularVelocity
=======================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Angular velocity vector of one set of axes computed with respect to the reference set.

.. py:currentmodule:: VectorGeometryToolVectorAngularVelocity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity.axes`
              - Specify the axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorAngularVelocity


Property detail
---------------

.. py:property:: axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity.axes
    :type: VectorGeometryToolAxesReference

    Specify the axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorAngularVelocity.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


