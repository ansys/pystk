IVectorGeometryToolAxesSpinning
===============================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning

   object
   
   Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

.. py:currentmodule:: IVectorGeometryToolAxesSpinning

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.spin_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.reference_axes`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.epoch`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.initial_offset`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.spin_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesSpinning


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.spin_vector
    :type: IVectorGeometryToolVectorRefTo

    Specify a spin vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.reference_axes
    :type: IVectorGeometryToolAxesRefTo

    Specify a reference axes.

.. py:property:: epoch
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.epoch
    :type: typing.Any

    Specify an epoch at which the axes are aligned with the reference axes.

.. py:property:: initial_offset
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.initial_offset
    :type: float

    Specify an additional rotational offset.

.. py:property:: spin_rate
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.spin_rate
    :type: float

    Specify a spin rate the axes spins about the spin vector.


