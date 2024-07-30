RefractionModelSCFMethod
========================

.. py:class:: ansys.stk.core.stkobjects.RefractionModelSCFMethod

   Bases: 

   SCF Method.

.. py:currentmodule:: RefractionModelSCFMethod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.min_target_altitude`
              - Minimum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.use_extrapolation`
              - Flag controls whether extrapolation is used past the minimum target altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.ceiling`
              - Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.atmos_altitude`
              - Altitude of the atmosphere. Used to compute the knee bend point of the refracted path. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.knee_bend_factor`
              - Used to compute the distance to the knee bend point of the refracted path. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.use_refraction_index`
              - Flag controls whether a constant refraction index is used or the refraction polynomial fit.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.refraction_index`
              - Index of refraction at the surface. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelSCFMethod.coefficients`
              - Gets the polynomial coefficients.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RefractionModelSCFMethod


Property detail
---------------

.. py:property:: min_target_altitude
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.min_target_altitude
    :type: float

    Minimum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.

.. py:property:: use_extrapolation
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.use_extrapolation
    :type: bool

    Flag controls whether extrapolation is used past the minimum target altitude.

.. py:property:: ceiling
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.ceiling
    :type: float

    Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.atmos_altitude
    :type: float

    Altitude of the atmosphere. Used to compute the knee bend point of the refracted path. Uses Distance Dimension.

.. py:property:: knee_bend_factor
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.knee_bend_factor
    :type: float

    Used to compute the distance to the knee bend point of the refracted path. Dimensionless.

.. py:property:: use_refraction_index
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.use_refraction_index
    :type: bool

    Flag controls whether a constant refraction index is used or the refraction polynomial fit.

.. py:property:: refraction_index
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.refraction_index
    :type: float

    Index of refraction at the surface. Dimensionless.

.. py:property:: coefficients
    :canonical: ansys.stk.core.stkobjects.RefractionModelSCFMethod.coefficients
    :type: IRefractionCoefficients

    Gets the polynomial coefficients.


