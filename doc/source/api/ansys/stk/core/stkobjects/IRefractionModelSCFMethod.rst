IRefractionModelSCFMethod
=========================

.. py:class:: ansys.stk.core.stkobjects.IRefractionModelSCFMethod

   IRefractionModelBase
   
   SCF Method.

.. py:currentmodule:: IRefractionModelSCFMethod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.min_target_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.use_extrapolation`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.ceiling`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.atmos_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.knee_bend_factor`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.use_refraction_index`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.refraction_index`
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelSCFMethod.coefficients`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRefractionModelSCFMethod


Property detail
---------------

.. py:property:: min_target_altitude
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.min_target_altitude
    :type: float

    Minimum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.

.. py:property:: use_extrapolation
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.use_extrapolation
    :type: bool

    Flag controls whether extrapolation is used past the minimum target altitude.

.. py:property:: ceiling
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.ceiling
    :type: float

    Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.atmos_altitude
    :type: float

    Altitude of the atmosphere. Used to compute the knee bend point of the refracted path. Uses Distance Dimension.

.. py:property:: knee_bend_factor
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.knee_bend_factor
    :type: float

    Used to compute the distance to the knee bend point of the refracted path. Dimensionless.

.. py:property:: use_refraction_index
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.use_refraction_index
    :type: bool

    Flag controls whether a constant refraction index is used or the refraction polynomial fit.

.. py:property:: refraction_index
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.refraction_index
    :type: float

    Index of refraction at the surface. Dimensionless.

.. py:property:: coefficients
    :canonical: ansys.stk.core.stkobjects.IRefractionModelSCFMethod.coefficients
    :type: IRefractionCoefficients

    Gets the polynomial coefficients.


