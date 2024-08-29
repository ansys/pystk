VectorGeometryToolVectorCustomScript
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Customized vector components defined with respect to reference axes.

.. py:currentmodule:: VectorGeometryToolVectorCustomScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript.script_file`
              - Specify a script file.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript.initialization_script_file`
              - Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorCustomScript


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript.reference_axes
    :type: VectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: script_file
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript.script_file
    :type: str

    Specify a script file.

.. py:property:: initialization_script_file
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorCustomScript.initialization_script_file
    :type: str

    Specify an initialization script file (optional). The initialization script is run once, at the beginning of the calculation.


