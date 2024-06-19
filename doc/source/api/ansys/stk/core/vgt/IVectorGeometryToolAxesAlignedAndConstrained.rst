IVectorGeometryToolAxesAlignedAndConstrained
============================================

.. py:class:: IVectorGeometryToolAxesAlignedAndConstrained

   object
   
   Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~alignment_reference_vector`
            * - :py:meth:`~constraint_reference_vector`
            * - :py:meth:`~alignment_direction`
            * - :py:meth:`~constraint_direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesAlignedAndConstrained


Property detail
---------------

.. py:property:: alignment_reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector
    :type: IAgCrdnVectorRefTo

    Specify an alignment reference vector.

.. py:property:: constraint_reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector
    :type: IAgCrdnVectorRefTo

    Specify a constraint reference vector.

.. py:property:: alignment_direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.alignment_direction
    :type: IAgDirection

    Specify a desired alignment direction and the applicable parameters.

.. py:property:: constraint_direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.constraint_direction
    :type: IAgDirection

    Specify a desired constraint direction and the applicable parameters.


