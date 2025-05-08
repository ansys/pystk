VectorGeometryToolAxesModelAttachment
=====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesModelAttachment

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

.. py:currentmodule:: VectorGeometryToolAxesModelAttachment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesModelAttachment.pointable_element_name`
              - Specify a pointable element of the 3D model associated with the object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesModelAttachment


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesModelAttachment.pointable_element_name
    :type: str

    Specify a pointable element of the 3D model associated with the object.


