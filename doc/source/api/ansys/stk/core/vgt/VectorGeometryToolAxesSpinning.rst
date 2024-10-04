VectorGeometryToolAxesSpinning
==============================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolAxesSpinning

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolAxes`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

.. py:currentmodule:: VectorGeometryToolAxesSpinning

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.spin_vector`
              - Specify a spin vector.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.reference_axes`
              - Specify a reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.epoch`
              - Specify an epoch at which the axes are aligned with the reference axes.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.initial_offset`
              - Specify an additional rotational offset.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.spin_rate`
              - Specify a spin rate the axes spins about the spin vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolAxesSpinning


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.spin_vector
    :type: VectorGeometryToolVectorReference

    Specify a spin vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.reference_axes
    :type: VectorGeometryToolAxesReference

    Specify a reference axes.

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.epoch
    :type: typing.Any

    Specify an epoch at which the axes are aligned with the reference axes.

.. py:property:: initial_offset
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.initial_offset
    :type: float

    Specify an additional rotational offset.

.. py:property:: spin_rate
    :canonical: ansys.stk.core.vgt.VectorGeometryToolAxesSpinning.spin_rate
    :type: float

    Specify a spin rate the axes spins about the spin vector.


