IVectorGeometryToolVectorScaled
===============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled

   object
   
   Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

.. py:currentmodule:: IVectorGeometryToolVectorScaled

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.reference_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.scale`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.is_normalized`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorScaled


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.reference_vector
    :type: IVectorGeometryToolVectorRefTo

    A vector being scaled.

.. py:property:: scale
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.scale
    :type: float

    A scaling multiple.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.is_normalized
    :type: bool

    Controls whether to convert the reference vector to a unit vector before scalling.


