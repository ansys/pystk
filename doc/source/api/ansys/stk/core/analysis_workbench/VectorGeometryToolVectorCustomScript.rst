VectorGeometryToolVectorCustomScript
====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Customized vector components defined with respect to reference axes.

.. py:currentmodule:: VectorGeometryToolVectorCustomScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript.script_file`
              - Specify a script file.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript.initialization_script_file`
              - Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorCustomScript


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: script_file
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript.script_file
    :type: str

    Specify a script file.

.. py:property:: initialization_script_file
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorCustomScript.initialization_script_file
    :type: str

    Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.


