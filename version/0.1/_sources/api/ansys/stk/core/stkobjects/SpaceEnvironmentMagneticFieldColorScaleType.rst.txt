SpaceEnvironmentMagneticFieldColorScaleType
===========================================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentMagneticFieldColorScaleType

   IntEnum


.. py:currentmodule:: SpaceEnvironmentMagneticFieldColorScaleType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - An invalid SpaceEnvironmentMagneticFieldColorScaleType value.

            * - :py:attr:`~LINEAR`
              - Assign colors based upon a linear scaling from minimum to maximum value.

            * - :py:attr:`~LOG`
              - Assign colors based upon a linear scaling from log10(minimum) to log10(maximum) value. Ignores 0.0 values.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentMagneticFieldColorScaleType


