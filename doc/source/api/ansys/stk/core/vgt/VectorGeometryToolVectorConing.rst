VectorGeometryToolVectorConing
==============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolVectorConing

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Vector created by revolving the Reference vector around the About vector with the specified rate.

.. py:currentmodule:: VectorGeometryToolVectorConing

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.about_vector`
              - Specify a vector around which the the reference vector is revolved.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.reference_vector`
              - Specify a reference vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.start_clock_angle`
              - Specify a start angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.stop_clock_angle`
              - Specify a stop angle.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.start_epoch`
              - Specify an epoch at which the coning vector is aligned with the reference vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.clock_angle_rate`
              - Specify a rotation rate.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolVectorConing.mode`
              - Specify either unidirectional or bidirectional mode.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolVectorConing


Property detail
---------------

.. py:property:: about_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.about_vector
    :type: VectorGeometryToolVectorReference

    Specify a vector around which the the reference vector is revolved.

.. py:property:: reference_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.reference_vector
    :type: VectorGeometryToolVectorReference

    Specify a reference vector.

.. py:property:: start_clock_angle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.start_clock_angle
    :type: float

    Specify a start angle.

.. py:property:: stop_clock_angle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.stop_clock_angle
    :type: float

    Specify a stop angle.

.. py:property:: start_epoch
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.start_epoch
    :type: typing.Any

    Specify an epoch at which the coning vector is aligned with the reference vector.

.. py:property:: clock_angle_rate
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.clock_angle_rate
    :type: float

    Specify a rotation rate.

.. py:property:: mode
    :canonical: ansys.stk.core.vgt.VectorGeometryToolVectorConing.mode
    :type: ROTATION_SWEEP_MODE_TYPE

    Specify either unidirectional or bidirectional mode.


