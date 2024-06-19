IVectorGeometryToolAxesSpinning
===============================

.. py:class:: IVectorGeometryToolAxesSpinning

   object
   
   Axes created by spinning the Reference axes about the Spin vector with the specified rate. The axes are aligned with the Reference axes at the specified epoch plus the additional rotational offset.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~spin_vector`
            * - :py:meth:`~reference_axes`
            * - :py:meth:`~epoch`
            * - :py:meth:`~initial_offset`
            * - :py:meth:`~spin_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesSpinning


Property detail
---------------

.. py:property:: spin_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.spin_vector
    :type: IAgCrdnVectorRefTo

    Specify a spin vector.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesSpinning.reference_axes
    :type: IAgCrdnAxesRefTo

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


