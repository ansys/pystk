VectorGeometryToolAxesAngularOffset
===================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes created by rotating the Reference axes about the Spin vector through the specified rotation angle plus the additional rotational offset.

.. py:currentmodule:: VectorGeometryToolAxesAngularOffset

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.spin_vector`
              - Specify a spin vector.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.rotation_angle`
              - Specify a rotational angle.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.fixed_offset_angle`
              - Specify an additional rotational offset.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesAngularOffset


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.spin_vector
    :type: VectorGeometryToolVectorReference

    Specify a spin vector.

.. py:property:: rotation_angle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.rotation_angle
    :type: VectorGeometryToolAngleReference

    Specify a rotational angle.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: fixed_offset_angle
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesAngularOffset.fixed_offset_angle
    :type: float

    Specify an additional rotational offset.


