VectorGeometryToolVectorDisplacement
====================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Vector defined by its start and end points.

.. py:currentmodule:: VectorGeometryToolVectorDisplacement

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.origin`
              - Specify the vector's origin point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.destination`
              - Specify the vector's destination point.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.apparent`
              - Controls whether to take a light speed delay into account.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.ignore_aberration`
              - Set to true if you do not want to calculate the aberration correction. This property is read-only if Apparent is set to false.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.signal_sense`
              - Specify a sense of signal transmission. This property is read-only if Apparent is set to false.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.reference_system`
              - Specify a frame in which the light time delay is computed. This property is read-only if Apparent is set to false.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorDisplacement


Property detail
---------------

.. py:property:: origin
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.origin
    :type: VectorGeometryToolPointRefTo

    Specify the vector's origin point.

.. py:property:: destination
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.destination
    :type: VectorGeometryToolPointRefTo

    Specify the vector's destination point.

.. py:property:: apparent
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.apparent
    :type: bool

    Controls whether to take a light speed delay into account.

.. py:property:: ignore_aberration
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.ignore_aberration
    :type: bool

    Set to true if you do not want to calculate the aberration correction. This property is read-only if Apparent is set to false.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.signal_sense
    :type: CRDN_SIGNAL_SENSE

    Specify a sense of signal transmission. This property is read-only if Apparent is set to false.

.. py:property:: reference_system
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorDisplacement.reference_system
    :type: VectorGeometryToolSystemRefTo

    Specify a frame in which the light time delay is computed. This property is read-only if Apparent is set to false.


