RefractionModelEffectiveRadiusMethod
====================================

.. py:class:: ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod

   Effective Radius Method.

.. py:currentmodule:: RefractionModelEffectiveRadiusMethod

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.effective_radius`
              - Effective radius used to compute refracted elevation. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.maximum_target_altitude`
              - Maximum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.use_extrapolation`
              - Flag controls whether extrapolation is used past the maximum target altitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.ceiling`
              - Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RefractionModelEffectiveRadiusMethod


Property detail
---------------

.. py:property:: effective_radius
    :canonical: ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.effective_radius
    :type: float

    Effective radius used to compute refracted elevation. Dimensionless.

.. py:property:: maximum_target_altitude
    :canonical: ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.maximum_target_altitude
    :type: float

    Maximum altitude of target for which the refraction will be computed unless extrapolation is used. Uses Distance Dimension.

.. py:property:: use_extrapolation
    :canonical: ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.use_extrapolation
    :type: bool

    Flag controls whether extrapolation is used past the maximum target altitude.

.. py:property:: ceiling
    :canonical: ansys.stk.core.stkobjects.RefractionModelEffectiveRadiusMethod.ceiling
    :type: float

    Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.


