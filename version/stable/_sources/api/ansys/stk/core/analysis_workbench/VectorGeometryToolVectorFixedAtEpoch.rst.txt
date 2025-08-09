VectorGeometryToolVectorFixedAtEpoch
====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Based on another vector fixed at a specified epoch.

.. py:currentmodule:: VectorGeometryToolVectorFixedAtEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch.epoch`
              - Specify an epoch.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch.source_vector`
              - Specify a source vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch.reference_axes`
              - Specify a reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorFixedAtEpoch


Property detail
---------------

.. py:property:: epoch
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch.epoch
    :type: typing.Any

    Specify an epoch.

.. py:property:: source_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch.source_vector
    :type: VectorGeometryToolVectorReference

    Specify a source vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorFixedAtEpoch.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.


