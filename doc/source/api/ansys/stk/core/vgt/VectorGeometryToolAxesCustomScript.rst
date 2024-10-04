VectorGeometryToolAxesCustomScript
==================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesCustomScript

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Customized axes offset with respect to a set of reference Axes.

.. py:currentmodule:: VectorGeometryToolAxesCustomScript

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesCustomScript.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesCustomScript.filename`
              - Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesCustomScript


Property detail
---------------

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesCustomScript.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesCustomScript.filename
    :type: str

    Can be MATLAB (.m or .dll) or VB Script (.vbs) script file.


