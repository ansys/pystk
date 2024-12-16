CalculationScalarType
=====================

.. py:class:: ansys.stk.core.vgt.CalculationScalarType

   IntEnum


.. py:currentmodule:: CalculationScalarType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported calculation scalar types.

            * - :py:attr:`~ANGLE`
              - Scalar equal to angular displacement obtained from any angle in VGT.

            * - :py:attr:`~FIXED_AT_TIME_INSTANT`
              - Constant scalar created by evaluating input scalar calculation at specified reference time instant.

            * - :py:attr:`~CONSTANT`
              - Constant scalar value of specified dimension.

            * - :py:attr:`~DATA_ELEMENT`
              - Any time-dependent data element from STK data providers available for parent STK object.

            * - :py:attr:`~DERIVATIVE`
              - Derivative of input scalar calculation.

            * - :py:attr:`~ELAPSED_TIME`
              - Time elapsed since reference time instant.

            * - :py:attr:`~FILE`
              - Tabulated scalar calculation data loaded from specified file.

            * - :py:attr:`~FUNCTION`
              - Defined by performing one of specified functions on input scalar.

            * - :py:attr:`~INTEGRAL`
              - Integral of input scalar computed with respect to time using one of specified numerical methods and using one of specified accumulation types.

            * - :py:attr:`~FUNCTION_OF_2_VARIABLES`
              - Defined by performing one of specified binary operations on two scalar arguments.

            * - :py:attr:`~VECTOR_MAGNITUDE`
              - Scalar equal to magnitude of specified vector.

            * - :py:attr:`~PLUGIN`
              - A calc scalar plugin based on a COM object.

            * - :py:attr:`~CUSTOM_SCRIPT`
              - A calc scalar uses scripted algorithm in MATLAB (.m or .dll), Perl or VBScript to define its value and rate.

            * - :py:attr:`~SURFACE_DISTANCE_BETWEEN_POINTS`
              - Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

            * - :py:attr:`~DOT_PRODUCT`
              - Scalar equal to the dot product between two vectors.

            * - :py:attr:`~VECTOR_COMPONENT`
              - Scalar equal to the specified component of a vector when resolved in the specified axes.

            * - :py:attr:`~AVERAGE`
              - Average of input scalar computed with respect to time using one of specified numerical methods and using one of specified accumulation types.

            * - :py:attr:`~STANDARD_DEVIATION`
              - Standard deviation of input scalar computed with respect to time using one of specified numerical methods and using one of specified accumulation types.

            * - :py:attr:`~CALCULATION_ALONG_TRAJECTORY`
              - Calculations Along Trajectory. Use IAgCrdnCalcScalarPointInVolumeCalc to access it.

            * - :py:attr:`~CUSTOM_INLINE_SCRIPT`
              - Custom inline script scalar.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import CalculationScalarType


