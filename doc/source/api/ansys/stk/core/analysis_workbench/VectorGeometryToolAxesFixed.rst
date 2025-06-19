VectorGeometryToolAxesFixed
===========================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixed

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes fixed in reference axes.

.. py:currentmodule:: VectorGeometryToolAxesFixed

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixed.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixed.fixed_orientation`
              - Specify a desired orientation and the applicable parameters.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesFixed


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixed.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: fixed_orientation
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesFixed.fixed_orientation
    :type: IOrientation

    Specify a desired orientation and the applicable parameters.


