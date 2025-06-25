VectorGeometryToolVectorVelocityAcceleration
============================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`

   Velocity vector of a point in a coordinate system.

.. py:currentmodule:: VectorGeometryToolVectorVelocityAcceleration

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration.reference_system`
              - A reference (coordinate) system. Can be any VGT system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration.point`
              - A point which velocity this vector represents. Can be any VGT point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration.differencing_time_step`
              - Time step used in numerical evaluation of derivatives using central differencing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorVelocityAcceleration


Property detail
---------------

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration.reference_system
    :type: IVectorGeometryToolSystem

    A reference (coordinate) system. Can be any VGT system.

.. py:property:: point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration.point
    :type: IVectorGeometryToolPoint

    A point which velocity this vector represents. Can be any VGT point.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorVelocityAcceleration.differencing_time_step
    :type: float

    Time step used in numerical evaluation of derivatives using central differencing.


