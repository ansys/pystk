IVectorGeometryToolAxesAlignedAndConstrained
============================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained

   object
   
   Axes aligned using two pairs of vectors. One vector in each pair is fixed in these axes and the other vector serves as an independent reference.

.. py:currentmodule:: IVectorGeometryToolAxesAlignedAndConstrained

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.alignment_direction`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.constraint_direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesAlignedAndConstrained


Property detail
---------------

.. py:property:: alignment_reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.alignment_reference_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify an alignment reference vector.

.. py:property:: constraint_reference_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.constraint_reference_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a constraint reference vector.

.. py:property:: alignment_direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.alignment_direction
    :type: IDirection

    Specify a desired alignment direction and the applicable parameters.

.. py:property:: constraint_direction
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesAlignedAndConstrained.constraint_direction
    :type: IDirection

    Specify a desired constraint direction and the applicable parameters.


