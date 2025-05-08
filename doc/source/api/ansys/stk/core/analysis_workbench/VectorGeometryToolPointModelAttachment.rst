VectorGeometryToolPointModelAttachment
======================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointModelAttachment

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

.. py:currentmodule:: VectorGeometryToolPointModelAttachment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointModelAttachment.pointable_element_name`
              - Specify a model attachment point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointModelAttachment.use_scale`
              - Specify whether to use the model scale.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointModelAttachment


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointModelAttachment.pointable_element_name
    :type: str

    Specify a model attachment point.

.. py:property:: use_scale
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointModelAttachment.use_scale
    :type: bool

    Specify whether to use the model scale.


