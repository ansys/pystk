IVectorGeometryToolVectorProjectAlongVector
===========================================

.. py:class:: IVectorGeometryToolVectorProjectAlongVector

   object
   
   A projection of a source vector in the direction of another vector.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~source_vector`
            * - :py:meth:`~along_vector`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorProjectAlongVector


Property detail
---------------

.. py:property:: source_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorProjectAlongVector.source_vector
    :type: "IAgCrdnVector"

    A source vector. Can be any VGT vector.

.. py:property:: along_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorProjectAlongVector.along_vector
    :type: "IAgCrdnVector"

    A vector along which the source vector is projected. Can be any VGT vector.


