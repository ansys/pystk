VectorGeometryToolVectorScaled
==============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorScaled

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

.. py:currentmodule:: VectorGeometryToolVectorScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScaled.reference_vector`
              - A vector being scaled.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScaled.scale`
              - A scaling multiple.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorScaled.is_normalized`
              - Controls whether to convert the reference vector to a unit vector before scalling.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorScaled


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScaled.reference_vector
    :type: VectorReference

    A vector being scaled.

.. py:property:: scale
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScaled.scale
    :type: float

    A scaling multiple.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorScaled.is_normalized
    :type: bool

    Controls whether to convert the reference vector to a unit vector before scalling.


