VectorGeometryToolAxesAtTimeInstant
===================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`

   Axes orientation fixed relative to reference axes based on orientation of another set of axes evaluated at specified time instant.

.. py:currentmodule:: VectorGeometryToolAxesAtTimeInstant

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant.reference_axes`
              - A reference axes. Can be any VGT axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant.reference_time_instant`
              - A reference time instant. Can be any Time event.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant.source_axes`
              - A base axes defining the orientation. Can be any VGT axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesAtTimeInstant


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant.reference_axes
    :type: IVectorGeometryToolAxes

    A reference axes. Can be any VGT axes.

.. py:property:: reference_time_instant
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant.reference_time_instant
    :type: ITimeToolInstant

    A reference time instant. Can be any Time event.

.. py:property:: source_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAtTimeInstant.source_axes
    :type: IVectorGeometryToolAxes

    A base axes defining the orientation. Can be any VGT axes.


