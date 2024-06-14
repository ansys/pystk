IRefractionModelSCFMethod
=========================

.. py:class:: IRefractionModelSCFMethod

   IRefractionModelBase
   
   SCF Method.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~min_target_altitude`
            * - :py:meth:`~use_extrapolation`
            * - :py:meth:`~ceiling`
            * - :py:meth:`~atmos_altitude`
            * - :py:meth:`~knee_bend_factor`
            * - :py:meth:`~use_refraction_index`
            * - :py:meth:`~refraction_index`
            * - :py:meth:`~coefficients`


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
    :type: "IAgRfCoefficients"

    Gets the polynomial coefficients.


