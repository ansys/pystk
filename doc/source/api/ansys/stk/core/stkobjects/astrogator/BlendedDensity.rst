BlendedDensity
==============

.. py:class:: ansys.stk.core.stkobjects.astrogator.BlendedDensity

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Blended atmospheric density propagator function.

.. py:currentmodule:: BlendedDensity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmosphere_density_model`
              - Embeds a nominal atmosphere model from the component browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model`
              - Embeds a low altitude atmosphere model from the component browser.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.density_blending_altitude_range`
              - Gets or sets the blending range (distance dimension), begins at lower bound of upper model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmosphere_density_model_name`
              - Returns the name of the embedded nominal atmospheric model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model_name`
              - Returns the name of the embedded low altitude atmospheric model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.use_approx_altitude`
              - True if using approximate altitude formula (enforced on embedded models).
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.lower_bound_upper_atmosphere_model`
              - Get the lowest valid altitude of the upper atmospheric density model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BlendedDensity


Property detail
---------------

.. py:property:: density_blending_altitude_range
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.density_blending_altitude_range
    :type: float

    Gets or sets the blending range (distance dimension), begins at lower bound of upper model.

.. py:property:: atmosphere_density_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmosphere_density_model_name
    :type: str

    Returns the name of the embedded nominal atmospheric model.

.. py:property:: low_altitude_atmosphere_density_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model_name
    :type: str

    Returns the name of the embedded low altitude atmospheric model.

.. py:property:: use_approx_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.use_approx_altitude
    :type: bool

    True if using approximate altitude formula (enforced on embedded models).

.. py:property:: lower_bound_upper_atmosphere_model
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.lower_bound_upper_atmosphere_model
    :type: float

    Get the lowest valid altitude of the upper atmospheric density model.


Method detail
-------------

.. py:method:: atmosphere_density_model(self, pInVal: IComponentInfo) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmosphere_density_model

    Embeds a nominal atmosphere model from the component browser.

    :Parameters:

    **pInVal** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~None`

.. py:method:: low_altitude_atmosphere_density_model(self, pInVal: IComponentInfo) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model

    Embeds a low altitude atmosphere model from the component browser.

    :Parameters:

    **pInVal** : :obj:`~IComponentInfo`

    :Returns:

        :obj:`~None`








