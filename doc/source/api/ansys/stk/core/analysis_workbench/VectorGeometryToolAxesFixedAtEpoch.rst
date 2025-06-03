VectorGeometryToolAxesFixedAtEpoch
==================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes based on another set fixed at a specified epoch.

.. py:currentmodule:: VectorGeometryToolAxesFixedAtEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch.source_axes`
              - Specify a source axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch.epoch`
              - Specify an epoch.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesFixedAtEpoch


Property detail
---------------

.. py:property:: source_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch.source_axes
    :type: VectorGeometryToolAxesReference

    Specify a source axes.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: epoch
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixedAtEpoch.epoch
    :type: typing.Any

    Specify an epoch.


