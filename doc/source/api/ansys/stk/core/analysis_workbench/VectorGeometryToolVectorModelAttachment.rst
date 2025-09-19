VectorGeometryToolVectorModelAttachment
=======================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorModelAttachment

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

.. py:currentmodule:: VectorGeometryToolVectorModelAttachment

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorModelAttachment.pointable_element_name`
              - Specify a pointable element of the 3D model associated with the object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorModelAttachment


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorModelAttachment.pointable_element_name
    :type: str

    Specify a pointable element of the 3D model associated with the object.


