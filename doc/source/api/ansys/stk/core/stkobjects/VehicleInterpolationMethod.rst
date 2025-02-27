VehicleInterpolationMethod
==========================

.. py:class:: ansys.stk.core.stkobjects.VehicleInterpolationMethod

   IntEnum


.. py:currentmodule:: VehicleInterpolationMethod

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported interpolation method.

            * - :py:attr:`~HERMITIAN`
              - Hermitian: uses the position and velocity ephemeris to interpolate position and velocity together.

            * - :py:attr:`~LAGRANGE`
              - Lagrange: interpolates position and velocity separately.

            * - :py:attr:`~VOP`
              - VOP: a special interpolator that deals well with ephemeris produced at a large step size.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleInterpolationMethod


