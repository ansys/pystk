VectorGeometryToolAngleBetweenVectors
=====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAngleBetweenVectors

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAngle`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   An angle between two vectors.

.. py:currentmodule:: VectorGeometryToolAngleBetweenVectors

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleBetweenVectors.from_vector`
              - Specify the first of the two vectors the angle is measured.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAngleBetweenVectors.to_vector`
              - Specify the second of the two vectors the angle is measured.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAngleBetweenVectors


Property detail
---------------

.. py:property:: from_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleBetweenVectors.from_vector
    :type: VectorGeometryToolVectorReference

    Specify the first of the two vectors the angle is measured.

.. py:property:: to_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAngleBetweenVectors.to_vector
    :type: VectorGeometryToolVectorReference

    Specify the second of the two vectors the angle is measured.


