VectorGeometryToolAxesCustomScript
==================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCustomScript

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Customized axes offset with respect to a set of reference Axes.

.. py:currentmodule:: VectorGeometryToolAxesCustomScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCustomScript.filename`
              - Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCustomScript.reference_axes`
              - Specify a reference axes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesCustomScript


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCustomScript.filename
    :type: str

    Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCustomScript.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.


