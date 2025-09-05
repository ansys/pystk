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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmos_density_model`
              - Embeds a nominal atmosphere model from the component browser.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model`
              - Embeds a low altitude atmosphere model from the component browser.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmos_density_model_name`
              - Return the name of the embedded nominal atmospheric model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.density_blending_altitude_range`
              - Get or set the blending range (distance dimension), begins at lower bound of upper model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model_name`
              - Return the name of the embedded low altitude atmospheric model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.lower_bound_upper_atmosphere_model`
              - Get the lowest valid altitude of the upper atmospheric density model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BlendedDensity.use_approx_altitude`
              - True if using approximate altitude formula (enforced on embedded models).



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BlendedDensity


Property detail
---------------

.. py:property:: atmos_density_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmos_density_model_name
    :type: str

    Return the name of the embedded nominal atmospheric model.

.. py:property:: density_blending_altitude_range
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.density_blending_altitude_range
    :type: float

    Get or set the blending range (distance dimension), begins at lower bound of upper model.

.. py:property:: low_altitude_atmosphere_density_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model_name
    :type: str

    Return the name of the embedded low altitude atmospheric model.

.. py:property:: lower_bound_upper_atmosphere_model
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.lower_bound_upper_atmosphere_model
    :type: float

    Get the lowest valid altitude of the upper atmospheric density model.

.. py:property:: use_approx_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.use_approx_altitude
    :type: bool

    True if using approximate altitude formula (enforced on embedded models).


Method detail
-------------

.. py:method:: atmos_density_model(self, value: IComponentInfo) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.atmos_density_model

    Embeds a nominal atmosphere model from the component browser.

    :Parameters:

        **value** : :obj:`~IComponentInfo`


    :Returns:

        :obj:`~None`




.. py:method:: low_altitude_atmosphere_density_model(self, value: IComponentInfo) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.BlendedDensity.low_altitude_atmosphere_density_model

    Embeds a low altitude atmosphere model from the component browser.

    :Parameters:

        **value** : :obj:`~IComponentInfo`


    :Returns:

        :obj:`~None`





