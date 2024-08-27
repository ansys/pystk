VectorGeometryToolVectorModelAttach
===================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorModelAttach

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

.. py:currentmodule:: VectorGeometryToolVectorModelAttach

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorModelAttach.pointable_element_name`
              - Specify a pointable element of the 3D model associated with the object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorModelAttach


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorModelAttach.pointable_element_name
    :type: str

    Specify a pointable element of the 3D model associated with the object.


