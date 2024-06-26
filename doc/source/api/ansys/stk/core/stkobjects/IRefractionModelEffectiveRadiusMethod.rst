IRefractionModelEffectiveRadiusMethod
=====================================

.. py:class:: ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod

   IRefractionModelBase
   
   Effective Radius Method.

.. py:currentmodule:: IRefractionModelEffectiveRadiusMethod

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.eff_rad`
              - Effective radius used to compute refracted elevation. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.max_target_altitude`
              - Maximum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.use_extrapolation`
              - Flag controls whether extrapolation is used past the maximum target altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.ceiling`
              - Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IRefractionModelEffectiveRadiusMethod


Property detail
---------------

.. py:property:: eff_rad
    :canonical: ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.eff_rad
    :type: float

    Effective radius used to compute refracted elevation. Dimensionless.

.. py:property:: max_target_altitude
    :canonical: ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.max_target_altitude
    :type: float

    Maximum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.

.. py:property:: use_extrapolation
    :canonical: ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.use_extrapolation
    :type: bool

    Flag controls whether extrapolation is used past the maximum target altitude.

.. py:property:: ceiling
    :canonical: ansys.stk.core.stkobjects.IRefractionModelEffectiveRadiusMethod.ceiling
    :type: float

    Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.


