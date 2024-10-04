VectorGeometryToolVectorModelAttachment
=======================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorModelAttachment

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

.. py:currentmodule:: VectorGeometryToolVectorModelAttachment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorModelAttachment.pointable_element_name`
              - Specify a pointable element of the 3D model associated with the object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorModelAttachment


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorModelAttachment.pointable_element_name
    :type: str

    Specify a pointable element of the 3D model associated with the object.


