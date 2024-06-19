IVectorGeometryToolVectorScaled
===============================

.. py:class:: IVectorGeometryToolVectorScaled

   object
   
   Scaled version of the input vector. Set IsNormalized to convert the input vector to a unit vector before scaling it.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_vector`
            * - :py:meth:`~scale`
            * - :py:meth:`~is_normalized`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorScaled


Property detail
---------------

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.reference_vector
    :type: IAgCrdnVectorRefTo

    A vector being scaled.

.. py:property:: scale
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.scale
    :type: float

    A scaling multiple.

.. py:property:: is_normalized
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorScaled.is_normalized
    :type: bool

    Controls whether to convert the reference vector to a unit vector before scalling.


