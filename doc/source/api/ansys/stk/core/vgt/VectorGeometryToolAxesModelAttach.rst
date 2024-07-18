VectorGeometryToolAxesModelAttach
=================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesModelAttach

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Axes aligned with the specified pointable element of the object's 3D model. The axes follow the model as well as any articulations that affect the specified pointable element.

.. py:currentmodule:: VectorGeometryToolAxesModelAttach

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesModelAttach.pointable_element_name`
              - Specify a pointable element of the 3D model associated with the object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesModelAttach


Property detail
---------------

.. py:property:: pointable_element_name
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesModelAttach.pointable_element_name
    :type: str

    Specify a pointable element of the 3D model associated with the object.


